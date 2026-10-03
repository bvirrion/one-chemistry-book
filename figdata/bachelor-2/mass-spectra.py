"""Mass spectra (chapter 32).
- a: isotope clusters of Cl, Cl2, Br, Br2 and ClBr, computed from the ledger
     abundances (iso:Cl35/37, iso:Br79/81) by expanding the binomial products;
     columns: offset (0, 2, 4), then one column per pattern, the most intense
     peak of each pattern set to 100;
- b: EI spectrum of butan-2-one; c: of 1-bromopropane; d: of the unknown of
     the problem (1-bromo-3-chloropropane); sticks read from the ledger rows
     ms:* (NIST WebBook), relative intensities."""
import os
import sys
from itertools import product

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _ledger import text, value
from _table import write_table


def abundances():
    return {"Cl": [(0, value("iso:Cl35")), (2, value("iso:Cl37"))],
            "Br": [(0, value("iso:Br79")), (2, value("iso:Br81"))]}


def cluster(atoms):
    """Relative intensities of M, M+2, ... for a list of atoms such as
    ["Cl", "Br"], as a dict offset -> probability (sums to 1)."""
    ab = abundances()
    out = {}
    for combo in product(*[ab[a] for a in atoms]):
        off = sum(o for o, _ in combo)
        p = 1.0
        for _, f in combo:
            p *= f
        out[off] = out.get(off, 0.0) + p
    return out


def normalised(cl, ref=None):
    m = max(cl.values()) if ref is None else cl[ref]
    return {k: 100 * v / m for k, v in cl.items()}


def sticks(key):
    return [(int(a), float(b)) for a, b in (p.split(":") for p in text(key).split())]


def m_plus_one(n_c, a13=None, a12=None):
    a13 = value("iso:C13") if a13 is None else a13
    a12 = value("iso:C12") if a12 is None else a12
    return n_c * a13 / a12


PATTERNS = [("Cl", ["Cl"]), ("Cl2", ["Cl", "Cl"]), ("Br", ["Br"]), ("Br2", ["Br", "Br"]),
            ("ClBr", ["Cl", "Br"])]

if __name__ == "__main__":
    cols = [normalised(cluster(atoms)) for _, atoms in PATTERNS]
    rows = [(off,) + tuple(c.get(off, 0.0) for c in cols) for off in (0, 2, 4)]
    write_table(__file__, ("off",) + tuple(n for n, _ in PATTERNS), rows, part="a")
    for part, key in (("b", "ms:butanone"), ("c", "ms:bromopropane"), ("d", "ms:bromochloropropane")):
        write_table(__file__, ("mz", "I"), sticks(key), part=part)
