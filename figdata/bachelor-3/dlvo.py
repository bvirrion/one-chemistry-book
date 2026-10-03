"""Ch. 17, DLVO interaction of two equal spheres in water at 298.15 K
(model colloid: radius 100 nm, diffuse-layer potential -30 mV, Hamaker
constant 2.0e-20 J; model values, not a measured system), Derjaguin form:
V_R = 2 pi eps a psi^2 ln(1 + exp(-kappa h)) (constant potential, low
potential), V_A = -A a / (12 h); kappa from the ionic strength of a 1:1 salt
or of the weekend problem's soft water (1.0 mM NaHCO3)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

T = 298.15
A_SPH, PSI, HAMAKER = 100e-9, -0.030, 2.0e-20
EPS = value("eps:H2O.25C") * value("const:eps0")
KT = value("const:kB") * T
WATER = {"Na+": (1.0, 1), "HCO3-": (1.0, -1)}


def ionic_strength(ions):
    """mol/m3 from {name: (mmol/L, z)}"""
    return 0.5 * sum(c * z * z for c, z in ions.values())


def debye_length(I):
    """m, for ionic strength I in mol/m3"""
    F, R = value("const:F"), value("const:R")
    return math.sqrt(EPS * R * T / (2 * F * F * I))


def v_kt(h, I):
    k = 1 / debye_length(I)
    vr = 2 * math.pi * EPS * A_SPH * PSI ** 2 * math.log(1 + math.exp(-k * h))
    va = -HAMAKER * A_SPH / (12 * h)
    return (vr + va) / KT


def barrier(I):
    hs = [0.2e-9 * 1.02 ** i for i in range(400)]
    return max(v_kt(h, I) for h in hs)


def critical_I():
    """ionic strength at which the maximum of V falls to zero (bisection)"""
    lo, hi = 1.0, 2000.0
    for _ in range(80):
        mid = math.sqrt(lo * hi)
        if barrier(mid) > 0:
            lo = mid
        else:
            hi = mid
    return mid


IS = (ionic_strength(WATER), 10.0, 50.0, 200.0)


if __name__ == "__main__":
    rows = []
    for i in range(1, 301):
        h = 0.1e-9 * i
        rows.append((h * 1e9,) + tuple(v_kt(h, I) for I in IS))
    write_table(__file__, ("h_nm", "I1", "I10", "I50", "I200"), rows)
    print("I water %.2f mM, Debye %.2f nm; barriers %s; critical I %.0f mM" %
          (ionic_strength(WATER), debye_length(ionic_strength(WATER)) * 1e9,
           [round(barrier(I), 1) for I in IS], critical_I()))
