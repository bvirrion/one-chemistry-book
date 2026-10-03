import importlib.util
import os

spec = importlib.util.spec_from_file_location("sl", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "solid-liquid.py"))
sl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sl)
K0 = 273.15


def test_lens_ends_and_order():
    xs, xl = sl.lens(sl.tm("Cu") + 1e-6)
    assert abs(xs) < 1e-4 and abs(xl) < 1e-4
    xs, xl = sl.lens(sl.tm("Ni") - 1e-6)
    assert abs(xs - 1) < 1e-4 and abs(xl - 1) < 1e-4
    # the solid is richer in the higher-melting nickel than the liquid
    for t in (1150, 1250, 1350):
        xs, xl = sl.lens(t + K0)
        assert xs > xl


def test_eutectics():
    T, x = sl.eutectic("benzene", "naphthalene")
    assert -4.0 < T - K0 < -3.0 and 0.12 < x < 0.15
    # both branches meet: the liquid is saturated with both solids
    assert abs(sl.ideal_x("benzene", T) + sl.ideal_x("naphthalene", T) - 1) < 1e-9
    T2, xb = sl.eutectic("Sn", "Bi")
    assert round(T2 - K0) == 120
    assert T2 - K0 < sl.value("eut:Bi-Sn.T")


def test_mass_mole_round_trip():
    w = 0.5697
    x = sl.mole_fraction(w, "Sn", "Bi")
    assert abs(sl.mass_fraction(x, "Sn", "Bi") - w) < 1e-12
