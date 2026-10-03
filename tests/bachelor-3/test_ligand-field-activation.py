import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("lf", os.path.join(D, "ligand-field-activation.py"))
lf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lf)


def test_octahedral_splitting():
    assert lf.OH["z2"] == lf.OH["x2y2"] == 3                    # Delta_o = 3 e_sigma
    assert abs(lf.lfse(lf.OH, 3, True) * 10 / 3 + 12) < 1e-9     # d3: -12 Dq
    assert abs(lf.lfse(lf.OH, 6, False) * 10 / 3 + 24) < 1e-9    # low-spin d6: -24 Dq


def test_maxima():
    hs = [lf.lfae_dq(n) for n in range(11)]
    assert abs(hs[3] - 2) < 1e-9 and abs(hs[8] - 2) < 1e-9
    assert abs(lf.lfae_dq(6, False) - 4) < 1e-9
    assert max(hs + [lf.lfae_dq(n, False) for n in range(4, 8)]) == lf.lfae_dq(6, False)
    assert hs[0] == hs[5] == hs[10] == 0 and hs[4] < 0 and hs[9] < 0
