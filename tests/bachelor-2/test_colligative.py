import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("c", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "colligative.py"))
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def test_constants():
    assert round(c.dfus_molar() / 1000, 2) == 6.01
    assert round(c.kf(), 2) == 1.86
    assert round(c.kb(), 3) == 0.513
    assert round(c.debye_huckel_a(), 2) == 0.51


def test_glycol():
    x = c.water_fraction_for(253.15)
    assert abs(c.freezing_point_ideal(x) - 253.15) < 1e-9
    assert round(x, 3) == 0.811
    assert round(c.glycol_mass_fraction(x), 2) == 0.44
    assert round(c.glycol_mass_fraction_dilute(20.0), 2) == 0.40


def test_seawater():
    t, b = c.seawater_freezing()
    assert round(t, 1) == -2.3 and round(b, 2) == 1.24
