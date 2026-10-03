"""Ch. 7, photophysics of a model molecule (model values, not a real
compound): absorption and fluorescence bands built as vibronic progressions
(0-0 at 25000 cm-1, vibrational quantum 1400 cm-1, Huang-Rhys S = 1,
Gaussian lines of 450 cm-1 standard deviation): mirror images about the
0-0 line. Fluorescence decays with a dynamic quencher (tau0 = 10 ns,
kq = 5e9 L/mol/s) and the Stern-Volmer line I0/I = 1 + kq tau0 [Q]."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

E00, VIB, S, SIG = 25000.0, 1400.0, 1.0, 450.0
TAU0, KQ = 10e-9, 5e9


def fc(v):
    return math.exp(-S) * S ** v / math.factorial(v)


def band(x, sign):
    """sign +1: absorption (lines above E00), -1: emission (below)"""
    return sum(fc(v) * math.exp(-((x - (E00 + sign * v * VIB)) / SIG) ** 2 / 2) for v in range(8))


def tau(q):
    return TAU0 / (1 + KQ * TAU0 * q)


def stern_volmer(q):
    return 1 + KQ * TAU0 * q


if __name__ == "__main__":
    xs = [17000 + 20 * i for i in range(801)]
    top = max(band(x, 1) for x in xs)
    write_table(__file__, ("nu", "abs", "em"), [(x / 1000, band(x, 1) / top, band(x, -1) / top) for x in xs], part="bands")
    rows = []
    for i in range(201):
        t = i * 0.25e-9
        rows.append((t * 1e9,) + tuple(math.exp(-t / tau(q)) for q in (0, 0.01, 0.02, 0.04)))
    write_table(__file__, ("t", "q0", "q1", "q2", "q4"), rows, part="decays")
    write_table(__file__, ("Q", "I0I"), [(q / 1000, stern_volmer(q / 1000)) for q in range(0, 45, 5)], part="sv")
