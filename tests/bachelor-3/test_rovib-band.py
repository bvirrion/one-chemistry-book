import importlib.util
import os

spec = importlib.util.spec_from_file_location("rv", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3", "rovib-band.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_gap_at_origin():
    nu0 = m.constants(35)[0]
    assert m.R(0) > nu0 > m.P(1)
    assert abs((m.R(0) - m.P(1)) - 2 * (m.constants(35)[1] + m.constants(35)[2])) < 1e-9


def test_combination_differences():
    nu0, B0, B1 = m.constants(35)
    for J in range(1, 8):
        assert abs(m.R(J - 1) - m.P(J + 1) - 4 * B0 * (J + 0.5)) < 1e-9
        assert abs(m.R(J) - m.P(J) - 4 * B1 * (J + 0.5)) < 1e-9


def test_isotope_lower():
    assert m.R(3, 37) < m.R(3, 35)
    assert round(m.R(0) - m.R(0, 37), 1) == 2.1
