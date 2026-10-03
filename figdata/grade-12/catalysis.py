"""Catalysis (grade 12): energy profiles and oxygen evolution. SYNTHETIC.

part a: reaction coordinate s in [0, 1]; energy without catalyst (one
        barrier) and with catalyst (two smaller barriers through an
        intermediate); same start (0) and end (-50) levels, arbitrary
        kJ/mol scale.
part b: t (min) and volume of dioxygen (mL) given off by 10 mL of
        hydrogen peroxide solution, without and with catalyst: same final
        volume, first-order approach with k ten times larger with catalyst.
"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table

END = -50.0


def baseline(s):
    """Smooth step from 0 to END."""
    return END * (3 * s * s - 2 * s ** 3)


def bump(s, centre, height, width):
    return height * math.exp(-((s - centre) / width) ** 2)


def uncatalysed(s):
    return baseline(s) + bump(s, 0.5, 100.0, 0.16)


def catalysed(s):
    return baseline(s) + bump(s, 0.3, 55.0, 0.10) + bump(s, 0.7, 52.0, 0.10) - bump(s, 0.5, 6.0, 0.08)


VMAX = 72.0                 # mL of O2
K_SLOW, K_FAST = 0.02, 0.2  # 1/min


def volume(t, k):
    return VMAX * (1 - math.exp(-k * t))


def profiles(n=200):
    return [(round(i / n, 4), round(uncatalysed(i / n), 3), round(catalysed(i / n), 3))
            for i in range(n + 1)]


def evolution(tmax=60, step=0.5):
    return [(round(i * step, 2), round(volume(i * step, K_SLOW), 3), round(volume(i * step, K_FAST), 3))
            for i in range(int(tmax / step) + 1)]


if __name__ == "__main__":
    write_table(__file__, ("s", "Eu", "Ec"), profiles(), part="a", digits=6)
    write_table(__file__, ("t", "Vu", "Vc"), evolution(), part="b", digits=6)
