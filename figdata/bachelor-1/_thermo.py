"""Equilibrium constants and standard potentials computed from the NBS-82
standard Gibbs energies of formation in the ledger (rows dfg:...).

    dfg("NH4+(ao)")                      -> -79.31 (kJ/mol)
    pK({"NH4+(ao)": -1, "NH3(ao)": 1, "H+(ao)": 1})   -> 9.25
    e0({"Cu2+(ao)": -1, "Cu(cr)": 1}, n=2)            -> 0.34 V

A reaction is a dict species -> stoichiometric number (negative for
reactants). Electrons are left out of the dict; e0 takes their number n
for a reduction Ox + n e- -> Red written with the standard hydrogen
electrode as reference (H+ and H2 have zero Gibbs energy of formation).
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _ledger import value, _load  # noqa: E402

T = 298.15


def _key(species):
    return "dfg:" + species.replace("(", "_").replace(")", "").replace("^", "")


# elements in their reference state: zero by definition, no ledger row needed
REFERENCE_ELEMENTS = {
    "H2(g)", "O2(g)", "N2(g)", "F2(g)", "Cl2(g)", "Br2(l)", "I2(cr)", "S(cr)", "C(cr)",
    "Li(cr)", "Na(cr)", "K(cr)", "Mg(cr)", "Ca(cr)", "Ba(cr)", "Al(cr)", "Zn(cr)",
    "Fe(cr)", "Ni(cr)", "Pb(cr)", "Cu(cr)", "Ag(cr)", "Hg(l)", "Mn(cr)", "Cr(cr)",
}


def dfg(species):
    """Gibbs energy of formation in kJ/mol; elements in their reference state are 0."""
    if species in REFERENCE_ELEMENTS:
        return 0.0
    k = _key(species)
    if k in _load():
        return value(k)
    raise KeyError(species)


def drg(reaction):
    return sum(nu * dfg(sp) for sp, nu in reaction.items())


def rt_ln10():
    return value("const:R") * T * math.log(10) / 1000      # kJ/mol


def pK(reaction):
    """-log10 K for the reaction."""
    return drg(reaction) / rt_ln10()


def e0(reaction, n):
    """Standard potential (V) of the reduction written in `reaction` with n electrons."""
    return -drg(reaction) * 1000 / (n * value("const:F"))
