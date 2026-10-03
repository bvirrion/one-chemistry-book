"""Torsional energy of ethane and butane against the dihedral angle (ch. 16),
from the experimental Fourier coefficients in the ledger (CCCBDB):
    V(theta) = sum_n Vn/2 (1 - cos n(theta - 180 deg))
for butane (theta = 0: methyls eclipsed, 180: anti), and
    V(theta) = V3/2 (1 + cos 3 theta) for ethane (theta = 0: eclipsed).
Energies in kJ/mol (1 cm-1 = h c N_A)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

CM1 = value("const:h") * value("const:c") * 100 * value("const:NA") / 1000   # kJ/mol per cm-1


def butane(theta_deg):
    phi = math.radians(theta_deg - 180)
    v = sum(value("rot:butane-V%d" % n) / 2 * (1 - math.cos(n * phi)) for n in range(1, 7))
    return v * CM1


def ethane(theta_deg):
    return value("rot:ethane-V3") / 2 * (1 + math.cos(3 * math.radians(theta_deg))) * CM1


def gauche_minimum():
    best = min(range(30000, 90001), key=lambda k: butane(k / 1000))
    return best / 1000, butane(best / 1000)


if __name__ == "__main__":
    write_table(__file__, ("theta", "butane", "ethane"),
                [(t, butane(t), ethane(t)) for t in range(0, 361, 2)])
