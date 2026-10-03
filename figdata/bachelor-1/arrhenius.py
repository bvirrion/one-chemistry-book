"""Arrhenius plot of the degradation of a medicine (weekend problem of ch. 8):
rate constants measured at 40, 50 and 60 degC (data of the problem), the
line through the 40 and 60 degC points, ln k = ln A - Ea/(R T)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

DATA = ((40.0, 0.00127), (50.0, 0.00348), (60.0, 0.0090))   # degC, 1/day


def kelvin(c):
    return c + 273.15


def slope():
    (t1, k1), (t3, k3) = DATA[0], DATA[2]
    return (math.log(k3) - math.log(k1)) / (1 / kelvin(t3) - 1 / kelvin(t1))


def activation_energy():
    return -slope() * value("const:R")


def k_at(c):
    t3, k3 = DATA[2]
    return k3 * math.exp(slope() * (1 / kelvin(c) - 1 / kelvin(t3)))


if __name__ == "__main__":
    write_table(__file__, ("invT_1e3", "lnk"),
                [(1000 / kelvin(c), math.log(k)) for c, k in DATA], part="points")
    write_table(__file__, ("invT_1e3", "lnk"),
                [(1000 / kelvin(c), math.log(k_at(c))) for c in (20, 25, 30, 40, 50, 60, 65)],
                part="line")
