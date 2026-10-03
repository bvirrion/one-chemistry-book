"""Consecutive first-order reactions A -> B -> C (ch. 9), a0 = 1:
a = exp(-k1 t), b = k1/(k2 - k1) (exp(-k1 t) - exp(-k2 t)), c = 1 - a - b,
and the steady-state approximation b_ss = k1 a / k2."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402


def abc(t, k1, k2):
    a = math.exp(-k1 * t)
    b = k1 / (k2 - k1) * (math.exp(-k1 * t) - math.exp(-k2 * t))
    return a, b, 1 - a - b


def t_max(k1, k2):
    return math.log(k2 / k1) / (k2 - k1)


def b_ss(t, k1, k2):
    return k1 * math.exp(-k1 * t) / k2


if __name__ == "__main__":
    for name, k2 in (("slow", 0.5), ("fast", 20.0)):
        rows = []
        for i in range(0, 121):
            t = i * 0.05
            a, b, c = abc(t, 1.0, k2)
            rows.append((t, a, b, c, b_ss(t, 1.0, k2)))
        write_table(__file__, ("t", "a", "b", "c", "bss"), rows, part=name)
