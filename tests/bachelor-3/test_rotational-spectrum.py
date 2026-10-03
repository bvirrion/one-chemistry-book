import importlib.util
import os

spec = importlib.util.spec_from_file_location("rs", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3", "rotational-spectrum.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_spacing_2B_and_first_line():
    assert abs(m.line(5) - m.line(4) - 2 * m.b0("CO")) < 1e-12
    ghz = m.line(0) * 29.9792458
    assert abs(ghz - m.value("rotl:CO.1-0") / 1000) < 0.01


def test_jmax():
    J = max(range(30), key=lambda j: m.population(j, 300))
    assert abs(J - m.jmax(300)) < 0.6


def test_raman():
    assert abs(m.raman_shift(0) - 6 * m.b0("N2")) < 1e-12
    assert abs(m.raman_shift(1) - m.raman_shift(0) - 4 * m.b0("N2")) < 1e-12
    assert m.nuclear_weight(2) / m.nuclear_weight(1) == 2
