"""Ch. 3, minimal-basis (STO-3G) restricted Hartree-Fock for H2 and HeH+.

(a) RHF/STO-3G energy of H2 against R, with a Morse curve built from the
    ledger (D0 from JANAF, omega_e, omega_e x_e, r_e) and E(2 H) = -1 Eh;
(b) the SCF history of HeH+ at R = 1.4632 bohr, standard basis;
(c) the STO-1G/2G/3G fits to the 1s Slater function (zeta = 1).
The code is tested on the classic benchmark (H2 at 1.4 bohr, zeta_H = 1.24;
HeH+ with zeta_He = 2.0925, zeta_H = 1.24)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402
import _qm  # noqa: E402

COEF = ("bse:sto3g.c1", "bse:sto3g.c2", "bse:sto3g.c3")
UNIT = (2.227660, 0.4057711, 0.1098175)    # STO-3G exponents for zeta = 1 (BSE H / 1.24^2)


def sto3g(atom):
    return [(value("bse:%s.sto3g.a%d" % (atom, i + 1)), value(COEF[i])) for i in range(3)]


def scaled(zeta):
    return [(a * zeta * zeta, value(c)) for a, c in zip(UNIT, COEF)]


def h2(R, basis=None):
    b = basis or sto3g("H")
    return _qm.rhf([(0.0, b), (R, b)], [(0.0, 1), (R, 1)])


def heh(R, he=None, h=None):
    he, h = he or sto3g("He"), h or sto3g("H")
    return _qm.rhf([(0.0, he), (R, h)], [(0.0, 2), (R, 1)])


def hartree_kJ():
    return value("const:Eh") * value("const:NA") / 1000


def morse(R):
    """exact-ish H2 curve: Morse with D_e = D0 + G(0), from the ledger"""
    cm = 100 * value("const:h") * value("const:c") / value("const:Eh")   # cm-1 -> Eh
    we, wexe = value("diat:H2.we"), value("diat:H2.wexe")
    d0 = 2 * value("janaf:H.dfH0") / hartree_kJ()
    de = d0 + (we / 2 - wexe / 4) * cm
    re = value("re:H2") * 1e-10 / value("const:a0")
    # Morse beta from omega_e and the reduced mass: we = beta/(2 pi c) sqrt(2 De/mu)
    mu = value("aw:H") / 2 * value("const:u")
    de_J = de * value("const:Eh")
    b = 2 * math.pi * value("const:c") * 100 * we * math.sqrt(mu / (2 * de_J))   # 1/m
    b *= value("const:a0")                                                        # 1/bohr
    return -1.0 - de + de * (1 - math.exp(-b * (R - re))) ** 2, de, re


def h_atom(basis=None):
    """energy of one electron in the STO-3G 1s function of hydrogen"""
    b = basis or sto3g("H")
    S, T, V, G = _qm.integrals([(0.0, b)], [(0.0, 1)])
    return (T[0, 0] + V[0, 0]) / S[0, 0]


def h2_minimum():
    """golden-section search of the RHF/STO-3G minimum, R in bohr"""
    a, b = 1.2, 1.5
    g = (math.sqrt(5) - 1) / 2
    for _ in range(40):
        c, d = b - g * (b - a), a + g * (b - a)
        if h2(c)[0] < h2(d)[0]:
            b = d
        else:
            a = c
    R = (a + b) / 2
    return R, h2(R)[0]


def sto_ng_fit(r):
    """1s Slater function (zeta = 1) and its STO-1G (alpha 0.270950), STO-3G
    approximations, all normalised, at radius r (bohr)"""
    slater = math.exp(-r) / math.sqrt(math.pi)
    g1 = _qm.norm(0.270950) * math.exp(-0.270950 * r * r)
    g3 = sum(value(c) * _qm.norm(a) * math.exp(-a * r * r) for a, c in zip(UNIT, COEF))
    return slater, g1, g3


def overlap_sto3g_slater(steps=20000, rmax=20.0):
    h = rmax / steps
    s = 0.0
    for i in range(steps):
        r = (i + 0.5) * h
        sl, _, g3 = sto_ng_fit(r)
        s += 4 * math.pi * r * r * sl * g3 * h
    return s


if __name__ == "__main__":
    rows = []
    for i in range(8, 101):
        R = i / 10
        rows.append((R, h2(R)[0], morse(R)[0]))
    write_table(__file__, ("R", "rhf", "morse"), rows, part="h2")
    e, eps, hist, S = heh(1.4632)
    write_table(__file__, ("it", "E"), [(k + 1, v) for k, v in enumerate(hist[:8])], part="heh-scf")
    write_table(__file__, ("r", "slater", "g1", "g3"),
                [(r / 20, *sto_ng_fit(r / 20)) for r in range(0, 101)], part="sto")
