"""Ch. 13, the Lindemann-Hinshelwood fall-off curve k_uni = k1 k2 [M] /
(km1 [M] + k2) against [M], with model constants (not a measured system):
k1 = 1e3 L mol-1 s-1 (activation), km1 = 1e9 L mol-1 s-1 (deactivation),
k2 = 1e3 s-1 (reaction of the energised molecule). High-pressure limit
k_inf = k1 k2 / km1 = 1e-3 s-1; low-pressure limit k1 [M]; half-way at
[M]_1/2 = k2 / km1 = 1e-6 mol/L."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402

K1, KM1, K2 = 1.0e3, 1.0e9, 1.0e3   # L mol-1 s-1, L mol-1 s-1, s-1 (model)


def k_uni(m):
    return K1 * K2 * m / (KM1 * m + K2)


def k_inf():
    return K1 * K2 / KM1


def m_half():
    return K2 / KM1


def rows():
    return [(10 ** e, k_uni(10 ** e), min(K1 * 10 ** e, 10), k_inf())
            for e in [-10 + 0.05 * i for i in range(161)]]


if __name__ == "__main__":
    write_table(__file__, ("M", "k", "low", "high"), rows())
