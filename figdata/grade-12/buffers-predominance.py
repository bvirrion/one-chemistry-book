"""Distribution diagrams and buffer action (grade 12).

Computed from the ledger pKa values (pka:ethanoic 4.76, pka:glycine1 2.35,
pka:glycine2 9.78); the buffer experiment is exercise data.
  part a: pH, fraction of CH3COOH, fraction of CH3COO-
  part b: pH, fractions of glycine's cation, zwitterion and anion
  part c: volume of HCl 0.10 mol/L added (mL), pH of 100 mL of water,
          pH of 100 mL of buffer (0.10 mol/L CH3COOH + 0.10 mol/L CH3COO-)
"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table

PKA_AC = 4.76
PKA_G1, PKA_G2 = 2.35, 9.78


def frac_acid(ph, pka=PKA_AC):
    return 1.0 / (1.0 + 10 ** (ph - pka))


def glycine(ph):
    h = 10 ** (-ph)
    k1, k2 = 10 ** (-PKA_G1), 10 ** (-PKA_G2)
    d = h * h + k1 * h + k1 * k2
    return h * h / d, k1 * h / d, k1 * k2 / d


def ph_water(v_ml, c=0.10, v0=100.0):
    n = c * v_ml / 1000.0
    if n == 0:
        return 7.0
    return -math.log10(n / ((v0 + v_ml) / 1000.0))


def ph_buffer(v_ml, c=0.10, n0=0.010):
    n = c * v_ml / 1000.0
    return PKA_AC + math.log10((n0 - n) / (n0 + n))


def table_a():
    return [(round(p * 0.05, 2), round(frac_acid(p * 0.05), 4), round(1 - frac_acid(p * 0.05), 4))
            for p in range(0, 281)]


def table_b():
    return [(round(p * 0.05, 2),) + tuple(round(f, 4) for f in glycine(p * 0.05)) for p in range(0, 281)]


def table_c():
    return [(v / 2, round(ph_water(v / 2), 3), round(ph_buffer(v / 2), 3)) for v in range(0, 21)]


if __name__ == "__main__":
    write_table(__file__, ("pH", "HA", "A"), table_a(), part="a", digits=6)
    write_table(__file__, ("pH", "cation", "zwitterion", "anion"), table_b(), part="b", digits=6)
    write_table(__file__, ("V", "water", "buffer"), table_c(), part="c", digits=6)
