"""Ch. 8, relaxation curves (model values): inversion recovery
M_z(t) = M0 (1 - 2 exp(-t/T1)) with T1 = 2.0 s, and the transverse decay
M_xy(t) = M0 exp(-t/T2) with T2 = 0.5 s."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

T1, T2 = 2.0, 0.5


def mz(t):
    return 1 - 2 * math.exp(-t / T1)


def mxy(t):
    return math.exp(-t / T2)


def null_time():
    return T1 * math.log(2)


if __name__ == "__main__":
    write_table(__file__, ("t", "mz", "mxy"), [(0.05 * i, mz(0.05 * i), mxy(0.05 * i)) for i in range(201)])
