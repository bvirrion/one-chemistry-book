"""Ch. 13, chemical oscillators. (a) The Brusselator, dX/dt = A - (B+1)X +
X^2 Y, dY/dt = B X - X^2 Y, with A = 1 and B = 3 (beyond the Hopf boundary
B = 1 + A^2): time series and the approach to the limit cycle from two
starting points. (b) Lotka-Volterra, dx/dt = x(a - b y), dy/dt = y(d x - c),
a = b = c = d = 1: three closed orbits on which V = d x - c ln x + b y -
a ln y is conserved. Reduced (dimensionless) variables."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ode import rk4  # noqa: E402

A, B = 1.0, 3.0


def brusselator(t, y, a=A, b=B):
    x, w = y
    return [a - (b + 1) * x + x * x * w, b * x - x * x * w]


def lv(t, y):
    x, w = y
    return [x * (1 - w), w * (x - 1)]


def lv_invariant(x, w):
    return x - math.log(x) + w - math.log(w)


def jacobian_eigs(a, b):
    """eigenvalues of the Brusselator Jacobian at its steady state (A, B/A)"""
    tr = b - 1 - a * a
    det = a * a
    disc = tr * tr - 4 * det
    if disc >= 0:
        r = math.sqrt(disc)
        return complex((tr + r) / 2), complex((tr - r) / 2)
    r = math.sqrt(-disc)
    return complex(tr / 2, r / 2), complex(tr / 2, -r / 2)


def period(sol):
    """period from successive maxima of X (late part of the run)"""
    xs = [(t, y[0]) for t, y in sol]
    peaks = [xs[i][0] for i in range(1, len(xs) - 1) if xs[i][1] > xs[i - 1][1] and xs[i][1] >= xs[i + 1][1]]
    late = peaks[len(peaks) // 2:]
    return (late[-1] - late[0]) / (len(late) - 1)


def runs():
    ts = rk4(brusselator, [1.0, 1.0], 0, 40, 0.005, every=10)
    inner = rk4(brusselator, [1.2, 3.0], 0, 40, 0.005, every=10)
    outer = rk4(brusselator, [0.3, 5.0], 0, 40, 0.005, every=10)
    orbits = [rk4(lv, [x0, 1.0], 0, 20, 0.002, every=10) for x0 in (0.5, 0.3, 0.2)]
    return ts, inner, outer, orbits


if __name__ == "__main__":
    ts, inner, outer, orbits = runs()
    write_table(__file__, ("t", "X", "Y"), [(t, y[0], y[1]) for t, y in ts], part="series")
    write_table(__file__, ("X", "Y"), [tuple(y) for _, y in inner], part="inner")
    write_table(__file__, ("X", "Y"), [tuple(y) for _, y in outer], part="outer")
    for k, o in enumerate(orbits):
        write_table(__file__, ("x", "y"), [tuple(y) for _, y in o], part="lv%d" % (k + 1))
    print("period", period(ts), "eigs B=3", jacobian_eigs(A, B), "B=1.5", jacobian_eigs(A, 1.5))
