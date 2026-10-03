"""Ch. 1, the harmonic oscillator in reduced units y = x / sqrt(hbar/(m omega)):
V = y^2/2, levels v + 1/2 (units hbar omega), Hermite functions psi_0..psi_3
drawn at their levels, classical turning points y = +-sqrt(2v + 1)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

HERMITE = (lambda y: 1.0, lambda y: 2 * y, lambda y: 4 * y * y - 2,
           lambda y: 8 * y ** 3 - 12 * y)


def psi(v, y):
    c = 1 / math.sqrt(2 ** v * math.factorial(v) * math.sqrt(math.pi))
    return c * HERMITE[v](y) * math.exp(-y * y / 2)


def level(v):
    return v + 0.5


def turning(v):
    return math.sqrt(2 * v + 1)


def integral(f, a=-8, b=8, steps=8000):
    h = (b - a) / steps
    return sum(f(a + (i + 0.5) * h) for i in range(steps)) * h


if __name__ == "__main__":
    rows = []
    for i in range(241):
        y = -4.0 + i / 30
        rows.append([y, y * y / 2] + [level(v) + 0.75 * psi(v, y) for v in range(4)])
    write_table(__file__, ("y", "V", "p0", "p1", "p2", "p3"), rows)
