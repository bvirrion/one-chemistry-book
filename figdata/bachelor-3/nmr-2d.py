"""Ch. 8, peak lists of the COSY, HSQC and HMBC spectra of ethyl butanoate,
built at the ledger shifts. Protons: a OCH2 (4.13), b CH2C=O (2.28),
c CH2 (1.66), d OCH2CH3 (1.25), e CH3 (0.95). Carbons: C=O, OCH2, CH2C=O,
CH2, OCH2CH3, CH3. COSY cross peaks join protons three bonds apart (vicinal,
3J ~ 7 Hz); HSQC peaks join each proton to its own carbon; HMBC peaks join
protons to carbons two or three bonds away."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

H = {"a": "nmr:ethylbutanoate-OCH2", "b": "nmr:ethylbutanoate-CH2CO", "c": "nmr:ethylbutanoate-CH2",
     "d": "nmr:ethylbutanoate-OCH2CH3", "e": "nmr:ethylbutanoate-CH3"}
C = {"CO": "c13:ethylbutanoate.CO", "a": "c13:ethylbutanoate.OCH2", "b": "c13:ethylbutanoate.CH2CO",
     "c": "c13:ethylbutanoate.CH2", "d": "c13:ethylbutanoate.OCH2CH3", "e": "c13:ethylbutanoate.CH3"}
# skeleton: CH3(e)-CH2(c)-CH2(b)-C(=O)-O-CH2(a)-CH3(d); bonds between heavy atoms
CHAIN = ["e", "c", "b", "CO", "O", "a", "d"]


def bonds_between(x, y):
    """number of bonds between the carbons (or O) x and y along the chain"""
    return abs(CHAIN.index(x) - CHAIN.index(y))


def cosy_pairs():
    """protons on adjacent carbons: H-C-C-H, three bonds"""
    hs = list(H)
    return [(p, q) for p in hs for q in hs if p != q and bonds_between(p, q) == 1]


def hsqc_pairs():
    return [(p, p) for p in H]


def hmbc_pairs():
    """proton p (on carbon p) to carbon k two or three bonds away: carbon distance 1 or 2"""
    return [(p, k) for p in H for k in C if k != p and bonds_between(p, k) in (1, 2)]


if __name__ == "__main__":
    rows = [(value(H[p]), value(H[p])) for p in H]
    write_table(__file__, ("h1", "h2"), rows, part="cosy-diag")
    write_table(__file__, ("h1", "h2"), [(value(H[p]), value(H[q])) for p, q in cosy_pairs()], part="cosy-cross")
    write_table(__file__, ("h", "c"), [(value(H[p]), value(C[k])) for p, k in hsqc_pairs()], part="hsqc")
    write_table(__file__, ("h", "c"), [(value(H[p]), value(C[k])) for p, k in hmbc_pairs()], part="hmbc")
