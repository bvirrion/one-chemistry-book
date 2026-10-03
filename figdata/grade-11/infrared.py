"""Infrared spectra of six compounds (grade 11, infrared).

SYNTHETIC: transmittance curves built from bands placed at sourced positions
(ledger ir:* rows: OpenStax Organic Chemistry ranges and NIST WebBook gas-phase
maxima); band heights and widths are invented to look like real spectra, and
only the bands the chapter discusses are drawn.

Columns: wavenumber (cm-1), then T (%) of ethanol (liquid), ethanol (gas),
propanone, ethanoic acid, ethyl ethanoate, ethanamine.
"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table

# (centre cm-1, peak absorbance, half-width cm-1, shape) ; ledger id in comment
BANDS = {
    "ethanolL": [(3350, 1.10, 130, "g"),   # ir:OH-bonded (3300-3400), broad
                 (2950, 0.55, 35, "l"),    # ir:CH (2850-2960)
                 (1050, 1.20, 25, "l")],   # ir:CO-single (near 1050)
    "ethanolG": [(3666, 0.55, 12, "l"),    # ir:ethanol-OH (gas, sharp)
                 (2978, 0.70, 30, "l"),    # ir:ethanol-CH
                 (1060, 0.90, 22, "l")],   # ir:ethanol-CO
    "propanone": [(2960, 0.30, 35, "l"),   # ir:CH
                  (1715, 1.50, 18, "l"),   # ir:CO-ketone
                  (1224, 0.70, 20, "l")],  # ir:propanone-CCC
    "acid": [(2950, 0.85, 330, "g"),       # ir:OH-acid (2500-3300), very broad
             (1710, 1.40, 30, "l")],       # ir:CO-acid (dimer)
    "ester": [(2960, 0.30, 35, "l"),       # ir:CH
              (1735, 1.40, 18, "l"),       # ir:CO-ester
              (1238, 1.30, 25, "l")],      # ir:ethylethanoate-COC
    "amine": [(3370, 0.40, 30, "l"),       # ir:NH (3300-3500), two bands of -NH2
              (3300, 0.35, 30, "l"),
              (2960, 0.55, 35, "l")],      # ir:CH
}
NAMES = ("ethanolL", "ethanolG", "propanone", "acid", "ester", "amine")


def absorbance(name, sigma):
    a = 0.0
    for c, h, w, shape in BANDS[name]:
        x = (sigma - c) / w
        a += h * (math.exp(-0.5 * x * x) if shape == "g" else 1.0 / (1.0 + x * x))
    return a


def transmittance(name, sigma):
    return 100.0 * 10.0 ** (-absorbance(name, sigma))


def table(lo=500, hi=4000, step=5):
    return [(s,) + tuple(round(transmittance(n, s), 2) for n in NAMES)
            for s in range(hi, lo - 1, -step)]


def minimum(name, lo, hi):
    """Wavenumber of the lowest transmittance in [lo, hi] (1 cm-1 grid)."""
    return min(range(lo, hi + 1), key=lambda s: transmittance(name, s))


if __name__ == "__main__":
    write_table(__file__, ("sigma",) + NAMES, table(), digits=5)
