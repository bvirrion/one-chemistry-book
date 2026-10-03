"""Distribution diagrams (fractions of each acid-base form against pH) of
ethanoic acid and phosphoric acid (ch. 10). pKa values from the ledger
(IUPAC dataset for ethanoic acid, NBS-82 Gibbs energies for phosphoric
acid, through aqueous-constants)."""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "aqc", os.path.join(os.path.dirname(__file__), "aqueous-constants.py"))
_aqc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_aqc)


def fractions(ph, pkas):
    """Fractions of H_nA, H_(n-1)A, ..., A for the given pKa list."""
    h = 10 ** -ph
    ks = [10 ** -p for p in pkas]
    terms, prod = [], 1.0
    n = len(ks)
    for i in range(n + 1):
        terms.append(prod * h ** (n - i))
        if i < n:
            prod *= ks[i]
    s = sum(terms)
    return [t / s for t in terms]


def pka_ethanoic():
    return [value("pka:ethanoic")]


def pka_phosphoric():
    return [_aqc.pka("phosphoric1"), _aqc.pka("phosphoric2"), _aqc.pka("phosphoric3")]


if __name__ == "__main__":
    rows = [(i / 20,) + tuple(fractions(i / 20, pka_ethanoic())) for i in range(0, 281)]
    write_table(__file__, ("pH", "HA", "A"), rows, part="ethanoic")
    rows = [(i / 20,) + tuple(fractions(i / 20, pka_phosphoric())) for i in range(0, 281)]
    write_table(__file__, ("pH", "H3A", "H2A", "HA", "A"), rows, part="phosphoric")
