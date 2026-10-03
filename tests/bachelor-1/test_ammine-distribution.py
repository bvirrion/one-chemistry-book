import importlib.util
import os

spec = importlib.util.spec_from_file_location("am", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "ammine-distribution.py"))
am = importlib.util.module_from_spec(spec)
spec.loader.exec_module(am)


def test_fractions_sum_to_one():
    for m in ("Cu", "Ag"):
        for pl in (0, 2.5, 6):
            assert abs(sum(am.fractions(m, pl)) - 1) < 1e-12


def test_printed_constants():
    assert [round(x, 2) for x in am.log_betas("Cu")[1:]] == [4.10, 7.51, 10.33, 12.36]
    assert [round(x, 2) for x in am.successive("Cu")] == [4.10, 3.41, 2.82, 2.03]
    assert [round(x, 2) for x in am.log_betas("Ag")[1:]] == [3.32, 7.22]


def test_copper_constants_decrease_silver_inverted():
    k = am.successive("Cu")
    assert all(k[i] > k[i + 1] for i in range(3))
    a = am.successive("Ag")
    assert a[1] > a[0]          # AgNH3+ never predominates


def test_silver_monoammine_stays_minor():
    assert max(am.fractions("Ag", x / 100)[1] for x in range(0, 701)) < 0.5


def test_exercise_distribution_at_0_010():
    f = am.fractions("Cu", 2.0)
    assert [round(100 * x) for x in f] == [0, 0, 7, 45, 48]
