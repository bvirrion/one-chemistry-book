import importlib.util
import os

spec = importlib.util.spec_from_file_location("lv", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "liquid-vapour.py"))
lv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lv)
K0 = 273.15


def test_antoine_reproduces_boiling_points():
    assert abs(lv.tsat("benzene") - lv.value("tb:benzene")) < 0.2
    assert abs(lv.tsat("toluene") - lv.value("tb:toluene")) < 1.0
    assert abs(lv.tsat("water") - lv.value("tb:H2O.atm")) < 0.1


def test_ideal_diagram():
    T, y = lv.bubble(0.5, "benzene", "toluene")
    assert 91.5 < T - K0 < 92.5 and 0.70 < y < 0.73
    # dew point of the vapour y = 0.714 is the bubble point of x = 0.5
    Td, x = lv.ideal_dew(y, "benzene", "toluene")
    assert abs(Td - T) < 1e-6 and abs(x - 0.5) < 1e-6


def test_fenske_and_staircase():
    assert round(lv.fenske(), 1) == 6.5
    path, n = lv.staircase()
    assert n == 7 and path[-1][0] < 0.05


def test_azeotrope_model():
    x = lv.azeotrope_mole_fraction()
    assert abs(x - 0.881) < 0.001
    A, T = lv.ethanol_water_model()
    # at the fitted azeotrope, vapour and liquid have the same composition
    Tb, y = lv.bubble(x, "ethanol", "water", A)
    assert abs(Tb - T) < 1e-6 and abs(y - x) < 1e-6
    assert T < lv.tsat("ethanol")


def test_steam_distillation():
    T = lv.steam_temperature()
    assert 84 < T - K0 < 85 and T < lv.tsat("toluene") and T < lv.tsat("water")
    assert 4.0 < lv.steam_mass_ratio() < 4.2
