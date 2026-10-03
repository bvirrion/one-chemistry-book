"""Ch. 10, Boltzmann populations from spectroscopic constants: rotational
levels of H35Cl and 12C16O at 100, 300 and 1000 K (rigid rotor, exact sum),
and vibrational levels of I2 at 300 and 1000 K (harmonic, levels counted from
the zero-point level). Constants from the ledger through _statmech."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _statmech import theta_rot, theta_vib, populations_rot, populations_vib  # noqa: E402

TEMPS = (100, 300, 1000)


def rot_table(name, jmax):
    th = theta_rot(name)
    cols = [populations_rot(th, T, jmax) for T in TEMPS]
    return [(j,) + tuple(c[j] for c in cols) for j in range(jmax + 1)]


def vib_table(vmax):
    th = theta_vib("I2")
    cols = [populations_vib(th, T, vmax) for T in (300, 1000)]
    return [(v,) + tuple(c[v] for c in cols) for v in range(vmax + 1)]


if __name__ == "__main__":
    write_table(__file__, ("J", "T100", "T300", "T1000"), rot_table("HCl", 14), part="hcl")
    write_table(__file__, ("J", "T100", "T300", "T1000"), rot_table("CO", 40), part="co")
    write_table(__file__, ("v", "T300", "T1000"), vib_table(10), part="i2")
