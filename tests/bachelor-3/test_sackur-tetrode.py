"""Statistical entropies against the tabulated values, and the table the
chapter prints against the script."""
import importlib.util
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
spec = importlib.util.spec_from_file_location("st", os.path.join(ROOT, "figdata", "bachelor-3", "sackur-tetrode.py"))
st = importlib.util.module_from_spec(spec)
spec.loader.exec_module(st)


def test_agreement_with_tables():
    for n, r in st.table().items():
        assert abs(r["total"] - r["ref"]) < 0.5, n
    assert round(st.table()["N2"]["total"], 1) == 191.6


def test_printed_table():
    tex = open(os.path.join(ROOT, "parts", "bachelor-3", "10-partition-functions.tex"), encoding="utf8").read()
    block = tex[tex.index("% table: sackur-tetrode"):]
    block = block[:block.index("\\end{tabular}")]
    names = {"Ar": "Ar", "N2": "N2", "CO": "CO", "HCl": "HCl", "Cl2": "Cl2", "I2": "I2", "Cl": "Cl"}
    t = st.table()
    seen = 0
    for line in block.splitlines():
        m = re.match(r"\s*\\ce\{(\w+)\}\s*&(.*)\\\\", line)
        if not m:
            continue
        nums = [float(x) for x in re.findall(r"-?\d+\.\d+", m.group(2))]
        r = t[names[m.group(1)]]
        want = [r["trans"], r["rot"], r["vib"], r["elec"], r["total"], r["ref"]]
        assert len(nums) == 6, line
        assert all(abs(a - b) <= 0.0051 + 1e-9 for a, b in zip(nums, want)), (line, want)
        seen += 1
    assert seen == 7
