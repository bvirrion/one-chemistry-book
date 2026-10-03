"""First-order kinetics (grade 12, reaction rates).

SYNTHETIC, exercise data: k values are chosen, not measured.
  part a: t (min), [A] at k1 = 0.050 /min and at k2 = 0.100 /min (a warmer
          run), [A]0 = 10.0 mmol/L; plus the tangent at t = 0 of the first.
  part b: the "fading dye" data of the weekend problem: absorbance of
          crystal violet against time, A0 = 0.800, half-life 6.0 min, with
          small fixed "measurement" offsets; and ln A.
"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table

A0 = 10.0            # mmol/L
K1, K2 = 0.050, 0.100  # 1/min

DYE_A0 = 0.800
DYE_HALF = 6.0                       # min
DYE_K = math.log(2) / DYE_HALF       # 1/min
DYE_T = (0, 2, 4, 6, 8, 10, 12, 15, 20, 25)
DYE_OFFSETS = (0.000, 0.004, -0.003, 0.002, -0.002, 0.003, -0.001, 0.002, -0.001, 0.001)


def conc(t, k, a0=A0):
    return a0 * math.exp(-k * t)


def half_life(k):
    return math.log(2) / k


def curves(tmax=60, step=0.5):
    n = int(tmax / step)
    return [(round(i * step, 2), round(conc(i * step, K1), 4), round(conc(i * step, K2), 4),
             round(A0 - K1 * A0 * i * step, 4)) for i in range(n + 1)]


def dye():
    rows = []
    for t, d in zip(DYE_T, DYE_OFFSETS):
        a = round(DYE_A0 * math.exp(-DYE_K * t) + d, 3)
        rows.append((t, a, round(math.log(a), 3)))
    return rows


def ln_slope(rows):
    """Least-squares slope of ln A against t."""
    n = len(rows)
    mt = sum(r[0] for r in rows) / n
    my = sum(r[2] for r in rows) / n
    return sum((r[0] - mt) * (r[2] - my) for r in rows) / sum((r[0] - mt) ** 2 for r in rows)


if __name__ == "__main__":
    write_table(__file__, ("t", "A1", "A2", "tangent"), curves(), part="a", digits=6)
    write_table(__file__, ("t", "A", "lnA"), dye(), part="b", digits=6)
