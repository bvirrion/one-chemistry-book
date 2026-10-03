"""Ch. 16, rates of surface reactions (model constants in reduced units):
Langmuir-Hinshelwood r = k K_A p_A K_B p_B / (1 + K_A p_A + K_B p_B)^2 against
p_A for three values of p_B (K_A = K_B = 1, k = 1), and Eley-Rideal
r = k K_A p_A p_B / (1 + K_A p_A) for p_B = 1."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402

KA, KB, K = 1.0, 1.0, 1.0


def lh(pa, pb):
    return K * KA * pa * KB * pb / (1 + KA * pa + KB * pb) ** 2


def er(pa, pb):
    return K * KA * pa * pb / (1 + KA * pa)


def pa_max(pb):
    return (1 + KB * pb) / KA


if __name__ == "__main__":
    write_table(__file__, ("pA", "pB05", "pB1", "pB3", "ER"),
                [(0.05 * i, lh(0.05 * i, 0.5), lh(0.05 * i, 1), lh(0.05 * i, 3), er(0.05 * i, 1) / 4) for i in range(0, 201)])
