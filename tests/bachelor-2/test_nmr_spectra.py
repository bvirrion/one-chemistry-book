import importlib.util
import os

spec = importlib.util.spec_from_file_location("nmr", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "nmr-spectra.py"))
nmr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nmr)


def test_every_line_has_a_kind():
    for key, kinds in nmr.KINDS.items():
        assert sorted(s for s, _ in nmr.lines(key)) == sorted(kinds)
        assert sorted(kinds) == sorted(nmr.CLASS[key])


def test_benzyl_acetate_named_number():
    # seven kinds of carbon (C=O, ipso, ortho, meta, para, CH2, CH3); six resolved lines,
    # one of them a CH2 (down in DEPT-135)
    t = nmr.table("c13:benzylacetate")
    assert len(t) == 6
    assert sum(1 for r in t if r[2] < 0) == 1
    assert sum(1 for r in t if r[2] == 0) == 2   # C=O and ipso vanish


def test_dept_rules():
    assert nmr.dept135(2) < 0 < nmr.dept135(3) and nmr.dept135(0) == 0
    assert nmr.dept90(1) > 0 and nmr.dept90(3) == 0


def test_two_carbon13_neighbours_are_rare():
    a13 = 0.011
    assert abs(a13 ** 2 - 1.2e-4) < 0.05e-4
