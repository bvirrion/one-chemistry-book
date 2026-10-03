"""Ch. 14, stratospheric and tropospheric ozone with the IUPAC rate constants.
(a) The Chapman mechanism at a model altitude (T = 230 K, [M] = 4.0e17 cm-3,
[O2] = 0.21 [M], j(O2) = 1.0e-11 s-1, j(O3) = 1.0e-3 s-1: data of the
weekend problem), with O in steady state and O3 integrated over days, alone
and with a ClOx catalytic cycle ([ClOx] = 1e7 and 3e7 cm-3).
(b) The chain length of the ClOx cycle before capture by CH4 (as HCl) and by
NO2 (as ClONO2; Troe fall-off with the IUPAC Fc).
(c) The Leighton photostationary state of the polluted troposphere,
[O3] = j(NO2)[NO2]/(k[NO]), against the NO2/NO ratio at 298 K (j(NO2) =
8.0e-3 s-1, model value at noon)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402
from _ode import rk4  # noqa: E402

T, M = 230.0, 4.0e17
O2 = 0.21 * M
J1, J3 = 1.0e-11, 1.0e-3
CH4, NO2 = 4.0e11, 1.0e9
CLOX = 1.0e7
J_NO2 = 8.0e-3


def arr(key, temp=T):
    return value(f"kin:{key}.A") * math.exp(-value(f"kin:{key}.EaR") / temp)


def k2(temp=T):
    return value("kin:O+O2+M.k0") * (temp / 300) ** (-value("kin:O+O2+M.n"))


def k_clono2(temp=T, m=M):
    k0 = value("kin:ClO+NO2+M.k0") * (temp / 300) ** (-value("kin:ClO+NO2+M.n")) * m
    kinf = value("kin:ClO+NO2+M.kinf")
    fc = value("kin:ClO+NO2+M.Fc")
    x = k0 / kinf
    return k0 / (1 + x) * fc ** (1 / (1 + math.log10(x) ** 2))


def o_over_o3():
    return J3 / (k2() * M * O2)


def o3_chapman():
    return O2 * math.sqrt(J1 * k2() * M / (J3 * arr("O+O3")))


def clo_over_cl(o3=None):
    o3 = o3 or o3_chapman()
    return arr("Cl+O3") * o3 / (arr("O+ClO") * o_over_o3() * o3)


def chain():
    o3 = o3_chapman()
    o = o_over_o3() * o3
    a = arr("Cl+O3") * o3
    p1 = a / (a + arr("Cl+CH4") * CH4)
    b = arr("O+ClO") * o
    p2 = b / (b + k_clono2() * NO2)
    p = p1 * p2
    return dict(p1=p1, p2=p2, p=p, cycles=p / (1 - p))


def o3_rate(t, y, clox=0.0):
    o3 = y[0]
    o = o_over_o3() * o3
    r = clo_over_cl(o3)
    clo = clox * r / (1 + r)
    return [2 * J1 * O2 - 2 * arr("O+O3") * o * o3 - 2 * arr("O+ClO") * clo * o]


def runs(days=120):
    out = {}
    for clox in (0.0, 1.0e7, 3.0e7):
        sol = rk4(lambda t, y: o3_rate(t, y, clox), [0.0], 0.0, days * 86400.0, 3600.0, every=12)
        out[clox] = sol
    return out


def o3_steady_with_cl(clox):
    """root of the odd-oxygen balance with the Cl cycle (bisection)"""
    lo, hi = 1.0, 2 * o3_chapman()
    for _ in range(200):
        mid = (lo + hi) / 2
        if o3_rate(0, [mid], clox)[0] > 0:
            lo = mid
        else:
            hi = mid
    return mid


def leighton_ppb(ratio, temp=298.15):
    n_air = 1e5 / (value("const:kB") * temp) * 1e-6        # molecules per cm3 at 1 bar
    k = value("kin:NO+O3.A") * math.exp(-value("kin:NO+O3.EaR") / temp)
    return J_NO2 * ratio / k / n_air * 1e9


if __name__ == "__main__":
    r = runs()
    write_table(__file__, ("day", "noCl", "Cl1", "Cl3"),
                [(t / 86400, y[0] / 1e12, r[1.0e7][i][1][0] / 1e12, r[3.0e7][i][1][0] / 1e12)
                 for i, (t, y) in enumerate(r[0.0])], part="chapman")
    write_table(__file__, ("ratio", "O3ppb"), [(0.05 * i, leighton_ppb(0.05 * i)) for i in range(0, 81)],
                part="leighton")
    print("k2 %.3g k4 %.3g kClO3 %.3g kOClO %.3g kClCH4 %.3g kClONO2 %.3g" %
          (k2(), arr("O+O3"), arr("Cl+O3"), arr("O+ClO"), arr("Cl+CH4"), k_clono2()))
    print("O/O3 %.3g O3 %.3g O %.3g ClO/Cl %.3g" % (o_over_o3(), o3_chapman(), o_over_o3() * o3_chapman(), clo_over_cl()))
    print("chain", chain())
    print("O3 with Cl 1e7: %.3g, 3e7: %.3g" % (o3_steady_with_cl(1e7), o3_steady_with_cl(3e7)))
    print("Leighton ratio 1.5: %.1f ppb" % leighton_ppb(1.5))
