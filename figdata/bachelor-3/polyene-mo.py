"""Ch. 26, Hückel molecular orbitals of linear polyenes (ethene N = 2,
allyl N = 3, butadiene N = 4, hexatriene N = 6): coefficients
c_jk = sqrt(2/(N + 1)) sin(j k pi/(N + 1)) on atom j of orbital k (k = 1 the
lowest), energies alpha + 2 beta cos(k pi/(N + 1)). The chapter's lobe drawings
use these coefficients (rounded to two decimals). Symmetry of orbital k of the
s-cis polyene: under the mirror plane sigma perpendicular to the chain axis,
symmetric when k is odd; under the C2 axis, symmetric when k is even."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

NS = (2, 3, 4, 6)


def coeffs(n, k):
    return [math.sqrt(2 / (n + 1)) * math.sin(j * k * math.pi / (n + 1)) for j in range(1, n + 1)]


def energy_x(n, k):
    """E = alpha + x beta."""
    return 2 * math.cos(k * math.pi / (n + 1))


def nodes(c):
    return sum(1 for a, b in zip(c, c[1:]) if a * b < 0)


def mirror_parity(c):
    """+1 if c_j = c_(n+1-j) (symmetric under sigma), -1 if antisymmetric."""
    if all(abs(a - b) < 1e-12 for a, b in zip(c, reversed(c))):
        return 1
    if all(abs(a + b) < 1e-12 for a, b in zip(c, reversed(c))):
        return -1
    return 0


def c2_parity(c):
    """The p lobes of the termini are exchanged with a change of sign by C2
    (the axis lies in the plane of the polyene): parity = -mirror parity."""
    return -mirror_parity(c)


if __name__ == "__main__":
    rows = []
    for n in NS:
        for k in range(1, n + 1):
            for j, c in enumerate(coeffs(n, k), start=1):
                rows.append((n, k, j, c, energy_x(n, k)))
    write_table(__file__, ("N", "k", "j", "c", "x"), rows, digits=4)
    for n in (4, 6):
        for k in range(1, n + 1):
            print(n, k, [round(c, 3) for c in coeffs(n, k)], "sigma", mirror_parity(coeffs(n, k)), "C2", c2_parity(coeffs(n, k)))
