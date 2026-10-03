"""Ch. 29, synthetic 1H NMR spectra of pyridine, pyrrole and furan in CDCl3:
Lorentzian lines (half-width 0.012 ppm; couplings ignored) at the ledger
shifts, with areas equal to the proton counts: pyridine H2/6 : H4 : H3/5 =
2 : 1 : 2; pyrrole H2/5 : H3/4 = 2 : 2 and a broad N-H (half-width 0.12 ppm);
furan 2 : 2. Parts pyridine, pyrrole, furan: columns ppm, y (normalised so
that the tallest line of each spectrum is 1)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

W = 0.012
SPECTRA = {
    "pyridine": [("h1:pyridine.a", 2, W), ("h1:pyridine.g", 1, W), ("h1:pyridine.b", 2, W)],
    "pyrrole": [("h1:pyrrole.a", 2, W), ("h1:pyrrole.b", 2, W), ("h1:pyrrole.NH", 1, 0.12)],
    "furan": [("h1:furan.a", 2, W), ("h1:furan.b", 2, W)],
}


def lines(name):
    return [(value(k), n, w) for k, n, w in SPECTRA[name]]


def spectrum(name, x):
    return sum(n * (w / math.pi) / ((x - d) ** 2 + w * w) for d, n, w in lines(name))


def grid():
    return [9.0 - 0.002 * j for j in range(0, 1751)]   # 9.0 down to 5.5 ppm


def integrals(name, half=0.25):
    """Areas of the windows +-half around each line (W lines) by the trapezoid rule."""
    out = []
    for d, n, w in lines(name):
        xs = [d - half + 0.0005 * j for j in range(int(2 * half / 0.0005) + 1)]
        ys = [spectrum(name, x) for x in xs]
        out.append(sum((ys[i] + ys[i + 1]) / 2 * 0.0005 for i in range(len(xs) - 1)))
    return out


if __name__ == "__main__":
    for name in SPECTRA:
        xs = grid()
        ys = [spectrum(name, x) for x in xs]
        m = max(ys)
        write_table(__file__, ("ppm", "y"), [(x, y / m) for x, y in zip(xs, ys)], part=name)
        print(name, [round(a, 2) for a in integrals(name)])
