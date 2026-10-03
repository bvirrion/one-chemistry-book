"""Ch. 13, chemical relaxation after a temperature jump for A + B <=> C
(model constants at the final temperature: k1 = 1.0e8 L mol-1 s-1,
km1 = 1.0e3 s-1; total concentrations 1.0e-4 mol/L each of A and B). The
system starts at the equilibrium of the initial temperature (K 5 % larger)
and relaxes to the new one; the numerical solution is compared with the
exponential of time constant tau, 1/tau = k1([A]e + [B]e) + km1."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ode import rk4  # noqa: E402

K1, KM1, A0, B0 = 1.0e8, 1.0e3, 1.0e-4, 1.0e-4


def eq_c(k):
    """[C] at equilibrium for K = k (L/mol) with totals A0, B0"""
    # k (A0 - c)(B0 - c) = c
    a, b, cc = k, -(k * (A0 + B0) + 1), k * A0 * B0
    return (-b - math.sqrt(b * b - 4 * a * cc)) / (2 * a)


def tau():
    c = eq_c(K1 / KM1)
    return 1 / (K1 * ((A0 - c) + (B0 - c)) + KM1)


def rhs(t, y):
    c = y[0]
    return [K1 * (A0 - c) * (B0 - c) - KM1 * c]


def run():
    c0 = eq_c(1.05 * K1 / KM1)
    return rk4(rhs, [c0], 0.0, 5 * tau(), tau() / 400, every=4)


if __name__ == "__main__":
    ce, c0, ta = eq_c(K1 / KM1), eq_c(1.05 * K1 / KM1), tau()
    write_table(__file__, ("t_us", "dC", "exp"),
                [(t * 1e6, (y[0] - ce) / (c0 - ce), math.exp(-t / ta)) for t, y in run()])
    print("tau = %.3g s, [C]e = %.4g, [C]0 = %.4g" % (ta, ce, c0))
