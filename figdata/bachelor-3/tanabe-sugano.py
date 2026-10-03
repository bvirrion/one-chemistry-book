"""Ch. 18, Tanabe-Sugano diagrams of d3 (C/B = 4.5) and d8 (C/B = 4.71) ions in
an octahedral field, by full diagonalisation (_ligandfield.py): energies of
all states above the ground state, E/B against Delta/B, separated by spin
(spin-allowed: S of the ground state). Also the free-ion Racah B of Cr3+,
V2+ and Ni2+ from the NIST level barycentres (E(P) - E(F) = 15 B for d2,
d3, d7, d8), and the fit of Delta and B of ruby and emerald from their two
spin-allowed bands (closed d3 formula, checked against the diagonalisation)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402
from _ligandfield import spectrum_with_spin  # noqa: E402

def barycentre(ion, term):
    """weighted mean of the J levels of a term, from the lev: rows"""
    spec = {
        "Cr3": {"4F": ["4F3_2", "4F5_2", "4F7_2", "4F9_2"], "4P": ["4P1_2", "4P3_2", "4P5_2"]},
        "V2": {"4F": ["4F3_2", "4F5_2", "4F7_2", "4F9_2"], "4P": ["4P1_2", "4P3_2", "4P5_2"]},
        "Ni2": {"3F": ["3F4", "3F3", "3F2"], "3P": ["3P2", "3P1", "3P0"]},
    }[ion][term]
    num = den = 0.0
    for lv in spec:
        jtxt = lv[2:]
        J = float(jtxt.replace("_", "/").split("/")[0]) / (2 if "_" in jtxt else 1)
        g = 2 * J + 1
        ground = lv in ("4F3_2", "3F4")
        e = 0.0 if ground else value(f"lev:{ion}.{lv}")
        num += g * e
        den += g
    return num / den


def free_ion_B(ion):
    if ion == "Ni2":
        return (barycentre(ion, "3P") - barycentre(ion, "3F")) / 15
    return (barycentre(ion, "4P") - barycentre(ion, "4F")) / 15


def d3_nu2(delta, B):
    return 7.5 * B + 1.5 * delta - 0.5 * math.sqrt(225 * B * B - 18 * B * delta + delta * delta)


def fit_d3(nu1, nu2):
    """Delta = nu1; B from nu2 by bisection"""
    lo, hi = 1.0, 2000.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if d3_nu2(nu1, mid) < nu2:
            lo = mid
        else:
            hi = mid
    return nu1, mid


def _cluster(values, tol=0.01):
    """distinct levels: energies closer than tol (in units of B) are one level"""
    out = []
    for v in sorted(values):
        if not out or v - out[-1] > tol:
            out.append(round(v, 4))
    return out


def ts_rows(n, cb, dmax=40.0, steps=161):
    B = 1000.0
    s_ground = {3: 1.5, 8: 1.0}[n]
    rows = []
    for i in range(steps):
        x = 0.05 + dmax * i / (steps - 1)
        sp = spectrum_with_spin(n, x * B, B, cb * B)
        e0 = min(e for e, _ in sp)
        hi = _cluster((e - e0) / B for e, s in sp if abs(s - s_ground) < 0.1)
        lo = _cluster((e - e0) / B for e, s in sp if abs(s - s_ground) > 0.1)
        rows.append((x, hi, lo))
    return rows


def _fill(cur, prev, n):
    """where two levels touch (an accidental crossing) the cluster count drops by
    one: duplicate the level where the previous row had its closest pair, so
    that each column keeps following one curve"""
    cur = list(cur)
    while prev is not None and len(cur) < n and len(prev) == n:
        gaps = [prev[i + 1] - prev[i] for i in range(n - 1)]
        i = gaps.index(min(gaps))
        cur.insert(i, cur[min(i, len(cur) - 1)])
    return cur + [float("nan")] * (n - len(cur))


def write_ts(n, cb, name):
    rows = ts_rows(n, cb)
    nh = max(len(r[1]) for r in rows)
    nl = max(len(r[2]) for r in rows)
    out = []
    ph = pl = None
    for x, hi, lo in rows:
        hi = _fill(hi, ph, nh)
        lo = _fill(lo, pl, nl)
        ph, pl = hi, lo
        out.append(tuple([x] + hi + lo))
    header = tuple(["x"] + ["a%d" % i for i in range(nh)] + ["f%d" % i for i in range(nl)])
    write_table(__file__, header, out, part=name)
    return nh, nl


if __name__ == "__main__":
    print("d3:", write_ts(3, 4.5, "d3"), "d8:", write_ts(8, 4.71, "d8"))
    for ion in ("Cr3", "V2", "Ni2"):
        print(ion, "free-ion B = %.0f cm-1" % free_ion_B(ion))
    for gem in ("ruby", "emerald"):
        d, b = fit_d3(value(f"lf:{gem}.nu1"), value(f"lf:{gem}.nu2"))
        print(gem, "Delta %.0f B %.0f Delta/B %.2f beta %.3f" % (d, b, d / b, b / free_ion_B("Cr3")))
