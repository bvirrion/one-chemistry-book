import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("op", os.path.join(D, "ortho-para.py"))
op = importlib.util.module_from_spec(spec)
spec.loader.exec_module(op)


def test_limits():
    assert abs(op.para_fraction_h2(1000) - 0.25) < 1e-6
    assert op.para_fraction_h2(5) > 0.99999
    assert abs(op.ortho_fraction_d2(1000) - 2 / 3) < 1e-6
    assert op.ortho_fraction_d2(5) > 0.9999


def test_named_values():
    assert round(op.para_fraction_h2(20.37), 3) == 0.998
    assert round(op.para_fraction_h2(77), 2) == 0.51
