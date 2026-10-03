import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("nr", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3", "nmr-relaxation.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_null_and_limits():
    assert abs(m.mz(m.null_time())) < 1e-12
    assert m.mz(0) == -1 and abs(m.mz(50) - 1) < 1e-9
    assert abs(m.mxy(m.T2) - math.exp(-1)) < 1e-12
