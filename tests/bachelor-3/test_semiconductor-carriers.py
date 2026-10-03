import importlib.util
import math
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("sc", os.path.join(D, "semiconductor-carriers.py"))
sc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sc)


def test_intrinsic_values_at_300K():
    assert 0.7e10 < sc.ni("Si", 300) < 1.3e10
    assert 1.5e13 < sc.ni("Ge", 300) < 2.6e13


def test_slope_is_half_the_gap():
    # ln(ni / T^1.5) against 1/T has slope -Eg/2k with Eg the gap extrapolated
    # linearly to 0 K, close to the Varshni E0 (the T^1.5 factor removed).
    t1, t2 = 300.0, 350.0
    f = lambda t: math.log(sc.ni("Si", t) / t ** 1.5)
    s = (f(t2) - f(t1)) / (1 / t2 - 1 / t1)
    e_apparent = -2 * sc.K_EV * s
    assert abs(e_apparent - sc.value("eg:Si.E0")) / sc.value("eg:Si.E0") < 0.05


def test_saturation_at_ND_and_regimes():
    assert abs(sc.doped_n(300) / sc.ND - 1) < 0.02
    assert sc.doped_n(40) < 0.3 * sc.ND           # freeze-out
    assert sc.doped_n(800) > 3 * sc.ND            # intrinsic regime
