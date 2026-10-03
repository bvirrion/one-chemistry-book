# Data ledger — One Chemistry Book (shared rows)

Every number the books quote for a real substance (an atomic weight, a pKa, a
standard potential, a bond energy, a solubility, an IR band, a ¹H shift, an
abundance) has a row in a ledger, with its source and the date the source was
read. **A value with no row is not printed.** A chapter that uses a row says so
in a source comment, `% ledger: <id>[, <id>...]`, next to the first use.

The ledger is split so that books written at the same time never edit the same
file:

- **this file** holds the rows every book shares and nobody needs to extend:
  the complete CIAAW standard atomic weights (`aw:`, every element that has
  one, 84 rows) and the fundamental constants (`const:`). Book agents
  treat it as read-only; a missing shared value is reported to the main
  session.
- **`sources/ledger/book<N>.md`** holds each book's own rows, with its own
  Sources table. A book may cite a row of another book's ledger (read-only)
  rather than duplicate it.

Row ids are unique across all ledger files, and `tools/check_ledger.py` checks
it: every `% ledger:` id resolves to exactly one row, every row names a source
key of its own file (or of this one) and an access date.

Numbers the book *computes* (a molar mass, a yield, a pH) are not ledger rows:
they are computed from rows, with `tools/molar_mass.py` or a `figdata/` script.
Values invented for an exercise (a concentration, a mass weighed) are data of
the exercise and need no row; values presented as facts about the world do.

`tools/chem.py` reads the `aw:` rows of this file: change an atomic weight here
and every molar mass computed by the tools follows.

## Sources

| key | source | URL |
|---|---|---|
| CIAAW-2024 | IUPAC Commission on Isotopic Abundances and Atomic Weights, *Abridged Standard Atomic Weights* (2024 table, from the Atomic Weights 2021 report) | https://www.ciaaw.org/abridged-atomic-weights.htm |
| CODATA-2022 | NIST, CODATA 2022 recommended values of the fundamental physical constants | https://physics.nist.gov/cuu/Constants/ (ASCII table: https://physics.nist.gov/cuu/Constants/Table/allascii.txt) |
| SI-2019 | BIPM, *The International System of Units*, 9th edition (2019), defining constants | https://www.bipm.org/en/publications/si-brochure |

## Rows

| id | quantity | value | unit | source | accessed |
|---|---|---|---|---|---|
| aw:H | standard atomic weight of H (hydrogen, Z = 1) | 1.0080 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:He | standard atomic weight of He (helium, Z = 2) | 4.0026 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Li | standard atomic weight of Li (lithium, Z = 3) | 6.94 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Be | standard atomic weight of Be (beryllium, Z = 4) | 9.0122 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:B | standard atomic weight of B (boron, Z = 5) | 10.81 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:C | standard atomic weight of C (carbon, Z = 6) | 12.011 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:N | standard atomic weight of N (nitrogen, Z = 7) | 14.007 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:O | standard atomic weight of O (oxygen, Z = 8) | 15.999 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:F | standard atomic weight of F (fluorine, Z = 9) | 18.998 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Ne | standard atomic weight of Ne (neon, Z = 10) | 20.180 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Na | standard atomic weight of Na (sodium, Z = 11) | 22.990 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Mg | standard atomic weight of Mg (magnesium, Z = 12) | 24.305 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Al | standard atomic weight of Al (aluminium, Z = 13) | 26.982 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Si | standard atomic weight of Si (silicon, Z = 14) | 28.085 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:P | standard atomic weight of P (phosphorus, Z = 15) | 30.974 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:S | standard atomic weight of S (sulfur, Z = 16) | 32.06 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Cl | standard atomic weight of Cl (chlorine, Z = 17) | 35.45 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Ar | standard atomic weight of Ar (argon, Z = 18) | 39.95 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:K | standard atomic weight of K (potassium, Z = 19) | 39.098 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Ca | standard atomic weight of Ca (calcium, Z = 20) | 40.078 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Sc | standard atomic weight of Sc (scandium, Z = 21) | 44.956 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Ti | standard atomic weight of Ti (titanium, Z = 22) | 47.867 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:V | standard atomic weight of V (vanadium, Z = 23) | 50.942 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Cr | standard atomic weight of Cr (chromium, Z = 24) | 51.996 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Mn | standard atomic weight of Mn (manganese, Z = 25) | 54.938 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Fe | standard atomic weight of Fe (iron, Z = 26) | 55.845 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Co | standard atomic weight of Co (cobalt, Z = 27) | 58.933 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Ni | standard atomic weight of Ni (nickel, Z = 28) | 58.693 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Cu | standard atomic weight of Cu (copper, Z = 29) | 63.546 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Zn | standard atomic weight of Zn (zinc, Z = 30) | 65.38 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Ga | standard atomic weight of Ga (gallium, Z = 31) | 69.723 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Ge | standard atomic weight of Ge (germanium, Z = 32) | 72.630 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:As | standard atomic weight of As (arsenic, Z = 33) | 74.922 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Se | standard atomic weight of Se (selenium, Z = 34) | 78.971 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Br | standard atomic weight of Br (bromine, Z = 35) | 79.904 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Kr | standard atomic weight of Kr (krypton, Z = 36) | 83.798 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Rb | standard atomic weight of Rb (rubidium, Z = 37) | 85.468 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Sr | standard atomic weight of Sr (strontium, Z = 38) | 87.62 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Y | standard atomic weight of Y (yttrium, Z = 39) | 88.906 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Zr | standard atomic weight of Zr (zirconium, Z = 40) | 91.222 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Nb | standard atomic weight of Nb (niobium, Z = 41) | 92.906 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Mo | standard atomic weight of Mo (molybdenum, Z = 42) | 95.95 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Ru | standard atomic weight of Ru (ruthenium, Z = 44) | 101.07 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Rh | standard atomic weight of Rh (rhodium, Z = 45) | 102.91 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Pd | standard atomic weight of Pd (palladium, Z = 46) | 106.42 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Ag | standard atomic weight of Ag (silver, Z = 47) | 107.87 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Cd | standard atomic weight of Cd (cadmium, Z = 48) | 112.41 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:In | standard atomic weight of In (indium, Z = 49) | 114.82 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Sn | standard atomic weight of Sn (tin, Z = 50) | 118.71 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Sb | standard atomic weight of Sb (antimony, Z = 51) | 121.76 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Te | standard atomic weight of Te (tellurium, Z = 52) | 127.60 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:I | standard atomic weight of I (iodine, Z = 53) | 126.90 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Xe | standard atomic weight of Xe (xenon, Z = 54) | 131.29 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Cs | standard atomic weight of Cs (caesium, Z = 55) | 132.91 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Ba | standard atomic weight of Ba (barium, Z = 56) | 137.33 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:La | standard atomic weight of La (lanthanum, Z = 57) | 138.91 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Ce | standard atomic weight of Ce (cerium, Z = 58) | 140.12 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Pr | standard atomic weight of Pr (praseodymium, Z = 59) | 140.91 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Nd | standard atomic weight of Nd (neodymium, Z = 60) | 144.24 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Sm | standard atomic weight of Sm (samarium, Z = 62) | 150.36 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Eu | standard atomic weight of Eu (europium, Z = 63) | 151.96 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Gd | standard atomic weight of Gd (gadolinium, Z = 64) | 157.25 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Tb | standard atomic weight of Tb (terbium, Z = 65) | 158.93 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Dy | standard atomic weight of Dy (dysprosium, Z = 66) | 162.50 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Ho | standard atomic weight of Ho (holmium, Z = 67) | 164.93 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Er | standard atomic weight of Er (erbium, Z = 68) | 167.26 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Tm | standard atomic weight of Tm (thulium, Z = 69) | 168.93 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Yb | standard atomic weight of Yb (ytterbium, Z = 70) | 173.05 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Lu | standard atomic weight of Lu (lutetium, Z = 71) | 174.97 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Hf | standard atomic weight of Hf (hafnium, Z = 72) | 178.49 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Ta | standard atomic weight of Ta (tantalum, Z = 73) | 180.95 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:W | standard atomic weight of W (tungsten, Z = 74) | 183.84 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Re | standard atomic weight of Re (rhenium, Z = 75) | 186.21 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Os | standard atomic weight of Os (osmium, Z = 76) | 190.23 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Ir | standard atomic weight of Ir (iridium, Z = 77) | 192.22 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Pt | standard atomic weight of Pt (platinum, Z = 78) | 195.08 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Au | standard atomic weight of Au (gold, Z = 79) | 196.97 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Hg | standard atomic weight of Hg (mercury, Z = 80) | 200.59 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Tl | standard atomic weight of Tl (thallium, Z = 81) | 204.38 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Pb | standard atomic weight of Pb (lead, Z = 82) | 207.2 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Bi | standard atomic weight of Bi (bismuth, Z = 83) | 208.98 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Th | standard atomic weight of Th (thorium, Z = 90) | 232.04 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:Pa | standard atomic weight of Pa (protactinium, Z = 91) | 231.04 | g/mol | CIAAW-2024 | 2026-10-02 |
| aw:U | standard atomic weight of U (uranium, Z = 92) | 238.03 | g/mol | CIAAW-2024 | 2026-10-02 |
| const:NA | Avogadro constant (exact) | 6.02214076e23 | /mol | SI-2019 | 2026-10-02 |
| const:e | elementary charge (exact) | 1.602176634e-19 | C | SI-2019 | 2026-10-02 |
| const:F | Faraday constant, N_A e | 96485.33212 | C/mol | SI-2019 | 2026-10-02 |
| const:a0 | Bohr radius (size of the hydrogen atom: diameter about 2 a0 = 0.106 nm) | 5.29177210544e-11 | m | CODATA-2022 | 2026-10-02 |
| const:R | molar gas constant (exact), N_A k | 8.314462618 | J/(mol.K) | SI-2019 | 2026-10-02 |
| const:kB | Boltzmann constant (exact) | 1.380649e-23 | J/K | SI-2019 | 2026-10-02 |
| const:h | Planck constant (exact) | 6.62607015e-34 | J.s | SI-2019 | 2026-10-02 |
| const:c | speed of light in vacuum (exact) | 299792458 | m/s | SI-2019 | 2026-10-02 |
| const:eV | electronvolt (exact) | 1.602176634e-19 | J | SI-2019 | 2026-10-02 |
| const:me | electron mass | 9.1093837139e-31 | kg | CODATA-2022 | 2026-10-02 |
| const:mp | proton mass | 1.67262192595e-27 | kg | CODATA-2022 | 2026-10-02 |
| const:mn | neutron mass | 1.67492750056e-27 | kg | CODATA-2022 | 2026-10-02 |
| const:u | atomic mass constant (1 Da) | 1.66053906892e-27 | kg | CODATA-2022 | 2026-10-02 |
| const:eps0 | vacuum electric permittivity | 8.8541878188e-12 | F/m | CODATA-2022 | 2026-10-02 |
| const:Eh | Hartree energy | 4.3597447222060e-18 | J | CODATA-2022 | 2026-10-02 |
| const:RyhcEV | Rydberg energy hcR (ionisation energy scale of hydrogen) | 13.605693122990 | eV | CODATA-2022 | 2026-10-02 |
| const:Rinf | Rydberg constant | 10973731.568157 | 1/m | CODATA-2022 | 2026-10-02 |
| const:muB | Bohr magneton | 9.2740100657e-24 | J/T | CODATA-2022 | 2026-10-02 |
| const:muN | nuclear magneton | 5.0507837393e-27 | J/T | CODATA-2022 | 2026-10-02 |
| const:gammaP | proton gyromagnetic ratio over 2 pi | 42.577478461 | MHz/T | CODATA-2022 | 2026-10-02 |
| const:Vm0 | molar volume of an ideal gas at 273.15 K and 100 kPa (exact) | 22.71095464 | L/mol | CODATA-2022 | 2026-10-02 |
| const:Vm1 | molar volume of an ideal gas at 273.15 K and 101.325 kPa (exact) | 22.41396954 | L/mol | CODATA-2022 | 2026-10-02 |
| const:atm | standard atmosphere (exact) | 101325 | Pa | CODATA-2022 | 2026-10-02 |
| const:pstd | standard pressure p° (IUPAC) | 1e5 | Pa | SI-2019 | 2026-10-02 |
