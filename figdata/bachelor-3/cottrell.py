"""Ch. 15, potential-step chronoamperometry: concentration profiles
c(x,t)/c* = erf(x / 2 sqrt(D t)) at four times and the Cottrell current
i = nFAc* sqrt(D/(pi t)) (D = 1.0e-5 cm2/s, c* = 1.0 mM, A = 0.0707 cm2,
n = 1; model values). The erf profile is checked to solve Fick's second law
by finite differences in the test."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

D, C, A, N = 1.0e-5, 1.0e-6, 0.0707, 1      # cm2/s, mol/cm3, cm2


def profile(x, t):
    return math.erf(x / (2 * math.sqrt(D * t)))


def current(t):
    return N * value("const:F") * A * C * math.sqrt(D / (math.pi * t))


if __name__ == "__main__":
    write_table(__file__, ("x_um", "t1", "t2", "t3", "t4"),
                [(x, profile(x * 1e-4, 0.1), profile(x * 1e-4, 1), profile(x * 1e-4, 4), profile(x * 1e-4, 16))
                 for x in range(0, 601, 5)], part="profiles")
    write_table(__file__, ("t", "i_uA", "tm12"),
                [(0.05 * k, current(0.05 * k) * 1e6, (0.05 * k) ** -0.5) for k in range(2, 201)], part="current")
    print("i(1 s) = %.3f uA" % (current(1) * 1e6))
