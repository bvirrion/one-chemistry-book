"""Read ledger values by id, so that no figure script retypes a number.

    from _ledger import value, text
    value("const:Rinf")      -> 10973731.568157 (float)
    text("gs:Cr")            -> "[Ar] 3d5 4s1"

Reads sources/data_ledger.md and every sources/ledger/book*.md (the same
files tools/check_ledger.py checks).
"""
import glob
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
_ROWS = None


def _load():
    global _ROWS
    if _ROWS is None:
        _ROWS = {}
        files = [os.path.join(ROOT, "sources", "data_ledger.md")]
        files += sorted(glob.glob(os.path.join(ROOT, "sources", "ledger", "*.md")))
        for f in files:
            for line in open(f, encoding="utf8"):
                if not line.startswith("| ") or line.startswith("| id ") or line.startswith("| key "):
                    continue
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) >= 6 and ":" in cells[0]:
                    _ROWS[cells[0]] = cells
    return _ROWS


def text(key):
    return _load()[key][2]


def value(key):
    return float(text(key))
