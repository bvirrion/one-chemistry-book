import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("sr", os.path.join(D, "surface-rates.py"))
sr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sr)


def test_lh_maximum():
    for pb in (0.5, 1, 3):
        pm = sr.pa_max(pb)
        assert sr.lh(pm, pb) > sr.lh(pm * 0.98, pb) and sr.lh(pm, pb) > sr.lh(pm * 1.02, pb)


def test_er_saturates():
    assert abs(sr.er(1e6, 1) - sr.K) < 1e-5
