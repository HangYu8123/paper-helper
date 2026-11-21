# Committee writing style reference

Start with the [committee writing style reference](committee-writing-style-reference.md). It holds 63 patterns across vocabulary, wording preference, writing style, sentence style, sentence structure, and storytelling style, which are the six categories of [Hang's writing style reference](../writing_style_ref/README.md). The patterns come from the dissertations of three members of Hang's committee, which Hang named as the sources for the committee writing style. They are called Writer A, Writer B, and Writer C. Their names, the titles of their dissertations, the PDFs, and the text extracted from the PDFs are not in the repository.

| File | Use |
| --- | --- |
| [committee-writing-style-reference.md](committee-writing-style-reference.md) | The complete reference, with a quick reference, a comparison of the three writers, and a comparison with Hang's reference |
| [source-evidence.md](source-evidence.md) | All 282 quotations, grouped by pattern, each with its page |
| [writer-profiles.md](writer-profiles.md) | The measures for each writer and for Hang's draft, and how they were counted |
| [library.json](library.json) | The patterns, quotations, and measures in a structured format |
| [validation.md](validation.md) | Quotation, page number, link, and count checks |
| [tools](tools/) | The scripts that build and check the reference |

Each pattern says which of the three writers show it, gives reusable forms, and has a line on how it relates to Hang's dissertation. It is marked as saying the same as Hang's reference, adding to it, or differing from Hang's preference. Hang's instructions and Hang's reference take priority where the two differ. The quotations are evidence of how the three wrote, with their first person and their punctuation, and they are not text to copy.

Prepared on October 12, 2026. No dissertation file was changed.

To change a pattern, edit `tools/authored_entries.py` and run the build and the validation from the dissertation folder. The `.md` files and `library.json` are generated, so do not edit them.

```
python committee_style_ref/tools/build_reference.py
python committee_style_ref/tools/validate_reference.py
```

The build stops when a quotation is not found on its page and prints the page on which it was found. To refresh the last column of the measures after the draft has changed, compile `main.pdf` and run `python committee_style_ref/tools/profile_draft.py` before the build. To extract the text of the PDFs again, run `python committee_style_ref/tools/extract_text.py`. Both need pdftotext, which Git for Windows provides. The tools read the PDFs as `dessertation_reference/writer_a.pdf`, `writer_b.pdf`, and `writer_c.pdf`, and the build and the validation read their text from `sources/text/`, which is not in the repository.
