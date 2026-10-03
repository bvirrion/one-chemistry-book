"""Ch. 25, measuring binding. Exact 1:1 isotherm: with host H0 and guest G0,
[HG] = ((H0 + G0 + 1/K) - sqrt((H0 + G0 + 1/K)^2 - 4 H0 G0))/2.
Part a: fraction of host bound against equivalents of guest, H0 = 1.0 mmol/L,
K = 1e2, 1e3, 1e4 L/mol. Part b: Job plots (complex concentration against the
mole fraction of host, total 1.0 mmol/L) for 1:1 (K = 1e5) and 1:2 (beta2 =
1e10 L2/mol2, stepwise K1 = 4 K2: statistical). Part c: the data of the
chapter's problem, an NMR titration in fast exchange (H0 = 2.0 mmol/L, model
K = 1.5e3 L/mol, delta_free = 3.560 ppm, delta_bound = 3.720 ppm, fixed
deviations of a few thousandths of a ppm), and the fit of K and delta_bound by
nonlinear least squares with standard errors."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

H0_A = 1.0e-3


def bound_1to1(h0, g0, k):
    b = h0 + g0 + 1 / k
    return (b - math.sqrt(b * b - 4 * h0 * g0)) / 2


def job_1to1(x, total=1.0e-3, k=1e5):
    return bound_1to1(x * total, (1 - x) * total, k)


def job_1to2(x, total=1.0e-3, k1=2e5, k2=5e4):
    """[HG2] for H + G <=> HG (k1), HG + G <=> HG2 (k2); solve for free G."""
    h0, g0 = x * total, (1 - x) * total
    if h0 == 0 or g0 == 0:
        return 0.0
    lo, hi = 0.0, g0
    for _ in range(200):
        g = (lo + hi) / 2
        h = h0 / (1 + k1 * g + k1 * k2 * g * g)
        gtot = g + k1 * h * g + 2 * k1 * k2 * h * g * g
        if gtot > g0:
            hi = g
        else:
            lo = g
    h = h0 / (1 + k1 * g + k1 * k2 * g * g)
    return k1 * k2 * h * g * g


# --- the problem's NMR titration -------------------------------------------
H0_P, K_TRUE, D_FREE, D_BOUND = 2.0e-3, 1.5e3, 3.560, 3.720
EQUIV = (0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0)
NOISE = (0.0, 0.002, -0.001, 0.001, -0.002, 0.001, 0.002, -0.001, 0.0, -0.002, 0.001)


def delta_model(g0, k, db, h0=H0_P, df=D_FREE):
    return df + (db - df) * bound_1to1(h0, g0, k) / h0


def problem_data():
    return [(e, round(delta_model(e * H0_P, K_TRUE, D_BOUND) + n, 3)) for e, n in zip(EQUIV, NOISE)]


def fit(data, k0=1e3, db0=3.7):
    """Gauss-Newton on (log K, delta_bound); returns K, sK, db, sdb, rms."""
    lk, db = math.log(k0), db0
    for _ in range(100):
        J, r = [], []
        for e, d in data:
            g0 = e * H0_P
            f = delta_model(g0, math.exp(lk), db)
            h = 1e-6
            dfk = (delta_model(g0, math.exp(lk + h), db) - delta_model(g0, math.exp(lk - h), db)) / (2 * h)
            dfd = (delta_model(g0, math.exp(lk), db + h) - delta_model(g0, math.exp(lk), db - h)) / (2 * h)
            J.append((dfk, dfd))
            r.append(d - f)
        a = sum(j[0] * j[0] for j in J); b = sum(j[0] * j[1] for j in J); c = sum(j[1] * j[1] for j in J)
        u = sum(j[0] * ri for j, ri in zip(J, r)); v = sum(j[1] * ri for j, ri in zip(J, r))
        det = a * c - b * b
        dlk, ddb = (c * u - b * v) / det, (a * v - b * u) / det
        lk, db = lk + dlk, db + ddb
        if abs(dlk) < 1e-12 and abs(ddb) < 1e-12:
            break
    ss = sum(ri * ri for ri in r)
    s2 = ss / (len(data) - 2)
    var_lk, var_db = s2 * c / det, s2 * a / det
    k = math.exp(lk)
    return k, k * math.sqrt(var_lk), db, math.sqrt(var_db), math.sqrt(ss / len(data))


if __name__ == "__main__":
    rows = []
    for j in range(0, 101):
        eq = 0.06 * j
        rows.append((eq,) + tuple(bound_1to1(H0_A, eq * H0_A, k) / H0_A for k in (1e2, 1e3, 1e4)))
    write_table(__file__, ("equiv", "K2", "K3", "K4"), rows)
    xs = [j / 100 for j in range(0, 101)]
    write_table(__file__, ("x", "HG", "HG2"), [(x, job_1to1(x) / 1e-3, job_1to2(x) / 1e-3) for x in xs], part="b")
    data = problem_data()
    write_table(__file__, ("equiv", "delta"), data, part="c", digits=4)
    k, sk, db, sdb, rms = fit(data)
    print(data)
    print("fit K = %.0f +- %.0f, db = %.4f +- %.4f, rms %.4f" % (k, sk, db, sdb, rms))
    print("job max 1:1 at", max(xs, key=job_1to1), "1:2 at", max(xs, key=job_1to2))
