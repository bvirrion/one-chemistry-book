import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("dr", os.path.join(D, "dose-response.py"))
dr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dr)


def test_half_at_median_dose():
    for n in (2, 6):
        assert abs(dr.response(dr.D50, n) - 0.5) < 1e-12


def test_noael_below_loael():
    no, lo = dr.noael_loael()
    assert no < lo and dr.response(no, 6) < 0.05 <= dr.response(lo, 6)
