import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("cv", os.path.join(D, "cyclic-voltammetry.py"))
cv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cv)


def test_reversible_wave():
    for v in (0.05, 0.2):
        epc, ipc, epa, ipa = cv.peaks(*cv.simulate(v))
        assert 0.057 <= epa - epc <= 0.060
        assert abs(ipc / cv.randles_sevcik(v) - 1) < 0.01
        assert abs((epa + epc) / 2) < 0.002            # E1/2 = E0'


def test_quasi_reversible_wider():
    epc, ipc, epa, ipa = cv.peaks(*cv.simulate(0.1, k0=2.0e-3))
    assert epa - epc > 0.1
