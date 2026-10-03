import importlib.util
import os

spec = importlib.util.spec_from_file_location("mb", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3", "minimal-basis-hf.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_classic_benchmark():
    e, eps, hist, S = m.h2(1.4, m.scaled(1.24))
    assert abs(e + 1.1167) < 1e-4
    assert abs(S[0, 1] - 0.6593) < 1e-4
    e2 = m.heh(1.4632, m.scaled(2.0925), m.scaled(1.24))[0]
    assert abs(e2 + 2.8607) < 1e-4


def test_bse_hydrogen_is_the_benchmark_basis():
    assert abs(m.h2(1.4)[0] - m.h2(1.4, m.scaled(1.24))[0]) < 1e-6


def test_printed_standard_values():
    e, eps, hist, S = m.heh(1.4632)
    assert round(e, 4) == -2.8418
    assert len(hist) < 30
    R, E = m.h2_minimum()
    assert round(R, 3) == 1.346 and round(E, 4) == -1.1175
    assert round(m.h_atom(), 4) == -0.4666
    assert round(-m.h2(1.4)[1][0] * 27.2114, 2) == 15.73


def test_rhf_dissociates_wrongly_and_sto3g_fits():
    assert m.h2(10.0)[0] > 2 * m.h_atom() + 0.2
    assert m.overlap_sto3g_slater() > 0.999
    e, de, re = m.morse(re_ := 1.4011)
    assert abs(de - 0.1745) < 0.0005
