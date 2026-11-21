---
name: writing-style
description: Hang Yu's full writing style reference (72 patterns with weighted evidence from Hang's instructions, hand edits, and 16 review records) and the committee writing style reference (patterns, quotations, and measures from the three committee dissertations), about 2.5 MB in all. Use only when the writing-style-portable guide is not enough, such as a disputed wording, a sentence that may have been reviewed before, the evidence or strength behind a preference, committee-facing or thesis-chapter conventions, or importing a finished review's decisions into the reference. Technical vocabulary is in the separate writing-vocabulary skill.
---

# Full writing style references

Two large source libraries behind the portable writing style guide, which is the `writing-style-portable` skill. The portable guide covers ordinary writing and reviews; open these only when it is not enough. Search them by heading or pattern name and read only the entries needed. Do not load a whole library, evidence file, or source text.

In Claude Code, this skill's folder is `${CLAUDE_SKILL_DIR}`. Resolve the paths below from it.

| Folder | What it is | Start with |
| --- | --- | --- |
| [writing_style_ref](writing_style_ref/README.md) | Hang's writing style reference: 72 patterns, every instruction, hand edit, and review decision from Hang with its weight, the records of 16 reviews, and the build tools (about 2 MB) | [hangs-writing-style-reference.md](writing_style_ref/hangs-writing-style-reference.md) |
| [committee_style_ref](committee_style_ref/README.md) | The committee writing style reference: 63 patterns from three dissertations Hang named, with 282 quotations and per-writer measures (about 0.8 MB) | [committee-writing-style-reference.md](committee_style_ref/committee-writing-style-reference.md) |

## Which file answers which question

| Question | Read |
| --- | --- |
| A preference needs explanation or appears to conflict with the portable guide | The relevant entry in [Hang's full reference](writing_style_ref/hangs-writing-style-reference.md), then its linked evidence |
| A sentence was reviewed before, or the author disputes a wording | [Review index](writing_style_ref/review-decisions.md) and the relevant record in `writing_style_ref/reviews/` |
| How strong a preference is, or where it came from | [Preference signals](writing_style_ref/preference-signals.md) and the [source map](writing_style_ref/source-map.md) |
| Committee-facing clarity, study reporting, or a thesis chapter | The relevant entry in [the committee reference](committee_style_ref/committee-writing-style-reference.md) |
| Evidence of a writing pattern | [Hang's paper excerpts](writing_style_ref/source-evidence.md) or [committee excerpts](committee_style_ref/source-evidence.md); [writer profiles](committee_style_ref/writer-profiles.md) for approximate measures |
| Technical word choice, with examples and sources | The `writing-vocabulary` skill, if it is installed: its `vocabulary_ref/tech-vocabulary.md` and `vocabulary_ref/word-list.md`. Without it, the Vocabulary patterns of [Hang's full reference](writing_style_ref/hangs-writing-style-reference.md#vocabulary) cover word choices made in review |

Hang's current instructions and the facts of the passage come first. Among style sources, direct evidence of Hang's choices takes priority over the portable summary, then committee examples. Do not turn a past choice about one passage into a universal substitution. The committee quotations show how those writers wrote, with their first person and punctuation; they are not text to copy, and dissertation structure does not set the style of a conference paper or a peer review.

## Companion skills

This skill works alone. The portable guide (`writing-style-portable`) is its summary, and the technical vocabulary (`writing-vocabulary`) is separate. Find either by its name, in this order: next to this skill (`../<name>/` in a standalone install, `../../../<name>/skills/<name>/` in the repository), then the folder of the `<name>` skill that the app lists (in Claude Code, invoke the skill and its SKILL.md names its folder; in Codex, the list of skills gives the path to its SKILL.md). If neither finds it, the skill is not installed.

## Tools

The two READMEs give the full build steps. The commands below run from this skill's folder. To check a draft's vocabulary, use the `writing-vocabulary` skill.

- Bring a finished review into the reference: `python writing_style_ref/tools/import_review.py <review folder>`, then cite its decisions in `writing_style_ref/tools/authored_entries.py` and rebuild with `build_reference.py` and `validate_reference.py`. This changes the reference, so ask before running it. An installed copy is replaced on the next install or plugin update, so run it on the repository's copy (`plugins/writing-style/skills/writing-style/`) and reinstall.

The READMEs, validation reports, and build scripts refer to Hang's dissertation folder, the original PDFs, and paper sources that are not bundled here. Those paths are provenance, not required inputs. Do not claim to have opened a PDF that is absent, and do not run the rebuild, extraction, or validation scripts as part of an ordinary review. The validation scripts rewrite `validation.md` and need the unbundled sources, so without them they report broken links or stop on a missing file.
