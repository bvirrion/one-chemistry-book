import importlib.util
import os

spec = importlib.util.spec_from_file_location("dd", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "distribution-diagrams.py"))
dd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dd)


def test_half_at_pka_and_sum_one():
    p = dd.pka_ethanoic()[0]
    f = dd.fractions(p, [p])
    assert abs(f[0] - 0.5) < 1e-12 and abs(sum(f) - 1) < 1e-12
    for ph in (0, 3, 7.2, 12.3, 14):
        assert abs(sum(dd.fractions(ph, dd.pka_phosphoric())) - 1) < 1e-12


def test_polyacid_crossings():
    pk = dd.pka_phosphoric()
    for i, p in enumerate(pk):
        f = dd.fractions(p, pk)
        assert abs(f[i] - f[i + 1]) < 1e-3


def test_ampholyte_maximum():
    pk = dd.pka_phosphoric()
    mid = (pk[0] + pk[1]) / 2
    f = lambda ph: dd.fractions(ph, pk)[1]
    assert f(mid) > f(mid - 0.05) and f(mid) > f(mid + 0.05)
    assert f(mid) > 0.99
