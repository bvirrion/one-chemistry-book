import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("pm", os.path.join(D, "polyene-mo.py"))
pm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pm)


def test_normalised_and_nodes():
    for n in pm.NS:
        for k in range(1, n + 1):
            c = pm.coeffs(n, k)
            assert abs(sum(x * x for x in c) - 1) < 1e-12
            assert pm.nodes(c) == k - 1


def test_terminal_signs_give_the_rules():
    # thermal: HOMO of 4n electrons has opposite terminal signs (conrotatory),
    # of 4n+2 the same (disrotatory)
    homo4 = pm.coeffs(4, 2)
    homo6 = pm.coeffs(6, 3)
    assert homo4[0] * homo4[-1] < 0
    assert homo6[0] * homo6[-1] > 0


def test_symmetry_labels():
    assert [pm.mirror_parity(pm.coeffs(4, k)) for k in range(1, 5)] == [1, -1, 1, -1]
    assert [pm.c2_parity(pm.coeffs(4, k)) for k in range(1, 5)] == [-1, 1, -1, 1]
