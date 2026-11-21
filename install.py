#!/usr/bin/env python3
"""Install the skills on their own, without the plugin system.

    python install.py                          every skill, for both apps
    python install.py --app claude             Claude Code only (~/.claude/skills)
    python install.py --app codex              Codex only ($CODEX_HOME/skills, by default ~/.codex/skills)
    python install.py --dest <skills folder>   any skills folder, such as <project>/.claude/skills
    python install.py --skill review-paper     one skill, with the skills it needs (repeatable)
    python install.py --list                   each skill, the skills it needs, and the ones it can use
    python install.py --uninstall              remove what this script installed
    python install.py --dry-run                show what would happen
    python install.py --package dist           write dist/paper-helper-skills.zip to unpack into a skills folder
    python install.py --configure-keys         store API keys for find-sota-papers' bulk-search scripts

To install the skills as plugins from the marketplace instead, see README.md. Use one way or
the other, since both together list each skill twice.

Each skill is its own plugin in the repository, in plugins/<skill>/skills/<skill>/. This script
copies the chosen skills into a skills folder side by side, where each finds the others at
../<skill>/. A skill brings the skills it needs, which are the dependencies in its
plugins/<skill>/.claude-plugin/plugin.json. The skills it can use but does not need, such as the
vocabulary, are installed only when named or when installing everything. An installed folder is
replaced only if this script installed it, which it records in a marker file. Runs on Python 3.8
or newer.
"""
import argparse
import datetime
import json
import os
import shutil
import stat
import subprocess
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent
PLUGINS = REPO / "plugins"
SKILLS = ["polish-paper", "review-paper", "find-sota-papers", "writing-style", "writing-vocabulary",
          "html-templates"]
REVIEW_SKILLS = ["polish-paper", "review-paper"]  # each carries its own copy of review-tools/
# The skills each one can use when they are installed, without needing them. What a skill needs is read from
# the dependencies in its plugin.json (see needs()).
CAN_USE = {
    "polish-paper": ["find-sota-papers", "writing-vocabulary"],
    "review-paper": ["find-sota-papers", "writing-vocabulary"],
    "writing-style": ["writing-vocabulary"],
    "writing-vocabulary": ["writing-style"],
}
# Folders of earlier versions, each removed when every skill that replaced it is installed or uninstalled.
LEGACY = {
    "paper-review-shared": set(REVIEW_SKILLS),  # the old shared folder, now split into the skills they use
    "advisor-review-paper": {"polish-paper"},  # the old name of polish-paper
    "writing-style-portable": {"writing-style"},  # the compact guide, removed; writing-style took its place
}
MARKER = ".installed-by-paper-helper.json"
# Marker names written by earlier versions of this script, before the repository was renamed to paper-helper.
# A folder carrying one of them was installed by this script too, so it can be replaced or uninstalled.
OLD_MARKERS = [".installed-by-review-your-papers.json"]
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", MARKER, *OLD_MARKERS)
IGNORED_NAMES = {"__pycache__", ".DS_Store", MARKER, *OLD_MARKERS}
# API keys for find-sota-papers' scripts (scripts/arxiv_sweep.py, scripts/resolve_ids.py), which read this file.
KEYS_PATH = Path(os.environ.get("FIND_SOTA_PAPERS_CONFIG")
                 or Path.home() / ".config" / "find-sota-papers" / "config.json")
KEYS = {
    "openalex_api_key": "OpenAlex API key (free at openalex.org; anonymous use allows about ten searches a day)",
    "s2_api_key": "Semantic Scholar API key (free at semanticscholar.org/product/api; anonymous use is throttled)",
    "mailto": "Contact email for the Crossref and OpenAlex polite pools",
}


def claude_skills_dir():
    base = os.environ.get("CLAUDE_CONFIG_DIR")
    return (Path(base) if base else Path.home() / ".claude") / "skills"


def codex_skills_dir():
    base = os.environ.get("CODEX_HOME")
    return (Path(base) if base else Path.home() / ".codex") / "skills"


def is_link(path):
    """True for a symbolic link, or a junction or other reparse point on Windows."""
    if os.path.islink(str(path)):
        return True
    if os.name == "nt":
        try:
            st = os.lstat(str(path))
        except OSError:
            return False
        return bool(getattr(st, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT)
    return False


def git_commit():
    try:
        out = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"],
                             stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=True)
        return out.stdout.decode().strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def skill_src(name):
    """The skill's folder in the repository, where each skill is its own plugin."""
    return PLUGINS / name / "skills" / name


def needs(name):
    """The skills that a skill needs: the dependencies of its plugin."""
    manifest = PLUGINS / name / ".claude-plugin" / "plugin.json"
    return json.loads(manifest.read_text(encoding="utf-8")).get("dependencies", [])


def check_sources(names):
    for name in names:
        src = skill_src(name)
        if not src.is_dir():
            raise SystemExit("Missing source folder: %s" % src)
        if not (src / "SKILL.md").is_file():
            raise SystemExit("Missing %s" % (src / "SKILL.md"))


def files_of(folder):
    return {p.relative_to(folder).as_posix(): p.read_bytes() for p in folder.rglob("*") if p.is_file()}


def check_review_tools():
    """Each review skill carries its own copy of review-tools/. Warn if the copies differ."""
    copies = [skill_src(s) / "review-tools" for s in REVIEW_SKILLS]
    first = files_of(copies[0])
    for other in copies[1:]:
        if files_of(other) != first:
            print("Warning: %s differs from %s. Keep the copies of review-tools the same."
                  % (other.relative_to(REPO), copies[0].relative_to(REPO)))


def with_needed(chosen):
    """The chosen skills and every skill they need, in SKILLS order. polish-paper needs review-paper,
    since its technical audit uses review-paper's claim checks and statistics helper."""
    chosen = set(chosen)
    todo = list(chosen)
    while todo:
        for dep in needs(todo.pop()):
            if dep not in chosen:
                chosen.add(dep)
                todo.append(dep)
    return [n for n in SKILLS if n in chosen]


def print_list():
    for name in SKILLS:
        print(name)
        print("  needs:   %s" % (", ".join(needs(name)) or "nothing"))
        print("  can use: %s" % (", ".join(CAN_USE.get(name, [])) or "nothing"))


def owned(dest):
    return any((dest / name).is_file() for name in [MARKER] + OLD_MARKERS)


def refuse_reason(dest, force):
    if is_link(dest):
        return "it is a link or junction; remove it yourself first"
    if dest.exists() and not dest.is_dir():
        return "it is a file"
    if dest.exists() and not owned(dest) and not force:
        return "it was not installed by this script (use --force to replace it)"
    return ""


def install_one(src, dest, dry_run, force, commit):
    reason = refuse_reason(dest, force)
    if reason:
        print("  skipped %s: %s" % (dest, reason))
        return False
    action = "replace" if dest.exists() else "install"
    print("  %s %s" % (action, dest))
    if dry_run:
        return True
    tmp = dest.parent / (".%s.tmp-%d" % (dest.name, os.getpid()))
    if tmp.exists():
        shutil.rmtree(str(tmp))
    shutil.copytree(str(src), str(tmp), ignore=IGNORE)
    marker = {
        "source": str(REPO),
        "commit": commit,
        "installed_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    (tmp / MARKER).write_text(json.dumps(marker, indent=1) + "\n", encoding="utf-8")
    if dest.exists():
        shutil.rmtree(str(dest))
    os.rename(str(tmp), str(dest))
    return True


def uninstall_one(dest, dry_run):
    if not dest.exists() and not is_link(dest):
        return
    if is_link(dest) or not owned(dest):
        print("  left %s: it was not installed by this script" % dest)
        return
    print("  remove %s" % dest)
    if not dry_run:
        shutil.rmtree(str(dest))


def package(out_dir, names):
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "paper-helper-skills.zip"
    count = 0
    with zipfile.ZipFile(str(out), "w", zipfile.ZIP_DEFLATED) as zf:
        for name in names:
            src = skill_src(name)
            for root, dirs, files in os.walk(str(src)):
                dirs[:] = sorted(d for d in dirs if d not in IGNORED_NAMES)
                for f in sorted(files):
                    if f in IGNORED_NAMES or f.endswith(".pyc"):
                        continue
                    path = Path(root) / f
                    zf.write(str(path), (Path(name) / path.relative_to(src)).as_posix())
                    count += 1
    print("Wrote %s (%d files, %.1f MB)" % (out, count, out.stat().st_size / 1e6))
    print("Unpack it into a skills folder so the skill folders sit side by side.")


def configure_keys(assignments):
    """Write the API keys that find-sota-papers' scripts read. Environment variables (S2_API_KEY,
    OPENALEX_API_KEY, SOTA_MAILTO) override the file. The keys are optional: the skill itself works
    without them, and the scripts only search faster and more reliably with them."""
    config = {}
    if KEYS_PATH.is_file():
        try:
            loaded = json.loads(KEYS_PATH.read_text(encoding="utf-8"))
        except ValueError as exc:
            raise SystemExit("Cannot read %s: %s" % (KEYS_PATH, exc))
        if isinstance(loaded, dict):
            config = loaded
    if assignments:
        for item in assignments:
            key, sep, value = item.partition("=")
            if not sep or key not in KEYS:
                raise SystemExit("--set expects KEY=VALUE with KEY one of: %s" % ", ".join(sorted(KEYS)))
            if value:
                config[key] = value
            else:
                config.pop(key, None)
    else:
        if not sys.stdin.isatty():
            raise SystemExit("No terminal to ask on. Pass --set KEY=VALUE (keys: %s)." % ", ".join(sorted(KEYS)))
        print("API keys for find-sota-papers' scripts. Press Enter to keep a value, or type - to clear it.")
        for key, label in KEYS.items():
            current = config.get(key)
            shown = ("set" if key.endswith("_key") else current) if current else "not set"
            entered = input("  %s [%s]: " % (label, shown)).strip()
            if entered == "-":
                config.pop(key, None)
            elif entered:
                config[key] = entered
    KEYS_PATH.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(str(KEYS_PATH), os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as handle:
        json.dump(config, handle, indent=2)
        handle.write("\n")
    print("Wrote %s (%s)" % (KEYS_PATH, ", ".join(sorted(config)) or "empty"))


def main():
    ap = argparse.ArgumentParser(description="Install the skills for Claude Code and Codex.")
    ap.add_argument("--app", choices=["claude", "codex", "both"], default="both",
                    help="which app's personal skills folder to install into (default: both)")
    ap.add_argument("--dest", action="append", default=[],
                    help="install into this skills folder instead (repeatable)")
    ap.add_argument("--skill", action="append", choices=SKILLS, default=[],
                    help="install only this skill, with the skills it needs (repeatable; default: all)")
    ap.add_argument("--list", action="store_true", help="list the skills, what each needs, and what each can use")
    ap.add_argument("--uninstall", action="store_true", help="remove the installed folders")
    ap.add_argument("--force", action="store_true",
                    help="replace a folder of the same name that this script did not install")
    ap.add_argument("--dry-run", action="store_true", help="show what would happen without changing anything")
    ap.add_argument("--package", metavar="DIR", help="write a zip of the skills to DIR")
    ap.add_argument("--configure-keys", action="store_true",
                    help="store API keys for find-sota-papers' scripts in %s" % KEYS_PATH)
    ap.add_argument("--set", action="append", default=[], metavar="KEY=VALUE", dest="assignments",
                    help="with --configure-keys: set one key without prompting (repeatable)")
    args = ap.parse_args()

    if args.configure_keys:
        configure_keys(args.assignments)
        return 0
    if args.assignments:
        raise SystemExit("--set only works with --configure-keys")

    if args.list:
        print_list()
        return 0

    # Installing a skill brings the skills it needs. Uninstalling removes only what is named.
    if args.uninstall and args.skill:
        names = [n for n in SKILLS if n in args.skill]
    else:
        names = with_needed(args.skill or SKILLS)
    # An old folder is removed only together with the skills that replaced it.
    legacy = [old for old, successors in LEGACY.items() if successors <= set(names)]
    check_sources(names)
    check_review_tools()

    if args.package:
        package(Path(args.package).resolve(), names)
        return 0

    if args.dest:
        targets = [Path(d).expanduser().resolve() for d in args.dest]
    else:
        targets = []
        if args.app in ("claude", "both"):
            targets.append(claude_skills_dir())
        if args.app in ("codex", "both"):
            targets.append(codex_skills_dir())

    commit = git_commit()
    failed = False
    for skills_dir in targets:
        print("%s%s:" % (skills_dir, " (dry run)" if args.dry_run else ""))
        if args.uninstall:
            for name in names + legacy:
                uninstall_one(skills_dir / name, args.dry_run)
            continue
        if not args.dry_run:
            skills_dir.mkdir(parents=True, exist_ok=True)
        for name in names:
            if not install_one(skill_src(name), skills_dir / name, args.dry_run, args.force, commit):
                failed = True
        for name in legacy:
            if owned(skills_dir / name) and not is_link(skills_dir / name):
                uninstall_one(skills_dir / name, args.dry_run)

    if not args.uninstall and not failed:
        print("")
        print("Installed as standalone skills.")
        print("Claude Code: %s" % ", ".join("/" + n for n in names))
        print("Codex:       %s" % ", ".join("$" + n for n in names))
        optional = sorted({o for n in names for o in CAN_USE.get(n, []) if o not in names})
        if optional:
            print("Not installed, and used when present: %s. Add each with --skill <name>."
                  % ", ".join(optional))
        print("Restart the app if it is running, so it finds the new skills.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
