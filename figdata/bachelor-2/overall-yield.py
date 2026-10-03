"""Overall yield of a linear sequence (chapter 28): with n steps of yield rho
each, the overall yield is rho**n (exercise model, no measured data).
Columns: n, then the overall yield in % for rho = 0.95, 0.90, 0.80, 0.70."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table

RHOS = (0.95, 0.90, 0.80, 0.70)


def overall(step_yields):
    """Product of the step yields (fractions)."""
    y = 1.0
    for r in step_yields:
        y *= r
    return y


def curve(rho, n_max=20):
    return [(n, 100 * overall([rho] * n)) for n in range(0, n_max + 1)]


if __name__ == "__main__":
    cols = [curve(r) for r in RHOS]
    rows = [(cols[0][i][0],) + tuple(c[i][1] for c in cols) for i in range(len(cols[0]))]
    write_table(__file__, ("n", "r95", "r90", "r80", "r70"), rows)
