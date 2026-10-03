"""Ch. 19, Marcus theory with a model reorganisation energy lambda =
100 kJ/mol at 298.15 K: (a) intersecting parabolas G_R = lambda x^2 and
G_P = lambda (x - 1)^2 + dG for dG = 0, -lambda/2, -lambda and -3 lambda/2;
(b) log10 of the rate constant, k = k_max exp(-(lambda + dG)^2 / (4 lambda R T))
with k_max = 1e11 s-1 (model), against -dG, with the normal and inverted
regions."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

LAM, T, KMAX = 100.0, 298.15, 1.0e11       # kJ/mol, K, s-1
DGS = (0.0, -50.0, -100.0, -150.0)


def dg_act(dg, lam=LAM):
    return (lam + dg) ** 2 / (4 * lam)


def log10k(dg):
    R = value("const:R") / 1000
    return math.log10(KMAX) - dg_act(dg) / (R * T * math.log(10))


def crossing(dg, lam=LAM):
    """x at which the two parabolas cross"""
    return (lam + dg) / (2 * lam)


if __name__ == "__main__":
    rows = []
    for i in range(0, 161):
        x = -0.6 + 0.0175 * i
        rows.append((x, LAM * x * x) + tuple(LAM * (x - 1) ** 2 + dg for dg in DGS))
    write_table(__file__, ("x", "GR", "P0", "P50", "P100", "P150"), rows, part="parabolas")
    write_table(__file__, ("mdG", "logk"), [(m, log10k(-m)) for m in range(0, 251, 2)], part="rate")
