"""Tests for figdata/grade-12/catalysis.py."""
import importlib.util, os

spec = importlib.util.spec_from_file_location(
    "cat", os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12", "catalysis.py"))
cat = importlib.util.module_from_spec(spec); spec.loader.exec_module(cat)


def test_same_initial_and_final_levels():
    for f in (cat.uncatalysed, cat.catalysed):
        assert abs(f(0.0)) < 0.5 and abs(f(1.0) - cat.END) < 0.5


def test_catalysed_barrier_lower_and_two_humps():
    rows = cat.profiles()
    assert max(r[2] for r in rows) < max(r[1] for r in rows) - 20
    ec = [r[2] for r in rows]
    peaks = [i for i in range(1, len(ec) - 1) if ec[i] > ec[i - 1] and ec[i] > ec[i + 1]]
    assert len(peaks) == 2


def test_same_plateau_catalysed_faster():
    rows = cat.evolution(tmax=400, step=1)
    assert abs(rows[-1][1] - cat.VMAX) < 0.1 and abs(rows[-1][2] - cat.VMAX) < 0.1
    assert all(r[2] >= r[1] for r in rows)
