"""Integrated rate laws of orders 0, 1 and 2 for A -> products,
v = -d[A]/dt = k[A]^n, with [A]0 = 1.00 mol/L and the same initial rate
k0 = k1*a0 = k2*a0^2 = 0.050 (mol/L)/min (ch. 8)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

A0, V0 = 1.00, 0.050


def conc(order, t, a0=A0, v0=V0):
    k = v0 / a0 ** order
    if order == 0:
        return max(a0 - k * t, 0.0)
    if order == 1:
        return a0 * math.exp(-k * t)
    if order == 2:
        return 1 / (1 / a0 + k * t)
    raise ValueError(order)


def half_life(order, a0=A0, v0=V0):
    k = v0 / a0 ** order
    return {0: a0 / (2 * k), 1: math.log(2) / k, 2: 1 / (k * a0)}[order]


if __name__ == "__main__":
    rows = []
    for i in range(0, 61):
        t = i
        c0, c1, c2 = conc(0, t), conc(1, t), conc(2, t)
        rows.append((t, c0, c1, c2, math.log(c1), 1 / c2))
    write_table(__file__, ("t", "A0", "A1", "A2", "lnA1", "invA2"), rows)
