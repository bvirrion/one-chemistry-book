import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("bc", os.path.join(D, "band-chain.py"))
bc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bc)


def test_closed_form_matches_matrix():
    for n in (2, 3, 6, 16):
        a = bc.levels(n)
        b = bc.huckel_matrix_levels(n)
        assert max(abs(x - y) for x, y in zip(a, b)) < 1e-9


def test_ethene_and_band_width():
    assert [round(x, 9) for x in bc.levels(2)] == [-1.0, 1.0]
    w = bc.levels(64)[-1] - bc.levels(64)[0]
    assert 3.99 < w < 4.0


def test_dos_normalised():
    n = 200000
    s = sum(bc.dos(-2 + 4 * (j + 0.5) / n) for j in range(n)) * 4 / n
    assert abs(s - 1) < 0.01
