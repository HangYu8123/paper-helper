"""Validate the technical vocabulary and write validation.md.

Every paper example must quote its source line, and every reference example must be on the PDF page
it cites. Run from the writing-vocabulary skill's folder:  python vocabulary_ref/tools/validate_vocabulary.py
It needs the unbundled sources: the papers (VOCAB_PAPERS), the committee text in
sources/reference-dissertations/, and the lab dissertations' text (VOCAB_LAB_DISSERTATIONS).
"""

import datetime
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE / 'tools'))
import vocab_corpus as vc  # noqa: E402

ERRORS = []


def check(condition, message):
    if not condition:
        ERRORS.append(message)


vocab_path = HERE / 'tech-vocabulary.json'
if not vocab_path.exists():
    sys.exit('tech-vocabulary.json is missing. Run vocabulary_ref/tools/build_vocabulary.py first.')
vocab = json.loads(vocab_path.read_text(encoding='utf-8'))

examples = 0
for term in vocab['terms']:
    ex = term.get('example')
    if not ex:
        continue
    examples += 1
    source = vc.PAPERS / ex['file']
    lines = source.read_text(encoding='utf-8', errors='replace').replace('\r\n', '\n').split('\n')
    bold = re.search(r'\*\*(.+?)\*\*', ex['text'])
    first = bold.group(1).split()[0].split('-')[0].lower() if bold else ''
    check(0 < ex['line'] <= len(lines) and first in lines[ex['line'] - 1].lower(),
          f"Vocabulary example does not match its source line: {term['term']} ({ex['file']}:{ex['line']})")

# Examples from the reference dissertations must be on the PDF page they cite.
ref_pages = {}
for ref in vocab.get('references', []):
    text = vc.reference_text_path(ref['name']).read_text(encoding='utf-8')
    for a, b in [('ﬀ', 'ff'), ('ﬁ', 'fi'), ('ﬂ', 'fl'), ('ﬃ', 'ffi'), ('ﬄ', 'ffl'),
                 ('’', "'"), ('‘', "'")]:
        text = text.replace(a, b)
    pages = re.split(r'^\[\[page (\d+)\]\]$', text, flags=re.M)
    ref_pages[ref['file']] = {int(pages[i]): pages[i + 1].lower() for i in range(1, len(pages) - 1, 2)}
ref_examples = 0
for term in vocab['terms']:
    ex = term.get('reference_example')
    if not ex:
        continue
    ref_examples += 1
    bold = re.search(r'\*\*(.+?)\*\*', ex['text'])
    first = bold.group(1).split()[0].split('-')[0].lower() if bold else ''
    page_text = ref_pages.get(ex['file'], {}).get(ex['page'], '')
    check(first and first in page_text,
          f"Reference example is not on its PDF page: {term['term']} ({ex['file']} p. {ex['page']})")

shown = sum(1 for t in vocab['terms'] if t['tier'] != 'Not found')
missing = len(vocab['terms']) - shown
reference_only = sum(1 for t in vocab['terms'] if t['tier'] == 'Reference only')
today = datetime.date.today()
report = f"""# Validation of the technical vocabulary

Checked on {today.strftime('%B')} {today.day}, {today.year}.

| Check | Result |
| --- | --- |
| Terms | {shown} terms with familiarity estimates ({reference_only} Reference only) and {missing} field terms in none of the sources, built {vocab['built']} |
| Paper examples | {examples} checked against their source lines |
| Reference examples | {ref_examples} checked against their PDF pages |
| Overall result | {'PASS' if not ERRORS else 'FAIL'} |
"""
if ERRORS:
    report += '\n## Issues\n\n' + '\n'.join('- ' + error for error in ERRORS) + '\n'
(HERE / 'validation.md').write_text(report, encoding='utf-8')
print(f"{'PASS' if not ERRORS else 'FAIL'}: {shown} terms; {examples} paper examples; {ref_examples} reference examples.")
for error in ERRORS:
    print(error)
