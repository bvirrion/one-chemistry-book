"""Ch. 6, the Morse potential of H35Cl built from the ledger constants
(omega_e, omega_e x_e, r_e) in the Morse approximation (D_e = omega_e^2 /
4 omega_e x_e), its vibrational levels G(v) = omega_e (v+1/2) - omega_e x_e
(v+1/2)^2, the harmonic parabola, and the Birge-Sponer plot Delta G(v+1/2)
against v. The true D0 (JANAF enthalpies of formation at 0 K) is printed for
comparison."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402


def we():
    return value("diat:HCl.we")


def wexe():
    return value("diat:HCl.wexe")


def de_morse():
    return we() ** 2 / (4 * wexe())


def G(v):
    return we() * (v + 0.5) - wexe() * (v + 0.5) ** 2


def vmax():
    return int(we() / (2 * wexe()) - 0.5)


def d0_true():
    """cm-1, from JANAF 0 K formation enthalpies"""
    kj = value("janaf:H.dfH0") + value("janaf:Cl.dfH0") - value("janaf:HCl.dfH0")
    return kj * 1000 / (100 * value("const:h") * value("const:c") * value("const:NA"))


def reduced_mass():
    m1, m2 = value("imass:H1"), value("imass:Cl35")
    return m1 * m2 / (m1 + m2) * value("const:u")


def beta():
    """Morse parameter in 1/angstrom"""
    k = (2 * math.pi * value("const:c") * 100 * we()) ** 2 * reduced_mass()
    de_J = de_morse() * 100 * value("const:h") * value("const:c")
    return math.sqrt(k / (2 * de_J)) * 1e-10


def morse(r):
    re = value("re:HCl")
    return de_morse() * (1 - math.exp(-beta() * (r - re))) ** 2


def harmonic(r):
    re = value("re:HCl")
    return de_morse() * beta() ** 2 * (r - re) ** 2


def turning(v):
    """the two r where the Morse curve equals G(v)"""
    re, b, D = value("re:HCl"), beta(), de_morse()
    x = math.sqrt(G(v) / D)
    return re - math.log(1 + x) / b, re - math.log(1 - x) / b


if __name__ == "__main__":
    rs = [0.8 + 0.01 * i for i in range(321)]
    write_table(__file__, ("r", "V", "harm"), [(r, morse(r), harmonic(r)) for r in rs])
    rows = []
    for v in range(0, vmax() + 1, 3):
        a, b = turning(v)
        rows += [(a, G(v)), (b, G(v)), (float("nan"), float("nan"))]
    write_table(__file__, ("r", "E"), rows, part="levels")
    write_table(__file__, ("v", "dG"), [(v, G(v + 1) - G(v)) for v in range(vmax())], part="bs")
