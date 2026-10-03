import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("oy", os.path.join(D, "overall-yield.py"))
oy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(oy)


def test_product_law():
    assert abs(oy.linear(0.9, 10) - 0.9 ** 10) < 1e-15
    assert abs(oy.linear(0.9, 3) - oy.linear(0.9, 1) * oy.linear(0.9, 2)) < 1e-15


def test_convergent_beats_linear():
    for y in oy.YS:
        for n in range(3, 31, 2):
            assert oy.convergent(y, n) > oy.linear(y, n)
    assert abs(oy.convergent(0.9, 21) - 0.9 ** 11) < 1e-15
