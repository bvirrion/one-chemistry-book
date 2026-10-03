"""Ch. 13, the H2 + Br2 chain mechanism integrated numerically (model rate
constants in reduced units, chosen for the figure: initiation Br2 -> 2 Br,
k1 = 1e-4; termination 2 Br -> Br2, km1 = 100; propagation Br + H2 -> HBr + H,
k2 = 1, and H + Br2 -> HBr + Br, k3 = 100; inhibition H + HBr -> H2 + Br,
k4 = 10), against the steady-state rate law
v = 2 k2 (k1/km1)^(1/2) [H2][Br2]^(1/2) / (1 + (k4/k3)[HBr]/[Br2])."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ode import rk4  # noqa: E402

K1, KM1, K2, K3, K4 = 1e-4, 100.0, 1.0, 100.0, 10.0


def rhs(t, y):
    h2, br2, hbr, br, h = y
    r1, rm1 = K1 * br2, KM1 * br * br
    r2, r3, r4 = K2 * br * h2, K3 * h * br2, K4 * h * hbr
    return [-r2 + r4, -r1 + rm1 - r3, r2 + r3 - r4, 2 * r1 - 2 * rm1 - r2 + r3 + r4, r2 - r3 - r4]


def v_ss(h2, br2, hbr):
    return 2 * K2 * math.sqrt(K1 / KM1) * h2 * math.sqrt(br2) / (1 + (K4 / K3) * hbr / br2)


def integrate(tmax=800.0, dt=2e-3, every=500):
    return rk4(rhs, [1.0, 1.0, 0.0, 0.0, 0.0], 0.0, tmax, dt, every)


def rows(sol=None):
    sol = sol or integrate()
    out = []
    for t, (h2, br2, hbr, br, h) in sol:
        out.append((t, hbr, rhs(t, [h2, br2, hbr, br, h])[2], v_ss(h2, br2, hbr), br / 1e-3))
    return out


if __name__ == "__main__":
    write_table(__file__, ("t", "HBr", "v", "vss", "Br_rel"), rows())
