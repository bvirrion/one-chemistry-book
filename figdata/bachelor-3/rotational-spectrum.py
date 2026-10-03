"""Ch. 6, (a) the pure rotational absorption spectrum of 12C16O at 30 K and
300 K: lines at 2 B0 (J + 1) (B0 = Be - alpha_e/2, centrifugal distortion
neglected), relative intensities taken as the population of the lower level,
(2J + 1) exp(-hcB0 J(J+1)/kT), each spectrum scaled to its strongest line;
(b) the rotational Raman spectrum of 14N2 at 300 K: Stokes and anti-Stokes
lines at 4B0 (J + 3/2) from the exciting line, nuclear-spin weights 6 (even
J) and 3 (odd J) giving the 2:1 alternation."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402


def c2():
    """second radiation constant hc/k in cm K"""
    return 100 * value("const:h") * value("const:c") / value("const:kB")


def b0(mol):
    return value("diat:%s.Be" % mol) - value("diat:%s.ae" % mol) / 2


def line(J, mol="CO"):
    """absorption J+1 <- J, in cm-1"""
    return 2 * b0(mol) * (J + 1)


def population(J, T, mol="CO"):
    return (2 * J + 1) * math.exp(-c2() * b0(mol) * J * (J + 1) / T)


def jmax(T, mol="CO"):
    return math.sqrt(T / (2 * c2() * b0(mol))) - 0.5


def raman_shift(J, mol="N2"):
    """Stokes line J+2 <- J, shift from the exciting line, cm-1"""
    return 4 * b0(mol) * (J + 1.5)


def nuclear_weight(J):
    return 6 if J % 2 == 0 else 3


def raman_intensity(J, T=300):
    return nuclear_weight(J) * population(J, T, "N2")


if __name__ == "__main__":
    for T, part in ((30, "co-30"), (300, "co-300")):
        top = max(population(J, T) for J in range(60))
        write_table(__file__, ("nu", "I"), [(line(J), population(J, T) / top) for J in range(40)], part=part)
    top = max(raman_intensity(J) for J in range(40))
    rows = [(raman_shift(J), raman_intensity(J) / top) for J in range(25)]
    rows += [(-raman_shift(J), 0.9 * raman_intensity(J) / top) for J in range(25)]
    write_table(__file__, ("shift", "I"), sorted(rows), part="n2-raman")
