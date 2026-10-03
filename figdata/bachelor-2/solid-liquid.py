"""Binary solid-liquid diagrams (chapter 8), ideal models.
- a: copper-nickel, ideal solid and liquid solutions (the lens): for each T,
  the nickel mole fractions of the solid (solidus) and liquid (liquidus) from
  x_i(l)/x_i(s) = exp[-DfusH_i/R (1/T - 1/T_i)];
- b: benzene-naphthalene, pure solids and an ideal liquid (Schroder-van
  Laar): the two liquidus branches and their eutectic;
- d: bismuth-tin, the same ideal-liquid model, in mass % Bi, to compare with
  the assessed eutectic (NIST, 138.8 degC, 56.97 % Bi).
Melting points and enthalpies of fusion from the ledger (tfus:, dfus:)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

R = value("const:R")
K0 = 273.15


def tm(sp):
    return value("tfus:%s" % sp)


def dh(sp):
    return value("dfus:%s" % sp) * 1000.0


def ideal_x(sp, T):
    """Mole fraction of sp in an ideal liquid in equilibrium with pure solid sp."""
    return math.exp(-dh(sp) / R * (1 / T - 1 / tm(sp)))


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


def eutectic(a, b):
    """(T_e, x_b): ideal-liquid eutectic of two pure solids a and b."""
    T = solve(lambda T: ideal_x(a, T) + ideal_x(b, T) - 1, 50, min(tm(a), tm(b)) - 1e-6)
    return T, ideal_x(b, T)


def lens(T, a="Cu", b="Ni"):
    """(x_b solid, x_b liquid) at T for ideal solid and liquid solutions."""
    ka = math.exp(-dh(a) / R * (1 / T - 1 / tm(a)))   # x_a(l)/x_a(s)
    kb = math.exp(-dh(b) / R * (1 / T - 1 / tm(b)))
    # x_a(s) + x_b(s) = 1 and ka x_a(s) + kb x_b(s) = 1
    xs = (1 - ka) / (kb - ka)
    return xs, kb * xs


def mass_fraction(x_b, a, b):
    ma, mb = value("aw:%s" % a), value("aw:%s" % b)
    return x_b * mb / (x_b * mb + (1 - x_b) * ma)


def mole_fraction(w_b, a, b):
    ma, mb = value("aw:%s" % a), value("aw:%s" % b)
    return (w_b / mb) / (w_b / mb + (1 - w_b) / ma)


if __name__ == "__main__":
    rows = []
    Ta, Tb = tm("Cu"), tm("Ni")
    for i in range(61):
        T = Ta + (Tb - Ta) * i / 60
        xs, xl = lens(T)
        rows.append((T - K0, xs, xl))
    write_table(__file__, ("T", "xs", "xl"), rows, part="a")
    Te, xe = eutectic("benzene", "naphthalene")
    rows = []
    for i in range(41):  # benzene branch, x = naphthalene mole fraction
        T = tm("benzene") + (Te - tm("benzene")) * i / 40
        rows.append((1 - ideal_x("benzene", T), T - K0))
    write_table(__file__, ("x", "T"), rows, part="b-benzene")
    rows = []
    for i in range(41):
        T = tm("naphthalene") + (Te - tm("naphthalene")) * i / 40
        rows.append((ideal_x("naphthalene", T), T - K0))
    write_table(__file__, ("x", "T"), rows, part="b-naphthalene")
    Te2, xbi = eutectic("Sn", "Bi")
    rows = []
    for i in range(41):  # Sn branch, w = mass % Bi
        T = tm("Sn") + (Te2 - tm("Sn")) * i / 40
        rows.append((100 * mass_fraction(1 - ideal_x("Sn", T), "Sn", "Bi"), T - K0))
    write_table(__file__, ("w", "T"), rows, part="d-Sn")
    rows = []
    for i in range(41):
        T = tm("Bi") + (Te2 - tm("Bi")) * i / 40
        rows.append((100 * mass_fraction(ideal_x("Bi", T), "Sn", "Bi"), T - K0))
    write_table(__file__, ("w", "T"), rows, part="d-Bi")
