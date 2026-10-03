# Data ledger — Book 3 (University Year 2)

Book 3's own rows. Shared rows (atomic weights, constants) are in
`sources/data_ledger.md`; the rules are stated there. Owned by the Book 3
writer; other books may cite these rows read-only.

## Sources

| key | source | URL |
|---|---|---|
| CODATA-KEY | J. D. Cox, D. D. Wagman, V. A. Medvedev, *CODATA Key Values for Thermodynamics* (Hemisphere, 1989), online table of the CODATA key values: standard enthalpy of formation and entropy at 298.15 K, p° = 1 bar, with the stated uncertainty | https://www.codata.info/resources/databases/key1.html |
| JANAF | M. W. Chase, *NIST-JANAF Thermochemical Tables*, 4th ed., J. Phys. Chem. Ref. Data Monograph 9 (1998), online tables (`tables/<id>.txt`; table id and temperature in the row) | https://janaf.nist.gov/ |
| WEBBOOK-THERMO | NIST Chemistry WebBook, SRD 69, gas- and condensed-phase thermochemistry and reaction thermochemistry (the cited determination is named in the row) | https://webbook.nist.gov/chemistry/ |
| WEBBOOK-PHASE | NIST Chemistry WebBook, SRD 69, phase-change data (Antoine parameters, Tboil, Tfus, enthalpies of fusion and vaporisation; the cited determination is named in the row) | https://webbook.nist.gov/chemistry/ |
| WEBBOOK-DIAT | NIST Chemistry WebBook, SRD 69, constants of diatomic molecules (Huber and Herzberg compilation) | https://webbook.nist.gov/chemistry/ |
| WEBBOOK-IEMOL | NIST Chemistry WebBook, SRD 69, gas-phase ion energetics (ionisation energy determinations; the cited value is named in the row) | https://webbook.nist.gov/chemistry/ |
| WEBBOOK-MS | NIST Chemistry WebBook, SRD 69, electron-ionisation mass spectra (NIST Mass Spectrometry Data Center); m/z and relative intensity read from the JCAMP-DX data | https://webbook.nist.gov/chemistry/ |
| NBS-82 | D. D. Wagman et al., The NBS tables of chemical thermodynamic properties, J. Phys. Chem. Ref. Data 11, Suppl. 2 (1982); values at 298.15 K, read from the scanned tables (page in the row) | https://srd.nist.gov/JPCRD/jpcrdS2Vol11.pdf |
| NIST-SOLDER | NIST Metallurgy Division, *Phase Diagrams & Computational Thermodynamics: Solder Systems* (U. R. Kattner et al.), calculated invariant equilibria (system page in the row) | https://www.metallurgy.nist.gov/phase/solder/solder.html |
| SANDER-2023 | R. Sander, *Compilation of Henry's law constants (version 5.0.0) for water as solvent*, Atmos. Chem. Phys. 23, 10901 (2023), CC BY 4.0; the recommended value of the species is used | https://henry.mpch-mainz.gwdg.de/ |
| IUPAC-PKA | J. W. Zheng and O. Lafontant-Joseph, IUPAC Digitized pKa Dataset v2.4a (from Serjeant and Dempsey 1979; Perrin 1965, 1972), file iupac_high-confidence_v2_4.csv; unique_ID and original reference in the row | https://github.com/IUPAC/Dissociation-Constants |
| CIAAW-ISO | IUPAC Commission on Isotopic Abundances and Atomic Weights, isotopic compositions of the elements (element pages) | https://www.ciaaw.org/ |
| NIST-AWIC | NIST, *Atomic Weights and Isotopic Compositions with Relative Atomic Masses* (J. S. Coursey et al.), relative atomic masses of the isotopes | https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl |
| NIST-ASD | NIST Atomic Spectra Database, version 5, lines data (observed wavelength in air) | https://physics.nist.gov/PhysRefData/ASD/lines_form.html |
| NMRSHIFTDB | nmrshiftdb2, open NMR database (CC BY-SA); measured spectrum id in the row | https://nmrshiftdb.nmr.uni-koeln.de/ |
| PUBCHEM | PubChem compound records (PUG-View), the cited section and its source (HSDB, CRC, …) given in the row | https://pubchem.ncbi.nlm.nih.gov/ |
| PUBCHEM-GHSSUM | PubChem, *GHS Classification Summary* of the compound (ECHA C&L notifications), pictograms and hazard statements | https://pubchem.ncbi.nlm.nih.gov/ |
| USGS-MCS2026 | U.S. Geological Survey, *Mineral Commodity Summaries 2026*, commodity chapters, World Mine/Smelter Production tables; 2025 values are USGS estimates | https://pubs.usgs.gov/periodicals/mcs2026/ |
| IAI | International Aluminium Institute, statistics: primary aluminium smelting energy intensity (AC power used, world) | https://international-aluminium.org/statistics/ |
| WEBBOOK-FLUID | NIST Chemistry WebBook, SRD 69, thermophysical properties of fluid systems (E. W. Lemmon et al.; water from the IAPWS-95 formulation), isobaric and isothermal data | https://webbook.nist.gov/chemistry/fluid/ |
| IAPWS-ICE | IAPWS, *Revised Release on the Equation of State 2006 for H2O Ice Ih* (2009), Table 6: properties at the triple point (enthalpy of ice relative to the liquid at the triple point) | https://iapws.org/technical-guidance/release/Ice-2009 |
| WHO-DWQ | World Health Organization, *Guidelines for drinking-water quality*, 4th ed. incorporating the first and second addenda (2022), chemical fact sheet for lead | https://www.who.int/publications/i/item/9789240045064 |
| NIST-SOLDER-TDB | NIST Metallurgy Division, solder thermodynamic database `NIST-solder.tdb` (U. R. Kattner et al.), unary lattice stabilities from the SGTE data (A. T. Dinsdale, Calphad 15, 317 (1991)); fusion enthalpy = liquid-minus-solid enthalpy at the melting point, computed from the PARAMETER G(LIQUID,<el>;0) expression | https://www.metallurgy.nist.gov/phase/solder/NIST-solder.tdb |
| HAMP-2024 | R. E. Hamp, C. G. Salzmann et al., Metastable dihydrate of sodium chloride at ambient pressure, J. Phys. Chem. Lett. (2024), open access (PMC11664646): "The ice Ih and SC2-I eutectic is reached at 23.3 wt % (5.20 mol kg-1) NaCl and 252 K at 1 bar" | https://pmc.ncbi.nlm.nih.gov/articles/PMC11664646/ |

## Rows

| id | quantity | value | unit | source | accessed |
|---|---|---|---|---|---|
| dfh:H2O_g | standard enthalpy of formation of H2O(g) at 298.15 K (uncertainty 0.040) | -241.826 | kJ/mol | CODATA-KEY | 2026-10-02 |
| s0:H2O_l | standard molar entropy of H2O(l) at 298.15 K (uncertainty 0.03) | 69.95 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| s0:H2O_g | standard molar entropy of H2O(g) at 298.15 K (uncertainty 0.010) | 188.835 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| s0:CO2_g | standard molar entropy of CO2(g) at 298.15 K (uncertainty 0.010) | 213.785 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| dfh:CO_g | standard enthalpy of formation of CO(g) at 298.15 K (uncertainty 0.17) | -110.53 | kJ/mol | CODATA-KEY | 2026-10-02 |
| s0:CO_g | standard molar entropy of CO(g) at 298.15 K (uncertainty 0.004) | 197.660 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| s0:O2_g | standard molar entropy of O2(g) at 298.15 K (uncertainty 0.005) | 205.152 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| s0:N2_g | standard molar entropy of N2(g) at 298.15 K (uncertainty 0.004) | 191.609 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| s0:H2_g | standard molar entropy of H2(g) at 298.15 K (uncertainty 0.003) | 130.680 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| s0:C_gr | standard molar entropy of C(cr, graphite) at 298.15 K (uncertainty 0.10) | 5.74 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| dfh:C_g | standard enthalpy of formation of C(g) at 298.15 K (uncertainty 0.45) | 716.68 | kJ/mol | CODATA-KEY | 2026-10-02 |
| dfh:O_g | standard enthalpy of formation of O(g) at 298.15 K (uncertainty 0.10) | 249.18 | kJ/mol | CODATA-KEY | 2026-10-02 |
| dfh:N_g | standard enthalpy of formation of N(g) at 298.15 K (uncertainty 0.40) | 472.68 | kJ/mol | CODATA-KEY | 2026-10-02 |
| dfh:Na_g | standard enthalpy of formation of Na(g) at 298.15 K (uncertainty 0.7) | 107.5 | kJ/mol | CODATA-KEY | 2026-10-02 |
| dfh:NH3_g | standard enthalpy of formation of NH3(g) at 298.15 K (uncertainty 0.35) | -45.94 | kJ/mol | CODATA-KEY | 2026-10-02 |
| s0:NH3_g | standard molar entropy of NH3(g) at 298.15 K (uncertainty 0.05) | 192.77 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| s0:Ar_g | standard molar entropy of Ar(g) at 298.15 K (uncertainty 0.003) | 154.846 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| s0:Cl2_g | standard molar entropy of Cl2(g) at 298.15 K (uncertainty 0.010) | 223.081 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| s0:Na_cr | standard molar entropy of Na(cr) at 298.15 K (uncertainty 0.20) | 51.30 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| dfh:C4H10_g | standard enthalpy of formation of butane(g) at 298.15 K (Pittam and Pilcher, 1972; uncertainty 0.67) | -125.6 | kJ/mol | WEBBOOK-THERMO | 2026-10-02 |
| dfh:C3H8_g | standard enthalpy of formation of propane(g) at 298.15 K (Pittam and Pilcher, 1972; uncertainty 0.50) | -104.7 | kJ/mol | WEBBOOK-THERMO | 2026-10-02 |
| dfh:C2H6_g | standard enthalpy of formation of ethane(g) at 298.15 K (Pittam and Pilcher, 1972; uncertainty 0.3) | -83.8 | kJ/mol | WEBBOOK-THERMO | 2026-10-02 |
| dfh:C6H6_l | standard enthalpy of formation of benzene(l) at 298.15 K (review, Roux, Temprado et al., 2008; uncertainty 0.9) | 49.0 | kJ/mol | WEBBOOK-THERMO | 2026-10-02 |
| dfh:CH4_g | standard enthalpy of formation, Methane (CH4), table C-067 at 298.15 K | -74.873 | kJ/mol | JANAF | 2026-10-02 |
| s0:CH4_g | standard molar entropy, Methane (CH4), table C-067 at 298.15 K | 186.251 | J/(K.mol) | JANAF | 2026-10-02 |
| dfh:NaCl_cr | standard enthalpy of formation, Sodium Chloride (NaCl), table Cl-053 at 298.15 K | -411.12 | kJ/mol | JANAF | 2026-10-02 |
| s0:NaCl_cr | standard molar entropy, Sodium Chloride (NaCl), table Cl-053 at 298.15 K | 72.115 | J/(K.mol) | JANAF | 2026-10-02 |
| dfh:NO_g | standard enthalpy of formation, Nitrogen Oxide (NO), table N-005 at 298.15 K | 90.291 | kJ/mol | JANAF | 2026-10-02 |
| s0:NO_g | standard molar entropy, Nitrogen Oxide (NO), table N-005 at 298.15 K | 210.758 | J/(K.mol) | JANAF | 2026-10-02 |
| dfh:C2H4_g | standard enthalpy of formation, Ethene (C2H4), table C-128 at 298.15 K | 52.467 | kJ/mol | JANAF | 2026-10-02 |
| janafdfH:NH3.700 | standard enthalpy of formation, Ammonia (NH3), table H-083 at 700 K | -52.618 | kJ/mol | JANAF | 2026-10-02 |
| cp:CO2_g.298 | standard molar heat capacity Cp, Carbon Dioxide (CO2), table C-095 at 298.15 K | 37.129 | J/(K.mol) | JANAF | 2026-10-02 |
| cp:H2O_g.298 | standard molar heat capacity Cp, Water (H2O), table H-064 at 298.15 K | 33.59 | J/(K.mol) | JANAF | 2026-10-02 |
| cp:N2_g.298 | standard molar heat capacity Cp, Nitrogen (N2), table N-023 at 298.15 K | 29.124 | J/(K.mol) | JANAF | 2026-10-02 |
| cp:O2_g.298 | standard molar heat capacity Cp, Oxygen (O2), table O-029 at 298.15 K | 29.376 | J/(K.mol) | JANAF | 2026-10-02 |
| cp:Ar_g.298 | standard molar heat capacity Cp, Argon (Ar), table Ar-001 at 298.15 K | 20.786 | J/(K.mol) | JANAF | 2026-10-02 |
| cp:NH3_g.298 | standard molar heat capacity Cp, Ammonia (NH3), table H-083 at 298.15 K | 35.652 | J/(K.mol) | JANAF | 2026-10-02 |
| cp:H2_g.298 | standard molar heat capacity Cp, Hydrogen (H2), table H-050 at 298.15 K | 28.836 | J/(K.mol) | JANAF | 2026-10-02 |
| cp:H2O_l.298 | standard molar heat capacity Cp, Water (H2O), table H-063 at 298.15 K | 75.351 | J/(K.mol) | JANAF | 2026-10-02 |
| janafH:CO2.500 | enthalpy increment H(T)-H(298.15 K), Carbon Dioxide (CO2), table C-095 at 500 K | 8.305 | kJ/mol | JANAF | 2026-10-02 |
| janafH:CO2.1000 | enthalpy increment H(T)-H(298.15 K), Carbon Dioxide (CO2), table C-095 at 1000 K | 33.397 | kJ/mol | JANAF | 2026-10-02 |
| janafH:CO2.1500 | enthalpy increment H(T)-H(298.15 K), Carbon Dioxide (CO2), table C-095 at 1500 K | 61.705 | kJ/mol | JANAF | 2026-10-02 |
| janafH:CO2.2000 | enthalpy increment H(T)-H(298.15 K), Carbon Dioxide (CO2), table C-095 at 2000 K | 91.439 | kJ/mol | JANAF | 2026-10-02 |
| janafH:CO2.2100 | enthalpy increment H(T)-H(298.15 K), Carbon Dioxide (CO2), table C-095 at 2100 K | 97.488 | kJ/mol | JANAF | 2026-10-02 |
| janafH:CO2.2200 | enthalpy increment H(T)-H(298.15 K), Carbon Dioxide (CO2), table C-095 at 2200 K | 103.562 | kJ/mol | JANAF | 2026-10-02 |
| janafH:CO2.2300 | enthalpy increment H(T)-H(298.15 K), Carbon Dioxide (CO2), table C-095 at 2300 K | 109.66 | kJ/mol | JANAF | 2026-10-02 |
| janafH:CO2.2400 | enthalpy increment H(T)-H(298.15 K), Carbon Dioxide (CO2), table C-095 at 2400 K | 115.779 | kJ/mol | JANAF | 2026-10-02 |
| janafH:CO2.2500 | enthalpy increment H(T)-H(298.15 K), Carbon Dioxide (CO2), table C-095 at 2500 K | 121.917 | kJ/mol | JANAF | 2026-10-02 |
| janafH:CO2.3000 | enthalpy increment H(T)-H(298.15 K), Carbon Dioxide (CO2), table C-095 at 3000 K | 152.852 | kJ/mol | JANAF | 2026-10-02 |
| janafH:H2O.500 | enthalpy increment H(T)-H(298.15 K), Water (H2O), table H-064 at 500 K | 6.925 | kJ/mol | JANAF | 2026-10-02 |
| janafH:H2O.1000 | enthalpy increment H(T)-H(298.15 K), Water (H2O), table H-064 at 1000 K | 26.0 | kJ/mol | JANAF | 2026-10-02 |
| janafH:H2O.1500 | enthalpy increment H(T)-H(298.15 K), Water (H2O), table H-064 at 1500 K | 48.151 | kJ/mol | JANAF | 2026-10-02 |
| janafH:H2O.2000 | enthalpy increment H(T)-H(298.15 K), Water (H2O), table H-064 at 2000 K | 72.79 | kJ/mol | JANAF | 2026-10-02 |
| janafH:H2O.2100 | enthalpy increment H(T)-H(298.15 K), Water (H2O), table H-064 at 2100 K | 77.941 | kJ/mol | JANAF | 2026-10-02 |
| janafH:H2O.2200 | enthalpy increment H(T)-H(298.15 K), Water (H2O), table H-064 at 2200 K | 83.153 | kJ/mol | JANAF | 2026-10-02 |
| janafH:H2O.2300 | enthalpy increment H(T)-H(298.15 K), Water (H2O), table H-064 at 2300 K | 88.421 | kJ/mol | JANAF | 2026-10-02 |
| janafH:H2O.2400 | enthalpy increment H(T)-H(298.15 K), Water (H2O), table H-064 at 2400 K | 93.741 | kJ/mol | JANAF | 2026-10-02 |
| janafH:H2O.2500 | enthalpy increment H(T)-H(298.15 K), Water (H2O), table H-064 at 2500 K | 99.108 | kJ/mol | JANAF | 2026-10-02 |
| janafH:H2O.3000 | enthalpy increment H(T)-H(298.15 K), Water (H2O), table H-064 at 3000 K | 126.549 | kJ/mol | JANAF | 2026-10-02 |
| janafH:N2.500 | enthalpy increment H(T)-H(298.15 K), Nitrogen (N2), table N-023 at 500 K | 5.911 | kJ/mol | JANAF | 2026-10-02 |
| janafH:N2.1000 | enthalpy increment H(T)-H(298.15 K), Nitrogen (N2), table N-023 at 1000 K | 21.463 | kJ/mol | JANAF | 2026-10-02 |
| janafH:N2.1500 | enthalpy increment H(T)-H(298.15 K), Nitrogen (N2), table N-023 at 1500 K | 38.405 | kJ/mol | JANAF | 2026-10-02 |
| janafH:N2.2000 | enthalpy increment H(T)-H(298.15 K), Nitrogen (N2), table N-023 at 2000 K | 56.137 | kJ/mol | JANAF | 2026-10-02 |
| janafH:N2.2100 | enthalpy increment H(T)-H(298.15 K), Nitrogen (N2), table N-023 at 2100 K | 59.742 | kJ/mol | JANAF | 2026-10-02 |
| janafH:N2.2200 | enthalpy increment H(T)-H(298.15 K), Nitrogen (N2), table N-023 at 2200 K | 63.361 | kJ/mol | JANAF | 2026-10-02 |
| janafH:N2.2300 | enthalpy increment H(T)-H(298.15 K), Nitrogen (N2), table N-023 at 2300 K | 66.995 | kJ/mol | JANAF | 2026-10-02 |
| janafH:N2.2400 | enthalpy increment H(T)-H(298.15 K), Nitrogen (N2), table N-023 at 2400 K | 70.64 | kJ/mol | JANAF | 2026-10-02 |
| janafH:N2.2500 | enthalpy increment H(T)-H(298.15 K), Nitrogen (N2), table N-023 at 2500 K | 74.296 | kJ/mol | JANAF | 2026-10-02 |
| janafH:N2.3000 | enthalpy increment H(T)-H(298.15 K), Nitrogen (N2), table N-023 at 3000 K | 92.715 | kJ/mol | JANAF | 2026-10-02 |
| janafH:O2.500 | enthalpy increment H(T)-H(298.15 K), Oxygen (O2), table O-029 at 500 K | 6.084 | kJ/mol | JANAF | 2026-10-02 |
| janafH:O2.1000 | enthalpy increment H(T)-H(298.15 K), Oxygen (O2), table O-029 at 1000 K | 22.703 | kJ/mol | JANAF | 2026-10-02 |
| janafH:O2.1500 | enthalpy increment H(T)-H(298.15 K), Oxygen (O2), table O-029 at 1500 K | 40.599 | kJ/mol | JANAF | 2026-10-02 |
| janafH:O2.2000 | enthalpy increment H(T)-H(298.15 K), Oxygen (O2), table O-029 at 2000 K | 59.175 | kJ/mol | JANAF | 2026-10-02 |
| janafH:O2.2100 | enthalpy increment H(T)-H(298.15 K), Oxygen (O2), table O-029 at 2100 K | 62.961 | kJ/mol | JANAF | 2026-10-02 |
| janafH:O2.2200 | enthalpy increment H(T)-H(298.15 K), Oxygen (O2), table O-029 at 2200 K | 66.769 | kJ/mol | JANAF | 2026-10-02 |
| janafH:O2.2300 | enthalpy increment H(T)-H(298.15 K), Oxygen (O2), table O-029 at 2300 K | 70.6 | kJ/mol | JANAF | 2026-10-02 |
| janafH:O2.2400 | enthalpy increment H(T)-H(298.15 K), Oxygen (O2), table O-029 at 2400 K | 74.453 | kJ/mol | JANAF | 2026-10-02 |
| janafH:O2.2500 | enthalpy increment H(T)-H(298.15 K), Oxygen (O2), table O-029 at 2500 K | 78.328 | kJ/mol | JANAF | 2026-10-02 |
| janafH:O2.3000 | enthalpy increment H(T)-H(298.15 K), Oxygen (O2), table O-029 at 3000 K | 98.013 | kJ/mol | JANAF | 2026-10-02 |
| janafH:Ar.500 | enthalpy increment H(T)-H(298.15 K), Argon (Ar), table Ar-001 at 500 K | 4.196 | kJ/mol | JANAF | 2026-10-02 |
| janafH:Ar.1000 | enthalpy increment H(T)-H(298.15 K), Argon (Ar), table Ar-001 at 1000 K | 14.589 | kJ/mol | JANAF | 2026-10-02 |
| janafH:Ar.1500 | enthalpy increment H(T)-H(298.15 K), Argon (Ar), table Ar-001 at 1500 K | 24.982 | kJ/mol | JANAF | 2026-10-02 |
| janafH:Ar.2000 | enthalpy increment H(T)-H(298.15 K), Argon (Ar), table Ar-001 at 2000 K | 35.375 | kJ/mol | JANAF | 2026-10-02 |
| janafH:Ar.2100 | enthalpy increment H(T)-H(298.15 K), Argon (Ar), table Ar-001 at 2100 K | 37.453 | kJ/mol | JANAF | 2026-10-02 |
| janafH:Ar.2200 | enthalpy increment H(T)-H(298.15 K), Argon (Ar), table Ar-001 at 2200 K | 39.532 | kJ/mol | JANAF | 2026-10-02 |
| janafH:Ar.2300 | enthalpy increment H(T)-H(298.15 K), Argon (Ar), table Ar-001 at 2300 K | 41.61 | kJ/mol | JANAF | 2026-10-02 |
| janafH:Ar.2400 | enthalpy increment H(T)-H(298.15 K), Argon (Ar), table Ar-001 at 2400 K | 43.689 | kJ/mol | JANAF | 2026-10-02 |
| janafH:Ar.2500 | enthalpy increment H(T)-H(298.15 K), Argon (Ar), table Ar-001 at 2500 K | 45.768 | kJ/mol | JANAF | 2026-10-02 |
| janafH:Ar.3000 | enthalpy increment H(T)-H(298.15 K), Argon (Ar), table Ar-001 at 3000 K | 56.161 | kJ/mol | JANAF | 2026-10-02 |
| dfh:CH3Cl_g | standard enthalpy of formation, Chloromethane (CH3Cl), table C-063 at 298.15 K | -83.68 | kJ/mol | JANAF | 2026-10-02 |
| dfh:KCl_cr | standard enthalpy of formation, Potassium Chloride (KCl), table Cl-036 at 298.15 K | -436.684 | kJ/mol | JANAF | 2026-10-02 |
| dfh:K_g | standard enthalpy of formation of K(g) at 298.15 K (uncertainty 0.8) | 89.0 | kJ/mol | CODATA-KEY | 2026-10-02 |
| cp:NO_g.298 | standard molar heat capacity Cp, Nitrogen Oxide (NO), table N-005 at 298.15 K | 29.845 | J/(K.mol) | JANAF | 2026-10-02 |
| janafdfH:H2O_l.400 | standard enthalpy of formation, Water (H2O) liquid, table H-063 at 400 K | -282.591 | kJ/mol | JANAF | 2026-10-02 |
| janafdfH:H2O_g.400 | standard enthalpy of formation, Water (H2O) gas, table H-064 at 400 K | -242.846 | kJ/mol | JANAF | 2026-10-02 |
| dfh:CaCO3_cr | standard enthalpy of formation of CaCO3(cr, calcite) at 298.15 K (table page 2-272) | -1206.92 | kJ/mol | NBS-82 | 2026-10-02 |
| s0:CaCO3_cr | standard molar entropy of CaCO3(cr, calcite) at 298.15 K (table page 2-272) | 92.9 | J/(K.mol) | NBS-82 | 2026-10-02 |
| dfh:CaO_cr | standard enthalpy of formation of CaO(cr) at 298.15 K (table page 2-267) | -635.09 | kJ/mol | NBS-82 | 2026-10-02 |
| s0:CaO_cr | standard molar entropy of CaO(cr) at 298.15 K (table page 2-267) | 39.75 | J/(K.mol) | NBS-82 | 2026-10-02 |
| dfh:NH4NO3_cr | standard enthalpy of formation of NH4NO3(cr) at 298.15 K (table page 2-66) | -365.56 | kJ/mol | NBS-82 | 2026-10-02 |
| s0:NH4NO3_cr | standard molar entropy of NH4NO3(cr) at 298.15 K (table page 2-66) | 151.08 | J/(K.mol) | NBS-82 | 2026-10-02 |
| dfh:NH4NO3_ai | standard enthalpy of formation of NH4NO3 in water, ai (fully dissociated, standard state m = 1) at 298.15 K (table page 2-66) | -339.87 | kJ/mol | NBS-82 | 2026-10-02 |
| s0:NH4NO3_ai | standard molar entropy of NH4NO3 in water, ai, at 298.15 K (table page 2-66) | 259.8 | J/(K.mol) | NBS-82 | 2026-10-02 |
| dfh:N2O4_g | standard enthalpy of formation, Nitrogen Oxide (N2O4), table N-032 at 298.15 K | 9.079 | kJ/mol | JANAF | 2026-10-02 |
| s0:N2O4_g | standard molar entropy, Nitrogen Oxide (N2O4), table N-032 at 298.15 K | 304.376 | J/(K.mol) | JANAF | 2026-10-02 |
| dfh:NO2_g | standard enthalpy of formation, Nitrogen Oxide (NO2), table N-007 at 298.15 K | 33.095 | kJ/mol | JANAF | 2026-10-02 |
| s0:NO2_g | standard molar entropy, Nitrogen Oxide (NO2), table N-007 at 298.15 K | 240.034 | J/(K.mol) | JANAF | 2026-10-02 |
| s0:C2H4_g | standard molar entropy, Ethene (C2H4), table C-128 at 298.15 K | 219.33 | J/(K.mol) | JANAF | 2026-10-02 |
| s0T:Zn_crl.0 | standard molar entropy of zinc (cr below 692.73 K, l above), table Zn-004 at 0 K | 0.0 | J/(K.mol) | JANAF | 2026-10-02 |
| s0T:Zn_crl.100 | standard molar entropy of zinc (cr below 692.73 K, l above), table Zn-004 at 100 K | 16.523 | J/(K.mol) | JANAF | 2026-10-02 |
| s0T:Zn_crl.200 | standard molar entropy of zinc (cr below 692.73 K, l above), table Zn-004 at 200 K | 31.82 | J/(K.mol) | JANAF | 2026-10-02 |
| s0T:Zn_crl.250 | standard molar entropy of zinc (cr below 692.73 K, l above), table Zn-004 at 250 K | 37.29 | J/(K.mol) | JANAF | 2026-10-02 |
| s0T:Zn_crl.298.15 | standard molar entropy of zinc (cr below 692.73 K, l above), table Zn-004 at 298.15 K | 41.717 | J/(K.mol) | JANAF | 2026-10-02 |
| s0T:Zn_crl.400 | standard molar entropy of zinc (cr below 692.73 K, l above), table Zn-004 at 400 K | 49.314 | J/(K.mol) | JANAF | 2026-10-02 |
| s0T:Zn_crl.500 | standard molar entropy of zinc (cr below 692.73 K, l above), table Zn-004 at 500 K | 55.301 | J/(K.mol) | JANAF | 2026-10-02 |
| s0T:Zn_crl.600 | standard molar entropy of zinc (cr below 692.73 K, l above), table Zn-004 at 600 K | 60.399 | J/(K.mol) | JANAF | 2026-10-02 |
| s0T:Zn_crl.800 | standard molar entropy of zinc (cr below 692.73 K, l above), table Zn-004 at 800 K | 79.679 | J/(K.mol) | JANAF | 2026-10-02 |
| s0T:Zn_crl.1000 | standard molar entropy of zinc (cr below 692.73 K, l above), table Zn-004 at 1000 K | 86.681 | J/(K.mol) | JANAF | 2026-10-02 |
| s0T:Zn_cr.692 | standard molar entropy of solid zinc at the melting point 692.73 K, table Zn-004 | 64.591 | J/(K.mol) | JANAF | 2026-10-02 |
| s0T:Zn_l.692 | standard molar entropy of liquid zinc at the melting point 692.73 K, table Zn-004 | 75.161 | J/(K.mol) | JANAF | 2026-10-02 |
| hT:Zn_cr.692 | enthalpy increment H(692.73 K) - H(298.15 K) of solid zinc, table Zn-004 | 10.825 | kJ/mol | JANAF | 2026-10-02 |
| hT:Zn_l.692 | enthalpy increment H(692.73 K) - H(298.15 K) of liquid zinc, table Zn-004 | 18.147 | kJ/mol | JANAF | 2026-10-02 |
| s0T:Zn_l.1180 | standard molar entropy of liquid zinc at the boiling point 1180.173 K, table Zn-004 | 91.88 | J/(K.mol) | JANAF | 2026-10-02 |
| hT:Zn_l.1180 | enthalpy increment H(1180.173 K) - H(298.15 K) of liquid zinc, table Zn-004 | 33.443 | kJ/mol | JANAF | 2026-10-02 |
| s0T:Zn_g.1180 | standard molar entropy of gaseous zinc, table Zn-005 at 1180.17 K | 189.586 | J/(K.mol) | JANAF | 2026-10-02 |
| s0T:Zn_g.1300 | standard molar entropy of gaseous zinc, table Zn-005 at 1300 K | 191.597 | J/(K.mol) | JANAF | 2026-10-02 |
| s0T:Zn_g.1400 | standard molar entropy of gaseous zinc, table Zn-005 at 1400 K | 193.137 | J/(K.mol) | JANAF | 2026-10-02 |
| s0T:Zn_g.1500 | standard molar entropy of gaseous zinc, table Zn-005 at 1500 K | 194.571 | J/(K.mol) | JANAF | 2026-10-02 |
| hT:Zn_g.1180 | enthalpy increment H(1180.173 K) - H(298.15 K) of gaseous zinc, table Zn-005 | 18.334 | kJ/mol | JANAF | 2026-10-02 |
| dfh:Zn_g | standard enthalpy of formation of Zn(g), table Zn-005 at 298.15 K | 130.42 | kJ/mol | JANAF | 2026-10-02 |
| cpT:Zn_cr.300 | standard molar heat capacity of solid zinc, table Zn-004 at 300 K | 25.406 | J/(K.mol) | JANAF | 2026-10-02 |
| cpT:Zn_cr.400 | standard molar heat capacity of solid zinc, table Zn-004 at 400 K | 26.346 | J/(K.mol) | JANAF | 2026-10-02 |
| cpT:Zn_cr.500 | standard molar heat capacity of solid zinc, table Zn-004 at 500 K | 27.386 | J/(K.mol) | JANAF | 2026-10-02 |
| cpT:Zn_cr.600 | standard molar heat capacity of solid zinc, table Zn-004 at 600 K | 28.588 | J/(K.mol) | JANAF | 2026-10-02 |
| cp:CaCO3_cr.298 | standard molar heat capacity of CaCO3(cr, calcite) at 298.15 K (table page 2-272) | 81.88 | J/(K.mol) | NBS-82 | 2026-10-02 |
| cp:CaO_cr.298 | standard molar heat capacity of CaO(cr) at 298.15 K (table page 2-267) | 42.80 | J/(K.mol) | NBS-82 | 2026-10-02 |
| janafG:NH3.700 | standard Gibbs energy of formation, Ammonia (NH3), table H-083 at 700 K | 27.19 | kJ/mol | JANAF | 2026-10-02 |
| dfh:TiO2_cr | standard enthalpy of formation of TiO2(cr, rutile) at 298.15 K (uncertainty 0.8) | -944.0 | kJ/mol | CODATA-KEY | 2026-10-02 |
| s0:TiO2_cr | standard molar entropy of TiO2(cr, rutile) at 298.15 K (uncertainty 0.30) | 50.62 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| dfh:TiCl4_g | standard enthalpy of formation of TiCl4(g) at 298.15 K (uncertainty 3.0) | -763.2 | kJ/mol | CODATA-KEY | 2026-10-02 |
| s0:TiCl4_g | standard molar entropy of TiCl4(g) at 298.15 K (uncertainty 4.0) | 353.2 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| s0:HCl_g | standard molar entropy of HCl(g) at 298.15 K (uncertainty 0.005) | 186.902 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| rho:water.298 | density of liquid water at 298.15 K and 1.01325 bar (IAPWS-95) | 997.05 | kg/m3 | WEBBOOK-FLUID | 2026-10-02 |
| pvap:H2O.298 | vapour pressure of water at 298.15 K (IAPWS-95, saturation) | 3.170 | kPa | WEBBOOK-FLUID | 2026-10-02 |
| tb:H2O.atm | normal boiling point of water at 1.01325 bar (IAPWS-95) | 373.124 | K | WEBBOOK-FLUID | 2026-10-02 |
| dvap:H2O.nbp | enthalpy of vaporisation of water at its normal boiling point, 48.2004 - 7.54944 (IAPWS-95) | 40.651 | kJ/mol | WEBBOOK-FLUID | 2026-10-02 |
| dfus:H2O | specific enthalpy of melting of ice Ih at the triple point (minus the enthalpy of ice, liquid at the triple point as zero) | 333.444 | kJ/kg | IAPWS-ICE | 2026-10-02 |
| tfus:H2O | normal-pressure melting temperature of ice Ih (273.152519 K) | 273.15 | K | IAPWS-ICE | 2026-10-02 |
| henry:CO2 | Henry's law solubility constant of CO2 in water at 298.15 K, Hscp (Burkholder et al. 2019, evaluated) | 3.4e-4 | mol/(m3.Pa) | SANDER-2023 | 2026-10-02 |
| henry:O2 | Henry's law solubility constant of O2 in water at 298.15 K, Hscp (Burkholder et al. 2019, evaluated) | 1.3e-5 | mol/(m3.Pa) | SANDER-2023 | 2026-10-02 |
| henry:N2 | Henry's law solubility constant of N2 in water at 298.15 K, Hscp (Burkholder et al. 2019, evaluated) | 6.4e-6 | mol/(m3.Pa) | SANDER-2023 | 2026-10-02 |
| henryT:CO2 | temperature dependence d ln Hscp / d(1/T) for CO2 in water (Burkholder et al. 2019) | 2300 | K | SANDER-2023 | 2026-10-02 |
| tb:glycol | normal boiling point of ethane-1,2-diol (WebBook average of determinations, uncertainty 0.5) | 470.5 | K | WEBBOOK-PHASE | 2026-10-02 |
| janafG:NH3.298.15 | standard Gibbs energy of formation, Ammonia (NH3), table H-083 at 298.15 K | -16.367 | kJ/mol | JANAF | 2026-10-02 |
| janafG:NH3.400 | standard Gibbs energy of formation, Ammonia (NH3), table H-083 at 400 K | -5.941 | kJ/mol | JANAF | 2026-10-02 |
| janafG:NH3.500 | standard Gibbs energy of formation, Ammonia (NH3), table H-083 at 500 K | 4.8 | kJ/mol | JANAF | 2026-10-02 |
| janafG:NH3.600 | standard Gibbs energy of formation, Ammonia (NH3), table H-083 at 600 K | 15.879 | kJ/mol | JANAF | 2026-10-02 |
| janafG:NH3.800 | standard Gibbs energy of formation, Ammonia (NH3), table H-083 at 800 K | 38.662 | kJ/mol | JANAF | 2026-10-02 |
| janafG:NH3.900 | standard Gibbs energy of formation, Ammonia (NH3), table H-083 at 900 K | 50.247 | kJ/mol | JANAF | 2026-10-02 |
| janafG:NH3.1000 | standard Gibbs energy of formation, Ammonia (NH3), table H-083 at 1000 K | 61.91 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SO2.298.15 | standard Gibbs energy of formation, Sulfur Dioxide (SO2), table O-034 at 298.15 K | -300.125 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SO2.400 | standard Gibbs energy of formation, Sulfur Dioxide (SO2), table O-034 at 400 K | -300.971 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SO2.500 | standard Gibbs energy of formation, Sulfur Dioxide (SO2), table O-034 at 500 K | -300.871 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SO2.600 | standard Gibbs energy of formation, Sulfur Dioxide (SO2), table O-034 at 600 K | -300.305 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SO2.700 | standard Gibbs energy of formation, Sulfur Dioxide (SO2), table O-034 at 700 K | -299.444 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SO2.800 | standard Gibbs energy of formation, Sulfur Dioxide (SO2), table O-034 at 800 K | -298.37 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SO2.900 | standard Gibbs energy of formation, Sulfur Dioxide (SO2), table O-034 at 900 K | -296.051 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SO2.1000 | standard Gibbs energy of formation, Sulfur Dioxide (SO2), table O-034 at 1000 K | -288.725 | kJ/mol | JANAF | 2026-10-02 |
| dfh:SO2_g | standard enthalpy of formation, Sulfur Dioxide (SO2), table O-034 at 298.15 K | -296.842 | kJ/mol | JANAF | 2026-10-02 |
| s0:SO2_g | standard molar entropy, Sulfur Dioxide (SO2), table O-034 at 298.15 K | 248.212 | J/(K.mol) | JANAF | 2026-10-02 |
| janafG:SO3.298.15 | standard Gibbs energy of formation, Sulfur Trioxide (SO3), table O-058 at 298.15 K | -371.016 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SO3.400 | standard Gibbs energy of formation, Sulfur Trioxide (SO3), table O-058 at 400 K | -362.242 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SO3.500 | standard Gibbs energy of formation, Sulfur Trioxide (SO3), table O-058 at 500 K | -352.668 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SO3.600 | standard Gibbs energy of formation, Sulfur Trioxide (SO3), table O-058 at 600 K | -342.647 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SO3.700 | standard Gibbs energy of formation, Sulfur Trioxide (SO3), table O-058 at 700 K | -332.365 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SO3.800 | standard Gibbs energy of formation, Sulfur Trioxide (SO3), table O-058 at 800 K | -321.912 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SO3.900 | standard Gibbs energy of formation, Sulfur Trioxide (SO3), table O-058 at 900 K | -310.258 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SO3.1000 | standard Gibbs energy of formation, Sulfur Trioxide (SO3), table O-058 at 1000 K | -293.639 | kJ/mol | JANAF | 2026-10-02 |
| dfh:SO3_g | standard enthalpy of formation, Sulfur Trioxide (SO3), table O-058 at 298.15 K | -395.765 | kJ/mol | JANAF | 2026-10-02 |
| s0:SO3_g | standard molar entropy, Sulfur Trioxide (SO3), table O-058 at 298.15 K | 256.769 | J/(K.mol) | JANAF | 2026-10-02 |
| janafG:Cu2O.300 | standard Gibbs energy of formation, Copper Oxide (Cu2O) (Cu2O1(cr,l)), table Cu-021 at 300 K | -147.745 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cu2O.500 | standard Gibbs energy of formation, Copper Oxide (Cu2O) (Cu2O1(cr,l)), table Cu-021 at 500 K | -132.484 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cu2O.700 | standard Gibbs energy of formation, Copper Oxide (Cu2O) (Cu2O1(cr,l)), table Cu-021 at 700 K | -117.478 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cu2O.900 | standard Gibbs energy of formation, Copper Oxide (Cu2O) (Cu2O1(cr,l)), table Cu-021 at 900 K | -102.767 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cu2O.1100 | standard Gibbs energy of formation, Copper Oxide (Cu2O) (Cu2O1(cr,l)), table Cu-021 at 1100 K | -88.331 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cu2O.1300 | standard Gibbs energy of formation, Copper Oxide (Cu2O) (Cu2O1(cr,l)), table Cu-021 at 1300 K | -74.144 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cu2O.1500 | standard Gibbs energy of formation, Copper Oxide (Cu2O) (Cu2O1(cr,l)), table Cu-021 at 1500 K | -57.438 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cu2O.1700 | standard Gibbs energy of formation, Copper Oxide (Cu2O) (Cu2O1(cr,l)), table Cu-021 at 1700 K | -47.768 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cu2O.1900 | standard Gibbs energy of formation, Copper Oxide (Cu2O) (Cu2O1(cr,l)), table Cu-021 at 1900 K | -39.181 | kJ/mol | JANAF | 2026-10-02 |
| janafG:FeO.300 | standard Gibbs energy of formation, Iron Oxide (FeO) (Fe1O1(cr,l)), table Fe-020 at 300 K | -251.301 | kJ/mol | JANAF | 2026-10-02 |
| janafG:FeO.500 | standard Gibbs energy of formation, Iron Oxide (FeO) (Fe1O1(cr,l)), table Fe-020 at 500 K | -238.022 | kJ/mol | JANAF | 2026-10-02 |
| janafG:FeO.700 | standard Gibbs energy of formation, Iron Oxide (FeO) (Fe1O1(cr,l)), table Fe-020 at 700 K | -225.425 | kJ/mol | JANAF | 2026-10-02 |
| janafG:FeO.900 | standard Gibbs energy of formation, Iron Oxide (FeO) (Fe1O1(cr,l)), table Fe-020 at 900 K | -213.118 | kJ/mol | JANAF | 2026-10-02 |
| janafG:FeO.1100 | standard Gibbs energy of formation, Iron Oxide (FeO) (Fe1O1(cr,l)), table Fe-020 at 1100 K | -200.67 | kJ/mol | JANAF | 2026-10-02 |
| janafG:FeO.1300 | standard Gibbs energy of formation, Iron Oxide (FeO) (Fe1O1(cr,l)), table Fe-020 at 1300 K | -187.947 | kJ/mol | JANAF | 2026-10-02 |
| janafG:FeO.1500 | standard Gibbs energy of formation, Iron Oxide (FeO) (Fe1O1(cr,l)), table Fe-020 at 1500 K | -175.415 | kJ/mol | JANAF | 2026-10-02 |
| janafG:FeO.1700 | standard Gibbs energy of formation, Iron Oxide (FeO) (Fe1O1(cr,l)), table Fe-020 at 1700 K | -163.826 | kJ/mol | JANAF | 2026-10-02 |
| janafG:FeO.1900 | standard Gibbs energy of formation, Iron Oxide (FeO) (Fe1O1(cr,l)), table Fe-020 at 1900 K | -153.831 | kJ/mol | JANAF | 2026-10-02 |
| janafG:FeO.2100 | standard Gibbs energy of formation, Iron Oxide (FeO) (Fe1O1(cr,l)), table Fe-020 at 2100 K | -143.089 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SiO2.300 | standard Gibbs energy of formation, Silicon Oxide (SiO2) (O2Si1(cr,l)), table O-039 at 300 K | -856.106 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SiO2.500 | standard Gibbs energy of formation, Silicon Oxide (SiO2) (O2Si1(cr,l)), table O-039 at 500 K | -819.539 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SiO2.700 | standard Gibbs energy of formation, Silicon Oxide (SiO2) (O2Si1(cr,l)), table O-039 at 700 K | -783.331 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SiO2.900 | standard Gibbs energy of formation, Silicon Oxide (SiO2) (O2Si1(cr,l)), table O-039 at 900 K | -747.785 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SiO2.1100 | standard Gibbs energy of formation, Silicon Oxide (SiO2) (O2Si1(cr,l)), table O-039 at 1100 K | -712.805 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SiO2.1300 | standard Gibbs energy of formation, Silicon Oxide (SiO2) (O2Si1(cr,l)), table O-039 at 1300 K | -678.114 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SiO2.1500 | standard Gibbs energy of formation, Silicon Oxide (SiO2) (O2Si1(cr,l)), table O-039 at 1500 K | -643.681 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SiO2.1700 | standard Gibbs energy of formation, Silicon Oxide (SiO2) (O2Si1(cr,l)), table O-039 at 1700 K | -609.059 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SiO2.1900 | standard Gibbs energy of formation, Silicon Oxide (SiO2) (O2Si1(cr,l)), table O-039 at 1900 K | -570.178 | kJ/mol | JANAF | 2026-10-02 |
| janafG:SiO2.2100 | standard Gibbs energy of formation, Silicon Oxide (SiO2) (O2Si1(cr,l)), table O-039 at 2100 K | -531.741 | kJ/mol | JANAF | 2026-10-02 |
| janafG:TiO2.500 | standard Gibbs energy of formation, Titanium Oxide (TiO2) (O2Ti1(cr,l)), table O-045 at 500 K | -852.157 | kJ/mol | JANAF | 2026-10-02 |
| janafG:TiO2.700 | standard Gibbs energy of formation, Titanium Oxide (TiO2) (O2Ti1(cr,l)), table O-045 at 700 K | -815.868 | kJ/mol | JANAF | 2026-10-02 |
| janafG:TiO2.900 | standard Gibbs energy of formation, Titanium Oxide (TiO2) (O2Ti1(cr,l)), table O-045 at 900 K | -780.132 | kJ/mol | JANAF | 2026-10-02 |
| janafG:TiO2.1100 | standard Gibbs energy of formation, Titanium Oxide (TiO2) (O2Ti1(cr,l)), table O-045 at 1100 K | -744.803 | kJ/mol | JANAF | 2026-10-02 |
| janafG:TiO2.1300 | standard Gibbs energy of formation, Titanium Oxide (TiO2) (O2Ti1(cr,l)), table O-045 at 1300 K | -709.265 | kJ/mol | JANAF | 2026-10-02 |
| janafG:TiO2.1500 | standard Gibbs energy of formation, Titanium Oxide (TiO2) (O2Ti1(cr,l)), table O-045 at 1500 K | -673.798 | kJ/mol | JANAF | 2026-10-02 |
| janafG:TiO2.1700 | standard Gibbs energy of formation, Titanium Oxide (TiO2) (O2Ti1(cr,l)), table O-045 at 1700 K | -638.566 | kJ/mol | JANAF | 2026-10-02 |
| janafG:TiO2.1900 | standard Gibbs energy of formation, Titanium Oxide (TiO2) (O2Ti1(cr,l)), table O-045 at 1900 K | -603.489 | kJ/mol | JANAF | 2026-10-02 |
| janafG:TiO2.2100 | standard Gibbs energy of formation, Titanium Oxide (TiO2) (O2Ti1(cr,l)), table O-045 at 2100 K | -567.263 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Al2O3.300 | standard Gibbs energy of formation, Aluminum Oxide (Al2O3) (Al2O3(cr,l)), table Al-101 at 300 K | -1581.696 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Al2O3.500 | standard Gibbs energy of formation, Aluminum Oxide (Al2O3) (Al2O3(cr,l)), table Al-101 at 500 K | -1518.718 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Al2O3.700 | standard Gibbs energy of formation, Aluminum Oxide (Al2O3) (Al2O3(cr,l)), table Al-101 at 700 K | -1456.059 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Al2O3.900 | standard Gibbs energy of formation, Aluminum Oxide (Al2O3) (Al2O3(cr,l)), table Al-101 at 900 K | -1393.908 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Al2O3.1100 | standard Gibbs energy of formation, Aluminum Oxide (Al2O3) (Al2O3(cr,l)), table Al-101 at 1100 K | -1328.286 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Al2O3.1300 | standard Gibbs energy of formation, Aluminum Oxide (Al2O3) (Al2O3(cr,l)), table Al-101 at 1300 K | -1262.264 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Al2O3.1500 | standard Gibbs energy of formation, Aluminum Oxide (Al2O3) (Al2O3(cr,l)), table Al-101 at 1500 K | -1196.617 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Al2O3.1700 | standard Gibbs energy of formation, Aluminum Oxide (Al2O3) (Al2O3(cr,l)), table Al-101 at 1700 K | -1131.342 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Al2O3.1900 | standard Gibbs energy of formation, Aluminum Oxide (Al2O3) (Al2O3(cr,l)), table Al-101 at 1900 K | -1066.426 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Al2O3.2100 | standard Gibbs energy of formation, Aluminum Oxide (Al2O3) (Al2O3(cr,l)), table Al-101 at 2100 K | -1001.849 | kJ/mol | JANAF | 2026-10-02 |
| janafG:MgO.300 | standard Gibbs energy of formation, Magnesium Oxide (MgO) (Mg1O1(cr,l)), table Mg-010 at 300 K | -568.745 | kJ/mol | JANAF | 2026-10-02 |
| janafG:MgO.500 | standard Gibbs energy of formation, Magnesium Oxide (MgO) (Mg1O1(cr,l)), table Mg-010 at 500 K | -547.078 | kJ/mol | JANAF | 2026-10-02 |
| janafG:MgO.700 | standard Gibbs energy of formation, Magnesium Oxide (MgO) (Mg1O1(cr,l)), table Mg-010 at 700 K | -525.6 | kJ/mol | JANAF | 2026-10-02 |
| janafG:MgO.900 | standard Gibbs energy of formation, Magnesium Oxide (MgO) (Mg1O1(cr,l)), table Mg-010 at 900 K | -504.289 | kJ/mol | JANAF | 2026-10-02 |
| janafG:MgO.1100 | standard Gibbs energy of formation, Magnesium Oxide (MgO) (Mg1O1(cr,l)), table Mg-010 at 1100 K | -481.399 | kJ/mol | JANAF | 2026-10-02 |
| janafG:MgO.1300 | standard Gibbs energy of formation, Magnesium Oxide (MgO) (Mg1O1(cr,l)), table Mg-010 at 1300 K | -458.291 | kJ/mol | JANAF | 2026-10-02 |
| janafG:MgO.1500 | standard Gibbs energy of formation, Magnesium Oxide (MgO) (Mg1O1(cr,l)), table Mg-010 at 1500 K | -422.752 | kJ/mol | JANAF | 2026-10-02 |
| janafG:MgO.1700 | standard Gibbs energy of formation, Magnesium Oxide (MgO) (Mg1O1(cr,l)), table Mg-010 at 1700 K | -381.394 | kJ/mol | JANAF | 2026-10-02 |
| janafG:MgO.1900 | standard Gibbs energy of formation, Magnesium Oxide (MgO) (Mg1O1(cr,l)), table Mg-010 at 1900 K | -340.395 | kJ/mol | JANAF | 2026-10-02 |
| janafG:MgO.2100 | standard Gibbs energy of formation, Magnesium Oxide (MgO) (Mg1O1(cr,l)), table Mg-010 at 2100 K | -299.727 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CaO.300 | standard Gibbs energy of formation, Calcium Oxide (CaO) (Ca1O1(cr,l)), table Ca-029 at 300 K | -603.305 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CaO.500 | standard Gibbs energy of formation, Calcium Oxide (CaO) (Ca1O1(cr,l)), table Ca-029 at 500 K | -582.316 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CaO.700 | standard Gibbs energy of formation, Calcium Oxide (CaO) (Ca1O1(cr,l)), table Ca-029 at 700 K | -561.701 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CaO.900 | standard Gibbs energy of formation, Calcium Oxide (CaO) (Ca1O1(cr,l)), table Ca-029 at 900 K | -541.024 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CaO.1100 | standard Gibbs energy of formation, Calcium Oxide (CaO) (Ca1O1(cr,l)), table Ca-029 at 1100 K | -520.297 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CaO.1300 | standard Gibbs energy of formation, Calcium Oxide (CaO) (Ca1O1(cr,l)), table Ca-029 at 1300 K | -498.082 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CaO.1500 | standard Gibbs energy of formation, Calcium Oxide (CaO) (Ca1O1(cr,l)), table Ca-029 at 1500 K | -475.823 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CaO.1700 | standard Gibbs energy of formation, Calcium Oxide (CaO) (Ca1O1(cr,l)), table Ca-029 at 1700 K | -453.644 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CaO.1900 | standard Gibbs energy of formation, Calcium Oxide (CaO) (Ca1O1(cr,l)), table Ca-029 at 1900 K | -420.996 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CaO.2100 | standard Gibbs energy of formation, Calcium Oxide (CaO) (Ca1O1(cr,l)), table Ca-029 at 2100 K | -382.523 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cr2O3.300 | standard Gibbs energy of formation, Chromium Oxide (Cr2O3) (Cr2O3(cr,l)), table Cr-016 at 300 K | -1052.56 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cr2O3.500 | standard Gibbs energy of formation, Chromium Oxide (Cr2O3) (Cr2O3(cr,l)), table Cr-016 at 500 K | -998.699 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cr2O3.700 | standard Gibbs energy of formation, Chromium Oxide (Cr2O3) (Cr2O3(cr,l)), table Cr-016 at 700 K | -946.252 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cr2O3.900 | standard Gibbs energy of formation, Chromium Oxide (Cr2O3) (Cr2O3(cr,l)), table Cr-016 at 900 K | -894.736 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cr2O3.1100 | standard Gibbs energy of formation, Chromium Oxide (Cr2O3) (Cr2O3(cr,l)), table Cr-016 at 1100 K | -843.808 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cr2O3.1300 | standard Gibbs energy of formation, Chromium Oxide (Cr2O3) (Cr2O3(cr,l)), table Cr-016 at 1300 K | -793.188 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cr2O3.1500 | standard Gibbs energy of formation, Chromium Oxide (Cr2O3) (Cr2O3(cr,l)), table Cr-016 at 1500 K | -742.639 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cr2O3.1700 | standard Gibbs energy of formation, Chromium Oxide (Cr2O3) (Cr2O3(cr,l)), table Cr-016 at 1700 K | -691.967 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cr2O3.1900 | standard Gibbs energy of formation, Chromium Oxide (Cr2O3) (Cr2O3(cr,l)), table Cr-016 at 1900 K | -641.013 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Cr2O3.2100 | standard Gibbs energy of formation, Chromium Oxide (Cr2O3) (Cr2O3(cr,l)), table Cr-016 at 2100 K | -589.654 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO.300 | standard Gibbs energy of formation, Carbon Monoxide (CO) (C1O1(g)), table C-093 at 300 K | -137.328 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO.500 | standard Gibbs energy of formation, Carbon Monoxide (CO) (C1O1(g)), table C-093 at 500 K | -155.414 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO.700 | standard Gibbs energy of formation, Carbon Monoxide (CO) (C1O1(g)), table C-093 at 700 K | -173.518 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO.900 | standard Gibbs energy of formation, Carbon Monoxide (CO) (C1O1(g)), table C-093 at 900 K | -191.416 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO.1100 | standard Gibbs energy of formation, Carbon Monoxide (CO) (C1O1(g)), table C-093 at 1100 K | -209.075 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO.1300 | standard Gibbs energy of formation, Carbon Monoxide (CO) (C1O1(g)), table C-093 at 1300 K | -226.509 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO.1500 | standard Gibbs energy of formation, Carbon Monoxide (CO) (C1O1(g)), table C-093 at 1500 K | -243.74 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO.1700 | standard Gibbs energy of formation, Carbon Monoxide (CO) (C1O1(g)), table C-093 at 1700 K | -260.784 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO.1900 | standard Gibbs energy of formation, Carbon Monoxide (CO) (C1O1(g)), table C-093 at 1900 K | -277.658 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO.2100 | standard Gibbs energy of formation, Carbon Monoxide (CO) (C1O1(g)), table C-093 at 2100 K | -294.372 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO2.300 | standard Gibbs energy of formation, Carbon Dioxide (CO2) (C1O2(g)), table C-095 at 300 K | -394.394 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO2.500 | standard Gibbs energy of formation, Carbon Dioxide (CO2) (C1O2(g)), table C-095 at 500 K | -394.939 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO2.700 | standard Gibbs energy of formation, Carbon Dioxide (CO2) (C1O2(g)), table C-095 at 700 K | -395.398 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO2.900 | standard Gibbs energy of formation, Carbon Dioxide (CO2) (C1O2(g)), table C-095 at 900 K | -395.748 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO2.1100 | standard Gibbs energy of formation, Carbon Dioxide (CO2) (C1O2(g)), table C-095 at 1100 K | -396.001 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO2.1300 | standard Gibbs energy of formation, Carbon Dioxide (CO2) (C1O2(g)), table C-095 at 1300 K | -396.177 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO2.1500 | standard Gibbs energy of formation, Carbon Dioxide (CO2) (C1O2(g)), table C-095 at 1500 K | -396.288 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO2.1700 | standard Gibbs energy of formation, Carbon Dioxide (CO2) (C1O2(g)), table C-095 at 1700 K | -396.344 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO2.1900 | standard Gibbs energy of formation, Carbon Dioxide (CO2) (C1O2(g)), table C-095 at 1900 K | -396.349 | kJ/mol | JANAF | 2026-10-02 |
| janafG:CO2.2100 | standard Gibbs energy of formation, Carbon Dioxide (CO2) (C1O2(g)), table C-095 at 2100 K | -396.304 | kJ/mol | JANAF | 2026-10-02 |
| janafG:H2O.300 | standard Gibbs energy of formation, Water (H2O) (H2O1(g)), table H-064 at 300 K | -228.5 | kJ/mol | JANAF | 2026-10-02 |
| janafG:H2O.500 | standard Gibbs energy of formation, Water (H2O) (H2O1(g)), table H-064 at 500 K | -219.051 | kJ/mol | JANAF | 2026-10-02 |
| janafG:H2O.700 | standard Gibbs energy of formation, Water (H2O) (H2O1(g)), table H-064 at 700 K | -208.812 | kJ/mol | JANAF | 2026-10-02 |
| janafG:H2O.900 | standard Gibbs energy of formation, Water (H2O) (H2O1(g)), table H-064 at 900 K | -198.083 | kJ/mol | JANAF | 2026-10-02 |
| janafG:H2O.1100 | standard Gibbs energy of formation, Water (H2O) (H2O1(g)), table H-064 at 1100 K | -187.033 | kJ/mol | JANAF | 2026-10-02 |
| janafG:H2O.1300 | standard Gibbs energy of formation, Water (H2O) (H2O1(g)), table H-064 at 1300 K | -175.774 | kJ/mol | JANAF | 2026-10-02 |
| janafG:H2O.1500 | standard Gibbs energy of formation, Water (H2O) (H2O1(g)), table H-064 at 1500 K | -164.376 | kJ/mol | JANAF | 2026-10-02 |
| janafG:H2O.1700 | standard Gibbs energy of formation, Water (H2O) (H2O1(g)), table H-064 at 1700 K | -152.883 | kJ/mol | JANAF | 2026-10-02 |
| janafG:H2O.1900 | standard Gibbs energy of formation, Water (H2O) (H2O1(g)), table H-064 at 1900 K | -141.325 | kJ/mol | JANAF | 2026-10-02 |
| janafG:H2O.2100 | standard Gibbs energy of formation, Water (H2O) (H2O1(g)), table H-064 at 2100 K | -129.721 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe3O4.300 | standard Gibbs energy of formation, Iron Oxide, Magnetite (Fe3O4) (Fe3O4(cr)), table Fe-032 at 300 K | -1016.797 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe3O4.500 | standard Gibbs energy of formation, Iron Oxide, Magnetite (Fe3O4) (Fe3O4(cr)), table Fe-032 at 500 K | -948.681 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe3O4.700 | standard Gibbs energy of formation, Iron Oxide, Magnetite (Fe3O4) (Fe3O4(cr)), table Fe-032 at 700 K | -883.776 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe3O4.900 | standard Gibbs energy of formation, Iron Oxide, Magnetite (Fe3O4) (Fe3O4(cr)), table Fe-032 at 900 K | -822.428 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe3O4.1100 | standard Gibbs energy of formation, Iron Oxide, Magnetite (Fe3O4) (Fe3O4(cr)), table Fe-032 at 1100 K | -762.463 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe3O4.1300 | standard Gibbs energy of formation, Iron Oxide, Magnetite (Fe3O4) (Fe3O4(cr)), table Fe-032 at 1300 K | -701.771 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe3O4.1500 | standard Gibbs energy of formation, Iron Oxide, Magnetite (Fe3O4) (Fe3O4(cr)), table Fe-032 at 1500 K | -641.562 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe3O4.1700 | standard Gibbs energy of formation, Iron Oxide, Magnetite (Fe3O4) (Fe3O4(cr)), table Fe-032 at 1700 K | -581.785 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe3O4.1900 | standard Gibbs energy of formation, Iron Oxide, Magnetite (Fe3O4) (Fe3O4(cr)), table Fe-032 at 1900 K | -519.794 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe3O4.2100 | standard Gibbs energy of formation, Iron Oxide, Magnetite (Fe3O4) (Fe3O4(cr)), table Fe-032 at 2100 K | -455.087 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe2O3.300 | standard Gibbs energy of formation, Iron Oxide, Hematite (Fe2O3) (Fe2O3(cr)), table Fe-030 at 300 K | -743.014 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe2O3.500 | standard Gibbs energy of formation, Iron Oxide, Hematite (Fe2O3) (Fe2O3(cr)), table Fe-030 at 500 K | -688.929 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe2O3.700 | standard Gibbs energy of formation, Iron Oxide, Hematite (Fe2O3) (Fe2O3(cr)), table Fe-030 at 700 K | -636.837 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe2O3.900 | standard Gibbs energy of formation, Iron Oxide, Hematite (Fe2O3) (Fe2O3(cr)), table Fe-030 at 900 K | -586.51 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe2O3.1100 | standard Gibbs energy of formation, Iron Oxide, Hematite (Fe2O3) (Fe2O3(cr)), table Fe-030 at 1100 K | -537.171 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe2O3.1300 | standard Gibbs energy of formation, Iron Oxide, Hematite (Fe2O3) (Fe2O3(cr)), table Fe-030 at 1300 K | -487.562 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe2O3.1500 | standard Gibbs energy of formation, Iron Oxide, Hematite (Fe2O3) (Fe2O3(cr)), table Fe-030 at 1500 K | -438.347 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe2O3.1700 | standard Gibbs energy of formation, Iron Oxide, Hematite (Fe2O3) (Fe2O3(cr)), table Fe-030 at 1700 K | -389.52 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe2O3.1900 | standard Gibbs energy of formation, Iron Oxide, Hematite (Fe2O3) (Fe2O3(cr)), table Fe-030 at 1900 K | -339.338 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Fe2O3.2100 | standard Gibbs energy of formation, Iron Oxide, Hematite (Fe2O3) (Fe2O3(cr)), table Fe-030 at 2100 K | -287.474 | kJ/mol | JANAF | 2026-10-02 |
| dfh:ZnO_cr | standard enthalpy of formation of ZnO(cr) at 298.15 K (uncertainty 0.27) | -350.46 | kJ/mol | CODATA-KEY | 2026-10-02 |
| s0:ZnO_cr | standard molar entropy of ZnO(cr) at 298.15 K (uncertainty 0.40) | 43.65 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| s0:Zn_cr | standard molar entropy of Zn(cr) at 298.15 K (uncertainty 0.15) | 41.63 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| dfh:HgO_cr | standard enthalpy of formation of HgO(cr, red) at 298.15 K (uncertainty 0.12) | -90.79 | kJ/mol | CODATA-KEY | 2026-10-02 |
| s0:HgO_cr | standard molar entropy of HgO(cr, red) at 298.15 K (uncertainty 0.30) | 70.25 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| s0:Hg_l | standard molar entropy of Hg(l) at 298.15 K (uncertainty 0.12) | 75.90 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| dfh:Hg_g | standard enthalpy of formation of Hg(g) at 298.15 K (uncertainty 0.04) | 61.38 | kJ/mol | CODATA-KEY | 2026-10-02 |
| s0:Hg_g | standard molar entropy of Hg(g) at 298.15 K (uncertainty 0.005) | 174.971 | J/(K.mol) | CODATA-KEY | 2026-10-02 |
| janafG:Fe2O3.298 | standard Gibbs energy of formation of Fe2O3(cr) (hematite), table Fe-030 at 298.15 K | -743.523 | kJ/mol | JANAF | 2026-10-02 |
| janafG:Al2O3.298 | standard Gibbs energy of formation of Al2O3(cr), table Al-101 at 298.15 K | -1582.275 | kJ/mol | JANAF | 2026-10-02 |
| antoine:benzene.A | Antoine A of benzene (C6H6), log10(p/bar) = A - B/(T + C), T in K, valid 287.70-354.07 K, Williamham, Taylor et al. 1945 | 4.01814 | 1 | WEBBOOK-PHASE | 2026-10-02 |
| antoine:benzene.B | Antoine B of benzene (C6H6), log10(p/bar) = A - B/(T + C), T in K, valid 287.70-354.07 K, Williamham, Taylor et al. 1945 | 1203.835 | K | WEBBOOK-PHASE | 2026-10-02 |
| antoine:benzene.C | Antoine C of benzene (C6H6), log10(p/bar) = A - B/(T + C), T in K, valid 287.70-354.07 K, Williamham, Taylor et al. 1945 | -53.226 | K | WEBBOOK-PHASE | 2026-10-02 |
| antoine:toluene.A | Antoine A of toluene (C7H8), log10(p/bar) = A - B/(T + C), T in K, valid 308.52-384.66 K, Williamham, Taylor et al. 1945 | 4.07827 | 1 | WEBBOOK-PHASE | 2026-10-02 |
| antoine:toluene.B | Antoine B of toluene (C7H8), log10(p/bar) = A - B/(T + C), T in K, valid 308.52-384.66 K, Williamham, Taylor et al. 1945 | 1343.943 | K | WEBBOOK-PHASE | 2026-10-02 |
| antoine:toluene.C | Antoine C of toluene (C7H8), log10(p/bar) = A - B/(T + C), T in K, valid 308.52-384.66 K, Williamham, Taylor et al. 1945 | -53.773 | K | WEBBOOK-PHASE | 2026-10-02 |
| antoine:water.A | Antoine A of water (H2O), log10(p/bar) = A - B/(T + C), T in K, valid 344-373 K, Bridgeman and Aldrich 1964 | 5.08354 | 1 | WEBBOOK-PHASE | 2026-10-02 |
| antoine:water.B | Antoine B of water (H2O), log10(p/bar) = A - B/(T + C), T in K, valid 344-373 K, Bridgeman and Aldrich 1964 | 1663.125 | K | WEBBOOK-PHASE | 2026-10-02 |
| antoine:water.C | Antoine C of water (H2O), log10(p/bar) = A - B/(T + C), T in K, valid 344-373 K, Bridgeman and Aldrich 1964 | -45.622 | K | WEBBOOK-PHASE | 2026-10-02 |
| antoine:ethanol.A | Antoine A of ethanol (C2H5OH), log10(p/bar) = A - B/(T + C), T in K, valid 292.77-366.63 K, Ambrose and Sprake 1970 | 5.24677 | 1 | WEBBOOK-PHASE | 2026-10-02 |
| antoine:ethanol.B | Antoine B of ethanol (C2H5OH), log10(p/bar) = A - B/(T + C), T in K, valid 292.77-366.63 K, Ambrose and Sprake 1970 | 1598.673 | K | WEBBOOK-PHASE | 2026-10-02 |
| antoine:ethanol.C | Antoine C of ethanol (C2H5OH), log10(p/bar) = A - B/(T + C), T in K, valid 292.77-366.63 K, Ambrose and Sprake 1970 | -46.424 | K | WEBBOOK-PHASE | 2026-10-02 |
| tb:benzene | normal boiling point of benzene (WebBook AVG, ± 0.1 K) | 353.3 | K | WEBBOOK-PHASE | 2026-10-02 |
| tb:toluene | normal boiling point of toluene (WebBook AVG, ± 0.2 K) | 383.8 | K | WEBBOOK-PHASE | 2026-10-02 |
| azeo:ethanol-water.w | mass fraction of ethanol in the ethanol-water azeotrope at atmospheric pressure (HSDB via PubChem CID 702, Other Experimental Properties: 'water azeotrope is 95% by weight ethanol') | 95 | % | PUBCHEM | 2026-10-02 |
| tfus:Cu | melting point of copper, table Cu-004 (cr,l) | 1358 | K | JANAF | 2026-10-03 |
| dfus:Cu | enthalpy of fusion of copper, H(l) - H(cr) at 1358 K, table Cu-004 | 13.138 | kJ/mol | JANAF | 2026-10-03 |
| tfus:Ni | melting point of nickel, table Ni-004 (cr,l) | 1728 | K | JANAF | 2026-10-03 |
| dfus:Ni | enthalpy of fusion of nickel, H(l) - H(cr) at 1728 K, table Ni-004 | 17.155 | kJ/mol | JANAF | 2026-10-03 |
| tfus:Pb | melting point of lead, table Pb-004 (cr,l) | 600.6 | K | JANAF | 2026-10-03 |
| dfus:Pb | enthalpy of fusion of lead, H(l) - H(cr) at 600.6 K, table Pb-004 | 4.774 | kJ/mol | JANAF | 2026-10-03 |
| tfus:Sn | melting point of tin (breakpoint of the SGTE liquid expression) | 505.08 | K | NIST-SOLDER-TDB | 2026-10-03 |
| dfus:Sn | enthalpy of fusion of tin at 505.08 K, from G(LIQUID,SN;0) = 7103.092 - 14.087767 T + 1.47031E-18 T^7 + GHSERSN | 7.03 | kJ/mol | NIST-SOLDER-TDB | 2026-10-03 |
| tfus:Bi | melting point of bismuth (breakpoint of the SGTE liquid expression) | 544.55 | K | NIST-SOLDER-TDB | 2026-10-03 |
| dfus:Bi | enthalpy of fusion of bismuth at 544.55 K, from G(LIQUID,BI;0) = 11246.067 - 20.63651 T - 5.955E-19 T^7 + GHSERBI | 11.30 | kJ/mol | NIST-SOLDER-TDB | 2026-10-03 |
| tfus:benzene | melting point of benzene (WebBook AVG, uncertainty 0.08 K) | 278.64 | K | WEBBOOK-PHASE | 2026-10-03 |
| dfus:benzene | enthalpy of fusion of benzene (Domalski and Hearing 1996 compilation, 278.7 K; other determinations 9.80-9.94) | 9.87 | kJ/mol | WEBBOOK-PHASE | 2026-10-03 |
| tfus:naphthalene | melting point of naphthalene (WebBook AVG, uncertainty 0.7 K) | 353.2 | K | WEBBOOK-PHASE | 2026-10-03 |
| dfus:naphthalene | enthalpy of fusion of naphthalene, median of seven determinations (16.4-19.6 kJ/mol) listed by the WebBook | 19.1 | kJ/mol | WEBBOOK-PHASE | 2026-10-03 |
| eut:Pb-Sn.T | eutectic temperature L -> (Pb) + (Sn), calculated invariant equilibrium (Pb-Sn system page) | 182.2 | degC | NIST-SOLDER | 2026-10-03 |
| eut:Pb-Sn.wL | mass % Sn of the eutectic liquid, Pb-Sn | 62.13 | % | NIST-SOLDER | 2026-10-03 |
| eut:Pb-Sn.wPb | mass % Sn of the (Pb) solid solution at the eutectic, Pb-Sn | 18.91 | % | NIST-SOLDER | 2026-10-03 |
| eut:Pb-Sn.wSn | mass % Sn of the (Sn) solid solution at the eutectic, Pb-Sn | 96.59 | % | NIST-SOLDER | 2026-10-03 |
| eut:Bi-Sn.T | eutectic temperature L -> (Bi) + (Sn), calculated invariant equilibrium (Bi-Sn system page) | 138.8 | degC | NIST-SOLDER | 2026-10-03 |
| eut:Bi-Sn.wL | mass % Bi of the eutectic liquid, Bi-Sn | 56.97 | % | NIST-SOLDER | 2026-10-03 |
| eut:Bi-Sn.wBi | mass % Bi of the (Bi) solid solution at the eutectic, Bi-Sn | 99.89 | % | NIST-SOLDER | 2026-10-03 |
| eut:Bi-Sn.wSn | mass % Bi of the (Sn) solid solution at the eutectic, Bi-Sn | 21.01 | % | NIST-SOLDER | 2026-10-03 |
| eut:NaCl-water.T | temperature of the ice + NaCl.2H2O eutectic at 1 bar | 252 | K | HAMP-2024 | 2026-10-03 |
| eut:NaCl-water.w | mass % NaCl of the ice + NaCl.2H2O eutectic solution at 1 bar | 23.3 | % | HAMP-2024 | 2026-10-03 |
| janafG:H2O_l.298 | standard Gibbs energy of formation of H2O(l), table H-063 at 298.15 K | -237.141 | kJ/mol | JANAF | 2026-10-03 |
| janafG:H2O_l.300 | standard Gibbs energy of formation of H2O(l), table H-063 at 300 K | -236.839 | kJ/mol | JANAF | 2026-10-03 |
| janafG:H2O_l.400 | standard Gibbs energy of formation of H2O(l), table H-063 at 400 K (liquid above its boiling point, 1 bar standard state) | -221.006 | kJ/mol | JANAF | 2026-10-03 |
| janafG:H2O_l.500 | standard Gibbs energy of formation of H2O(l), table H-063 at 500 K (metastable liquid, 1 bar standard state) | -206.002 | kJ/mol | JANAF | 2026-10-03 |
| janafdfH:H2O_l.300 | standard enthalpy of formation of H2O(l), table H-063 at 300 K | -285.771 | kJ/mol | JANAF | 2026-10-03 |
| janafdfH:H2O_l.500 | standard enthalpy of formation of H2O(l), table H-063 at 500 K | -279.095 | kJ/mol | JANAF | 2026-10-03 |
| janafG:H2O.298 | standard Gibbs energy of formation of H2O(g), table H-064 at 298.15 K | -228.582 | kJ/mol | JANAF | 2026-10-03 |
| janafG:H2O.400 | standard Gibbs energy of formation of H2O(g), table H-064 at 400 K | -223.901 | kJ/mol | JANAF | 2026-10-03 |
| janafG:H2O.600 | standard Gibbs energy of formation of H2O(g), table H-064 at 600 K | -214.007 | kJ/mol | JANAF | 2026-10-03 |
| janafG:H2O.800 | standard Gibbs energy of formation of H2O(g), table H-064 at 800 K | -203.496 | kJ/mol | JANAF | 2026-10-03 |
| janafG:H2O.1000 | standard Gibbs energy of formation of H2O(g), table H-064 at 1000 K | -192.59 | kJ/mol | JANAF | 2026-10-03 |
| janafdfH:H2O_g.300 | standard enthalpy of formation of H2O(g), table H-064 at 300 K | -241.844 | kJ/mol | JANAF | 2026-10-03 |
| janafdfH:H2O_g.500 | standard enthalpy of formation of H2O(g), table H-064 at 500 K | -243.826 | kJ/mol | JANAF | 2026-10-03 |
| janafdfH:H2O_g.600 | standard enthalpy of formation of H2O(g), table H-064 at 600 K | -244.758 | kJ/mol | JANAF | 2026-10-03 |
| janafdfH:H2O_g.700 | standard enthalpy of formation of H2O(g), table H-064 at 700 K | -245.632 | kJ/mol | JANAF | 2026-10-03 |
| janafdfH:H2O_g.800 | standard enthalpy of formation of H2O(g), table H-064 at 800 K | -246.443 | kJ/mol | JANAF | 2026-10-03 |
| janafdfH:H2O_g.900 | standard enthalpy of formation of H2O(g), table H-064 at 900 K | -247.185 | kJ/mol | JANAF | 2026-10-03 |
| janafdfH:H2O_g.1000 | standard enthalpy of formation of H2O(g), table H-064 at 1000 K | -247.857 | kJ/mol | JANAF | 2026-10-03 |
| dfh:CH3OH_l | standard enthalpy of formation of liquid methanol (WebBook; Chao and Rossini 1965 -239.5 +- 0.2, Green 1960 -238.9, Baroody and Carpenter 1972 -238.4: consensus -239) | -239 | kJ/mol | WEBBOOK-THERMO | 2026-10-03 |
| s0:CH3OH_l | standard molar entropy of liquid methanol (WebBook; Carlson and Westrum 1971) | 127.19 | J/(K.mol) | WEBBOOK-THERMO | 2026-10-03 |
| janafdfH:H2O_g.1100 | standard enthalpy of formation of H2O(g), table H-064 at 1100 K | -248.46 | kJ/mol | JANAF | 2026-10-03 |
| janafdfH:H2O_g.1300 | standard enthalpy of formation of H2O(g), table H-064 at 1300 K | -249.473 | kJ/mol | JANAF | 2026-10-03 |
| janafdfH:H2O_g.1500 | standard enthalpy of formation of H2O(g), table H-064 at 1500 K | -250.265 | kJ/mol | JANAF | 2026-10-03 |
| dfg:PbSO4_cr | standard Gibbs energy of formation of PbSO4(cr) at 298.15 K (table page 2-120) | -813.14 | kJ/mol | NBS-82 | 2026-10-03 |
| hT:Al_l.933 | enthalpy increment H(933.45 K) - H(298.15 K) of liquid aluminium at its melting point, table Al-004 | 28.693 | kJ/mol | JANAF | 2026-10-03 |
| janafG:NaCl.1100 | standard Gibbs energy of formation of NaCl (liquid at 1100 K, Na liquid reference), table Cl-055 | -310.674 | kJ/mol | JANAF | 2026-10-03 |
| re:C2 | equilibrium bond length of C2, ground state X 1Sigma g+ | 1.24253 | angstrom | WEBBOOK-DIAT | 2026-10-03 |
| re:Li2 | equilibrium bond length of Li2, ground state X 1Sigma g+ | 2.6729 | angstrom | WEBBOOK-DIAT | 2026-10-03 |
| re:NO | equilibrium bond length of NO, ground state X 2Pi | 1.15077 | angstrom | WEBBOOK-DIAT | 2026-10-03 |
| janafH0:N | standard enthalpy of formation of N(g) at 0 K, table N-002 | 470.82 | kJ/mol | JANAF | 2026-10-03 |
| janafH0:O | standard enthalpy of formation of O(g) at 0 K, table O-001 | 246.79 | kJ/mol | JANAF | 2026-10-03 |
| janafH0:F | standard enthalpy of formation of F(g) at 0 K, table F-001 | 77.284 | kJ/mol | JANAF | 2026-10-03 |
| janafH0:C | standard enthalpy of formation of C(g) at 0 K, table C-003 | 711.185 | kJ/mol | JANAF | 2026-10-03 |
| janafH0:Li | standard enthalpy of formation of Li(g) at 0 K, table Li-005 | 157.725 | kJ/mol | JANAF | 2026-10-03 |
| janafH0:CO | standard enthalpy of formation of CO(g) at 0 K, table C-093 | -113.805 | kJ/mol | JANAF | 2026-10-03 |
| janafH0:NO | standard enthalpy of formation of NO(g) at 0 K, table N-005 | 89.775 | kJ/mol | JANAF | 2026-10-03 |
| janafH0:C2 | standard enthalpy of formation of C2(g) at 0 K, table C-113 | 829.262 | kJ/mol | JANAF | 2026-10-03 |
| janafH0:Li2 | standard enthalpy of formation of Li2(g) at 0 K, table Li-013 | 215.469 | kJ/mol | JANAF | 2026-10-03 |
| ie:N2 | ionisation energy of N2 (WebBook evaluated, +- 0.008) | 15.581 | eV | WEBBOOK-IEMOL | 2026-10-03 |
| ie:CO | ionisation energy of CO (WebBook evaluated) | 14.014 | eV | WEBBOOK-IEMOL | 2026-10-03 |
| ie:NO | ionisation energy of NO (WebBook evaluated) | 9.2642 | eV | WEBBOOK-IEMOL | 2026-10-03 |
| ie:H2O | first (adiabatic) ionisation energy of H2O (WebBook evaluated, +- 0.002) | 12.621 | eV | WEBBOOK-IEMOL | 2026-10-03 |
| ie:CH4 | first ionisation energy of CH4 (WebBook evaluated, +- 0.01) | 12.61 | eV | WEBBOOK-IEMOL | 2026-10-03 |
| ie:NH3 | first ionisation energy of NH3 (WebBook evaluated, +- 0.020) | 10.070 | eV | WEBBOOK-IEMOL | 2026-10-03 |
| ie:C2H4 | first ionisation energy of C2H4 (WebBook evaluated) | 10.5138 | eV | WEBBOOK-IEMOL | 2026-10-03 |
| dfh:C6H6_g | standard enthalpy of formation of benzene(g) (WebBook; review Roux, Temprado et al. 2008, +- 0.9) | 82.9 | kJ/mol | WEBBOOK-THERMO | 2026-10-03 |
| dfh:C6H10_g | standard enthalpy of formation of cyclohexene(g) (WebBook; Steele, Chirico et al. 1996, +- 1.0; other determinations -4.7 to -7.1) | -4.3 | kJ/mol | WEBBOOK-THERMO | 2026-10-03 |
| dfh:C6H12_g | standard enthalpy of formation of cyclohexane(g) (WebBook; Prosen, Johnson et al. 1946, +- 0.8) | -123.1 | kJ/mol | WEBBOOK-THERMO | 2026-10-03 |
| dfh:C6H8_g | standard enthalpy of formation of cyclohexa-1,3-diene(g) (WebBook; Steele, Chirico et al. 1989, +- 0.6) | 104.6 | kJ/mol | WEBBOOK-THERMO | 2026-10-03 |
| ghs:cyclopentadiene | cyclopentadiene (CID 7612), GHS classification summary: pictograms | GHS02 GHS06 GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:dicyclopentadiene | dicyclopentadiene (CID 6492), GHS classification summary: pictograms | GHS02 GHS06 GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:maleic-anhydride | maleic anhydride (CID 7923), GHS classification summary: pictograms | GHS05 GHS06 GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| bp:cyclopentadiene | boiling point of cyclopentadiene (PubChem CID 7612, Boiling Point: 41.5-42.0 degC, 41 degC) | 41 | degC | PUBCHEM | 2026-10-03 |
| bp:dicyclopentadiene | boiling point of dicyclopentadiene (PubChem CID 6492, Boiling Point: 172 degC; 166.6 degC at 760 mmHg) | 170 | degC | PUBCHEM | 2026-10-03 |
| dfh:C5H6_g | standard enthalpy of formation of cyclopentadiene(g) (WebBook; Roth, Adamczak et al. 1991 139, Furuyama, Golden et al. 1970 133.4) | 134 | kJ/mol | WEBBOOK-THERMO | 2026-10-03 |
| s0:C5H6_g | standard molar entropy of cyclopentadiene(g) (WebBook; Furuyama 1970) | 274.5 | J/(K.mol) | WEBBOOK-THERMO | 2026-10-03 |
| ghs:Pd-acetate | palladium(II) acetate (CID 167845), GHS classification summary: pictograms | GHS05 GHS07 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:PPh3 | triphenylphosphine (CID 11776), GHS classification summary: pictograms | GHS05 GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:phenylboronic-acid | phenylboronic acid (CID 66827), GHS classification summary: pictograms | GHS07 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:4-bromotoluene | 4-bromotoluene (CID 7805), GHS classification summary: pictograms | GHS07 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:OsO4 | osmium tetroxide (CID 30318), GHS classification summary: pictograms | GHS05 GHS06 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:mCPBA | 3-chloroperbenzoic acid (CID 70297), GHS classification summary: pictograms | GHS02 GHS03 GHS05 GHS07 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:BH3-THF | borane tetrahydrofuran (CID 11062302), GHS classification summary: pictograms | GHS02 GHS05 GHS07 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:NaIO4 | sodium periodate (CID 23667635), GHS classification summary: pictograms | GHS03 GHS05 GHS06 GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:O3 | ozone (CID 24823), GHS classification summary: pictograms | GHS03 GHS05 GHS06 GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:limonene | limonene (CID 22311), GHS classification summary: pictograms | GHS02 GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| mp:2-nitrotoluene | melting point of 2-nitrotoluene (PubChem CID 6944: -9.55 degC alpha form, -3.85 degC beta form; -10 degC) | -10 | degC | PUBCHEM | 2026-10-03 |
| mp:3-nitrotoluene | melting point of 3-nitrotoluene (PubChem CID 7422: 15.5, 16.1, 16 degC) | 16 | degC | PUBCHEM | 2026-10-03 |
| mp:4-nitrotoluene | melting point of 4-nitrotoluene (PubChem CID 7473: 51.7, 51.63, 53-54 degC) | 52 | degC | PUBCHEM | 2026-10-03 |
| ghs:nitrotoluene-4 | 4-nitrotoluene (CID 7473), GHS classification summary: pictograms | GHS06 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:toluene | toluene (CID 1140), GHS classification summary: pictograms | GHS02 GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:AlCl3 | aluminium chloride (CID 24012), GHS classification summary: pictograms | GHS05 GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:HNO3 | nitric acid (CID 944), GHS classification summary: pictograms | GHS03 GHS05 GHS06 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:Br2 | bromine (CID 24408), GHS classification summary: pictograms | GHS05 GHS06 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:benzene | benzene (CID 241), GHS classification summary: pictograms | GHS02 GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:NaNO2 | sodium nitrite (CID 23668193), GHS classification summary: pictograms | GHS03 GHS06 GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:aniline | aniline (CID 6115), GHS classification summary: pictograms | GHS05 GHS06 GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:NaBH3CN | sodium cyanoborohydride (CID 5003444), GHS classification summary: pictograms | GHS02 GHS05 GHS06 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:sulfanilic-acid | sulfanilic acid (CID 8479), GHS classification summary: pictograms | GHS07 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:dimethylaniline | N,N-dimethylaniline (CID 949), GHS classification summary: pictograms | GHS02 GHS05 GHS06 GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| pka:dimethylammonium | dimethylammonium (pKaH of dimethylamine) at 25 degC (perrin26, ref H31, I = 0.03-1.5; S61 10.81) | 10.73 | - | IUPAC-PKA | 2026-10-03 |
| pka:trimethylammonium | trimethylammonium (pKaH of trimethylamine) at 25 degC (perrin_supp4004 ref N23 9.801; perrin18 ref M15 9.81) | 9.80 | - | IUPAC-PKA | 2026-10-03 |
| pka:ethanamideH | protonated ethanamide (pKaH of acetamide) at 25 degC (perrin11, ref K14, from rates of acid hydrolysis; other determinations -1.4 to +0.4) | -0.6 | - | IUPAC-PKA | 2026-10-03 |
| ghs:SOCl2 | thionyl chloride (CID 24386), GHS classification summary: pictograms | GHS05 GHS06 GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:ethanoyl-chloride | acetyl chloride (CID 6367), GHS classification summary: pictograms | GHS02 GHS05 GHS07 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:LiAlH4 | lithium aluminum hydride (CID 28112), GHS classification summary: pictograms | GHS02 GHS05 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:methanol | methanol (CID 887), GHS classification summary: pictograms | GHS02 GHS06 GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| pka:acac | pentane-2,4-dione, pKa (C-H) at 25 degC (serjeant2558 ref C5 9.01; perrin3433 ref E18 8.95; others 8.8-9.0) | 9.0 | - | IUPAC-PKA | 2026-10-03 |
| pka:acetoacetate | ethyl 3-oxobutanoate, pKa (C-H) at 25 degC (serjeant2876, ref E1l, Approximate) | 10.7 | - | IUPAC-PKA | 2026-10-03 |
| pka:nitromethane | nitromethane, pKa (C-H) at 25 degC (serjeant2009, refs T67, W22, Approximate) | 10.2 | - | IUPAC-PKA | 2026-10-03 |
| rho:benzaldehyde | density of benzaldehyde near 20 degC (PubChem CID 240: 1.046 at 68 degF; 1.040-1.047) | 1.045 | g/cm3 | PUBCHEM | 2026-10-03 |
| ghs:benzaldehyde | benzaldehyde (CID 240), GHS classification summary: pictograms | GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:NaOEt | sodium ethoxide (CID 2723922), GHS classification summary: pictograms | GHS02 GHS05 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:LDA | lithium diisopropylamide (CID 2724682), GHS classification summary: pictograms | GHS02 GHS05 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:dibenzalacetone | dibenzylideneacetone (CID 640180), GHS classification summary: pictograms | GHS07 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| pka:cyclohexanedione | cyclohexane-1,3-dione, pKa1 at 25 degC (serjeant2846, ref S47, Approximate; dimedone serjeant4064 5.27) | 5.3 | - | IUPAC-PKA | 2026-10-03 |
| ghs:MVK | but-3-en-2-one, methyl vinyl ketone (CID 6570), GHS classification summary: pictograms | GHS02 GHS05 GHS06 GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:cyclohexenone | cyclohex-2-en-1-one (CID 13594), GHS classification summary: pictograms | GHS02 GHS06 GHS07 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:methylcyclohexanedione | 2-methylcyclohexane-1,3-dione (CID 70945), GHS classification summary: pictograms | GHS07 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:MeMgBr | methylmagnesium bromide (CID 6349), GHS classification summary: pictograms | GHS02 GHS05 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| pka:diethylmalonate | diethyl propanedioate, pKa (C-H) in water (serjeant3475, ref B47, kinetic method, temperature not stated, Uncertain; printed as about 13) | 13 | - | IUPAC-PKA | 2026-10-03 |
| use:muscalure | role of (9Z)-tricos-9-ene, muscalure (PubChem CID 5365075, MeSH description: 'sex attractant pheromone of housefly') | housefly sex attractant pheromone | -- | PUBCHEM | 2026-10-03 |
| ghs:BuLi | butyllithium (CID 53627823), GHS classification summary: pictograms | GHS02 GHS05 GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:triethyl-phosphite | triethyl phosphite (CID 31215), GHS classification summary: pictograms | GHS02 GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:nonanal | nonanal (CID 31289), GHS classification summary: pictograms | GHS07 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:Ph3PO | triphenylphosphine oxide (CID 13097), GHS classification summary: pictograms | GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:BnPPh3Cl | benzyltriphenylphosphonium chloride (CID 70671), GHS classification summary: pictograms | GHS05 GHS06 GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:phosphonoacetate | triethyl phosphonoacetate (CID 13345), GHS classification summary: pictograms | GHS07 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:DMP | Dess-Martin periodinane, triacetoxyperiodinane (CID 159087), GHS classification summary: pictograms | GHS03 GHS07 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:oxalyl-chloride | oxalyl chloride (CID 65578), GHS classification summary: pictograms | GHS02 GHS05 GHS06 GHS07 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:DMSO | dimethyl sulfoxide (CID 679), GHS classification summary: pictograms | GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:raspberry-ketone | 4-(4-hydroxyphenyl)butan-2-one (CID 21648), GHS classification summary: pictograms | GHS07 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:4-iodophenol | 4-iodophenol (CID 10894), GHS classification summary: pictograms | GHS05 GHS07 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| use:raspberry-ketone | occurrence and use of 4-(4-hydroxyphenyl)butan-2-one (PubChem CID 21648, Record Description, ChEBI): found in raspberries, blackberries and cranberries; used in perfumery, cosmetics, as a flavouring agent | fruits; flavour and fragrance | -- | PUBCHEM | 2026-10-03 |
| ghs:styrene | styrene (CID 7501), GHS classification summary: pictograms | GHS02 GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:BPO | dibenzoyl peroxide (CID 7187), GHS classification summary: pictograms | GHS01 GHS02 GHS03 GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:hexanediamine | hexane-1,6-diamine (CID 16402), GHS classification summary: pictograms | GHS05 GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:adipic-acid | hexanedioic acid (CID 196), GHS classification summary: pictograms | GHS05 GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:MMA | methyl methacrylate (CID 6658), GHS classification summary: pictograms | GHS02 GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| pka:alanine1 | alanine, pKa of the carboxylic group at 25 degC (perrin2979, Reliable: 2.345, 2.348, 2.34) | 2.35 | - | IUPAC-PKA | 2026-10-03 |
| pka:alanine2 | alanine, pKa of the ammonium group at 25 degC (perrin2979, Reliable: 9.87, 9.866) | 9.87 | - | IUPAC-PKA | 2026-10-03 |
| pka:asp1 | aspartic acid, pKa of the alpha-carboxylic group at 25 degC (perrin3090, Reliable 1.99; others 1.94-2.04) | 2.0 | - | IUPAC-PKA | 2026-10-03 |
| pka:asp2 | aspartic acid, pKa of the side-chain carboxylic group at 25 degC (perrin3090, Reliable 3.90 and 3.895) | 3.9 | - | IUPAC-PKA | 2026-10-03 |
| pka:asp3 | aspartic acid, pKa of the ammonium group at 25 degC (perrin3090: 9.842 Reliable, 10.002 Approximate, others 9.86-9.93) | 9.9 | - | IUPAC-PKA | 2026-10-03 |
| pka:glu1 | glutamic acid, pKa of the alpha-carboxylic group at 25 degC (perrin3126, Approximate 2.13, 2.10) | 2.1 | - | IUPAC-PKA | 2026-10-03 |
| pka:glu2 | glutamic acid, pKa of the side-chain carboxylic group at 25 degC (perrin3126, Approximate 4.31; others 4.07-4.51) | 4.3 | - | IUPAC-PKA | 2026-10-03 |
| pka:glu3 | glutamic acid, pKa of the ammonium group at 25 degC (perrin3126, Approximate 9.76; others 9.45-9.95) | 9.8 | - | IUPAC-PKA | 2026-10-03 |
| pka:lys1 | lysine, pKa of the carboxylic group at 25 degC (perrin3226, Approximate 2.18, 2.15) | 2.2 | - | IUPAC-PKA | 2026-10-03 |
| pka:lys2 | lysine, pKa of the alpha-ammonium group at 25 degC (perrin3226 and perrin_supp7698: 8.95-9.18, Approximate) | 9.1 | - | IUPAC-PKA | 2026-10-03 |
| pka:lys3 | lysine, pKa of the side-chain ammonium group at 25 degC (perrin3226 and perrin_supp7698: 10.53-10.81, Approximate) | 10.7 | - | IUPAC-PKA | 2026-10-03 |
| pka:his1 | histidine, pKa of the carboxylic group at 25 degC (perrin3191, 1.80-1.82, Approximate) | 1.8 | - | IUPAC-PKA | 2026-10-03 |
| pka:his2 | histidine, pKa of the imidazolium side chain at 25 degC (perrin3191, 5.96-6.12, Approximate) | 6.0 | - | IUPAC-PKA | 2026-10-03 |
| pka:his3 | histidine, pKa of the ammonium group at 25 degC (perrin3191, 9.12-9.33, Approximate) | 9.2 | - | IUPAC-PKA | 2026-10-03 |
| rot:glucose-eq | specific rotation of D-glucose at equilibrium in water, 20 degC, sodium D line (HSDB via PubChem CID 5793) | +52.7 | deg dm-1 (g/mL)-1 | PUBCHEM | 2026-10-03 |
| mp:stearic | melting point of stearic (octadecanoic) acid (PubChem CID 5281: HSDB 69.3, HMDB 68.8 degC) | 69 | degC | PUBCHEM | 2026-10-03 |
| mp:oleic | melting point of oleic ((Z)-octadec-9-enoic) acid (PubChem CID 445639: HMDB, ICSC 13.4 degC; HSDB 16.3 degC for another form) | 13 | degC | PUBCHEM | 2026-10-03 |
| use:aspartame | aspartame (PubChem CID 134601, ChEBI and MeSH): dipeptide of L-aspartic acid and methyl L-phenylalaninate, used as a sweetener 'sweeter than sugar', metabolised to phenylalanine and aspartic acid | sweetener | -- | PUBCHEM | 2026-10-03 |
| ghs:acetonitrile | acetonitrile (CID 6342), GHS classification summary: pictograms | GHS02 GHS05 GHS06 GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:hexane | hexane (CID 8058), GHS classification summary: pictograms | GHS02 GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:caffeine | caffeine (CID 2519), GHS classification summary: pictograms | GHS06 GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ms:butanone | EI mass spectrum of butan-2-one (CAS 78-93-3), m/z:relative intensity (base peak 100) for peaks of at least 1.0 % | 15:4 26:1 27:8 28:3 29:17 39:2 41:1 42:3 43:100 44:3 57:8 71:1 72:25 73:1 | % | WEBBOOK-MS | 2026-10-03 |
| ms:bromopropane | EI mass spectrum of 1-bromopropane (CAS 106-94-5), m/z:relative intensity (base peak 100) for peaks of at least 0.8 % | 15:1.6 26:2.4 27:25.6 28:1.6 29:4 37:1.2 38:2.2 39:9 40:2.1 41:31 42:7.7 43:100 44:3.5 79:0.9 80:0.9 81:0.8 82:0.8 93:1.1 95:1 107:1.5 109:1.2 122:8.6 124:8.3 | % | WEBBOOK-MS | 2026-10-03 |
| ms:pentan-2-one | EI mass spectrum of pentan-2-one (CAS 107-87-9), m/z:relative intensity (base peak 100) for peaks of at least 1.0 % | 15:1.7 26:1.2 27:7.7 29:1.6 38:1.3 39:7.8 40:1.1 41:13.8 42:6 43:100 44:2.9 58:9.8 71:9.7 86:19.7 87:1.2 | % | WEBBOOK-MS | 2026-10-03 |
| ms:pentan-3-one | EI mass spectrum of pentan-3-one (CAS 96-22-0), m/z:relative intensity (base peak 100) for peaks of at least 1.0 % | 26:2.5 27:12.4 28:4.3 29:59.4 30:1.4 39:1.8 41:2 42:1.8 43:1.6 55:1.3 56:3.7 57:100 58:3.4 86:21.2 87:1.2 | % | WEBBOOK-MS | 2026-10-03 |
| ms:bromochloropropane | EI mass spectrum of 1-bromo-3-chloropropane (CAS 109-70-6), m/z:relative intensity (base peak 100) for peaks of at least 0.5 % | 15:1.1 26:4 27:24.6 28:3.4 35:0.5 36:1.3 37:2.7 38:5.1 39:26.2 40:5.1 41:100 42:3.9 47:0.6 48:0.8 49:12.9 51:4.3 61:1.2 62:0.6 63:2 75:2.7 76:39.5 77:59 78:13.7 79:18.7 80:1 81:1.6 82:1 93:3.3 95:2.9 107:6.7 108:0.5 109:6.3 120:1.4 122:1.3 156:14.5 157:0.5 158:18.6 159:0.6 160:4.4 | % | WEBBOOK-MS | 2026-10-03 |
| mass:H1 | relative atomic mass of hydrogen-1 (NIST AWIC, AME) | 1.00782503223 | u | NIST-AWIC | 2026-10-03 |
| mass:C12 | relative atomic mass of carbon-12 (exact by definition) (NIST AWIC, AME) | 12 | u | NIST-AWIC | 2026-10-03 |
| mass:C13 | relative atomic mass of carbon-13 (NIST AWIC, AME) | 13.00335483507 | u | NIST-AWIC | 2026-10-03 |
| mass:N14 | relative atomic mass of nitrogen-14 (NIST AWIC, AME) | 14.00307400443 | u | NIST-AWIC | 2026-10-03 |
| mass:O16 | relative atomic mass of oxygen-16 (NIST AWIC, AME) | 15.99491461957 | u | NIST-AWIC | 2026-10-03 |
| mass:Cl35 | relative atomic mass of chlorine-35 (NIST AWIC, AME) | 34.968852682 | u | NIST-AWIC | 2026-10-03 |
| mass:Cl37 | relative atomic mass of chlorine-37 (NIST AWIC, AME) | 36.965902602 | u | NIST-AWIC | 2026-10-03 |
| mass:Br79 | relative atomic mass of bromine-79 (NIST AWIC, AME) | 78.9183376 | u | NIST-AWIC | 2026-10-03 |
| mass:Br81 | relative atomic mass of bromine-81 (NIST AWIC, AME) | 80.9162897 | u | NIST-AWIC | 2026-10-03 |
| iso:Br79 | amount fraction of bromine-79, representative isotopic composition 0.5069(7) (NIST AWIC) | 0.5069 | -- | NIST-AWIC | 2026-10-03 |
| iso:Br81 | amount fraction of bromine-81, representative isotopic composition 0.4931(7) (NIST AWIC) | 0.4931 | -- | NIST-AWIC | 2026-10-03 |
| iso:N15 | amount fraction of nitrogen-15, representative isotopic composition 0.00364(20) (NIST AWIC) | 0.00364 | -- | NIST-AWIC | 2026-10-03 |
| iso:O18 | amount fraction of oxygen-18, representative isotopic composition 0.00205(14) (NIST AWIC) | 0.00205 | -- | NIST-AWIC | 2026-10-03 |
| iso:S34 | amount fraction of sulfur-34, representative isotopic composition 0.0425(24) (NIST AWIC) | 0.0425 | -- | NIST-AWIC | 2026-10-03 |
| asd:NaD2 | Na I 3s 2S1/2 - 3p 2P3/2 (D2), observed wavelength in air | 588.995 | nm | NIST-ASD | 2026-10-03 |
| asd:NaD1 | Na I 3s 2S1/2 - 3p 2P1/2 (D1), observed wavelength in air | 589.592 | nm | NIST-ASD | 2026-10-03 |
| asd:Li671 | Li I 2s - 2p resonance doublet (670.776 and 670.791), observed wavelength in air | 670.78 | nm | NIST-ASD | 2026-10-03 |
| asd:Sr461 | Sr I 5s2 1S0 - 5s5p 1P1 resonance line, observed wavelength in air | 460.733 | nm | NIST-ASD | 2026-10-03 |
| asd:Ba455 | Ba II 6s 2S1/2 - 6p 2P3/2 resonance line, observed wavelength in air | 455.403 | nm | NIST-ASD | 2026-10-03 |
| asd:Cu325 | Cu I 4s 2S1/2 - 4p 2P3/2 resonance line, observed wavelength in air | 324.754 | nm | NIST-ASD | 2026-10-03 |
| mass:Ar40 | relative atomic mass of argon-40 (NIST AWIC, AME) | 39.9623831237 | u | NIST-AWIC | 2026-10-03 |
| mass:Fe56 | relative atomic mass of iron-56 (NIST AWIC, AME) | 55.93493633 | u | NIST-AWIC | 2026-10-03 |
| c13:butanone | butan-2-one, decoupled 13C spectrum, CDCl3, 15.09 MHz (PubChem CID 6569, 13C NMR Spectra, HMDB peak list 3330), shift:relative height | 209.28:313 36.87:1000 29.43:559 7.87:799 | ppm | PUBCHEM | 2026-10-03 |
| c13:ethylbenzoate | ethyl benzoate, decoupled 13C spectrum, CDCl3, 25.16 MHz (PubChem CID 7165, HMDB peak list 3399), shift:relative height | 166.54:194 132.80:418 130.62:244 129.57:1000 128.34:801 60.90:353 14.33:294 | ppm | PUBCHEM | 2026-10-03 |
| c13:benzylacetate | benzyl ethanoate, decoupled 13C spectrum, CDCl3, 25.16 MHz (PubChem CID 8785, HMDB peak list 2934), shift:relative height; six resolved lines | 170.70:204 136.14:199 128.56:776 128.24:1000 66.24:328 20.82:204 | ppm | PUBCHEM | 2026-10-03 |
| c13:pentan-2-one | pentan-2-one, decoupled 13C spectrum, CDCl3, 15.09 MHz (PubChem CID 7895, HMDB peak list), shift:relative height | 208.93:443 45.71:1000 29.78:590 17.41:951 13.70:820 | ppm | PUBCHEM | 2026-10-03 |
| nmr:butanone | butan-2-one, 1H spectrum, CDCl3, 500 MHz (PubChem CID 6569, HMDB peak list 1387): signal centres, multiplicity from the lines (2.43-2.48 q; 2.14 s; 1.04-1.07 t) | 2.45 q 2H; 2.14 s 3H; 1.06 t 3H | ppm | PUBCHEM | 2026-10-03 |
| nmr:ethylbenzoate | ethyl benzoate, 1H spectrum, CDCl3, 90 MHz (PubChem CID 7165, HMDB peak list 2707): 8.02-8.10 m; 7.35-7.63 m; 4.25-4.49 q; 1.30-1.46 t | 8.05 m 2H; 7.35-7.63 m 3H; 4.37 q 2H; 1.38 t 3H | ppm | PUBCHEM | 2026-10-03 |
| nmr:benzylacetate | benzyl ethanoate, 1H spectrum, CDCl3, 90 MHz (PubChem CID 8785, HMDB peak list 2239) | 7.33 m 5H; 5.09 s 2H; 2.06 s 3H | ppm | PUBCHEM | 2026-10-03 |
| nmr:pentan-2-one | pentan-2-one, 1H spectrum, CDCl3, 90 MHz (PubChem CID 7895, HMDB peak list): 2.33-2.49 t; 2.12-2.13 s; 1.48-1.74 sextet; 0.82-1.00 t | 2.41 t 2H; 2.13 s 3H; 1.61 m 2H; 0.91 t 3H | ppm | PUBCHEM | 2026-10-03 |
| ms:benzylacetate | EI mass spectrum of benzyl ethanoate (CAS 140-11-4), m/z:relative intensity (base peak 100) for peaks of at least 2.0 % | 39:9.1 43:37.6 50:7 51:16.7 52:4.1 62:2.7 63:8.4 64:2.2 65:18.6 77:24.6 78:5.8 79:31.1 80:3 89:17.9 90:40.6 91:71.7 92:5.5 105:5.2 107:19.5 108:100 109:7.8 150:31.7 151:3.1 | % | WEBBOOK-MS | 2026-10-03 |
| use:benzylacetate | odour and occurrence of benzyl ethanoate (PubChem CID 8785: HSDB 'characteristic flowery (jasmine) odor'; T3DB: occurs in jasmine and fruits) | jasmine odour | -- | PUBCHEM | 2026-10-03 |
| ghs:benzylacetate | benzyl ethanoate (CID 8785), GHS classification summary: pictograms | GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:butanone | butan-2-one (CID 6569), GHS classification summary: pictograms | GHS02 GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| who:lead | WHO provisional guideline value for lead in drinking-water (GDWQ 4th ed. with addenda, chemical fact sheet 2022: '0.01 mg/l (10 ug/l)', provisional on the basis of treatment performance and analytical achievability) | 10 | ug/L | WHO-DWQ | 2026-10-03 |
| asd:Pb283 | Pb I 6s2 6p2 3P0 - 6p7s resonance line used in atomic absorption, observed wavelength in air | 283.305 | nm | NIST-ASD | 2026-10-03 |
| tb:bromobenzene | normal boiling point of bromobenzene (WebBook average of 27 values, ± 0.6 K) | 429.1 | K | WEBBOOK-PHASE | 2026-10-03 |
| dvap:bromobenzene | enthalpy of vaporisation of bromobenzene near 344-348 K (WebBook: 42.3 at 348 K, 42.4 at 344 K) | 42.4 | kJ/mol | WEBBOOK-PHASE | 2026-10-03 |
| tbp:bromobenzene.7mbar | boiling temperature of bromobenzene at 0.007 bar (WebBook reduced-pressure table, Buckingham and Donaghy 1982) | 300.9 | K | WEBBOOK-PHASE | 2026-10-03 |
| tb:benzaldehyde | boiling point of benzaldehyde at 1.00 bar (WebBook reduced-pressure table; average of 13 values 452 ± 7 K) | 452 | K | WEBBOOK-PHASE | 2026-10-03 |
| dvap:benzaldehyde | enthalpy of vaporisation of benzaldehyde near 385 K (WebBook, Stephenson and Malanowski, data 370-475 K) | 45.5 | kJ/mol | WEBBOOK-PHASE | 2026-10-03 |
| tbp:benzaldehyde.13mbar | boiling temperature of benzaldehyde at 0.013 bar (WebBook reduced-pressure table) | 335 | K | WEBBOOK-PHASE | 2026-10-03 |
| tb:ether | normal boiling point of ethoxyethane (WebBook average of 20 values, ± 0.4 K) | 307.7 | K | WEBBOOK-PHASE | 2026-10-03 |
| ghs:ether | ethoxyethane, diethyl ether (CID 3283), GHS classification summary: pictograms | GHS02 GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:THF | oxolane, tetrahydrofuran (CID 8028), GHS classification summary: pictograms | GHS02 GHS07 GHS08 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:bromobenzene | bromobenzene (CID 7961), GHS classification summary: pictograms | GHS02 GHS06 GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:MgSO4 | magnesium sulfate (CID 24083), GHS classification summary: pictograms | GHS07 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:biphenyl | biphenyl (CID 7095), GHS classification summary: pictograms | GHS06 GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:NH4Cl | ammonium chloride (CID 25517), GHS classification summary: pictograms | GHS07 GHS08 GHS09 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| ghs:benzhydrol | diphenylmethanol (CID 7037), GHS classification summary: pictograms | GHS07 | -- | PUBCHEM-GHSSUM | 2026-10-03 |
| nmr:biphenyl | biphenyl, 1H spectrum, CDCl3, 400 MHz (PubChem CID 7095, HMDB peak list): all lines between | 7.33-7.61 | ppm | PUBCHEM | 2026-10-03 |
| ph:NaHCO3 | pH of a freshly prepared 0.1 mol/L sodium hydrogencarbonate solution at 25 degC (PubChem CID 516892, HSDB) | 8.3 | -- | PUBCHEM | 2026-10-03 |
