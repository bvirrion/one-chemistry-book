import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("ar", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "arrhenius.py"))
ar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ar)


def test_slope_is_minus_ea_over_r():
    assert abs(ar.slope() * ar.value("const:R") + ar.activation_energy()) < 1e-9
    assert round(ar.activation_energy() / 1000) == 85


def test_middle_point_on_the_line():
    assert abs(math.log(ar.k_at(50)) - math.log(0.00348)) < 0.01


def test_printed_values():
    k25 = ar.k_at(25)
    assert round(k25 * 1e4, 2) == 2.46
    assert round(math.log(10 / 9) / k25) == 428
