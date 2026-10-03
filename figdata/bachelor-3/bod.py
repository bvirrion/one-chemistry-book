"""Ch. 32, oxygen demand. Part a: first-order BOD curve BOD_t = L0 (1 - e^(-k t))
for a model sewage, L0 = 250 mg/L, k = 0.23 per day. Part b: Streeter-Phelps
oxygen sag below an outfall, deficit D(t) = k1 L0/(k2 - k1) (e^(-k1 t) -
e^(-k2 t)) + D0 e^(-k2 t), with river L0 = 10 mg/L, k1 = 0.23/d, k2 = 0.50/d,
D0 = 1.0 mg/L, saturation 9.1 mg/L (model values); dissolved O2 = 9.1 - D."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

L0, K = 250.0, 0.23
R_L0, K1, K2, D0, SAT = 10.0, 0.23, 0.50, 1.0, 9.1


def bod(t):
    return L0 * (1 - math.exp(-K * t))


def deficit(t):
    return K1 * R_L0 / (K2 - K1) * (math.exp(-K1 * t) - math.exp(-K2 * t)) + D0 * math.exp(-K2 * t)


def t_critical():
    return math.log((K2 / K1) * (1 - D0 * (K2 - K1) / (K1 * R_L0))) / (K2 - K1)


if __name__ == "__main__":
    write_table(__file__, ("t", "bod"), [(0.2 * j, bod(0.2 * j)) for j in range(0, 151)])
    write_table(__file__, ("t", "O2"), [(0.1 * j, SAT - deficit(0.1 * j)) for j in range(0, 151)], part="b")
    tc = t_critical()
    print(bod(5), tc, SAT - deficit(tc))
