"""Ch. 33, quantitative NMR. Synthetic 1H spectrum of a ferrocene sample
(20.0 mg, true purity 98.0 %) weighed with 1,3,5-trimethoxybenzene as internal
standard (15.0 mg, purity 99.9 %) in CDCl3 (data of the chapter's problem):
singlets at 4.16 ppm (ferrocene, 10 H), 6.09 ppm (standard, aromatic, 3 H) and
3.77 ppm (standard, OCH3, 9 H), Lorentzian half-width 0.004 ppm, areas
proportional to amount x protons. The purity formula
P = (I_x/I_s)(N_s/N_x)(M_x/M_s)(m_s/m_x) P_s recovers the input. Molar masses
from the book's atomic weights."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
from _table import write_table  # noqa: E402
import chem  # noqa: E402
import molar_mass  # noqa: E402

W = molar_mass.book_weights()
MX, MS = chem.molar_mass("C10H10Fe", W), chem.molar_mass("C9H12O3", W)
MASS_X, MASS_S, P_TRUE, P_S = 20.0, 15.0, 0.980, 0.999
HW = 0.004


def amounts():
    return P_TRUE * MASS_X / MX, P_S * MASS_S / MS     # mmol


def lines():
    nx, ns = amounts()
    return [(4.16, 10 * nx), (6.09, 3 * ns), (3.77, 9 * ns)]


def spectrum(x):
    return sum(a * (HW / math.pi) / ((x - d) ** 2 + HW * HW) for d, a in lines())


def integral(d, half=0.1, step=0.0002):
    xs = [d - half + step * j for j in range(int(2 * half / step) + 1)]
    ys = [spectrum(x) for x in xs]
    return sum((ys[i] + ys[i + 1]) / 2 * step for i in range(len(xs) - 1))


def purity(ix, i_s, nx=10, ns=3):
    return (ix / i_s) * (ns / nx) * (MX / MS) * (MASS_S / MASS_X) * P_S


if __name__ == "__main__":
    xs = [7.0 - 0.001 * j for j in range(0, 4001)]
    ys = [spectrum(x) for x in xs]
    m = max(ys)
    write_table(__file__, ("ppm", "y"), [(x, y / m) for x, y in zip(xs, ys)])
    ix, i_s = integral(4.16), integral(6.09)
    print("MX", MX, "MS", MS, "ratio", ix / i_s, "purity", purity(ix, i_s))
