"""Ch. 11, nuclear-spin isomers at equilibrium: the para fraction of H2
(even J, spin weight 1 against 3) and the ortho fraction of D2 (even J,
spin weight 6 against 3) from 5 to 300 K."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _statmech import para_fraction_h2, ortho_fraction_d2  # noqa: E402


def rows():
    return [(T, para_fraction_h2(T), ortho_fraction_d2(T)) for T in range(5, 301)]


if __name__ == "__main__":
    write_table(__file__, ("T", "pH2", "oD2"), rows())
