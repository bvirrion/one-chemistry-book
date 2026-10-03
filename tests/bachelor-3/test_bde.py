import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("bde", os.path.join(D, "bde.py"))
bde = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bde)


def test_formula_and_order():
    v = [bde.bde(r, p) for _, r, p in bde.BONDS]
    assert abs(v[0] - (bde.value("dfh4:CH3r") + bde.value("dfh4:H") - bde.value("dfh:CH4_g"))) < 1e-9
    # methyl > primary > secondary > tertiary > benzylic
    assert all(a > b for a, b in zip(v, v[1:]))
    assert 430 < v[0] < 445 and 365 < v[-1] < 385
