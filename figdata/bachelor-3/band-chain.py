"""Ch. 22, from orbitals to bands. Hückel levels of a linear chain of N
identical atoms (alpha, beta < 0): E_k = alpha + 2 beta cos(k pi/(N + 1)),
k = 1..N, written as (E - alpha)/|beta| = -2 cos(k pi/(N + 1)) for
N = 2, 4, 8, 16, 64 (column positions 1..5), and the density of states of
the infinite chain per atom, g(e) = 1/(pi sqrt(4 - e^2)) in units of
1/|beta| (part b). The band spans 4|beta|."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

NS = (2, 4, 8, 16, 64)


def levels(n):
    """(E - alpha)/|beta|, lowest first (beta < 0)."""
    return sorted(-2 * math.cos(k * math.pi / (n + 1)) for k in range(1, n + 1))


def huckel_matrix_levels(n):
    """Independent check: eigenvalues of the tridiagonal Hückel matrix in
    units of |beta| (alpha = 0, beta = -1), by the Sturm count bisection."""
    def count_below(x):
        c, d = 0, 1.0
        for i in range(n):
            d = (0 - x) - (1.0 / d if i else 0.0) if d != 0 else (0 - x) - 1e300
            if d < 0:
                c += 1
        return c
    out = []
    for k in range(1, n + 1):
        lo, hi = -2.0, 2.0
        for _ in range(80):
            mid = (lo + hi) / 2
            if count_below(mid) >= k:
                hi = mid
            else:
                lo = mid
        out.append((lo + hi) / 2)
    return out


def dos(e):
    return 1 / (math.pi * math.sqrt(4 - e * e))


if __name__ == "__main__":
    write_table(__file__, ("col", "e"),
                [(i + 1, e) for i, n in enumerate(NS) for e in levels(n)])
    es = [-1.995 + 3.99 * j / 200 for j in range(201)]
    write_table(__file__, ("e", "g"), [(e, dos(e)) for e in es], part="b")
    print([round(x, 4) for x in levels(2)], levels(64)[0], levels(64)[-1])
