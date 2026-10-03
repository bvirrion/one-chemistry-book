"""Every character table printed in Book 4 (environment omchartable) is
checked: the irreducible representations are orthonormal under the class
weights, sum of squared dimensions = order, number of irreps = number of
classes. The tables are integers or simple surds; entries such as 2\\cos72
are not used in the book."""
import glob
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
ENV = re.compile(r"\\begin\{omchartable\}\{([^}]*(?:\{[^}]*\}[^}]*)*)\}\{([^}]*)\}\{(.*?)\}\s*\n(.*?)\\end\{omchartable\}", re.S)


def class_size(h):
    m = re.match(r"\s*(\d+)", h)
    return int(m.group(1)) if m else 1


def number(c):
    c = c.strip().replace("{", "").replace("}", "")
    if c in ("", ):
        raise ValueError
    return int(c)


def tables():
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "parts", "bachelor-3", "[0-9]*.tex"))):
        for m in ENV.finditer(open(f, encoding="utf8").read()):
            group, spec, head, body = m.groups()
            sizes = [class_size(h) for h in head.split("&")]
            rows = []
            for line in body.split("\\\\"):
                cells = line.split("&")
                if len(cells) < len(sizes) + 1:
                    continue
                rows.append([number(c) for c in cells[1:1 + len(sizes)]])
            out.append((os.path.basename(f), group, sizes, rows))
    return out


def test_tables_exist():
    assert len(tables()) >= 3


def test_orthogonality():
    for f, group, sizes, rows in tables():
        h = sum(sizes)
        assert len(rows) == len(sizes), (f, group)
        assert sum(r[0] ** 2 for r in rows) == h, (f, group)
        for i, a in enumerate(rows):
            for j, b in enumerate(rows):
                s = sum(g * x * y for g, x, y in zip(sizes, a, b))
                assert s == (h if i == j else 0), (f, group, i, j)
