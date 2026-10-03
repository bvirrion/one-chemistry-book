"""Ch. 8, a free induction decay with two lines (offsets 100 and 250 Hz from
the reference, equal amplitudes, T2 = 0.10 s) and its spectrum obtained by
a discrete Fourier transform (numpy), real part: two Lorentzians of full
width at half maximum 1/(pi T2) = 3.2 Hz."""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

OFFSETS, T2, DT, N = (100.0, 250.0), 0.10, 1 / 1000, 4096


def fid(t):
    return sum(math.cos(2 * math.pi * f * t) for f in OFFSETS) * math.exp(-t / T2)


def spectrum():
    t = np.arange(N) * DT
    s = np.sum([np.exp(2j * np.pi * f * t) for f in OFFSETS], axis=0) * np.exp(-t / T2)
    s[0] *= 0.5
    spec = np.fft.fft(s) * DT
    freq = np.fft.fftfreq(N, DT)
    order = np.argsort(freq)
    return freq[order], spec.real[order]


def fwhm_of_line(f0):
    freq, re = spectrum()
    i0 = int(np.argmin(abs(freq - f0)))
    half = re[i0] / 2
    lo = i0
    while re[lo] > half:
        lo -= 1
    hi = i0
    while re[hi] > half:
        hi += 1
    def cross(a, b):
        return freq[a] + (half - re[a]) * (freq[b] - freq[a]) / (re[b] - re[a])
    return cross(hi - 1, hi) - cross(lo + 1, lo)


if __name__ == "__main__":
    write_table(__file__, ("t", "s"), [(i * 0.001, fid(i * 0.001)) for i in range(0, 401)])
    f, r = spectrum()
    top = max(r)
    write_table(__file__, ("f", "I"), [(a, b / top) for a, b in zip(f, r) if 0 <= a <= 350], part="spectrum")
