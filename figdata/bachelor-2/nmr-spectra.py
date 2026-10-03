"""Carbon-13 spectra (chapter 33), from the ledger peak lists (PubChem/HMDB).
- a, b, c: butan-2-one, ethyl benzoate, benzyl ethanoate: one row per line,
  columns shift, dec (decoupled height, tallest line = 1), d135 (DEPT-135:
  +0.8 for CH and CH3, -0.8 for CH2, 0 for C; schematic heights), d90
  (DEPT-90: 0.8 for CH only);
- d: the measured shifts of this chapter's compounds sorted by carbon class
  (0 alkyl C, 1 C-O, 2 aromatic and alkene C, 3 ester C=O, 4 ketone C=O),
  for the shift chart."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _ledger import text
from _table import write_table

# carbon kinds (number of attached H) per line, in the order of the ledger rows
KINDS = {
    "c13:butanone": {209.28: 0, 36.87: 2, 29.43: 3, 7.87: 3},
    "c13:ethylbenzoate": {166.54: 0, 132.80: 1, 130.62: 0, 129.57: 1, 128.34: 1, 60.90: 2, 14.33: 3},
    "c13:benzylacetate": {170.70: 0, 136.14: 0, 128.56: 1, 128.24: 1, 66.24: 2, 20.82: 3},
    "c13:pentan-2-one": {208.93: 0, 45.71: 2, 29.78: 3, 17.41: 2, 13.70: 3},
}
CLASS = {  # shift class for the chart
    "c13:butanone": {209.28: 4, 36.87: 0, 29.43: 0, 7.87: 0},
    "c13:ethylbenzoate": {166.54: 3, 132.80: 2, 130.62: 2, 129.57: 2, 128.34: 2, 60.90: 1, 14.33: 0},
    "c13:benzylacetate": {170.70: 3, 136.14: 2, 128.56: 2, 128.24: 2, 66.24: 1, 20.82: 0},
    "c13:pentan-2-one": {208.93: 4, 45.71: 0, 29.78: 0, 17.41: 0, 13.70: 0},
}


def lines(key):
    return [(float(a), float(b)) for a, b in (p.split(":") for p in text(key).split())]


def dept135(n_h):
    return {0: 0.0, 1: 0.8, 2: -0.8, 3: 0.8}[n_h]


def dept90(n_h):
    return 0.8 if n_h == 1 else 0.0


def table(key):
    ls = lines(key)
    top = max(h for _, h in ls)
    return [(s, h / top, dept135(KINDS[key][s]), dept90(KINDS[key][s])) for s, h in ls]


if __name__ == "__main__":
    for part, key in (("a", "c13:butanone"), ("b", "c13:ethylbenzoate"), ("c", "c13:benzylacetate")):
        write_table(__file__, ("shift", "dec", "d135", "d90"), table(key), part=part)
    rows = []
    for key in CLASS:
        for s, _ in lines(key):
            rows.append((s, CLASS[key][s]))
    write_table(__file__, ("shift", "cls"), sorted(rows), part="d")
