"""Ch. 29, type A evaluation of uncertainty: twenty repeated readings of the
same titration end point (burette read to 0.05 mL). The readings are story
data, chosen by hand to look like a real series (not measurements); the
script computes their mean, experimental standard deviation and the standard
uncertainty of the mean, the histogram (bins of 0.05 mL centred on the
readable values) and the Gaussian curve of the same mean and standard
deviation scaled to the histogram (n x bin width x density).

Part a: histogram (x = volume, count); part b: Gaussian curve."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

READINGS = (12.40, 12.45, 12.50, 12.45, 12.35, 12.55, 12.45, 12.40, 12.50, 12.45,
            12.60, 12.45, 12.40, 12.50, 12.30, 12.45, 12.55, 12.45, 12.50, 12.40)
BIN = 0.05


def mean(xs=READINGS):
    return sum(xs) / len(xs)


def std(xs=READINGS):
    """Experimental standard deviation (n - 1 in the denominator)."""
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def u_mean(xs=READINGS):
    return std(xs) / math.sqrt(len(xs))


def histogram(xs=READINGS):
    lo, hi = 12.25, 12.65
    centres = [round(lo + BIN * k, 2) for k in range(int(round((hi - lo) / BIN)) + 1)]
    return [(c, sum(1 for x in xs if abs(x - c) < BIN / 2)) for c in centres]


def gaussian(xs=READINGS, npts=81):
    m, s, n = mean(xs), std(xs), len(xs)
    rows = []
    for k in range(npts):
        x = 12.20 + 0.50 * k / (npts - 1)
        rows.append((x, n * BIN * math.exp(-0.5 * ((x - m) / s) ** 2) / (s * math.sqrt(2 * math.pi))))
    return rows


if __name__ == "__main__":
    write_table(__file__, ("V", "count"), histogram(), part="a", digits=5)
    write_table(__file__, ("V", "g"), gaussian(), part="b", digits=5)
