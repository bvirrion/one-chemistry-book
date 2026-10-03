"""Ch. 28, enantioselectivity and energy. For two competing diastereomeric
transition states with equal prefactors, er = exp(ddG/RT) and
ee = (er - 1)/(er + 1). Part a: ee against ddG at -78, 0 and 25 C. Part b:
a chiral HPLC chromatogram synthesised from two Gaussian peaks (retention 8.2
and 9.1 min, standard deviation 0.12 min, areas 97.5 and 2.5, ee 95 %)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

R = value("const:R")
TS = (195.15, 273.15, 298.15)
PEAKS = ((8.2, 97.5), (9.1, 2.5))
SIG = 0.12


def ee_from_ddg(ddg_kj, T):
    er = math.exp(ddg_kj * 1000 / (R * T))
    return (er - 1) / (er + 1)


def ddg_for_ee(ee, T):
    return R * T * math.log((1 + ee) / (1 - ee)) / 1000


def signal(t):
    return sum(A / (SIG * math.sqrt(2 * math.pi)) * math.exp(-((t - t0) ** 2) / (2 * SIG ** 2)) for t0, A in PEAKS)


def areas(dt=0.001):
    a1 = sum(signal(7.0 + j * dt) for j in range(int(1.65 / dt))) * dt   # 7.0-8.65
    a2 = sum(signal(8.65 + j * dt) for j in range(int(1.35 / dt))) * dt  # 8.65-10.0
    return a1, a2


if __name__ == "__main__":
    rows = [(0.2 * j,) + tuple(ee_from_ddg(0.2 * j, T) for T in TS) for j in range(0, 101)]
    write_table(__file__, ("ddg", "eeA", "eeB", "eeC"), rows)
    write_table(__file__, ("t", "y"), [(7.5 + 0.005 * j, signal(7.5 + 0.005 * j)) for j in range(0, 401)], part="b")
    a1, a2 = areas()
    print(ddg_for_ee(0.95, 298.15), (a1 - a2) / (a1 + a2))
