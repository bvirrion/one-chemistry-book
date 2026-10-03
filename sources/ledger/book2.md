# Data ledger — Book 2 (University Year 1)

Book 2's own rows. Shared rows (atomic weights, constants) are in
`sources/data_ledger.md`; the rules are stated there. Owned by the Book 2
writer; other books may cite these rows read-only.

## Sources

| key | source | URL |
|---|---|---|
| ASD-IE | NIST Atomic Spectra Database, ionization energies (ground configurations, ground levels, ionisation energies of atoms and ions), version 5 | https://physics.nist.gov/PhysRefData/ASD/ionEnergy.html |
| ASD-LINES | NIST Atomic Spectra Database, lines data (H I, observed wavelengths in air) | https://physics.nist.gov/PhysRefData/ASD/lines_form.html |
| PUBCHEM-PT | PubChem periodic table (JSON download; Pauling electronegativities, compiled by PubChem from the CRC Handbook) | https://pubchem.ncbi.nlm.nih.gov/rest/pug/periodictable/JSON |
| WEBBOOK-IEN | NIST Chemistry WebBook, SRD 69, gas-phase ion energetics of atoms (electron affinity determinations; the laser photodetachment value is taken, reference in the row) | https://webbook.nist.gov/chemistry/ |
| WEBBOOK-DIAT | NIST Chemistry WebBook, SRD 69, constants of diatomic molecules (Huber and Herzberg compilation), ground state X | https://webbook.nist.gov/chemistry/ |
| CCCBDB | NIST Computational Chemistry Comparison and Benchmark Database, SRD 101, release 22: experimental geometries (expgeom2x.asp, original reference in the row) and experimental dipole moments (diplistx.asp) | https://cccbdb.nist.gov/ |
| WEBBOOK-PHASE | NIST Chemistry WebBook, SRD 69, phase change data (Tboil; AVG = WebBook average of the listed determinations, otherwise the cited determination) | https://webbook.nist.gov/chemistry/ |
| PUBCHEM | PubChem compound records (PUG-View), the cited section and its source (HSDB, CRC Handbook, NIOSH, EPA, ...) given in the row | https://pubchem.ncbi.nlm.nih.gov/ |
| NBS-C514 | A. A. Maryott and E. R. Smith, Table of Dielectric Constants of Pure Liquids, NBS Circular 514 (1951); PDF page given in the row | https://nvlpubs.nist.gov/nistpubs/Legacy/circ/nbscircular514.pdf |
| IAPWS-R8-97 | IAPWS Release on the Static Dielectric Constant of Ordinary Water Substance for Temperatures from 238 K to 873 K and Pressures up to 1000 MPa (R8-97) | https://iapws.org/technical-guidance/release/Dielec |
| COD | Crystallography Open Database; COD entry number and original reference in the row (most entries: R. W. G. Wyckoff, Crystal Structures, 2nd ed., Interscience, 1963) | https://www.crystallography.net/cod/ |
| NBS-82 | D. D. Wagman et al., The NBS tables of chemical thermodynamic properties, J. Phys. Chem. Ref. Data 11, Suppl. 2 (1982); standard Gibbs energies of formation at 298.15 K and 1 bar, read from the scanned tables (page in the row); ao = aqueous, undissociated, standard state m = 1 | https://srd.nist.gov/JPCRD/jpcrdS2Vol11.pdf |
| NIST-SP260-142 | R. H. Shreiner and K. W. Pratt, *Standard Reference Materials: Primary Standards and Standard Reference Materials for Electrolytic Conductivity*, NIST Special Publication 260-142, 2004 edition, sec. 1.3 (limiting ionic conductivities of H+ and OH-, citing its ref. [7]) | https://www.nist.gov/system/files/documents/srm/260-142-2ndVersion.pdf |
| NIST-JRES100 | Y. C. Wu and P. A. Berezansky, *Low Electrolytic Conductivity Standards*, J. Res. Natl. Inst. Stand. Technol. 100, 521 (1995), Table 1 (limiting equivalent conductivities in water, 25 degC) | https://nvlpubs.nist.gov/nistpubs/jres/100/5/j15wu.pdf |
| WEBBOOK-IR | NIST Chemistry WebBook (SRD 69), gas-phase IR spectra (JCAMP-DX, origin Sadtler Research Labs under US-EPA contract, owner NIST SRD Program): band maxima read by a peak search on the absorbance data; the row gives the CAS number | https://webbook.nist.gov/chemistry/ |
| USGS-MCS2026 | U.S. Geological Survey, *Mineral Commodity Summaries 2026*, commodity chapters (lithium, soda ash, nitrogen, sulfur, phosphate rock, bauxite, silicon, boron, iodine, bromine), World Mine Production tables; 2025 values are USGS estimates | https://pubs.usgs.gov/periodicals/mcs2026/ |
| NEA-TDB9 | Hummel, Anderegg, Puigdomènech, Rao, Tochiyama, *Chemical Thermodynamics of Compounds and Complexes of U, Np, Pu, Am, Tc, Se, Ni and Zr with Selected Organic Ligands*, OECD Nuclear Energy Agency, Chemical Thermodynamics vol. 9 (Elsevier, 2005), Table III-6 (edta, I = 0, 298.15 K) and Table III-2 (oxalate) | https://www.oecd-nea.org/dbtdb/pubs/vol9-organic-ligands.pdf |
| IUPAC-PKA | J. W. Zheng and O. Lafontant-Joseph, IUPAC Digitized pKa Dataset v2.4a (from Serjeant and Dempsey 1979; Perrin 1965, 1972), CC BY-NC 4.0, file iupac_high-confidence_v2_4.csv; unique_ID and original reference code in the row | https://github.com/IUPAC/Dissociation-Constants |
| JANAF | NIST-JANAF Thermochemical Tables, 4th ed. (online tables, 298.15 K row) | https://janaf.nist.gov/ |
| SHANNON | R. D. Shannon, Acta Cryst. A32 (1976) 751, effective ionic radii, as tabulated in the Database of Ionic Radii (Imperial College) | http://abulafia.mt.ic.ac.uk/shannon/ptable.php |
| WEBBOOK-IEMOL | NIST Chemistry WebBook (SRD 69), gas-phase ion energetics of molecules, ionization energy determinations (the first, spectroscopic, value of the list is taken; reference in the row) | https://webbook.nist.gov/chemistry/ |
| GRAHAM-2000 | L. Graham, O. Graudejus, N. K. Jha and N. Bartlett, *Concerning the nature of XePtF6*, Coord. Chem. Rev. 197 (2000) 321-334, doi:10.1016/S0010-8545(99)00190-3 (bibliographic record checked through the Crossref API) | https://doi.org/10.1016/S0010-8545(99)00190-3 |
| PUBCHEM-GHSSUM | PubChem, *GHS Classification (Rev.11, 2025) Summary*, after UNECE GHS Rev.11: pictogram names, hazard statements with hazard class, category and signal word, precautionary statements | https://pubchem.ncbi.nlm.nih.gov/ghs/ |

## Rows

| id | quantity | value | unit | source | accessed |
|---|---|---|---|---|---|
| asd:Halpha | H I Balmer line 3 -> 2 (H-alpha), observed wavelength in air | 656.279 | nm | ASD-LINES | 2026-10-02 |
| asd:Hbeta | H I Balmer line 4 -> 2 (H-beta), observed wavelength in air | 486.135 | nm | ASD-LINES | 2026-10-02 |
| asd:Hgamma | H I Balmer line 5 -> 2 (H-gamma), observed wavelength in air | 434.047 | nm | ASD-LINES | 2026-10-02 |
| asd:Hdelta | H I Balmer line 6 -> 2 (H-delta), observed wavelength in air | 410.173 | nm | ASD-LINES | 2026-10-02 |
| ie:H | first ionisation energy of H | 13.598434599702 | eV | ASD-IE | 2026-10-02 |
| gs:K | ground configuration of K | [Ar] 4s1 | - | ASD-IE | 2026-10-02 |
| gs:Ca | ground configuration of Ca | [Ar] 4s2 | - | ASD-IE | 2026-10-02 |
| gs:Sc | ground configuration of Sc | [Ar] 3d1 4s2 | - | ASD-IE | 2026-10-02 |
| gs:V | ground configuration of V | [Ar] 3d3 4s2 | - | ASD-IE | 2026-10-02 |
| gs:Cr | ground configuration of Cr | [Ar] 3d5 4s1 | - | ASD-IE | 2026-10-02 |
| gs:Fe | ground configuration of Fe | [Ar] 3d6 4s2 | - | ASD-IE | 2026-10-02 |
| gs:Ni | ground configuration of Ni | [Ar] 3d8 4s2 | - | ASD-IE | 2026-10-02 |
| gs:Cu | ground configuration of Cu | [Ar] 3d10 4s1 | - | ASD-IE | 2026-10-02 |
| gs:Fe2+ | ground configuration of Fe2+ (Fe III) | [Ar] 3d6 | - | ASD-IE | 2026-10-02 |
| gs:Fe3+ | ground configuration of Fe3+ (Fe IV) | [Ar] 3d5 | - | ASD-IE | 2026-10-02 |
| gs:Mn2+ | ground configuration of Mn2+ (Mn III) | [Ar] 3d5 | - | ASD-IE | 2026-10-02 |
| gs:Cu+ | ground configuration of Cu+ (Cu II) | [Ar] 3d10 | - | ASD-IE | 2026-10-02 |
| gs:Cu2+ | ground configuration of Cu2+ (Cu III) | [Ar] 3d9 | - | ASD-IE | 2026-10-02 |
| gs:Zn2+ | ground configuration of Zn2+ (Zn III) | [Ar] 3d10 | - | ASD-IE | 2026-10-02 |
| gs:Ti2+ | ground configuration of Ti2+ (Ti III) | [Ar] 3d2 | - | ASD-IE | 2026-10-02 |
| gs:Co2+ | ground configuration of Co2+ (Co III) | [Ar] 3d7 | - | ASD-IE | 2026-10-02 |
| ie:He | first ionisation energy of He (Z = 2) | 24.587389011 | eV | ASD-IE | 2026-10-02 |
| ie:Li | first ionisation energy of Li (Z = 3) | 5.391714996 | eV | ASD-IE | 2026-10-02 |
| ie:Be | first ionisation energy of Be (Z = 4) | 9.322699 | eV | ASD-IE | 2026-10-02 |
| ie:B | first ionisation energy of B (Z = 5) | 8.298019 | eV | ASD-IE | 2026-10-02 |
| ie:C | first ionisation energy of C (Z = 6) | 11.2602880 | eV | ASD-IE | 2026-10-02 |
| ie:N | first ionisation energy of N (Z = 7) | 14.53413 | eV | ASD-IE | 2026-10-02 |
| ie:O | first ionisation energy of O (Z = 8) | 13.618055 | eV | ASD-IE | 2026-10-02 |
| ie:F | first ionisation energy of F (Z = 9) | 17.42282 | eV | ASD-IE | 2026-10-02 |
| ie:Ne | first ionisation energy of Ne (Z = 10) | 21.564541 | eV | ASD-IE | 2026-10-02 |
| ie:Na | first ionisation energy of Na (Z = 11) | 5.13907696 | eV | ASD-IE | 2026-10-02 |
| ie:Mg | first ionisation energy of Mg (Z = 12) | 7.646236 | eV | ASD-IE | 2026-10-02 |
| ie:Al | first ionisation energy of Al (Z = 13) | 5.985769 | eV | ASD-IE | 2026-10-02 |
| ie:Si | first ionisation energy of Si (Z = 14) | 8.15168 | eV | ASD-IE | 2026-10-02 |
| ie:P | first ionisation energy of P (Z = 15) | 10.486686 | eV | ASD-IE | 2026-10-02 |
| ie:S | first ionisation energy of S (Z = 16) | 10.3600167 | eV | ASD-IE | 2026-10-02 |
| ie:Cl | first ionisation energy of Cl (Z = 17) | 12.967633 | eV | ASD-IE | 2026-10-02 |
| ie:Ar | first ionisation energy of Ar (Z = 18) | 15.7596119 | eV | ASD-IE | 2026-10-02 |
| ie:K | first ionisation energy of K (Z = 19) | 4.34066373 | eV | ASD-IE | 2026-10-02 |
| ie:Ca | first ionisation energy of Ca (Z = 20) | 6.1131549210 | eV | ASD-IE | 2026-10-02 |
| ie:Sc | first ionisation energy of Sc (Z = 21) | 6.56149 | eV | ASD-IE | 2026-10-02 |
| ie:Ti | first ionisation energy of Ti (Z = 22) | 6.828120 | eV | ASD-IE | 2026-10-02 |
| ie:V | first ionisation energy of V (Z = 23) | 6.746187 | eV | ASD-IE | 2026-10-02 |
| ie:Cr | first ionisation energy of Cr (Z = 24) | 6.76651 | eV | ASD-IE | 2026-10-02 |
| ie:Mn | first ionisation energy of Mn (Z = 25) | 7.4340380 | eV | ASD-IE | 2026-10-02 |
| ie:Fe | first ionisation energy of Fe (Z = 26) | 7.9024681 | eV | ASD-IE | 2026-10-02 |
| ie:Co | first ionisation energy of Co (Z = 27) | 7.88101 | eV | ASD-IE | 2026-10-02 |
| ie:Ni | first ionisation energy of Ni (Z = 28) | 7.639878 | eV | ASD-IE | 2026-10-02 |
| ie:Cu | first ionisation energy of Cu (Z = 29) | 7.726380 | eV | ASD-IE | 2026-10-02 |
| ie:Zn | first ionisation energy of Zn (Z = 30) | 9.394197 | eV | ASD-IE | 2026-10-02 |
| ie:Ga | first ionisation energy of Ga (Z = 31) | 5.9993020 | eV | ASD-IE | 2026-10-02 |
| ie:Ge | first ionisation energy of Ge (Z = 32) | 7.899435 | eV | ASD-IE | 2026-10-02 |
| ie:As | first ionisation energy of As (Z = 33) | 9.78855 | eV | ASD-IE | 2026-10-02 |
| ie:Se | first ionisation energy of Se (Z = 34) | 9.752368 | eV | ASD-IE | 2026-10-02 |
| ie:Br | first ionisation energy of Br (Z = 35) | 11.81381 | eV | ASD-IE | 2026-10-02 |
| ie:Kr | first ionisation energy of Kr (Z = 36) | 13.9996055 | eV | ASD-IE | 2026-10-02 |
| ie2:Mg | ionisation energy number 2 of Mg (Mg II -> next ion) | 15.035271 | eV | ASD-IE | 2026-10-02 |
| ie3:Mg | ionisation energy number 3 of Mg (Mg III -> next ion) | 80.1436 | eV | ASD-IE | 2026-10-02 |
| ie4:Mg | ionisation energy number 4 of Mg (Mg IV -> next ion) | 109.2654 | eV | ASD-IE | 2026-10-02 |
| ie2:Na | ionisation energy number 2 of Na (Na II -> next ion) | 47.28636 | eV | ASD-IE | 2026-10-02 |
| ie2:Al | ionisation energy number 2 of Al (Al II -> next ion) | 18.82855 | eV | ASD-IE | 2026-10-02 |
| ie3:Al | ionisation energy number 3 of Al (Al III -> next ion) | 28.447642 | eV | ASD-IE | 2026-10-02 |
| ie4:Al | ionisation energy number 4 of Al (Al IV -> next ion) | 119.9924 | eV | ASD-IE | 2026-10-02 |
| en:H | Pauling electronegativity of H | 2.2 | - | PUBCHEM-PT | 2026-10-02 |
| en:Li | Pauling electronegativity of Li | 0.98 | - | PUBCHEM-PT | 2026-10-02 |
| en:Be | Pauling electronegativity of Be | 1.57 | - | PUBCHEM-PT | 2026-10-02 |
| en:B | Pauling electronegativity of B | 2.04 | - | PUBCHEM-PT | 2026-10-02 |
| en:C | Pauling electronegativity of C | 2.55 | - | PUBCHEM-PT | 2026-10-02 |
| en:N | Pauling electronegativity of N | 3.04 | - | PUBCHEM-PT | 2026-10-02 |
| en:O | Pauling electronegativity of O | 3.44 | - | PUBCHEM-PT | 2026-10-02 |
| en:F | Pauling electronegativity of F | 3.98 | - | PUBCHEM-PT | 2026-10-02 |
| en:Na | Pauling electronegativity of Na | 0.93 | - | PUBCHEM-PT | 2026-10-02 |
| en:Mg | Pauling electronegativity of Mg | 1.31 | - | PUBCHEM-PT | 2026-10-02 |
| en:Al | Pauling electronegativity of Al | 1.61 | - | PUBCHEM-PT | 2026-10-02 |
| en:Si | Pauling electronegativity of Si | 1.9 | - | PUBCHEM-PT | 2026-10-02 |
| en:P | Pauling electronegativity of P | 2.19 | - | PUBCHEM-PT | 2026-10-02 |
| en:S | Pauling electronegativity of S | 2.58 | - | PUBCHEM-PT | 2026-10-02 |
| en:Cl | Pauling electronegativity of Cl | 3.16 | - | PUBCHEM-PT | 2026-10-02 |
| en:K | Pauling electronegativity of K | 0.82 | - | PUBCHEM-PT | 2026-10-02 |
| en:Ca | Pauling electronegativity of Ca | 1 | - | PUBCHEM-PT | 2026-10-02 |
| en:Ti | Pauling electronegativity of Ti | 1.54 | - | PUBCHEM-PT | 2026-10-02 |
| en:Cr | Pauling electronegativity of Cr | 1.66 | - | PUBCHEM-PT | 2026-10-02 |
| en:Mn | Pauling electronegativity of Mn | 1.55 | - | PUBCHEM-PT | 2026-10-02 |
| en:Fe | Pauling electronegativity of Fe | 1.83 | - | PUBCHEM-PT | 2026-10-02 |
| en:Co | Pauling electronegativity of Co | 1.88 | - | PUBCHEM-PT | 2026-10-02 |
| en:Ni | Pauling electronegativity of Ni | 1.91 | - | PUBCHEM-PT | 2026-10-02 |
| en:Cu | Pauling electronegativity of Cu | 1.9 | - | PUBCHEM-PT | 2026-10-02 |
| en:Zn | Pauling electronegativity of Zn | 1.65 | - | PUBCHEM-PT | 2026-10-02 |
| en:Ga | Pauling electronegativity of Ga | 1.81 | - | PUBCHEM-PT | 2026-10-02 |
| en:Ge | Pauling electronegativity of Ge | 2.01 | - | PUBCHEM-PT | 2026-10-02 |
| en:As | Pauling electronegativity of As | 2.18 | - | PUBCHEM-PT | 2026-10-02 |
| en:Se | Pauling electronegativity of Se | 2.55 | - | PUBCHEM-PT | 2026-10-02 |
| en:Br | Pauling electronegativity of Br | 2.96 | - | PUBCHEM-PT | 2026-10-02 |
| en:Rb | Pauling electronegativity of Rb | 0.82 | - | PUBCHEM-PT | 2026-10-02 |
| en:Sr | Pauling electronegativity of Sr | 0.95 | - | PUBCHEM-PT | 2026-10-02 |
| en:Ag | Pauling electronegativity of Ag | 1.93 | - | PUBCHEM-PT | 2026-10-02 |
| en:In | Pauling electronegativity of In | 1.78 | - | PUBCHEM-PT | 2026-10-02 |
| en:Sn | Pauling electronegativity of Sn | 1.96 | - | PUBCHEM-PT | 2026-10-02 |
| en:Sb | Pauling electronegativity of Sb | 2.05 | - | PUBCHEM-PT | 2026-10-02 |
| en:Te | Pauling electronegativity of Te | 2.1 | - | PUBCHEM-PT | 2026-10-02 |
| en:I | Pauling electronegativity of I | 2.66 | - | PUBCHEM-PT | 2026-10-02 |
| en:Cs | Pauling electronegativity of Cs | 0.79 | - | PUBCHEM-PT | 2026-10-02 |
| en:Ba | Pauling electronegativity of Ba | 0.89 | - | PUBCHEM-PT | 2026-10-02 |
| ea:C | electron affinity of C (LPD; Scheer, Bilodeau, et al., 1998) | 1.262114 | eV | WEBBOOK-IEN | 2026-10-02 |
| ea:O | electron affinity of O (LPD; Joiner, Mohr, et al., 2011) | 1.439157 | eV | WEBBOOK-IEN | 2026-10-02 |
| ea:F | electron affinity of F (LPD; Blondel, Delsart, et al., 2001) | 3.401191 | eV | WEBBOOK-IEN | 2026-10-02 |
| ea:Na | electron affinity of Na (LPES; Patterson, Hotop, et al., 1974) | 0.5480 | eV | WEBBOOK-IEN | 2026-10-02 |
| ea:Si | electron affinity of Si (LPD; Blondel, Chaibi, et al., 2005) | 1.389517 | eV | WEBBOOK-IEN | 2026-10-02 |
| ea:P | electron affinity of P (LPD; Andersson, Lindahl, et al., 2007) | 0.746679 | eV | WEBBOOK-IEN | 2026-10-02 |
| ea:S | electron affinity of S (LPD; Wells and Yukich, 2009) | 2.017149 | eV | WEBBOOK-IEN | 2026-10-02 |
| ea:Cl | electron affinity of Cl (LPD; Trainham, Fletcher, et al., 1987) | 3.612709 | eV | WEBBOOK-IEN | 2026-10-02 |
| ea:Br | electron affinity of Br (LPD; Blondel, Cacciani, et al., 1989) | 3.363583 | eV | WEBBOOK-IEN | 2026-10-02 |
| ea:I | electron affinity of I (LPD; Hanstorp and Gustafsson, 1992) | 3.059036 | eV | WEBBOOK-IEN | 2026-10-02 |
| janaf:H | standard enthalpy of formation of H(g) at 298.15 K | 217.999 | kJ/mol | JANAF | 2026-10-02 |
| janaf:Cl | standard enthalpy of formation of Cl(g) at 298.15 K | 121.302 | kJ/mol | JANAF | 2026-10-02 |
| janaf:HCl | standard enthalpy of formation of HCl(g) at 298.15 K | -92.312 | kJ/mol | JANAF | 2026-10-02 |
| rion:Li+IV | Shannon effective ionic radius of Li+ with coordination number IV | 59 | pm | SHANNON | 2026-10-02 |
| rion:Li+VI | Shannon effective ionic radius of Li+ with coordination number VI | 76 | pm | SHANNON | 2026-10-02 |
| rion:Na+VI | Shannon effective ionic radius of Na+ with coordination number VI | 102 | pm | SHANNON | 2026-10-02 |
| rion:Na+VIII | Shannon effective ionic radius of Na+ with coordination number VIII | 118 | pm | SHANNON | 2026-10-02 |
| rion:K+VI | Shannon effective ionic radius of K+ with coordination number VI | 138 | pm | SHANNON | 2026-10-02 |
| rion:Rb+VI | Shannon effective ionic radius of Rb+ with coordination number VI | 152 | pm | SHANNON | 2026-10-02 |
| rion:Cs+VI | Shannon effective ionic radius of Cs+ with coordination number VI | 167 | pm | SHANNON | 2026-10-02 |
| rion:Cs+VIII | Shannon effective ionic radius of Cs+ with coordination number VIII | 174 | pm | SHANNON | 2026-10-02 |
| rion:Be2+IV | Shannon effective ionic radius of Be2+ with coordination number IV | 27 | pm | SHANNON | 2026-10-02 |
| rion:Mg2+VI | Shannon effective ionic radius of Mg2+ with coordination number VI | 72 | pm | SHANNON | 2026-10-02 |
| rion:Ca2+VI | Shannon effective ionic radius of Ca2+ with coordination number VI | 100 | pm | SHANNON | 2026-10-02 |
| rion:Ca2+VIII | Shannon effective ionic radius of Ca2+ with coordination number VIII | 112 | pm | SHANNON | 2026-10-02 |
| rion:Sr2+VI | Shannon effective ionic radius of Sr2+ with coordination number VI | 118 | pm | SHANNON | 2026-10-02 |
| rion:Ba2+VI | Shannon effective ionic radius of Ba2+ with coordination number VI | 135 | pm | SHANNON | 2026-10-02 |
| rion:Al3+VI | Shannon effective ionic radius of Al3+ with coordination number VI | 53.5 | pm | SHANNON | 2026-10-02 |
| rion:Zn2+IV | Shannon effective ionic radius of Zn2+ with coordination number IV | 60 | pm | SHANNON | 2026-10-02 |
| rion:O2-IV | Shannon effective ionic radius of O2- with coordination number IV | 138 | pm | SHANNON | 2026-10-02 |
| rion:O2-VI | Shannon effective ionic radius of O2- with coordination number VI | 140 | pm | SHANNON | 2026-10-02 |
| rion:O2-VIII | Shannon effective ionic radius of O2- with coordination number VIII | 142 | pm | SHANNON | 2026-10-02 |
| rion:F-IV | Shannon effective ionic radius of F- with coordination number IV | 131 | pm | SHANNON | 2026-10-02 |
| rion:F-VI | Shannon effective ionic radius of F- with coordination number VI | 133 | pm | SHANNON | 2026-10-02 |
| rion:Cl-VI | Shannon effective ionic radius of Cl- with coordination number VI | 181 | pm | SHANNON | 2026-10-02 |
| rion:Br-VI | Shannon effective ionic radius of Br- with coordination number VI | 196 | pm | SHANNON | 2026-10-02 |
| rion:I-VI | Shannon effective ionic radius of I- with coordination number VI | 220 | pm | SHANNON | 2026-10-02 |
| rion:S2-VI | Shannon effective ionic radius of S2- with coordination number VI | 184 | pm | SHANNON | 2026-10-02 |
| rion:Se2-VI | Shannon effective ionic radius of Se2- with coordination number VI | 198 | pm | SHANNON | 2026-10-02 |
| re:H2 | equilibrium bond length of H2, ground state | 0.74144 | angstrom | WEBBOOK-DIAT | 2026-10-02 |
| re:F2 | equilibrium bond length of F2, ground state | 1.41193 | angstrom | WEBBOOK-DIAT | 2026-10-02 |
| re:Cl2 | equilibrium bond length of Cl2, ground state | 1.9879 | angstrom | WEBBOOK-DIAT | 2026-10-02 |
| re:Br2 | equilibrium bond length of Br2, ground state | 2.28105 | angstrom | WEBBOOK-DIAT | 2026-10-02 |
| re:I2 | equilibrium bond length of I2, ground state | 2.6663 | angstrom | WEBBOOK-DIAT | 2026-10-02 |
| re:N2 | equilibrium bond length of N2, ground state | 1.097685 | angstrom | WEBBOOK-DIAT | 2026-10-02 |
| re:O2 | equilibrium bond length of O2, ground state | 1.20752 | angstrom | WEBBOOK-DIAT | 2026-10-02 |
| re:HCl | equilibrium bond length of HCl, ground state | 1.274552 | angstrom | WEBBOOK-DIAT | 2026-10-02 |
| re:HF | equilibrium bond length of HF, ground state | 0.916808 | angstrom | WEBBOOK-DIAT | 2026-10-02 |
| re:CO | equilibrium bond length of CO, ground state | 1.128323 | angstrom | WEBBOOK-DIAT | 2026-10-02 |
| en:Kr | Pauling electronegativity of Kr | 3 | - | PUBCHEM-PT | 2026-10-02 |
| en:Xe | Pauling electronegativity of Xe | 2.6 | - | PUBCHEM-PT | 2026-10-02 |
| geo:H2O.rOH | experimental bond length rOH of H2O (ref. 1979Hoy/Bun:1) | 0.958 | angstrom | CCCBDB | 2026-10-02 |
| geo:H2O.aHOH | experimental angle aHOH of H2O (ref. 1979Hoy/Bun:1) | 104.4776 | degree | CCCBDB | 2026-10-02 |
| geo:NH3.rNH | experimental bond length rNH of NH3 (ref. 1966Herzberg) | 1.012 | angstrom | CCCBDB | 2026-10-02 |
| geo:NH3.aHNH | experimental angle aHNH of NH3 (ref. 1966Herzberg) | 106.67 | degree | CCCBDB | 2026-10-02 |
| geo:NH3.aXNH | experimental angle aXNH of NH3 (ref. 1966Herzberg) | 112.15 | degree | CCCBDB | 2026-10-02 |
| geo:CH4.rCH | experimental bond length rCH of CH4 (ref. 1979Hir:213) | 1.087 | angstrom | CCCBDB | 2026-10-02 |
| geo:CH4.aHCH | experimental angle aHCH of CH4 (ref. 1974sve/kov) | 109.471 | degree | CCCBDB | 2026-10-02 |
| geo:O3.rOO | experimental bond length rOO of O3 (ref. 1966Herzberg) | 1.278 | angstrom | CCCBDB | 2026-10-02 |
| geo:O3.aOOO | experimental angle aOOO of O3 (ref. 1966Herzberg) | 116.8 | degree | CCCBDB | 2026-10-02 |
| geo:SO2.rSO | experimental bond length rSO of SO2 (ref. 1966Herzberg) | 1.432 | angstrom | CCCBDB | 2026-10-02 |
| geo:SO2.aOSO | experimental angle aOSO of SO2 (ref. 1966Herzberg) | 119.5 | degree | CCCBDB | 2026-10-02 |
| geo:CO2.rCO | experimental bond length rCO of CO2 (ref. 1966Herzberg) | 1.162 | angstrom | CCCBDB | 2026-10-02 |
| geo:CO2.aOCO | experimental angle aOCO of CO2 (ref. 1966Herzberg) | 180 | degree | CCCBDB | 2026-10-02 |
| geo:BF3.rBF | experimental bond length rBF of BF3 (ref. 1998Kuc) | 1.307 | angstrom | CCCBDB | 2026-10-02 |
| geo:BF3.aFBF | experimental angle aFBF of BF3 (ref. 1998Kuc) | 120 | degree | CCCBDB | 2026-10-02 |
| geo:C2H6.rCC | experimental bond length rCC of C2H6 (ref. 1966Herzberg) | 1.536 | angstrom | CCCBDB | 2026-10-02 |
| geo:C2H6.rCH | experimental bond length rCH of C2H6 (ref. 1966Herzberg) | 1.091 | angstrom | CCCBDB | 2026-10-02 |
| geo:C2H6.aHCH | experimental angle aHCH of C2H6 (ref. 1966Herzberg) | 108 | degree | CCCBDB | 2026-10-02 |
| geo:C2H6.aHCC | experimental angle aHCC of C2H6 (ref. 1966Herzberg) | 110.91 | degree | CCCBDB | 2026-10-02 |
| geo:C2H4.rCC | experimental bond length rCC of C2H4 (ref. 1966Herzberg) | 1.339 | angstrom | CCCBDB | 2026-10-02 |
| geo:C2H4.rCH | experimental bond length rCH of C2H4 (ref. 1966Herzberg) | 1.086 | angstrom | CCCBDB | 2026-10-02 |
| geo:C2H4.aHCH | experimental angle aHCH of C2H4 (ref. 1966Herzberg) | 117.6 | degree | CCCBDB | 2026-10-02 |
| geo:C2H4.aHCC | experimental angle aHCC of C2H4 (ref. 1966Herzberg) | 121.2 | degree | CCCBDB | 2026-10-02 |
| geo:C2H2.rCH | experimental bond length rCH of C2H2 (ref. 1998Kuc) | 1.063 | angstrom | CCCBDB | 2026-10-02 |
| geo:C2H2.rCC | experimental bond length rCC of C2H2 (ref. 1998Kuc) | 1.203 | angstrom | CCCBDB | 2026-10-02 |
| geo:C2H2.aHCC | experimental angle aHCC of C2H2 (ref. 1966Herzberg) | 180 | degree | CCCBDB | 2026-10-02 |
| geo:C6H6.rCC | experimental bond length rCC of C6H6 (ref. 1966Herzberg) | 1.397 | angstrom | CCCBDB | 2026-10-02 |
| geo:C6H6.rCH | experimental bond length rCH of C6H6 (ref. 1966Herzberg) | 1.084 | angstrom | CCCBDB | 2026-10-02 |
| geo:C6H6.aCCC | experimental angle aCCC of C6H6 (ref. 1966Herzberg) | 120 | degree | CCCBDB | 2026-10-02 |
| geo:C6H6.aHCC | experimental angle aHCC of C6H6 (ref. 1966Herzberg) | 120 | degree | CCCBDB | 2026-10-02 |
| geo:H2S.rSH | experimental bond length rSH of H2S (ref. 1975Coo/DeL:237) | 1.336 | angstrom | CCCBDB | 2026-10-02 |
| geo:H2S.aHSH | experimental angle aHSH of H2S (ref. 1975Coo/DeL:237) | 92.11 | degree | CCCBDB | 2026-10-02 |
| geo:PCl5.rPCl | experimental bond length rPCl of PCl5 (ref. Gurvich) | 2.124 | angstrom | CCCBDB | 2026-10-02 |
| geo:PCl5.rPCl2 | experimental bond length rPCl of PCl5 (ref. Gurvich) | 2.020 | angstrom | CCCBDB | 2026-10-02 |
| geo:SF6.rSF | experimental bond length rSF of SF6 (ref. 1998Kuc) | 1.561 | angstrom | CCCBDB | 2026-10-02 |
| geo:SF6.aFSF | experimental angle aFSF of SF6 (ref. 1998Kuc) | 90 | degree | CCCBDB | 2026-10-02 |
| geo:SF6.aFSF2 | experimental angle aFSF of SF6 (ref. 1998Kuc) | 180 | degree | CCCBDB | 2026-10-02 |
| geo:ClF3.rFCl | experimental bond length rFCl of ClF3 (ref. 2001Muller:1570) | 1.597 | angstrom | CCCBDB | 2026-10-02 |
| geo:ClF3.rFCl2 | experimental bond length rFCl of ClF3 (ref. 2001Muller:1570) | 1.697 | angstrom | CCCBDB | 2026-10-02 |
| geo:ClF3.aFClF | experimental angle aFClF of ClF3 (ref. 2001Muller:1570) | 87.45 | degree | CCCBDB | 2026-10-02 |
| geo:ClF3.aFClF2 | experimental angle aFClF of ClF3 (ref. 2001Muller:1570) | 174.9 | degree | CCCBDB | 2026-10-02 |
| geo:XeF2.rFXe | experimental bond length rFXe of XeF2 (ref. 1993Bur/Ma:536-539) | 1.974 | angstrom | CCCBDB | 2026-10-02 |
| geo:XeF2.aFXeF | experimental angle aFXeF of XeF2 (ref. ) | 180 | degree | CCCBDB | 2026-10-02 |
| geo:SF4.rSF | experimental bond length rSF of SF4 (ref. 1962Tol/Gwi:1119) | 1.646 | angstrom | CCCBDB | 2026-10-02 |
| geo:SF4.rSF2 | experimental bond length rSF of SF4 (ref. 1962Tol/Gwi:1119) | 1.545 | angstrom | CCCBDB | 2026-10-02 |
| geo:SF4.aFSF | experimental angle aFSF of SF4 (ref. 1962Tol/Gwi:1119) | 173.07 | degree | CCCBDB | 2026-10-02 |
| geo:SF4.aFSF2 | experimental angle aFSF of SF4 (ref. 1962Tol/Gwi:1119) | 101.55 | degree | CCCBDB | 2026-10-02 |
| geo:SF4.aFSF3 | experimental angle aFSF of SF4 (ref. 1962Tol/Gwi:1119) | 87.81 | degree | CCCBDB | 2026-10-02 |
| geo:NO2.rNO | experimental bond length rNO of NO2 (ref. 1966Herzberg) | 1.193 | angstrom | CCCBDB | 2026-10-02 |
| geo:NO2.aONO | experimental angle aONO of NO2 (ref. 1966Herzberg) | 134.1 | degree | CCCBDB | 2026-10-02 |
| geo:HNO3.rOH | experimental bond length rOH of HNO3 (ref. 1965Cox/Riv:3106) | 0.964 | angstrom | CCCBDB | 2026-10-02 |
| geo:HNO3.rNO | experimental bond length rNO of HNO3 (ref. 1965Cox/Riv:3106) | 1.406 | angstrom | CCCBDB | 2026-10-02 |
| geo:HNO3.rNO2 | experimental bond length rNO of HNO3 (ref. 1965Cox/Riv:3106) | 1.211 | angstrom | CCCBDB | 2026-10-02 |
| geo:HNO3.rNO3 | experimental bond length rNO of HNO3 (ref. 1965Cox/Riv:3106) | 1.199 | angstrom | CCCBDB | 2026-10-02 |
| geo:HNO3.aHON | experimental angle aHON of HNO3 (ref. 1965Cox/Riv:3106) | 102.15 | degree | CCCBDB | 2026-10-02 |
| geo:HNO3.aONO | experimental angle aONO of HNO3 (ref. 1965Cox/Riv:3106) | 115.0883 | degree | CCCBDB | 2026-10-02 |
| geo:HNO3.aONO2 | experimental angle aONO of HNO3 (ref. 1965Cox/Riv:3106) | 130.267 | degree | CCCBDB | 2026-10-02 |
| geo:HNO3.aONO3 | experimental angle aONO of HNO3 (ref. 1965Cox/Riv:3106) | 113.85 | degree | CCCBDB | 2026-10-02 |
| geo:PCl3.rPCl | experimental bond length rPCl of PCl3 (ref. 1976Hellwege(II/7)) | 2.043 | angstrom | CCCBDB | 2026-10-02 |
| geo:PCl3.aClPCl | experimental angle aClPCl of PCl3 (ref. 1976Hellwege(II/7)) | 100.1 | degree | CCCBDB | 2026-10-02 |
| geo:PCl3.aXPCl | experimental angle aXPCl of PCl3 (ref. 1976Hellwege(II/7)) | 117.7 | degree | CCCBDB | 2026-10-02 |
| geo:PH3.rPH | experimental bond length rPH of PH3 (ref. 1966Herzberg) | 1.421 | angstrom | CCCBDB | 2026-10-02 |
| geo:PH3.aHPH | experimental angle aHPH of PH3 (ref. 1966Herzberg) | 93.3 | degree | CCCBDB | 2026-10-02 |
| geo:PH3.aXPH | experimental angle aXPH of PH3 (ref. 1966Herzberg) | 122.89 | degree | CCCBDB | 2026-10-02 |
| dip:CO | gas-phase dipole moment of Carbon monoxide (CO) | 0.112 | D | CCCBDB | 2026-10-02 |
| dip:HF | gas-phase dipole moment of Hydrogen fluoride (HF) | 1.827 | D | CCCBDB | 2026-10-02 |
| dip:HCl | gas-phase dipole moment of Hydrogen chloride (HCl) | 1.093 | D | CCCBDB | 2026-10-02 |
| dip:HBr | gas-phase dipole moment of hydrogen bromide (HBr) | 0.827 | D | CCCBDB | 2026-10-02 |
| dip:HI | gas-phase dipole moment of Hydrogen iodide (HI) | 0.448 | D | CCCBDB | 2026-10-02 |
| dip:H2O | gas-phase dipole moment of Water (H2O) | 1.857 | D | CCCBDB | 2026-10-02 |
| dip:N2O | gas-phase dipole moment of Nitrous oxide (N2O) | 0.161 | D | CCCBDB | 2026-10-02 |
| dip:NO2 | gas-phase dipole moment of Nitrogen dioxide (NO2) | 0.316 | D | CCCBDB | 2026-10-02 |
| dip:O3 | gas-phase dipole moment of Ozone (O3) | 0.530 | D | CCCBDB | 2026-10-02 |
| dip:H2S | gas-phase dipole moment of Hydrogen sulfide (H2S) | 0.977 | D | CCCBDB | 2026-10-02 |
| dip:SO2 | gas-phase dipole moment of Sulfur dioxide (SO2) | 1.633 | D | CCCBDB | 2026-10-02 |
| dip:NH3 | gas-phase dipole moment of Ammonia (NH3) | 1.476 | D | CCCBDB | 2026-10-02 |
| dip:H2CO | gas-phase dipole moment of Formaldehyde (H2CO) | 2.332 | D | CCCBDB | 2026-10-02 |
| dip:NF3 | gas-phase dipole moment of Nitrogen trifluoride (NF3) | 0.235 | D | CCCBDB | 2026-10-02 |
| dip:PH3 | gas-phase dipole moment of Phosphine (PH3) | 0.580 | D | CCCBDB | 2026-10-02 |
| dip:PCl3 | gas-phase dipole moment of Phosphorus trichloride (PCl3) | 0.560 | D | CCCBDB | 2026-10-02 |
| dip:CH3Cl | gas-phase dipole moment of Methyl chloride (CH3Cl) | 1.870 | D | CCCBDB | 2026-10-02 |
| dip:CH2Cl2 | gas-phase dipole moment of Methylene chloride (CH2Cl2) | 1.620 | D | CCCBDB | 2026-10-02 |
| dip:CHCl3 | gas-phase dipole moment of Chloroform (CHCl3) | 1.040 | D | CCCBDB | 2026-10-02 |
| dip:CCl4 | gas-phase dipole moment of Carbon tetrachloride (CCl4) | 0.000 | D | CCCBDB | 2026-10-02 |
| dip:CH3CN | gas-phase dipole moment of Acetonitrile (CH3CN) | 3.919 | D | CCCBDB | 2026-10-02 |
| dip:CH3OH | gas-phase dipole moment of Methyl alcohol (CH3OH) | 1.672 | D | CCCBDB | 2026-10-02 |
| dip:CH3NO2 | gas-phase dipole moment of Methane, nitro- (CH3NO2) | 3.460 | D | CCCBDB | 2026-10-02 |
| dip:CH3COOH | gas-phase dipole moment of Acetic acid (CH3COOH) | 1.700 | D | CCCBDB | 2026-10-02 |
| dip:CH3COCH3 | gas-phase dipole moment of Acetone (CH3COCH3) | 2.880 | D | CCCBDB | 2026-10-02 |
| dip:CH3SOCH3 | gas-phase dipole moment of Dimethyl sulfoxide (CH3SOCH3) | 3.960 | D | CCCBDB | 2026-10-02 |
| dip:pyridine | gas-phase dipole moment of Pyridine (C5H5N) | 2.190 | D | CCCBDB | 2026-10-02 |
| dip:C6H6 | gas-phase dipole moment of Benzene (C6H6) | 0.000 | D | CCCBDB | 2026-10-02 |
| dip:EtOAc | gas-phase dipole moment of Ethyl acetate (C4H8O2) | 1.780 | D | CCCBDB | 2026-10-02 |
| dip:toluene | gas-phase dipole moment of toluene (C6H5CH3) | 0.332 | D | CCCBDB | 2026-10-02 |
| dip:Et2O | gas-phase dipole moment of Ethoxy ethane (C4H10O) | 1.150 | D | CCCBDB | 2026-10-02 |
| dip:C2H5OH | gas-phase dipole moment of ethanol (trans conformer, state 1A') | 1.520 | D | CCCBDB | 2026-10-02 |
| geo:H2O2.rOH | experimental bond length rOH of H2O2 (ref. 1962Red/Ols:1311) | 0.950 | angstrom | CCCBDB | 2026-10-02 |
| geo:H2O2.rOO | experimental bond length rOO of H2O2 (ref. 1962Red/Ols:1311) | 1.475 | angstrom | CCCBDB | 2026-10-02 |
| geo:H2O2.aHOO | experimental angle aHOO of H2O2 (ref. 1962Red/Ols:1311) | 94.8 | degree | CCCBDB | 2026-10-02 |
| geo:H2O2.dHOOH | experimental angle dHOOH of H2O2 (ref. 1962Red/Ols:1311) | 119.8 | degree | CCCBDB | 2026-10-02 |
| geo:N2O.rNN | experimental bond length rNN of N2O (ref. 1966Herzberg) | 1.128 | angstrom | CCCBDB | 2026-10-02 |
| geo:N2O.rNO | experimental bond length rNO of N2O (ref. 1966Herzberg) | 1.184 | angstrom | CCCBDB | 2026-10-02 |
| geo:N2O.aNNO | experimental angle aNNO of N2O (ref. 1966Herzberg) | 180 | degree | CCCBDB | 2026-10-02 |
| geo:HCN.rCH | experimental bond length rCH of HCN (ref. 1966Herzberg) | 1.064 | angstrom | CCCBDB | 2026-10-02 |
| geo:HCN.rCN | experimental bond length rCN of HCN (ref. 1966Herzberg) | 1.156 | angstrom | CCCBDB | 2026-10-02 |
| geo:HCN.aHCN | experimental angle aHCN of HCN (ref. 1966Herzberg) | 180 | degree | CCCBDB | 2026-10-02 |
| geo:CH3OH.rOH | experimental bond length rOH of CH3OH (ref. 1955Ven/Gor:1200) | 0.956 | angstrom | CCCBDB | 2026-10-02 |
| geo:CH3OH.rCO | experimental bond length rCO of CH3OH (ref. 1955Ven/Gor:1200) | 1.427 | angstrom | CCCBDB | 2026-10-02 |
| geo:CH3OH.rCH | experimental bond length rCH of CH3OH (ref. 1955Ven/Gor:1200) | 1.096 | angstrom | CCCBDB | 2026-10-02 |
| geo:CH3OH.aHCH | experimental angle aHCH of CH3OH (ref. 1955Ven/Gor:1200) | 109.03 | degree | CCCBDB | 2026-10-02 |
| geo:CH3OH.aHOC | experimental angle aHOC of CH3OH (ref. 1955Ven/Gor:1200) | 108.87 | degree | CCCBDB | 2026-10-02 |
| geo:CH3OH.dHCOH | experimental angle dHCOH of CH3OH (ref. 1955Ven/Gor:1200) | 180 | degree | CCCBDB | 2026-10-02 |
| geo:H2CO2.rCO | experimental bond length rCO of H2CO2 (ref. 1966Herzberg) | 1.202 | angstrom | CCCBDB | 2026-10-02 |
| geo:H2CO2.rCO2 | experimental bond length rCO of H2CO2 (ref. 1966Herzberg) | 1.343 | angstrom | CCCBDB | 2026-10-02 |
| geo:H2CO2.rCH | experimental bond length rCH of H2CO2 (ref. 1966Herzberg) | 1.097 | angstrom | CCCBDB | 2026-10-02 |
| geo:H2CO2.rOH | experimental bond length rOH of H2CO2 (ref. 1966Herzberg) | 0.972 | angstrom | CCCBDB | 2026-10-02 |
| geo:H2CO2.aOCO | experimental angle aOCO of H2CO2 (ref. 1966Herzberg) | 124.9 | degree | CCCBDB | 2026-10-02 |
| geo:H2CO2.aHCO | experimental angle aHCO of H2CO2 (ref. 1966Herzberg) | 124.1 | degree | CCCBDB | 2026-10-02 |
| geo:H2CO2.aHOC | experimental angle aHOC of H2CO2 (ref. 1966Herzberg) | 106.3 | degree | CCCBDB | 2026-10-02 |
| bp:CH4 | normal boiling point of methane (PubChem CID 297, Boiling Point section: -161.50 degC; the WebBook gives only an average, 111 +- 2 K) | -161.5 | degC | PUBCHEM | 2026-10-02 |
| bp:H2O | normal boiling point of H2O (WebBook AVG; N/A) | 373.17 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:H2S | normal boiling point of H2S (WebBook N/A; Goodwin, 1983) | 212.87 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:HF | normal boiling point of HF (WebBook N/A; Streng, 1971) | 292.7 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:C2H6 | normal boiling point of C2H6 (WebBook AVG; N/A) | 184.6 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:C3H8 | normal boiling point of C3H8 (WebBook AVG; N/A) | 231.1 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:C4H10 | normal boiling point of C4H10 (WebBook AVG; N/A) | 273 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:C5H12 | normal boiling point of C5H12 (WebBook AVG; N/A) | 309.2 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:C6H14 | normal boiling point of C6H14 (WebBook AVG; N/A) | 341.9 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:C7H16 | normal boiling point of C7H16 (WebBook AVG; N/A) | 371.5 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:C8H18 | normal boiling point of C8H18 (WebBook AVG; N/A) | 398.7 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:C9H20 | normal boiling point of C9H20 (WebBook AVG; N/A) | 423.8 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:C10H22 | normal boiling point of C10H22 (WebBook AVG; N/A) | 447.2 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:Ar | normal boiling point of Ar (WebBook, the 87.28 K entry; the other entry, 87.5 K from Streng 1971, is the outlier) | 87.28 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:Kr | normal boiling point of Kr (WebBook N/A; Ziegler, Yarbrough, et al., 1964) | 119.78 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:Xe | normal boiling point of Xe (WebBook N/A; Ziegler, Mullins, et al., 1966) | 165.02 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:F2 | normal boiling point of F2 (WebBook N/A; Streng, 1971) | 85.2 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:Cl2 | normal boiling point of Cl2 (WebBook N/A; Thiele and Schulte, 1920) | 239.5 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:SiH4 | normal boiling point of silane (PubChem, Boiling Point section; HSDB, at 760 mmHg) | -112 | degC | PUBCHEM | 2026-10-02 |
| bp:GeH4 | normal boiling point of germane (PubChem, Boiling Point section; CRC Handbook via PubChem) | -88.1 | degC | PUBCHEM | 2026-10-02 |
| bp:NH3 | normal boiling point of ammonia (PubChem, Boiling Point section; at 760 mm Hg) | -33.35 | degC | PUBCHEM | 2026-10-02 |
| bp:PH3 | normal boiling point of phosphine (PubChem, Boiling Point section; at 760 mm Hg) | -87.75 | degC | PUBCHEM | 2026-10-02 |
| bp:AsH3 | normal boiling point of arsine (PubChem, Boiling Point section) | -62.5 | degC | PUBCHEM | 2026-10-02 |
| bp:SbH3 | normal boiling point of stibine (PubChem, Boiling Point section; at 760 mm Hg) | -18.4 | degC | PUBCHEM | 2026-10-02 |
| bp:H2Se | normal boiling point of hydrogen selenide (PubChem, Boiling Point section) | -41.3 | degC | PUBCHEM | 2026-10-02 |
| bp:HCl | normal boiling point of hydrogen chloride (PubChem, Boiling Point section; at 760 mm Hg) | -85.05 | degC | PUBCHEM | 2026-10-02 |
| bp:HBr | normal boiling point of hydrogen bromide (PubChem, Boiling Point section) | -66.38 | degC | PUBCHEM | 2026-10-02 |
| bp:HI | normal boiling point of hydrogen iodide (PubChem, Boiling Point section; at 760 mm Hg) | -35.1 | degC | PUBCHEM | 2026-10-02 |
| bp:He | normal boiling point of helium (PubChem, Boiling Point section) | -268.928 | degC | PUBCHEM | 2026-10-02 |
| bp:Ne | normal boiling point of neon (PubChem, Boiling Point section) | -246.053 | degC | PUBCHEM | 2026-10-02 |
| bp:Br2 | normal boiling point of bromine (PubChem, Boiling Point section) | 58.8 | degC | PUBCHEM | 2026-10-02 |
| bp:I2 | normal boiling point of iodine (PubChem, Boiling Point section) | 184.4 | degC | PUBCHEM | 2026-10-02 |
| epsr:H2O | relative permittivity of liquid water at 25 degC, 0.1 MPa (IAPWS R8-97, the modern consensus; replaces NBS C514's 1951 value 78.54, main session 2026-10-03; agrees with Book 4's eps:H2O.25C) | 78.4 | - | IAPWS-R8-97 | 2026-10-03 |
| epsr:CH3OH | relative permittivity of liquid methanol at 25 degC (PDF p. 13) | 32.63 | - | NBS-C514 | 2026-10-02 |
| epsr:C2H5OH | relative permittivity of liquid ethanol at 25 degC (PDF p. 16) | 24.3 | - | NBS-C514 | 2026-10-02 |
| epsr:CH3COCH3 | relative permittivity of liquid propanone (acetone) at 25 degC (PDF p. 18) | 20.7 | - | NBS-C514 | 2026-10-02 |
| epsr:CH3CN | relative permittivity of liquid acetonitrile at 20 degC (PDF p. 15) | 37.5 | - | NBS-C514 | 2026-10-02 |
| epsr:Et2O | relative permittivity of liquid ethoxyethane (ethyl ether) at 20 degC (PDF p. 22) | 4.335 | - | NBS-C514 | 2026-10-02 |
| epsr:EtOAc | relative permittivity of liquid ethyl ethanoate at 25 degC (PDF p. 20) | 6.02 | - | NBS-C514 | 2026-10-02 |
| epsr:C6H6 | relative permittivity of liquid benzene at 20 degC (PDF p. 26) | 2.284 | - | NBS-C514 | 2026-10-02 |
| epsr:CCl4 | relative permittivity of liquid tetrachloromethane at 20 degC (PDF p. 13) | 2.238 | - | NBS-C514 | 2026-10-02 |
| epsr:C6H12 | relative permittivity of liquid cyclohexane at 20 degC (PDF p. 28) | 2.023 | - | NBS-C514 | 2026-10-02 |
| epsr:C6H14 | relative permittivity of liquid hexane at 20 degC (PDF p. 29) | 1.89 | - | NBS-C514 | 2026-10-02 |
| epsr:CHCl3 | relative permittivity of liquid trichloromethane at 20 degC (PDF p. 13) | 4.806 | - | NBS-C514 | 2026-10-02 |
| epsr:CH2Cl2 | relative permittivity of liquid dichloromethane at 20 degC (PDF p. 13) | 9.08 | - | NBS-C514 | 2026-10-02 |
| epsr:HCONH2 | relative permittivity of liquid methanamide (formamide) at 20 degC (PDF p. 13) | 109 | - | NBS-C514 | 2026-10-02 |
| epsr:C5H5N | relative permittivity of liquid pyridine at 25 degC (PDF p. 22) | 12.3 | - | NBS-C514 | 2026-10-02 |
| bp:C2H5OH | normal boiling point of C2H5OH (WebBook AVG; N/A) | 351.5 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:CH3OCH3 | normal boiling point of CH3OCH3 (WebBook N/A; Weast and Grasselli, 1989) | 248.2 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:CH3COOH | normal boiling point of CH3COOH (WebBook AVG; N/A) | 391.2 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:C2H5NH2 | normal boiling point of C2H5NH2 (WebBook AVG; N/A) | 291 | K | WEBBOOK-PHASE | 2026-10-02 |
| bp:CH3OH | normal boiling point of CH3OH (WebBook AVG; N/A) | 337.8 | K | WEBBOOK-PHASE | 2026-10-02 |
| lat:Cu | lattice parameter: a of copper, FCC (COD 9008468, Wyckoff 1963) | 3.61496 | angstrom | COD | 2026-10-02 |
| lat:Al | lattice parameter: a of aluminium, FCC (COD 9008460, Wyckoff 1963) | 4.04958 | angstrom | COD | 2026-10-02 |
| lat:Ag | lattice parameter: a of silver, FCC (COD 9008459, Wyckoff 1963) | 4.0862 | angstrom | COD | 2026-10-02 |
| lat:Au | lattice parameter: a of gold, FCC (COD 9008463, Wyckoff 1963) | 4.07825 | angstrom | COD | 2026-10-02 |
| lat:Na | lattice parameter: a of sodium, BCC, 293 K (COD 9008545, Wyckoff 1963) | 4.2906 | angstrom | COD | 2026-10-02 |
| lat:W | lattice parameter: a of tungsten, BCC (COD 9008558, Wyckoff 1963) | 3.16469 | angstrom | COD | 2026-10-02 |
| lat:Fe-alpha | lattice parameter: a of alpha-iron, BCC, 298 K (COD 9008536, Wyckoff 1963) | 2.8665 | angstrom | COD | 2026-10-02 |
| lat:Fe-alpha-1189 | lattice parameter: a of alpha-iron, BCC, at 1189 K (COD 9013484, 1955, lattice expansion of iron) | 2.898 | angstrom | COD | 2026-10-02 |
| lat:Fe-gamma-1189 | lattice parameter: a of gamma-iron, FCC, at 1189 K (COD 9012706, 1955, lattice expansion of iron) | 3.639 | angstrom | COD | 2026-10-02 |
| lat:Mg.a | lattice parameter: a of magnesium, HCP (COD 9008506, Wyckoff 1963) | 3.20927 | angstrom | COD | 2026-10-02 |
| lat:Mg.c | lattice parameter: c of magnesium, HCP (COD 9008506, Wyckoff 1963) | 5.21033 | angstrom | COD | 2026-10-02 |
| lat:Zn.a | lattice parameter: a of zinc, HCP (COD 9008522, Wyckoff 1963) | 2.6648 | angstrom | COD | 2026-10-02 |
| lat:Zn.c | lattice parameter: c of zinc, HCP (COD 9008522, Wyckoff 1963) | 4.9467 | angstrom | COD | 2026-10-02 |
| lat:NaCl | lattice parameter: a of sodium chloride, rock salt (COD 9008678, Wyckoff 1963) | 5.64056 | angstrom | COD | 2026-10-02 |
| lat:CsCl | lattice parameter: a of caesium chloride, Pm-3m (COD 9008789, Wyckoff 1963) | 4.123 | angstrom | COD | 2026-10-02 |
| lat:ZnS | lattice parameter: a of sphalerite ZnS, F-43m (COD 9000107, Skinner 1961, synthetic) | 5.4093 | angstrom | COD | 2026-10-02 |
| lat:CaF2 | lattice parameter: a of fluorite CaF2 (COD 9009005, Wyckoff 1963) | 5.46295 | angstrom | COD | 2026-10-02 |
| lat:Li2O | lattice parameter: a of Li2O, antifluorite (COD 9009059, Wyckoff 1963) | 4.619 | angstrom | COD | 2026-10-02 |
| lat:C-diamond | lattice parameter: a of diamond (COD 9008564, Wyckoff 1963) | 3.56679 | angstrom | COD | 2026-10-02 |
| lat:C-graphite.a | lattice parameter: a of graphite, P63mc (COD 9008569, Wyckoff 1963) | 2.456 | angstrom | COD | 2026-10-02 |
| lat:C-graphite.c | lattice parameter: c of graphite (COD 9008569, Wyckoff 1963) | 6.696 | angstrom | COD | 2026-10-02 |
| lat:Si | lattice parameter: a of silicon, diamond type, 300 K (COD 9008565, Wyckoff 1963) | 5.4307 | angstrom | COD | 2026-10-02 |
| rho:Cu | density of solid Cu near room temperature (PubChem periodic table) | 8.933 | g/cm3 | PUBCHEM-PT | 2026-10-02 |
| rho:Al | density of solid Al near room temperature (PubChem periodic table) | 2.70 | g/cm3 | PUBCHEM-PT | 2026-10-02 |
| rho:Ag | density of solid Ag near room temperature (PubChem periodic table) | 10.501 | g/cm3 | PUBCHEM-PT | 2026-10-02 |
| rho:Na | density of solid Na near room temperature (PubChem periodic table) | 0.97 | g/cm3 | PUBCHEM-PT | 2026-10-02 |
| rho:W | density of solid W near room temperature (PubChem periodic table) | 19.3 | g/cm3 | PUBCHEM-PT | 2026-10-02 |
| rho:Mg | density of solid Mg near room temperature (PubChem periodic table) | 1.74 | g/cm3 | PUBCHEM-PT | 2026-10-02 |
| lat:Ni | lattice parameter: a of nickel, FCC (COD 9008476, Wyckoff 1963) | 3.52387 | angstrom | COD | 2026-10-02 |
| lat:Fe-gamma-1661 | lattice parameter: a of gamma-iron, FCC, at 1661 K (COD 9012714, 1955, lattice expansion of iron) | 3.679 | angstrom | COD | 2026-10-02 |
| lat:Fe-delta-1662 | lattice parameter: a of delta-iron, BCC, at 1662 K (COD 9013485, 1955, lattice expansion of iron) | 2.925 | angstrom | COD | 2026-10-02 |
| rho:CaF2 | density of calcium fluoride (HSDB, at 25 degC; CID 84512) | 3.18 | g/cm3 | PUBCHEM | 2026-10-02 |
| rho:CsCl | density of caesium chloride (HSDB, at 25 degC; CID 24293) | 3.99 | g/cm3 | PUBCHEM | 2026-10-02 |
| rho:ZnS | density of zinc sulfide, sphalerite (CID 9833931) | 4.04 | g/cm3 | PUBCHEM | 2026-10-02 |
| rho:Li2O | density of lithium oxide (HSDB, at 25 degC; CID 166630) | 2.013 | g/cm3 | PUBCHEM | 2026-10-02 |
| rho:Si | density of solid Si near room temperature (PubChem periodic table) | 2.3296 | g/cm3 | PUBCHEM-PT | 2026-10-02 |
| lat:RbCl | lattice parameter: a of rubidium chloride, rock-salt type, ambient conditions (COD 9008707, Wyckoff 1963) | 6.581 | angstrom | COD | 2026-10-02 |
| dfg:O2_g | standard Gibbs energy of formation of O2(g) at 298.15 K (table page 2-37) | 0 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:O3_g | standard Gibbs energy of formation of O3(g) at 298.15 K (table page 2-37) | 163.2 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:H+_ao | standard Gibbs energy of formation of H+(ao) at 298.15 K (table page 2-38) | 0 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:OH-_ao | standard Gibbs energy of formation of OH-(ao) at 298.15 K (table page 2-38) | -157.244 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:H2O_l | standard Gibbs energy of formation of H2O(l) at 298.15 K (table page 2-38) | -237.129 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:H2O2_ao | standard Gibbs energy of formation of H2O2(ao) at 298.15 K (table page 2-38) | -134.03 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:HO2-_ao | standard Gibbs energy of formation of HO2-(ao) at 298.15 K (table page 2-38) | -67.3 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:H2_g | standard Gibbs energy of formation of H2(g) at 298.15 K (table page 2-38) | 0 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:F-_ao | standard Gibbs energy of formation of F-(ao) at 298.15 K (table page 2-45) | -278.79 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:HF_ao | standard Gibbs energy of formation of HF(ao) at 298.15 K (table page 2-45) | -296.82 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Cl-_ao | standard Gibbs energy of formation of Cl-(ao) at 298.15 K (table page 2-47) | -131.228 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Cl2_g | standard Gibbs energy of formation of Cl2(g) at 298.15 K (table page 2-47) | 0 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Cl2_ao | standard Gibbs energy of formation of Cl2(ao) at 298.15 K (table page 2-47) | 6.94 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:ClO-_ao | standard Gibbs energy of formation of ClO-(ao) at 298.15 K (table page 2-47) | -36.8 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:ClO3-_ao | standard Gibbs energy of formation of ClO3-(ao) at 298.15 K (table page 2-47) | -7.95 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:ClO4-_ao | standard Gibbs energy of formation of ClO4-(ao) at 298.15 K (table page 2-47) | -8.52 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:HClO_ao | standard Gibbs energy of formation of HClO(ao) at 298.15 K (table page 2-48) | -79.9 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Br-_ao | standard Gibbs energy of formation of Br-(ao) at 298.15 K (table page 2-50) | -103.96 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Br2_l | standard Gibbs energy of formation of Br2(l) at 298.15 K (table page 2-50) | 0 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Br2_ao | standard Gibbs energy of formation of Br2(ao) at 298.15 K (table page 2-50) | 3.93 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:I-_ao | standard Gibbs energy of formation of I-(ao) at 298.15 K (table page 2-52) | -51.57 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:I2_cr | standard Gibbs energy of formation of I2(cr) at 298.15 K (table page 2-52) | 0 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:I2_ao | standard Gibbs energy of formation of I2(ao) at 298.15 K (table page 2-52) | 16.4 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:I3-_ao | standard Gibbs energy of formation of I3-(ao) at 298.15 K (table page 2-52) | -51.4 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:IO3-_ao | standard Gibbs energy of formation of IO3-(ao) at 298.15 K (table page 2-52) | -128.0 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:S_cr | standard Gibbs energy of formation of S(cr) at 298.15 K (table page 2-56) | 0 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:SO2_g | standard Gibbs energy of formation of SO2(g) at 298.15 K (table page 2-56) | -300.194 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:SO3_g | standard Gibbs energy of formation of SO3(g) at 298.15 K (table page 2-57) | -371.06 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:SO32-_ao | standard Gibbs energy of formation of SO3^2-(ao) at 298.15 K (table page 2-57) | -486.5 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:SO42-_ao | standard Gibbs energy of formation of SO4^2-(ao) at 298.15 K (table page 2-57) | -744.53 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:S2O32-_ao | standard Gibbs energy of formation of S2O3^2-(ao) at 298.15 K (table page 2-57) | -522.5 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:S4O62-_ao | standard Gibbs energy of formation of S4O6^2-(ao) at 298.15 K (table page 2-57) | -1040.4 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:HS-_ao | standard Gibbs energy of formation of HS-(ao) at 298.15 K (table page 2-57) | 12.08 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:H2S_g | standard Gibbs energy of formation of H2S(g) at 298.15 K (table page 2-57) | -33.56 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:H2S_ao | standard Gibbs energy of formation of H2S(ao) at 298.15 K (table page 2-57) | -27.83 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:S2-_ao | standard Gibbs energy of formation of S^2-(ao) at 298.15 K (table page 2-56) | 85.8 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:HSO3-_ao | standard Gibbs energy of formation of HSO3-(ao) at 298.15 K (table page 2-57) | -527.73 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:HSO4-_ao | standard Gibbs energy of formation of HSO4-(ao) at 298.15 K (table page 2-57) | -755.91 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:H2SO3_ao | standard Gibbs energy of formation of H2SO3(ao) at 298.15 K (table page 2-57) | -537.81 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:N2_g | standard Gibbs energy of formation of N2(g) at 298.15 K (table page 2-64) | 0 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:NO_g | standard Gibbs energy of formation of NO(g) at 298.15 K (table page 2-64) | 86.55 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:NO2_g | standard Gibbs energy of formation of NO2(g) at 298.15 K (table page 2-64) | 51.31 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:NO2-_ao | standard Gibbs energy of formation of NO2-(ao) at 298.15 K (table page 2-64) | -32.2 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:NO3-_ao | standard Gibbs energy of formation of NO3-(ao) at 298.15 K (table page 2-64) | -108.74 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:N2O_g | standard Gibbs energy of formation of N2O(g) at 298.15 K (table page 2-64) | 104.2 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:N2O4_g | standard Gibbs energy of formation of N2O4(g) at 298.15 K (table page 2-64) | 97.89 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:NH3_g | standard Gibbs energy of formation of NH3(g) at 298.15 K (table page 2-64) | -16.45 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:NH3_ao | standard Gibbs energy of formation of NH3(ao) at 298.15 K (table page 2-64) | -26.5 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:NH4+_ao | standard Gibbs energy of formation of NH4+(ao) at 298.15 K (table page 2-65) | -79.31 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:HNO2_ao | standard Gibbs energy of formation of HNO2(ao) at 298.15 K (table page 2-65) | -50.6 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:PO43-_ao | standard Gibbs energy of formation of PO4^3-(ao) at 298.15 K (table page 2-73) | -1018.7 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:HPO42-_ao | standard Gibbs energy of formation of HPO4^2-(ao) at 298.15 K (table page 2-73) | -1089.15 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:H2PO4-_ao | standard Gibbs energy of formation of H2PO4-(ao) at 298.15 K (table page 2-73) | -1130.28 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:H3PO4_ao | standard Gibbs energy of formation of H3PO4(ao) at 298.15 K (table page 2-74) | -1142.54 | kJ/mol | NBS-82 | 2026-10-02 |
| pka:ethanoic | acetic acid (ethanoic acid), pKa at 25 degC (serjeant2043, ref E13, m = 0.01) | 4.76 | - | IUPAC-PKA | 2026-10-02 |
| pka:methanoic | methanoic acid, pKa at 25 degC (Reliable) | 3.737 | - | IUPAC-PKA | 2026-10-02 |
| pka:benzoic | benzoic acid, pKa at 25 degC (serjeant3388, ref K30, Reliable) | 4.205 | - | IUPAC-PKA | 2026-10-02 |
| pka:propanoic | propanoic acid, pKa at 25 degC (serjeant2143, Approximate, ref S1, I = 0.0025-1.8) | 4.89 | - | IUPAC-PKA | 2026-10-02 |
| pka:chloroethanoic | chloroacetic acid, pKa at 25 degC (serjeant2064, ref S89, Reliable) | 2.866 | - | IUPAC-PKA | 2026-10-02 |
| pka:dichloroethanoic | dichloroacetic acid, pKa at 25 degC (serjeant2058, ref K69, Approximate) | 1.35 | - | IUPAC-PKA | 2026-10-02 |
| pka:trichloroethanoic | trichloroacetic acid, pKa at 25 degC (serjeant2054, ref K69, Approximate) | 0.512 | - | IUPAC-PKA | 2026-10-02 |
| pka:trifluoroethanoic | trifluoroacetic acid, pKa at 25 degC (serjeant2056, ref K69, Approximate) | 0.52 | - | IUPAC-PKA | 2026-10-02 |
| pka:phenol | phenol, pKa at 25 degC (serjeant2825, ref F12, Reliable) | 9.994 | - | IUPAC-PKA | 2026-10-02 |
| pka:4-nitrophenol | 4-nitrophenol, pKa at 25 degC (serjeant2998, ref A47, Reliable) | 7.156 | - | IUPAC-PKA | 2026-10-02 |
| pka:3-nitrophenol | 3-nitrophenol, pKa at 25 degC (serjeant2997, ref R38, Reliable) | 8.355 | - | IUPAC-PKA | 2026-10-02 |
| pka:2-nitrophenol | 2-nitrophenol, pKa at 25 degC (serjeant2996, ref R37, Reliable) | 7.23 | - | IUPAC-PKA | 2026-10-02 |
| pka:methanol | methanol, pKa at 25 degC (serjeant2004, ref B8, Uncertain) | 15.5 | - | IUPAC-PKA | 2026-10-02 |
| pka:ethanol | ethanol, pKa at 25 degC (serjeant2046, ref M126, Uncertain) | 15.93 | - | IUPAC-PKA | 2026-10-02 |
| pka:2-propanol | propan-2-ol, pKa at 25 degC (serjeant2149, ref M126, Uncertain) | 17.1 | - | IUPAC-PKA | 2026-10-02 |
| pka:tBuOH | 2-methylpropan-2-ol, pKa at 25 degC (serjeant2333, ref M126, Uncertain) | 19.2 | - | IUPAC-PKA | 2026-10-02 |
| pka:methylammonium | methylammonium (pKaH of methylamine) at 25 degC (perrin2, ref H31, Reliable) | 10.657 | - | IUPAC-PKA | 2026-10-02 |
| pka:anilinium | anilinium (pKaH of aniline) at 25 degC (perrin387, ref B66, Reliable) | 4.603 | - | IUPAC-PKA | 2026-10-02 |
| pka:pyridinium | pyridinium (pKaH of pyridine) at 25 degC (perrin_supp5003, ref G30, Reliable) | 5.229 | - | IUPAC-PKA | 2026-10-02 |
| pka:ascorbic1 | ascorbic acid, first pKa at 25 degC (serjeant2861, ref K25, I = 0.1, Approximate) | 4.04 | - | IUPAC-PKA | 2026-10-02 |
| pka:glycine1 | glycine, pKa of the carboxylic group (pKaH1) at 25 degC (perrin3140, ref K26, Reliable) | 2.3503 | - | IUPAC-PKA | 2026-10-02 |
| pka:glycine2 | glycine, pKa of the ammonium group at 25 degC (perrin3140, ref K26, Reliable) | 9.7796 | - | IUPAC-PKA | 2026-10-02 |
| dfg:CO_g | standard Gibbs energy of formation of CO(g) at 298.15 K (table page 2-83) | -137.168 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:CO2_g | standard Gibbs energy of formation of CO2(g) at 298.15 K (table page 2-83) | -394.359 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:CO2_ao | standard Gibbs energy of formation of CO2(ao) at 298.15 K (table page 2-83) | -385.98 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:CO32-_ao | standard Gibbs energy of formation of CO3^2-(ao) at 298.15 K (table page 2-83) | -527.81 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:HCO3-_ao | standard Gibbs energy of formation of HCO3-(ao) at 298.15 K (table page 2-83) | -586.77 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:CH4_g | standard Gibbs energy of formation of CH4(g) at 298.15 K (table page 2-83) | -50.72 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:HCOO-_ao | standard Gibbs energy of formation of HCOO-(ao) at 298.15 K (table page 2-83) | -351.0 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:HCOOH_ao | standard Gibbs energy of formation of HCOOH(ao) at 298.15 K (table page 2-83) | -372.3 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:H2CO3_ao | standard Gibbs energy of formation of H2CO3(ao) at 298.15 K (table page 2-83) | -623.08 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Ag_cr | standard Gibbs energy of formation of Ag(cr) at 298.15 K (table page 2-160) | 0 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Ag+_ao | standard Gibbs energy of formation of Ag+(ao) at 298.15 K (table page 2-160) | 77.107 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Ag2O_cr | standard Gibbs energy of formation of Ag2O(cr) at 298.15 K (table page 2-160) | -11.20 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:AgCl_cr | standard Gibbs energy of formation of AgCl(cr) at 298.15 K (table page 2-160) | -109.789 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:AgCl2-_ao | standard Gibbs energy of formation of AgCl2-(ao) at 298.15 K (table page 2-160) | -215.4 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:AgBr_cr | standard Gibbs energy of formation of AgBr(cr) at 298.15 K (table page 2-160) | -96.90 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:AgI_cr | standard Gibbs energy of formation of AgI(cr) at 298.15 K (table page 2-161) | -66.19 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Ag2S_cr | standard Gibbs energy of formation of Ag2S(cr) at 298.15 K (table page 2-161) | -40.67 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Ag2SO4_cr | standard Gibbs energy of formation of Ag2SO4(cr) at 298.15 K (table page 2-161) | -618.41 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:AgNH3+_ao | standard Gibbs energy of formation of AgNH3+(ao) at 298.15 K (table page 2-162) | 31.68 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Ag_NH32+_ao | standard Gibbs energy of formation of Ag(NH3)2+(ao) at 298.15 K (table page 2-162) | -17.12 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Zn2+_ao | standard Gibbs energy of formation of Zn2+(ao) at 298.15 K (table page 2-138) | -147.06 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:ZnO_cr | standard Gibbs energy of formation of ZnO(cr) at 298.15 K (table page 2-138) | -318.30 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:ZnOH+_ao | standard Gibbs energy of formation of ZnOH+(ao) at 298.15 K (table page 2-138) | -330.1 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Zn_OH2_ao | standard Gibbs energy of formation of Zn(OH)2(ao) at 298.15 K (table page 2-138) | -522.73 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Zn_OH3-_ao | standard Gibbs energy of formation of Zn(OH)3-(ao) at 298.15 K (table page 2-138) | -694.22 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Zn_OH42-_ao | standard Gibbs energy of formation of Zn(OH)4^2-(ao) at 298.15 K (table page 2-138) | -858.52 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Cu+_ao | standard Gibbs energy of formation of Cu+(ao) at 298.15 K (table page 2-154) | 49.98 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Cu2+_ao | standard Gibbs energy of formation of Cu2+(ao) at 298.15 K (table page 2-154) | 65.49 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:CuO_cr | standard Gibbs energy of formation of CuO(cr) at 298.15 K (table page 2-154) | -129.7 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Cu2O_cr | standard Gibbs energy of formation of Cu2O(cr) at 298.15 K (table page 2-154) | -146.0 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:CuCl_cr | standard Gibbs energy of formation of CuCl(cr) at 298.15 K (table page 2-154) | -119.86 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Fe2+_ao | standard Gibbs energy of formation of Fe2+(ao) at 298.15 K (table page 2-177) | -78.90 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Fe3+_ao | standard Gibbs energy of formation of Fe3+(ao) at 298.15 K (table page 2-177) | -4.7 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Fe2O3_cr | standard Gibbs energy of formation of Fe2O3(cr) (hematite) at 298.15 K (table page 2-177) | -742.2 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:FeOH+_ao | standard Gibbs energy of formation of FeOH+(ao) at 298.15 K (table page 2-177) | -277.4 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:FeOH2+_ao | standard Gibbs energy of formation of FeOH2+(ao) at 298.15 K (table page 2-177) | -229.41 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Fe_OH2_cr | standard Gibbs energy of formation of Fe(OH)2(cr) (precipitated) at 298.15 K (table page 2-177) | -486.5 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Fe_OH3_cr | standard Gibbs energy of formation of Fe(OH)3(cr) (precipitated) at 298.15 K (table page 2-177) | -696.5 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Fe_cr | standard Gibbs energy of formation of Fe(cr) at 298.15 K (table page 2-177) | 0 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Mg2+_ao | standard Gibbs energy of formation of Mg2+(ao) at 298.15 K (table page 2-260) | -454.8 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Mg_OH2_cr | standard Gibbs energy of formation of Mg(OH)2(cr) at 298.15 K (table page 2-260) | -833.51 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:MgO_cr | standard Gibbs energy of formation of MgO(cr) at 298.15 K (table page 2-260) | -569.43 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:MgF2_cr | standard Gibbs energy of formation of MgF2(cr) at 298.15 K (table page 2-260) | -1070.2 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Mg_cr | standard Gibbs energy of formation of Mg(cr) at 298.15 K (table page 2-260) | 0 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Ca2+_ao | standard Gibbs energy of formation of Ca2+(ao) at 298.15 K (table page 2-267) | -553.58 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:CaO_cr | standard Gibbs energy of formation of CaO(cr) at 298.15 K (table page 2-267) | -604.03 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Ca_OH2_cr | standard Gibbs energy of formation of Ca(OH)2(cr) at 298.15 K (table page 2-267) | -898.49 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:CaF2_cr | standard Gibbs energy of formation of CaF2(cr) at 298.15 K (table page 2-267) | -1167.3 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Ca_cr | standard Gibbs energy of formation of Ca(cr) at 298.15 K (table page 2-267) | 0 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Ba2+_ao | standard Gibbs energy of formation of Ba2+(ao) at 298.15 K (table page 2-282) | -560.77 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:BaSO4_cr | standard Gibbs energy of formation of BaSO4(cr) at 298.15 K (table page 2-284) | -1362.2 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Al3+_ao | standard Gibbs energy of formation of Al3+(ao) at 298.15 K (table page 2-127) | -485. | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Al_OH4-_ao | standard Gibbs energy of formation of Al(OH)4-(ao) at 298.15 K (table page 2-127) | -1305.3 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:AlOH2+_ao | standard Gibbs energy of formation of AlOH2+(ao) at 298.15 K (table page 2-127) | -694.1 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:CrO42-_ao | standard Gibbs energy of formation of CrO4^2-(ao) at 298.15 K (table page 2-197) | -727.75 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Cr2O72-_ao | standard Gibbs energy of formation of Cr2O7^2-(ao) at 298.15 K (table page 2-197) | -1301.1 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:HCrO4-_ao | standard Gibbs energy of formation of HCrO4-(ao) at 298.15 K (table page 2-197) | -764.7 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Cr2O3_cr | standard Gibbs energy of formation of Cr2O3(cr) at 298.15 K (table page 2-197) | -1058.1 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Zn_OH2_cr | standard Gibbs energy of formation of Zn(OH)2(cr) (epsilon form) at 298.15 K (table page 2-138) | -555.07 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:CaCO3_cr | standard Gibbs energy of formation of CaCO3(cr) (calcite) at 298.15 K (table page 2-272) | -1128.79 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Al2O3.3H2O_cr | standard Gibbs energy of formation of Al2O3.3H2O(cr) (gibbsite) at 298.15 K (table page 2-127) | -2310.21 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Ag2CrO4_cr | standard Gibbs energy of formation of Ag2CrO4(cr) at 298.15 K (table page 2-200) | -641.76 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:CuNH32+_ao | standard Gibbs energy of formation of CuNH3^2+(ao) at 298.15 K (table page 2-156) | 15.60 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Cu_NH322+_ao | standard Gibbs energy of formation of Cu(NH3)2^2+(ao) at 298.15 K (table page 2-156) | -30.36 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Cu_NH332+_ao | standard Gibbs energy of formation of Cu(NH3)3^2+(ao) at 298.15 K (table page 2-156) | -72.97 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Cu_NH342+_ao | standard Gibbs energy of formation of Cu(NH3)4^2+(ao) at 298.15 K (table page 2-156) | -111.07 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:SCN-_ao | standard Gibbs energy of formation of SCN-(ao) at 298.15 K (table page 2-92) | 92.71 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:FeSCN2+_ao | standard Gibbs energy of formation of FeSCN^2+(ao) at 298.15 K (table page 2-181) | 71.1 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Fe_CN63-_ao | standard Gibbs energy of formation of Fe(CN)6^3-(ao) at 298.15 K (table page 2-181) | 729.4 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Fe_CN64-_ao | standard Gibbs energy of formation of Fe(CN)6^4-(ao) at 298.15 K (table page 2-181) | 695.08 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:FeF2+_ao | standard Gibbs energy of formation of FeF^2+(ao) at 298.15 K (table page 2-177) | -322.6 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Li+_ao | standard Gibbs energy of formation of Li+(ao) at 298.15 K (table page 2-290) | -293.31 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Na+_ao | standard Gibbs energy of formation of Na+(ao) at 298.15 K (table page 2-299) | -261.905 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:K+_ao | standard Gibbs energy of formation of K+(ao) at 298.15 K (table page 2-328) | -283.27 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Ni2+_ao | standard Gibbs energy of formation of Ni2+(ao) at 298.15 K (table page 2-166) | -45.6 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Pb2+_ao | standard Gibbs energy of formation of Pb2+(ao) at 298.15 K (table page 2-119) | -24.43 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:PbO2_cr | standard Gibbs energy of formation of PbO2(cr) at 298.15 K (table page 2-119) | -217.33 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Mn2+_ao | standard Gibbs energy of formation of Mn2+(ao) at 298.15 K (table page 2-191) | -228.1 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:MnO4-_ao | standard Gibbs energy of formation of MnO4-(ao) at 298.15 K (table page 2-191) | -447.2 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:MnO2_cr | standard Gibbs energy of formation of MnO2(cr) at 298.15 K (table page 2-191) | -465.14 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Hg22+_ao | standard Gibbs energy of formation of Hg2^2+(ao) at 298.15 K (table page 2-150) | 153.52 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Hg2+_ao | standard Gibbs energy of formation of Hg2+(ao) at 298.15 K (table page 2-150) | 164.40 | kJ/mol | NBS-82 | 2026-10-02 |
| dfg:Hg2Cl2_cr | standard Gibbs energy of formation of Hg2Cl2(cr) at 298.15 K (table page 2-150) | -210.745 | kJ/mol | NBS-82 | 2026-10-02 |
| logb:Ca-edta | log10 K of Ca2+ + edta4- = Ca(edta)2-, I = 0, 298.15 K (Table III-6) | 12.69 | - | NEA-TDB9 | 2026-10-02 |
| logb:Mg-edta | log10 K of Mg2+ + edta4- = Mg(edta)2-, I = 0, 298.15 K (Table III-6) | 10.90 | - | NEA-TDB9 | 2026-10-02 |
| logb:Ni-edta | log10 K of Ni2+ + edta4- = Ni(edta)2-, I = 0, 298.15 K (Table III-6) | 20.54 | - | NEA-TDB9 | 2026-10-02 |
| pka:edta1 | pKa of H4edta(aq) = H+ + H3edta-, I = 0, 298.15 K (Table III-6, log10 K = -2.230) | 2.23 | - | NEA-TDB9 | 2026-10-02 |
| pka:edta2 | pKa of H3edta- = H+ + H2edta2-, I = 0, 298.15 K (Table III-6, log10 K = -3.150) | 3.15 | - | NEA-TDB9 | 2026-10-02 |
| pka:edta3 | pKa of H2edta2- = H+ + Hedta3-, I = 0, 298.15 K (Table III-6, log10 K = -6.800) | 6.80 | - | NEA-TDB9 | 2026-10-02 |
| pka:edta4 | pKa of Hedta3- = H+ + edta4-, I = 0, 298.15 K (Table III-6, log10 K = -11.240) | 11.24 | - | NEA-TDB9 | 2026-10-02 |
| pks:CaC2O4.H2O | pKs (log10 K of formation from Ca2+ + ox2- + H2O) of calcium oxalate monohydrate, whewellite, I = 0, 298.15 K (Table III-2) | 8.73 | - | NEA-TDB9 | 2026-10-02 |
| lam:H+ | limiting molar ionic conductivity of H+ (H3O+) in water at 25 degC | 349.81 | S cm2/mol | NIST-SP260-142 | 2026-10-02 |
| lam:OH- | limiting molar ionic conductivity of OH- in water at 25 degC | 198.3 | S cm2/mol | NIST-SP260-142 | 2026-10-02 |
| lamsalt:HCl | limiting molar conductivity of HCl in water at 25 degC (Table 1) | 426 | S cm2/mol | NIST-JRES100 | 2026-10-02 |
| lamsalt:NaCl | limiting molar conductivity of NaCl in water at 25 degC (Table 1) | 126.5 | S cm2/mol | NIST-JRES100 | 2026-10-02 |
| lamsalt:KCl | limiting molar conductivity of KCl in water at 25 degC (Table 1) | 150 | S cm2/mol | NIST-JRES100 | 2026-10-02 |
| pka:methylorange | methyl orange, pKa of the acid (red) form, I = 0 (perrin_supp8125) | 3.47 | - | IUPAC-PKA | 2026-10-02 |
| pka:methylred | methyl red, pKa1 at 25 degC in acetate buffers (perrin3669) | 4.82 | - | IUPAC-PKA | 2026-10-02 |
| pka:phenolred | phenol red, pKa2 (serjeant6358, conditions not stated) | 7.92 | - | IUPAC-PKA | 2026-10-02 |
| pka:thymolblue2 | thymol blue, second (alkaline) pKa at 25 degC (perrin_supp8138) | 9.186 | - | IUPAC-PKA | 2026-10-02 |
| rot:ethane-V3 | ethane, threefold barrier to internal rotation V3 (Gurvich, Veyts, Alcock 1989, via CCCBDB exprotbar2x.asp?casno=74840) | 1024 | cm-1 | CCCBDB | 2026-10-02 |
| rot:butane-V1 | butane, torsional potential coefficient V1 about the central C-C bond, V = sum Vn/2 (1 - cos n phi), phi = 0 anti (Herrebout, van der Veken, Wang, Durig, J. Phys. Chem. 99, 578 (1995), via CCCBDB casno=106978) | 242 | cm-1 | CCCBDB | 2026-10-02 |
| rot:butane-V2 | butane, coefficient V2 (same source) | 43 | cm-1 | CCCBDB | 2026-10-02 |
| rot:butane-V3 | butane, coefficient V3 (same source) | 1146 | cm-1 | CCCBDB | 2026-10-02 |
| rot:butane-V4 | butane, coefficient V4 (same source) | 40 | cm-1 | CCCBDB | 2026-10-02 |
| rot:butane-V5 | butane, coefficient V5 (same source) | -6 | cm-1 | CCCBDB | 2026-10-02 |
| rot:butane-V6 | butane, coefficient V6 (same source) | -36 | cm-1 | CCCBDB | 2026-10-02 |
| alpha:l-menthol-range | specific rotation of l-menthol at 25 degC, sodium D line, range given by HSDB (PubChem CID 1254, Other Experimental Properties) | -45 to -51 | deg | PUBCHEM | 2026-10-02 |
| ir:ethanol-OH | ethanol (gas, C64175), O-H stretch, centre of the P/R doublet 3658/3674 | 3666 | cm-1 | WEBBOOK-IR | 2026-10-02 |
| ir:ethanol-CH | ethanol (gas), C-H stretch, strongest maximum | 2978 | cm-1 | WEBBOOK-IR | 2026-10-02 |
| ir:ethanol-CO | ethanol (gas), C-O stretch, centre of the doublet 1054/1066 (strongest band) | 1060 | cm-1 | WEBBOOK-IR | 2026-10-02 |
| ir:propanone-CO | propanone (gas, C67641), C=O stretch (strongest band) | 1738 | cm-1 | WEBBOOK-IR | 2026-10-02 |
| ir:propanone-CCC | propanone (gas), C-C-C stretch, doublet 1218/1230 | 1224 | cm-1 | WEBBOOK-IR | 2026-10-02 |
| ir:ethanoic-CO | ethanoic acid (gas, C64197), C=O stretch, doublet 1778/1798 (strongest band) | 1788 | cm-1 | WEBBOOK-IR | 2026-10-02 |
| ir:ethanoic-OH | ethanoic acid (gas), O-H stretch | 3582 | cm-1 | WEBBOOK-IR | 2026-10-02 |
| ir:ethanoic-CO2 | ethanoic acid (gas), C-O stretch | 1178 | cm-1 | WEBBOOK-IR | 2026-10-02 |
| ir:ethylethanoate-CO | ethyl ethanoate (gas, C141786), C=O stretch, doublet 1758/1770 | 1764 | cm-1 | WEBBOOK-IR | 2026-10-02 |
| ir:ethylethanoate-COC | ethyl ethanoate (gas), C-O stretch (strongest band) | 1238 | cm-1 | WEBBOOK-IR | 2026-10-02 |
| ir:ethylbutanoate-CO | ethyl butanoate (gas, C105544), C=O stretch | 1754 | cm-1 | WEBBOOK-IR | 2026-10-02 |
| ir:ethylbutanoate-COC | ethyl butanoate (gas), C-O stretch (strongest band) | 1182 | cm-1 | WEBBOOK-IR | 2026-10-02 |
| ir:ethylbutanoate-CH | ethyl butanoate (gas), C-H stretch, strongest maximum | 2982 | cm-1 | WEBBOOK-IR | 2026-10-02 |
| nmr:ethylethanoate-OCH2 | ethyl ethanoate, 1H shift of OCH2 (quartet, lines 4.00/4.08/4.16/4.24), CDCl3, 90 MHz (PubChem CID 8857, 1H NMR Spectra, HMDB peak list) | 4.12 | ppm | PUBCHEM | 2026-10-02 |
| nmr:ethylethanoate-COCH3 | ethyl ethanoate, 1H shift of CH3CO (singlet), same spectrum | 2.04 | ppm | PUBCHEM | 2026-10-02 |
| nmr:ethylethanoate-CH3 | ethyl ethanoate, 1H shift of OCH2CH3 (triplet 1.18/1.26/1.34), same spectrum | 1.26 | ppm | PUBCHEM | 2026-10-02 |
| nmr:ethylethanoate-J | ethyl ethanoate, 3J(CH2-CH3) from the line spacing 0.08 ppm at 90 MHz | 7.2 | Hz | PUBCHEM | 2026-10-02 |
| nmr:ethanol-CH2 | ethanol, 1H shift of CH2 (quartet 3.58/3.65/3.73/3.81), CDCl3, 90 MHz (PubChem CID 702, HMDB peak list) | 3.69 | ppm | PUBCHEM | 2026-10-02 |
| nmr:ethanol-CH3 | ethanol, 1H shift of CH3 (triplet 1.15/1.23/1.30), same spectrum | 1.23 | ppm | PUBCHEM | 2026-10-02 |
| nmr:ethanol-OH | ethanol, 1H shift of OH (singlet, concentration dependent), same spectrum | 2.61 | ppm | PUBCHEM | 2026-10-02 |
| nmr:ethanol-J | ethanol, 3J(CH2-CH3) from the line spacing (0.077 ppm at 90 MHz) | 7.0 | Hz | PUBCHEM | 2026-10-02 |
| nmr:ethylbutanoate-OCH2 | ethyl butanoate, 1H shift of OCH2 (quartet 4.01/4.09/4.17/4.25), CDCl3, 90 MHz (PubChem CID 7762, HMDB peak list) | 4.13 | ppm | PUBCHEM | 2026-10-02 |
| nmr:ethylbutanoate-CH2CO | ethyl butanoate, CH2C=O (triplet 2.20/2.28/2.37), same spectrum | 2.28 | ppm | PUBCHEM | 2026-10-02 |
| nmr:ethylbutanoate-CH2 | ethyl butanoate, central CH2 of the butanoyl chain (multiplet 1.46-1.86), same spectrum | 1.66 | ppm | PUBCHEM | 2026-10-02 |
| nmr:ethylbutanoate-OCH2CH3 | ethyl butanoate, OCH2CH3 (triplet 1.17/1.25/1.33), same spectrum | 1.25 | ppm | PUBCHEM | 2026-10-02 |
| nmr:ethylbutanoate-CH3 | ethyl butanoate, CH3 of the butanoyl chain (triplet 0.86/0.95/1.03), same spectrum | 0.95 | ppm | PUBCHEM | 2026-10-02 |
| nmr:ethylbutanoate-J | ethyl butanoate, 3J of the ethyl group from the line spacing 0.08 ppm at 90 MHz | 7.2 | Hz | PUBCHEM | 2026-10-02 |
| bp:diethylether | normal boiling point of ethoxyethane (diethyl ether), PubChem CID 3283, Boiling Point (HSDB: 34.6 degC at 760 mm Hg) | 34.6 | degC | PUBCHEM | 2026-10-02 |
| bp:propanal | normal boiling point of propanal, PubChem CID 527, Boiling Point (48 degC at 760 mm Hg) | 48 | degC | PUBCHEM | 2026-10-02 |
| bp:propan-1-ol | normal boiling point of propan-1-ol, PubChem CID 1031, Boiling Point | 97.2 | degC | PUBCHEM | 2026-10-02 |
| usgs:li-world-2025 | world lithium mine production 2025, estimate, rounded (lithium content; mcs2026-lithium.pdf) | 290000 | t Li | USGS-MCS2026 | 2026-10-02 |
| usgs:li-australia-2025 | lithium mine production 2025, Australia (estimate) | 92000 | t Li | USGS-MCS2026 | 2026-10-02 |
| usgs:li-china-2025 | lithium mine production 2025, China (estimate) | 62000 | t Li | USGS-MCS2026 | 2026-10-02 |
| usgs:li-chile-2025 | lithium mine production 2025, Chile (estimate) | 56000 | t Li | USGS-MCS2026 | 2026-10-02 |
| usgs:li-zimbabwe-2025 | lithium mine production 2025, Zimbabwe (estimate) | 28000 | t Li | USGS-MCS2026 | 2026-10-02 |
| usgs:li-argentina-2025 | lithium mine production 2025, Argentina (estimate) | 23000 | t Li | USGS-MCS2026 | 2026-10-02 |
| usgs:li-brazil-2025 | lithium mine production 2025, Brazil (estimate) | 12000 | t Li | USGS-MCS2026 | 2026-10-02 |
| usgs:li-mali-2025 | lithium mine production 2025, Mali (estimate) | 9400 | t Li | USGS-MCS2026 | 2026-10-02 |
| usgs:li-canada-2025 | lithium mine production 2025, Canada (estimate) | 5600 | t Li | USGS-MCS2026 | 2026-10-02 |
| usgs:sodaash-natural-2025 | world soda ash production 2025, natural (estimate, rounded; mcs2026-soda-ash.pdf) | 19000 | kt | USGS-MCS2026 | 2026-10-02 |
| usgs:sodaash-synthetic-2025 | world soda ash production 2025, synthetic (estimate) | 52000 | kt | USGS-MCS2026 | 2026-10-02 |
| usgs:sodaash-total-2025 | world soda ash production 2025, natural and synthetic (estimate, rounded) | 71000 | kt | USGS-MCS2026 | 2026-10-02 |
| usgs:N-world-2025 | world ammonia production 2025, nitrogen content (estimate, rounded; mcs2026-nitrogen.pdf) | 160000 | kt N | USGS-MCS2026 | 2026-10-02 |
| usgs:S-world-2025 | world sulfur production 2025, all forms, sulfur content (estimate, rounded; mcs2026-sulfur.pdf) | 84000 | kt S | USGS-MCS2026 | 2026-10-02 |
| sol:Li2CO3-20 | solubility of lithium carbonate in water at 20 degC (PubChem CID 11125, Solubility, ref. 39) | 1.31 | wt% | PUBCHEM | 2026-10-02 |
| sol:Li2CO3-80 | solubility of lithium carbonate in water at 80 degC (same source) | 0.84 | wt% | PUBCHEM | 2026-10-02 |
| sol:Li2CO3-100 | solubility of lithium carbonate in water at 100 degC (same source) | 0.71 | wt% | PUBCHEM | 2026-10-02 |
| usgs:bauxite-world-2025 | world bauxite mine production 2025 (estimate, rounded; mcs2026-bauxite-alumina.pdf) | 440000 | kt dry | USGS-MCS2026 | 2026-10-02 |
| usgs:alumina-world-2025 | world alumina refinery production 2025 (estimate, rounded; same chapter) | 150000 | kt | USGS-MCS2026 | 2026-10-02 |
| usgs:phosphate-world-2025 | world marketable phosphate rock production 2025 (estimate, rounded; mcs2026-phosphate.pdf) | 250000 | kt | USGS-MCS2026 | 2026-10-02 |
| usgs:iodine-world-2025 | world iodine production 2025 (estimate, rounded, elemental iodine; mcs2026-iodine.pdf) | 34000 | t | USGS-MCS2026 | 2026-10-02 |
| usgs:fluorspar-world-2025 | world fluorspar mine production 2025 (estimate, rounded; mcs2026-fluorspar.pdf) | 10000 | kt | USGS-MCS2026 | 2026-10-02 |
| ie:Xe | first ionisation energy of Xe (Z = 54) | 12.1298437 | eV | ASD-IE | 2026-10-02 |
| ie:Rn | first ionisation energy of Rn (Z = 86) | 10.74850 | eV | ASD-IE | 2026-10-02 |
| ie:O2 | adiabatic ionisation energy of O2 (Tonkyn, Winniczek, et al., 1989) | 12.0697 | eV | WEBBOOK-IEMOL | 2026-10-02 |
| lit:XePtF6 | solid formed by xenon with PtF6, studied under the formula XePtF6 (title of the paper) | XePtF6 | - | GRAHAM-2000 | 2026-10-02 |
| ghspic:GHS01 | GHS01 pictogram: exploding bomb (explosives) | exploding bomb | - | PUBCHEM-GHSSUM | 2026-10-02 |
| ghspic:GHS02 | GHS02 pictogram: flame (flammables) | flame | - | PUBCHEM-GHSSUM | 2026-10-02 |
| ghspic:GHS03 | GHS03 pictogram: flame over circle (oxidizers) | flame over circle | - | PUBCHEM-GHSSUM | 2026-10-02 |
| ghspic:GHS04 | GHS04 pictogram: gas cylinder (compressed gases) | gas cylinder | - | PUBCHEM-GHSSUM | 2026-10-02 |
| ghspic:GHS05 | GHS05 pictogram: corrosion (corrosives) | corrosion | - | PUBCHEM-GHSSUM | 2026-10-02 |
| ghspic:GHS06 | GHS06 pictogram: skull and crossbones (acute toxicity) | skull and crossbones | - | PUBCHEM-GHSSUM | 2026-10-02 |
| ghspic:GHS07 | GHS07 pictogram: exclamation mark (irritant) | exclamation mark | - | PUBCHEM-GHSSUM | 2026-10-02 |
| ghspic:GHS08 | GHS08 pictogram: health hazard | health hazard | - | PUBCHEM-GHSSUM | 2026-10-02 |
| ghspic:GHS09 | GHS09 pictogram: environment | environment | - | PUBCHEM-GHSSUM | 2026-10-02 |
| hstat:H225 | H225 highly flammable liquid and vapour; flammable liquids cat. 2; signal word | Danger | - | PUBCHEM-GHSSUM | 2026-10-02 |
| hstat:H226 | H226 flammable liquid and vapour; flammable liquids cat. 3; signal word | Warning | - | PUBCHEM-GHSSUM | 2026-10-02 |
| hstat:H290 | H290 may be corrosive to metals; cat. 1; signal word | Warning | - | PUBCHEM-GHSSUM | 2026-10-02 |
| hstat:H302 | H302 harmful if swallowed; acute toxicity oral cat. 4; signal word | Warning | - | PUBCHEM-GHSSUM | 2026-10-02 |
| hstat:H304 | H304 may be fatal if swallowed and enters airways; aspiration hazard cat. 1; signal word | Danger | - | PUBCHEM-GHSSUM | 2026-10-02 |
| hstat:H314 | H314 causes severe skin burns and eye damage; skin corrosion cat. 1; signal word | Danger | - | PUBCHEM-GHSSUM | 2026-10-02 |
| hstat:H315 | H315 causes skin irritation; cat. 2; signal word | Warning | - | PUBCHEM-GHSSUM | 2026-10-02 |
| hstat:H318 | H318 causes serious eye damage; cat. 1; signal word | Danger | - | PUBCHEM-GHSSUM | 2026-10-02 |
| hstat:H319 | H319 causes serious eye irritation; cat. 2A; signal word | Warning | - | PUBCHEM-GHSSUM | 2026-10-02 |
| hstat:H335 | H335 may cause respiratory irritation; STOT SE cat. 3; signal word | Warning | - | PUBCHEM-GHSSUM | 2026-10-02 |
| hstat:H336 | H336 may cause drowsiness or dizziness; STOT SE cat. 3; signal word | Warning | - | PUBCHEM-GHSSUM | 2026-10-02 |
| hstat:H351 | H351 suspected of causing cancer; carcinogenicity cat. 2; signal word | Warning | - | PUBCHEM-GHSSUM | 2026-10-02 |
| hstat:H400 | H400 very toxic to aquatic life; acute cat. 1; signal word | Warning | - | PUBCHEM-GHSSUM | 2026-10-02 |
| hstat:H410 | H410 very toxic to aquatic life with long lasting effects; chronic cat. 1; signal word | Warning | - | PUBCHEM-GHSSUM | 2026-10-02 |
| pstat:P210 | P210 keep away from heat, hot surfaces, sparks, open flames and other ignition sources; no smoking | P210 | - | PUBCHEM-GHSSUM | 2026-10-02 |
| pstat:P233 | P233 keep container tightly closed | P233 | - | PUBCHEM-GHSSUM | 2026-10-02 |
| pstat:P260 | P260 do not breathe dust/fume/gas/mist/vapours/spray | P260 | - | PUBCHEM-GHSSUM | 2026-10-02 |
| pstat:P261 | P261 avoid breathing dust/fume/gas/mist/vapours/spray | P261 | - | PUBCHEM-GHSSUM | 2026-10-02 |
| pstat:P264 | P264 wash hands thoroughly after handling | P264 | - | PUBCHEM-GHSSUM | 2026-10-02 |
| pstat:P270 | P270 do not eat, drink or smoke when using this product | P270 | - | PUBCHEM-GHSSUM | 2026-10-02 |
| pstat:P273 | P273 avoid release to the environment | P273 | - | PUBCHEM-GHSSUM | 2026-10-02 |
| pstat:P280 | P280 wear protective gloves/protective clothing/eye protection/face protection | P280 | - | PUBCHEM-GHSSUM | 2026-10-02 |
| pstat:P301+P330+P331 | P301+P330+P331 if swallowed: rinse mouth; do not induce vomiting | P301+P330+P331 | - | PUBCHEM-GHSSUM | 2026-10-02 |
| pstat:P305+P351+P338 | P305+P351+P338 if in eyes: rinse cautiously with water for several minutes; remove contact lenses if present and easy to do; continue rinsing | P305+P351+P338 | - | PUBCHEM-GHSSUM | 2026-10-02 |
| pstat:P403+P235 | P403+P235 store in a well-ventilated place; keep cool | P403+P235 | - | PUBCHEM-GHSSUM | 2026-10-02 |
| pstat:P501 | P501 dispose of contents/container to ... (an approved disposal route) | P501 | - | PUBCHEM-GHSSUM | 2026-10-02 |
| mp:acetanilide | melting point of acetanilide (HSDB; CID 904) | 114.3 | °C | PUBCHEM | 2026-10-02 |
| mp:benzoic | melting point of benzoic acid (HSDB; CID 243) | 122.35 | °C | PUBCHEM | 2026-10-02 |
| nD:water | refractive index of water, sodium D line (HSDB; CID 962; no temperature given) | 1.333 | - | PUBCHEM | 2026-10-02 |
| nD:ethanol | refractive index of ethanol at 20 °C, sodium D line (HSDB; CID 702) | 1.3611 | - | PUBCHEM | 2026-10-02 |
| nD:cyclohexane | refractive index of cyclohexane at 20 °C, sodium D line (HSDB; CID 8078) | 1.42662 | - | PUBCHEM | 2026-10-02 |
