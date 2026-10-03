import importlib.util
import math
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("ob", os.path.join(D, "oxygen-binding.py"))
ob = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ob)


def test_half_saturation_at_p50():
    assert abs(ob.hb(ob.P50_HB) - 0.5) < 1e-12
    assert abs(ob.mb(ob.P50_MB) - 0.5) < 1e-12


def test_hill_slope_is_n():
    h = 1e-4
    f = lambda lp: math.log10(ob.hb(10 ** lp) / (1 - ob.hb(10 ** lp)))
    lp = math.log10(ob.P50_HB)
    assert abs((f(lp + h) - f(lp - h)) / (2 * h) - ob.N_HB) < 1e-6


def test_bohr_shift_releases_oxygen():
    assert ob.hb(5, ob.P50_HB_ACID) < ob.hb(5)
    assert ob.mb(5) > 0.9
