import importlib.util
import os

spec = importlib.util.spec_from_file_location("rd", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3", "reduction.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_tables_orthogonal():
    for g, (classes, irreps, *_ ) in m.GROUPS.items():
        h = sum(c[0] for c in classes)
        assert sum(r[0] ** 2 for r in irreps.values()) == h, g
        assert len(irreps) == len(classes), g
        rows = list(irreps.values())
        for i, a in enumerate(rows):
            for j, b in enumerate(rows):
                s = sum(c[0] * x * y for c, x, y in zip(classes, a, b))
                assert s == (h if i == j else 0), (g, i, j)


def test_reductions_are_integers():
    for mol, (g, _, _) in m.MOLECULES.items():
        for v in m.reduce(g, m.gamma_3n(mol)).values():
            assert abs(v - round(v)) < 1e-9 and v >= 0, mol


def test_printed_results():
    assert m.label(m.gamma_vib("H2O")) == "2A1 + B1"
    assert m.label(m.gamma_vib("NH3")) == "2A1 + 2E"
    assert m.label(m.gamma_vib("CH4")) == "A1 + E + 2T2"
    assert m.label(m.gamma_vib("CO2")) == "Ag + B1u + B2u + B3u"
    assert m.label(m.gamma_vib("BF3")) == "A1' + 2E' + A2''"
    assert m.label(m.gamma_vib("XeF4")) == "A1g + B1g + B2g + A2u + B2u + 2Eu"
    assert m.label(m.gamma_vib("SF6")) == "A1g + Eg + T2g + 2T1u + T2u"


def test_mode_counts_3n_minus_6():
    for mol, n_atoms, linear in (("H2O", 3, 0), ("NH3", 4, 0), ("CH4", 5, 0), ("CO2", 3, 1),
                                 ("BF3", 4, 0), ("XeF4", 5, 0), ("SF6", 7, 0)):
        assert m.counts(mol)[0] == 3 * n_atoms - 6 + linear
    assert m.counts("SF6")[1:] == (2, 3)
    assert m.counts("CH4")[1:] == (2, 4)
