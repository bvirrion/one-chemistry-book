"""Ch. 28, kinetic resolution. A racemic substrate whose enantiomers react by
first-order (or pseudo-first-order) kinetics with rate constants k_fast and
k_slow = k_fast/s. With a = fraction of the slow enantiomer left, the fast one
has a^s left; conversion c = 1 - (a + a^s)/2, ee of the remaining substrate
(a - a^s)/(a + a^s), ee of the product (a - a^s)/(2 - a - a^s). Kagan's
equation: s = ln[(1 - c)(1 - ee_sm)]/ln[(1 - c)(1 + ee_sm)]. Curves for
s = 2, 10, 50 against conversion (parts s2, s10, s50: c, ee_sm, ee_p)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

SS = (2, 10, 50)


def state(a, s):
    f = a ** s
    c = 1 - (a + f) / 2
    ee_sm = (a - f) / (a + f)
    ee_p = (a - f) / (2 - a - f) if c > 0 else 0.0
    return c, ee_sm, ee_p


def kagan_s(c, ee_sm):
    return math.log((1 - c) * (1 - ee_sm)) / math.log((1 - c) * (1 + ee_sm))


def curve(s, n=300):
    rows = []
    for j in range(1, n):
        a = 1 - j / n          # slow enantiomer left
        c, e1, e2 = state(a, s)
        if c <= 0.995:
            rows.append((c, e1, e2))
    return rows


if __name__ == "__main__":
    for s in SS:
        write_table(__file__, ("c", "eesm", "eep"), curve(s), part="s%d" % s)
    print([round(kagan_s(*state(0.8, s)[:2]), 6) for s in SS])
