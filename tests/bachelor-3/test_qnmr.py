import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("qn", os.path.join(D, "qnmr.py"))
qn = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qn)


def test_integrals_proportional_to_protons():
    nx, ns = qn.amounts()
    a, b, c = (qn.integral(d) for d in (4.16, 6.09, 3.77))
    assert abs((c / b) - 3.0) < 0.01          # 9 H : 3 H of the standard
    assert abs((a / b) - 10 * nx / (3 * ns)) / (a / b) < 0.01


def test_purity_formula_recovers_input():
    nx, ns = qn.amounts()
    exact = qn.purity(10 * nx, 3 * ns)
    assert abs(exact - qn.P_TRUE) < 1e-12
    measured = qn.purity(qn.integral(4.16), qn.integral(6.09))
    assert abs(measured - qn.P_TRUE) < 0.005
