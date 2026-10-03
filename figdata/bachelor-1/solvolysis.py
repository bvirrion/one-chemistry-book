"""Data of the ch. 19 weekend problem: solvolysis of 2-chloro-2-methylpropane
followed by conductimetry at two temperatures. The 'measured' conductivities
are generated from first-order kinetics with the problem's chosen rate
constant k(25 degC) = 3.0e-4 s-1 and activation energy 90 kJ/mol (story
data, not literature values), rounded to 0.001 mS/cm; the test checks that
the analysis asked of the student recovers them."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

K25, EA, KINF = 3.0e-4, 90.0e3, 2.000
TIMES = (0, 5, 10, 15, 20, 30, 45, 60)       # min


def k_at(t_celsius):
    r = value("const:R")
    return K25 * math.exp(-EA / r * (1 / (t_celsius + 273.15) - 1 / 298.15))


def kappa(t_min, t_celsius=25.0):
    return round(KINF * (1 - math.exp(-k_at(t_celsius) * 60 * t_min)), 3)


def fit_k(t_celsius):
    """Least-squares slope of ln(kappa_inf - kappa) against t (s)."""
    xs = [60 * t for t in TIMES]
    ys = [math.log(KINF - kappa(t, t_celsius)) for t in TIMES]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    return -sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)


def activation_energy():
    r = value("const:R")
    k1, k2 = fit_k(25.0), fit_k(35.0)
    return r * math.log(k2 / k1) / (1 / 298.15 - 1 / 308.15)


if __name__ == "__main__":
    write_table(__file__, ("t", "k25", "k35"), [(t, kappa(t), kappa(t, 35.0)) for t in TIMES], digits=4)
