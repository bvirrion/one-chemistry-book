import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("kr", os.path.join(D, "kinetic-resolution.py"))
kr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kr)


def test_kagan_recovers_s():
    for s in kr.SS:
        for a in (0.95, 0.8, 0.6):
            c, ee, _ = kr.state(a, s)
            assert abs(kr.kagan_s(c, ee) - s) < 1e-5 * s


def test_substrate_ee_tends_to_one():
    for s in kr.SS:
        c, ee, _ = kr.state(1e-3, s)
        assert ee > 0.99 and c > 0.99 * 0.5


def test_product_ee_at_low_conversion():
    # at c -> 0 the product ee tends to (s - 1)/(s + 1)
    for s in kr.SS:
        _, _, eep = kr.state(1 - 1e-7, s)
        assert abs(eep - (s - 1) / (s + 1)) < 1e-4
