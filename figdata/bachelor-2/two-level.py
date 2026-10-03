"""Two interacting levels (chapter 14, reused in chapter 17).
Orbitals of energies alpha_A = abar + Delta/2 and alpha_B = abar - Delta/2
coupled by beta < 0, overlap neglected: E+- = abar -+ sqrt(Delta^2/4 + beta^2)
(E- bonding, below). In units of |beta| with abar = 0:
- a: exact E against Delta/|beta|, with the perturbative limits
  +-(Delta/2 + beta^2/Delta) valid for Delta >> |beta|, and the bonding
  orbital's weight on the lower atom."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402


def levels(delta, beta=-1.0):
    s = math.sqrt(delta * delta / 4 + beta * beta)
    return -s, s


def weight_lower(delta, beta=-1.0):
    """Fraction c_B^2 of the bonding orbital on the lower atom B."""
    e, _ = levels(delta, beta)
    # (alpha_B - E) c_B + beta c_A = 0 with alpha_B = -delta/2
    a = -delta / 2
    if abs(beta) < 1e-15:
        return 1.0
    ratio = (e - a) / beta          # c_A / c_B
    return 1 / (1 + ratio * ratio)


def perturbative(delta, beta=-1.0):
    return -(delta / 2 + beta * beta / delta), delta / 2 + beta * beta / delta


if __name__ == "__main__":
    rows = []
    for k in range(0, 161):
        d = k * 0.05
        lo, hi = levels(d)
        rows.append((d, lo, hi, d / 2, -d / 2, weight_lower(d)))
    write_table(__file__, ("d", "Elow", "Ehigh", "aA", "aB", "wB"), rows, part="a")
    rows = []
    for k in range(30, 161):
        d = k * 0.05
        lo, hi = perturbative(d)
        rows.append((d, lo, hi))
    write_table(__file__, ("d", "Plow", "Phigh"), rows, part="a-pert")
