# Data ledger — Book 4 (University Year 3)

Book 4's own rows. Shared rows (atomic weights, constants) are in
`sources/data_ledger.md`; the rules are stated there. Owned by the Book 4
writer; other books may cite these rows read-only.

## Sources

| key | source | URL |
|---|---|---|
| WEBBOOK-DIAT | NIST Chemistry WebBook, SRD 69, constants of diatomic molecules (K. P. Huber and G. Herzberg compilation, with later updates cited on the page); X ground state unless the row says otherwise; footnote digits dropped | https://webbook.nist.gov/chemistry/ |
| PHOTOCHEMCAD | PhotochemCAD common-compounds database: M. Taniguchi, H. Du and J. S. Lindsey, "Database of absorption and fluorescence spectra of >300 common compounds for use in PhotochemCAD", Photochem. Photobiol. 94 (2018) 290; absorption maxima in the solvent given in the row | https://www.photochemcad.com/databases/common-compounds |
| CCCBDB | NIST Computational Chemistry Comparison and Benchmark Database, SRD 101, release 22 (experimental and computed data; original reference in the row) | https://cccbdb.nist.gov/ |
| CODATA2022 | CODATA 2022 recommended values of the fundamental physical constants (NIST, physics.nist.gov/cuu) | https://physics.nist.gov/cuu/Constants/ |
| ASD-LEVELS | NIST Atomic Spectra Database (Kramida, Ralchenko, Reader and NIST ASD Team), energy levels, version 5; level energies in cm-1 above the ground level | https://physics.nist.gov/PhysRefData/ASD/levels_form.html |
| ASD-IE4 | NIST Atomic Spectra Database, ionization energies | https://physics.nist.gov/PhysRefData/ASD/ionEnergy.html |
| JANAF4 | NIST-JANAF Thermochemical Tables, 4th ed. (M. W. Chase, 1998), online tables; the row and temperature are given | https://janaf.nist.gov/ |
| WEBBOOK-IEMOL4 | NIST Chemistry WebBook (SRD 69), gas-phase ion energetics, ionization energy determinations (evaluated value; reference in the row) | https://webbook.nist.gov/chemistry/ |
| GUSTEN-2019 | R. Güsten et al., "Astrophysical detection of the helium hydride ion HeH+", Nature 568 (2019) 357-359, doi:10.1038/s41586-019-1090-x (metadata read from Crossref) | https://doi.org/10.1038/s41586-019-1090-x |
| KATZER | G. Katzer, Character tables for chemically important point groups (online tables, each with classes, irreducible representations and Cartesian functions); each printed table is also checked by tests/bachelor-3/test_character-tables.py (orthogonality, sum of squared dimensions = order) | https://gernot-katzers-spice-pages.com/character_tables/ |
| WEBBOOK-VIB | NIST Chemistry WebBook (SRD 69), vibrational energy levels compiled by T. Shimanouchi, Tables of Molecular Vibrational Frequencies Consolidated Volume I, NSRDS-NBS 39 (1972); "selected" gas-phase fundamentals | https://webbook.nist.gov/chemistry/ |
| NIST-AWIC | J. S. Coursey et al., Atomic Weights and Isotopic Compositions (NIST, version 4.1), relative atomic masses of nuclides (AME2016) | https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl |
| CDMS | Cologne Database for Molecular Spectroscopy (H. S. P. Müller et al., J. Mol. Struct. 742 (2005) 215; C. P. Endres et al., J. Mol. Spectrosc. 327 (2016) 95), catalogue entries c028503 (CO) and c029501 (13CO), rest frequencies | https://cdms.astro.uni-koeln.de/ |
| WEBBOOK-FLUID | NIST Chemistry WebBook (SRD 69), thermophysical properties of fluid systems (reference correlations cited in the row), 298.15 K and 0.1 MPa | https://webbook.nist.gov/chemistry/fluid/ |
| IAEA-NUC | N. J. Stone, Table of Nuclear Magnetic Dipole and Electric Quadrupole Moments, IAEA report INDC(NDS)-0658 (2014), doi:10.61092/iaea.zhrz-3g5j; magnetic moments in nuclear magnetons | https://nds.iaea.org/ |
| PUBCHEM4 | PubChem compound records (PUG-View), section and original source given in the row (13C NMR peak lists from the Wiley SpectraBase collection) | https://pubchem.ncbi.nlm.nih.gov/ |
| NIST-XRAY | R. D. Deslattes et al., X-ray Transition Energies (NIST SRD 128, version 1.2), experimental "combined" wavelengths | https://physics.nist.gov/PhysRefData/XrayTrans/Html/search.html |
| COD4 | Crystallography Open Database; COD entry number and original reference in the row | https://www.crystallography.net/cod/ |
| CODATA-KEY4 | J. D. Cox, D. D. Wagman, V. A. Medvedev, *CODATA Key Values for Thermodynamics* (Hemisphere, 1989), online table: standard entropy at 298.15 K, p° = 1 bar, with the stated uncertainty | https://www.codata.info/resources/databases/key1.html |
| IUPAC-ATMOS | IUPAC Task Group on Atmospheric Chemical Kinetic Data Evaluation, preferred values (datasheet code and evaluation date in the row), IUPAC/AERIS catalogue | https://iupac.aeris-data.fr/ |
| PMC-DEUT | K. Banno et al., "Deuterated alkyl sulfonium salt reagents; importance of H/D exchange methods in drug discovery", ChemMedChem (2024), open access, PMC13494818 (introduction: the first deuterated drug and its two OCD3 groups) | https://pmc.ncbi.nlm.nih.gov/articles/PMC13494818/ |
| BAR-EVEN-2011 | A. Bar-Even et al., "The moderately efficient enzyme: evolutionary and physicochemical trends shaping enzyme parameters", Biochemistry 50 (2011) 4402-4410, doi:10.1021/bi2002289 (abstract, PubMed 21506553) | https://pubmed.ncbi.nlm.nih.gov/21506553/ |
| NASA-OZONE | NASA Ozone Watch, "Dobson Units" fact page (Goddard Space Flight Center) | https://ozonewatch.gsfc.nasa.gov/facts/dobson_SH.html |
| SCHOENLEIN-1991 | R. W. Schoenlein, L. A. Peteanu, R. A. Mathies and C. V. Shank, "The first step in vision: femtosecond isomerization of rhodopsin", Science 254 (1991) 412-415, doi:10.1126/science.1925597 (abstract, PubMed 1925597) | https://pubmed.ncbi.nlm.nih.gov/1925597/ |
| IAPWS-R8-97 | IAPWS Release on the Static Dielectric Constant of Ordinary Water Substance for Temperatures from 238 K to 873 K and Pressures up to 1000 MPa (R8-97), Eqs. (2)-(7) with Tables 1-2; the implementation reproduces the check values of its Table 3 (87.96 at 273 K, 69.96 at 323 K) | https://iapws.org/technical-guidance/release/Dielec |
| NIST-SP960-17 | L. Espinal, "Porosity and specific surface area measurements for solid materials", NIST Recommended Practice Guide, Special Publication 960-17 (2006), section on the BET area | https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication960-17.pdf |
| IAPWS-R1-76 | IAPWS Revised Release on Surface Tension of Ordinary Water Substance, R1-76(2014), Table 1 | https://iapws.org/technical-guidance/release/Surf-H2O |
| NSRDS-NBS36 | P. Mukerjee and K. J. Mysels, Critical Micelle Concentrations of Aqueous Surfactant Systems, NSRDS-NBS 36 (1971), Table of Recommended and Selected CMCs (compound number in the row) | https://nvlpubs.nist.gov/nistpubs/Legacy/NSRDS/nbsnsrds36.pdf |
| CALTECH-MS | G. R. Rossman, Mineral Spectroscopy Server, California Institute of Technology: visible absorption spectra of gem minerals (data files; sample and polarisation in the row; band maxima read by this book from a 7-point running mean) | http://minerals.gps.caltech.edu/ |
| BSE | Basis Set Exchange (B. P. Pritchard et al., J. Chem. Inf. Model. 59 (2019) 4814), basis STO-3G (W. J. Hehre, R. F. Stewart and J. A. Pople, J. Chem. Phys. 51 (1969) 2657), version 1 | https://www.basissetexchange.org/ |
| IOFFE-NSM | Ioffe Institute, "New Semiconductor Materials. Characteristics and Properties" (NSM archive), band structure pages of Si, Ge, GaAs, GaN, GaP (basic parameters at 300 K, temperature dependences, donors and acceptors) | http://www.ioffe.ru/SVA/NSM/Semicond/ |
| IZA-DB | Structure Commission of the International Zeolite Association, Database of Zeolite Structures: framework pages (cell, framework density, largest diffusing sphere) and type-material pages (formula, channels) | https://europe.iza-structure.org/IZA-SC/ftc_table.php |
| SHANNON4 | R. D. Shannon, Acta Cryst. A32 (1976) 751, effective ionic radii, as tabulated in the Database of Ionic Radii (Imperial College), element pages | http://abulafia.mt.ic.ac.uk/shannon/radius.php |
| RCSB-PDB | RCSB Protein Data Bank: entries 2DN1 (oxy) and 2DN2 (deoxy) human haemoglobin at 1.25 A, S.-Y. Park et al., J. Mol. Biol. 360 (2006) 690; distances computed by this book from the HETATM coordinates of the haem groups | https://www.rcsb.org/ |
| BURCAT | A. Burcat and B. Ruscic, Extended Third Millennium Thermodynamic Database for Combustion and Air-Pollution Use with updates from Active Thermochemical Tables (file BURCAT.THR); the value used and its original reference are given in the row | https://respecth.elte.hu/burcat/BURCAT.THR |
| WEBBOOK-THERMO4 | NIST Chemistry WebBook (SRD 69), gas-phase thermochemistry data pages (value and reference in the row) | https://webbook.nist.gov/chemistry/ |
| IUPAC-PKA4 | J. W. Zheng and O. Lafontant-Joseph, IUPAC Digitized pKa Dataset v2.4a (from Serjeant and Dempsey 1979; Perrin 1965, 1972), CC BY-NC 4.0, file iupac_high-confidence_v2_4.csv; unique_ID and original reference code in the row | https://github.com/IUPAC/Dissociation-Constants |
| CCCBDB4 | NIST Computational Chemistry Comparison and Benchmark Database, SRD 101: experimental dipole moments (diplistx.asp; method code in the row) | https://cccbdb.nist.gov/diplistx.asp |
| NOAA-GML | NOAA Global Monitoring Laboratory, global annual mean mole fractions from the marine surface sites (files co2_annmean_gl.txt, ch4_annmean_gl.txt, n2o_annmean_gl.txt; uncertainty in the row) | https://gml.noaa.gov/ccgg/trends/ |
| IPCC-AR6-WG1 | IPCC, Climate Change 2021: The Physical Science Basis, Working Group I, Chapter 7 (Forster et al.), Table 7.15 | https://www.ipcc.ch/report/ar6/wg1/ |
| PHREEQC | D. L. Parkhurst and C. A. J. Appelo, PHREEQC database phreeqc.dat (USGS; log K at 25 C, original references in the file) | https://github.com/usgs-coupled/phreeqc3 |
| KUVEKE-2022 | R. E. Kuveke et al., An International Study Evaluating Elemental Analysis, ACS Cent. Sci. 8 (2022) 855, open access (PMC9335920), Table 1 of journal requirements | https://doi.org/10.1021/acscentsci.2c00325 |
| WILKINSON-2016 | M. D. Wilkinson et al., The FAIR Guiding Principles for scientific data management and stewardship, Sci. Data 3 (2016) 160018, open access (PMC4792175) | https://doi.org/10.1038/sdata.2016.18 |
| CODATA-2022-4 | NIST, CODATA 2022 recommended values of the fundamental physical constants (electron mass in u: 5.485799090441e-4) | https://physics.nist.gov/cuu/Constants/ |

## Rows

| id | quantity | value | unit | source | accessed |
|---|---|---|---|---|---|
| uvvis:cyanine | 1,1'-diethyl-2,2'-cyanine iodide, absorption maximum in ethanol | 524 | nm | PHOTOCHEMCAD | 2026-10-02 |
| uvvis:carbocyanine | 1,1'-diethyl-2,2'-carbocyanine iodide, absorption maximum in ethanol | 603 | nm | PHOTOCHEMCAD | 2026-10-02 |
| uvvis:dicarbocyanine | 1,1'-diethyl-2,2'-dicarbocyanine iodide, absorption maximum in ethanol | 711 | nm | PHOTOCHEMCAD | 2026-10-02 |
| diat:H2.we | H2 X state, harmonic wavenumber omega_e | 4401.213 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:H2.wexe | H2 X state, anharmonicity omega_e x_e | 121.336 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:H2.Be | H2 X state, rotational constant B_e | 60.8530 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:H2.ae | H2 X state, vibration-rotation constant alpha_e | 3.0622 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:D2.we | D2 X state, omega_e | 3115.50 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:D2.wexe | D2 X state, omega_e x_e | 61.82 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:D2.Be | D2 X state, B_e | 30.4436 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:D2.ae | D2 X state, alpha_e | 1.0786 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:HD.we | HD X state, omega_e | 3813.15 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:HD.wexe | HD X state, omega_e x_e | 91.65 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:HD.Be | HD X state, B_e | 45.655 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:HD.ae | HD X state, alpha_e | 1.986 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:HCl.we | H35Cl X state, omega_e | 2990.9463 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:HCl.wexe | H35Cl X state, omega_e x_e | 52.8186 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:HCl.Be | H35Cl X state, B_e | 10.593416 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:HCl.ae | H35Cl X state, alpha_e | 0.307181 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:HCl.De | H35Cl X state, centrifugal distortion constant D_e | 5.3194e-4 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:CO.we | 12C16O X state, omega_e | 2169.81358 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:CO.wexe | 12C16O X state, omega_e x_e | 13.28831 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:CO.Be | 12C16O X state, B_e | 1.93128087 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:CO.ae | 12C16O X state, alpha_e | 0.01750441 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:N2.we | N2 X state, omega_e | 2358.57 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:N2.wexe | N2 X state, omega_e x_e | 14.324 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:N2.Be | N2 X state, B_e | 1.998241 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:N2.ae | N2 X state, alpha_e | 0.017318 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:Cl2.we | 35Cl2 X state, omega_e | 559.72 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:Cl2.wexe | 35Cl2 X state, omega_e x_e | 2.675 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:Cl2.Be | 35Cl2 X state, B_e | 0.24399 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:Cl2.ae | 35Cl2 X state, alpha_e | 0.00149 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:I2.we | 127I2 X state, omega_e | 214.502 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:I2.wexe | 127I2 X state, omega_e x_e | 0.6147 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:I2.Be | 127I2 X state, B_e | 0.037372 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:I2.ae | 127I2 X state, alpha_e | 0.0001138 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:I2.re | 127I2 X state, equilibrium bond length | 2.6663 | angstrom | WEBBOOK-DIAT | 2026-10-02 |
| diat:I2B.Te | 127I2 B state (B 3Pi0+u), term value T_e | 15769.01 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:I2B.we | 127I2 B state, omega_e | 125.697 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:I2B.wexe | 127I2 B state, omega_e x_e | 0.7642 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:I2B.re | 127I2 B state, equilibrium bond length | 3.0247 | angstrom | WEBBOOK-DIAT | 2026-10-02 |
| diat:O2.we | O2 X 3Sigma-g state, omega_e | 1580.193 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:O2.Be | O2 X state, B_e | 1.4376766 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:NO.split | NO X 2Pi, spin-orbit splitting 2Pi3/2 - 2Pi1/2 (nu00 of the 3/2 <- 1/2 transition) | 119.73 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:NO.we | NO X state, omega_e | 1904.040 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| diat:NO.Be | NO X state, B_e | 1.72016 | cm-1 | WEBBOOK-DIAT | 2026-10-02 |
| codata:md | deuteron mass | 3.3435837768e-27 | kg | CODATA2022 | 2026-10-02 |
| lev:He.2s3S1 | He I 1s2s 3S1 level | 159855.9718 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:He.2s1S0 | He I 1s2s 1S0 level | 166277.4376 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:He.2p3P2 | He I 1s2p 3P2 level | 169086.7639 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:He.2p3P1 | He I 1s2p 3P1 level | 169086.8403 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:He.2p3P0 | He I 1s2p 3P0 level | 169087.8283 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:He.2p1P1 | He I 1s2p 1P1 level | 171134.8944 | cm-1 | ASD-LEVELS | 2026-10-02 |
| ie4:He2 | second ionisation energy of He (He II, hydrogen-like) | 54.4177655282 | eV | ASD-IE4 | 2026-10-02 |
| lev:C.3P1 | C I 2s2 2p2 3P1 level | 16.41671 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:C.3P2 | C I 2s2 2p2 3P2 level | 43.41346 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:C.1D2 | C I 2s2 2p2 1D2 level | 10192.657 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:C.1S0 | C I 2s2 2p2 1S0 level | 21648.030 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:N.2D5_2 | N I 2s2 2p3 2D5/2 level | 19224.464 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:N.2D3_2 | N I 2s2 2p3 2D3/2 level | 19233.177 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:N.2P1_2 | N I 2s2 2p3 2P1/2 level | 28838.920 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:N.2P3_2 | N I 2s2 2p3 2P3/2 level | 28839.306 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:O.3P1 | O I 2s2 2p4 3P1 level (ground 3P2) | 158.265 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:O.3P0 | O I 2s2 2p4 3P0 level (ground 3P2) | 226.977 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:O.1D2 | O I 2s2 2p4 1D2 level (ground 3P2) | 15867.862 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:O.1S0 | O I 2s2 2p4 1S0 level (ground 3P2) | 33792.583 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Na.3p1_2 | Na I 3p 2P1/2 level | 16956.17025 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Na.3p3_2 | Na I 3p 2P3/2 level | 16973.36619 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Ti2.3F3 | Ti III (Ti2+) 3d2 3F3 level (ground 3F2) | 184.9 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Ti2.3F4 | Ti III (Ti2+) 3d2 3F4 level (ground 3F2) | 420.4 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Ti2.1D2 | Ti III (Ti2+) 3d2 1D2 level (ground 3F2) | 8473.5 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Ti2.3P0 | Ti III (Ti2+) 3d2 3P0 level (ground 3F2) | 10538.4 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Ti2.3P1 | Ti III (Ti2+) 3d2 3P1 level (ground 3F2) | 10603.6 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Ti2.3P2 | Ti III (Ti2+) 3d2 3P2 level (ground 3F2) | 10721.2 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Ti2.1G4 | Ti III (Ti2+) 3d2 1G4 level (ground 3F2) | 14397.6 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Ti2.1S0 | Ti III (Ti2+) 3d2 1S0 level (ground 3F2) | 32475.5 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:V2.4F5_2 | V III (V2+) 3d3 4F5/2 level (ground 4F3/2) | 145.5 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:V2.4F7_2 | V III (V2+) 3d3 4F7/2 level (ground 4F3/2) | 341.5 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:V2.4F9_2 | V III (V2+) 3d3 4F9/2 level (ground 4F3/2) | 583.8 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:V2.4P1_2 | V III (V2+) 3d3 4P1/2 level (ground 4F3/2) | 11513.8 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:V2.4P3_2 | V III (V2+) 3d3 4P3/2 level (ground 4F3/2) | 11591.8 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:V2.4P5_2 | V III (V2+) 3d3 4P5/2 level (ground 4F3/2) | 11769.7 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Cr3.4F5_2 | Cr IV (Cr3+) 3d3 4F5/2 level (ground 4F3/2) | 237.4 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Cr3.4F7_2 | Cr IV (Cr3+) 3d3 4F7/2 level (ground 4F3/2) | 556.4 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Cr3.4F9_2 | Cr IV (Cr3+) 3d3 4F9/2 level (ground 4F3/2) | 945.5 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Cr3.4P1_2 | Cr IV (Cr3+) 3d3 4P1/2 level (ground 4F3/2) | 14059.9 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Cr3.4P3_2 | Cr IV (Cr3+) 3d3 4P3/2 level (ground 4F3/2) | 14177.5 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Cr3.4P5_2 | Cr IV (Cr3+) 3d3 4P5/2 level (ground 4F3/2) | 14472.2 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Cr3.2G7_2 | Cr IV (Cr3+) 3d3 2G7/2 level (ground 4F3/2) | 15053.6 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Cr3.2G9_2 | Cr IV (Cr3+) 3d3 2G9/2 level (ground 4F3/2) | 15402.4 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Ni2.3F3 | Ni III (Ni2+) 3d8 3F3 level (ground 3F4) | 1360.7 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Ni2.3F2 | Ni III (Ni2+) 3d8 3F2 level (ground 3F4) | 2269.6 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Ni2.1D2 | Ni III (Ni2+) 3d8 1D2 level (ground 3F4) | 14031.6 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Ni2.3P2 | Ni III (Ni2+) 3d8 3P2 level (ground 3F4) | 16661.6 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Ni2.3P1 | Ni III (Ni2+) 3d8 3P1 level (ground 3F4) | 16977.8 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Ni2.3P0 | Ni III (Ni2+) 3d8 3P0 level (ground 3F4) | 17230.7 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Ni2.1G4 | Ni III (Ni2+) 3d8 1G4 level (ground 3F4) | 23108.7 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:Fe2.ground | Fe III (Fe2+) 3d6 ground level | 5D4 | - | ASD-LEVELS | 2026-10-02 |
| lev:Co2.ground | Co III (Co2+) 3d7 ground level | 4F9/2 | - | ASD-LEVELS | 2026-10-02 |
| lev:Cu2.ground | Cu III (Cu2+) 3d9 ground level | 2D5/2 | - | ASD-LEVELS | 2026-10-02 |
| lev:Cl.2P1_2 | Cl I 3p5 2P1/2 level (ground 2P3/2) | 882.3515 | cm-1 | ASD-LEVELS | 2026-10-02 |
| lev:I.2P1_2 | I I 5p5 2P1/2 level (ground 2P3/2) | 7602.9762 | cm-1 | ASD-LEVELS | 2026-10-02 |
| janaf:H.dfH0 | standard enthalpy of formation of H(g) at 0 K (JANAF H-001, T = 0 row) | 216.035 | kJ/mol | JANAF4 | 2026-10-02 |
| bse:H.sto3g.a1 | STO-3G hydrogen 1s, exponent 1 (zeta = 1.24) | 3.42525091 | bohr-2 | BSE | 2026-10-02 |
| bse:H.sto3g.a2 | STO-3G hydrogen 1s, exponent 2 | 0.62391373 | bohr-2 | BSE | 2026-10-02 |
| bse:H.sto3g.a3 | STO-3G hydrogen 1s, exponent 3 | 0.16885540 | bohr-2 | BSE | 2026-10-02 |
| bse:sto3g.c1 | STO-3G 1s contraction coefficient 1 (H and He) | 0.15432897 | - | BSE | 2026-10-02 |
| bse:sto3g.c2 | STO-3G 1s contraction coefficient 2 | 0.53532814 | - | BSE | 2026-10-02 |
| bse:sto3g.c3 | STO-3G 1s contraction coefficient 3 | 0.44463454 | - | BSE | 2026-10-02 |
| bse:He.sto3g.a1 | STO-3G helium 1s, exponent 1 (zeta = 1.69) | 6.36242139 | bohr-2 | BSE | 2026-10-02 |
| bse:He.sto3g.a2 | STO-3G helium 1s, exponent 2 | 1.15892300 | bohr-2 | BSE | 2026-10-02 |
| bse:He.sto3g.a3 | STO-3G helium 1s, exponent 3 | 0.31364979 | bohr-2 | BSE | 2026-10-02 |
| ie4:H2 | adiabatic ionisation energy of H2 (evaluation by Shiner, Gilligan et al. 1993) | 15.42593 | eV | WEBBOOK-IEMOL4 | 2026-10-02 |
| hist4:HeHp.2019 | first astrophysical detection of HeH+ (planetary nebula NGC 7027), year of publication | 2019 | year | GUSTEN-2019 | 2026-10-02 |
| pa:He | proton affinity of He (enthalpy, 298 K; review by Hunter and Lias 1998) | 177.8 | kJ/mol | WEBBOOK-IEMOL4 | 2026-10-02 |
| ct:C2v | character table of C2v, as printed (value = order of the group) | 4 | - | KATZER | 2026-10-02 |
| ct:C3v | character table of C3v, as printed (value = order of the group) | 6 | - | KATZER | 2026-10-02 |
| ct:Td | character table of Td, as printed (value = order of the group) | 24 | - | KATZER | 2026-10-02 |
| ct:D3h | character table of D3h, as printed (value = order of the group) | 12 | - | KATZER | 2026-10-02 |
| ct:Oh | character table of Oh, as printed (value = order of the group) | 48 | - | KATZER | 2026-10-02 |
| ct:D2h | character table of D2h, as printed (value = order of the group) | 8 | - | KATZER | 2026-10-02 |
| ct:C2h | character table of C2h, as printed (value = order of the group) | 4 | - | KATZER | 2026-10-02 |
| ct:D4h | character table of D4h, as printed (value = order of the group) | 16 | - | KATZER | 2026-10-02 |
| vib:H2O.sym | H2O gas, symmetric stretch (a1) fundamental | 3657 | cm-1 | WEBBOOK-VIB | 2026-10-02 |
| vib:H2O.bend | H2O gas, bend (a1) fundamental | 1595 | cm-1 | WEBBOOK-VIB | 2026-10-02 |
| vib:H2O.asym | H2O gas, antisymmetric stretch fundamental (b1 with the molecule in the xz plane) | 3756 | cm-1 | WEBBOOK-VIB | 2026-10-02 |
| vib:NH3.sym | NH3 gas, symmetric stretch (a1) | 3337 | cm-1 | WEBBOOK-VIB | 2026-10-02 |
| vib:NH3.umbrella | NH3 gas, symmetric deformation (a1, umbrella), mean of the inversion doublet 932.5/968.3 | 950 | cm-1 | WEBBOOK-VIB | 2026-10-02 |
| vib:NH3.degstr | NH3 gas, degenerate stretch (e) | 3444 | cm-1 | WEBBOOK-VIB | 2026-10-02 |
| vib:NH3.degdef | NH3 gas, degenerate deformation (e) | 1627 | cm-1 | WEBBOOK-VIB | 2026-10-02 |
| vib:CH4.nu1 | CH4 gas, symmetric stretch (a1), Raman only | 2917 | cm-1 | WEBBOOK-VIB | 2026-10-02 |
| vib:CH4.nu2 | CH4 gas, degenerate deformation (e), Raman | 1534 | cm-1 | WEBBOOK-VIB | 2026-10-02 |
| vib:CH4.nu3 | CH4 gas, degenerate stretch (f2) | 3019 | cm-1 | WEBBOOK-VIB | 2026-10-02 |
| vib:CH4.nu4 | CH4 gas, degenerate deformation (f2) | 1306 | cm-1 | WEBBOOK-VIB | 2026-10-02 |
| vib:CO2.sym | CO2, symmetric stretch (Sigma g+), unperturbed value (Herzberg 1945), Raman active | 1333 | cm-1 | CCCBDB | 2026-10-02 |
| vib:CO2.asym | CO2, antisymmetric stretch (Sigma u+) fundamental (Herzberg 1945) | 2349 | cm-1 | CCCBDB | 2026-10-02 |
| vib:CO2.bend | CO2, bend (Pi u) fundamental (Herzberg 1945) | 667 | cm-1 | CCCBDB | 2026-10-02 |
| ir:CO2.asym.int | CO2, infrared intensity of the antisymmetric stretch (1969 Davies and Oreski, via CCCBDB) | 665.0 | km/mol | CCCBDB | 2026-10-02 |
| ir:CO2.bend.int | CO2, infrared intensity of the bend (1982 compilation, via CCCBDB) | 54.2 | km/mol | CCCBDB | 2026-10-02 |
| imass:H1 | relative atomic mass of hydrogen-1 | 1.00782503223 | u | NIST-AWIC | 2026-10-02 |
| imass:H2 | relative atomic mass of hydrogen-2 (deuterium) | 2.01410177812 | u | NIST-AWIC | 2026-10-02 |
| imass:C13 | relative atomic mass of carbon-13 (carbon-12 is 12 exactly) | 13.00335483507 | u | NIST-AWIC | 2026-10-02 |
| imass:N14 | relative atomic mass of nitrogen-14 | 14.00307400443 | u | NIST-AWIC | 2026-10-02 |
| imass:O16 | relative atomic mass of oxygen-16 | 15.99491461957 | u | NIST-AWIC | 2026-10-02 |
| imass:Cl35 | relative atomic mass of chlorine-35 | 34.968852682 | u | NIST-AWIC | 2026-10-02 |
| imass:Cl37 | relative atomic mass of chlorine-37 | 36.965902602 | u | NIST-AWIC | 2026-10-02 |
| rotl:CO.1-0 | 12C16O, rest frequency of the J = 1 <- 0 rotational line | 115271.2018 | MHz | CDMS | 2026-10-02 |
| rotl:CO.2-1 | 12C16O, J = 2 <- 1 | 230538.0000 | MHz | CDMS | 2026-10-02 |
| rotl:CO.3-2 | 12C16O, J = 3 <- 2 | 345795.9899 | MHz | CDMS | 2026-10-02 |
| rotl:13CO.1-0 | 13C16O, J = 1 <- 0 | 110201.3543 | MHz | CDMS | 2026-10-02 |
| janaf:Cl.dfH0 | standard enthalpy of formation of Cl(g) at 0 K (JANAF Cl-001, T = 0 row) | 119.621 | kJ/mol | JANAF4 | 2026-10-02 |
| janaf:HCl.dfH0 | standard enthalpy of formation of HCl(g) at 0 K (JANAF Cl-026, T = 0 row) | -92.127 | kJ/mol | JANAF4 | 2026-10-02 |
| fl:quinine.labs | quinine sulfate in 0.5 M H2SO4, absorption maximum | 349 | nm | PHOTOCHEMCAD | 2026-10-03 |
| fl:quinine.eps | quinine sulfate in 0.5 M H2SO4, molar absorption coefficient at 349 nm | 5700 | L mol-1 cm-1 | PHOTOCHEMCAD | 2026-10-03 |
| fl:quinine.phi | quinine sulfate in 0.5 M H2SO4, fluorescence quantum yield (literature value compiled in the database) | 0.546 | - | PHOTOCHEMCAD | 2026-10-03 |
| fl:anthracene.labs | anthracene in cyclohexane, absorption maximum (longest-wavelength band) | 356 | nm | PHOTOCHEMCAD | 2026-10-03 |
| fl:anthracene.eps | anthracene in cyclohexane, molar absorption coefficient at 356 nm | 9700 | L mol-1 cm-1 | PHOTOCHEMCAD | 2026-10-03 |
| fl:anthracene.phi | anthracene in cyclohexane, fluorescence quantum yield | 0.36 | - | PHOTOCHEMCAD | 2026-10-03 |
| visc:H2O.25C | viscosity of liquid water at 298.15 K, 0.1 MPa (Huber et al. 2009, IAPWS formulation) | 0.89002 | mPa s | WEBBOOK-FLUID | 2026-10-03 |
| visc:hexane.25C | viscosity of liquid n-hexane at 298.15 K, 0.1 MPa (Michailidou et al. 2013) | 0.29796 | mPa s | WEBBOOK-FLUID | 2026-10-03 |
| imass:I127 | relative atomic mass of iodine-127 | 126.9044719 | u | NIST-AWIC | 2026-10-03 |
| nuc:C13.mu | carbon-13, ground state I = 1/2, magnetic moment | 0.7024118 | nuclear magneton | IAEA-NUC | 2026-10-03 |
| nuc:N15.mu | nitrogen-15, ground state I = 1/2, magnetic moment | -0.28318884 | nuclear magneton | IAEA-NUC | 2026-10-03 |
| nuc:N14.mu | nitrogen-14, ground state I = 1, magnetic moment | 0.40376100 | nuclear magneton | IAEA-NUC | 2026-10-03 |
| nuc:F19.mu | fluorine-19, ground state I = 1/2, magnetic moment | 2.628868 | nuclear magneton | IAEA-NUC | 2026-10-03 |
| nuc:P31.mu | phosphorus-31, ground state I = 1/2, magnetic moment | 1.13160 | nuclear magneton | IAEA-NUC | 2026-10-03 |
| iso4:N15 | isotopic composition of nitrogen-15 in natural nitrogen | 0.00364 | - | NIST-AWIC | 2026-10-03 |
| c13:ethylbutanoate.CO | ethyl butanoate, 13C shift of C=O, CDCl3, 25.16 MHz (PubChem CID 7762, SpectraBase spectrum 4031) | 173.61 | ppm | PUBCHEM4 | 2026-10-03 |
| c13:ethylbutanoate.OCH2 | ethyl butanoate, 13C shift of OCH2, same spectrum | 60.13 | ppm | PUBCHEM4 | 2026-10-03 |
| c13:ethylbutanoate.CH2CO | ethyl butanoate, 13C shift of CH2C=O, same spectrum | 36.32 | ppm | PUBCHEM4 | 2026-10-03 |
| c13:ethylbutanoate.CH2 | ethyl butanoate, 13C shift of the central CH2 of the butanoyl chain, same spectrum | 18.57 | ppm | PUBCHEM4 | 2026-10-03 |
| c13:ethylbutanoate.OCH2CH3 | ethyl butanoate, 13C shift of OCH2CH3, same spectrum (assignment: the higher of the two methyl signals) | 14.32 | ppm | PUBCHEM4 | 2026-10-03 |
| c13:ethylbutanoate.CH3 | ethyl butanoate, 13C shift of the butanoyl CH3, same spectrum | 13.70 | ppm | PUBCHEM4 | 2026-10-03 |
| xray:CuKa1 | Cu K alpha 1 (K-L3) X-ray wavelength, experimental | 1.5405929 | angstrom | NIST-XRAY | 2026-10-03 |
| xray:CuKa2 | Cu K alpha 2 (K-L2) X-ray wavelength, experimental | 1.5444274 | angstrom | NIST-XRAY | 2026-10-03 |
| lat:KCl | lattice parameter a of potassium chloride (sylvite), rock-salt type (COD 9008651, Wyckoff 1963) | 6.29294 | angstrom | COD4 | 2026-10-03 |
| lat:KBr | lattice parameter a of potassium bromide, rock-salt type (COD 9009734, Ahtee 1969) | 6.5847 | angstrom | COD4 | 2026-10-03 |
| s0:I2_g | standard molar entropy of I2(g) at 298.15 K, 1 bar (uncertainty 0.005) | 260.687 | J/(K.mol) | CODATA-KEY4 | 2026-10-03 |
| s0:Cl_g | standard molar entropy of Cl(g) at 298.15 K, 1 bar (uncertainty 0.004) | 165.190 | J/(K.mol) | CODATA-KEY4 | 2026-10-03 |
| s0:Kr_g | standard molar entropy of Kr(g) at 298.15 K, 1 bar (uncertainty 0.003) | 164.085 | J/(K.mol) | CODATA-KEY4 | 2026-10-03 |
| s0:Ne_g | standard molar entropy of Ne(g) at 298.15 K, 1 bar (uncertainty 0.003) | 146.328 | J/(K.mol) | CODATA-KEY4 | 2026-10-03 |
| diat:H2.De | H2 X state, centrifugal distortion constant D_e | 0.0471 | cm-1 | WEBBOOK-DIAT | 2026-10-03 |
| janaf:I.dfH0 | standard enthalpy of formation of I(g) at 0 K (JANAF I-001, T = 0 row) | 107.164 | kJ/mol | JANAF4 | 2026-10-03 |
| janaf:I2g.dfH0 | standard enthalpy of formation of I2(g) at 0 K (JANAF I-027, T = 0 row) | 65.504 | kJ/mol | JANAF4 | 2026-10-03 |
| janaf:I.logKf.800 | log10 Kf of I(g) at 800 K (JANAF I-001; reference state I2(g) above 457.67 K) | -2.258 | -- | JANAF4 | 2026-10-03 |
| janaf:I.logKf.1000 | log10 Kf of I(g) at 1000 K (JANAF I-001; reference state I2(g) above 457.67 K) | -1.256 | -- | JANAF4 | 2026-10-03 |
| janaf:I.logKf.1200 | log10 Kf of I(g) at 1200 K (JANAF I-001; reference state I2(g) above 457.67 K) | -0.584 | -- | JANAF4 | 2026-10-03 |
| janaf:I.logKf.1500 | log10 Kf of I(g) at 1500 K (JANAF I-001; reference state I2(g) above 457.67 K) | 0.090 | -- | JANAF4 | 2026-10-03 |
| janaf:N2.Cp.100 | Cp of N2(g) at 100 K (JANAF N-023) | 29.104 | J/(K.mol) | JANAF4 | 2026-10-03 |
| janaf:N2.Cp.200 | Cp of N2(g) at 200 K (JANAF N-023) | 29.107 | J/(K.mol) | JANAF4 | 2026-10-03 |
| janaf:N2.Cp.300 | Cp of N2(g) at 300 K (JANAF N-023) | 29.125 | J/(K.mol) | JANAF4 | 2026-10-03 |
| janaf:N2.Cp.500 | Cp of N2(g) at 500 K (JANAF N-023) | 29.580 | J/(K.mol) | JANAF4 | 2026-10-03 |
| janaf:N2.Cp.1000 | Cp of N2(g) at 1000 K (JANAF N-023) | 32.697 | J/(K.mol) | JANAF4 | 2026-10-03 |
| janaf:N2.Cp.1500 | Cp of N2(g) at 1500 K (JANAF N-023) | 34.843 | J/(K.mol) | JANAF4 | 2026-10-03 |
| janaf:N2.Cp.2000 | Cp of N2(g) at 2000 K (JANAF N-023) | 35.971 | J/(K.mol) | JANAF4 | 2026-10-03 |
| janaf:N2.Cp.3000 | Cp of N2(g) at 3000 K (JANAF N-023) | 37.030 | J/(K.mol) | JANAF4 | 2026-10-03 |
| janaf:Cl2.Cp.100 | Cp of Cl2(g) at 100 K (JANAF Cl-073) | 29.299 | J/(K.mol) | JANAF4 | 2026-10-03 |
| janaf:Cl2.Cp.200 | Cp of Cl2(g) at 200 K (JANAF Cl-073) | 31.720 | J/(K.mol) | JANAF4 | 2026-10-03 |
| janaf:Cl2.Cp.300 | Cp of Cl2(g) at 300 K (JANAF Cl-073) | 33.981 | J/(K.mol) | JANAF4 | 2026-10-03 |
| janaf:Cl2.Cp.500 | Cp of Cl2(g) at 500 K (JANAF Cl-073) | 36.064 | J/(K.mol) | JANAF4 | 2026-10-03 |
| janaf:Cl2.Cp.1000 | Cp of Cl2(g) at 1000 K (JANAF Cl-073) | 37.438 | J/(K.mol) | JANAF4 | 2026-10-03 |
| janaf:Cl2.Cp.1500 | Cp of Cl2(g) at 1500 K (JANAF Cl-073) | 37.954 | J/(K.mol) | JANAF4 | 2026-10-03 |
| janaf:Cl2.Cp.2000 | Cp of Cl2(g) at 2000 K (JANAF Cl-073) | 38.428 | J/(K.mol) | JANAF4 | 2026-10-03 |
| janaf:Cl2.Cp.3000 | Cp of Cl2(g) at 3000 K (JANAF Cl-073) | 40.075 | J/(K.mol) | JANAF4 | 2026-10-03 |
| hvap:nH2 | enthalpy of vaporisation of normal hydrogen at 1.01325 bar (saturation data, Leachman et al. 2009 equation of state) | 0.905 | kJ/mol | WEBBOOK-FLUID | 2026-10-03 |
| tb:nH2 | normal boiling point of normal hydrogen (saturation pressure 1.01325 bar) | 20.37 | K | WEBBOOK-FLUID | 2026-10-03 |
| hvap:pH2 | enthalpy of vaporisation of parahydrogen at 1.01325 bar (saturation data, Leachman et al. 2009 equation of state) | 0.899 | kJ/mol | WEBBOOK-FLUID | 2026-10-03 |
| tb:pH2 | normal boiling point of parahydrogen (saturation pressure 1.01325 bar) | 20.27 | K | WEBBOOK-FLUID | 2026-10-03 |
| diat:H2.re | H2 X state, equilibrium bond length | 0.74144 | angstrom | WEBBOOK-DIAT | 2026-10-03 |
| vib:CD4.nu1 | CD4 gas, symmetric stretch (a1), Raman only | 2109 | cm-1 | WEBBOOK-VIB | 2026-10-03 |
| vib:CD4.nu3 | CD4 gas, degenerate stretch (f2) | 2259 | cm-1 | WEBBOOK-VIB | 2026-10-03 |
| kin:NO+O3.A | NO + O3 -> NO2 + O2, pre-exponential factor of the preferred expression k = A exp(-E/RT) (datasheet NOx24, evaluated 2013, valid 195-310 K) | 2.07e-12 | cm3 molecule-1 s-1 | IUPAC-ATMOS | 2026-10-03 |
| kin:NO+O3.EaR | NO + O3, E/R of the preferred expression (uncertainty +-200 K) | 1400 | K | IUPAC-ATMOS | 2026-10-03 |
| kin:NO+O3.k298 | NO + O3, preferred k at 298 K (uncertainty +-0.07 in log k) | 1.9e-14 | cm3 molecule-1 s-1 | IUPAC-ATMOS | 2026-10-03 |
| hist4:deut.2017 | year of approval of the first deuterated drug (deutetrabenazine, two OCD3 groups in place of the OCH3 groups of tetrabenazine) | 2017 | -- | PMC-DEUT | 2026-10-03 |
| ghs4:Br2 | bromine (CID 24408): pictograms of the aggregated classification; H314, H330, H400 | GHS05 GHS06 GHS09 | -- | PUBCHEM4 | 2026-10-03 |
| enz:median.kcatKM | k_cat/K_M of the "average enzyme" in a survey of several thousand enzymes (order of magnitude) | 1e5 | L mol-1 s-1 | BAR-EVEN-2011 | 2026-10-03 |
| kin:O+O2+M.k0 | O + O2 + M -> O3 + M, low-pressure rate coefficient k0 = 6.0e-34 (T/300)^-2.6 [M] in air (datasheet Ox1, evaluated 2009, 200-300 K) | 6.0e-34 | cm6 molecule-2 s-1 | IUPAC-ATMOS | 2026-10-03 |
| kin:O+O2+M.n | O + O2 + M, temperature exponent of k0 (T/300)^-n | 2.6 | -- | IUPAC-ATMOS | 2026-10-03 |
| kin:O+O3.A | O + O3 -> 2 O2, k = A exp(-E/RT) (datasheet Ox2, evaluated 2001, 200-400 K) | 8.0e-12 | cm3 molecule-1 s-1 | IUPAC-ATMOS | 2026-10-03 |
| kin:O+O3.EaR | O + O3, E/R (uncertainty +-200 K) | 2060 | K | IUPAC-ATMOS | 2026-10-03 |
| kin:Cl+O3.A | Cl + O3 -> ClO + O2, A (datasheet iClOx14, evaluated 2003, 180-300 K) | 2.8e-11 | cm3 molecule-1 s-1 | IUPAC-ATMOS | 2026-10-03 |
| kin:Cl+O3.EaR | Cl + O3, E/R (uncertainty +-150 K) | 250 | K | IUPAC-ATMOS | 2026-10-03 |
| kin:O+ClO.A | O + ClO -> Cl + O2, A (datasheet iClOx2, evaluated 2003, 220-390 K) | 2.5e-11 | cm3 molecule-1 s-1 | IUPAC-ATMOS | 2026-10-03 |
| kin:O+ClO.EaR | O + ClO, E/R (negative: k = A exp(110/T)) | -110 | K | IUPAC-ATMOS | 2026-10-03 |
| kin:Cl+CH4.A | Cl + CH4 -> HCl + CH3, A (datasheet X_VOC2, evaluated 2002, 200-300 K) | 6.6e-12 | cm3 molecule-1 s-1 | IUPAC-ATMOS | 2026-10-03 |
| kin:Cl+CH4.EaR | Cl + CH4, E/R (uncertainty +-200 K) | 1240 | K | IUPAC-ATMOS | 2026-10-03 |
| kin:ClO+NO2+M.k0 | ClO + NO2 + M -> ClONO2 + M, low-pressure limit k0 = 1.6e-31 (T/300)^-3.4 [M], air (datasheet iClOx32, evaluated 2005; k_inf 7.0e-11, Fc 0.4) | 1.6e-31 | cm6 molecule-2 s-1 | IUPAC-ATMOS | 2026-10-03 |
| kin:ClO+NO2+M.n | ClO + NO2 + M, temperature exponent of k0 | 3.4 | -- | IUPAC-ATMOS | 2026-10-03 |
| kin:ClO+NO2+M.kinf | ClO + NO2 + M, high-pressure limit | 7.0e-11 | cm3 molecule-1 s-1 | IUPAC-ATMOS | 2026-10-03 |
| kin:ClO+NO2+M.Fc | ClO + NO2 + M, broadening factor Fc | 0.4 | -- | IUPAC-ATMOS | 2026-10-03 |
| kin:O+NO2.A | O + NO2 -> O2 + NO, A (datasheet NOx2, evaluated 2009, 220-420 K) | 5.1e-12 | cm3 molecule-1 s-1 | IUPAC-ATMOS | 2026-10-03 |
| kin:O+NO2.EaR | O + NO2, E/R (k = A exp(198/T)) | -198 | K | IUPAC-ATMOS | 2026-10-03 |
| janaf:O.dfH0 | standard enthalpy of formation of O(g) at 0 K (JANAF O-001, T = 0 row) | 246.790 | kJ/mol | JANAF4 | 2026-10-03 |
| janaf:O3.dfH0 | standard enthalpy of formation of O3(g) at 0 K (JANAF O-056, T = 0 row) | 145.348 | kJ/mol | JANAF4 | 2026-10-03 |
| oz:column.mean | average total ozone column over the Earth | 300 | DU | NASA-OZONE | 2026-10-03 |
| oz:column.hole | average ozone column inside the Antarctic ozone hole | 100 | DU | NASA-OZONE | 2026-10-03 |
| oz:DU | ozone molecules per cm2 in a column of 1 Dobson unit (a layer 0.01 mm thick at standard conditions) | 2.69e16 | cm-2 | NASA-OZONE | 2026-10-03 |
| hist4:retinal.fs | time in which the 11-cis to all-trans isomerisation of the retinal of rhodopsin is essentially complete | 200 | fs | SCHOENLEIN-1991 | 2026-10-03 |
| ghs4:benzophenone | benzophenone (CID 3102): pictograms of the aggregated classification; H350, H373, H411 | GHS08 GHS09 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:PbNO32 | lead(II) nitrate (CID 24924): pictograms of the aggregated classification; H272, H302, H317, H318, H332, H351, H360, H373, H410 | GHS03 GHS05 GHS07 GHS08 GHS09 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:K3FeCN6 | potassium hexacyanoferrate(III) (CID 26250): pictograms of the aggregated classification; H302, H315, H319, H335, H361, H411 | GHS07 GHS08 GHS09 | -- | PUBCHEM4 | 2026-10-03 |
| eps:H2O.25C | relative permittivity (static dielectric constant) of liquid water at 298.15 K, 0.1 MPa (IAPWS R8-97 evaluated at the density 997.047 kg/m3 of the NIST WebBook fluid data; stated uncertainty of the formulation about 0.04) | 78.4 | -- | IAPWS-R8-97 | 2026-10-03 |
| sa:N2.am | cross-sectional area of an adsorbed N2 molecule in a close-packed BET monolayer at 77 K (conventional value) | 0.162 | nm2 | NIST-SP960-17 | 2026-10-03 |
| lat:Pt | lattice parameter of platinum (fcc, Fm-3m), room temperature (COD 9008480, Wyckoff; COD 4334349 gives 3.9218 A) | 3.923 | angstrom | COD4 | 2026-10-03 |
| ghs4:V2O5 | vanadium(V) oxide (CID 14814): pictograms of the aggregated classification; H301, H330, H335, H341, H350, H361, H372, H411 | GHS06 GHS08 GHS09 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:Ni | nickel (CID 935), the metal of nickel catalysts: pictograms; H317, H351, H372 | GHS07 GHS08 | -- | PUBCHEM4 | 2026-10-03 |
| st:H2O.25C | surface tension of water at 25 degC (calculated 71.97, experimental 71.98 +- 0.36 mN/m) | 72.0 | mN/m | IAPWS-R1-76 | 2026-10-03 |
| cmc:SDS | CMC of sodium dodecyl sulfate in water at 25 degC (compound 1; 8.1-8.4 mM by several methods, 8.2 from the best-rated surface-tension value) | 8.2e-3 | mol/L | NSRDS-NBS36 | 2026-10-03 |
| cmc:CTAB | CMC of hexadecyltrimethylammonium bromide in water at 25 degC (compound 99, molal) | 9.2e-4 | mol/kg | NSRDS-NBS36 | 2026-10-03 |
| cmc:C12E6 | CMC of hexaethylene glycol monododecyl ether (dodecyl/oxyethylene/6 alcohol, homogeneous head group) at 25 degC (compound 110) | 8.7e-5 | mol/L | NSRDS-NBS36 | 2026-10-03 |
| ghs4:SDS | sodium dodecyl sulfate (CID 3423265): pictograms of the aggregated classification; H228, H302, H315, H318, H335, H412 | GHS02 GHS05 GHS07 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:Al2SO43 | aluminium sulfate (CID 24850): pictogram; H290, H318 | GHS05 | -- | PUBCHEM4 | 2026-10-03 |
| lf:ruby.nu1 | ruby (corundum with Cr3+, GRR 1843, 0.787 mm, E perp c): maximum of the 4A2g -> 4T2g band | 17820 | cm-1 | CALTECH-MS | 2026-10-03 |
| lf:ruby.nu2 | ruby, GRR 1843, E perp c: maximum of the 4A2g -> 4T1g(F) band | 24170 | cm-1 | CALTECH-MS | 2026-10-03 |
| lf:emerald.nu1 | emerald (synthetic flux-grown beryl with Cr3+, RDS 65674, 0.756 mm, E perp c): maximum of the 4A2g -> 4T2g band | 16740 | cm-1 | CALTECH-MS | 2026-10-03 |
| lf:emerald.nu2 | emerald, RDS 65674, E perp c: maximum of the 4A2g -> 4T1g(F) band | 23040 | cm-1 | CALTECH-MS | 2026-10-03 |
| lf:ruby.Rline | ruby: wavelength of the sharp spin-forbidden band (R line, 2Eg <-> 4A2g), "near 695 nm" | 695 | nm | CALTECH-MS | 2026-10-03 |
| ghs4:K2PtCl4 | potassium tetrachloroplatinate(II) (CID 61440): pictograms of the aggregated classification; H301, H315, H317, H318, H334 | GHS05 GHS06 GHS08 | -- | PUBCHEM4 | 2026-10-03 |
| geom:Re2Cl8.ReRe | Re-Re distance in K2[Re2Cl8].2H2O, computed by this book from the atomic coordinates of COD 4344219 (Cotton and Harris, Inorg. Chem. 4 (1965) 330) | 2.24 | angstrom | COD4 | 2026-10-03 |
| ghs4:NiCO4 | nickel tetracarbonyl (CID 26039): pictograms; H225, H330, H351, H360D, H400, H410 | GHS02 GHS06 GHS08 GHS09 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:ferrocene | ferrocene (CID 10219726): pictograms of the aggregated classification; H228, H302 (and minority H332, H360, H373, H410) | GHS02 GHS07 GHS08 GHS09 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:MeI | iodomethane (CID 6328): pictograms; H301, H312, H315, H331, H335, H351 | GHS06 GHS08 | -- | PUBCHEM4 | 2026-10-03 |
| eg:Si | band gap of silicon at 300 K (indirect) | 1.12 | eV | IOFFE-NSM | 2026-10-03 |
| eg:Ge | band gap of germanium at 300 K (indirect; basic-parameter table 0.661) | 0.66 | eV | IOFFE-NSM | 2026-10-03 |
| eg:GaAs | band gap of gallium arsenide at 300 K (direct) | 1.42 | eV | IOFFE-NSM | 2026-10-03 |
| eg:GaN | band gap of wurtzite gallium nitride at 300 K (direct; the page lists 3.39 and 3.44 eV) | 3.4 | eV | IOFFE-NSM | 2026-10-03 |
| eg:GaP | band gap of gallium phosphide at 300 K (indirect) | 2.26 | eV | IOFFE-NSM | 2026-10-03 |
| eg:Si.E0 | Varshni fit of the gap of Si, Eg = E0 - a T^2/(T + b): E0 | 1.17 | eV | IOFFE-NSM | 2026-10-03 |
| eg:Si.a | Varshni fit of the gap of Si: a | 4.73e-4 | eV/K | IOFFE-NSM | 2026-10-03 |
| eg:Si.b | Varshni fit of the gap of Si: b | 636 | K | IOFFE-NSM | 2026-10-03 |
| eg:Ge.E0 | Varshni fit of the gap of Ge: E0 | 0.742 | eV | IOFFE-NSM | 2026-10-03 |
| eg:Ge.a | Varshni fit of the gap of Ge: a | 4.8e-4 | eV/K | IOFFE-NSM | 2026-10-03 |
| eg:Ge.b | Varshni fit of the gap of Ge: b | 235 | K | IOFFE-NSM | 2026-10-03 |
| dos:Si.Nc | effective density of states of the conduction band of Si, Nc = 6.2e15 T^1.5 (coefficient) | 6.2e15 | cm-3 K-1.5 | IOFFE-NSM | 2026-10-03 |
| dos:Si.Nv | effective density of states of the valence band of Si, Nv = 3.5e15 T^1.5 (coefficient) | 3.5e15 | cm-3 K-1.5 | IOFFE-NSM | 2026-10-03 |
| dos:Ge.Nc | effective density of states of the conduction band of Ge (coefficient of T^1.5) | 1.98e15 | cm-3 K-1.5 | IOFFE-NSM | 2026-10-03 |
| dos:Ge.Nv | effective density of states of the valence band of Ge (coefficient of T^1.5) | 9.6e14 | cm-3 K-1.5 | IOFFE-NSM | 2026-10-03 |
| ni:Si | intrinsic carrier concentration of Si at 300 K | 1e10 | cm-3 | IOFFE-NSM | 2026-10-03 |
| ni:Ge | intrinsic carrier concentration of Ge at 300 K | 2.0e13 | cm-3 | IOFFE-NSM | 2026-10-03 |
| dop:Si.P | ionisation energy of the phosphorus donor in Si | 0.045 | eV | IOFFE-NSM | 2026-10-03 |
| dop:Si.B | ionisation energy of the boron acceptor in Si | 0.045 | eV | IOFFE-NSM | 2026-10-03 |
| trans:AgI | beta (hexagonal) to alpha (cubic, superionic) transition of silver iodide (CID 24563, HSDB text: above 145.8 C) | 146 | C | PUBCHEM4 | 2026-10-03 |
| rion:Ba2+XII | Shannon effective ionic radius of Ba2+ with coordination number XII | 161 | pm | SHANNON4 | 2026-10-03 |
| rion:Sr2+XII | Shannon effective ionic radius of Sr2+ with coordination number XII | 144 | pm | SHANNON4 | 2026-10-03 |
| rion:Ca2+XII | Shannon effective ionic radius of Ca2+ with coordination number XII | 134 | pm | SHANNON4 | 2026-10-03 |
| rion:Ti4+VI | Shannon effective ionic radius of Ti4+ with coordination number VI | 60.5 | pm | SHANNON4 | 2026-10-03 |
| iza:LTA.formula | zeolite A (Linde Type A), type material: Na12 (H2O)27 per [Al12Si12O48] (eight per cell), i.e. Na12Al12Si12O48.27H2O | Na12Al12Si12O48.27H2O | -- | IZA-DB | 2026-10-03 |
| iza:LTA.window | zeolite A, channels along <100>: 8-ring 4.1 x 4.1 A | 4.1 | angstrom | IZA-DB | 2026-10-03 |
| iza:LTA.FD | zeolite A, framework density of the type material | 12.9 | T/1000 A3 | IZA-DB | 2026-10-03 |
| iza:MFI.channels | ZSM-5 (MFI), 10-ring channels 5.1 x 5.5 A along [100] and 5.3 x 5.6 A along [010] | 5.1-5.6 | angstrom | IZA-DB | 2026-10-03 |
| iza:FAU.sphere | FAU framework, diameter of the largest sphere that can diffuse along a | 7.35 | angstrom | IZA-DB | 2026-10-03 |
| ghs4:TEOS | tetraethyl orthosilicate (CID 6517): pictograms; H226, H319, H332, H335 (and H370/H372/H373 in some notifications) | GHS02 GHS07 GHS08 | -- | PUBCHEM4 | 2026-10-03 |
| pore:micro | IUPAC convention: micropores have widths below | 2 | nm | NIST-SP960-17 | 2026-10-03 |
| pore:macro | IUPAC convention: macropores have widths above (mesopores between 2 nm and this) | 50 | nm | NIST-SP960-17 | 2026-10-03 |
| cod:MOF5.formula | MOF-5, Zn4O(O2C-C6H4-CO2)3, chemical formula sum (COD 1516287, J. Phys. Chem. C 2010) | C24H12O13Zn4 | -- | COD4 | 2026-10-03 |
| cod:MOF5.a | MOF-5, cubic Fm-3m, lattice parameter a at 280 K (COD 1516287; other COD entries 25.76-25.88 A) | 25.82 | angstrom | COD4 | 2026-10-03 |
| cod:MOF5.Z | MOF-5, formula units per cell (COD 1516287) | 8 | -- | COD4 | 2026-10-03 |
| pdb:Hb.deoxy.FeN4 | displacement of Fe from the mean plane of the four pyrrole N of haem, deoxyhaemoglobin (2DN2, mean of the four chains, range 0.31-0.39 A), computed | 0.34 | angstrom | RCSB-PDB | 2026-10-03 |
| pdb:Hb.oxy.FeN4 | displacement of Fe from the mean plane of the four pyrrole N of haem, oxyhaemoglobin (2DN1, two chains: 0.05 and 0.03 A), computed | 0.04 | angstrom | RCSB-PDB | 2026-10-03 |
| ghs4:cisplatin | cisplatin (CID 5460033): pictograms GHS05 GHS06 GHS08 (aggregated record also lists GHS07); H300 (99 %), H350 (91 %), H318, H317, H334, H340, H360 | GHS05 GHS06 GHS08 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:EDTA | edetic acid (CID 6049): pictograms; H319 (99 %), H332, H373, H412 and others in fewer notifications | GHS07 GHS08 GHS09 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:18C6 | 18-crown-6 (CID 28557): pictogram; H302 (99 %), H315, H319, H335 in fewer notifications | GHS07 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:butadiene | buta-1,3-diene (CID 7845): pictograms GHS02 GHS04 GHS08 (aggregated record also lists GHS07); H220 (100 %), H340 (100 %), H350 (100 %), H280 |GHS02 GHS04 GHS08 | -- | PUBCHEM4 | 2026-10-03 |
| dfh4:CH3r | standard enthalpy of formation of the methyl radical CH3 (g), 298.15 K (ATcT value quoted in Burcat; Ruscic 2003: 146.7) | 146.5 | kJ/mol | BURCAT | 2026-10-03 |
| dfh4:C2H5r | standard enthalpy of formation of the ethyl radical (g), 298.15 K (ATcT 2011, +-0.4) | 119.9 | kJ/mol | BURCAT | 2026-10-03 |
| dfh4:iC3H7r | standard enthalpy of formation of the 2-propyl radical (g), 298.15 K (ATcT 1.122, 2017, +-0.7) | 88.0 | kJ/mol | BURCAT | 2026-10-03 |
| dfh4:tC4H9r | standard enthalpy of formation of the tert-butyl radical (g), 298.15 K (Tsang, J. Phys. Chem. Ref. Data 19 (1990) 1, quoted in Burcat; Burcat's own G3B3 value 55) | 52 | kJ/mol | BURCAT | 2026-10-03 |
| dfh4:PhCH2r | standard enthalpy of formation of the benzyl radical (g), 298.15 K (IUPAC data sheet 2003, +-1.9) | 208.0 | kJ/mol | BURCAT | 2026-10-03 |
| dfh4:H | standard enthalpy of formation of the hydrogen atom (g), 298.15 K (ATcT) | 218.0 | kJ/mol | BURCAT | 2026-10-03 |
| dfh4:iC4H10 | standard enthalpy of formation of 2-methylpropane (isobutane) (g), 298.15 K (ATcT -135.4 +-0.4, quoted in Burcat; WebBook -134.2 and -135.6) | -135.4 | kJ/mol | BURCAT | 2026-10-03 |
| dfh4:toluene_g | standard enthalpy of formation of toluene (g), 298.15 K (review by Roux, Temprado et al., +-1.1) | 50.1 | kJ/mol | WEBBOOK-THERMO4 | 2026-10-03 |
| ghs4:Bu3SnH | tributyltin hydride (CID 5948): pictograms GHS06 GHS08 GHS09 (record also GHS02, GHS07); H301, H312, H315, H319, H372, H410 | GHS06 GHS08 GHS09 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:diazomethane | diazomethane (CID 9550): pictograms of the record (no notification percentages given) | GHS02 GHS05 GHS07 GHS08 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:AIBN | 2,2'-azobis(2-methylpropionitrile) (CID 6547): pictograms; H242 (self-reactive, heating may cause a fire), H302, H332, H412 | GHS02 GHS06 GHS07 GHS08 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:TBHP | tert-butyl hydroperoxide (CID 6410), aqueous and organic solutions: main pictograms GHS02 GHS05 GHS06 GHS08 GHS09 (record also GHS01, GHS07); H226, H242, H311, H314, H317, H341, H411 | GHS02 GHS05 GHS06 GHS08 GHS09 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:TiOiPr4 | titanium(IV) isopropoxide (CID 11026): pictograms; H226, H319, H332 | GHS02 GHS05 GHS07 | -- | PUBCHEM4 | 2026-10-03 |
| pka4:imidazolium | imidazolium (pKaH of imidazole), 25 C (perrin1393, ref K32, Reliable) | 6.95 | -- | IUPAC-PKA4 | 2026-10-03 |
| pka4:piperidinium | piperidinium (pKaH of piperidine), 25 C (perrin967, ref B28, Reliable) | 11.12 | -- | IUPAC-PKA4 | 2026-10-03 |
| pka4:DMAPH | 4-(dimethylamino)pyridinium, 25 C (perrin_supp5181, ref C34, Approximate) | 9.6 | -- | IUPAC-PKA4 | 2026-10-03 |
| pka4:pyrrolium | pyrrolium, C-protonated (pKaH of pyrrole), special acidity function (perrin1337, ref C25a, Uncertain; perrin_supp5358 gives -4.4) | -3.8 | -- | IUPAC-PKA4 | 2026-10-03 |
| pka4:quinolinium | quinolinium (pKaH of quinoline), 20 C (perrin1923, refs A39, A50: 4.90, 4.89) | 4.9 | -- | IUPAC-PKA4 | 2026-10-03 |
| pka4:thiazolium | thiazolium (pKaH of thiazole), 25 C (perrin_supp6453, ref P38, Reliable) | 2.52 | -- | IUPAC-PKA4 | 2026-10-03 |
| dip4:pyrrole | gas-phase dipole moment of pyrrole (CCCBDB diplistx, method DT) | 1.84 | D | CCCBDB4 | 2026-10-03 |
| dip4:furan | gas-phase dipole moment of furan (CCCBDB diplistx, MW) | 0.66 | D | CCCBDB4 | 2026-10-03 |
| dip4:thiophene | gas-phase dipole moment of thiophene (CCCBDB diplistx, DT) | 0.55 | D | CCCBDB4 | 2026-10-03 |
| h1:pyridine.a | pyridine, 1H shift of H2/H6 in CDCl3 (PubChem CID 1049, peak list, 500 MHz; multiplet centre read by this book) | 8.61 | ppm | PUBCHEM4 | 2026-10-03 |
| h1:pyridine.g | pyridine, 1H shift of H4 in CDCl3 (same spectrum) | 7.67 | ppm | PUBCHEM4 | 2026-10-03 |
| h1:pyridine.b | pyridine, 1H shift of H3/H5 in CDCl3 (same spectrum) | 7.28 | ppm | PUBCHEM4 | 2026-10-03 |
| h1:pyrrole.a | pyrrole, 1H shift of H2/H5 in CDCl3 (PubChem CID 8027, peak list, 90 MHz; multiplet centre) | 6.73 | ppm | PUBCHEM4 | 2026-10-03 |
| h1:pyrrole.b | pyrrole, 1H shift of H3/H4 in CDCl3 (same spectrum) | 6.22 | ppm | PUBCHEM4 | 2026-10-03 |
| h1:pyrrole.NH | pyrrole, 1H shift of N-H in CDCl3 (same spectrum, broad, weak) | 8.1 | ppm | PUBCHEM4 | 2026-10-03 |
| h1:furan.a | furan, 1H shift of H2/H5 in CDCl3 (PubChem CID 8029, peak list, 90 MHz; multiplet centre) | 7.43 | ppm | PUBCHEM4 | 2026-10-03 |
| h1:furan.b | furan, 1H shift of H3/H4 in CDCl3 (same spectrum) | 6.38 | ppm | PUBCHEM4 | 2026-10-03 |
| h1:thiophene.a | thiophene, 1H shift of H2/H5 in CDCl3 (PubChem CID 8030, peak list, 90 MHz; multiplet centre) | 7.33 | ppm | PUBCHEM4 | 2026-10-03 |
| h1:thiophene.b | thiophene, 1H shift of H3/H4 in CDCl3 (same spectrum) | 7.12 | ppm | PUBCHEM4 | 2026-10-03 |
| ghs4:pyridine | pyridine (CID 1049): main pictograms GHS02 GHS07 (record also GHS05, GHS06, GHS08, GHS09 in fewer notifications); H225, H302, H312, H332 | GHS02 GHS07 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:phenylhydrazine | phenylhydrazine (CID 7516): pictograms; H301, H311, H331, H315, H317, H319, H341, H350, H372, H400 | GHS06 GHS08 GHS09 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:NaN3 | sodium azide (CID 33557): pictograms GHS06 GHS08 GHS09 (record also GHS05); H300 (fatal if swallowed), H400, H410; contact with acids liberates toxic hydrazoic acid | GHS06 GHS08 GHS09 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:EO | ethylene oxide (CID 6354): main pictograms GHS02 GHS04 GHS06 GHS08 (record also GHS05, GHS07, GHS09); H220, H280, H331, H340, H350, H372 | GHS02 GHS04 GHS06 GHS08 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:2MeTHF | 2-methyltetrahydrofuran (CID 7301): pictograms; H225, H302, H314/H318, H335 | GHS02 GHS05 GHS07 | -- | PUBCHEM4 | 2026-10-03 |
| atm:CO2.2025 | global annual mean CO2 mole fraction in dry air, 2025 (+-0.05) | 425.6 | ppm | NOAA-GML | 2026-10-03 |
| atm:CH4.2025 | global annual mean CH4 mole fraction, 2025 (+-0.5) | 1936 | ppb | NOAA-GML | 2026-10-03 |
| atm:N2O.2025 | global annual mean N2O mole fraction, 2025 (+-0.02) | 338.9 | ppb | NOAA-GML | 2026-10-03 |
| gwp:CH4.fossil | GWP-100 of fossil methane (+-11), AR6 | 29.8 | -- | IPCC-AR6-WG1 | 2026-10-03 |
| gwp:CH4.nonfossil | GWP-100 of non-fossil methane (+-11), AR6 | 27.0 | -- | IPCC-AR6-WG1 | 2026-10-03 |
| gwp:N2O | GWP-100 of nitrous oxide (+-130), AR6 | 273 | -- | IPCC-AR6-WG1 | 2026-10-03 |
| life:CH4 | perturbation lifetime of methane (+-1.8), AR6 | 11.8 | yr | IPCC-AR6-WG1 | 2026-10-03 |
| life:N2O | lifetime of nitrous oxide (+-10), AR6 | 109 | yr | IPCC-AR6-WG1 | 2026-10-03 |
| pka4:H2CO3.1 | CO2(aq) + H2O = HCO3- + H+, pKa1 at 25 C (from log K 16.681 for CO3-2 + 2H+ = CO2 + H2O and 10.329, phreeqc.dat) | 6.35 | -- | PHREEQC | 2026-10-03 |
| pka4:H2CO3.2 | HCO3- = CO3-2 + H+, pKa2 at 25 C (log K 10.329 for CO3-2 + H+ = HCO3-, phreeqc.dat) | 10.33 | -- | PHREEQC | 2026-10-03 |
| ksp4:calcite | calcite CaCO3 = Ca+2 + CO3-2, log Ksp at 25 C (phreeqc.dat; Plummer and Busenberg 1982) | -8.45 | -- | PHREEQC | 2026-10-03 |
| logkow:DDT | p,p'-DDT (CID 3036), experimental log Kow (PubChem LogP section; values 6.36 to 6.91 listed) | 6.91 | -- | PUBCHEM4 | 2026-10-03 |
| logkow:benzene | benzene (CID 241), experimental log Kow (PubChem LogP section) | 2.13 | -- | PUBCHEM4 | 2026-10-03 |
| logkow:atrazine | atrazine (CID 2256), experimental log Kow (PubChem LogP section) | 2.61 | -- | PUBCHEM4 | 2026-10-03 |
| logkow:PCB153 | 2,2',4,4',5,5'-hexachlorobiphenyl (CID 37034), log Kow (PubChem LogP section) | 6.67 | -- | PUBCHEM4 | 2026-10-03 |
| ld50:NaCl | sodium chloride (CID 5234), LD50 rat oral (PubChem Non-Human Toxicity Values) | 3000 | mg/kg | PUBCHEM4 | 2026-10-03 |
| ld50:caffeine | caffeine (CID 2519), LD50 rat oral (PubChem Non-Human Toxicity Values) | 192 | mg/kg | PUBCHEM4 | 2026-10-03 |
| ld50:nicotine | nicotine (CID 89594), LD50 rat oral (PubChem Non-Human Toxicity Values; other routes and species lower) | 188 | mg/kg | PUBCHEM4 | 2026-10-03 |
| ghs4:HgSO4 | mercury(II) sulfate (CID 24544): pictograms; H300, H310, H330, H373, H410 | GHS06 GHS08 GHS09 | -- | PUBCHEM4 | 2026-10-03 |
| pkw4:25C | ionic product of water, pKw at 25 C (phreeqc.dat: H2O = OH- + H+, log K -14) | 14.00 | -- | PHREEQC | 2026-10-03 |
| ea:tolerance | agreement usually required by chemistry journals between found and calculated C, H, N mass percentages (absolute percentage points; questioned by the study) | 0.4 | % | KUVEKE-2022 | 2026-10-03 |
| hrms:tolerance | accuracy of HRMS required by some journals for a molecular-formula assignment (Table 1, e.g. Organic Letters) | 5 | ppm | KUVEKE-2022 | 2026-10-03 |
| fair:year | year of publication of the FAIR guiding principles (Findable, Accessible, Interoperable, Reusable) | 2016 | -- | WILKINSON-2016 | 2026-10-03 |
| ghs4:BuLi | butyllithium (CID 53627823), solutions: pictograms; H250 (pyrophoric), H260 (releases flammable gas with water), H314 | GHS02 GHS05 GHS07 GHS08 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:Et2O | diethyl ether (CID 3283): pictograms; H224, H302, H336 (peroxide former) | GHS02 GHS07 GHS08 | -- | PUBCHEM4 | 2026-10-03 |
| ghs4:THF | tetrahydrofuran (CID 8028): pictograms; H225, H319, H335, H351 (peroxide former) | GHS02 GHS07 GHS08 | -- | PUBCHEM4 | 2026-10-03 |
| const4:me.u | electron mass in atomic mass units, me/u (from const:me and const:u) | 5.48580e-4 | u | CODATA-2022-4 | 2026-10-03 |
