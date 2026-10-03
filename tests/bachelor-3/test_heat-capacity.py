import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("hc", os.path.join(D, "heat-capacity.py"))
hc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hc)
sm = hc.cv_h2.__globals__


def test_limits():
    assert abs(hc.cv_h2(10, "normal") - 1.5) < 1e-3          # rotation frozen
    assert abs(hc.cv_diatomic("N2", 300) - 2.5) < 0.01       # rotation classical, vibration frozen
    assert abs(hc.cv_diatomic("Cl2", 1e5) - 3.5) < 1e-3      # equipartition limit 7/2
    assert abs(hc.cv_h2(500, "normal") - hc.cv_h2(500, "equilibrium")) < 1e-6


def test_hydrogen_anomaly():
    eq = [hc.cv_h2(T, "equilibrium") for T in range(20, 300)]
    peak = max(eq)
    assert 3.4 < peak < 3.7 and 40 < 20 + eq.index(peak) < 70     # equilibrium H2 overshoots 5/2
    nrm = [hc.cv_h2(T, "normal") for T in range(20, 300)]
    assert max(nrm) < 2.5 and all(b >= a - 1e-9 for a, b in zip(nrm, nrm[1:]))


def test_against_janaf():
    for T, n2, cl2 in hc.janaf_rows():
        if T <= 1000:
            assert abs(hc.cv_diatomic("N2", T) - n2) < 0.02
            assert abs(hc.cv_diatomic("Cl2", T) - cl2) < 0.06
