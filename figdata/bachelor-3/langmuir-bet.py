"""Ch. 16, adsorption isotherms. (a) Langmuir isotherms theta = Kp/(1 + Kp) at
two temperatures, K = K0 exp(-dH/RT) with K0 = 1.0e-8 kPa-1 and dH = -40 kJ/mol
(model values).
(b) A BET isotherm (v_m = 45.0 cm3(STP)/g, c = 120: model values of the
weekend problem) and its linear form; the weekend problem's 'measured'
points are the BET values with a fixed scatter of about 1 %.
(c) The problem's catalyst: BET area with the ledger N2 cross-section,
dispersion of Pt from H2 chemisorption and the mean particle size (spheres,
area per surface Pt atom from the mean of the (111), (100), (110) faces)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

VM, CB = 45.0, 120.0
X_DATA = (0.05, 0.10, 0.15, 0.20, 0.25, 0.30)
SCAT = (1.008, 0.992, 1.011, 0.994, 1.006, 0.997)
PT_WT, H2_UPTAKE, RATE = 0.0100, 0.205, 2.0e-5        # g Pt per g, cm3(STP) H2 per g, mol/(g s)


def K_ADS(T):
    """model Langmuir constant, kPa-1"""
    return 1.0e-8 * math.exp(40000 / (value("const:R") * T))


def langmuir(p, K):
    return K * p / (1 + K * p)


def bet(x, vm=VM, c=CB):
    return vm * c * x / ((1 - x) * (1 - x + c * x))


def bet_data():
    return [(x, round(bet(x) * s, 1)) for x, s in zip(X_DATA, SCAT)]


def fit_bet(data=None):
    data = data or bet_data()
    xs = [x for x, _ in data]
    ys = [x / (v * (1 - x)) for x, v in data]
    n = len(xs)
    xm, ym = sum(xs) / n, sum(ys) / n
    sxx = sum((x - xm) ** 2 for x in xs)
    b = sum((x - xm) * (y - ym) for x, y in zip(xs, ys)) / sxx
    a = ym - b * xm
    vm = 1 / (a + b)
    return dict(slope=b, intercept=a, vm=vm, c=1 + b / a)


def area_bet(vm):
    """m2/g from v_m in cm3(STP)/g"""
    n = vm / (1000 * value("const:Vm1"))
    return n * value("const:NA") * value("sa:N2.am") * 1e-18


def pt_geometry():
    a = value("lat:Pt")
    v_atom = a ** 3 / 4                                  # A3 per Pt atom
    areas = (math.sqrt(3) / 4 * a * a, a * a / 2, a * a / math.sqrt(2))
    a_m = 1 / (sum(1 / s for s in areas) / 3)            # A2 per surface atom
    return v_atom, a_m


def dispersion():
    h_mol = 2 * H2_UPTAKE / (1000 * value("const:Vm1"))
    pt_mol = PT_WT / value("aw:Pt")
    return h_mol / pt_mol, h_mol


def diameter_nm():
    v, a_m = pt_geometry()
    D, _ = dispersion()
    return 6 * v / (a_m * D) / 10


def tof():
    return RATE / dispersion()[1]


if __name__ == "__main__":
    R = value("const:R")
    k1 = [(p, langmuir(p, K_ADS(300)), langmuir(p, K_ADS(350)))
          for p in [0.5 * i for i in range(0, 201)]]
    write_table(__file__, ("p_kPa", "T300", "T350"), k1, part="langmuir")
    write_table(__file__, ("x", "v"), [(0.005 * i, bet(0.005 * i)) for i in range(0, 181)], part="bet")
    write_table(__file__, ("x", "v", "y"), [(x, v, x / (v * (1 - x))) for x, v in bet_data()], part="data")
    f = fit_bet()
    write_table(__file__, ("x", "y"), [(x, f["intercept"] + f["slope"] * x) for x in (0.0, 0.35)], part="line")
    print("data", bet_data(), "fit", f, "area %.1f m2/g" % area_bet(f["vm"]))
    print("geometry", pt_geometry(), "D %.3f" % dispersion()[0], "d %.2f nm" % diameter_nm(), "TOF %.2f s-1" % tof())
