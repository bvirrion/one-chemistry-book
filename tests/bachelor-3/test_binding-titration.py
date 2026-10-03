import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("bt", os.path.join(D, "binding-titration.py"))
bt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bt)


def test_isotherm_satisfies_mass_action():
    for k in (1e2, 1e3, 1e4):
        h0, g0 = 1e-3, 1.5e-3
        hg = bt.bound_1to1(h0, g0, k)
        assert abs(hg / ((h0 - hg) * (g0 - hg)) / k - 1) < 1e-9


def test_job_maxima():
    xs = [j / 1000 for j in range(1, 1000)]
    assert abs(max(xs, key=bt.job_1to1) - 0.5) < 2e-3
    assert abs(max(xs, key=bt.job_1to2) - 1 / 3) < 0.02


def test_fit_recovers_the_model_constant():
    k, sk, db, sdb, rms = bt.fit(bt.problem_data())
    assert abs(k - bt.K_TRUE) < 2 * sk
    assert abs(db - bt.D_BOUND) < 3 * sdb + 1e-3
    assert rms < 0.003


def test_problem_table_matches_data():
    import re
    tex = open(os.path.join(os.path.dirname(__file__), "..", "..", "parts", "bachelor-3",
                            "25-supramolecular.tex"), encoding="utf8").read()
    row = re.search(r"\$\\delta\$ & ([0-9. &]+)\\\\", tex).group(1)
    printed = [float(v) for v in row.split("&")]
    assert printed == [d for _, d in bt.problem_data()]
