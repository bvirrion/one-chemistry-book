"""tools/chem.py: the parser behind the balance gate and the molar masses."""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
import chem  # noqa: E402
import molar_mass  # noqa: E402


@pytest.mark.parametrize("expr", [
    "2H2 + O2 -> 2H2O",
    "CH4 + 2O2 -> CO2 + 2H2O",
    "C3H8 + 5O2 -> 3CO2 + 4H2O",
    "Cu^{2+}(aq) + 2e- -> Cu(s)",
    "Cu^2+ + 2e- <=> Cu",
    "MnO4^- + 8H+ + 5e- <=> Mn^{2+} + 4H2O",
    "Fe(s) + 2H+(aq) -> Fe^{2+}(aq) + H2(g)",
    "H3O+ + HO- <=> 2H2O",
    "Ag+ + Cl- -> AgCl v",
    "CaCO3 ->[heat] CaO + CO2 ^",
    "Ca(OH)2 + CO2 -> CaCO3 + H2O",
    "CuSO4 + 5H2O -> CuSO4.5H2O",
    "CH3-CH2-OH + 3O2 -> 2CO2 + 3H2O",
    "CH2=CH2 + H2O -> CH3CH2OH",
    "H2 + 1/2O2 -> H2O",
    "Cr2O7^{2-} + 14H+ + 6e- <=> 2Cr^{3+} + 7H2O",
    "Al2(SO4)3 -> 2Al^{3+} + 3SO4^{2-}",
    "[Cu(H2O)6]^{2+} + 4NH3 <=> [Cu(NH3)4(H2O)2]^{2+} + 4H2O",
    "2Na + Cl2 -> 2NaCl",
    "N2 + 3H2 <=> 2NH3",
])
def test_balanced(expr):
    assert chem.balance(expr) is None


@pytest.mark.parametrize("expr,frag", [
    ("H2 + O2 -> H2O", "O"),
    ("CH4 + O2 -> CO2 + 2H2O", "O"),
    ("Cu^{2+} + e- -> Cu", "charge"),
    ("Fe + H+ -> Fe^{2+} + H2", "H"),
    ("MnO4- + 8H+ + 4e- <=> Mn^2+ + 4H2O", "charge"),
])
def test_unbalanced(expr, frag):
    res = chem.balance(expr)
    assert res and frag in res


@pytest.mark.parametrize("expr", [
    "H2O", "CO2", "methane + oxygen -> carbon dioxide + water",
])
def test_nothing_to_check(expr):
    assert chem.balance(expr) == ""


def test_species_parts():
    coef, atoms, q = chem.parse_species("3SO4^{2-}(aq)")
    assert coef == 3 and atoms == {"S": 1, "O": 4} and q == -2
    assert chem.parse_species("OH-")[2] == -1
    assert chem.parse_species("NH4+")[1] == {"N": 1, "H": 4}
    assert chem.parse_species("2e-")[0] == 2


def test_unreadable():
    with pytest.raises(chem.ParseError):
        chem.balance("Ca(OH2 -> Ca")


def test_molar_masses():
    w = chem.atomic_weights()
    assert chem.molar_mass("H2O", w) == pytest.approx(18.015, abs=1e-3)
    assert chem.molar_mass("CuSO4.5H2O", w) == pytest.approx(249.677, abs=1e-3)
    wb = molar_mass.book_weights()
    assert wb["Cl"] == 35.5 and wb["H"] == 1.0 and wb["Cu"] == 63.5
    assert chem.molar_mass("NaCl", wb) == pytest.approx(58.5)
