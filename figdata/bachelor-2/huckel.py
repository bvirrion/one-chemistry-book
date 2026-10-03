"""Hueckel theory (chapter 16). Energies E = alpha + m beta (beta < 0), plotted
as e = (E - alpha)/|beta| = -m, so that bonding levels are below zero.
- a: levels of ethene, allyl, butadiene, hexatriene (chains) and of
  cyclobutadiene, benzene (rings), from the eigenvalues of the adjacency
  matrix, with their occupation for the neutral molecules;
- b: HOMO-LUMO gap of linear polyenes C_nH_(n+2), n even, in units of |beta|;
- e: the coefficients of the four pi orbitals of butadiene;
- c (chapter 17, a MODEL with the usual textbook heteroatom parameters
  alpha_X = alpha + h beta, beta_CX = k beta): HOMO coefficients of
  1-methoxybutadiene (O: h = 2.0, k = 0.8) and LUMO coefficients of propenal
  (O: h = 1.0, k = 1.0), and those of butadiene and ethene for comparison.
- d: propenal LUMO coefficients and pi charges (chapter 26)."""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402


def adjacency(n, ring=False):
    A = np.zeros((n, n))
    for i in range(n - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    if ring and n > 2:
        A[0, n - 1] = A[n - 1, 0] = 1
    return A


def huckel(n, ring=False):
    """Eigenvalues m (E = alpha + m beta) in decreasing order (most bonding
    first) and the matching coefficient vectors (columns)."""
    w, v = np.linalg.eigh(adjacency(n, ring))
    order = np.argsort(-w)
    return w[order], v[:, order]


def hetero(n_c, hetero_at, h, k, ring=False):
    """Chain of n_c carbons plus one heteroatom bonded to carbon hetero_at
    (index 0-based); returns (m sorted decreasing, vectors); the heteroatom is
    the last index."""
    n = n_c + 1
    A = np.zeros((n, n))
    A[:n_c, :n_c] = adjacency(n_c, ring)
    A[n_c, n_c] = h
    A[n_c, hetero_at] = A[hetero_at, n_c] = k
    w, v = np.linalg.eigh(A)
    order = np.argsort(-w)
    return w[order], v[:, order]


def frontier(m, v, electrons):
    """(HOMO index, LUMO index) for a closed shell of `electrons`."""
    homo = electrons // 2 - 1
    return homo, homo + 1


def methoxybutadiene_homo():
    m, v = hetero(4, 0, 2.0, 0.8)
    homo, _ = frontier(m, v, 6)
    c = v[:, homo]
    return m[homo], c * (1 if c[3] > 0 else -1)


def propenal_charges():
    """pi charges of propenal (C3=C2-C1=O; atoms 0,1,2 = beta, alpha, carbonyl
    carbon, 3 = O): q = (pi electrons the atom brings, 1) - sum over the two
    occupied orbitals of 2 c^2."""
    m, v = hetero(3, 2, 1.0, 1.0)
    occ = v[:, :2]
    pop = 2 * (occ ** 2).sum(axis=1)
    return 1 - pop


def propenal_lumo():
    m, v = hetero(3, 2, 1.0, 1.0)
    _, lumo = frontier(m, v, 4)
    c = v[:, lumo]
    return m[lumo], c * (1 if c[0] > 0 else -1)


def chain_closed_form(n):
    return sorted((2 * math.cos(k * math.pi / (n + 1)) for k in range(1, n + 1)), reverse=True)


def ring_closed_form(n):
    return sorted((2 * math.cos(2 * math.pi * k / n) for k in range(n)), reverse=True)


def pi_energy(n, electrons, ring=False):
    """Sum of m over the occupied levels (E_pi = electrons*alpha + this*beta)."""
    m, _ = huckel(n, ring)
    total, left = 0.0, electrons
    for mk in m:
        take = min(2, left)
        total += take * mk
        left -= take
        if left == 0:
            break
    return total


def gap(n):
    return 4 * math.sin(math.pi / (2 * (n + 1)))


SYSTEMS = [("ethene", 2, False), ("allyl", 3, False), ("butadiene", 4, False),
           ("hexatriene", 6, False), ("cyclobutadiene", 4, True), ("benzene", 6, True)]

if __name__ == "__main__":
    rows = []
    for col, (name, n, ring) in enumerate(SYSTEMS):
        m, _ = huckel(n, ring)
        # group degenerate levels: x offset within the column
        groups = {}
        for mk in m:
            key = round(mk, 6)
            groups.setdefault(key, 0)
            groups[key] += 1
        for key, deg in groups.items():
            for d in range(deg):
                x = col * 2.0 + (d - (deg - 1) / 2) * 0.7
                rows.append((x, -key + 0.0))
    write_table(__file__, ("x", "e"), rows, part="a")
    write_table(__file__, ("n", "gap"), [(n, gap(n)) for n in range(2, 22, 2)], part="b")
    e1, c1 = methoxybutadiene_homo()
    e2, c2 = propenal_lumo()
    rows = [(j + 1, c1[j]) for j in range(4)] + [(0, c1[4])]
    write_table(__file__, ("atom", "c"), rows, part="c-diene")
    rows = [(j + 1, c2[j]) for j in range(3)] + [(4, c2[3])]
    write_table(__file__, ("atom", "c"), rows, part="c-dienophile")
    q = propenal_charges()
    rows = [(j + 1, c2[j], q[j]) for j in range(4)]
    write_table(__file__, ("atom", "c", "q"), rows, part="d")
    m, v = huckel(4)
    rows = [(j + 1,) + tuple(v[j, k] * (1 if v[0, k] > 0 else -1) for k in range(4)) for j in range(4)]
    write_table(__file__, ("atom", "psi1", "psi2", "psi3", "psi4"), rows, part="e")
