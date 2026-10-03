"""Ch. 19, ligand-field activation energies of a dissociative substitution
(octahedron -> square pyramid) in the simplest sigma-only ligand-field model:
each ligand raises a d orbital by e_sigma times the square of the orbital's
angular amplitude in its direction (normalised so that d_z2 and d_x2-y2 get 1
from a ligand on their lobe axis): an axial ligand gives d_z2 1; an equatorial
one gives d_z2 1/4 and d_x2-y2 3/4; the t_2g orbitals get nothing. The
ligand-field stabilisation of n electrons is E - (n/5) sum(levels); the
activation energy is the loss of stabilisation, in units of Dq (Delta_o =
3 e_sigma = 10 Dq)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402

OH = {"xy": 0, "xz": 0, "yz": 0, "z2": 2 * 1 + 4 * 0.25, "x2y2": 4 * 0.75}
SP = {"xy": 0, "xz": 0, "yz": 0, "z2": 1 * 1 + 4 * 0.25, "x2y2": 4 * 0.75}


def fill(levels, n, high_spin):
    """total d-electron energy (units of e_sigma): Aufbau, with Hund's rule
    across the whole set (high spin) or pairing in the lowest levels first
    (low spin, for the octahedron: fill t2g with 6 before e_g)"""
    order = sorted(levels.values())
    if high_spin:
        # one electron in each orbital first (lowest first), then pair from the lowest
        occ = [1 if k < n else 0 for k in range(5)]
        for k in range(max(0, n - 5)):
            occ[k] += 1
        return sum(o * e for o, e in zip(occ, order))
    e = 0.0
    left = n
    for lev in order:
        take = min(2, left)
        e += take * lev
        left -= take
    return e


def lfse(levels, n, high_spin):
    return fill(levels, n, high_spin) - n / 5 * sum(levels.values())


def lfae_dq(n, high_spin=True):
    """activation energy (Dq) of Oh -> square pyramid"""
    es = lfse(SP, n, high_spin) - lfse(OH, n, high_spin)
    return es * 10 / 3


if __name__ == "__main__":
    rows = [(n, lfae_dq(n, True), lfae_dq(n, False) if 4 <= n <= 7 else float("nan")) for n in range(11)]
    write_table(__file__, ("n", "hs", "ls"), rows)
    for r in rows:
        print(r)
