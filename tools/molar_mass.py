#!/usr/bin/env python3
"""Molar masses from the ledger's standard atomic weights.

    python3 tools/molar_mass.py CuSO4.5H2O C2H5OH "Fe2(SO4)3"

Every molar mass printed in the book, and every number computed from one, is
taken from this tool -- never typed from memory. It prints the value from the
ledger's atomic weights (sources/data_ledger.md, rows aw:<Symbol>) and the
value the book prints, rounded to 0.1 g/mol (the book's convention: atomic
weights quoted to 0.1 g/mol, e.g. H 1.0, C 12.0, O 16.0, Cl 35.5).
"""
import decimal
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chem  # noqa: E402


def book_weights():
    """The atomic weights the book quotes: ledger values rounded to 0.1."""
    # half-up on the decimal text, not float round(): 35.45 must give 35.5
    q = decimal.Decimal("0.1")
    return {el: float(decimal.Decimal(repr(w)).quantize(q, decimal.ROUND_HALF_UP))
            for el, w in chem.atomic_weights().items()}


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    w, wb = chem.atomic_weights(), book_weights()
    for f in argv:
        m = chem.molar_mass(f, w)
        mb = chem.molar_mass(f, wb)
        print("%-20s M = %10.4f g/mol   (book, from 0.1-rounded weights: %.1f g/mol)"
              % (f, m, mb))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
