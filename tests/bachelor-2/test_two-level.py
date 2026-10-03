import importlib.util
import os

spec = importlib.util.spec_from_file_location("tl", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "two-level.py"))
tl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tl)


def test_degenerate_and_far_limits():
    lo, hi = tl.levels(0.0)
    assert (lo, hi) == (-1.0, 1.0)
    assert abs(tl.weight_lower(0.0) - 0.5) < 1e-12
    # far apart: the perturbative shift beta^2/Delta
    lo, hi = tl.levels(8.0)
    plo, phi = tl.perturbative(8.0)
    assert abs(lo - plo) < 0.01 and abs(hi - phi) < 0.01
    assert tl.weight_lower(8.0) > 0.98
