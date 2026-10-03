import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("ps", os.path.join(D, "photostationary.py"))
ps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ps)


def test_pss_formula():
    for lam, b in ps.BANDS.items():
        ratio = b["eE"] * b["pEZ"] / (b["eZ"] * b["pZE"])
        assert abs(ps.z_pss(lam) - ratio / (1 + ratio)) < 1e-12
    assert round(ps.z_pss(365), 2) == 0.80 and round(ps.z_pss(440), 2) == 0.16


def test_time_course_reaches_both_states():
    assert abs(ps.z_of_t(60) - ps.z_pss(365)) < 0.01
    assert abs(ps.z_of_t(120) - ps.z_pss(440)) < 0.01
    assert ps.z_of_t(0) == 0
