"""Ch. 5, the reduction formula at work: Gamma_3N from the unshifted atoms,
its reduction, Gamma_vib after removing translations and rotations, and the
numbers of IR- and Raman-active fundamentals, for seven molecules. The
character tables are those printed in ch. 4-5 (Katzer's tables); a test
checks their orthogonality and that every reduction gives integers.
Written out as a table (one row per molecule, irreps coded in a string)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

# class: (size, kind, angle in degrees); kind R = proper, S = improper
GROUPS = {
    "C2v": ([(1, "R", 0), (1, "R", 180), (1, "S", 0), (1, "S", 0)],
            {"A1": (1, 1, 1, 1), "A2": (1, 1, -1, -1), "B1": (1, -1, 1, -1), "B2": (1, -1, -1, 1)},
            ["A1", "B1", "B2"], ["A2", "B1", "B2"], ["A1", "B1", "B2"], ["A1", "A2", "B1", "B2"]),
    "C3v": ([(1, "R", 0), (2, "R", 120), (3, "S", 0)],
            {"A1": (1, 1, 1), "A2": (1, 1, -1), "E": (2, -1, 0)},
            ["A1", "E"], ["A2", "E"], ["A1", "E"], ["A1", "E"]),
    "Td": ([(1, "R", 0), (8, "R", 120), (3, "R", 180), (6, "S", 90), (6, "S", 0)],
           {"A1": (1, 1, 1, 1, 1), "A2": (1, 1, 1, -1, -1), "E": (2, -1, 2, 0, 0),
            "T1": (3, 0, -1, 1, -1), "T2": (3, 0, -1, -1, 1)},
           ["T2"], ["T1"], ["T2"], ["A1", "E", "T2"]),
    "D2h": ([(1, "R", 0), (1, "R", 180), (1, "R", 180), (1, "R", 180), (1, "S", 180),
             (1, "S", 0), (1, "S", 0), (1, "S", 0)],
            {"Ag": (1, 1, 1, 1, 1, 1, 1, 1), "B1g": (1, 1, -1, -1, 1, 1, -1, -1),
             "B2g": (1, -1, 1, -1, 1, -1, 1, -1), "B3g": (1, -1, -1, 1, 1, -1, -1, 1),
             "Au": (1, 1, 1, 1, -1, -1, -1, -1), "B1u": (1, 1, -1, -1, -1, -1, 1, 1),
             "B2u": (1, -1, 1, -1, -1, 1, -1, 1), "B3u": (1, -1, -1, 1, -1, 1, 1, -1)},
            ["B1u", "B2u", "B3u"], ["B2g", "B3g"], ["B1u", "B2u", "B3u"],
            ["Ag", "B1g", "B2g", "B3g"]),
    "D3h": ([(1, "R", 0), (2, "R", 120), (3, "R", 180), (1, "S", 0), (2, "S", 120), (3, "S", 0)],
            {"A1'": (1, 1, 1, 1, 1, 1), "A2'": (1, 1, -1, 1, 1, -1), "E'": (2, -1, 0, 2, -1, 0),
             "A1''": (1, 1, 1, -1, -1, -1), "A2''": (1, 1, -1, -1, -1, 1), "E''": (2, -1, 0, -2, 1, 0)},
            ["E'", "A2''"], ["A2'", "E''"], ["E'", "A2''"], ["A1'", "E'", "E''"]),
    "D4h": ([(1, "R", 0), (2, "R", 90), (1, "R", 180), (2, "R", 180), (2, "R", 180), (1, "S", 180),
             (2, "S", 90), (1, "S", 0), (2, "S", 0), (2, "S", 0)],
            {"A1g": (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), "A2g": (1, 1, 1, -1, -1, 1, 1, 1, -1, -1),
             "B1g": (1, -1, 1, 1, -1, 1, -1, 1, 1, -1), "B2g": (1, -1, 1, -1, 1, 1, -1, 1, -1, 1),
             "Eg": (2, 0, -2, 0, 0, 2, 0, -2, 0, 0), "A1u": (1, 1, 1, 1, 1, -1, -1, -1, -1, -1),
             "A2u": (1, 1, 1, -1, -1, -1, -1, -1, 1, 1), "B1u": (1, -1, 1, 1, -1, -1, 1, -1, -1, 1),
             "B2u": (1, -1, 1, -1, 1, -1, 1, -1, 1, -1), "Eu": (2, 0, -2, 0, 0, -2, 0, 2, 0, 0)},
            ["A2u", "Eu"], ["A2g", "Eg"], ["A2u", "Eu"], ["A1g", "B1g", "B2g", "Eg"]),
    "Oh": ([(1, "R", 0), (8, "R", 120), (6, "R", 180), (6, "R", 90), (3, "R", 180), (1, "S", 180),
            (6, "S", 90), (8, "S", 60), (3, "S", 0), (6, "S", 0)],
           {"A1g": (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), "A2g": (1, 1, -1, -1, 1, 1, -1, 1, 1, -1),
            "Eg": (2, -1, 0, 0, 2, 2, 0, -1, 2, 0), "T1g": (3, 0, -1, 1, -1, 3, 1, 0, -1, -1),
            "T2g": (3, 0, 1, -1, -1, 3, -1, 0, -1, 1), "A1u": (1, 1, 1, 1, 1, -1, -1, -1, -1, -1),
            "A2u": (1, 1, -1, -1, 1, -1, 1, -1, -1, 1), "Eu": (2, -1, 0, 0, 2, -2, 0, 1, -2, 0),
            "T1u": (3, 0, -1, 1, -1, -3, -1, 0, 1, 1), "T2u": (3, 0, 1, -1, -1, -3, 1, 0, 1, -1)},
           ["T1u"], ["T1g"], ["T1u"], ["A1g", "Eg", "T2g"]),
}

# molecule: group, unshifted atoms per class, linear?
MOLECULES = {
    "H2O": ("C2v", (3, 1, 3, 1), False),
    "NH3": ("C3v", (4, 1, 2), False),
    "CH4": ("Td", (5, 2, 1, 1, 3), False),
    "CO2": ("D2h", (3, 3, 1, 1, 1, 1, 3, 3), True),
    "BF3": ("D3h", (4, 1, 2, 4, 1, 2), False),
    "XeF4": ("D4h", (5, 1, 1, 3, 1, 1, 1, 5, 3, 1), False),
    "SF6": ("Oh", (7, 1, 1, 3, 3, 1, 1, 1, 5, 3), False),
}


def contribution(kind, angle):
    c = 2 * math.cos(math.radians(angle))
    return round(1 + c) if kind == "R" else round(-1 + c)


def reduce(group, chars):
    classes, irreps = GROUPS[group][0], GROUPS[group][1]
    h = sum(g for g, _, _ in classes)
    out = {}
    for name, row in irreps.items():
        n = sum(g * x * y for (g, _, _), x, y in zip(classes, chars, row)) / h
        out[name] = n
    return out


def gamma_3n(mol):
    group, unshifted, _ = MOLECULES[mol]
    return [u * contribution(k, a) for u, (_, k, a) in zip(unshifted, GROUPS[group][0])]


def gamma_vib(mol):
    group, _, linear = MOLECULES[mol]
    _, irreps, trans, rot, _, _ = GROUPS[group]
    n = {k: int(round(v)) for k, v in reduce(group, gamma_3n(mol)).items()}
    for t in trans:
        n[t] -= 1
    for r in rot:
        n[r] -= 1
    # a linear molecule (CO2 along z) has only two rotations: the GROUPS entry
    # for D2h lists R_x, R_y (B3g, B2g) and not R_z
    return {k: v for k, v in n.items() if v}


def dim(group, name):
    return GROUPS[group][1][name][0]


def counts(mol):
    group = MOLECULES[mol][0]
    _, _, _, _, ir, raman = GROUPS[group]
    v = gamma_vib(mol)
    modes = sum(n * dim(group, k) for k, n in v.items())
    n_ir = sum(n for k, n in v.items() if k in ir)
    n_raman = sum(n for k, n in v.items() if k in raman)
    return modes, n_ir, n_raman


def label(v):
    order = list(v)
    return " + ".join(("%d%s" % (n, k) if n > 1 else k) for k, n in v.items())


if __name__ == "__main__":
    rows = []
    for i, m in enumerate(MOLECULES):
        modes, n_ir, n_raman = counts(m)
        rows.append((i + 1, modes, n_ir, n_raman))
    write_table(__file__, ("index", "modes", "IR", "Raman"), rows)
    for m in MOLECULES:
        print(m, MOLECULES[m][0], label(gamma_vib(m)), counts(m))
