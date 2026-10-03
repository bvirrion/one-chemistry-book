import importlib.util
import math
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("sm", os.path.join(D, "_statmech.py"))
sm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sm)
spec = importlib.util.spec_from_file_location("pf", os.path.join(D, "partition-functions.py"))
pf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pf)


def test_rotor_limits():
    th = sm.theta_rot("HCl")
    assert abs(sm.q_rot_exact(th, 1.0) - 1) < 1e-6          # only J = 0 at 1 K
    T = 300 * th
    assert abs(sm.q_rot_exact(th, T) - (T / th + 1 / 3)) < 1e-3
    assert round(sm.q_rot_exact(th, 298.15), 2) == 20.19 and round(T / th / 300) == 1
    assert round(sm.q_rot_high(sm.theta_rot("N2"), 298.15, 2), 1) == 52.1


def test_vibration_limits():
    th = sm.theta_vib("I2")
    assert abs(sm.q_vib(th, 10) - 1) < 1e-12
    assert abs(sm.q_vib(th, 1e5) / (1e5 / th) - 1) < 2e-3
    assert round(sm.q_vib(th, 298.15), 3) == 1.556


def test_tables_shape():
    assert len(pf.rot_rows()) == 121 and len(pf.vib_rows()) == 296
    assert all(r[1] >= r[2] - 1e-9 for r in pf.rot_rows()[1:])   # exact sum above T/theta
