"""Energy profiles drawn through given stationary points (chs. 9, 19, 25).

Between two consecutive stationary points (x_i, E_i) the curve is
E = E_i + (E_{i+1} - E_i) (1 - cos(pi u)) / 2, u = (x - x_i)/(x_{i+1} - x_i):
the slope is zero at every stationary point and the curve is monotonic in
between, so the minima and maxima are exactly the points given. Energies in
kJ/mol, illustrative (no real reaction is implied).
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

PROFILES = {
    "one-step": [(0, 0), (5, 80), (10, -40)],
    "two-step": [(0, 0), (3, 70), (5, 30), (7, 55), (10, -40)],
    "uncatalysed": [(0, 0), (5, 100), (10, -30)],
    "catalysed": [(0, 0), (3, 55), (5, 20), (7, 50), (10, -30)],
    "sn2": [(0, 0), (5, 90), (10, -20)],
    "sn1": [(0, 0), (3.5, 95), (5, 70), (6.5, 80), (10, -20)],
    "primary": [(0, 0), (4, 110), (5, 85), (6, 95), (10, -30)],
    "secondary": [(0, 0), (4, 75), (5, 45), (6, 55), (10, -35)],
}


def energy(points, x):
    for (x0, e0), (x1, e1) in zip(points, points[1:]):
        if x0 <= x <= x1:
            u = (x - x0) / (x1 - x0)
            return e0 + (e1 - e0) * (1 - math.cos(math.pi * u)) / 2
    raise ValueError(x)


def curve(name, n=201):
    pts = PROFILES[name]
    return [(10 * i / (n - 1), energy(pts, 10 * i / (n - 1))) for i in range(n)]


if __name__ == "__main__":
    for name in PROFILES:
        write_table(__file__, ("x", "E"), curve(name), part=name)
