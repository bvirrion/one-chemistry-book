import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("ns", os.path.join(D, "nanoparticle-size.py"))
ns = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ns)


def test_magic_numbers_and_shell_sum():
    assert [ns.n_atoms(n) for n in range(1, 6)] == [13, 55, 147, 309, 561]
    assert all(ns.n_atoms(n) == ns.n_atoms_by_shells(n) for n in range(0, 40))


def test_surface_fraction_falls():
    f = [ns.n_surface(n) / ns.n_atoms(n) for n in range(1, 30)]
    assert all(a > b for a, b in zip(f, f[1:]))
    assert abs(f[0] - 12 / 13) < 1e-12


def test_inverse_square_law():
    assert abs(ns.confinement_eV(1.0) / ns.confinement_eV(2.0) - 4) < 1e-9
    assert 0.9 < ns.confinement_eV(2.0) < 1.0
