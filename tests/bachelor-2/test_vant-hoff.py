import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("vh", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "vant-hoff.py"))
vh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vh)


def test_van_t_hoff_slope_near_298():
    # d lnK / d(1/T) = -DrH/R, with DrH from the formation enthalpy
    d = (vh.lnK_ammonia(400) - vh.lnK_ammonia(298.15)) / (1 / 400 - 1 / 298.15)
    assert abs(-d * vh.R / 1000 - vh.drH_ammonia()) < 3.0


def test_equilibrium_fraction_solves_q_equals_k():
    T, p = 723.15, 200
    x = vh.x_ammonia(T, p)
    q = x * x / (((1 - x) / 4) * (3 * (1 - x) / 4) ** 3) / p ** 2
    assert abs(math.log(q) - vh.lnK_ammonia_interp(T)) < 1e-9
    assert round(x, 2) == 0.25


def test_le_chatelier_monotone():
    assert vh.x_ammonia(723.15, 300) > vh.x_ammonia(723.15, 200) > vh.x_ammonia(723.15, 50)
    assert vh.x_ammonia(673.15, 200) > vh.x_ammonia(723.15, 200) > vh.x_ammonia(773.15, 200)


def test_so2():
    assert round(vh.k_so2(700)) == 286
    assert vh.conversion_so2(700) > vh.conversion_so2(800)
    b = vh.beds()
    assert len(b) == 3 and b[-1][-1][1] > b[0][-1][1]
