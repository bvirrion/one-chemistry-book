import importlib.util
import os

spec = importlib.util.spec_from_file_location("eph", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "eph-diagrams.py"))
eph = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eph)


def segment(system, a, b):
    for s in eph.boundaries(system):
        if {s[0], s[1]} == {a, b}:
            return s
    raise KeyError((a, b))


def test_iron_printed_boundaries():
    s = segment("iron", "Fe3+(ao)", "Fe(OH)3(cr)")
    assert round(s[2][0], 2) == 1.81
    s = segment("iron", "Fe2+(ao)", "Fe(OH)2(cr)")
    assert round(s[2][0], 2) == 6.84
    s = segment("iron", "Fe(cr)", "Fe2+(ao)")
    assert round(s[2][1], 2) == -0.47
    s = segment("iron", "Fe2+(ao)", "Fe3+(ao)")
    assert round(s[2][1], 2) == 0.77


def test_copper_and_zinc():
    s = segment("copper", "CuO(cr)", "Cu2+(ao)")
    assert round(s[2][0], 2) == 4.67
    s = segment("copper", "Cu(cr)", "Cu2+(ao)")
    assert round(s[2][1], 2) == 0.28
    s = segment("zinc", "Zn2+(ao)", "Zn(OH)2(cr)")
    assert round(s[2][0], 2) == 6.80
    s = segment("zinc", "Zn(OH)2(cr)", "Zn(OH)4^2-(ao)")
    assert round(s[2][0], 2) == 13.96
    # Cu+ has no domain: it disproportionates
    assert not any("Cu+(ao)" in (s[0], s[1]) for s in eph.boundaries("copper"))


def test_water():
    h2, o2 = eph.water_lines(0)
    assert round(o2, 2) == 1.23 and h2 == 0
    h2, o2 = eph.water_lines(14)
    assert round(h2, 2) == -0.83


def test_chlorine_named_number():
    s = segment("chlorine", "Cl-(ao)", "Cl2(ao)")
    assert round(s[2][1], 2) == 1.45 and round(s[3][0], 1) == 1.6
    assert round(eph.triple_point_cl2(), 2) == 1.64
    s = segment("chlorine", "HClO(ao)", "ClO-(ao)")
    assert round(s[2][0], 2) == 7.55


def test_printed_arithmetic_with_rounded_data():
    # the chapter prints boundaries computed from pKe = 14.00 and 2-decimal pKs
    assert round(14 - (38.55 - 2) / 3, 2) == 1.82
    assert round(14 - (16.31 - 2) / 2 + 1e-9, 2) == 6.85
    assert round(14 - (20.64 - 2) / 2, 2) == 4.68
    assert round(14 - (16.38 - 2) / 2, 2) == 6.81
    s = segment("iron", "Fe3+(ao)", "Fe(OH)3(cr)")
    assert abs(s[2][0] - 1.82) < 0.015          # figure vs printed value
