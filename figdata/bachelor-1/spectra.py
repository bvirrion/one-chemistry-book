"""Spectra of ch. 17, simulated from measured band positions and NMR
parameters in the ledger (rows ir:..., nmr:...).

IR: transmittance (%) built from Lorentzian bands at the measured gas-phase
positions; band heights and widths are schematic (stated in the captions).
1H NMR: first-order spectra at 90 MHz (the field of the measured spectra), every multiplet split by the n + 1
rule with binomial intensities, Lorentzian lines of 1.2 Hz full width, tallest line scaled to 1;
peak areas proportional to the number of protons."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

IR = {   # compound: [(ledger id, schematic absorbance, half width cm-1)]
    "ethanol": [("ir:ethanol-OH", 0.25, 18), ("ir:ethanol-CH", 0.9, 30), ("ir:ethanol-CO", 1.0, 20)],
    "propanone": [("ir:propanone-CO", 1.0, 15), ("ir:propanone-CCC", 0.6, 15)],
    "ethanoic": [("ir:ethanoic-OH", 0.3, 20), ("ir:ethanoic-CO", 1.0, 18), ("ir:ethanoic-CO2", 0.6, 15)],
    "ethylbutanoate": [("ir:ethylbutanoate-CH", 0.55, 30), ("ir:ethylbutanoate-CO", 1.0, 15),
                       ("ir:ethylbutanoate-COC", 0.95, 18)],
}


def transmittance(compound, nu):
    a = sum(h / (1 + ((nu - value(k)) / w) ** 2) for k, h, w in IR[compound])
    return 100 * 10 ** (-a)


def binomial(n):
    return [math.comb(n, k) for k in range(n + 1)]


NMR = {   # compound: [(shift id, number of H, number of neighbours n, J id)]
    "ethylethanoate": [("nmr:ethylethanoate-OCH2", 2, 3, "nmr:ethylethanoate-J"),
                       ("nmr:ethylethanoate-COCH3", 3, 0, None),
                       ("nmr:ethylethanoate-CH3", 3, 2, "nmr:ethylethanoate-J")],
    "ethanol": [("nmr:ethanol-CH2", 2, 3, "nmr:ethanol-J"), ("nmr:ethanol-OH", 1, 0, None),
                ("nmr:ethanol-CH3", 3, 2, "nmr:ethanol-J")],
    "ethylbutanoate": [("nmr:ethylbutanoate-OCH2", 2, 3, "nmr:ethylbutanoate-J"),
                       ("nmr:ethylbutanoate-CH2CO", 2, 2, "nmr:ethylbutanoate-J"),
                       ("nmr:ethylbutanoate-CH2", 2, 5, "nmr:ethylbutanoate-J"),
                       ("nmr:ethylbutanoate-OCH2CH3", 3, 2, "nmr:ethylbutanoate-J"),
                       ("nmr:ethylbutanoate-CH3", 3, 2, "nmr:ethylbutanoate-J")],
}
MHZ, WIDTH = 90.0, 1.2


def lines(compound):
    """(ppm, intensity) of every line, intensities summing to the H count."""
    out = []
    for sid, nh, n, jid in NMR[compound]:
        d = value(sid)
        j = value(jid) / MHZ if jid else 0.0
        b = binomial(n)
        tot = sum(b)
        for k, c in enumerate(b):
            out.append((d + (k - n / 2) * j, nh * c / tot))
    return out


def spectrum(compound, ppm):
    g = WIDTH / 2 / MHZ
    return sum(i * g / math.pi / ((ppm - p) ** 2 + g ** 2) for p, i in lines(compound)) * 1e-3


def integral(compound, lo, hi, step=0.0001):
    n = int((hi - lo) / step)
    return sum(spectrum(compound, lo + (k + 0.5) * step) for k in range(n)) * step * 1e3


if __name__ == "__main__":
    for c in IR:
        write_table(__file__, ("nu", "T"), [(nu, transmittance(c, nu)) for nu in range(4000, 499, -4)],
                    part="ir-" + c, digits=5)
    for c in NMR:
        pts = [i / 2000 for i in range(0, 10001)]
        ys = [spectrum(c, p) for p in pts]
        top = max(ys)
        write_table(__file__, ("ppm", "I"), [(p, y / top) for p, y in zip(pts, ys)], part="nmr-" + c, digits=4)
