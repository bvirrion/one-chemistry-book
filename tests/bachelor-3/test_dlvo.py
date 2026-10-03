import importlib.util
import math
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("dl", os.path.join(D, "dlvo.py"))
dl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dl)


def test_debye_length():
    assert abs(dl.debye_length(100) * 1e9 - 0.961) < 0.005
    assert abs(dl.debye_length(1) / dl.debye_length(100) - 10) < 1e-9


def test_barrier_disappears():
    assert dl.barrier(1.0) > 30 and dl.barrier(10.0) > 10
    ci = dl.critical_I()
    assert 40 < ci < 60 and dl.barrier(1.5 * ci) <= 0 < dl.barrier(0.7 * ci)
