import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("xr", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3", "xrd-powder.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_bragg_positions():
    a = m.value("lat:NaCl")
    tt = m.two_theta("NaCl", 2, 0, 0)
    assert abs(2 * (a / 2) * math.sin(math.radians(tt / 2)) - m.lam()) < 1e-12
    assert round(m.two_theta("KCl", 4, 2, 0), 2) == 66.38


def test_absences():
    for h, k, l in ((1, 0, 0), (1, 1, 0), (2, 1, 0)):
        assert m.structure_factor("NaCl", h, k, l) == 0      # F lattice, mixed parity
        assert m.structure_factor("Cu", h, k, l) == 0
    assert m.structure_factor("W", 1, 0, 0) == 0 and m.structure_factor("W", 1, 1, 0) != 0
    assert m.structure_factor("KCl", 1, 1, 1) == 0           # K+ and Cl- isoelectronic
    assert m.structure_factor("NaCl", 1, 1, 1) != 0 and m.structure_factor("KBr", 1, 1, 1) != 0


def test_scherrer():
    tt = 66.38
    fw = m.scherrer_fwhm(38, tt)
    assert abs(fw - 0.25) < 0.01
