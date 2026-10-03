"""First ionisation energies of Z = 1-36 and the successive ionisation
energies of magnesium (ch. 2). Values read from the ledger (NIST ASD)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

SYMBOLS = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe "
           "Co Ni Cu Zn Ga Ge As Se Br Kr").split()


def first_ie():
    """[(Z, symbol, IE1 in eV)] for Z = 1..36."""
    return [(z, s, value("ie:" + s)) for z, s in enumerate(SYMBOLS, 1)]


def successive_mg():
    return [(1, value("ie:Mg")), (2, value("ie2:Mg")), (3, value("ie3:Mg")),
            (4, value("ie4:Mg"))]


if __name__ == "__main__":
    write_table(__file__, ("Z", "IE_eV"), [(z, e) for z, _, e in first_ie()])
    write_table(__file__, ("k", "IE_eV"), successive_mg(), part="mg")
