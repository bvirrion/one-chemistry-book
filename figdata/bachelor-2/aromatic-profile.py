"""Energy profiles for an electrophile meeting benzene (chapter 22). A MODEL:
smooth curves built from Gaussians, energies in arbitrary units, to show the
shape (two transition states around the Wheland intermediate; the second
step either loses a proton, restoring the aromatic ring, or adds a
nucleophile, which would leave a non-aromatic product higher in energy)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402


SUB = [(0, 0.0), (1, 10.0), (2, 6.0), (3, 7.5), (4, -4.0)]
ADD = [(0, 0.0), (1, 10.0), (2, 6.0), (3, 9.5), (4, 2.0)]


def through(points, x):
    """Smooth curve through the given extrema (zero slope at each point)."""
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        if x0 <= x <= x1:
            t = (x - x0) / (x1 - x0)
            return y0 + (y1 - y0) * (1 - math.cos(math.pi * t)) / 2
    return points[-1][1]


def substitution(x):
    return through(SUB, x)


def addition(x):
    return through(ADD, x)


if __name__ == "__main__":
    xs = [k * 0.02 for k in range(0, 201)]
    write_table(__file__, ("x", "sub", "add"), [(x, substitution(x), addition(x)) for x in xs])
