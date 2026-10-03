"""Ch. 23, Zachariasen's picture of a crystal and a glass in two dimensions:
network formers (three-coordinate, like B in B2O3 drawn flat) joined by
bridging oxygens. Crystal: a honeycomb patch, an oxygen at the middle of each
bond. Glass: the same patch with Stone-Wales rotations (four hexagons become
two five- and two seven-membered rings), relaxed with bond and second-
neighbour springs so that every former keeps its three bonds and nearly its
bond length and angles, then two bonds broken: each break leaves two
non-bridging oxygens, with a modifier cation (Na+) between them.
Outputs (in units of the former-former distance d = 1):
  part crystal-bonds, crystal-T, crystal-O; part glass-bonds, glass-T,
  glass-O (bridging), glass-NBO, glass-Na. Bond tables: x y u v (segment
  from (x, y) to (x + u, y + v), drawn with pgfplots quiver)."""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

D = 1.0
NX, NY = 7, 6          # hexagon columns and rows
SW_BONDS = ((3, 1), (1, 4), (5, 4))   # (column, row) of hexagons whose upper-right bond rotates
BREAKS = ((2, 3), (5, 2))             # hexagons whose right-hand vertical bond is broken


def honeycomb():
    """Pointy-top hexagons; returns vertex array, bond set and hexagon centres."""
    a = math.sqrt(3) * D
    centres = []
    for j in range(NY):
        for i in range(NX):
            centres.append(((i + 0.5 * (j % 2)) * a, j * 1.5 * D))
    verts, index = [], {}

    def vid(p):
        key = (round(p[0], 4), round(p[1], 4))
        if key not in index:
            index[key] = len(verts)
            verts.append(p)
        return index[key]
    bonds = set()
    hexes = []
    for (cx, cy) in centres:
        ring = [vid((cx + D * math.cos(math.radians(30 + 60 * k)), cy + D * math.sin(math.radians(30 + 60 * k))))
                for k in range(6)]
        hexes.append(ring)
        for k in range(6):
            b = tuple(sorted((ring[k], ring[(k + 1) % 6])))
            bonds.add(b)
    return np.array(verts, float), bonds, centres, hexes


def neighbours(bonds, n):
    nb = [set() for _ in range(n)]
    for i, j in bonds:
        nb[i].add(j)
        nb[j].add(i)
    return nb


def stone_wales(pos, bonds, i, j):
    nb = neighbours(bonds, len(pos))
    outer_i = list(nb[i] - {j})
    outer_j = list(nb[j] - {i})
    m = (pos[i] + pos[j]) / 2
    rot = np.array([[0, -1], [1, 0]])
    pos[i] = m + rot @ (pos[i] - m)
    pos[j] = m + rot @ (pos[j] - m)
    for k in outer_i:
        bonds.discard(tuple(sorted((i, k))))
    for k in outer_j:
        bonds.discard(tuple(sorted((j, k))))
    outer = outer_i + outer_j
    # each new end takes the two outer atoms nearest to it
    best = None
    from itertools import combinations
    for pair in combinations(range(4), 2):
        rest = [q for q in range(4) if q not in pair]
        cost = sum(np.linalg.norm(pos[i] - pos[outer[q]]) for q in pair) + \
            sum(np.linalg.norm(pos[j] - pos[outer[q]]) for q in rest)
        if best is None or cost < best[0]:
            best = (cost, pair, rest)
    for q in best[1]:
        bonds.add(tuple(sorted((i, outer[q]))))
    for q in best[2]:
        bonds.add(tuple(sorted((j, outer[q]))))


def relax(pos, bonds, fixed, apart=(), steps=4000, lr=0.05):
    nb = neighbours(bonds, len(pos))
    second = set()
    for c in range(len(pos)):
        for a in nb[c]:
            for b in nb[c]:
                if a < b:
                    second.add((a, b))
    second -= set(bonds)
    pairs = [(i, j, D, 1.0) for i, j in bonds] + [(i, j, math.sqrt(3) * D, 0.3) for i, j in second] + \
        [(i, j, 1.7 * D, 1.0) for i, j in apart]
    P = np.array([(p[0], p[1]) for p in pairs], int)
    L = np.array([p[2] for p in pairs])
    W = np.array([p[3] for p in pairs])
    free = np.ones(len(pos), bool)
    free[list(fixed)] = False
    for _ in range(steps):
        dvec = pos[P[:, 1]] - pos[P[:, 0]]
        dist = np.linalg.norm(dvec, axis=1)
        f = (W * (dist - L) / dist)[:, None] * dvec
        g = np.zeros_like(pos)
        np.add.at(g, P[:, 0], f)
        np.add.at(g, P[:, 1], -f)
        pos[free] += lr * g[free]
    return pos


def rings(pos, bonds):
    """Sizes of the faces of the planar network, the outer face excluded."""
    nb = neighbours(bonds, len(pos))
    order = {}
    for v in range(len(pos)):
        order[v] = sorted(nb[v], key=lambda c: math.atan2(pos[c][1] - pos[v][1], pos[c][0] - pos[v][0]))
    seen, faces = set(), []
    for i, j in list(bonds) + [(j, i) for i, j in bonds]:
        if (i, j) in seen:
            continue
        face, a, b = [], i, j
        while (a, b) not in seen:
            seen.add((a, b))
            face.append(a)
            ring = order[b]
            k = ring.index(a)
            c = ring[(k - 1) % len(ring)]   # next neighbour clockwise from a
            a, b = b, c
        area = 0.5 * sum(pos[face[k]][0] * pos[face[(k + 1) % len(face)]][1] -
                         pos[face[(k + 1) % len(face)]][0] * pos[face[k]][1] for k in range(len(face)))
        faces.append((abs(area), len(face)))
    faces.sort()
    return [n for _, n in faces[:-1]]


def build():
    pos, bonds, centres, hexes = honeycomb()
    crystal = (pos.copy(), set(bonds))
    nb = neighbours(bonds, len(pos))
    boundary = {k for k in range(len(pos)) if len(nb[k]) < 3}
    for (ci, cj) in SW_BONDS:
        ring = hexes[cj * NX + ci]
        stone_wales(pos, bonds, ring[0], ring[1])   # bond between vertices at 30 and 90 degrees
    pos = relax(pos, bonds, boundary)
    broken = []
    for (ci, cj) in BREAKS:
        ring = hexes[cj * NX + ci]
        b = tuple(sorted((ring[5], ring[0])))   # vertices at 330 and 30 degrees: right-hand bond
        if b in bonds:
            bonds.discard(b)
            broken.append(b)
    pos = relax(pos, bonds, boundary, apart=broken)
    return crystal, (pos, bonds, broken)


def tables(pos, bonds, broken=()):
    seg = [(pos[i][0], pos[i][1], pos[j][0] - pos[i][0], pos[j][1] - pos[i][1]) for i, j in sorted(bonds)]
    T = [(p[0], p[1]) for p in pos]
    O = [((pos[i][0] + pos[j][0]) / 2, (pos[i][1] + pos[j][1]) / 2) for i, j in sorted(bonds)]
    nbo, na = [], []
    for i, j in broken:
        u = (pos[j] - pos[i]) / np.linalg.norm(pos[j] - pos[i])
        a, b = pos[i] + 0.5 * D * u, pos[j] - 0.5 * D * u
        nbo += [tuple(a), tuple(b)]
        seg += [(pos[i][0], pos[i][1], a[0] - pos[i][0], a[1] - pos[i][1]),
                (pos[j][0], pos[j][1], b[0] - pos[j][0], b[1] - pos[j][1])]
        mid = (a + b) / 2
        na.append(tuple(mid + 0.35 * D * np.array([-u[1], u[0]])))
    return seg, T, O, nbo, na


if __name__ == "__main__":
    (cpos, cb), (gpos, gb, broken) = build()
    seg, T, O, _, _ = tables(cpos, cb)
    write_table(__file__, ("x", "y", "u", "v"), seg, part="crystal-bonds")
    write_table(__file__, ("x", "y"), T, part="crystal-T")
    write_table(__file__, ("x", "y"), O, part="crystal-O")
    seg, T, O, nbo, na = tables(gpos, gb, broken)
    write_table(__file__, ("x", "y", "u", "v"), seg, part="glass-bonds")
    write_table(__file__, ("x", "y"), T, part="glass-T")
    write_table(__file__, ("x", "y"), O, part="glass-O")
    write_table(__file__, ("x", "y"), nbo, part="glass-NBO")
    write_table(__file__, ("x", "y"), na, part="glass-Na")
    from collections import Counter
    print("crystal rings", Counter(rings(cpos, cb)), "glass rings", Counter(rings(gpos, gb)))
