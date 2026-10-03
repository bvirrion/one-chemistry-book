import importlib.util
import os

spec = importlib.util.spec_from_file_location("pib", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3", "particle-in-box.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_energies_and_nodes():
    assert m.energy_ratio(2) / m.energy_ratio(1) == 4
    for n in (1, 2, 3, 4):
        assert m.nodes(n) == n - 1
        assert abs(m.norm(n, n) - 1) < 1e-6
    assert abs(m.norm(1, 2)) < 1e-6


def test_dyes():
    d = m.fitted_delta()
    assert abs(m.wavelength(7, d) * 1e9 - 603) < 1e-6
    assert round(d * 1e12) == 222                # pm, printed
    assert round(m.wavelength(5, d) * 1e9) == 474  # printed predictions
    assert round(m.wavelength(9, d) * 1e9) == 732
    assert round(m.wavelength(5, 0) * 1e9) == 147
