"""Hydrogen-like orbitals and Slater's rules (chapter 13).
r in units of a0, Z = 1 unless stated. Radial functions R_nl (n <= 3) in
units of (Z/a0)^(3/2):
- a: radial distribution functions P(r) = r^2 R^2 of 1s, 2s, 2p, 3s, 3p, 3d;
- b: R_2s and R_3s, which change sign at their radial nodes;
- c: dot-density pictures of 1s and 2s in a plane through the nucleus,
  deterministic (Halton) sampling of the in-plane density r |psi|^2;
- d: Slater effective charge Z* and Slater radius n*^2 a0/Z* of the valence
  orbital along period 2 (Li to Ne) and down group 1 (Li to Cs).
Slater's rules: J. C. Slater, Phys. Rev. 36, 57 (1930); a model."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

S3, S6, S30 = math.sqrt(3), math.sqrt(6), math.sqrt(30)


def R(n, l, r, Z=1.0):
    p = Z * r
    k = Z ** 1.5
    if (n, l) == (1, 0):
        return k * 2 * math.exp(-p)
    if (n, l) == (2, 0):
        return k / (2 * math.sqrt(2)) * (2 - p) * math.exp(-p / 2)
    if (n, l) == (2, 1):
        return k / (2 * S6) * p * math.exp(-p / 2)
    if (n, l) == (3, 0):
        return k * 2 / (81 * S3) * (27 - 18 * p + 2 * p * p) * math.exp(-p / 3)
    if (n, l) == (3, 1):
        return k * 4 / (81 * S6) * (6 * p - p * p) * math.exp(-p / 3)
    if (n, l) == (3, 2):
        return k * 4 / (81 * S30) * p * p * math.exp(-p / 3)
    raise ValueError((n, l))


def P(n, l, r, Z=1.0):
    return r * r * R(n, l, r, Z) ** 2


def integrate(f, a, b, steps=20000):
    h = (b - a) / steps
    s = f(a) + f(b)
    for k in range(1, steps):
        s += (4 if k % 2 else 2) * f(a + k * h)
    return s * h / 3


def most_probable(n, l, lo=0.01, hi=40.0):
    """Largest maximum of P (golden-section search near the outer peak)."""
    xs = [lo + (hi - lo) * k / 4000 for k in range(4001)]
    best = max(xs, key=lambda r: P(n, l, r))
    return best


def outside_probability_1s(r0):
    """P(r > r0) for 1s, exact: e^(-2 r0) (1 + 2 r0 + 2 r0^2)."""
    return math.exp(-2 * r0) * (1 + 2 * r0 + 2 * r0 * r0)


def halton(i, b):
    f, r = 1.0, 0.0
    while i > 0:
        f /= b
        r += f * (i % b)
        i //= b
    return r


def dots(n, l, count=1500, rmax=None):
    """Points (x, y) in a plane through the nucleus distributed as
    |psi_n00|^2 (s orbitals): in-plane radial density r R^2, inverse CDF."""
    rmax = rmax or (6 if n == 1 else 14)
    grid = [rmax * k / 2000 for k in range(2001)]
    w = [r * R(n, l, r) ** 2 for r in grid]
    cdf = [0.0]
    for k in range(1, len(grid)):
        cdf.append(cdf[-1] + (w[k] + w[k - 1]) / 2)
    tot = cdf[-1]
    pts = []
    for i in range(1, count + 1):
        u = halton(i, 2) * tot
        lo, hi = 0, len(cdf) - 1
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if cdf[mid] < u:
                lo = mid
            else:
                hi = mid
        r = grid[hi]
        a = 2 * math.pi * halton(i, 3)
        pts.append((r * math.cos(a), r * math.sin(a)))
    return pts


# Slater's rules for the valence s/p electron of main-group atoms
PERIOD2 = ["Li", "Be", "B", "C", "N", "O", "F", "Ne"]
GROUP1 = [("Li", 3, 2), ("Na", 11, 3), ("K", 19, 4), ("Rb", 37, 5), ("Cs", 55, 6)]
NSTAR = {1: 1.0, 2: 2.0, 3: 3.0, 4: 3.7, 5: 4.0, 6: 4.2}


def zstar_period2(k):
    """k = 1..8 valence electrons in n = 2 (Li..Ne)."""
    Z = 2 + k
    return Z - 2 * 0.85 - (k - 1) * 0.35


def zstar_alkali(Z, n):
    """ns1 alkali: 8 electrons in shell n-1 (s, p) at 0.85, all others 1.00
    (for n = 2: the 1s pair at 0.85)."""
    if n == 2:
        return Z - 2 * 0.85
    return Z - 8 * 0.85 - (Z - 9) * 1.0


def slater_radius(zs, n):
    return NSTAR[n] ** 2 / zs


def slater_energy_ev(zs, n):
    return -value("const:RyhcEV") * zs ** 2 / NSTAR[n] ** 2


def slater_ie_2p(k):
    """First ionisation energy of a period-2 atom with k valence electrons, as
    the difference of the total (2s, 2p) group energies of ion and atom."""
    zs_atom = zstar_period2(k)
    zs_ion = 2 + k - 2 * 0.85 - (k - 2) * 0.35
    e_atom = k * slater_energy_ev(zs_atom, 2)
    e_ion = (k - 1) * slater_energy_ev(zs_ion, 2)
    return e_ion - e_atom


if __name__ == "__main__":
    rows = []
    for k in range(0, 601):
        r = k * 0.04
        rows.append((r, P(1, 0, r), P(2, 0, r), P(2, 1, r), P(3, 0, r), P(3, 1, r), P(3, 2, r)))
    write_table(__file__, ("r", "s1", "s2", "p2", "s3", "p3", "d3"), rows, part="a")
    rows = []
    for k in range(0, 501):
        r = k * 0.04
        rows.append((r, R(2, 0, r), R(3, 0, r)))
    write_table(__file__, ("r", "R2s", "R3s"), rows, part="b")
    write_table(__file__, ("x", "y"), dots(1, 0), part="c-1s", digits=4)
    write_table(__file__, ("x", "y"), dots(2, 0, count=2500), part="c-2s", digits=4)
    rows = [(k, zstar_period2(k), slater_radius(zstar_period2(k), 2)) for k in range(1, 9)]
    write_table(__file__, ("k", "zs", "r"), rows, part="d-period")
    rows = [(n, zstar_alkali(Z, n), slater_radius(zstar_alkali(Z, n), n)) for _, Z, n in GROUP1]
    write_table(__file__, ("n", "zs", "r"), rows, part="d-group")
