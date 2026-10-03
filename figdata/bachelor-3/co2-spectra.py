"""Ch. 5, synthetic gas-phase spectra of CO2 built at ledger positions:
infrared absorption (Lorentzian bands, FWHM 30 cm-1, heights proportional
to the ledger intensities) shows only the bend and the antisymmetric
stretch; the Raman spectrum shows only the symmetric stretch (unperturbed
position; in the real spectrum it is split by Fermi resonance). Band shapes
are schematic: no rotational structure."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

W = 15.0       # half width at half maximum, cm-1


def lorentz(x, x0):
    return 1 / (1 + ((x - x0) / W) ** 2)


def ir(x):
    imax = value("ir:CO2.asym.int")
    return (value("ir:CO2.asym.int") * lorentz(x, value("vib:CO2.asym"))
            + value("ir:CO2.bend.int") * lorentz(x, value("vib:CO2.bend"))) / imax


def raman(x):
    return lorentz(x, value("vib:CO2.sym"))


if __name__ == "__main__":
    xs = [400 + 2 * i for i in range(1101)]
    write_table(__file__, ("nu", "ir", "raman"), [(x, ir(x), raman(x)) for x in xs])
