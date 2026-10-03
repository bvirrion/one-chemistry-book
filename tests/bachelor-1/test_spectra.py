import importlib.util
import os

spec = importlib.util.spec_from_file_location("sp", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "spectra.py"))
sp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sp)


def test_n_plus_one_patterns():
    assert sp.binomial(2) == [1, 2, 1]
    assert sp.binomial(3) == [1, 3, 3, 1]
    assert sp.binomial(5) == [1, 5, 10, 10, 5, 1]


def test_areas_are_proton_counts():
    # ethyl ethanoate: 2 : 3 : 3 around 4.12, 2.04, 1.26 ppm
    a = sp.integral("ethylethanoate", 3.8, 4.45)
    b = sp.integral("ethylethanoate", 1.75, 2.35)
    c = sp.integral("ethylethanoate", 0.95, 1.55)
    assert abs(a / c - 2 / 3) < 0.03 and abs(b / c - 1) < 0.03


def test_ir_minimum_at_measured_band():
    t = {nu: sp.transmittance("propanone", nu) for nu in range(1700, 1781)}
    assert min(t, key=t.get) == 1738


def test_unknown_molar_mass():
    # problem data: vapour density 3.74 g/L at 100 degC and 1.000 bar
    m = 3.74 * sp.value("const:R") * 373.15 / 1.000e5 * 1000
    assert round(m) == 116
