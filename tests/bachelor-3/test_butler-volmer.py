import importlib.util
import math
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("bv", os.path.join(D, "butler-volmer.py"))
bv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bv)


def test_tafel_slope_and_linear_region():
    eta = 0.25
    slope = (math.log10(bv.bv(eta + 0.01, 0.5)) - math.log10(bv.bv(eta, 0.5))) / 0.01
    assert abs(1000 / slope - bv.tafel_slope_mV(0.5)) < 0.5
    assert round(bv.tafel_slope_mV(0.5)) == 118
    # low overpotential: i/i0 = f eta, so R_ct i0 = RT/F
    assert abs(bv.bv(1e-5, 0.3) / 1e-5 - bv.f()) < 1e-3 * bv.f()
