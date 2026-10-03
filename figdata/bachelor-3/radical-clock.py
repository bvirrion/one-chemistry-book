"""Ch. 27, the 5-hexenyl radical clock. A hex-5-enyl radical either cyclises
(5-exo, first order, k_c) or is trapped by tributyltin hydride (k_H [Bu3SnH]);
with the hydride in excess, [cyclised]/[direct] = k_c/(k_H [Bu3SnH]).
Model rate constants at 25 C (data of the chapter's exercises):
k_c = 2.3e5 s-1, k_H = 2.4e6 L mol-1 s-1. Part a: fraction cyclised against
[Bu3SnH]; part b: [direct]/[cyclised] against [Bu3SnH], a straight line of
slope k_H/k_c through the origin."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

KC, KH = 2.3e5, 2.4e6


def ratio_cyc_direct(c, kc=KC, kh=KH):
    return kc / (kh * c)


def frac_cyclised(c, kc=KC, kh=KH):
    return kc / (kc + kh * c)


if __name__ == "__main__":
    cs = [10 ** (-3 + 3 * j / 120) for j in range(121)]
    write_table(__file__, ("c", "fcyc"), [(c, frac_cyclised(c)) for c in cs])
    cs = [0.02 * j for j in range(0, 51)]
    write_table(__file__, ("c", "inv"), [(c, 1 / ratio_cyc_direct(c) if c > 0 else 0.0) for c in cs], part="b")
    print(frac_cyclised(0.01), frac_cyclised(0.1), frac_cyclised(1.0), KH / KC)
