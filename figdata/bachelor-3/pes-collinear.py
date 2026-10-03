"""Ch. 12, a LEPS (London-Eyring-Polanyi-Sato) model surface for the collinear
reaction H + H2 -> H2 + H: Morse singlet and anti-Morse triplet pair curves
built from the H2 constants of the ledger (D_e = D_0 + G(0), r_e, omega_e),
with a Sato parameter of 0.17 (a model constant, not a measurement). Writes
contour lines (marching squares, chained into polylines) in the
`contour prepared` format, the minimum energy path, and the saddle point."""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table, out_path  # noqa: E402
from _ledger import value  # noqa: E402

SATO = 0.17
CM_EV = value("const:h") * value("const:c") * 100 / value("const:eV")


def morse_params():
    """D_e (eV), r_e (angstrom), beta (1/angstrom) of H2"""
    we, wexe = value("diat:H2.we"), value("diat:H2.wexe")
    g0 = we / 2 - wexe / 4
    d0_kj = 2 * value("janaf:H.dfH0")          # H2(g) has dfH = 0 at 0 K
    d0_cm = d0_kj * 1000 / (value("const:h") * value("const:c") * 100 * value("const:NA"))
    de = (d0_cm + g0) * CM_EV
    re = value("diat:H2.re")
    mu = value("imass:H1") / 2 * value("const:u")
    k = mu * (2 * math.pi * value("const:c") * 100 * we) ** 2          # force constant, N/m
    beta = math.sqrt(k / (2 * de * value("const:eV"))) * 1e-10         # 1/angstrom
    return de, re, beta


DE, RE, BETA = morse_params()


def singlet(r):
    x = np.exp(-BETA * (r - RE))
    return DE * (x * x - 2 * x)


def triplet(r):
    x = np.exp(-BETA * (r - RE))
    return DE / 2 * (x * x + 2 * x)


def leps(rab, rbc):
    rac = rab + rbc
    q, j = [], []
    for r in (rab, rbc, rac):
        s, t = singlet(r), triplet(r)
        q.append((s * (1 + SATO) + t * (1 - SATO)) / 2)
        j.append((s * (1 + SATO) - t * (1 - SATO)) / 2)
    root = np.sqrt(0.5 * ((j[0] - j[1]) ** 2 + (j[1] - j[2]) ** 2 + (j[2] - j[0]) ** 2))
    return (q[0] + q[1] + q[2] - root) / (1 + SATO)      # eV; zero for H + H + H, -D_e for H2 + H


def saddle():
    """symmetric saddle: minimise along the diagonal r_AB = r_BC"""
    rs = np.linspace(0.6, 1.4, 80001)
    e = leps(rs, rs)
    i = int(np.argmin(e))   # along the symmetric line the saddle is a minimum (a maximum along the path)
    return rs[i], e[i]


def grad(x, y, h=1e-5):
    return ((leps(x + h, y) - leps(x - h, y)) / (2 * h), (leps(x, y + h) - leps(x, y - h)) / (2 * h))


def mep(step=0.002, nmax=4000):
    """steepest descent from the saddle, displaced along r_AB - r_BC"""
    rs, _ = saddle()
    branch = []
    for sgn in (1, -1):
        x, y = rs + sgn * 1e-3, rs - sgn * 1e-3
        pts = [(x, y)]
        for _ in range(nmax):
            gx, gy = grad(x, y)
            n = math.hypot(gx, gy)
            if n < 1e-6 or max(x, y) > 3.0:
                break
            x, y = x - step * gx / n, y - step * gy / n
            pts.append((x, y))
        branch.append(pts)
    return list(reversed(branch[1])) + [(rs, rs)] + branch[0]


def contours(levels, n=241, lo=0.4, hi=3.0):
    xs = np.linspace(lo, hi, n)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    Z = leps(X, Y)
    lines = []
    for lev in levels:
        segs = []
        for i in range(n - 1):
            for j in range(n - 1):
                c = [(xs[i], xs[j], Z[i, j]), (xs[i + 1], xs[j], Z[i + 1, j]),
                     (xs[i + 1], xs[j + 1], Z[i + 1, j + 1]), (xs[i], xs[j + 1], Z[i, j + 1])]
                pts = []
                for k in range(4):
                    (x1, y1, z1), (x2, y2, z2) = c[k], c[(k + 1) % 4]
                    if (z1 - lev) * (z2 - lev) < 0:
                        t = (lev - z1) / (z2 - z1)
                        pts.append((round(x1 + t * (x2 - x1), 6), round(y1 + t * (y2 - y1), 6)))
                if len(pts) == 2:
                    segs.append(tuple(pts))
                elif len(pts) == 4:
                    segs.append((pts[0], pts[1]))
                    segs.append((pts[2], pts[3]))
        lines += [(lev, p) for p in chain(segs)]
    return lines


def chain(segs):
    """join 2-point segments sharing end points into polylines"""
    from collections import defaultdict
    adj = defaultdict(list)
    for a, b in segs:
        adj[a].append(b)
        adj[b].append(a)
    seen = set()
    polys = []
    for a, b in segs:
        if (a, b) in seen or (b, a) in seen:
            continue
        seen.add((a, b))
        line = [a, b]
        for end in (1, 0):
            while True:
                tip = line[-1] if end else line[0]
                nxt = [p for p in adj[tip] if (tip, p) not in seen and (p, tip) not in seen]
                if not nxt:
                    break
                p = nxt[0]
                seen.add((tip, p))
                if end:
                    line.append(p)
                else:
                    line.insert(0, p)
        polys.append(line)
    return polys


LEVELS = [-4.65, -4.55, -4.45, -4.2, -3.8, -3.2, -2.4, -1.6, -0.8]   # eV, H + H + H = 0


if __name__ == "__main__":
    rows = []
    with open(out_path(__file__, "contours"), "w", encoding="utf8") as f:
        f.write("x y z\n")
        for lev, line in contours([lv for lv in LEVELS]):
            for x, y in line:
                f.write("%.5f %.5f %.2f\n" % (x, y, lev))
            f.write("\n")
    write_table(__file__, ("x", "y"), mep()[::5], part="mep")
    rs, es = saddle()
    print("De %.4f eV re %.5f beta %.4f /A; saddle r = %.4f A, E = %.4f eV, barrier %.4f eV = %.1f kJ/mol"
          % (DE, RE, BETA, rs, es, es + DE, (es + DE) * 96.485))
