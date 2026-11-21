# Hang's technical vocabulary

The full technical vocabulary behind the compact [vocabulary.md](../vocabulary.md). Start with [tech-vocabulary.md](tech-vocabulary.md), and search it by term or heading rather than reading it whole.

| File | Use |
| --- | --- |
| [tech-vocabulary.md](tech-vocabulary.md) | Technical terms from Hang's papers and 15 reference dissertations (the committee's three and 12 recent lab dissertations), each with an estimate of how familiar it is to Hang, an example, and its source |
| [word-list.md](word-list.md) | Every word family the papers use, grouped by the same familiarity estimate, and the words only the reference dissertations use |
| [tech-vocabulary.json](tech-vocabulary.json) | The vocabulary and the full word list in a structured format, read by the checker |
| [vocabulary-check-chapters.md](vocabulary-check-chapters.md) | The chapters of Hang's dissertation checked against the vocabulary, as an example of the checker's report |
| [general-english-zipf.tsv](general-english-zipf.tsv) | General English word frequencies, read by the tools |
| [validation.md](validation.md) | The check of every example against its source line or PDF page |
| `tools/` | The checker, the build and validation scripts, the corpus definition (`vocab_corpus.py`), and the curated term list (`vocab_authored.py`) |

## Check a draft

Run from the writing-vocabulary skill's folder, with Python 3.8 or newer and nothing else installed:

```
python vocabulary_ref/tools/check_vocabulary.py <file>.tex
python vocabulary_ref/tools/check_vocabulary.py "<paper>/chapters/*.tex" --out <report>.md
```

The report sorts the draft's words into groups, such as common academic words the papers never use, words only the reference dissertations use, and words in none of the sources. A match is a prompt to look at the sentence, not an error.

## Rebuild

To rebuild after adding a paper to `tools/vocab_corpus.py` or editing the term list in `tools/vocab_authored.py`, run `python vocabulary_ref/tools/build_vocabulary.py` from the skill's folder, then `python vocabulary_ref/tools/validate_vocabulary.py`. If the reference dissertation PDFs change, run `tools/extract_reference_text.py` first. Set `VOCAB_PAPERS` to the dissertation's `reference_papers/` and `VOCAB_LAB_DISSERTATIONS` to the lab dissertations' folder when either is not in its default place. The example report is made with `python vocabulary_ref/tools/check_vocabulary.py "<dissertation>/chapters/*.tex" --out vocabulary_ref/vocabulary-check-chapters.md`. The writing-style skill's `build_reference.py` quotes the number of terms when this skill sits next to it, so rebuild that reference after a change in the count.

The build and the validation need Hang's papers, the committee dissertations' text in `sources/reference-dissertations/`, and the lab dissertations' text, none of which is bundled. Their paths in the tools and in the generated files are provenance, not required inputs. Do not run the build, extraction, or validation scripts as part of ordinary writing or review.

## History

The vocabulary was added to Hang's writing style reference on October 17, 2026 from a scan of six of Hang's papers (CHARM, Demonstration Sidetracks, PHIRL, Progress, the prospectus, and STEADY), and expanded the same day with the three committee dissertations, which are counted separately and never raise a familiarity tier. It was expanded on November 8, 2026 with 12 recent dissertations from the labs of Matarić, Song, Li, Writer B, and Scassellati, which added 171 terms, two groups (Simulation, vision, and generative models; Application areas and populations), and 22 acronyms. On November 20, 2026 it moved, with its tools, from the writing-style skill to this skill, so that the style guides and the vocabulary can be installed separately.
