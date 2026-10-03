"""Binary liquid-vapour diagrams (chapter 7).
Vapour pressures from the WebBook Antoine parameters (rows antoine:<sp>.A/B/C,
log10(p/bar) = A - B/(T + C), T in K).
- a: benzene-toluene, isobaric at 1.01325 bar (ideal, Raoult): x, T_bubble, y;
- b: the same pair, isothermal at 80 degC: x, p_bubble; y, p_dew;
- c: ethanol-water, a MODEL: one-parameter (symmetric) Margules activity
  coefficients, the parameter and the azeotrope temperature fitted to the
  sourced azeotrope composition (95 % by mass of ethanol) at 1.01325 bar;
- d: a model pair with a strongly negative deviation (benzene and toluene
  vapour pressures, Margules A = -2.0): a maximum-boiling azeotrope;
- e: toluene and water, immiscible: p*(T) of each and their sum;
- f: the staircase of theoretical plates at total reflux, benzene-toluene,
  from x_D = 0.95 down to x_B <= 0.05.
Temperatures are written in degC for the plots."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

P_ATM = 1.01325  # bar
K0 = 273.15


def psat(sp, T):
    """Vapour pressure in bar at T in K."""
    A, B, C = (value("antoine:%s.%s" % (sp, n)) for n in "ABC")
    return 10 ** (A - B / (T + C))


def tsat(sp, p=P_ATM):
    A, B, C = (value("antoine:%s.%s" % (sp, n)) for n in "ABC")
    return B / (A - math.log10(p)) - C


def solve(f, lo, hi):
    flo = f(lo)
    for _ in range(200):
        mid = (lo + hi) / 2
        fm = f(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2


def gammas(x, A):
    return math.exp(A * (1 - x) ** 2), math.exp(A * x ** 2)


def bubble(x, sp1, sp2, A=0.0, p=P_ATM):
    """Bubble temperature (K) and vapour composition y1 of a liquid x1."""
    def f(T):
        g1, g2 = gammas(x, A)
        return x * g1 * psat(sp1, T) + (1 - x) * g2 * psat(sp2, T) - p
    lo = min(tsat(sp1, p), tsat(sp2, p)) - 40
    hi = max(tsat(sp1, p), tsat(sp2, p)) + 40
    T = solve(f, lo, hi)
    g1, _ = gammas(x, A)
    return T, x * g1 * psat(sp1, T) / p


def ideal_dew(y, sp1, sp2, p=P_ATM):
    """Dew temperature (K) and liquid composition of an ideal pair's vapour y1."""
    T = solve(lambda T: y * p / psat(sp1, T) + (1 - y) * p / psat(sp2, T) - 1,
              tsat(sp1, p) - 1, tsat(sp2, p) + 1)
    return T, y * p / psat(sp1, T)


def azeotrope_mole_fraction():
    w = value("azeo:ethanol-water.w") / 100
    m_e = 2 * value("aw:C") + 6 * value("aw:H") + value("aw:O")
    m_w = 2 * value("aw:H") + value("aw:O")
    return (w / m_e) / (w / m_e + (1 - w) / m_w)


def ethanol_water_model():
    """(A, T_az): symmetric Margules fitted to the azeotrope composition."""
    x = azeotrope_mole_fraction()

    def T_of(A):  # temperature where the ethanol partial pressure alone gives p
        return solve(lambda T: math.exp(A * (1 - x) ** 2) * psat("ethanol", T) - P_ATM, 320, 380)

    def g(A):  # water condition at that temperature
        T = T_of(A)
        return math.exp(A * x ** 2) * psat("water", T) - P_ATM
    A = solve(g, 0.2, 3.0)
    return A, T_of(A)


def relative_volatility(T):
    return psat("benzene", T) / psat("toluene", T)


def mean_alpha():
    return math.sqrt(relative_volatility(tsat("benzene")) * relative_volatility(tsat("toluene")))


def fenske(xD=0.95, xB=0.05, alpha=None):
    a = alpha or mean_alpha()
    return math.log(xD / (1 - xD) * (1 - xB) / xB) / math.log(a)


def staircase(xD=0.95, xB=0.05):
    """Corners of the plate-to-plate construction at total reflux (operating
    line y = x): from (xD, xD) horizontally to the equilibrium curve, then
    vertically to the diagonal, until x <= xB. Returns the path and the
    number of steps."""
    path = [(xD, xD)]
    y = xD
    n = 0
    while True:
        T, x = ideal_dew(y, "benzene", "toluene")
        n += 1
        path.append((x, y))
        path.append((x, x))
        if x <= xB or n > 30:
            break
        y = x
    return path, n


def steam_temperature(sp="toluene", p=P_ATM):
    return solve(lambda T: psat(sp, T) + psat("water", T) - p, 330, 373)


def steam_mass_ratio(sp="toluene", M=None):
    T = steam_temperature(sp)
    M = M or (7 * value("aw:C") + 8 * value("aw:H"))
    Mw = 2 * value("aw:H") + value("aw:O")
    return psat(sp, T) * M / (psat("water", T) * Mw)


def xs(n=50):
    return [i / n for i in range(n + 1)]


if __name__ == "__main__":
    rows = []
    for x in xs():
        T, y = bubble(x, "benzene", "toluene")
        rows.append((x, T - K0, y))
    write_table(__file__, ("x", "T", "y"), rows, part="a")
    T80 = K0 + 80
    p1, p2 = psat("benzene", T80), psat("toluene", T80)
    rows = []
    for x in xs():
        rows.append((x, x * p1 + (1 - x) * p2, 1 / (x / p1 + (1 - x) / p2)))
    write_table(__file__, ("x", "pbub", "pdew"), rows, part="b")
    A, _ = ethanol_water_model()
    rows = []
    for x in xs(100):
        T, y = bubble(x, "ethanol", "water", A)
        rows.append((x, T - K0, y))
    write_table(__file__, ("x", "T", "y"), rows, part="c")
    rows = []
    for x in xs(100):
        T, y = bubble(x, "benzene", "toluene", -2.0)
        rows.append((x, T - K0, y))
    write_table(__file__, ("x", "T", "y"), rows, part="d")
    rows = []
    for t in range(70, 101):
        T = K0 + t
        rows.append((t, psat("toluene", T), psat("water", T), psat("toluene", T) + psat("water", T)))
    write_table(__file__, ("t", "ptol", "pwat", "psum"), rows, part="e")
    path, n = staircase()
    write_table(__file__, ("x", "y"), path, part="f")
    write_table(__file__, ("x", "y"), [(x, bubble(x, "benzene", "toluene")[1]) for x in xs()], part="f-eq")
