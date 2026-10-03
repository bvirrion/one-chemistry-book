"""Statistics of measurement (chapter 34). Exercise data and mathematics only.
- a: calibration of lead by graphite-furnace atomic absorption (exercise
     data): standards (x, A) and the least-squares line;
- b: residuals of that fit;
- c: Student densities for 2 and 5 degrees of freedom and the normal law;
- d: a standard-addition line (exercise data) and its x-intercept;
- e: Student coefficients t(0.975, nu) for the text's table, computed by
     integrating the density (no table copied)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table

CAL_X = [0.0, 5.0, 10.0, 15.0, 20.0]          # ug/L
CAL_Y = [0.003, 0.051, 0.101, 0.148, 0.199]    # absorbance
SAMPLE_Y = [0.104, 0.098, 0.101]
BLANKS = [0.002, 0.004, 0.003, 0.001, 0.003, 0.005, 0.002, 0.003, 0.004, 0.003]
DILUTION = 50.5 / 50.0
ADD_X = [0.0, 2.0, 4.0, 6.0]                   # added concentration, mg/L
ADD_Y = [0.125, 0.205, 0.284, 0.366]


def mean(v):
    return sum(v) / len(v)


def stdev(v):
    m = mean(v)
    return math.sqrt(sum((x - m) ** 2 for x in v) / (len(v) - 1))


def fit(x, y):
    """Least-squares slope b, intercept a, residual standard deviation s_yx."""
    n = len(x)
    xm, ym = mean(x), mean(y)
    sxx = sum((a - xm) ** 2 for a in x)
    b = sum((a - xm) * (c - ym) for a, c in zip(x, y)) / sxx
    a = ym - b * xm
    res = [c - (a + b * xi) for xi, c in zip(x, y)]
    syx = math.sqrt(sum(r * r for r in res) / (n - 2))
    return b, a, syx, res, sxx


def interpolate(x, y, y0s):
    """Concentration from m replicate readings and its standard deviation."""
    b, a, syx, _, sxx = fit(x, y)
    y0 = mean(y0s)
    x0 = (y0 - a) / b
    s = syx / b * math.sqrt(1 / len(y0s) + 1 / len(x) + (y0 - mean(y)) ** 2 / (b * b * sxx))
    return x0, s


def t_pdf(t, nu):
    c = math.exp(math.lgamma((nu + 1) / 2) - math.lgamma(nu / 2)) / math.sqrt(nu * math.pi)
    return c * (1 + t * t / nu) ** (-(nu + 1) / 2)


def normal_pdf(t):
    return math.exp(-t * t / 2) / math.sqrt(2 * math.pi)


def t_cdf(t, nu, steps=20000):
    h = t / steps
    s = t_pdf(0, nu) + t_pdf(t, nu)
    for i in range(1, steps):
        s += (4 if i % 2 else 2) * t_pdf(i * h, nu)
    return 0.5 + s * h / 3


def t_quantile(p, nu):
    lo, hi = 0.0, 100.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if t_cdf(mid, nu) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


NUS = (1, 2, 3, 4, 5, 6, 8, 9, 10, 20, 30)

if __name__ == "__main__":
    b, a, syx, res, _ = fit(CAL_X, CAL_Y)
    write_table(__file__, ("x", "A", "fit", "res"),
                [(x, y, a + b * x, r) for x, y, r in zip(CAL_X, CAL_Y, res)], part="a")
    write_table(__file__, ("x", "line"), [(x, a + b * x) for x in (0.0, 22.0)], part="b")
    ts = [i / 20 for i in range(-100, 101)]
    write_table(__file__, ("t", "nu2", "nu5", "normal"),
                [(t, t_pdf(t, 2), t_pdf(t, 5), normal_pdf(t)) for t in ts], part="c")
    bb, aa, _, _, _ = fit(ADD_X, ADD_Y)
    write_table(__file__, ("x", "A", "line"), [(x, y, aa + bb * x) for x, y in zip(ADD_X, ADD_Y)], part="d")
    write_table(__file__, ("x", "line"), [(-aa / bb, 0.0), (7.0, aa + bb * 7.0)], part="d-line")
    write_table(__file__, ("nu", "t975"), [(nu, round(t_quantile(0.975, nu), 3)) for nu in NUS], part="e")
