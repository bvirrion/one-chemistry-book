"""pH-metric and conductimetric titrations (grade 12).

Exact pH from the charge balance at 25 degC (Ke = 1.0e-14, ledger ke:25C;
pKa of ethanoic acid 4.76, ledger pka:ethanoic). Conductivities from the
limiting molar ionic conductivities (ledger lam:H+, lam:OH-, lam:Na+,
lam:Cl-), dilute solutions, Kohlrausch's law; volumes add.
  part a: V (mL), pH and dpH/dV for 20.0 mL HCl 0.100 mol/L + NaOH 0.100 mol/L
  part b: V (mL), pH and dpH/dV for 10.0 mL ethanoic acid 0.101 mol/L
          (the diluted vinegar of the problem) + NaOH 0.100 mol/L
  part c: V (mL), conductivity (mS/cm) of 100 mL HCl 0.0100 mol/L titrated
          by NaOH 0.100 mol/L
"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table

KE = 1.0e-14
KA = 10 ** -4.76
LAM = {"H": 349.81, "OH": 198.3, "Na": 50.3, "Cl": 76.2}   # S cm2/mol


def ph_strong(vb, ca=0.100, va=20.0, cb=0.100):
    vt = va + vb
    d = (cb * vb - ca * va) / vt          # [Na+] - [Cl-]
    # h - KE/h + d = 0  ->  h^2 + d h - KE = 0
    h = (-d + math.sqrt(d * d + 4 * KE)) / 2
    return -math.log10(h)


def ph_weak(vb, ca=0.101, va=10.0, cb=0.100, ka=KA):
    vt = va + vb
    c = ca * va / vt
    na = cb * vb / vt

    def f(logh):
        h = 10 ** logh
        return h + na - KE / h - c * ka / (ka + h)
    lo, hi = -14.0, 0.0                      # f(lo) < 0 < f(hi)
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return -(lo + hi) / 2


def curve(fun, vmax, step=0.05):
    n = int(round(vmax / step))
    vs = [i * step for i in range(n + 1)]
    ph = [fun(v) for v in vs]
    out = []
    for i, v in enumerate(vs):
        if 0 < i < n:
            d = (ph[i + 1] - ph[i - 1]) / (2 * step)
        else:
            d = 0.0
        out.append((round(v, 3), round(ph[i], 4), round(d, 4)))
    return out


def sigma(vb, ca=0.0100, va=100.0, cb=0.100):
    vt = va + vb
    nh = ca * va - cb * vb
    cl = ca * va / vt
    na = cb * vb / vt
    h = max(nh, 0) / vt
    oh = max(-nh, 0) / vt
    return LAM["H"] * h + LAM["OH"] * oh + LAM["Na"] * na + LAM["Cl"] * cl   # mS/cm


def conductimetric(vmax=20.0, step=0.5):
    return [(round(i * step, 2), round(sigma(i * step), 4)) for i in range(int(vmax / step) + 1)]


def v_of_max_slope(rows):
    return max(rows, key=lambda r: r[2])[0]


if __name__ == "__main__":
    write_table(__file__, ("V", "pH", "dpH"), curve(ph_strong, 30.0), part="a", digits=6)
    write_table(__file__, ("V", "pH", "dpH"), curve(ph_weak, 16.0), part="b", digits=6)
    write_table(__file__, ("V", "sigma"), conductimetric(), part="c", digits=6)
