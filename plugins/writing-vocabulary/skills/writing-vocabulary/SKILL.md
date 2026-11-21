---
name: writing-vocabulary
description: Hang Yu's vocabulary for writing about robot learning and human-robot interaction, kept apart from the writing style guides so that each can be installed alone. A compact vocabulary (about 47 KB) of terms with fixed meanings, terms marked by how familiar they are to the author, the vocabulary of field dissertations, words the author uses more than field writers, and acronyms, plus the full technical vocabulary (1,100 terms with counts, examples, and sources from the author's papers and 15 field dissertations), every word family in the papers, and a checker that sorts a draft's words by familiarity. Use when choosing or checking technical terms in Hang's writing, deciding whether a term needs a definition, expanding an acronym, or checking a draft's vocabulary. The writing-style skill reads it first when both are installed, and works without it.
---

# Writing vocabulary

The words and terms of Hang Yu's research writing in robot learning and human-robot interaction, with an estimate of how familiar each one is to Hang. It says which words to use. How to use them is the subject of the `writing-style` skill, which reads this vocabulary first when both are installed. This skill needs no other skill.

In Claude Code, this skill's folder is `${CLAUDE_SKILL_DIR}`. Resolve the paths below from it.

| File | Use |
| --- | --- |
| [vocabulary.md](vocabulary.md) | Start here. Terms with fixed meanings, the author's technical and research-writing vocabulary by familiarity, the vocabulary of five field dissertations and of twelve recent lab dissertations, the words the author uses more than field writers, and acronyms |
| [vocabulary_ref/tech-vocabulary.md](vocabulary_ref/tech-vocabulary.md) | The full technical vocabulary, with each term's counts, an example, and its source (about 390 KB, so search it by term or heading) |
| [vocabulary_ref/word-list.md](vocabulary_ref/word-list.md) | Every word family the papers use, by familiarity, and the words only the reference dissertations use |
| [vocabulary_ref/README.md](vocabulary_ref/README.md) | The other files, the checker, and how the vocabulary is rebuilt |

## How to use it

Before drafting or revising Hang's prose, read the terms with fixed meanings and how familiarity is marked in [vocabulary.md](vocabulary.md), then look up terms as they come up. A term marked Core or Familiar needs no explanation. Define a term marked Read only or Cited only on first use, or check that its field meaning fits. The marks describe Hang's usage, not the reader's knowledge, so define a term when the audience needs it even if it is marked Core.

For a term's counts, an example sentence, or its source, search [vocabulary_ref/tech-vocabulary.md](vocabulary_ref/tech-vocabulary.md).

To check a draft, run from this skill's folder `python vocabulary_ref/tools/check_vocabulary.py <file>.tex`, with `--out <report>.md` to save the report. It needs Python 3.8 or newer and nothing else. A word in the report is a prompt to look at the sentence, not an error, and a word outside the vocabulary is not wrong for that reason alone.

The common academic words that read as AI-drafted and the phrases Hang replaced in review are rules of style, not vocabulary, so they are not listed here. The phrases are in the `writing-style` skill.

## Where it comes from

Part 1 of the vocabulary comes from six of Hang's published papers and their drafts (about 54,000 words). Part 2 comes from 15 field dissertations, counted apart from the papers so that they never raise a familiarity mark: three committee dissertations that Hang named, and 12 recent dissertations (2023 to 2026) from the labs of Matarić, Song, Li, Writer B, and Scassellati. The lab dissertations' PDFs and text are not bundled. They are in the plugin repository's `dissertation_reference/` folder.

The vocabulary was part of the writing style skills until November 20, 2026, when it moved here: the compact vocabulary from `writing-style-portable` (a skill since removed), and the full technical vocabulary and its tools from `writing-style`.

The build and validation scripts in `vocabulary_ref/tools/` need Hang's papers and the dissertations' text, which are not bundled. Their paths are provenance, not required inputs. Do not run them as part of ordinary writing or review, and do not claim to have opened a source that is absent.
