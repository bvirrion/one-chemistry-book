"""Ch. 6, the fundamental band of HCl at 300 K: P and R branches of H35Cl
and H37Cl (abundances 0.758/0.242), lines from the ledger constants
(band origin nu0 = we - 2 wexe; B0 = Be - ae/2, B1 = Be - 3ae/2; the 37Cl
constants scaled by rho = sqrt(mu35/mu37): we*rho, wexe*rho^2, Be*rho^2,
ae*rho^3), intensities proportional to the lower-level population,
Lorentzian lines of HWHM 0.5 cm-1."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402


def c2():
    return 100 * value("const:h") * value("const:c") / value("const:kB")


def rho():
    h, c35, c37 = value("imass:H1"), value("imass:Cl35"), value("imass:Cl37")
    mu35, mu37 = h * c35 / (h + c35), h * c37 / (h + c37)
    return math.sqrt(mu35 / mu37)


def constants(iso=35):
    r = 1.0 if iso == 35 else rho()
    we, wexe = value("diat:HCl.we") * r, value("diat:HCl.wexe") * r * r
    Be, ae = value("diat:HCl.Be") * r * r, value("diat:HCl.ae") * r ** 3
    return we - 2 * wexe, Be - ae / 2, Be - 1.5 * ae


def R(J, iso=35):
    nu0, B0, B1 = constants(iso)
    return nu0 + B1 * (J + 1) * (J + 2) - B0 * J * (J + 1)


def P(J, iso=35):
    nu0, B0, B1 = constants(iso)
    return nu0 + B1 * (J - 1) * J - B0 * J * (J + 1)


def weight(J, iso=35, T=300):
    B0 = constants(iso)[1]
    a = value("iso:Cl35") if iso == 35 else value("iso:Cl37")
    return a * (2 * J + 1) * math.exp(-c2() * B0 * J * (J + 1) / T)


def spectrum(x):
    s = 0.0
    for iso in (35, 37):
        for J in range(0, 20):
            s += weight(J, iso) / (1 + ((x - R(J, iso)) / 0.5) ** 2)
            if J >= 1:
                s += weight(J, iso) / (1 + ((x - P(J, iso)) / 0.5) ** 2)
    return s


if __name__ == "__main__":
    xs = [2600 + 0.2 * i for i in range(2501)]
    ys = [spectrum(x) for x in xs]
    top = max(ys)
    write_table(__file__, ("nu", "A"), [(x, y / top) for x, y in zip(xs, ys)])
