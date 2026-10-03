"""Ch. 10, partition functions against temperature: the exact rigid-rotor
sum for H35Cl against the high-temperature form T/theta_r (and its first
correction T/theta_r + 1/3), and the vibrational partition function (levels
from the zero-point level) of N2, Cl2 and I2 from 50 to 3000 K."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _statmech import theta_rot, theta_vib, q_rot_exact, q_rot_high, q_vib  # noqa: E402


def rot_rows():
    th = theta_rot("HCl")
    rows = []
    for i in range(0, 121):
        T = 2.5 * i if i else 1.0
        rows.append((T, q_rot_exact(th, T), q_rot_high(th, T), q_rot_high(th, T) + 1 / 3))
    return rows


def vib_rows():
    ths = [theta_vib(n) for n in ("N2", "Cl2", "I2")]
    rows = []
    for i in range(0, 296):
        T = 50 + 10 * i
        rows.append((T,) + tuple(q_vib(th, T) for th in ths))
    return rows


if __name__ == "__main__":
    write_table(__file__, ("T", "exact", "high", "corr"), rot_rows(), part="rot")
    write_table(__file__, ("T", "N2", "Cl2", "I2"), vib_rows(), part="vib")
