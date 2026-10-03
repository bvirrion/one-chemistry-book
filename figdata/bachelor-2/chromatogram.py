"""Chromatography (chapter 31). Models and exercise data, no measured chromatogram.
- a: two Gaussian peaks of equal area and width (sigma = 1) at resolution
     R_s = 0.75, 1.0 and 1.5 (separation 4 sigma R_s), signal summed;
- b: van Deemter curve H = A + B/u + C u (exercise parameters A = 10 um,
     B = 20 um mm/s, C = 5 um s/mm), with its three terms;
- c: simulated reversed-phase chromatogram of the caffeine problem (invented
     retention data): unretained sugars at t_M = 1.0 min, theophylline
     (internal standard) 3.0 min, caffeine 3.4 min; widths at base 4 sigma."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table

RS = (0.75, 1.0, 1.5)
A, B, C = 10.0, 20.0, 5.0
PEAKS_C = [  # (t_R / min, base width w / min, height)
    (1.0, 0.12, 0.35),   # sugars, unretained
    (3.0, 0.18, 0.80),   # theophylline, internal standard
    (3.4, 0.20, 0.78),   # caffeine
]


def gauss(x, mu, sigma, height=1.0):
    return height * math.exp(-0.5 * ((x - mu) / sigma) ** 2)


def two_peaks(x, rs, sigma=1.0):
    d = 4 * sigma * rs
    return gauss(x, -d / 2, sigma) + gauss(x, d / 2, sigma)


def van_deemter(u, a=A, b=B, c=C):
    return a + b / u + c * u


def optimum(a=A, b=B, c=C):
    u = math.sqrt(b / c)
    return u, a + 2 * math.sqrt(b * c)


def plate_number(t_r, w):
    return 16 * (t_r / w) ** 2


def resolution(t1, w1, t2, w2):
    return 2 * (t2 - t1) / (w1 + w2)


def resolution_equation(n, alpha, k2):
    return math.sqrt(n) / 4 * (alpha - 1) / alpha * k2 / (1 + k2)


def chromatogram_c(t):
    return sum(gauss(t, tr, w / 4, h) for tr, w, h in PEAKS_C)


if __name__ == "__main__":
    xs = [i / 20 for i in range(-160, 161)]
    write_table(__file__, ("x", "r075", "r100", "r150"),
                [(x,) + tuple(two_peaks(x, r) for r in RS) for x in xs], part="a")
    us = [0.4 + i * 0.05 for i in range(0, 153)]
    write_table(__file__, ("u", "H", "A", "B", "C"),
                [(u, van_deemter(u), A, B / u, C * u) for u in us], part="b")
    ts = [i / 200 for i in range(0, 1001)]
    write_table(__file__, ("t", "s"), [(t, chromatogram_c(t)) for t in ts], part="c")
