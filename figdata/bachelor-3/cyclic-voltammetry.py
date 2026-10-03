"""Ch. 15, cyclic voltammograms simulated by explicit finite differences
(Fick's second law for O and R with equal D, semi-infinite planar
diffusion). Reduction O + e- = R, starting with O only (c* = 1.0 mM,
D = 1.0e-5 cm2/s, A = 0.0707 cm2, n = 1, 298.15 K: model values); the
potential scans from +0.30 V to -0.30 V vs E0' and back. Surface condition:
Nernst (reversible) or Butler-Volmer with k0 (quasi-reversible, alpha =
0.5). Currents are cathodic positive (the plotting convention of the
chapter is applied in the figure)."""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

F, R, T = value("const:F"), value("const:R"), 298.15
FRT = F / (R * T)
D, C, A = 1.0e-5, 1.0e-6, 0.0707
E1, E2 = 0.30, -0.30


def simulate(v, k0=None, alpha=0.5, nx=600, lam=0.45):
    """return arrays E (V vs E0'), i (A, cathodic positive)"""
    ttot = 2 * (E1 - E2) / v
    L = 6 * math.sqrt(D * ttot)
    dx = L / nx
    dt = lam * dx * dx / D
    nt = int(math.ceil(ttot / dt))
    dt = ttot / nt
    lam = D * dt / dx / dx
    co = np.full(nx + 1, 1.0)
    cr = np.zeros(nx + 1)
    Es, Is = [], []
    for k in range(1, nt + 1):
        t = k * dt
        e = E1 - v * t if t <= ttot / 2 else E2 + v * (t - ttot / 2)
        co_new = co.copy()
        cr_new = cr.copy()
        co_new[1:-1] = co[1:-1] + lam * (co[2:] - 2 * co[1:-1] + co[:-2])
        cr_new[1:-1] = cr[1:-1] + lam * (cr[2:] - 2 * cr[1:-1] + cr[:-2])
        if k0 is None:
            th = math.exp(FRT * e)
            co_new[0] = th / (1 + th)            # equal D: c_O + c_R = c* everywhere
            cr_new[0] = 1 - co_new[0]
        else:
            kf = k0 * math.exp(-alpha * FRT * e)
            kb = k0 * math.exp((1 - alpha) * FRT * e)
            # flux J = D (co1 - co0)/dx = kf co0 - kb cr0 and D (cr0 - cr1)/dx = J
            g = D / dx
            a11, a12, b1 = g + kf, -kb, g * co_new[1]
            a21, a22, b2 = -kf, g + kb, g * cr_new[1]
            det = a11 * a22 - a12 * a21
            co_new[0] = (b1 * a22 - a12 * b2) / det
            cr_new[0] = (a11 * b2 - a21 * b1) / det
        co, cr = co_new, cr_new
        flux = D * (-3 * co[0] + 4 * co[1] - co[2]) / (2 * dx)   # second-order gradient at x = 0
        Es.append(e)
        Is.append(F * A * C * flux)
    return np.array(Es), np.array(Is)


def peaks(E, I):
    n = len(E) // 2
    ic = int(np.argmax(I[:n]))
    ia = n + int(np.argmin(I[n:]))
    return E[ic], I[ic], E[ia], I[ia]


def randles_sevcik(v):
    return 0.4463 * F * A * C * math.sqrt(F * v * D / (R * T))


SCANS = (0.025, 0.05, 0.1, 0.2)


if __name__ == "__main__":
    res = {}
    for v in SCANS:
        E, I = simulate(v)
        res[v] = (E, I)
        epc, ipc, epa, ipa = peaks(E, I)
        print("v=%.3f: Epc %.1f mV Epa %.1f mV dEp %.1f mV ip %.3f uA RS %.3f uA E1/2 %.1f mV"
              % (v, 1000 * epc, 1000 * epa, 1000 * (epa - epc), ipc * 1e6, randles_sevcik(v) * 1e6,
                 500 * (epa + epc)))
    step = 8
    n = min(len(res[v][0]) for v in SCANS)
    for v in SCANS:
        E, I = res[v]
        idx = np.linspace(0, len(E) - 1, 600).astype(int)
        write_table(__file__, ("E_mV", "i_uA"), [(1000 * E[j], -1e6 * I[j]) for j in idx], part="v%d" % int(1000 * v))
    Eq, Iq = simulate(0.1, k0=2.0e-3)
    idx = np.linspace(0, len(Eq) - 1, 600).astype(int)
    write_table(__file__, ("E_mV", "i_uA"), [(1000 * Eq[j], -1e6 * Iq[j]) for j in idx], part="quasi")
    epc, ipc, epa, ipa = peaks(Eq, Iq)
    print("quasi k0=2e-3: dEp %.1f mV" % (1000 * (epa - epc)))
    write_table(__file__, ("sqrtv", "ip_uA"), [(math.sqrt(v), 1e6 * peaks(*res[v])[1]) for v in SCANS], part="ip")
