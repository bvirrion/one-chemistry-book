"""Chapter 4: equilibrium constants from tabulated Gibbs energies of
formation (JANAF rows janafG:<species>.<T>).
  part a: ln K of N2 + 3 H2 = 2 NH3 against 1/T, with the van 't Hoff line of
          slope -DrH/R (DrH at 298.15 K, Ellingham approximation);
  part b: equilibrium mole fraction of NH3 against T at several pressures,
          stoichiometric feed N2 : H2 = 1 : 3, perfect gases;
  part c: equilibrium conversion of SO2 to SO3 against T for a model feed
          (10 % SO2, 11 % O2, 79 % N2 at 1 bar) with the adiabatic lines of
          three catalyst beds."""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

R = value("const:R")
TS = [298.15, 400, 500, 600, 700, 800, 900, 1000]


def dfg(sp, T):
    return value("janafG:%s.%g" % (sp, T))


def lnK_ammonia(T):
    """ln K of N2 + 3 H2 = 2 NH3 at a tabulated temperature."""
    return -2 * dfg("NH3", T) * 1000.0 / (R * T)


def drH_ammonia():
    return 2 * value("dfh:NH3_g")


def lnK_ammonia_interp(T):
    """ln K between tabulated temperatures: linear in 1/T (van 't Hoff with
    the local DrH)."""
    xs = [1.0 / t for t in TS][::-1]
    ys = [lnK_ammonia(t) for t in TS][::-1]
    return float(np.interp(1.0 / T, xs, ys))


def x_ammonia(T, p_bar):
    """Equilibrium mole fraction of NH3 from a stoichiometric feed.
    With x = x(NH3), x(N2) = (1-x)/4, x(H2) = 3(1-x)/4:
    K = x^2 / [((1-x)/4) (3(1-x)/4)^3] (p0/p)^2."""
    K = math.exp(lnK_ammonia_interp(T))
    a = math.sqrt(K * 27.0 / 256.0) * p_bar          # x / (1-x)^2 = a
    # a (1-x)^2 - x = 0 -> a x^2 - (2a+1) x + a = 0, root in (0, 1)
    if a == 0:
        return 0.0
    return ((2 * a + 1) - math.sqrt((2 * a + 1) ** 2 - 4 * a * a)) / (2 * a)


def k_so2(T):
    """K of SO2 + 1/2 O2 = SO3."""
    return math.exp(-(dfg("SO3", T) - dfg("SO2", T)) * 1000.0 / (R * T))


def k_so2_interp(T):
    xs = [1.0 / t for t in TS][::-1]
    ys = [math.log(k_so2(t)) for t in TS][::-1]
    return math.exp(float(np.interp(1.0 / T, xs, ys)))


FEED = {"SO2": 0.10, "O2": 0.11, "N2": 0.79}   # model feed, 1 bar


def conversion_so2(T, p_bar=1.0):
    """Equilibrium conversion X of SO2 (bisection on Q = K)."""
    K = k_so2_interp(T)
    y0, o0 = FEED["SO2"], FEED["O2"]

    def f(X):
        n_so2 = y0 * (1 - X)
        n_so3 = y0 * X
        n_o2 = o0 - 0.5 * y0 * X
        n_tot = 1.0 - 0.5 * y0 * X
        Q = (n_so3 / n_tot) / ((n_so2 / n_tot) * math.sqrt(n_o2 / n_tot * p_bar))
        return Q - K
    lo, hi = 1e-9, 1 - 1e-12
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


DT_AD = 300.0   # model adiabatic rise for full conversion of this feed, K
BEDS = [(690.0, 0.0), (710.0, None), (710.0, None)]   # inlet T of each bed


def bed_path(T_in, X_in):
    """Adiabatic line T = T_in + DT_AD (X - X_in) up to the equilibrium curve."""
    pts = []
    X = X_in
    while True:
        T = T_in + DT_AD * (X - X_in)
        if X >= conversion_so2(T) or X > 0.999:
            pts.append((T, X))
            break
        pts.append((T, X))
        X += 0.002
    return pts


def beds():
    out = []
    X = 0.0
    for T_in, _ in BEDS:
        path = bed_path(T_in, X)
        out.append(path)
        X = path[-1][1]
    return out


if __name__ == "__main__":
    write_table(__file__, ("invT", "lnK"), [(1000.0 / T, lnK_ammonia(T)) for T in TS], part="a")
    h = drH_ammonia() * 1000.0
    line = [(1000.0 / T, lnK_ammonia(298.15) - h / R * (1.0 / T - 1.0 / 298.15)) for T in TS]
    write_table(__file__, ("invT", "lnK"), line, part="a-line")
    rows = []
    for T in np.arange(500.0, 1000.1, 10.0):
        rows.append((T,) + tuple(x_ammonia(T, p) for p in (1, 50, 200, 300)))
    write_table(__file__, ("T", "p1", "p50", "p200", "p300"), rows, part="b")
    write_table(__file__, ("T", "X"), [(T, conversion_so2(T)) for T in np.arange(600.0, 900.1, 5.0)], part="c")
    for k, path in enumerate(beds()):
        write_table(__file__, ("T", "X"), path, part="bed%d" % (k + 1))
