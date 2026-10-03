"""Synthetic 1H NMR spectra with integration curves (grade 12, proton NMR).

SYNTHETIC: each signal is a multiplet of Lorentzian lines centred at a
ledger shift (PubChem / HMDB peak lists: nmr:ethanol-*, nmr:ethylethanoate-*,
nmr:acetone, nmr:propanoic-*, nmr:meoac-*), with the n + 1 lines spaced by
J = 7 Hz drawn as at 90 MHz and binomial intensities; the line width is
invented. The integration curve is the running area from high to low shift,
scaled so that one proton is one unit.

Parts a-e: delta (ppm), intensity, integral -- ethanol, ethyl ethanoate,
propanone, propanoic acid, methyl ethanoate.
"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table

SPACING = 7.0 / 90.0      # ppm between lines: J = 7 Hz at 90 MHz
WIDTH = 0.006             # half-width of a line, ppm (invented)

# (shift, number of protons, number of neighbouring H giving the splitting)
COMPOUNDS = {
    "ethanol": [(3.69, 2, 3), (2.61, 1, 0), (1.23, 3, 2)],
    "ethylethanoate": [(4.12, 2, 3), (2.04, 3, 0), (1.26, 3, 2)],
    "propanone": [(2.16, 6, 0)],
    "propanoic": [(11.73, 1, 0), (2.39, 2, 3), (1.16, 3, 2)],
    "methylethanoate": [(3.66, 3, 0), (2.05, 3, 0)],
}
RANGE = {"propanoic": (0.0, 12.5)}


def lines(compound):
    """(position, area) of every line: n + 1 lines, binomial areas summing to H."""
    out = []
    for d, h, n in COMPOUNDS[compound]:
        coeff = [math.comb(n, k) for k in range(n + 1)]
        tot = sum(coeff)
        for k, c in enumerate(coeff):
            out.append((d + (k - n / 2.0) * SPACING, h * c / tot))
    return out


def intensity(compound, x):
    return sum(a * (WIDTH / math.pi) / ((x - p) ** 2 + WIDTH ** 2)
               for p, a in lines(compound))


def table(compound, step=0.002):
    lo, hi = RANGE.get(compound, (0.0, 5.0))
    n = int(round((hi - lo) / step))
    xs = [hi - i * step for i in range(n + 1)]
    ys = [intensity(compound, x) for x in xs]
    peak = max(ys)
    rows, area = [], 0.0
    for i, (x, y) in enumerate(zip(xs, ys)):
        if i:
            area += 0.5 * (y + ys[i - 1]) * step
        rows.append((round(x, 3), round(y / peak, 4), round(area, 3)))
    return rows


def steps(compound):
    """Integral gained across each signal (should equal its proton count)."""
    rows = table(compound)
    out = []
    for d, h, n in COMPOUNDS[compound]:
        half = (n / 2.0) * SPACING + 0.35
        inside = [a for x, _, a in rows if d - half <= x <= d + half]
        out.append(round(max(inside) - min(inside), 1))
    return out


if __name__ == "__main__":
    for part, c in zip("abcde", ("ethanol", "ethylethanoate", "propanone",
                                 "propanoic", "methylethanoate")):
        write_table(__file__, ("delta", "I", "integral"), table(c), part=part, digits=6)
