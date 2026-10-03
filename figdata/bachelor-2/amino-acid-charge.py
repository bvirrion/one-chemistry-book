"""Acid-base behaviour of amino acids (chapter 30), pKa values from the ledger.
- a: net charge against pH for glycine, aspartic acid and lysine (pH 0..14);
- b: fractions of the three forms of glycine (cation, zwitterion, anion).
Each acidic group i of pKa_i is deprotonated to the fraction
1/(1 + 10^(pKa_i - pH)); the net charge sums the charges of all groups."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _ledger import value
from _table import write_table

# (pKa, charge when protonated): carboxylic groups 0 -> -1, ammonium groups +1 -> 0
def groups(name):
    if name == "glycine":
        return [(value("pka:glycine1"), 0), (value("pka:glycine2"), 1)]
    if name == "asp":
        return [(value("pka:asp1"), 0), (value("pka:asp2"), 0), (value("pka:asp3"), 1)]
    if name == "lys":
        return [(value("pka:lys1"), 0), (value("pka:lys2"), 1), (value("pka:lys3"), 1)]
    raise KeyError(name)


def deprotonated(pka, ph):
    return 1 / (1 + 10 ** (pka - ph))


def net_charge(gs, ph):
    return sum(q - deprotonated(pka, ph) for pka, q in gs)


def isoelectric(gs, lo=0.0, hi=14.0):
    """pH of zero net charge, by bisection (charge decreases with pH)."""
    for _ in range(100):
        mid = (lo + hi) / 2
        if net_charge(gs, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def glycine_fractions(ph):
    k1, k2 = 10 ** -value("pka:glycine1"), 10 ** -value("pka:glycine2")
    h = 10 ** -ph
    d = h * h + h * k1 + k1 * k2
    return h * h / d, h * k1 / d, k1 * k2 / d


if __name__ == "__main__":
    phs = [i / 20 for i in range(0, 281)]
    rows = [(ph, net_charge(groups("glycine"), ph), net_charge(groups("asp"), ph),
             net_charge(groups("lys"), ph)) for ph in phs]
    write_table(__file__, ("pH", "gly", "asp", "lys"), rows, part="a")
    write_table(__file__, ("pH", "cation", "zwitterion", "anion"),
                [(ph,) + glycine_fractions(ph) for ph in phs], part="b")
