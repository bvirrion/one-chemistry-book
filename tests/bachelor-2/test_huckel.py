import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("hk", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "huckel.py"))
hk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hk)


def test_closed_forms():
    for n in (2, 3, 4, 6, 8):
        m, _ = hk.huckel(n)
        assert all(abs(a - b) < 1e-9 for a, b in zip(m, hk.chain_closed_form(n)))
    for n in (4, 5, 6, 7, 8):
        m, _ = hk.huckel(n, ring=True)
        assert all(abs(a - b) < 1e-9 for a, b in zip(m, hk.ring_closed_form(n)))


def test_energies_and_delocalisation():
    assert abs(hk.pi_energy(4, 4) - (2 * 1.618034 + 2 * 0.618034)) < 1e-5
    # benzene: 8 beta, three ethenes 6 beta -> delocalisation 2 |beta|
    assert abs(hk.pi_energy(6, 6, ring=True) - 8) < 1e-9
    # trace: the m values sum to zero
    for n in (4, 6):
        m, _ = hk.huckel(n, ring=True)
        assert abs(sum(m)) < 1e-9


def test_gap_falls():
    gaps = [hk.gap(n) for n in range(2, 22, 2)]
    assert all(b < a for a, b in zip(gaps, gaps[1:]))
    assert abs(hk.gap(2) - 2) < 1e-12


def test_propenal_charges():
    q = hk.propenal_charges()
    assert abs(q.sum()) < 1e-9          # 4 pi electrons over 4 centres
    assert q[3] < 0 < q[2]              # O negative, carbonyl carbon positive
    assert q[0] > 0                     # beta carbon positive
    assert q[1] < q[0]                  # alpha carbon less positive than beta
    _, c = hk.propenal_lumo()
    assert abs(c[0]) > max(abs(c[1]), abs(c[2]))   # beta carbon: largest LUMO coefficient
