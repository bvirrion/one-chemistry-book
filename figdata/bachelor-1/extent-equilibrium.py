"""Reaction quotient as a function of the extent (ch. 7).

Part a: the water-gas shift CO + H2O = CO2 + H2 from 1 mol CO, 2 mol H2O,
3 mol H2 (the weekend problem), K = 4.0 (data of the problem).
Part b: CaCO3(s) = CaO(s) + CO2(g) in a closed 10.0 L vessel at 1100 K,
K = 0.20 (data of the exercise), for two initial amounts of CaCO3.
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

K_SHIFT = 4.0
K_CARB, V, T, P0 = 0.20, 10.0e-3, 1100.0, 1.0e5


def q_shift(xi):
    return xi * (3 + xi) / ((1 - xi) * (2 - xi))


def xi_eq_shift(K=K_SHIFT):
    # xi(3 + xi) = K (1 - xi)(2 - xi)  ->  (K - 1) xi^2 - (3K + 3) xi + 2K = 0
    a, b, c = K - 1, -(3 * K + 3), 2 * K
    return (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)


def q_carbonate(xi, n0):
    """Q = p(CO2)/p0 for an extent xi (mol), capped when the carbonate is gone."""
    xi = min(xi, n0)
    return xi * value("const:R") * T / (V * P0)


def xi_eq_carbonate(n0):
    """Equilibrium extent, or None if the solid disappears first."""
    xi = K_CARB * V * P0 / (value("const:R") * T)
    return xi if xi < n0 else None


if __name__ == "__main__":
    rows = [(x / 100, q_shift(x / 100)) for x in range(1, 99)]
    write_table(__file__, ("xi", "Q"), rows, part="shift")
    # the larger sample stops at equilibrium: Q stays at K beyond xi_eq
    rows = [(x / 1000, q_carbonate(x / 1000, 0.010), min(q_carbonate(x / 1000, 0.050), K_CARB))
            for x in range(0, 41)]
    write_table(__file__, ("xi", "Q_small", "Q_large"), rows, part="carbonate")
