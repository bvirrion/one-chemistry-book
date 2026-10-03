"""Every standard reaction quantity printed in the thermochemistry chapters of
the Year 2 volume (enthalpies, entropies, Gibbs energies, equilibrium
constants), computed from the ledger's rows (CODATA key values, JANAF,
WebBook). The values printed in the chapters are those of this table,
rounded; tests/bachelor-2/test_thermo-data.py pins them."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

R = value("const:R")
T0 = 298.15

# species -> (ledger id of DfH in kJ/mol or None for an element in its
# reference state, ledger id of S in J/(K mol) or None)
SP = {
    "H2O(l)": ("dfh:H2O-l", "s0:H2O_l"),
    "H2O(g)": ("dfh:H2O_g", "s0:H2O_g"),
    "CO2(g)": ("dfh:CO2", "s0:CO2_g"),
    "CO(g)": ("dfh:CO_g", "s0:CO_g"),
    "O2(g)": (None, "s0:O2_g"),
    "N2(g)": (None, "s0:N2_g"),
    "H2(g)": (None, "s0:H2_g"),
    "C(gr)": (None, "s0:C_gr"),
    "Cl2(g)": (None, "s0:Cl2_g"),
    "Na(cr)": (None, "s0:Na_cr"),
    "C(g)": ("dfh:C_g", None),
    "H(g)": ("janaf:H", None),
    "O(g)": ("dfh:O_g", None),
    "N(g)": ("dfh:N_g", None),
    "Cl(g)": ("janaf:Cl", None),
    "Na(g)": ("dfh:Na_g", None),
    "HCl(g)": ("janaf:HCl", None),
    "NH3(g)": ("dfh:NH3_g", "s0:NH3_g"),
    "NO(g)": ("dfh:NO_g", "s0:NO_g"),
    "CH4(g)": ("dfh:CH4_g", "s0:CH4_g"),
    "C2H6(g)": ("dfh:C2H6_g", None),
    "C2H4(g)": ("dfh:C2H4_g", None),
    "C3H8(g)": ("dfh:C3H8_g", None),
    "C4H10(g)": ("dfh:C4H10_g", None),
    "C8H18(l)": ("dfh:C8H18", None),
    "C6H6(l)": ("dfh:C6H6_l", None),
    "NaCl(cr)": ("dfh:NaCl_cr", "s0:NaCl_cr"),
    "CaCO3(cr)": ("dfh:CaCO3_cr", "s0:CaCO3_cr"),
    "CaO(cr)": ("dfh:CaO_cr", "s0:CaO_cr"),
    "NH4NO3(cr)": ("dfh:NH4NO3_cr", "s0:NH4NO3_cr"),
    "NH4NO3(ai)": ("dfh:NH4NO3_ai", "s0:NH4NO3_ai"),
    "N2O4(g)": ("dfh:N2O4_g", "s0:N2O4_g"),
    "NO2(g)": ("dfh:NO2_g", "s0:NO2_g"),
    "TiO2(cr)": ("dfh:TiO2_cr", "s0:TiO2_cr"),
    "TiCl4(g)": ("dfh:TiCl4_g", "s0:TiCl4_g"),
}


def dfh(sp):
    k = SP[sp][0]
    return 0.0 if k is None else value(k)


def s0(sp):
    return value(SP[sp][1])


def dfh_ethanol_l():
    """DfH of liquid ethanol from its measured combustion enthalpy."""
    return 2 * dfh("CO2(g)") + 3 * dfh("H2O(l)") + value("dch:C2H5OH")


REACTIONS = {
    # chapter 1
    "methane-combustion-l": {"CH4(g)": -1, "O2(g)": -2, "CO2(g)": 1, "H2O(l)": 2},
    "methane-combustion-g": {"CH4(g)": -1, "O2(g)": -2, "CO2(g)": 1, "H2O(g)": 2},
    "butane-combustion-l": {"C4H10(g)": -1, "O2(g)": -6.5, "CO2(g)": 4, "H2O(l)": 5},
    "butane-combustion-g": {"C4H10(g)": -1, "O2(g)": -6.5, "CO2(g)": 4, "H2O(g)": 5},
    "propane-combustion-l": {"C3H8(g)": -1, "O2(g)": -5, "CO2(g)": 3, "H2O(l)": 4},
    "octane-combustion-l": {"C8H18(l)": -1, "O2(g)": -12.5, "CO2(g)": 8, "H2O(l)": 9},
    "co-combustion": {"CO(g)": -1, "O2(g)": -0.5, "CO2(g)": 1},
    "c-to-co": {"C(gr)": -1, "O2(g)": -0.5, "CO(g)": 1},
    "c-to-co2": {"C(gr)": -1, "O2(g)": -1, "CO2(g)": 1},
    "ammonia-synthesis": {"N2(g)": -1, "H2(g)": -3, "NH3(g)": 2},
    "no-formation": {"N2(g)": -0.5, "O2(g)": -0.5, "NO(g)": 1},
    "water-vaporisation": {"H2O(l)": -1, "H2O(g)": 1},
    "hydrogen-combustion-l": {"H2(g)": -1, "O2(g)": -0.5, "H2O(l)": 1},
    "ethene-hydrogenation": {"C2H4(g)": -1, "H2(g)": -1, "C2H6(g)": 1},
    "benzene-combustion-l": {"C6H6(l)": -1, "O2(g)": -7.5, "CO2(g)": 6, "H2O(l)": 3},
    # chapter 2
    "calcite-decomposition": {"CaCO3(cr)": -1, "CaO(cr)": 1, "CO2(g)": 1},
    "nh4no3-dissolution": {"NH4NO3(cr)": -1, "NH4NO3(ai)": 1},
    "n2o4-dissociation": {"N2O4(g)": -1, "NO2(g)": 2},
    "methane-formation": {"C(gr)": -1, "H2(g)": -2, "CH4(g)": 1},
    "rutile-chlorination": {"TiO2(cr)": -1, "Cl2(g)": -2, "TiCl4(g)": 1, "O2(g)": 1},
}


def inversion_temperature(rx):
    """Temperature at which DrG = 0 in the Ellingham approximation, K."""
    return drH(rx) * 1000.0 / drS(rx)


def drH(rx):
    return sum(nu * dfh(sp) for sp, nu in REACTIONS[rx].items())


def drS(rx):
    return sum(nu * s0(sp) for sp, nu in REACTIONS[rx].items())


def drG(rx, T=T0):
    return drH(rx) - T * drS(rx) / 1000.0


def K(rx, T=T0):
    return math.exp(-drG(rx, T) * 1000.0 / (R * T))


def mean_bond(molecule, atoms, nbonds, other=0.0):
    """Mean bond enthalpy: atomisation enthalpy (minus the enthalpy of the
    other bonds, `other`) divided by the number of equal bonds."""
    atomisation = sum(n * dfh(a) for a, n in atoms.items()) - dfh(molecule)
    return (atomisation - other) / nbonds


def bonds():
    ch = mean_bond("CH4(g)", {"C(g)": 1, "H(g)": 4}, 4)
    return {
        "H-H": 2 * dfh("H(g)"),
        "O=O": 2 * dfh("O(g)"),
        "N#N": 2 * dfh("N(g)"),
        "Cl-Cl": 2 * dfh("Cl(g)"),
        "H-Cl": dfh("H(g)") + dfh("Cl(g)") - dfh("HCl(g)"),
        "C-H": ch,
        "O-H": mean_bond("H2O(g)", {"O(g)": 1, "H(g)": 2}, 2),
        "N-H": mean_bond("NH3(g)", {"N(g)": 1, "H(g)": 3}, 3),
        "C=O": mean_bond("CO2(g)", {"C(g)": 1, "O(g)": 2}, 2),
        "C-C": mean_bond("C2H6(g)", {"C(g)": 2, "H(g)": 6}, 1, other=6 * ch),
        "C=C": mean_bond("C2H4(g)", {"C(g)": 2, "H(g)": 4}, 1, other=4 * ch),
    }


def born_haber_nacl():
    """Lattice enthalpy of NaCl, NaCl(cr) -> Na+(g) + Cl-(g), kJ/mol. The
    ionisation energy and electron affinity are 0 K energies; their 5/2 RT
    corrections cancel in the sum."""
    ev = value("const:eV") * value("const:NA") / 1000.0
    ie = value("ie:Na") * ev
    ea = value("ea:Cl") * ev
    return -dfh("NaCl(cr)") + dfh("Na(g)") + dfh("Cl(g)") + ie - ea, ie, ea


def kirchhoff_ammonia(T=700.0):
    """DrH of 2 NH3 synthesis at T with a constant DrCp (298 values), and the
    JANAF value 2 DfH(NH3, T)."""
    dcp = 2 * value("cp:NH3_g.298") - value("cp:N2_g.298") - 3 * value("cp:H2_g.298")
    est = drH("ammonia-synthesis") + dcp * (T - T0) / 1000.0
    return est, 2 * value("janafdfH:NH3.700"), dcp


def table():
    rows = []
    for rx in REACTIONS:
        try:
            s = drS(rx)
        except (KeyError, TypeError):
            s = float("nan")
        rows.append((rx, drH(rx), s))
    return rows


def calcite_lines():
    """DrH and T DrS of the calcite decomposition against T (Ellingham
    approximation), kJ/mol: they cross at the inversion temperature."""
    h, s = drH("calcite-decomposition"), drS("calcite-decomposition")
    return [(T, h, T * s / 1000.0) for T in range(0, 1601, 100)]


if __name__ == "__main__":
    write_table(__file__, ("T", "DrH", "TDrS"), calcite_lines(), part="calcite")
    write_table(__file__, ("reaction", "DrH_kJ", "DrS_JK"), table())
    write_table(__file__, ("bond", "H_kJ"), sorted(bonds().items()), part="bonds")
