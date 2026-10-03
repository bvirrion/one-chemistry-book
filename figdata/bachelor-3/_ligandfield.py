"""d^n ions in an octahedral field: full diagonalisation of the ligand-field
and electron-repulsion Hamiltonian over Slater determinants (complex d
orbitals m = -2..2, Condon-Shortley phases), with Racah parameters B and C.
Used for the Tanabe-Sugano diagrams of Book 4, ch. 18.

One-electron octahedral potential (z along a C4 axis), in units of Dq:
<+-2|V|+-2> = 1, <+-1|V|+-1> = -4, <0|V|0> = 6, <2|V|-2> = <-2|V|2> = 5,
whose eigenvalues are 6 Dq (e_g, twice) and -4 Dq (t_2g, three times).
Two-electron integrals <m1 m2|1/r12|m3 m4> = sum_k c^k(m1,m3) c^k(m4,m2) F^k
with F^0 = A + 49F4 (A plays no role in the spectra), F^2 = 49(B + 5F4),
F^4 = 441 F4, F4 = C/35."""
import itertools
import math

import numpy as np


def _fact(n):
    return math.factorial(n)


def three_j(j1, j2, j3, m1, m2, m3):
    if m1 + m2 + m3 != 0 or j3 > j1 + j2 or j3 < abs(j1 - j2):
        return 0.0
    if abs(m1) > j1 or abs(m2) > j2 or abs(m3) > j3:
        return 0.0
    t = (_fact(j1 + j2 - j3) * _fact(j1 - j2 + j3) * _fact(-j1 + j2 + j3) / _fact(j1 + j2 + j3 + 1))
    pre = math.sqrt(t * _fact(j1 + m1) * _fact(j1 - m1) * _fact(j2 + m2) * _fact(j2 - m2)
                    * _fact(j3 + m3) * _fact(j3 - m3))
    s = 0.0
    for k in range(0, 2 * (j1 + j2 + j3) + 1):
        a = [k, j1 + j2 - j3 - k, j1 - m1 - k, j2 + m2 - k, j3 - j2 + m1 + k, j3 - j1 - m2 + k]
        if min(a) < 0:
            continue
        s += (-1) ** k / math.prod(_fact(x) for x in a)
    return (-1) ** (j1 - j2 - m3) * pre * s


def ck(k, m, mp, l=2):
    """Gaunt coefficient c^k(l m, l m')"""
    return (-1) ** m * (2 * l + 1) * three_j(l, k, l, 0, 0, 0) * three_j(l, k, l, -m, m - mp, mp)


MS = (-2, -1, 0, 1, 2)
ORB = [(m, s) for m in MS for s in (1, -1)]          # spin-orbitals: (m_l, 2 m_s)


def v_lf(m, mp):
    if m == mp:
        return {2: 1, -2: 1, 1: -4, -1: -4, 0: 6}[m]
    if {m, mp} == {2, -2}:
        return 5
    return 0


def two_e(m1, m2, m3, m4, F):
    if m1 + m2 != m3 + m4:
        return 0.0
    return sum(ck(k, m1, m3) * ck(k, m4, m2) * F[k] for k in (0, 2, 4))


def hamiltonian(n, dq, B, C, two_ms=None):
    """matrix over the determinants of n electrons (optionally with fixed 2 M_S)"""
    F4 = C / 35
    F = {0: 0.0, 2: 49 * (B + 5 * F4), 4: 441 * F4}
    dets = [d for d in itertools.combinations(range(10), n)
            if two_ms is None or sum(ORB[i][1] for i in d) == two_ms]
    idx = {d: i for i, d in enumerate(dets)}
    N = len(dets)
    Hm = np.zeros((N, N))
    # one-electron part
    for a, d in enumerate(dets):
        for p_pos, p in enumerate(d):
            mp, sp = ORB[p]
            for q in range(10):
                mq, sq = ORB[q]
                if sq != sp:
                    continue
                v = v_lf(mq, mp)
                if v == 0:
                    continue
                if q != p and q in d:
                    continue
                new = list(d)
                new[p_pos] = q
                sign = 1
                # sort and count transpositions
                arr = new[:]
                for i in range(len(arr)):
                    for j in range(len(arr) - 1 - i):
                        if arr[j] > arr[j + 1]:
                            arr[j], arr[j + 1] = arr[j + 1], arr[j]
                            sign = -sign
                b = idx.get(tuple(arr))
                if b is not None:
                    Hm[b, a] += sign * v * dq
    # two-electron part: a+_r a+_s a_q a_p with <rs|pq>
    for a, d in enumerate(dets):
        for (ip, p), (iq, q) in itertools.combinations(enumerate(d), 2):
            mp, sp = ORB[p]
            mq, sq = ORB[q]
            rest = [x for x in d if x not in (p, q)]
            for r, s in itertools.combinations(range(10), 2):
                if r in rest or s in rest:
                    continue
                mr, sr = ORB[r]
                ms_, ss = ORB[s]
                val = 0.0
                if sr == sp and ss == sq:
                    val += two_e(mr, ms_, mp, mq, F)
                if sr == sq and ss == sp:
                    val -= two_e(mr, ms_, mq, mp, F)
                if val == 0:
                    continue
                # remove p, q (sign of moving them to the front), add r, s
                arr = [p, q] + rest
                sign1 = _perm_sign(list(d), arr)
                new = [r, s] + rest
                srt = sorted(new)
                sign2 = _perm_sign(srt, new)
                b = idx.get(tuple(srt))
                if b is not None:
                    Hm[b, a] += sign1 * sign2 * val
    return Hm, dets


def _perm_sign(target, arr):
    """sign of the permutation taking target order to arr order"""
    pos = [target.index(x) for x in arr]
    sign = 1
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            if pos[i] > pos[j]:
                sign = -sign
    return sign


def s2_matrix(dets):
    """<S^2> over the determinants (in units of hbar^2)"""
    idx = {d: i for i, d in enumerate(dets)}
    N = len(dets)
    S2 = np.zeros((N, N))
    for a, d in enumerate(dets):
        ms = sum(ORB[i][1] for i in d) / 2
        S2[a, a] += ms * ms + ms        # S^2 = S- S+ + Sz^2 + Sz
        # S- S+: raise one beta electron to alpha, then lower one alpha to beta
        for p in d:
            if ORB[p][1] != -1:
                continue
            up = ORB.index((ORB[p][0], 1))
            if up in d:
                continue
            lst1 = [up if x == p else x for x in d]
            new1 = sorted(lst1)
            s1 = _perm_sign(new1, lst1)
            for q in new1:
                if ORB[q][1] != 1:
                    continue
                dn = ORB.index((ORB[q][0], -1))
                if dn in new1:
                    continue
                lst = [dn if x == q else x for x in new1]
                new2 = sorted(lst)
                s2 = _perm_sign(new2, lst)
                b = idx.get(tuple(new2))
                if b is not None:
                    S2[b, a] += s1 * s2
    return S2


def levels(n, delta, B, C, two_ms=None):
    """energies (sorted) for Delta = 10 Dq"""
    Hm, dets = hamiltonian(n, delta / 10, B, C, two_ms)
    return np.linalg.eigvalsh(Hm), Hm, dets


def spectrum_with_spin(n, delta, B, C):
    """(energy, S) of all states with M_S = lowest |M_S| (contains every S)"""
    two_ms = n % 2
    Hm, dets = hamiltonian(n, delta / 10, B, C, two_ms)
    S2 = s2_matrix(dets)
    w, v = np.linalg.eigh(Hm)
    s2 = np.einsum('ij,jk,ki->i', v.T, S2, v)
    S = [(-1 + math.sqrt(1 + 4 * max(x, 0))) / 2 for x in s2]
    return list(zip(w, S))
