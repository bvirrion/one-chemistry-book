import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("sa", os.path.join(D, "standard-addition.py"))
sa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sa)


def test_x_intercept_is_minus_c0():
    f = sa.fit()
    assert abs(f["c0"] - sa.C0) < 3 * f["s_c0"]
    assert abs(f["a"] + f["b"] * (-f["c0"])) < 1e-12
