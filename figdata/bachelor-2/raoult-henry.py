"""Partial and total vapour pressures over a binary liquid mixture at fixed
T: (a) an ideal mixture (Raoult's law for both components); (b) a model
non-ideal mixture with positive deviation, activity coefficients from the
one-parameter Margules model ln g1 = A x2^2, ln g2 = A x1^2. Pressures are in
units of p1* (the pure component 1); the model parameters are those of the
figure, not data for a real pair."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

P1, P2 = 1.0, 0.55      # pure vapour pressures (model units)
A = 1.1                 # Margules parameter (model)


def gammas(x1, a=A):
    x2 = 1.0 - x1
    return math.exp(a * x2 * x2), math.exp(a * x1 * x1)


def pressures(x1, a=A):
    g1, g2 = gammas(x1, a)
    p1 = x1 * g1 * P1
    p2 = (1.0 - x1) * g2 * P2
    return p1, p2, p1 + p2


def henry_constant_1(a=A):
    """Limit of p1/x1 as x1 -> 0: k_H = p1* exp(A)."""
    return P1 * math.exp(a)


def curve(a):
    rows = []
    for k in range(101):
        x1 = k / 100.0
        p1, p2, p = pressures(x1, a)
        rows.append((x1, p1, p2, p))
    return rows


if __name__ == "__main__":
    write_table(__file__, ("x1", "p1", "p2", "p"), curve(0.0), part="ideal")
    write_table(__file__, ("x1", "p1", "p2", "p"), curve(A), part="margules")
