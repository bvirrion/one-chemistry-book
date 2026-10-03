"""Ch. 15, weekend problem data (generated here; model values with a fixed
scatter): (a) chronoamperometry of a 10.0 mM ferrocyanide fill on a strip
electrode of 0.0300 cm2 (Cottrell, D = 6.5e-6 cm2/s chosen for the problem);
(b) the calibration of the strip with glucose standards (current at 5.0 s),
its least-squares line with standard errors, and the inverse prediction of a
blood sample's concentration with its standard uncertainty."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

A, CFILL, DTRUE = 0.0300, 1.00e-5, 6.5e-6          # cm2, mol/cm3, cm2/s
TIMES = (1.0, 2.0, 3.0, 4.0, 5.0)
SC1 = (1.008, 0.994, 1.004, 0.997, 1.002)
STD = (2.0, 4.0, 6.0, 8.0, 10.0, 15.0, 20.0)        # mM
B0, B1 = 0.35, 0.92                                  # uA, uA/mM (model)
SC2 = (0.985, 1.012, 0.994, 1.009, 0.990, 1.006, 0.997)
I_SAMPLE = 7.10                                      # uA, one reading


def cottrell_data():
    k = value("const:F") * A * CFILL * math.sqrt(DTRUE / math.pi)
    return [(t, round(1e6 * k / math.sqrt(t) * s, 1)) for t, s in zip(TIMES, SC1)]


def line(xs, ys):
    n = len(xs)
    xm, ym = sum(xs) / n, sum(ys) / n
    sxx = sum((x - xm) ** 2 for x in xs)
    b = sum((x - xm) * (y - ym) for x, y in zip(xs, ys)) / sxx
    a = ym - b * xm
    s = math.sqrt(sum((y - a - b * x) ** 2 for x, y in zip(xs, ys)) / (n - 2))
    return dict(a=a, b=b, s=s, sa=s * math.sqrt(1 / n + xm ** 2 / sxx), sb=s / math.sqrt(sxx),
                xm=xm, ym=ym, sxx=sxx, n=n)


def d_from_cottrell():
    d = cottrell_data()
    xs = [t ** -0.5 for t, _ in d]
    ys = [i * 1e-6 for _, i in d]
    # fit through the origin: slope = sum(xy)/sum(x^2)
    slope = sum(x * y for x, y in zip(xs, ys)) / sum(x * x for x in xs)
    k = value("const:F") * A * CFILL
    return slope, math.pi * (slope / k) ** 2


def calibration():
    return [(c, round((B0 + B1 * c) * s, 2)) for c, s in zip(STD, SC2)]


def inverse(i_obs=I_SAMPLE, m=1):
    cal = calibration()
    f = line([c for c, _ in cal], [i for _, i in cal])
    c = (i_obs - f["a"]) / f["b"]
    u = f["s"] / f["b"] * math.sqrt(1 / m + 1 / f["n"] + (i_obs - f["ym"]) ** 2 / (f["b"] ** 2 * f["sxx"]))
    return c, u, f


if __name__ == "__main__":
    print("cottrell", cottrell_data(), "slope, D", d_from_cottrell())
    print("calibration", calibration())
    c, u, f = inverse()
    print("line a=%.4f (%.4f) b=%.5f (%.5f) s=%.4f; c = %.3f +- %.3f mM" % (f["a"], f["sa"], f["b"], f["sb"], f["s"], c, u))
    write_table(__file__, ("c", "i"), calibration(), part="cal")
