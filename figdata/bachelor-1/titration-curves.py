"""Titration curves of ch. 15, computed exactly (no approximation):
pH-metric curves from the charge balance (solved by bisection), the
potentiometric curve of iron(II) by permanganate in 1 mol/L acid from the
Nernst equation, and the conductimetric curve of hydrochloric acid by
sodium hydroxide from Kohlrausch's law. Constants: pKa from the ledger /
aqueous-constants.py, standard potentials from standard-potentials.py,
limiting conductivities from the ledger (lam:, Lam: rows)."""
import importlib.util
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402


def _load(name):
    spec = importlib.util.spec_from_file_location(
        name.replace("-", "_"), os.path.join(os.path.dirname(__file__), name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


aqc = _load("aqueous-constants")
stp = _load("standard-potentials")
PKE = aqc.pka("water")
SLOPE = value("const:R") * 298.15 * math.log(10) / value("const:F")


def _anion_charge(h, c, pkas):
    """Mean negative charge carried by c mol/L of a polyprotic acid at [H+] = h."""
    ks = [10 ** -p for p in pkas]
    terms, prod = [1.0], 1.0
    for k in ks:
        prod *= k / h
        terms.append(prod)
    s = sum(terms)
    return c * sum(i * t for i, t in enumerate(terms)) / s


def ph_of(na, strong, weak):
    """pH of a solution with [Na+] = na, strong acid conc 'strong', and a list
    of (c, [pKa...]) weak acids, from the charge balance."""
    lo, hi = -2.0, 16.0
    for _ in range(80):
        mid = (lo + hi) / 2
        h = 10 ** -mid
        excess = h + na - 10 ** (mid - PKE) - strong - sum(_anion_charge(h, c, p) for c, p in weak)
        if excess > 0:      # too many positive charges: pH must rise
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def curve(v, v0=10.0, cb=0.100, strong=0.0, weak=()):
    """pH after adding v mL of NaOH at cb to v0 mL of the acid mixture."""
    f = v0 / (v0 + v)
    return ph_of(cb * v / (v0 + v), strong * f, [(c * f, p) for c, p in weak])


ETH = value("pka:ethanoic")
PHOS = [aqc.pka("phosphoric1"), aqc.pka("phosphoric2"), aqc.pka("phosphoric3")]


def potentiometric(v, v0=10.0, cfe=0.100, cmn=0.0200):
    """E (V vs SHE) of a platinum wire while v mL of permanganate at cmn are
    added to v0 mL of iron(II) at cfe, in 1 mol/L acid (pH 0)."""
    e1, e2 = stp.E0("Fe3+/Fe2+"), stp.E0("MnO4-/Mn2+")
    n_fe, n_mn = cfe * v0, cmn * v
    veq = cfe * v0 / (5 * cmn)
    if v < 1e-9:
        return None
    if abs(v - veq) < 1e-9:
        return (e1 + 5 * e2) / 6
    if v < veq:
        return e1 + SLOPE * math.log10(5 * n_mn / (n_fe - 5 * n_mn))
    return e2 + SLOPE / 5 * math.log10((n_mn - n_fe / 5) / (n_fe / 5))


def ionic_conductivities():
    """lambda (S cm2/mol) of H+, OH-, Cl-, Na+; Cl- and Na+ by Kohlrausch's law
    from the limiting conductivities of HCl and NaCl."""
    lh, loh = value("lam:H+"), value("lam:OH-")
    lcl = value("lamsalt:HCl") - lh
    lna = value("lamsalt:NaCl") - lcl
    return {"H+": lh, "OH-": loh, "Cl-": lcl, "Na+": lna}


def conductimetric(v, v0=100.0, ca=0.0100, cb=0.100):
    """Conductivity (mS/cm) while v mL of NaOH at cb are added to v0 mL of HCl
    at ca; strong acid and base, ion concentrations from the reaction table."""
    lam = ionic_conductivities()
    vt = v0 + v
    n_h0, n_oh = ca * v0, cb * v
    h = max(n_h0 - n_oh, 0) / vt
    oh = max(n_oh - n_h0, 0) / vt
    na, cl = n_oh / vt, n_h0 / vt                 # mol/L
    kappa = (lam["H+"] * h + lam["OH-"] * oh + lam["Na+"] * na + lam["Cl-"] * cl)  # S cm2/L
    return kappa          # S cm2 mol-1 * mol L-1 = mS/cm (1 L = 1000 cm3)


if __name__ == "__main__":
    vs = [i / 20 for i in range(0, 401)]
    write_table(__file__, ("V", "pH"), [(v, curve(v, strong=0.100)) for v in vs], part="strong")
    rows = []
    for v in vs:
        p = curve(v, weak=[(0.100, [ETH])])
        d = (curve(v + 0.01, weak=[(0.100, [ETH])]) - curve(max(v - 0.01, 0), weak=[(0.100, [ETH])])) \
            / (0.02 if v > 0 else 0.01)
        rows.append((v, p, d))
    write_table(__file__, ("V", "pH", "dpH"), rows, part="weak")
    vs3 = [i / 20 for i in range(0, 701)]
    write_table(__file__, ("V", "pH"), [(v, curve(v, weak=[(0.100, PHOS)])) for v in vs3],
                part="phosphoric")
    write_table(__file__, ("V", "pH"),
                [(v, curve(v, strong=0.050, weak=[(0.050, [ETH])])) for v in vs], part="mixture")
    rows = [(v, potentiometric(v)) for v in [i / 20 for i in range(1, 401)]]
    write_table(__file__, ("V", "E"), rows, part="potentiometric")
    write_table(__file__, ("V", "kappa"), [(v, conductimetric(v)) for v in [i / 10 for i in range(0, 201)]],
                part="conductimetric")
