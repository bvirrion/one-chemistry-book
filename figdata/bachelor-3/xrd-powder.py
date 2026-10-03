"""Ch. 9, powder X-ray diffraction patterns (Cu K alpha 1) of cubic crystals
from their ledger lattice parameters: positions by Bragg's law; intensities
|F|^2 x multiplicity x Lorentz-polarisation factor, with the simplification
f = number of electrons of each ion or atom (no fall-off with angle, no
thermal factor) -- enough to show which reflections are absent and which are
strong. (a) NaCl and KCl (rock salt, F lattice); (b) Cu (F) and W (I);
(c) Scherrer broadening of one line for crystallites of 10, 50, 200 nm."""
import itertools
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

ELECTRONS = {"Na+": 10, "K+": 18, "Cl-": 18, "Br-": 36, "Cu": 29, "W": 74}
STRUCT = {
    "NaCl": ("lat:NaCl", "rocksalt", ("Na+", "Cl-")),
    "KCl": ("lat:KCl", "rocksalt", ("K+", "Cl-")),
    "KBr": ("lat:KBr", "rocksalt", ("K+", "Br-")),
    "Cu": ("lat:Cu", "fcc", ("Cu",)),
    "W": ("lat:W", "bcc", ("W",)),
}


def lam():
    return value("xray:CuKa1")


def structure_factor(name, h, k, l):
    _, kind, ions = STRUCT[name]
    if kind == "fcc" or kind == "rocksalt":
        centring = 1 + (-1) ** (h + k) + (-1) ** (h + l) + (-1) ** (k + l)   # 4 or 0
        if kind == "fcc":
            return centring * ELECTRONS[ions[0]]
        return centring * (ELECTRONS[ions[0]] + ELECTRONS[ions[1]] * (-1) ** (h + k + l))
    if kind == "bcc":
        return (1 + (-1) ** (h + k + l)) * ELECTRONS[ions[0]]
    raise ValueError(kind)


def two_theta(name, h, k, l):
    a = value(STRUCT[name][0])
    d = a / math.sqrt(h * h + k * k + l * l)
    s = lam() / (2 * d)
    return None if s >= 1 else 2 * math.degrees(math.asin(s))


def reflections(name, tt_max=100.0):
    """list of (N = h2+k2+l2, 2theta, relative intensity) for the families present"""
    fam = {}
    for h, k, l in itertools.product(range(0, 9), repeat=3):
        if (h, k, l) == (0, 0, 0) or not (h >= k >= l):
            continue
        tt = two_theta(name, h, k, l)
        if tt is None or tt > tt_max:
            continue
        F = structure_factor(name, h, k, l)
        mult = len({(sh * a, sk * b, sl * c) for a, b, c in set(itertools.permutations((h, k, l)))
                    for sh in (1, -1) for sk in (1, -1) for sl in (1, -1)})
        th = math.radians(tt / 2)
        lp = (1 + math.cos(2 * th) ** 2) / (math.sin(th) ** 2 * math.cos(th))
        N = h * h + k * k + l * l
        fam.setdefault(N, [tt, 0.0, (h, k, l)])
        fam[N][1] += abs(F) ** 2 * mult * lp
    top = max(v[1] for v in fam.values()) or 1
    return sorted((N, v[0], v[1] / top, v[2]) for N, v in fam.items())


def pattern(name, x, width=0.15):
    return sum(I * math.exp(-((x - tt) / width) ** 2 / 2) for _, tt, I, _ in reflections(name))


def scherrer_fwhm(L_nm, tt_deg, K=0.9):
    """FWHM in degrees 2theta for crystallites of size L"""
    th = math.radians(tt_deg / 2)
    return math.degrees(K * lam() * 1e-10 / (L_nm * 1e-9 * math.cos(th)))


if __name__ == "__main__":
    for part, names, x0, n in (("salts", ("NaCl", "KCl"), 20, 3501), ("metals", ("Cu", "W"), 35, 3251)):
        xs = [x0 + 0.02 * i for i in range(n)]
        write_table(__file__, ("tt",) + names, [(x,) + tuple(pattern(n, x) for n in names) for x in xs], part=part)
    tt0 = two_theta("NaCl", 2, 0, 0)
    rows = []
    for i in range(401):
        x = tt0 - 4 + 0.02 * i
        rows.append((x,) + tuple(math.exp(-4 * math.log(2) * ((x - tt0) / scherrer_fwhm(L, tt0)) ** 2)
                                 for L in (10, 50, 200)))
    write_table(__file__, ("tt", "L10", "L50", "L200"), rows, part="scherrer")
    for n in ("KCl",):
        for N, tt, I, hkl in reflections(n):
            print(n, N, hkl, round(tt, 3), round(I, 4))
