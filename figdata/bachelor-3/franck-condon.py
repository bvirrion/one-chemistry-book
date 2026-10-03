"""Ch. 7, the Franck-Condon principle for two harmonic potential curves of
the same frequency displaced by Delta (reduced units): the Franck-Condon
factors from v'' = 0 are Poisson, |<v'|0>|^2 = exp(-S) S^v'/v'!, with
S = Delta^2/2 the Huang-Rhys factor. Writes the two curves, a stick
progression for S = 0.3, 1.5 and 5, and the I2 B <- X estimate of S."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402


def fc(v, S):
    return math.exp(-S) * S ** v / math.factorial(v)


def overlap_numeric(v, delta, steps=6000, a=-10.0, b=14.0):
    """<v'|0''> by quadrature with Hermite functions, to check the formula"""
    H = [lambda y: 1.0, lambda y: 2 * y, lambda y: 4 * y * y - 2, lambda y: 8 * y ** 3 - 12 * y]

    def psi(n, y):
        return H[n](y) * math.exp(-y * y / 2) / math.sqrt(2 ** n * math.factorial(n) * math.sqrt(math.pi))
    h = (b - a) / steps
    return sum(psi(v, a + (i + .5) * h - delta) * psi(0, a + (i + .5) * h) for i in range(steps)) * h


def huang_rhys_I2():
    mu = value("imass:I127") / 2 * value("const:u")
    w = 2 * math.pi * value("const:c") * 100 * value("diat:I2B.we")
    dR = (value("diat:I2B.re") - value("diat:I2.re")) * 1e-10
    hbar = value("const:h") / (2 * math.pi)
    return mu * w * dR ** 2 / (2 * hbar)


if __name__ == "__main__":
    ys = [-4 + 0.05 * i for i in range(201)]
    D = math.sqrt(2 * 1.5)
    write_table(__file__, ("y", "ground", "excited"),
                [(y, 0.5 * y * y, 9 + 0.5 * (y - D) ** 2) for y in ys], part="curves")
    rows = [(v, fc(v, 0.3), fc(v, 1.5), fc(v, 5.0)) for v in range(13)]
    write_table(__file__, ("v", "s03", "s15", "s5"), rows, part="sticks")
