"""Extract the text of a paper PDF with a marker before each page.

    python pdf_pages.py <paper.pdf> <out.txt>

The markers (=== Page N ===) make it easy to cite page numbers and to search
the paper for quotes. pdftotext (poppler) is used when it can be found, since
it keeps the reading order of two-column papers. Verify its page breaks with
pdfinfo or pypdf. When the count differs, extract one physical page at a time.
pypdf also supplies page text when pdftotext fails.

Tables come out scrambled in any text extraction, so read results tables and
figures from the page images as well.
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

PDFTOTEXT_CANDIDATES = [
    r'C:\Program Files\Git\mingw64\bin\pdftotext.exe',
    '/mingw64/bin/pdftotext',
    '/usr/bin/pdftotext',
    '/opt/homebrew/bin/pdftotext',
]


def find_pdftotext():
    exe = shutil.which('pdftotext')
    if exe:
        return exe
    for path in PDFTOTEXT_CANDIDATES:
        if Path(path).exists():
            return path
    return None


def physical_page_count(pdf):
    exe = shutil.which('pdfinfo')
    if exe:
        result = subprocess.run([exe, str(pdf)], capture_output=True)
        match = re.search(rb'^Pages:[ \t]+(\d+)[ \t\r]*$', result.stdout, re.MULTILINE)
        if result.returncode == 0 and match and int(match.group(1)) > 0:
            return int(match.group(1))
    try:
        import pypdf
    except ImportError:
        return None
    return len(pypdf.PdfReader(str(pdf)).pages)


def with_pdftotext(pdf):
    exe = find_pdftotext()
    if not exe:
        return None
    options = dict(capture_output=True, encoding='utf-8', errors='replace')
    result = subprocess.run([exe, '-enc', 'UTF-8', str(pdf), '-'], **options)
    if result.returncode != 0:
        return None
    pages = result.stdout.split('\f')
    if pages and not pages[-1].strip():
        pages.pop()
    count = physical_page_count(pdf)
    if not count:
        raise SystemExit('Cannot verify physical pages. Provide working pdfinfo or pypdf, '
                         'or read and cite the PDF pages directly.')
    if len(pages) == count:
        return pages

    print(f'Found {len(pages)} text markers for {count} physical pages. '
          'Extracting each physical page separately.', file=sys.stderr)
    pages = []
    for i in range(1, count + 1):
        result = subprocess.run([exe, '-f', str(i), '-l', str(i), '-enc', 'UTF-8', str(pdf), '-'],
                                **options)
        if result.returncode != 0:
            return None
        pages.append(result.stdout.replace('\f', '\n'))
    return pages


def with_pypdf(pdf):
    try:
        import pypdf
    except ImportError:
        return None
    return [page.extract_text() or '' for page in pypdf.PdfReader(str(pdf)).pages]


def main(argv):
    if len(argv) != 2:
        raise SystemExit(__doc__)
    pdf, out = Path(argv[0]), Path(argv[1])
    if not pdf.exists():
        raise SystemExit(f'No such file: {pdf}')
    pages, tool = with_pdftotext(pdf), 'pdftotext'
    if pages is None:
        pages, tool = with_pypdf(pdf), 'pypdf'
    if pages is None:
        raise SystemExit('Neither pdftotext nor pypdf is available. Read the PDF with the Read tool instead, '
                         'a few pages at a time.')
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('w', encoding='utf-8') as f:
        for i, text in enumerate(pages, 1):
            f.write(f'\n=== Page {i} ===\n\n{text.strip()}\n')
    chars = sum(len(t) for t in pages)
    print(f'{len(pages)} pages, {chars} characters, extracted with {tool}, written to {out}')
    thin = [i for i, t in enumerate(pages, 1) if len(t.strip()) < 200]
    if thin:
        print('Pages with little or no text (figures or scans, read them as images): '
              + ', '.join(map(str, thin)))


if __name__ == '__main__':
    main(sys.argv[1:])
