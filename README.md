# paper-helper

Paper Helper is a collection of skills for Claude Code and Codex. Use it to revise a research draft, write a peer review with evidence from the manuscript, or find papers for a related-work check.

| Skill | What it does | Required skills |
| --- | --- | --- |
| [polish-paper](plugins/polish-paper/skills/polish-paper/SKILL.md) | Reviews a draft using an advisor's writing guide. Proposes edits with reasons and gives the author a page to accept, edit, or reject each suggestion before applying it. | `writing-style`, `html-templates`, `review-paper` |
| [review-paper](plugins/review-paper/skills/review-paper/SKILL.md) | Drafts a peer review and shows the evidence under each point. It can also propose wording changes when asked. | `writing-style`, `html-templates` |
| [find-sota-papers](plugins/find-sota-papers/skills/find-sota-papers/SKILL.md) | Finds papers for a research question and verifies the paper details on source pages. The review skills can call it for a short related-work, novelty, baseline, or citation check. | None |
| [writing-style](plugins/writing-style/skills/writing-style/SKILL.md) | Guides the wording of drafts, revisions, and reviews with Hang Yu's writing patterns, the evidence and prior decisions behind them, and examples from committee dissertations. Uses `writing-vocabulary` when it is installed. | None |
| [writing-vocabulary](plugins/writing-vocabulary/skills/writing-vocabulary/SKILL.md) | Records how Hang uses terms in robot learning and human-robot interaction. Includes a technical vocabulary with examples and a checker that groups draft words by familiarity. | None |
| [html-templates](plugins/html-templates/skills/html-templates/SKILL.md) | Provides the editing page and the peer-review page. | None |

## Install in Claude Code

```sh
claude plugin marketplace add HangYu8123/paper-helper
claude plugin install review-paper@paper-helper
```

Claude Code also installs the required skills listed in the table. Add any other skill the same way, such as `claude plugin install writing-vocabulary@paper-helper`. Installing `polish-paper`, `find-sota-papers`, and `writing-vocabulary` brings all six skills. Invoke the review skill as `/review-paper:review-paper`.

## Install in Codex

These commands install the peer-review skill and its two required plugins.

```sh
codex plugin marketplace add HangYu8123/paper-helper
codex plugin add writing-style@paper-helper
codex plugin add html-templates@paper-helper
codex plugin add review-paper@paper-helper
```

Add any other skill with `codex plugin add <skill>@paper-helper`. Use `$review-paper` in a prompt to request a review.

If you used the `review-your-papers` marketplace, remove that entry by name before adding `paper-helper`. Update the new marketplace with `claude plugin marketplace update paper-helper` or `codex plugin marketplace upgrade paper-helper`.

## Install as standalone skills

Clone this repository and run the installer from its root with Python 3.8 or newer. Choose one installation method so each skill appears once.

```sh
git clone https://github.com/HangYu8123/paper-helper.git
cd paper-helper
python install.py
```

`python install.py` installs all six skills for both apps. Pass `--app claude` or `--app codex` to choose one app. Use `--skill review-paper` to install one skill and its required skills, or `--list` to see all dependencies. The standalone commands are `/review-paper` in Claude Code and `$review-paper` in Codex. Restart the app to load the skills.

## Use the writing references

Start with the [Quick reference](plugins/writing-style/skills/writing-style/writing_style_ref/hangs-writing-style-reference.md#quick-reference) of Hang's writing style reference, then look up patterns by heading. When `writing-vocabulary` is installed, the `writing-style` skill consults it for technical terms and acronyms; without it, the skill uses the Vocabulary patterns of its own reference. Use the vocabulary's familiarity marks to decide whether a term needs a definition for your readers. The [vocabulary checker](plugins/writing-vocabulary/skills/writing-vocabulary/vocabulary_ref/README.md) can flag unfamiliar terms for a closer look.

Open the review records and the committee reference in `writing-style` when a wording choice is disputed, a sentence may have been reviewed before, or a thesis chapter needs committee-facing examples. Keep the source facts and definitions while revising the wording.

## Run a paper search

Ask `find-sota-papers` directly to choose a topic, date range, search depth, and number of papers. Each paper comes with a link and the sources checked for it. The review skills can run a shorter search when the question is about related work, novelty, baselines, or a citation. Both modes need live web search and page access.

Optional OpenAlex and Semantic Scholar keys can raise rate limits for the bulk search scripts. To set them locally, run `python install.py --configure-keys`.

## Tool requirements

- The standalone installer, vocabulary checker, editing tools, and search scripts run on Python 3.8 or newer.
- The `polish-paper` scripts need Python 3.10 or newer. Figure rendering uses Poppler. The `review-paper` PDF text helper uses Poppler or `pypdf`.
- The review-data checker needs Node.js.

Keep manuscript files, review decisions, and generated reports with each paper.
