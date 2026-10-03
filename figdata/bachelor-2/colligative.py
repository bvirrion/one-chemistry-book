"""Cryoscopic and ebullioscopic constants of water, the Debye-Hueckel
coefficient A at 25 degC, and the freezing of water-ethane-1,2-diol mixtures
(ideal-mixture model), from ledger rows. No curve: the printed numbers of
chapter 3 are pinned by tests/bachelor-2/test_colligative.py."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _ledger import value  # noqa: E402

R = value("const:R")
M_W = 2 * value("aw:H") + value("aw:O")            # g/mol
M_GLYCOL = 2 * value("aw:C") + 6 * value("aw:H") + 2 * value("aw:O")


def dfus_molar():
    """Enthalpy of fusion of ice, J/mol."""
    return value("dfus:H2O") * M_W        # kJ/kg * g/mol = J/mol


def kf():
    T = value("tfus:H2O")
    return R * T * T * (M_W / 1000.0) / dfus_molar()


def kb():
    T = value("tb:H2O.atm")
    return R * T * T * (M_W / 1000.0) / (value("dvap:H2O.nbp") * 1000.0)


def debye_huckel_a(T=298.15):
    """A of log10 g = -A |z+ z-| sqrt(I), I in mol/kg."""
    e = value("const:e")
    eps = value("const:eps0") * value("epsr:H2O")
    kB = value("const:kB")
    NA = value("const:NA")
    rho = value("rho:water.298")          # kg/m3
    # kappa^2 = 2 e^2 NA rho I / (eps kB T) with I in mol/kg -> mol/m3 via rho
    lb = e * e / (4 * math.pi * eps * kB * T)  # Bjerrum length, m
    return (lb ** 1.5) * math.sqrt(2 * math.pi * NA * rho) / math.log(10)


def freezing_point_ideal(x_water):
    """Freezing temperature of the solvent in an ideal mixture (solid = pure
    ice): ln x = -(DfusH/R)(1/T - 1/T*)."""
    T0 = value("tfus:H2O")
    return 1.0 / (1.0 / T0 - R * math.log(x_water) / dfus_molar())


def water_fraction_for(T):
    T0 = value("tfus:H2O")
    return math.exp(-dfus_molar() / R * (1.0 / T - 1.0 / T0))


def glycol_mass_fraction(x_water):
    xg = 1.0 - x_water
    return xg * M_GLYCOL / (xg * M_GLYCOL + x_water * M_W)


def glycol_mass_fraction_dilute(dT):
    """Dilute linear law dT = Kf b."""
    b = dT / kf()                         # mol/kg
    return b * M_GLYCOL / (1000.0 + b * M_GLYCOL)


def seawater_freezing():
    """35 g of salt per kg of sea water, as NaCl (2 particles), dilute law."""
    m_salt = value("sea:salinity")
    m_nacl = value("aw:Na") + value("aw:Cl")
    b = 2 * (m_salt / m_nacl) / ((1000.0 - m_salt) / 1000.0)
    return -kf() * b, b
