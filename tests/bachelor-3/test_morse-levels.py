import importlib.util
import os

spec = importlib.util.spec_from_file_location("ml", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3", "morse-levels.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_levels_and_de():
    assert abs(m.G(1) - m.G(0) - (m.we() - 2 * m.wexe())) < 1e-9
    assert round(m.de_morse()) == 42342 and m.vmax() == 27
    assert round(m.de_morse() - m.G(0)) == 40860
    assert round(m.d0_true()) == 35760


def test_turning_points_on_curve():
    a, b = m.turning(5)
    assert abs(m.morse(a) - m.G(5)) < 1e-6 and abs(m.morse(b) - m.G(5)) < 1e-6


def test_birge_sponer_linear():
    d = [m.G(v + 1) - m.G(v) for v in range(5)]
    assert all(abs((d[i] - d[i + 1]) - 2 * m.wexe()) < 1e-9 for i in range(4))
