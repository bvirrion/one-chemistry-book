"""Merge the physics glossaries (Books 1-5) and sources/GLOSSARY_BOOK_{1..N}_ZH.md into one file for glossary.py
split: a later line replaces every earlier line that shares one of its English forms (case-insensitive).
Usage: merge_glossary.py N out.md"""
import re, sys
n, out = int(sys.argv[1]), sys.argv[2]
LINE = re.compile(r'^(\d\d) \| (.*?) \| (.*)$')
files = [f'../one-physics-book/sources/GLOSSARY_BOOK_{b}_ZH.md' for b in range(1, 6)] + \
        [f'sources/GLOSSARY_BOOK_{b}_ZH.md' for b in range(1, n + 1)]
lines = []
for path in files:
    for raw in open(path, encoding='utf-8'):
        m = LINE.match(raw.strip())
        if not m:
            continue
        forms = {f.strip().lower() for f in m.group(2).split(' / ')}
        lines = [(f, r) for f, r in lines if not (f & forms)]
        lines.append((forms, raw.strip()))
hdr = open(f'sources/GLOSSARY_BOOK_{n}_ZH.md', encoding='utf-8').read().split('\n00 |')[0].rstrip()
open(out, 'w', encoding='utf-8').write(hdr + f'\n\n(Merged physics Books 1–5 and chemistry Books 1–{n}; generated, do not edit.)\n\n'
                                       + '\n'.join(r for _, r in lines) + '\n')
print(f'book {n}: {len(lines)} lines')
