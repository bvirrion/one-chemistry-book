import importlib.util
import os

spec = importlib.util.spec_from_file_location("ms", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "mass-spectra.py"))
ms = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ms)


def test_clusters_sum_to_one():
    for _, atoms in ms.PATTERNS:
        assert abs(sum(ms.cluster(atoms).values()) - 1) < 1e-12


def test_cl_br_named_number():
    c = ms.cluster(["Cl", "Br"])
    r = [c[0] / c[4], c[2] / c[4]]
    # about 3 : 4 : 1
    assert abs(r[0] - 3.22) < 0.02 and abs(r[1] - 4.16) < 0.02


def test_cl2_br2():
    c = ms.normalised(ms.cluster(["Cl", "Cl"]))
    assert abs(c[2] - 100 * 2 * 0.242 / 0.758) < 1e-6
    b = ms.normalised(ms.cluster(["Br", "Br"]), ref=0)
    assert 190 < b[2] < 200


def test_measured_cluster_agrees():
    # 1-bromo-3-chloropropane, WebBook: 156, 158, 160
    s = dict(ms.sticks("ms:bromochloropropane"))
    c = ms.cluster(["Cl", "Br"])
    assert abs(s[158] / s[156] - c[2] / c[0]) < 0.05
    assert abs(s[160] / s[156] - c[4] / c[0]) < 0.03
    # M+1 / M for three carbons
    assert abs(s[157] / s[156] - ms.m_plus_one(3)) < 0.005
