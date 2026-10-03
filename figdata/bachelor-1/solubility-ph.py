"""Solubility of the amphoteric hydroxides of zinc and aluminium against pH
(ch. 11), and the pH at which each metal hydroxide starts and finishes
precipitating from a 0.010 mol/L solution. Constants computed from NBS-82
Gibbs energies in aqueous-constants.py.

Two-species model (printed as the solid curve): the free ion M^n+ and the
hydroxo complex M(OH)_(n+1)^-, so that
    s = Ks/[OH-]^n + K [OH-]       with K = beta Ks  (equilibrium solid + OH-).
For zinc the 'full' column adds ZnOH+, Zn(OH)2(aq) and Zn(OH)3-.
"""
import importlib.util
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "aqc", os.path.join(os.path.dirname(__file__), "aqueous-constants.py"))
aqc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(aqc)

PKE = aqc.pka("water")


def zinc(ph):
    """(log s model, log s full, log [Zn2+], log [Zn(OH)4^2-]) at this pH."""
    loh = ph - PKE
    lzn = -aqc.pks("ZnOH2") - 2 * loh
    l4 = lzn + aqc.logb("ZnOH4") + 4 * loh
    model = math.log10(10 ** lzn + 10 ** l4)
    full = math.log10(10 ** lzn + 10 ** l4
                      + 10 ** (lzn + aqc.logb("ZnOH") + loh)
                      + 10 ** (lzn + aqc.logb("ZnOH2aq") + 2 * loh)
                      + 10 ** (lzn + aqc.logb("ZnOH3") + 3 * loh))
    return model, full, lzn, l4


def aluminium(ph):
    loh = ph - PKE
    lal = -aqc.pks("AlOH3") - 3 * loh
    l4 = lal + aqc.logb("AlOH4") + 4 * loh
    return math.log10(10 ** lal + 10 ** l4), lal, l4


def ph_start(pks, n, c):
    """pH at which M(OH)n starts to precipitate from c mol/L of M^n+."""
    return PKE - (pks + math.log10(c)) / n


THRESHOLDS = [   # (row, label, solid key, charge)
    (1, "Fe3+", "FeOH3", 3), (2, "Al3+", "AlOH3", 3), (3, "Zn2+", "ZnOH2", 2),
    (4, "Fe2+", "FeOH2", 2), (5, "Mg2+", "MgOH2", 2), (6, "Ca2+", "CaOH2", 2)]


def thresholds(c=0.010):
    return [(i, lab, ph_start(aqc.pks(k), n, c), ph_start(aqc.pks(k), n, c / 1000))
            for i, lab, k, n in THRESHOLDS]


def zinc_redissolved(c):
    """pH above which c mol/L of zinc is entirely in solution as Zn(OH)4^2-."""
    lk = aqc.logb("ZnOH4") - aqc.pks("ZnOH2")       # Zn(OH)2 + 2 OH- = Zn(OH)4^2-
    return PKE + (math.log10(c) - lk) / 2


if __name__ == "__main__":
    rows = [(x / 20,) + zinc(x / 20) for x in range(120, 281)]
    write_table(__file__, ("pH", "model", "full", "Zn", "ZnOH4"), rows, part="zinc")
    rows = [(x / 20,) + aluminium(x / 20) for x in range(50, 281)]
    write_table(__file__, ("pH", "model", "Al", "AlOH4"), rows, part="aluminium")
    write_table(__file__, ("row", "ion", "start", "end"), thresholds(), part="thresholds")
