"""Esterification and hydrolysis reaching the same equilibrium (grade 12).

SYNTHETIC kinetics, real equilibrium: acid + alcohol <=> ester + water with
rate = kf [acid][alcohol] - kb [ester][water], kf/kb = K = 4 (ledger
ester:berthelot: two thirds esterified from an equimolar start). Amounts
in mol for 1 mol of each starting species, in a constant volume taken as
1 L; time in hours, kf chosen for the picture.
  columns: t, ester formed from acid + alcohol, ester left from ester + water
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table

K = 4.0
KF = 0.06            # L/(mol.h), invented
KB = KF / K


def rate(e):
    """d(ester)/dt for 1 mol acid + 1 mol alcohol initially, e mol ester present."""
    return KF * (1 - e) ** 2 - KB * e ** 2


def run(e0, tmax=200.0, dt=0.05):
    out, e, t = [(0.0, e0)], e0, 0.0
    n = int(round(tmax / dt))
    for i in range(1, n + 1):
        k1 = rate(e); k2 = rate(e + dt * k1 / 2); k3 = rate(e + dt * k2 / 2); k4 = rate(e + dt * k3)
        e += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t = i * dt
        if i % 20 == 0:
            out.append((round(t, 2), e))
    return out


def table():
    a = run(0.0)
    b = run(1.0)    # 1 mol ester + 1 mol water: same as e = 1 in the acid frame
    return [(ta, round(ea, 4), round(eb, 4)) for (ta, ea), (_, eb) in zip(a, b)]


def final_extent(acid, alcohol, k=K):
    """Root in [0, min] of x^2 = k (acid - x)(alcohol - x)."""
    a = k - 1.0
    b = -k * (acid + alcohol)
    c = k * acid * alcohol
    d = (b * b - 4 * a * c) ** 0.5
    return (-b - d) / (2 * a)


if __name__ == "__main__":
    write_table(__file__, ("t", "fromAcid", "fromEster"), table(), digits=6)
