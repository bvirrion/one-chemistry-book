import importlib.util
import os

spec = importlib.util.spec_from_file_location("pp", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3", "photophysics.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_mirror_image():
    for d in (500, 1400, 3000):
        assert abs(m.band(m.E00 + d, 1) - m.band(m.E00 - d, -1)) < 1e-12


def test_stern_volmer():
    q = 0.02
    assert abs(m.TAU0 / m.tau(q) - m.stern_volmer(q)) < 1e-12
    assert abs((m.stern_volmer(0.04) - 1) / 0.04 - m.KQ * m.TAU0) < 1e-9
