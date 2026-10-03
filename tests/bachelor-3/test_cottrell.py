import importlib.util
import math
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("ct", os.path.join(D, "cottrell.py"))
ct = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ct)


def test_erf_profile_solves_fick():
    x, t, h, k = 2e-3, 1.0, 1e-5, 1e-4
    dcdt = (ct.profile(x, t + k) - ct.profile(x, t - k)) / (2 * k)
    d2 = (ct.profile(x + h, t) - 2 * ct.profile(x, t) + ct.profile(x - h, t)) / h ** 2
    assert abs(dcdt - ct.D * d2) < 1e-3 * abs(dcdt)
    assert ct.profile(0, 1) == 0 and abs(ct.profile(1.0, 1) - 1) < 1e-12


def test_current_is_flux():
    t = 2.0
    h = 1e-6
    grad = (ct.profile(h, t) - ct.profile(0, t)) / h * ct.C
    i = ct.N * ct.value("const:F") * ct.A * ct.D * grad
    assert abs(i / ct.current(t) - 1) < 1e-3
