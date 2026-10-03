"""Ch. 18, magnetism. chi_m T against T for a Curie paramagnet (S = 5/2,
g = 2) and for a model iron(II) spin-crossover compound (high spin S = 2,
low spin S = 0; dH = 15 kJ/mol, dS = 75 J K-1 mol-1: model values, T1/2 =
200 K); and chi_m against 1/T for the Curie paramagnet. Curie constant
C = N_A mu0 g^2 muB^2 S(S+1) / (3 k), here in cm3 K mol-1 (cgs-emu
convention, C = 0.12505 g^2 S(S+1))."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

DH, DS = 15000.0, 75.0


def curie_C(S, g=2.0):
    """cm3 K / mol: N_A muB^2 g^2 S(S+1)/(3k) in cgs-emu"""
    NA, muB, k = value("const:NA"), value("const:muB"), value("const:kB")
    # SI molar chi (m3/mol) = mu0 NA g^2 muB^2 S(S+1)/(3kT); cgs-emu cm3/mol = SI / (4 pi 1e-6)
    mu0 = 4 * math.pi * 1e-7
    return mu0 * NA * g * g * muB ** 2 * S * (S + 1) / (3 * k) / (4 * math.pi * 1e-6)


def x_hs(T):
    R = value("const:R")
    return 1 / (1 + math.exp((DH - T * DS) / (R * T)))


def rows():
    return [(T, curie_C(2.5), x_hs(T) * curie_C(2.0)) for T in range(20, 401, 2)]


if __name__ == "__main__":
    write_table(__file__, ("T", "chiT_para", "chiT_sco"), rows(), part="chiT")
    write_table(__file__, ("invT", "chi"), [(1000 / T, curie_C(2.5) / T) for T in range(10, 401, 2)], part="chi")
    print("C(S=1/2) %.4f C(S=2) %.3f C(5/2) %.3f T1/2 %.0f" % (curie_C(0.5), curie_C(2), curie_C(2.5), DH / DS))
