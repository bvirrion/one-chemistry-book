"""Ch. 1, the particle in a box: wavefunctions psi_n and densities for
n = 1..4 (x in units of L, energies in units of E_1), and the free-electron
model of three symmetric cyanine dyes (absorption maxima from the ledger):
a chain of j atoms (5, 7, 9) between the two nitrogens carries N = j + 1
pi electrons; the box is (j - 1) bonds of length l plus an extension delta
at each end, delta fitted on the middle dye."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

DYES = (("cyanine", 5, "uvvis:cyanine"), ("carbocyanine", 7, "uvvis:carbocyanine"),
        ("dicarbocyanine", 9, "uvvis:dicarbocyanine"))


def psi(n, x):
    """normalised on [0, 1] (box of unit length)"""
    return math.sqrt(2) * math.sin(n * math.pi * x)


def energy_ratio(n):
    return n * n


def norm(n, m, steps=4000):
    h = 1 / steps
    return sum(psi(n, (i + 0.5) * h) * psi(m, (i + 0.5) * h) for i in range(steps)) * h


def nodes(n, steps=4000):
    vals = [psi(n, (i + 0.5) / steps) for i in range(steps)]
    return sum(1 for a, b in zip(vals, vals[1:]) if a * b < 0)


def bond():
    return value("geo:C6H6.rCC") * 1e-10        # m, an aromatic C-C bond


def wavelength(j, delta):
    """lambda (m) of the HOMO->LUMO transition, N = j + 1 electrons"""
    n_el = j + 1
    L = (j - 1) * bond() + 2 * delta
    return 8 * value("const:me") * value("const:c") * L ** 2 / (value("const:h") * (n_el + 1))


def fitted_delta():
    """delta (m) that reproduces the middle dye exactly"""
    j, lam = 7, value("uvvis:carbocyanine") * 1e-9
    n_el = j + 1
    L = math.sqrt(lam * value("const:h") * (n_el + 1) / (8 * value("const:me") * value("const:c")))
    return (L - (j - 1) * bond()) / 2


if __name__ == "__main__":
    rows = []
    for i in range(201):
        x = i / 200
        rows.append([x] + [energy_ratio(n) + 0.9 * psi(n, x) for n in (1, 2, 3, 4)]
                    + [energy_ratio(n) + 0.9 * psi(n, x) ** 2 for n in (1, 2, 3, 4)])
    write_table(__file__, ("x", "p1", "p2", "p3", "p4", "d1", "d2", "d3", "d4"), rows)
    d = fitted_delta()
    write_table(__file__, ("j", "measured", "bare", "fitted"),
                [(j, value(k), wavelength(j, 0) * 1e9, wavelength(j, d) * 1e9) for _, j, k in DYES],
                part="dyes")
