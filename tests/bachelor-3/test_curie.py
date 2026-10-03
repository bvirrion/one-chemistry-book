import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("cu", os.path.join(D, "curie.py"))
cu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cu)


def test_curie_constants():
    assert abs(cu.curie_C(0.5) - 0.3752) < 0.0005            # 0.12505 g^2 S(S+1) with g = 2
    assert abs(cu.curie_C(2) / cu.curie_C(0.5) - 8) < 1e-12


def test_crossover_midpoint():
    T = cu.DH / cu.DS
    assert abs(cu.x_hs(T) - 0.5) < 1e-12
    assert cu.x_hs(50) < 1e-3 and cu.x_hs(400) > 0.95
