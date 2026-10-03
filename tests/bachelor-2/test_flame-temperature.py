import importlib.util
import os

spec = importlib.util.spec_from_file_location("flame", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "flame-temperature.py"))
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)


def test_energy_balance_closes():
    for fuel in ("butane", "methane"):
        T = f.flame_temperature(fuel)
        assert abs(f.products_enthalpy(fuel, T) - f.heat_released(fuel)) < 1e-3


def test_printed_values():
    assert round(f.flame_temperature("butane"), -1) == 2400
    assert round(f.flame_temperature("methane"), -1) == 2330
    # constant heat capacity overestimates, since Cp grows with T
    assert f.flame_temperature_constant_cp("butane") > f.flame_temperature("butane") + 400
    assert round(f.heat_capacity_298("butane")) == 1028
    assert round(f.flame_temperature_constant_cp("butane"), -1) == 2880


def test_constant_cp_closed_form():
    fuel = "methane"
    T = f.flame_temperature_constant_cp(fuel)
    assert abs((T - 298.15) * f.heat_capacity_298(fuel) / 1000 - f.heat_released(fuel)) < 1e-9
