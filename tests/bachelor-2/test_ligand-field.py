import importlib.util
import os

spec = importlib.util.spec_from_file_location("lf", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "ligand-field.py"))
lf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lf)


def test_cfse_values():
    assert abs(lf.cfse(3, False) + 1.2) < 1e-12
    assert abs(lf.cfse(6, True) + 2.4) < 1e-12
    assert abs(lf.cfse(6, False) + 0.4) < 1e-12
    assert abs(lf.cfse(5, False)) < 1e-12 and abs(lf.cfse(10, False)) < 1e-12


def test_unpaired():
    assert lf.configuration(6, False)[2] == 4 and lf.configuration(6, True)[2] == 0
    assert lf.configuration(5, False)[2] == 5 and lf.configuration(5, True)[2] == 1
    assert lf.configuration(3, False)[2] == 3 and lf.configuration(8, False)[2] == 2
