"""Ch. 22, carriers in semiconductors. Part a: intrinsic carrier
concentration n_i = sqrt(Nc Nv) exp(-Eg(T)/2kT) of Si and Ge against
1000/T, with Nc, Nv proportional to T^1.5 and the Varshni gap Eg(T)
(ledger, IOFFE-NSM). Part b: electron concentration of silicon doped with
phosphorus, N_D = 1e15 cm-3 (model doping), donor level 0.045 eV below the
conduction band, from charge neutrality n = p + N_D+ with
N_D+ = N_D/(1 + 2 exp((E_F - E_D)/kT)), solved for E_F by bisection: the
freeze-out, saturation and intrinsic regimes."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

K_EV = value("const:kB") / value("const:e")
ND = 1e15


def eg(mat, T):
    return value(f"eg:{mat}.E0") - value(f"eg:{mat}.a") * T * T / (T + value(f"eg:{mat}.b"))


def nc(mat, T):
    return value(f"dos:{mat}.Nc") * T ** 1.5


def nv(mat, T):
    return value(f"dos:{mat}.Nv") * T ** 1.5


def ni(mat, T):
    return math.sqrt(nc(mat, T) * nv(mat, T)) * math.exp(-eg(mat, T) / (2 * K_EV * T))


def doped_n(T, nd=ND, ed=None):
    """Electron concentration (cm-3) of n-type Si; energies from Ev = 0."""
    ed = value("dop:Si.P") if ed is None else ed
    g = eg("Si", T)
    kT = K_EV * T
    Nc, Nv = nc("Si", T), nv("Si", T)

    def excess(ef):  # positive charge minus negative charge
        n = Nc * math.exp(-(g - ef) / kT)
        p = Nv * math.exp(-ef / kT)
        ndp = nd / (1 + 2 * math.exp((ef - (g - ed)) / kT))
        return p + ndp - n

    lo, hi = -0.5, g + 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if excess(mid) > 0:
            lo = mid
        else:
            hi = mid
    ef = (lo + hi) / 2
    return Nc * math.exp(-(g - ef) / kT)


if __name__ == "__main__":
    rows = []
    for j in range(61):
        inv = 1.2 + 0.05 * j  # 1000/T from 1.2 to 4.2
        T = 1000 / inv
        rows.append((inv, math.log10(ni("Si", T)), math.log10(ni("Ge", T))))
    write_table(__file__, ("invT", "lgSi", "lgGe"), rows)
    rows = []
    for j in range(121):
        inv = 1.0 + 0.2 * j  # 1000/T from 1 to 25 (T 40 K to 1000 K)
        T = 1000 / inv
        rows.append((inv, math.log10(doped_n(T)), math.log10(ni("Si", T))))
    write_table(__file__, ("invT", "lgn", "lgni"), rows, part="b")
    print("ni Si 300", ni("Si", 300), "Ge", ni("Ge", 300), "n(300)", doped_n(300))
