import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("sf", os.path.join(D, "schulz-flory.py"))
sf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sf)


def test_dispersity_tends_to_two():
    n, w, d = sf.moments()
    assert abs(n - 1 / (1 - sf.P)) / n < 1e-3
    assert abs(d - (1 + sf.P)) < 1e-3 and abs(d - 2) < 2e-3


def test_normalised():
    assert abs(sum(sf.xn(k) for k in range(1, 40000)) - 1) < 1e-9
    assert abs(sum(sf.wn(k) for k in range(1, 40000)) - 1) < 1e-9
