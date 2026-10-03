"""Ch. 13, enzyme kinetics. (a) Model curves v([S]) for K_M = 0.80 mM and
V_max = 0.500 uM/s, with no inhibitor, a competitive inhibitor at [I] = 2 K_i
and an uncompetitive one at [I] = K_i', and the Lineweaver-Burk lines.
(b) The weekend problem's data (generated here with a fixed 2 % scatter):
initial rates at seven [S]; apparent K_M at four inhibitor concentrations; a
stopped-flow burst trace. Fits: nonlinear least squares (Gauss-Newton) with
standard errors from s^2 (J^T J)^-1, and the Lineweaver-Burk line for
comparison."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402

KM, VMAX = 0.80, 0.500          # mM, uM/s
E0 = 5.0e-3                      # uM (5 nM) in the initial-rate assays
KI = 25.0                        # uM, competitive inhibitor of the problem
S_DATA = (0.10, 0.20, 0.40, 0.80, 1.60, 3.20, 6.40)
SCAT = (1.018, 0.981, 1.012, 0.987, 1.021, 0.992, 1.006, 0.985, 1.015, 0.990)
I_DATA = (0.0, 20.0, 50.0, 100.0)   # uM
# pre-steady-state (stopped-flow) model: E + S -> ES (fast) -> E-acyl + P1 (k2) -> E + P2 (k3)
K2, K3, E0_SF = 500.0, 125.0, 2.0   # s-1, s-1, uM


def mm(s, km=KM, vmax=VMAX):
    return vmax * s / (km + s)


def rate_data():
    return [(s, float("%.3g" % (mm(s) * SCAT[i]))) for i, s in enumerate(S_DATA)]


def km_app_data():
    return [(i, float("%.3g" % (KM * (1 + i / KI) * SCAT[3 + k]))) for k, i in enumerate(I_DATA)]


def solve2(a, b):
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return [(b[0] * a[1][1] - b[1] * a[0][1]) / det, (a[0][0] * b[1] - a[1][0] * b[0]) / det]


def fit_mm(data, km=1.0, vmax=1.0, iters=50):
    for _ in range(iters):
        J, r = [], []
        for s, v in data:
            J.append((-vmax * s / (km + s) ** 2, s / (km + s)))
            r.append(v - mm(s, km, vmax))
        jtj = [[sum(a[i] * a[j] for a in J) for j in range(2)] for i in range(2)]
        jtr = [sum(a[i] * ri for a, ri in zip(J, r)) for i in range(2)]
        d = solve2(jtj, jtr)
        km, vmax = km + d[0], vmax + d[1]
    J = [(-vmax * s / (km + s) ** 2, s / (km + s)) for s, _ in data]
    jtj = [[sum(a[i] * a[j] for a in J) for j in range(2)] for i in range(2)]
    s2 = sum((v - mm(s, km, vmax)) ** 2 for s, v in data) / (len(data) - 2)
    det = jtj[0][0] * jtj[1][1] - jtj[0][1] ** 2
    return dict(KM=km, Vmax=vmax, s_KM=math.sqrt(s2 * jtj[1][1] / det),
                s_Vmax=math.sqrt(s2 * jtj[0][0] / det), s=math.sqrt(s2))


def line(xs, ys):
    n = len(xs)
    xm, ym = sum(xs) / n, sum(ys) / n
    sxx = sum((x - xm) ** 2 for x in xs)
    b = sum((x - xm) * (y - ym) for x, y in zip(xs, ys)) / sxx
    a = ym - b * xm
    s2 = sum((y - a - b * x) ** 2 for x, y in zip(xs, ys)) / (n - 2)
    return a, b, math.sqrt(s2 * (1 / n + xm ** 2 / sxx)), math.sqrt(s2 / sxx)


def fit_lb(data):
    a, b, sa, sb = line([1 / s for s, _ in data], [1 / v for _, v in data])
    return dict(Vmax=1 / a, KM=b / a)


def fit_ki():
    d = km_app_data()
    a, b, sa, sb = line([i for i, _ in d], [k for _, k in d])
    ki = a / b
    s_ki = ki * math.sqrt((sa / a) ** 2 + (sb / b) ** 2)
    return dict(KM0=a, slope=b, Ki=ki, s_Ki=s_ki)


def burst(t):
    kc = K2 * K3 / (K2 + K3)
    amp = E0_SF * (K2 / (K2 + K3)) ** 2
    return amp * (1 - math.exp(-(K2 + K3) * t)) + E0_SF * kc * t


def model_rows():
    out = []
    for i in range(0, 161):
        s = 0.05 * i
        out.append((s, mm(s), mm(s, KM * 3), mm(s, KM / 2, VMAX / 2)))
    return out


def lb_rows():
    out = []
    for i in range(0, 61):
        x = -2.5 + 0.1 * i        # 1/[S] in 1/mM
        out.append((x, (KM / VMAX) * x + 1 / VMAX, (3 * KM / VMAX) * x + 1 / VMAX,
                    (KM / VMAX) * x + 2 / VMAX))
    return out


if __name__ == "__main__":
    write_table(__file__, ("S", "none", "comp", "uncomp"), model_rows(), part="model")
    write_table(__file__, ("invS", "none", "comp", "uncomp"), lb_rows(), part="lb")
    write_table(__file__, ("S", "v"), rate_data(), part="data")
    f = fit_mm(rate_data())
    write_table(__file__, ("S", "v"), [(0.05 * i, mm(0.05 * i, f["KM"], f["Vmax"])) for i in range(141)], part="fit")
    write_table(__file__, ("t_ms", "P_uM"), [(0.05 * i, burst(0.05e-3 * i)) for i in range(0, 401)], part="burst")
    print("data", rate_data())
    print("NLS", f)
    print("LB", fit_lb(rate_data()))
    print("Km app", km_app_data(), fit_ki())
    print("burst amp", E0_SF * (K2 / (K2 + K3)) ** 2, "kobs", K2 + K3, "slope", E0_SF * K2 * K3 / (K2 + K3))
