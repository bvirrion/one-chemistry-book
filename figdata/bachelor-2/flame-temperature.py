"""Adiabatic flame temperature of a fuel burnt in stoichiometric air at
constant pressure (complete combustion, no dissociation), from the JANAF
enthalpy increments H(T) - H(298.15 K) of the products (ledger rows
janafH:<species>.<T>) and the standard reaction enthalpy at 298.15 K
(thermo-data.py). Part a: enthalpy of the products of one mole of butane
against T; part b: the same for methane."""
import importlib.util
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "thermo", os.path.join(os.path.dirname(__file__), "thermo-data.py"))
thermo = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(thermo)

T0 = 298.15
TGRID = [500, 1000, 1500, 2000, 2100, 2200, 2300, 2400, 2500, 3000]
SPECIES = ("CO2", "H2O", "N2", "O2", "Ar")
FUELS = {   # fuel: (reaction with water as gas, moles of CO2, H2O, O2 needed)
    "butane": ("butane-combustion-g", 4, 5, 6.5),
    "methane": ("methane-combustion-g", 1, 2, 2.0),
}


def increment(sp, T):
    """H(T) - H(298.15 K) of one mole of sp, kJ/mol, linear between the
    tabulated temperatures (enthalpy is nearly linear in T up there)."""
    xs = [T0] + TGRID
    ys = [0.0] + [value("janafH:%s.%d" % (sp, t)) for t in TGRID]
    return float(np.interp(T, xs, ys))


def air_per_o2():
    """Moles of N2 and Ar that accompany one mole of O2 in dry air."""
    o2 = value("air:O2")
    return value("air:N2") / o2, value("air:Ar") / o2


def products(fuel):
    rx, nco2, nh2o, no2 = FUELS[fuel]
    n2, ar = air_per_o2()
    return {"CO2": nco2, "H2O": nh2o, "N2": no2 * n2, "Ar": no2 * ar}


def heat_released(fuel):
    """-DrH(298.15 K), kJ per mole of fuel, water as gas."""
    return -thermo.drH(FUELS[fuel][0])


def products_enthalpy(fuel, T):
    return sum(n * increment(sp, T) for sp, n in products(fuel).items())


def flame_temperature(fuel):
    lo, hi = T0, 3000.0
    q = heat_released(fuel)
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if products_enthalpy(fuel, mid) < q:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def heat_capacity_298(fuel):
    """Heat capacity of the products at 298.15 K, J/K per mole of fuel."""
    cp = {"CO2": "cp:CO2_g.298", "H2O": "cp:H2O_g.298", "N2": "cp:N2_g.298",
          "Ar": "cp:Ar_g.298"}
    return sum(n * value(cp[sp]) for sp, n in products(fuel).items())


def flame_temperature_constant_cp(fuel):
    return T0 + heat_released(fuel) * 1000.0 / heat_capacity_298(fuel)


def curve(fuel):
    return [(T, products_enthalpy(fuel, T)) for T in np.arange(300.0, 3001.0, 50.0)]


if __name__ == "__main__":
    write_table(__file__, ("T", "H"), curve("butane"), part="butane")
    write_table(__file__, ("T", "H"), curve("methane"), part="methane")
