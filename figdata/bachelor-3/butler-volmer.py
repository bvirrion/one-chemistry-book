"""Ch. 15, the Butler-Volmer equation i/i0 = exp(alpha_a f eta) -
exp(-alpha_c f eta), f = nF/RT (n = 1, 298.15 K), with alpha_c = 0.3, 0.5,
0.7 (alpha_a = 1 - alpha_c), and the Tafel plot log10|i/i0| against eta."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

T = 298.15


def f(n=1):
    return n * value("const:F") / (value("const:R") * T)


def bv(eta, ac, n=1):
    return math.exp((1 - ac) * f(n) * eta) - math.exp(-ac * f(n) * eta)


def tafel_slope_mV(a, n=1):
    """mV per decade for a branch with coefficient a"""
    return 1000 * math.log(10) / (a * f(n))


def r_ct_times_i0(n=1):
    """R_ct i0 = RT/nF (V)"""
    return 1 / f(n)


def rows():
    out = []
    for i in range(0, 241):
        eta = -0.3 + 0.0025 * i
        out.append((1000 * eta,) + tuple(bv(eta, a) for a in (0.3, 0.5, 0.7))
                   + tuple(math.log10(abs(bv(eta, a))) if abs(eta) > 1e-9 else float("nan") for a in (0.3, 0.5, 0.7)))
    return out


if __name__ == "__main__":
    write_table(__file__, ("eta_mV", "a3", "a5", "a7", "l3", "l5", "l7"), rows())
    print("Tafel slope a=0.5: %.1f mV/dec; RT/F = %.2f mV" % (tafel_slope_mV(0.5), 1000 / f()))
