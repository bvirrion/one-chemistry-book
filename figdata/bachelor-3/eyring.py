"""Ch. 12, Eyring analysis of the weekend problem's rate constants (data of
the problem, generated here): first-order rate constants of the enzymatic
O-demethylation of a drug (C-H cleavage) and of its CD3 analogue at five
temperatures, built from chosen activation parameters with a fixed 3 %
scatter. The least-squares line ln(k/T) = a + b/T gives
dH = -R b and dS = R (a - ln(k_B/h)) with their standard errors."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

R = value("const:R")
KB = value("const:kB")
H = value("const:h")
TEMPS = (278.15, 288.15, 298.15, 308.15, 318.15)
# chosen parameters: dH(H) 62.0 kJ/mol, dS -60 J/K/mol; the D compound loses
# the zero-point energy difference of the CH4/CD4 symmetric stretches in dH
DH_H, DS = 62.0e3, -60.0
SCATTER = (1.021, 0.974, 1.032, 0.985, 1.008, 0.979, 1.026, 0.991, 1.018, 0.970)


def ddh():
    return (value("vib:CH4.nu1") - value("vib:CD4.nu1")) / 2 * H * value("const:c") * 100 * value("const:NA")


def k_true(T, dh):
    return KB * T / H * math.exp(DS / R) * math.exp(-dh / (R * T))


def data():
    """the printed table: T, k_H, k_D (s-1), rounded to 3 significant digits"""
    rows = []
    for i, T in enumerate(TEMPS):
        kh = float("%.3g" % (k_true(T, DH_H) * SCATTER[2 * i]))
        kd = float("%.3g" % (k_true(T, DH_H + ddh()) * SCATTER[2 * i + 1]))
        rows.append((T, kh, kd))
    return rows


def fit(xs, ys):
    """least squares y = a + b x; returns a, b, s_a, s_b, s"""
    n = len(xs)
    xm, ym = sum(xs) / n, sum(ys) / n
    sxx = sum((x - xm) ** 2 for x in xs)
    b = sum((x - xm) * (y - ym) for x, y in zip(xs, ys)) / sxx
    a = ym - b * xm
    s2 = sum((y - a - b * x) ** 2 for x, y in zip(xs, ys)) / (n - 2)
    sb = math.sqrt(s2 / sxx)
    sa = math.sqrt(s2 * (1 / n + xm ** 2 / sxx))
    return a, b, sa, sb, math.sqrt(s2), xm, sxx


def eyring(col):
    rows = data()
    xs = [1 / r[0] for r in rows]
    ys = [math.log(r[col] / r[0]) for r in rows]
    a, b, sa, sb, s, xm, sxx = fit(xs, ys)
    return dict(dH=-R * b, s_dH=R * sb, dS=R * (a - math.log(KB / H)), s_dS=R * sa,
                a=a, b=b, s=s, xm=xm, sxx=sxx, xs=xs, ys=ys)


def band(col, t975=3.182):
    """fitted line and its 95 % confidence band (n = 5, t = 3.182)"""
    e = eyring(col)
    out = []
    for i in range(41):
        x = 1 / 320.0 + i * (1 / 276.0 - 1 / 320.0) / 40
        y = e["a"] + e["b"] * x
        h = t975 * e["s"] * math.sqrt(1 / 5 + (x - e["xm"]) ** 2 / e["sxx"])
        out.append((1000 * x, y, y - h, y + h))
    return out


if __name__ == "__main__":
    write_table(__file__, ("invT", "lnkT_H", "lnkT_D"),
                [(1000 / r[0], math.log(r[1] / r[0]), math.log(r[2] / r[0])) for r in data()], part="points")
    for col, name in ((1, "H"), (2, "D")):
        write_table(__file__, ("invT", "fit", "lo", "hi"), band(col), part="band-" + name)
    print("data:", data())
    for col in (1, 2):
        e = eyring(col)
        print(col, "dH = %.2f +- %.2f kJ/mol, dS = %.1f +- %.1f J/K/mol"
              % (e["dH"] / 1000, e["s_dH"] / 1000, e["dS"], e["s_dS"]))
    print("ddH (ZPE) = %.3f kJ/mol" % (ddh() / 1000))
