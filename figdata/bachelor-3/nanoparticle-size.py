"""Ch. 23, size effects. Part a: cuboctahedral ("magic") clusters of n
shells around one atom, N(n) = (10n^3 + 15n^2 + 11n + 3)/3 atoms of which
10n^2 + 2 on the surface; the surface fraction against the cluster diameter
(2n + 1) d for gold, d = a/sqrt(2) the nearest-neighbour distance of the fcc
metal (ledger lat:Au). Part b: confinement energy of an electron-hole pair in
a spherical quantum dot of radius R, particle-in-a-sphere ground state
h^2/(8 mu R^2), for a model reduced mass mu = 0.10 m_e (Coulomb attraction
neglected)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

MU = 0.10


def n_atoms(n):
    return (10 * n ** 3 + 15 * n ** 2 + 11 * n + 3) // 3


def n_surface(n):
    return 10 * n * n + 2 if n > 0 else 1


def n_atoms_by_shells(n):
    return 1 + sum(10 * k * k + 2 for k in range(1, n + 1))


def d_au_nm():
    return value("lat:Au") / math.sqrt(2) / 10


def confinement_eV(r_nm, mu=MU):
    h, me, e = value("const:h"), value("const:me"), value("const:e")
    return h * h / (8 * mu * me * (r_nm * 1e-9) ** 2) / e


if __name__ == "__main__":
    d = d_au_nm()
    write_table(__file__, ("n", "N", "diam_nm", "fsurf"),
                [(n, n_atoms(n), (2 * n + 1) * d, n_surface(n) / n_atoms(n)) for n in range(1, 31)])
    write_table(__file__, ("R_nm", "dE_eV"),
                [(r / 20, confinement_eV(r / 20)) for r in range(16, 121)], part="b")
    print(n_atoms(1), n_atoms(2), n_atoms(8), n_surface(8) / n_atoms(8), confinement_eV(2.0), confinement_eV(3.0))
