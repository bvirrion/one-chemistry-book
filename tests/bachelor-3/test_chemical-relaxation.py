import importlib.util
import math
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("cr", os.path.join(D, "chemical-relaxation.py"))
cr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cr)


def test_tau_formula():
    sol = cr.run()
    ce = cr.eq_c(cr.K1 / cr.KM1)
    c0 = sol[0][1][0]
    t, y = [(t, y) for t, y in sol if t >= cr.tau()][0]
    assert abs((y[0] - ce) / (c0 - ce) - math.exp(-t / cr.tau())) < 0.01
    assert abs(cr.tau() - 1.56e-4) < 0.01e-4
