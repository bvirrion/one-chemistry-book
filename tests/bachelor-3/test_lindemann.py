import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("li", os.path.join(D, "lindemann.py"))
li = importlib.util.module_from_spec(spec)
spec.loader.exec_module(li)


def test_limits():
    assert abs(li.k_uni(1e3) / li.k_inf() - 1) < 1e-5
    assert abs(li.k_uni(1e-12) / (li.K1 * 1e-12) - 1) < 1e-5
    assert abs(li.k_uni(li.m_half()) - li.k_inf() / 2) < 1e-15
