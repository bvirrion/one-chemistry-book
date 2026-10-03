"""Minimal Hartree-Fock machinery for s-type contracted Gaussians on two
centres (used by minimal-basis-hf.py). Integral formulas for normalised
primitive Gaussians exp(-a r^2), the Boys function F0 through math.erf;
restricted closed-shell SCF with symmetric orthogonalisation (numpy)."""
import math

import numpy as np


def boys0(t):
    if t < 1e-12:
        return 1.0 - t / 3
    return 0.5 * math.sqrt(math.pi / t) * math.erf(math.sqrt(t))


def norm(a):
    return (2 * a / math.pi) ** 0.75


def prim_s(a, b, r2):
    p = a + b
    return norm(a) * norm(b) * (math.pi / p) ** 1.5 * math.exp(-a * b / p * r2)


def prim_t(a, b, r2):
    p = a + b
    return a * b / p * (3 - 2 * a * b / p * r2) * prim_s(a, b, r2)


def prim_v(a, b, A, B, C, Z):
    p = a + b
    P = (a * A + b * B) / p
    r2 = (A - B) ** 2
    return (-2 * math.pi / p * Z * math.exp(-a * b / p * r2) * boys0(p * (P - C) ** 2)
            * norm(a) * norm(b))


def prim_eri(a, b, c, d, A, B, C, D):
    p, q = a + b, c + d
    P, Q = (a * A + b * B) / p, (c * C + d * D) / q
    return (2 * math.pi ** 2.5 / (p * q * math.sqrt(p + q))
            * math.exp(-a * b / p * (A - B) ** 2 - c * d / q * (C - D) ** 2)
            * boys0(p * q / (p + q) * (P - Q) ** 2)
            * norm(a) * norm(b) * norm(c) * norm(d))


def contracted(basis):
    """basis: list of (centre x, [(alpha, coef), ...]) on a line"""
    return basis


def integrals(basis, nuclei):
    n = len(basis)
    S, T, V = (np.zeros((n, n)) for _ in range(3))
    G = np.zeros((n, n, n, n))
    for i, (A, pi) in enumerate(basis):
        for j, (B, pj) in enumerate(basis):
            r2 = (A - B) ** 2
            for a, ca in pi:
                for b, cb in pj:
                    S[i, j] += ca * cb * prim_s(a, b, r2)
                    T[i, j] += ca * cb * prim_t(a, b, r2)
                    for C, Z in nuclei:
                        V[i, j] += ca * cb * prim_v(a, b, A, B, C, Z)
    for i, (A, pi) in enumerate(basis):
        for j, (B, pj) in enumerate(basis):
            for k, (C, pk) in enumerate(basis):
                for m, (D, pm) in enumerate(basis):
                    G[i, j, k, m] = sum(ca * cb * cc * cd * prim_eri(a, b, c, d, A, B, C, D)
                                        for a, ca in pi for b, cb in pj
                                        for c, cc in pk for d, cd in pm)
    return S, T, V, G


def rhf(basis, nuclei, n_el=2, iterations=60, tol=1e-10):
    """returns (total energy, orbital energies, history of total energies)"""
    S, T, V, G = integrals(basis, nuclei)
    H = T + V
    w, U = np.linalg.eigh(S)
    X = U @ np.diag(w ** -0.5) @ U.T
    P = np.zeros_like(S)
    enuc = sum(Z1 * Z2 / abs(C1 - C2) for i, (C1, Z1) in enumerate(nuclei)
               for (C2, Z2) in nuclei[i + 1:])
    hist, e_old = [], 0.0
    for _ in range(iterations):
        F = H + np.einsum("kl,ijlk->ij", P, G) - 0.5 * np.einsum("kl,iklj->ij", P, G)
        eps, Cp = np.linalg.eigh(X.T @ F @ X)
        C = X @ Cp
        occ = C[:, : n_el // 2]
        P = 2 * occ @ occ.T
        Fp = H + np.einsum("kl,ijlk->ij", P, G) - 0.5 * np.einsum("kl,iklj->ij", P, G)
        e = 0.5 * np.sum(P * (H + Fp)) + enuc      # energy of the new determinant
        hist.append(e)
        if abs(e - e_old) < tol:
            break
        e_old = e
    return e, eps, hist, S
