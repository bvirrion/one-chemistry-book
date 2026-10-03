"""Boiling temperature against pressure (chapter 35), integrated
Clausius-Clapeyron equation with a constant enthalpy of vaporisation:
1/T = 1/T_b - R ln(p/p_ref)/dvapH, from the ledger rows of bromobenzene and
benzaldehyde (reference: the boiling point at 1.01325 bar for bromobenzene,
at 1.00 bar for benzaldehyde). Columns: p in mbar, T in degC for each liquid."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _ledger import value
from _table import write_table

R = 8.314462618
LIQUIDS = {  # name: (T_b / K, p_ref / bar, dvapH / J/mol)
    "bromobenzene": ("tb:bromobenzene", 1.01325, "dvap:bromobenzene"),
    "benzaldehyde": ("tb:benzaldehyde", 1.00, "dvap:benzaldehyde"),
}


def t_boil(name, p_bar):
    tb, pref, dh = LIQUIDS[name]
    inv = 1 / value(tb) - R * math.log(p_bar / pref) / (1000 * value(dh))
    return 1 / inv


if __name__ == "__main__":
    ps = [5 * 1.2 ** k for k in range(0, 31) if 5 * 1.2 ** k <= 1100] + [1013.25]
    rows = [(p, t_boil("bromobenzene", p / 1000) - 273.15, t_boil("benzaldehyde", p / 1000) - 273.15)
            for p in sorted(ps)]
    write_table(__file__, ("p", "bromobenzene", "benzaldehyde"), rows)
