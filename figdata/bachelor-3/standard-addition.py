"""Ch. 15, anodic stripping voltammetry of lead with three standard additions
(data of the exercise, generated here): Gaussian stripping peaks near
-0.42 V, heights proportional to the lead concentration (sensitivity and
sample concentration are model values, with a fixed small scatter), and the
least-squares line of peak height against added concentration, whose
intercept on the concentration axis is minus the sample concentration."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402

C0 = 4.2                    # ug/L in the measured solution (model)
ADDED = (0.0, 5.0, 10.0, 15.0)
SENS = 0.110                # uA per ug/L (model)
SCAT = (1.012, 0.991, 1.006, 0.995)


def heights():
    return [round(SENS * (C0 + a) * s, 3) for a, s in zip(ADDED, SCAT)]


def fit():
    xs, ys = ADDED, heights()
    n = len(xs)
    xm, ym = sum(xs) / n, sum(ys) / n
    sxx = sum((x - xm) ** 2 for x in xs)
    b = sum((x - xm) * (y - ym) for x, y in zip(xs, ys)) / sxx
    a = ym - b * xm
    s = math.sqrt(sum((y - a - b * x) ** 2 for x, y in zip(xs, ys)) / (n - 2))
    c0 = a / b
    s_c0 = s / b * math.sqrt(1 / n + ym ** 2 / (b * b * sxx))
    return dict(a=a, b=b, s=s, c0=c0, s_c0=s_c0)


def peak(e, h):
    return h * math.exp(-((e + 0.42) / 0.025) ** 2)


if __name__ == "__main__":
    hs = heights()
    write_table(__file__, ("E_mV",) + tuple("s%d" % i for i in range(4)),
                [(1000 * (-0.6 + 0.002 * k),) + tuple(peak(-0.6 + 0.002 * k, h) + 0.05 for h in hs)
                 for k in range(0, 151)], part="peaks")
    f = fit()
    write_table(__file__, ("added", "h"), list(zip(ADDED, hs)), part="points")
    write_table(__file__, ("added", "h"), [(x, f["a"] + f["b"] * x) for x in (-f["c0"] - 1, 16.0)], part="line")
    print("heights", hs, "fit", f)
