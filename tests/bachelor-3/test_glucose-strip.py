import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("gs", os.path.join(D, "glucose-strip.py"))
gs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gs)


def test_cottrell_recovers_d():
    slope, d = gs.d_from_cottrell()
    assert abs(d / gs.DTRUE - 1) < 0.02


def test_inverse_prediction():
    c, u, f = gs.inverse()
    assert round(c, 2) == 7.34 and round(u, 2) == 0.09
    assert abs(f["b"] - gs.B1) < 3 * f["sb"]
