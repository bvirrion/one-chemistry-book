"""Ligand-field stabilisation (chapter 19). Octahedral crystal-field model:
t2g at -0.4 Delta_o, eg at +0.6 Delta_o. For d^n, high spin (Hund, then
pair) and low spin (fill t2g first): CFSE in units of Delta_o (pairing
energies not included; the number of extra pairs is reported)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402


def configuration(n, low_spin):
    """(t2g electrons, eg electrons, unpaired electrons)."""
    if low_spin:
        t = min(n, 6)
        e = n - t
    else:
        if n <= 3:
            t, e = n, 0
        elif n <= 5:
            t, e = 3, n - 3
        elif n <= 8:
            t, e = n - 2, 2
        else:
            t, e = 6, n - 6
    unpaired = (t if t <= 3 else 6 - t) + (e if e <= 2 else 4 - e)
    return t, e, unpaired


def cfse(n, low_spin):
    t, e, _ = configuration(n, low_spin)
    return round(-0.4 * t + 0.6 * e, 10) + 0.0


if __name__ == "__main__":
    rows = [(n, cfse(n, False), cfse(n, True)) for n in range(0, 11)]
    write_table(__file__, ("n", "high", "low"), rows, part="a")
