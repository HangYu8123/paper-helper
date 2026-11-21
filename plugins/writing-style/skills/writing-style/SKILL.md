---
name: writing-style
description: Hang Yu's writing style reference (72 patterns with weighted evidence from Hang's instructions, hand edits, and 16 review records) and the committee writing style reference (patterns, quotations, and measures from the three committee dissertations), about 2.5 MB in all, entered through a short quick reference and searched by heading. Use when choosing the wording of a draft, a revision, or a peer review, and also for a disputed wording, a sentence that may have been reviewed before, the evidence or strength behind a preference, committee-facing or thesis-chapter conventions, or importing a finished review's decisions into the reference. Uses the writing-vocabulary skill for technical terms when it is installed, and works without it.
---

# Writing style

Two references to Hang Yu's writing style. The polish-paper and review-paper skills use this skill for the wording of every proposal and review.

In Claude Code, this skill's folder is `${CLAUDE_SKILL_DIR}`. Resolve the paths below from it.

| Folder | What it is | Start with |
| --- | --- | --- |
| [writing_style_ref](writing_style_ref/README.md) | Hang's writing style reference: 72 patterns, every instruction, hand edit, and review decision from Hang with its weight, the records of 16 reviews, and the build tools (about 2 MB) | [hangs-writing-style-reference.md](writing_style_ref/hangs-writing-style-reference.md) |
| [committee_style_ref](committee_style_ref/README.md) | The committee writing style reference: 63 patterns from three dissertations Hang named, with 282 quotations and per-writer measures (about 0.8 MB) | [committee-writing-style-reference.md](committee_style_ref/committee-writing-style-reference.md) |

## How to read it

Before wording a draft, a revision, or a review, read the opening of [Hang's reference](writing_style_ref/hangs-writing-style-reference.md), through its Quick reference and Find a pattern. Then look up the patterns for the kind of sentence at hand by heading or pattern name, such as `Qualifying a result`, `Few colons and semicolons`, or `Correcting a sentence without rewording it`. Read only the entries needed. Do not load a whole library, evidence file, or source text.

| Question | Read |
| --- | --- |
| The wording of an ordinary draft, revision, or review | The opening and Quick reference of [Hang's reference](writing_style_ref/hangs-writing-style-reference.md), then the entries under Wording preference, Writing style, Sentence style, and Sentence structure that fit the sentence |
| Editing someone else's text | "Correcting a sentence without rewording it" and "Adding sentences that were not asked for" in [Hang's reference](writing_style_ref/hangs-writing-style-reference.md) |
| Technical word choice | The `writing-vocabulary` skill, if it is installed (see "Vocabulary" below). Without it, the [Vocabulary patterns](writing_style_ref/hangs-writing-style-reference.md#vocabulary) of Hang's reference and the document's own definitions |
| A preference needs explanation or appears to conflict with the Quick reference | The relevant entry in [Hang's reference](writing_style_ref/hangs-writing-style-reference.md), then its linked evidence |
| A sentence was reviewed before, or the author disputes a wording | [Review index](writing_style_ref/review-decisions.md) and the relevant record in `writing_style_ref/reviews/` |
| How strong a preference is, or where it came from | [Preference signals](writing_style_ref/preference-signals.md) and the [source map](writing_style_ref/source-map.md) |
| Committee-facing clarity, study reporting, a thesis chapter, or the structure of a long document | The relevant entry in [the committee reference](committee_style_ref/committee-writing-style-reference.md) |
| Evidence of a writing pattern | [Hang's paper excerpts](writing_style_ref/source-evidence.md) or [committee excerpts](committee_style_ref/source-evidence.md); [writer profiles](committee_style_ref/writer-profiles.md) for approximate measures |

Hang's current instructions and the facts of the passage come first. Among style sources, direct evidence of Hang's choices takes priority over paper examples, then committee examples. Do not turn a past choice about one passage into a universal substitution. The committee quotations show how those writers wrote, with their first person and punctuation; they are not text to copy.

Hang's reference was built from Hang's dissertation, talk, film, and papers. Its chapter, slide, and film patterns govern those genres only. Dissertation structure and the dissertation's impersonal voice do not set the style of a conference paper or a peer review, and a student's paper keeps the student's voice and terms.

## Vocabulary

The `writing-vocabulary` skill is optional. Look for it as described under "Companion skills" below.

- If it is installed, read its `vocabulary.md` before choosing technical terms, and use its `vocabulary_ref/tech-vocabulary.md` for a term's examples and sources. To check a draft's vocabulary, use that skill's checker.
- If it is not installed, proceed without it. Use the Vocabulary patterns of Hang's reference and the document's own definitions for word choice. Do not stop or ask the user to install it, and mention its absence only when a term's familiarity matters to a decision.

## Companion skills

This skill needs no other skill. Find `writing-vocabulary` by its name, in this order: next to this skill (`../writing-vocabulary/` in a standalone install, `../../../writing-vocabulary/skills/writing-vocabulary/` in the repository), then the folder of the `writing-vocabulary` skill that the app lists (in Claude Code, invoke the skill and its SKILL.md names its folder; in Codex, the list of skills gives the path to its SKILL.md). If neither finds it, the skill is not installed.

## Tools

The two READMEs give the full build steps. The commands below run from this skill's folder.

- Bring a finished review into the reference: `python writing_style_ref/tools/import_review.py <review folder>`, then cite its decisions in `writing_style_ref/tools/authored_entries.py` and rebuild with `build_reference.py` and `validate_reference.py`. This changes the reference, so ask before running it. An installed copy is replaced on the next install or plugin update, so run it on the repository's copy (`plugins/writing-style/skills/writing-style/`) and reinstall.

The READMEs, validation reports, and build scripts refer to Hang's dissertation folder, the original PDFs, and paper sources that are not bundled here. Those paths are provenance, not required inputs. Do not claim to have opened a PDF that is absent, and do not run the rebuild, extraction, or validation scripts as part of an ordinary review. The validation scripts rewrite `validation.md` and need the unbundled sources, so without them they report broken links or stop on a missing file.
