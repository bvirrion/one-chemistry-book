# Book 2 (University Chemistry, Year 1) — chapter briefs

Phase A plan, 2026-10-02. Year `parts/bachelor-1`, label prefix `b1`, entry
`one_chemistry_book_2_university_year_1.tex`. 29 chapters in outline order.
Binding rules: `sources/BATCH_BOOKS_1-4.md`. Term list: `DEFINITIONS.md`.
State and traps: `PROGRESS.md`.

## Conventions for every chapter

- University register: laws are `theorem`/`proposition` with a Year-1
  derivation (derivatives, first-order linear ODEs, exp/ln, small linear
  systems); otherwise `\admitted` plus a prose pointer ("derived in the
  Year 2 volume"). Every standard technique is a `method`.
- **Recall boxes** in Book 2 cite Book 1 in prose only ("the school volume
  showed …"), never `\cref`; a recall of an earlier Book 2 chapter uses
  `\cref{ch:b1:…}`.
- A notion owned by Year 2 or Year 3 is used as a plain word with a prose
  pointer ("studied in the Year 2 volume"), never `\emph{}\index{}`, and
  **never `\index{}` at all** (the harvester also collects multi-word
  `\index` entries outside definitions — see PROGRESS traps).
- Calibration: 12 exercises (4★, 5★★, 3★★★), one weekend problem of 22–28
  questions in Parts I–IV ending on a named number; ~11.5 pp per chapter;
  ~4 schematics per chapter, illustrations and photographs on top.
- Tags: **S** schematic (TikZ/chemfig/tikz-3dplot), **F** figdata curve
  (`figdata/bachelor-1/<name>.py` + `tests/bachelor-1/test_<name>.py`),
  **AI** illustration (everyday/industrial/lab scene only), **P**
  photograph (Commons, licence verified through the API).
- Ledger ids are prefixed by kind (`ie:`, `pka:`, `eo:`, `ks:`, `logb:`,
  `bp:`, `lat:`, `rad:`, `ir:`, `nmr:`, `uv:`, `ghs:`, `usgs:`, `dfg:`,
  `dip:`, `geo:`…); grep all ledgers before minting.
- Sources planned (keys for the Sources table of `sources/ledger/book2.md`):
  NIST-ASD (atomic spectra + ionisation energies), PUBCHEM (compound pages:
  GHS, optical rotation, mp; periodic-table JSON for EN/EA/radii),
  NIST-WEBBOOK (boiling points, IR JCAMP), CCCBDB (experimental geometries,
  dipoles, rotation barriers), NBS-82 (Wagman et al., NBS tables of
  chemical thermodynamic properties, JPCRD 11 suppl. 2: ΔfG° for E°, Ks,
  E–pH boundaries — computed, never typed), NBS-C514 (Maryott & Smith,
  dielectric constants of pure liquids), NSRDS-NBS10 (gas-phase dipole
  moments), IUPAC-PKA (IUPAC digitised dissociation-constants dataset, CC BY
  4.0), IUPAC-EDTA (Anderegg 2005 critical evaluation, Pure Appl. Chem.),
  IAPWS-KW (ionisation constant of water), SHANNON (database of ionic radii),
  AMCSD (American Mineralogist crystal structure database: lattice
  parameters), NIST-KIN (NIST chemical kinetics database), SDBS/HMDB/NMRSHIFTDB
  (¹H shifts and J), IUPAC-NIST-SDS (solubility data series), USGS-MCS
  (mineral commodity summaries), COMMONS (photographs).

---

## Ch. 1 — Quantum Numbers and Electron Configurations — `quantum-numbers`

- **Hook.** The light of a hydrogen lamp, through a prism, is not a rainbow
  but four sharp lines (red, cyan, blue, violet). Why only these?
- **Recall (prose).** The school volume placed electrons in shells 1s, 2s,
  2p, 3s, 3p and counted valence electrons; photon energy $E = h\nu =
  hc/\lambda$ is physics, used as known.
- **Sections.** 1 Quantised energies: the hydrogen spectrum. 2 Four quantum
  numbers. 3 Building configurations (Pauli, Klechkowski, Hund). 4
  Configurations of ions and the exceptions.
- **Definitions.** `def:b1:quantum-numbers:energy-level` (energy level,
  ground state, excited state); `:quantum-number` (principal, azimuthal,
  magnetic, spin quantum numbers); `:shell` (electron shell, subshell);
  `:orbital` (atomic orbital as the label $(n,l,m_l)$ — **contested**,
  see report; fallback: "quantum box" with orbital as prose pointing to
  the Year 2 volume); `:configuration` (electron configuration, valence
  electrons, core electrons); `:unpaired` (unpaired electron).
  Harvested statements: `prop:…:pauli` (Pauli exclusion principle),
  `prop:…:klechkowski` (Klechkowski rule), `prop:…:hund` (Hund's rule).
- **Ownership.** Re-founds g10 `electron-shells` (shell, configuration,
  valence electron). Takes nothing from Y2/Y3: wavefunctions, radial and
  angular parts, orbital shapes, effective nuclear charge stay in the Year
  2 volume (prose pointer); term symbols in Year 3.
- **Statements.** `thm:…:levels` hydrogen levels $E_n = -E_R/n^2$
  (`\admitted`, derived in the Year 2 volume); `prop:…:rydberg` line
  wavenumbers $1/\lambda = R_H(1/n_1^2 - 1/n_2^2)$ (proof from the levels
  and $E = hc/\lambda$); `prop:…:capacity` a subshell holds $2(2l+1)$, a
  shell $2n^2$ electrons (proof by summation); `prop:…:ions` transition
  ions lose $ns$ before $(n-1)d$ (admitted, observed); exceptions Cr, Cu
  (stated as observed, ledger).
- **Methods.** `met:…:configuration` (writing a ground-state
  configuration and its box diagram); `met:…:noble-core` (abbreviated
  configuration).
- **Figures.** S energy-level diagram of H with Lyman/Balmer/Paschen arrows
  (from F); F `hydrogen-levels` (levels and computed Balmer lines on a
  wavelength strip); S Klechkowski diagonal diagram; S box diagrams C, N,
  O, Fe, Cr, Cu; S periodic-table skeleton coloured by the subshell being
  filled (bridge to ch. 2); P hydrogen visible spectrum (`File:Hydrogen
  spectrum visible.png`, CC0); P Niels Bohr (`File:Niels Bohr.jpg`, PD) in
  a `history` box (1913 model); AI one: a night street of neon/sodium
  lamps (hook).
- **Ledger.** `asd:Halpha`…`asd:Hdelta` (Balmer wavelengths, NIST ASD);
  `ie:H` (13.598 eV, NIST ASD); ground configurations Cr, Cu, Fe²⁺,
  Fe³⁺ (NIST ASD ground levels); constants from the shared ledger
  (`const:Rinf`, `const:me`, `const:mp`, `const:h`, `const:c`,
  `const:RyhcEV`).
- **Exercises palette.** Count states of a shell; quantum numbers of the
  last electron; configurations of K, Ca, Ti, Br, Se²⁻, Mn²⁺; Lyman limit;
  identify an element from its configuration; why Z = 19 starts 4s.
- **Weekend problem — "Lines of a lamp, and a world with three spins".**
  I the hydrogen lamp (levels, Balmer lines, which line is red, series
  limit, ionisation energy from the limit); II counting states (2n², the
  lengths 2, 8, 8, 18, 18, 32 of the periods from Klechkowski); III
  transition metals and their ions (Fe, Fe²⁺, Fe³⁺, Cr, Cu; unpaired
  electrons); IV a counterfactual world where $m_s$ takes three values:
  subshell capacities, period lengths, which Z are the first noble gases.
  **Named number: Z = 15, the second noble gas of the three-spin world**
  (3 + 3 + 9). 25 questions.

## Ch. 2 — Periodicity — `periodicity`

- **Hook.** Lithium, sodium and potassium are the same kind of metal, yet
  lithium won the battery: lightest, and the most reducing couple. What
  makes elements of one column alike and of one row different?
- **Recall.** \cref{ch:b1:quantum-numbers} (configurations); prose: the
  school volume's rows/columns and the first look at electronegativity.
- **Sections.** 1 The table built from configurations (periods, groups,
  blocks). 2 Size: atomic and ionic radii. 3 Energies: ionisation energy
  and electron affinity. 4 Electronegativity (Pauling, Mulliken) and
  polarisability. 5 Trends in chemical character (metals, metalloids,
  non-metals; reducing and oxidising power).
- **Definitions.** `def:b1:periodicity:table` (period, group, block);
  `:screening` (screening, effective nuclear charge — **contested** with
  Y2 `atomic-orbitals`; fallback prose); `:radius` (covalent radius,
  ionic radius); `:ionisation-energy` (first ionisation energy, successive
  ionisation energies); `:electron-affinity` (electron affinity, IUPAC
  sign: energy released on attachment); `:electronegativity`
  (electronegativity, Pauling scale, Mulliken scale); `:polarisability`;
  `:metalloid` (metal, non-metal, metalloid).
- **Ownership.** Re-founds g11 `polarity-and-cohesion` (electronegativity)
  and g9 `periodic-table-first-look` (period, group). Nothing Y2/Y3
  taken; Slater rules not used.
- **Statements.** `prop:…:radius-trend` (proof sketch from $n$ and
  screening); `prop:…:ie-anomalies` dips at groups 13 and 16 (proof from
  subshell energies and pairing); `def` of Pauling $|\chi_A-\chi_B| =
  \sqrt{\Delta E/\mathrm{eV}}$ with the arithmetic-mean $\Delta E$; Mulliken
  $\chi_M = (E_i + E_{ea})/2$; `prop:…:polarisability-trend`.
- **Methods.** `met:…:predict-trend` (reading a trend from Z, n and
  screening).
- **Figures.** S long-form periodic table coloured by block; F
  `ionisation-energies` (IE₁ vs Z, Z = 1–36, part b: successive IE of Mg
  on a log axis); S Pauling-electronegativity heat table (main groups,
  ledger values printed); S radius trends (circles to scale for
  groups 1 and 17 and period 3); P Linus Pauling (`File:Linus Pauling
  1962.jpg`, PD) in a `history` box (1932 scale).
- **Ledger.** `ie:` Z = 1–36 (NIST ASD); `ie:Mg1`…`ie:Mg4`; `ea:` H, Li,
  C, O, F, Na, Cl, Br, I (PubChem PT, or Andersen 1999 JPCRD); `en:`
  Pauling values main groups periods 1–5 (PubChem PT); `rcov:`,
  `rion:` (PubChem PT; Shannon for ions); for the problem `janaf:` ΔfH° of
  H(g), Cl(g), HCl(g) → bond energies computed.
- **Weekend problem — "Pauling's arithmetic".** I successive ionisation
  energies of an unknown element (identify group 2 from the jump); II
  radii of isoelectronic ions O²⁻, F⁻, Na⁺, Mg²⁺; III bond energies of
  H₂, Cl₂, HCl from formation enthalpies given as data rows → Pauling's
  ΔE; IV Mulliken electronegativities of H and Cl compared.
  **Named number: Δχ(H–Cl) ≈ 0.98 on Pauling's scale** (computed in
  Phase B from the ledger). 24 questions.

## Ch. 3 — Lewis Structures, Resonance and VSEPR — `lewis-resonance-vsepr`

- **Hook.** Ozone: two O–O bonds measured identical, though any Lewis
  drawing shows one double and one single bond.
- **Recall.** prose: the school volume's covalent bond, lone pairs, octet,
  four shapes; \cref{ch:b1:periodicity} electronegativity.
- **Sections.** 1 Lewis structures and formal charges. 2 Beyond the octet
  (electron-deficient, hypervalent, odd-electron species; Lewis acids and
  bases). 3 Resonance. 4 VSEPR. 5 Polar molecules: dipole moments.
- **Definitions.** `def:b1:lewis-resonance-vsepr:lewis` (covalent bond,
  bonding pair, lone pair, Lewis structure, octet rule, duet rule);
  `:formal-charge`; `:hypervalent` (hypervalent molecule,
  electron-deficient molecule); `:lewis-acid` (Lewis acid, Lewis base,
  dative bond — **contested**); `:resonance` (resonance structure,
  resonance hybrid); `:sigma-pi` (σ bond, π bond, descriptive —
  **contested**); `:vsepr` (VSEPR model, steric number, AXₙEₘ
  notation); `:hybridisation` (sp³/sp²/sp, descriptive — **contested**);
  `:dipole` (bond dipole, dipole moment, polar molecule).
- **Ownership.** Re-founds g10 `lewis-and-shape` (covalent bond, lone
  pair, Lewis structure, octet), g11 `polarity-and-cohesion` (polar
  molecule). MOs, bond order (Y2), point groups (Y3) not taken.
- **Statements.** `prop:…:formal-sum` sum of formal charges = charge
  (proof by counting); `prop:…:resonance-rules` (admissible structures,
  weights) as a method; `prop:…:vsepr-geometries` (table, model
  admitted); `prop:…:lone-pair-angles` (E > X repulsion, angles below
  109.5°); `prop:…:dipole-sum` vector sum (proof), zero for symmetric
  shapes.
- **Methods.** `met:…:lewis` (count, skeleton, octets, formal charges);
  `met:…:resonance`; `met:…:vsepr`.
- **Figures.** S VSEPR gallery AX₂…AX₆ with AX₃E, AX₂E₂, AX₄E, AX₃E₂,
  AX₂E₃, AX₅E, AX₄E₂ (chemfig wedges + angles); S resonance sets (O₃,
  NO₃⁻, CO₃²⁻, benzene, ethanoate) with `\chemmove`; S dipole vector
  sums H₂O, CO₂, CHCl₃, CCl₄; S σ and π overlap sketch; P G. N. Lewis
  (Commons file to find; candidates not yet confirmed) in `history` (1916
  cubical atom).
- **Ledger.** `geo:` bond lengths/angles H₂O, NH₃, CH₄, O₃, SO₂, CO₂,
  BF₃, ethane/ethene/ethyne C–C, benzene (CCCBDB experimental); `dip:`
  H₂O, NH₃, HCl, CHCl₃, CH₂Cl₂, CO₂ (0) (NSRDS-NBS10 / CCCBDB).
- **Weekend problem — "The molecules of a lightning strike".** I Lewis
  and formal charges of N₂, NO, NO₂, N₂O, O₃, HNO₃; II resonance and
  measured bond lengths (O₃, NO₃⁻, HNO₃); III VSEPR shapes and polarity;
  IV the dipole of water: bond moment of O–H from μ(H₂O) and the angle,
  then the partial charge on H from the O–H length.
  **Named number: fractional ionic character of the O–H bond ≈ 0.33**
  (computed). 25 questions.

## Ch. 4 — Intermolecular Forces and Solvents — `intermolecular-forces-solvents`

- **Hook.** A gecko walks on a window pane; water, a molecule lighter than
  CO₂, boils 180 °C above it.
- **Recall.** \cref{ch:b1:lewis-resonance-vsepr} (dipole moments),
  \cref{ch:b1:periodicity} (polarisability); prose: Book 1 hydrogen bond,
  dissolving ionic solids, soaps.
- **Sections.** 1 Van der Waals interactions (Keesom, Debye, London). 2
  The hydrogen bond. 3 Consequences: boiling points, viscosity, structure
  of water. 4 Solvents (permittivity, polarity, proticity) and
  dissolution in steps. 5 Solubility, miscibility and amphiphiles.
- **Definitions.** `def:b1:intermolecular-forces-solvents:vdw` (van der
  Waals interaction, Keesom, Debye, London interaction); `:hbond`
  (hydrogen bond, donor, acceptor); `:permittivity` (relative
  permittivity); `:solvent-classes` (polar, protic, aprotic solvent);
  `:dissolution` (solvation, ionising power, dissociating power);
  `:miscibility` (miscible liquids); `:amphiphile` (hydrophilic,
  hydrophobic, amphiphilic). *Micelle* used, not defined
  (**contested**, owner Y3 `colloids` unless ruled otherwise).
- **Ownership.** Re-founds g11 `polarity-and-cohesion` (van der Waals,
  hydrogen bond), g11 `dissolution` (solvation, amphiphile), g6
  `solutions-and-solubility` (miscible). Surface tension, surfactants,
  colloids (Y3) not taken.
- **Statements.** `prop:…:distance-law` vdW energies vary as $r^{-6}$
  (admitted, physics); `prop:…:coulomb-in-solvent` force divided by
  $\varepsilon_r$ (physics, used); `prop:…:like-dissolves-like` (reasoned
  from the three steps).
- **Methods.** `met:…:choose-solvent` (permittivity + proticity + H-bonding
  table).
- **Figures.** F `hydride-boiling-points` (groups 14–17 vs period; part
  b: linear alkanes C1–C10); S the three vdW interactions sketched with
  δ charges; S H-bond networks (water, ethanoic-acid dimer) chemfig dotted;
  S solvation shells of Na⁺ and Cl⁻ (atom styles, oriented water); S
  amphiphile at an interface and in a micelle (drawn, word not defined); AI
  gecko on glass; AI oil-and-vinegar dressing separating.
- **Ledger.** `bp:` 16 hydrides + C1–C10 alkanes (NIST WebBook);
  `epsr:` water, methanol, ethanol, propanone, DMSO, acetonitrile,
  dichloromethane, ethoxyethane, hexane, toluene (NBS-C514); `dip:`
  of the same solvents (NSRDS-NBS10).
- **Weekend problem — "If water had no hydrogen bonds".** I London: boiling
  points of alkanes and of the noble gases' heavy analogues; II the
  hydrides H₂Te, H₂Se, H₂S: linear trend vs period; III extrapolation to
  H₂O and the hydrogen-bond excess; IV choosing solvents for three
  operations (dissolve NaCl, run an SN2 with an anion, extract iodine from
  water). **Named number: the boiling point water would have without
  hydrogen bonds, ≈ −70 °C** (extrapolated in Phase B). 24 questions.

## Ch. 5 — Crystals I: The Perfect Crystal and Metals — `crystals-metals`

- **Hook.** A copper wire, a steel spring, an aluminium can: why are
  metals ductile, why does a little carbon make iron hard?
- **Recall.** prose: metallic elements (Book 1); \cref{ch:b1:periodicity}
  (radii).
- **Sections.** 1 The perfect-crystal model (lattice, motif, cell). 2
  Close packings: FCC and HCP. 3 Body-centred cubic. 4 Interstitial sites.
  5 Metallic bonding and alloys.
- **Definitions.** `def:b1:crystals-metals:crystal` (crystal, amorphous
  solid, perfect crystal model); `:lattice` (lattice, node, motif, unit
  cell, lattice parameters); `:multiplicity` (multiplicity of a cell);
  `:coordination` (coordination number — **contested** with Y2
  `coordination-complexes`); `:compactness`; `:packings` (close packing,
  face-centred cubic, hexagonal close-packed, body-centred cubic);
  `:site` (interstitial site, tetrahedral site, octahedral site,
  habitability); `:metallic-bond`; `:alloy` (substitutional alloy,
  interstitial alloy); `:allotropy` (allotrope).
- **Ownership.** Owner of lattice/cell/sites per the map. Space groups,
  reciprocal lattice, Bragg (Y3) not taken; band theory (Y3) mentioned in
  prose only.
- **Statements.** `prop:…:fcc` Z = 4, CN 12, $a = 2\sqrt2 R$,
  $C = \pi/(3\sqrt2) \approx 0.74$ (proof); `prop:…:hcp` same C,
  $c/a = \sqrt{8/3}$ (proof); `prop:…:bcc` Z = 2, CN 8, $a\sqrt3 = 4R$,
  $C = \pi\sqrt3/8 \approx 0.68$ (proof); `prop:…:sites` 4 octahedral and
  8 tetrahedral sites per FCC cell, $r_O = (\sqrt2-1)R$, $r_T =
  (\sqrt{3/2}-1)R$ (proof); `prop:…:density` $\rho = ZM/(N_A a^3)$ (proof);
  Kepler's bound 0.74 (`\admitted`, history box).
- **Methods.** `met:…:cell-count` (counting corner/edge/face shares);
  `met:…:density`.
- **Figures.** S (tikz-3dplot) FCC cell; S BCC cell; S HCP prism; S
  close-packed layers A, B, C (2D) and the ABC/AB stacking; S octahedral
  and tetrahedral sites in FCC; P native copper (`File:Native copper
  mineral specimen.jpg`, CC0); AI blacksmith forging steel.
- **Ledger.** `lat:` Cu, Al, Ag, α-Fe, γ-Fe, Na, W, Mg (a, c), Zn (a, c)
  (AMCSD); `rad:C` (covalent radius of carbon, PubChem PT); `rho:Cu`
  (measured density to compare, PubChem).
- **Weekend problem — "Why steel holds carbon".** I α-iron (BCC): atomic
  radius from a, density; II γ-iron (FCC): radius, density, the volume
  change at the transition; III octahedral sites of γ-Fe vs the
  distorted sites of α-Fe, carbon's size; IV maximum carbon content if
  every k-th octahedral site is filled, mass fraction. **Named number:
  radius of the octahedral site of γ-iron ≈ 53 pm** ((√2−1)R, R from
  ledger a). 24 questions.

## Ch. 6 — Crystals II: Ionic, Covalent and Molecular Solids — `crystals-ionic-covalent`

- **Hook.** Table salt cleaves into cubes; diamond and graphite are the
  same element and opposite materials.
- **Recall.** \cref{ch:b1:crystals-metals} (cells, sites, compactness),
  \cref{ch:b1:periodicity} (ionic radius), \cref{ch:b1:intermolecular-forces-solvents}.
- **Sections.** 1 Ionic crystals and radius ratios. 2 Four structure types
  (CsCl, NaCl, zinc blende, fluorite/antifluorite). 3 Covalent crystals
  (diamond, silicon, graphite). 4 Molecular crystals (ice, iodine, dry
  ice). 5 Comparing solids (cohesion, melting, conduction — trends only).
- **Definitions.** `def:b1:crystals-ionic-covalent:ionic-crystal`;
  `:radius-ratio`; `:structure-type` (caesium chloride type, rock-salt
  type, zinc-blende type, fluorite type, antifluorite type);
  `:covalent-crystal`; `:molecular-crystal`.
- **Ownership.** Map owner (ionic/covalent/molecular types, radius
  ratio). Lattice energy by Born–Haber (Y2 Hess) not taken; band picture
  (Y3) prose only.
- **Statements.** For each type: coordination, contact condition, stability
  range of $r_+/r_-$ — `prop:…:cscl` ($\ge \sqrt3-1 = 0.732$),
  `prop:…:nacl` ($\sqrt2-1 = 0.414$ to 0.732), `prop:…:zns` ($\sqrt{3/2}-1
  = 0.225$ to 0.414), `prop:…:caf2` (8:4) — all proved from the geometry;
  `prop:…:diamond` C = $\pi\sqrt3/16 \approx 0.34$ (proof);
  `prop:…:ice` open H-bonded network (structure stated, ledger).
- **Methods.** `met:…:predict-structure` (radius ratio → type, with the
  caveat that it fails for polarisable ions).
- **Figures.** S NaCl cell; S CsCl cell; S ZnS cell; S CaF₂ cell; S
  diamond cell and graphite layers; S radius-ratio number line with the
  domains; P halite (`File:Halite-Egypt.jpg`, PD); P fluorite (`File:Fluorite
  crystal with inclusions.jpg`, CC BY 2.0); P diamond and graphite
  (`File:Octahedral diamond (18024044222).jpg` CC BY 2.0, `File:Graphite from
  Velke Tresne, Czech Republic.jpg` CC BY-SA 4.0); P W. A. Bentley
  snowflake (PD, file to find) for ice.
- **Ledger.** `lat:` NaCl, CsCl, ZnS, CaF₂, diamond, Si, graphite (a, c),
  ice Ih (AMCSD); `rion:` Shannon radii Na⁺(VI), Cl⁻(VI), Cs⁺(VIII),
  Zn²⁺(IV), S²⁻(IV), Ca²⁺(VIII), F⁻(IV), Li⁺(IV), O²⁻(VIII) (SHANNON);
  `rho:` fluorite, diamond, graphite (PubChem/AMCSD).
- **Weekend problem — "Fluorite, the mineral and the lens".** I CaF₂ cell
  (Z, coordination 8:4, contact); II radius ratio and ionic radii; III
  density from the cell vs measured; compactness; IV antifluorite Li₂O and
  diamond vs silicon by analogy. **Named number: density of fluorite from
  its cell ≈ 3.18 g/cm³** (computed, compared with the ledger). 25 q.

## Ch. 7 — Describing a Chemical System: Extent, Activities, Q and K — `extent-q-and-k`

- **Hook.** A hydrogen plant feeds steam and natural gas to a reactor; what
  leaves is never pure hydrogen. Predicting the outlet is predicting a
  final state.
- **Recall.** prose: the school volume's progress table, limiting
  reactant, Q and K; partial pressure / perfect-gas law are physics.
- **Sections.** 1 Describing a system (phases, intensive/extensive
  variables, composition). 2 Extent of reaction and the progress table.
  3 Activities. 4 Q, K° and the direction of change. 5 Final states:
  equilibrium, quantitative reaction, disappearance of a phase; two
  reactions at once.
- **Definitions.** `def:b1:extent-q-and-k:system` (physico-chemical
  system, closed system, phase); `:variables` (intensive variable,
  extensive variable); `:composition` (mole fraction, mass fraction,
  molar concentration, partial pressure); `:activity` (activity —
  *standard state* **contested**, see report); `:extent`
  (stoichiometric number, extent of reaction); `:max-extent` (maximum
  extent, limiting reactant); `:quotient` (reaction quotient);
  `:equilibrium-constant` (standard equilibrium constant);
  `:fractional-extent` (final fractional extent, yield);
  `:quantitative` (quantitative reaction, equilibrium state).
- **Ownership.** Re-founds g10 `reaction-progress-table` (extent, limiting
  reactant), g12 `equilibrium` (Q, K), g10 `synthesis-yield` (yield —
  not in the map, see report). Not taken: chemical potential, ΔrG,
  evolution criterion, van 't Hoff (Y2): the Q/K direction rule is
  `\admitted` with "derived in the Year 2 volume".
- **Statements.** `thm:…:mass-action` law of mass action (`\admitted`,
  Year 2); `prop:…:dalton` $p_i = x_i p$ (proof from the perfect gas);
  `prop:…:direction` Q < K → forward (admitted); `prop:…:combine-k`
  reverse 1/K, sum product, multiple power (proof); `prop:…:q-monotone`
  Q increases with ξ (proof by derivative) ⇒ one equilibrium extent.
- **Methods.** `met:…:progress-table`; `met:…:final-state` (solve
  $Q(\xi)=K$ in $(\xi_{\min},\xi_{\max})$); `met:…:quantitative` (assume
  total, check); `met:…:two-reactions`.
- **Figures.** F `extent-equilibrium` (Q(ξ) on a log axis rising through K;
  part b: a solid disappearing — no equilibrium); S the Q–K number line;
  S system boundary sketch (gas phase + solution + solid); AI hydrogen
  plant (industrial scene); P Guldberg and Waage (PD, file to find) in
  `history` (1864).
- **Ledger.** Light: exercise K values are data of the exercise. If a real
  K is quoted (N₂O₄/NO₂ at 298 K), computed from NBS-82 ΔfG°.
- **Weekend problem — "The outlet of a hydrogen plant".** I composition
  variables of the feed; II steam reforming as a quantitative reaction
  (progress table); III the water–gas shift equilibrium with a given K°:
  final state by solving a quadratic; IV both reactions together, partial
  pressures. **Named number: mole fraction of H₂ leaving the shift
  reactor** (from the given data). 24 questions.

## Ch. 8 — Chemical Kinetics: Rate Laws — `rate-laws`

- **Hook.** Milk keeps a week in the fridge and a day on the table; a drug
  bottle says "store below 25 °C".
- **Recall.** prose: the school volume's rate, kinetic factors, first-order
  half-life; \cref{ch:b1:extent-q-and-k} (extent).
- **Sections.** 1 Rate of a reaction in a closed reactor. 2 Rate laws and
  orders. 3 Integrated rate laws and half-lives (orders 0, 1, 2). 4
  Finding an order (integral method, half-lives, initial rates,
  isolation). 5 Temperature: the Arrhenius law.
- **Definitions.** `def:b1:rate-laws:rate` (rate of reaction, rate of
  formation, rate of disappearance); `:order` (rate law, partial order,
  overall order, rate constant); `:half-life`; `:apparent-order`
  (isolation method, apparent order, apparent rate constant);
  `:initial-rate`; `:activation-energy` (activation energy,
  pre-exponential factor); harvested `thm:…:arrhenius` (Arrhenius law).
- **Ownership.** Re-founds g12 `reaction-rates` (rate, half-life). TST,
  Eyring, collision theory (Y3) prose only.
- **Statements.** `prop:…:rate-relations` $v = \frac{1}{\nu_i V}\frac{dn_i}{dt}$;
  `thm:…:integrated` orders 0, 1, 2 (solving the ODEs) and their
  half-lives (proof); `prop:…:half-life-test` (t½ independent of $a_0$ iff
  order 1); `thm:…:arrhenius` (empirical law, stated; $E_a$ defined by
  $d\ln k/dT = E_a/RT^2$).
- **Methods.** `met:…:integral-method`; `met:…:half-life-method`;
  `met:…:initial-rates`; `met:…:isolation`; `met:…:arrhenius-plot`.
  `inthelab`: following a reaction (absorbance, conductivity, pressure,
  quenching).
- **Figures.** F `integrated-rate-laws` (three panels: [A], ln[A], 1/[A]);
  F `arrhenius` (ln k vs 1/T for a sourced gas-phase reaction); S
  initial-rate tangent construction; AI fridge vs table (food); P Svante
  Arrhenius (`File:Arrhenius2.jpg`, PD) in `history` (1889).
- **Ledger.** `kin:` Arrhenius parameters of one or two real reactions
  (N₂O₅ decomposition; H₂O₂ first-order data if used) (NIST-KIN).
- **Weekend problem — "The shelf life of a medicine".** I first-order
  degradation from assay data at 60 °C (integral method); II half-life and
  t₉₀; III rate constants at 40, 50, 60 °C → Arrhenius plot, E_a; IV
  extrapolation to 25 °C and to a tropical 30 °C storage. **Named number:
  shelf life t₉₀ at 25 °C, in months** (invented data of the problem).
  25 questions.

## Ch. 9 — Reaction Mechanisms: Elementary Steps and Approximations — `elementary-steps`

- **Hook.** $2\ce{NO} + \ce{O2} \to 2\ce{NO2}$ goes *slower* when heated —
  impossible for a single collision, natural for a mechanism.
- **Recall.** \cref{ch:b1:rate-laws}; prose: Book 1 curly arrows,
  intermediates, catalysts.
- **Sections.** 1 Elementary steps and molecularity. 2 Energy profiles. 3
  Rate-determining step and pre-equilibrium. 4 The steady-state
  approximation. 5 Catalysis; kinetic versus thermodynamic control.
- **Definitions.** `def:b1:elementary-steps:elementary-step` (elementary
  step, molecularity, reaction mechanism, reaction intermediate);
  `:energy-profile` (reaction coordinate, energy profile, transition
  state — **contested** with Y3 `rate-theories`); `:rds`
  (rate-determining step); `:qssa` (steady-state approximation);
  `:pre-equilibrium` (pre-equilibrium approximation); `:catalyst`
  (catalyst, homogeneous catalysis, heterogeneous catalysis —
  **contested** with Y3 `surfaces-catalysis`); `:control` (kinetic
  control, thermodynamic control — **contested**); harvested
  `prop:…:hammond` (Hammond postulate — **contested**).
- **Ownership.** Re-founds g12 `curly-arrows` (elementary step,
  intermediate) and g12 `catalysis` (catalyst). Not taken: activated
  complex/TST (Y3), chain reaction (Y3), Michaelis–Menten (Y3),
  organometallic cycles (Y2).
- **Statements.** `prop:…:elementary-law` (van 't Hoff's rule is **not**
  named so — the name belongs to Y2 thermodynamics; called "rate law of an
  elementary step"); `thm:…:consecutive` A → B → C solved exactly, $t_{\max}
  = \ln(k_2/k_1)/(k_2-k_1)$ (proof, first-order linear ODE);
  `prop:…:qssa-justified` (from the exact solution when $k_2 \gg k_1$);
  `prop:…:pre-equilibrium` (proof); `prop:…:catalysis` (a catalyst
  lowers the barrier, leaves K unchanged; proof via the ratio
  $k_+/k_- = K$ for an elementary step).
- **Methods.** `met:…:rate-law-from-mechanism`.
- **Figures.** F `energy-profiles` (one step; two steps with intermediate;
  catalysed vs uncatalysed — parts a–c); F `consecutive-reactions`
  (A, B, C vs t for k₂/k₁ = 0.5 and 20, with the QSSA curve); S generic
  catalytic cycle (closed loop); AI catalytic converter in a car underbody
  (industrial/everyday) or P a converter cutaway (to find).
- **Ledger.** Light (story data invented); none required.
- **Weekend problem — "Why nitrogen monoxide oxidises faster in the
  cold".** I the observed third-order law; II a pre-equilibrium mechanism
  via N₂O₂; III the rate law from the mechanism; IV apparent activation
  energy from the step parameters (given). **Named number: the apparent
  activation energy, negative, in kJ/mol** (computed from given data).
  24 questions.

## Ch. 10 — Acid–Base Equilibria and the Predominant-Reaction Method — `predominant-reaction`

- **Hook.** Descaling a kettle with vinegar works; with lemon juice
  faster: two weak acids, two pKa.
- **Recall.** \cref{ch:b1:extent-q-and-k} (K°, activity); prose: Book 1
  Brønsted, Ka, pKa, pH, buffers.
- **Sections.** 1 Brønsted couples, autoprotolysis, pH. 2 Ka, pKa and
  strength scales; levelling by water. 3 Predominance and distribution
  diagrams. 4 The predominant-reaction method: pH of a solution. 5
  Polyprotic acids, ampholytes and buffers.
- **Definitions.** `def:b1:predominant-reaction:bronsted` (Brønsted acid,
  Brønsted base, acid–base couple); `:ampholyte`; `:autoprotolysis`
  (autoprotolysis, ionic product of water, pH); `:acidity-constant`
  (acidity constant, pKa); `:strong-acid` (strong acid, weak acid,
  strong base, weak base); `:levelling` (levelling effect);
  `:predominance` (predominance diagram, distribution diagram);
  `:polyprotic` (polyprotic acid); `:predominant-reaction`
  (predominant reaction, equivalent solution); `:buffer` (buffer
  solution); `:dissociation` (degree of dissociation).
- **Ownership.** Map owner. Re-founds g12 `ka-and-pka` (Brønsted, Ka,
  pKa, Ke, pH) and g12 `buffers-predominance` (predominance diagram,
  buffer). Nothing Y2/Y3.
- **Statements.** `prop:…:k-of-reaction` $K = 10^{\mathrm{p}K_{a2} -
  \mathrm{p}K_{a1}}$ (proof); `prop:…:henderson` (proof);
  `prop:…:ph-formulas` strong acid, weak acid, weak base, ampholyte
  $\tfrac12(\mathrm pK_{a1}+\mathrm pK_{a2})$ with validity conditions
  (proofs); `prop:…:buffer` (small pH change, proof by differentiation).
- **Methods.** `met:…:predominant-reaction` (the full algorithm with the
  pKa scale, then the check); `met:…:check-approximation`.
- **Figures.** S pKa ladder (acids left, bases right, reactions as
  descending diagonals); F `distribution-diagrams` (ethanoic; phosphoric;
  citric); F `weak-acid-ph` (exact pH vs pC with the approximation
  lines); S predominance axis of H₃PO₄; AI kettle descaling / lemon and
  vinegar on a counter.
- **Ledger.** `pka:` ethanoic, methanoic, benzoic, ammonium,
  phosphoric 1–3, carbonic 1–2, citric 1–3, hypochlorous, hydrofluoric,
  phenol, methylammonium (IUPAC-PKA); `pke:` 14.00 at 25 °C (IAPWS-KW).
- **Weekend problem — "A phosphate buffer for the cell-culture lab".**
  I phosphoric acid: scale, predominance diagram; II pH of
  H₃PO₄, NaH₂PO₄, Na₂HPO₄ solutions (predominant reactions, checks);
  III mixing H₃PO₄ with NaOH: equivalent solutions; IV preparing 1 L of
  pH 7.20 buffer. **Named number: volume of 1.00 mol/L NaOH to add to
  0.100 mol of H₃PO₄ for pH 7.20** (computed). 26 questions.

## Ch. 11 — Precipitation and Solubility — `precipitation`

- **Hook.** Limescale in a kettle, a kidney stone, the white cloud of
  silver chloride in a chloride test.
- **Recall.** \cref{ch:b1:extent-q-and-k}, \cref{ch:b1:predominant-reaction};
  prose: Book 1 solubility in g/L, ion tests.
- **Sections.** 1 Solubility product. 2 Solubility and the condition of
  precipitation. 3 Common-ion and pH effects. 4 Existence domains and
  selective precipitation. 5 Amphoteric hydroxides.
- **Definitions.** `def:b1:precipitation:solubility-product` (solubility
  product, pKs); `:solubility` (solubility); `:existence-domain`
  (existence domain); `:common-ion` (common-ion effect);
  `:amphoteric-hydroxide`.
- **Ownership.** Map owner. Re-founds g6 `solutions-and-solubility`
  (solubility).
- **Statements.** `prop:…:precipitation-condition` Q ≥ Ks (proof from
  ch. 7); `prop:…:s-of-ks` for AB, AB₂, A₂B (proof); `prop:…:common-ion`
  (proof); `prop:…:hydroxide-ph` log s linear in pH, slope −n (proof);
  `prop:…:amphoteric` slope change at the complex (proof).
- **Methods.** `met:…:existence-domain`; `met:…:selective`.
- **Figures.** F `solubility-ph` (log s vs pH for Zn(OH)₂/Zn(OH)₄²⁻;
  part b Al(OH)₃); S existence domain on a pCl axis (AgCl); S hydroxide
  thresholds bar chart (Fe³⁺, Cu²⁺, Zn²⁺, Mg²⁺ at 0.01 mol/L); AI
  limestone cave; P coloured silver-halide precipitates (to find).
- **Ledger.** `ks:` AgCl, AgBr, AgI, Ag₂CrO₄, CaCO₃, CaF₂, BaSO₄,
  Fe(OH)₂, Fe(OH)₃, Cu(OH)₂, Zn(OH)₂, Mg(OH)₂, Al(OH)₃, CaC₂O₄ —
  computed from NBS-82 ΔfG° rows where no open critical compilation
  exists (see report); `logb:` Zn(OH)₄²⁻, Al(OH)₄⁻.
- **Weekend problem — "Cleaning a mine effluent".** I which hydroxides
  precipitate first; II pH thresholds at the given concentrations; III
  removing Fe³⁺ to 99.9 % while Cu²⁺ stays; IV then precipitating Cu²⁺ and
  Zn²⁺, amphoteric redissolution of Zn above a pH. **Named number: the pH
  window for removing iron(III) without losing copper(II)** (computed).
  25 questions.

## Ch. 12 — Complexation — `complexation`

- **Hook.** Ammonia poured on pale blue copper sulfate: first a pale
  precipitate, then an intense blue solution.
- **Recall.** \cref{ch:b1:lewis-resonance-vsepr} (Lewis acids/bases),
  \cref{ch:b1:predominant-reaction}, \cref{ch:b1:precipitation}.
- **Sections.** 1 Complexes and ligands. 2 Formation and dissociation
  constants. 3 Predominance and distribution in pL. 4 Competitions:
  two ligands, two metals, complexation against precipitation and
  against acidity.
- **Definitions.** `def:b1:complexation:complex` (complex, central atom,
  ligand); `:chelate` (polydentate ligand, chelate — **contested** with
  Y2 `coordination-complexes`, "denticity" left to Y2); `:formation-constant`
  (overall formation constant, successive formation constant,
  dissociation constant); `:pl-diagram` (pL scale).
- **Ownership.** Map owner (complex, ligand first meaning, constants).
  Not taken: denticity, coordination number of complexes, 18-electron
  rule, ligand field, isomerism and nomenclature of complexes (Y2).
- **Statements.** `prop:…:beta-k` β_n = ∏K_i (proof); `prop:…:pl-boundaries`
  (proof); `prop:…:competition-precipitation` K = β Ks (proof);
  `prop:…:ligand-acidity` (conditional constants qualitatively).
- **Methods.** `met:…:pl-diagram`; `met:…:dissolve-precipitate`.
- **Figures.** F `ammine-distribution` (Cu–NH₃ species vs pNH₃); S pL
  axis for Cu–NH₃ and Ag–NH₃; S structures [Cu(NH₃)₄]²⁺ (square plane),
  [Fe(CN)₆]⁴⁻ (octahedron), Ca–EDTA (chelate, chemfig + 3D); P copper
  sulfate vs copper ammine solutions (to find); no AI.
- **Ledger.** `logb:` Cu(NH₃)ₙ²⁺ n = 1–4, Ag(NH₃)ₙ⁺, Ag(S₂O₃)₂³⁻,
  FeSCN²⁺, Ca/Mg/Zn/Fe(III)–EDTA (IUPAC-EDTA; others: source to secure,
  **risk**, see report).
- **Weekend problem — "The photographer's fixer".** I silver bromide and
  its Ks; II thiosulfate complexes, β₂; III dissolution of AgBr by
  thiosulfate (K = β₂ Ks), solubility in 0.1 mol/L thiosulfate; IV
  ammonia cannot do it for AgBr but can for AgCl. **Named number: minimum
  thiosulfate concentration to dissolve 1.0 g of AgBr in 1 L**
  (computed). 25 questions.

## Ch. 13 — Redox Equilibria and the Nernst Equation — `nernst`

- **Hook.** A zinc strip and a copper strip in two beakers joined by a
  salt bridge light a diode: the redox reaction now runs through a wire.
- **Recall.** prose: Book 1 oxidants, reductants, couples, half-equations,
  cells; \cref{ch:b1:extent-q-and-k}.
- **Sections.** 1 Oxidation numbers. 2 Electrochemical cells. 3 Electrode
  potentials and the hydrogen electrode. 4 The Nernst equation. 5
  Predicting redox reactions; K° from standard potentials.
- **Definitions.** `def:b1:nernst:oxidation-number`; `:couple`
  (oxidant, reductant, redox couple, half-equation); `:cell`
  (electrochemical cell, half-cell, electrode, anode, cathode, salt
  bridge, cell voltage — **contested** with Y2 `cell-thermodynamics`);
  `:electrode-potential` (electrode potential, standard hydrogen
  electrode, standard potential); `:reference-electrode`;
  harvested `thm:…:nernst` (Nernst equation).
- **Ownership.** Map owner (electrode potential, Nernst). Re-founds g11
  `redox` and g12 `cells-and-electrolysis` (cell). Not taken: ΔrG = −nFE,
  concentration cell (Y2): the Nernst equation is `\admitted`, "derived
  in the Year 2 volume".
- **Statements.** `prop:…:on-rules` (oxidation-number rules; balancing by
  ON, proof of electron count); `thm:…:nernst` (admitted);
  `prop:…:equilibrium-constant` $\log K° = n(E°_1 - E°_2)/0.059$ (proof:
  equal potentials at equilibrium); `prop:…:combined-potentials`
  ($n_3E_3° = n_1E_1° + n_2E_2°$, proof from Nernst on a mixture);
  `prop:…:second-kind` $E°(\ce{AgCl}/\ce{Ag}) = E°(\ce{Ag+}/\ce{Ag}) -
  0.059\,\mathrm pK_s$ (proof).
- **Methods.** `met:…:oxidation-numbers`; `met:…:balance-by-on`;
  `met:…:predict-redox` (potential scale, rule of the gamma).
- **Figures.** S Daniell cell (two beakers, electrodes, salt bridge,
  voltmeter, electron and ion flows) — needs style pics; S standard
  hydrogen electrode; S vertical potential scale with the gamma rule
  (ledger E°); P Walther Nernst (`File:Walther Nernst.jpg`, PD) in
  `history` (1889); AI none.
- **Ledger.** `eo:` ~25 couples (alkali, Mg, Al, Zn, Fe, Ni, Pb, Cu, Ag,
  Au, Fe³⁺/Fe²⁺, I₂, Br₂, Cl₂, O₂/H₂O, MnO₄⁻, Cr₂O₇²⁻, H₂O₂, S₄O₆²⁻,
  Cu²⁺/Cu⁺, Cu⁺/Cu, Hg₂Cl₂/Hg, AgCl/Ag) — computed from NBS-82 ΔfG° in
  `figdata/bachelor-1/standard-potentials.py` (test asserts every printed
  value), unless an open primary E° table is found; `const:F`, `const:R`.
- **Weekend problem — "The electrode that measures chloride".** I
  oxidation numbers and half-equation of AgCl/Ag; II a cell Ag|AgCl|Cl⁻
  vs the hydrogen electrode; III E° of AgCl/Ag from E°(Ag⁺/Ag) and pKs;
  IV measuring the chloride of a water sample from a cell voltage.
  **Named number: E°(AgCl/Ag) ≈ 0.22 V** (computed). 24 questions.

## Ch. 14 — E–pH Diagrams — `e-ph-diagrams`

- **Hook.** An iron nail rusts in rain water, an iron hull is protected by
  zinc blocks, a copper roof turns green: one map reads them all.
- **Recall.** \cref{ch:b1:nernst}, \cref{ch:b1:predominant-reaction},
  \cref{ch:b1:precipitation}.
- **Sections.** 1 Conventions (working concentration, boundaries). 2
  Water. 3 Building a diagram: iron. 4 Copper and zinc. 5 Reading
  diagrams: stability in water, disproportionation, corrosion domains.
- **Definitions.** `def:b1:e-ph-diagrams:e-ph-diagram` (potential–pH
  diagram, working concentration); `:disproportionation`
  (disproportionation, comproportionation); `:water-domain` (stability
  domain of water); `:corrosion-domains` (immunity, corrosion,
  passivation domains — **contested** with Y2 `corrosion`, see report).
- **Ownership.** Map owner (E–pH, disproportionation). Not taken: i–E
  curves, fast/slow systems, overpotential, mixed potential (Y2) —
  kinetic stability told in prose with a pointer.
- **Statements.** `prop:…:boundary-slope` slope $-0.059\,m/n$ (proof);
  `prop:…:water-lines` (proof); `prop:…:disjoint-domains` (proof);
  `prop:…:disproportionation-criterion` (proof).
- **Methods.** `met:…:build` (ON ordering, vertical boundaries from Ks/pKa,
  Nernst boundaries, triple points); `met:…:read`.
- **Figures.** F `eph-diagrams` parts water, iron, copper, zinc (all
  boundaries computed from ledger rows); S method sketch (ON ladder →
  diagram); AI rusting ship hull with sacrificial anodes; P copper patina
  (Book 1 has one; Book 2 uses a different one if needed).
- **Ledger.** Reuse `eo:`, `ks:`, `pka:` rows; Cu₂O, CuO, Fe₂O₃/Fe(OH)₃,
  Fe(OH)₂, Zn(OH)₂, Zn(OH)₄²⁻ ΔfG° (NBS-82).
- **Weekend problem — "Bleach and the pool".** I oxidation numbers of
  Cl species; II the HClO/ClO⁻ boundary; III E–pH diagram of chlorine
  (Cl₂, HClO, ClO⁻, Cl⁻) at a working concentration; IV disproportionation
  of Cl₂ in base and the acidification danger. **Named number: the pH
  above which Cl₂ disproportionates at c = 0.010 mol/L** (computed).
  25 questions.

## Ch. 15 — Titration Methods and Curves — `titration-methods`

- **Hook.** A pharmacist must certify that a vitamin C tablet holds 500 mg:
  which titration, and how sure?
- **Recall.** \cref{ch:b1:predominant-reaction}, \cref{ch:b1:precipitation},
  \cref{ch:b1:complexation}, \cref{ch:b1:nernst}; prose: Book 1 colour
  titration, pH-metric and conductimetric curves.
- **Sections.** 1 Titration and equivalence. 2 Kinds: direct, back,
  successive, simultaneous. 3 pH-metric curves and indicators. 4
  Potentiometric curves. 5 Conductimetric curves; complexometric and
  precipitation titrations; precision.
- **Definitions.** `def:b1:titration-methods:titration` (titration,
  titrant, analyte, equivalence, equivalence point, end point);
  `:kinds` (direct titration, back titration, successive titrations,
  simultaneous titration); `:indicator` (colour indicator, turning
  zone); `:conductivity` (molar ionic conductivity; harvested
  `prop:…:kohlrausch` Kohlrausch's law); `:potentiometric`
  (potentiometric titration).
- **Ownership.** Map owner (titration types, rigorous equivalence).
  Re-founds g11 `titration`, g12 `ph-conductivity-titrations`,
  g12 `buffers-predominance` (indicator). Uncertainty forward-referenced
  to \cref{ch:b1:lab-techniques-1}.
- **Statements.** `prop:…:equivalence` (proof via the progress table);
  `prop:…:half-equivalence` pH = pKa (proof, conditions);
  `prop:…:ph-at-equivalence` (weak acid, proof); `prop:…:successive`
  (ΔpKa ≥ 4 criterion from a 99 % completeness requirement, proof);
  `prop:…:potentiometric-points` E(V_eq/2) = E°₁, E(2V_eq) = E°₂, E(V_eq)
  = (n₁E°₁ + n₂E°₂)/(n₁+n₂) (proof); `prop:…:conductimetric-slopes`
  (proof).
- **Methods.** `met:…:derivative`; `met:…:tangents`;
  `met:…:choose-indicator`; `met:…:back-titration`.
- **Figures.** F `titration-curves` parts strong–strong, weak–strong (+
  derivative), H₃PO₄ by NaOH, HCl + CH₃COOH mixture; F
  `potentiometric-titration` (Fe²⁺ by Ce⁴⁺); F
  `conductimetric-titration` (HCl and CH₃COOH by NaOH); S pH-metric
  set-up (burette, beaker, stirrer, combined electrode, meter) — needs
  style pics; AI teaching-lab bench with titrations (wide scene).
- **Ledger.** `lam:` λ° of H₃O⁺, HO⁻, Na⁺, Cl⁻, CH₃COO⁻, K⁺, NO₃⁻ (source to
  secure, **risk**); `ind:` turning zones of methyl orange, bromothymol
  blue, phenolphthalein (PubChem/IUPAC); `eo:` Ce⁴⁺/Ce³⁺ (formal, 1 mol/L
  H₂SO₄ — source to secure).
- **Weekend problem — "How much vitamin C in the tablet?".** I the
  iodine/ascorbic acid reaction; II why a back titration (excess I₂,
  thiosulfate); III the computation from the volumes; IV precision of the
  burette and of the pipette, the result's uncertainty (forward ref
  ch. 29). **Named number: mass of ascorbic acid per tablet ≈ 0.49 g**
  (from the given volumes). 25 questions.

## Ch. 16 — Stereochemistry in Depth — `stereochemistry-in-depth`

- **Hook.** Caraway and spearmint smell different, yet their main odorant
  is the same molecule — and its mirror image.
- **Recall.** prose: Book 1 chirality, enantiomers, Z/E, conformations;
  \cref{ch:b1:lewis-resonance-vsepr} (tetrahedral carbon).
- **Sections.** 1 Representations (Cram, Newman, Fischer). 2 Configuration:
  CIP rules, R/S, Z/E. 3 Chirality, enantiomers, diastereomers, meso. 4
  Conformations of ethane, butane, cyclohexane. 5 Optical activity.
- **Definitions.** `def:b1:stereochemistry-in-depth:isomers`
  (constitutional isomers, stereoisomers, configuration, conformation);
  `:representations` (Cram representation, Newman projection, Fischer
  projection — Fischer **contested** with Y2 `biomolecules`, earliest
  rule); `:cip` (CIP rules, R, S, Z, E descriptors);
  `:stereocentre` (stereogenic centre, chirality, chiral, achiral);
  `:enantiomers` (enantiomers, diastereomers, meso compound, racemic
  mixture); `:conformations` (torsion angle, eclipsed, staggered, anti,
  gauche, chair, axial, equatorial, ring flip); `:optical-activity`
  (optical activity, specific rotation, dextrorotatory, laevorotatory);
  harvested `prop:…:biot` (Biot's law).
- **Ownership.** Map owner (CIP, conformations, optical activity).
  Re-founds g12 `stereochemistry`. Not taken: enantiomeric excess,
  chiral auxiliaries (Y3 `asymmetric-synthesis`); point-group criteria
  (Y3) — chirality criterion stated with "no mirror plane, no centre"
  and `\admitted`.
- **Statements.** `prop:…:max-stereoisomers` $2^n$ (proof), fewer with meso
  (example); `prop:…:enantiomer-properties`; `prop:…:biot` (additivity,
  racemic zero, proof); `prop:…:chair-substituent` (equatorial preferred,
  1,3-diaxial reasoning).
- **Methods.** `met:…:cip`; `met:…:newman-from-cram`; `met:…:draw-chair`.
- **Figures.** S Cram/sawhorse/Newman of ethane and butane — needs Newman
  pic; F `butane-torsion` (energy vs torsion angle, ethane and butane); S
  chair cyclohexane, axial/equatorial, ring flip of methylcyclohexane —
  needs chair pic; S polarimeter; AI caraway seeds and spearmint leaves;
  P J. H. van 't Hoff (`File:Jacobus Henricus van 't Hoff.jpg`, PD) in
  `history` (1874 tetrahedral carbon).
- **Ledger.** `rot:` barriers ethane, butane anti→gauche and syn, cyclohexane
  ring flip, methyl A-value (CCCBDB / primary — **risk** for A-value);
  `alpha:` specific rotations of (R)- and (S)-carvone, (−)-menthol,
  sucrose (PubChem).
- **Weekend problem — "Menthol, the cool molecule".** I three
  stereocentres, eight stereoisomers, CIP of (−)-menthol (1R,2S,5R);
  II chair with all three substituents equatorial vs neomenthol; III
  specific rotation, the composition of a partly racemised sample
  (no ee term); IV comparing two commercial samples. **Named number: the
  percentage of (−)-menthol in a sample rotating at the given angle**
  (computed). 25 questions.

## Ch. 17 — Spectroscopy for Structure — `structure-spectroscopy`

- **Hook.** A perfumer's unknown smells of pineapple; three spectra and a
  formula name it in ten minutes.
- **Recall.** prose: Book 1 absorbance and Beer–Lambert, IR bands, ¹H NMR
  basics; \cref{ch:b1:lewis-resonance-vsepr} (π bonds).
- **Sections.** 1 UV–visible: conjugation and colour. 2 IR in depth. 3 ¹H
  NMR: shifts and equivalence. 4 Spin–spin coupling: multiplets and J. 5
  Solving a structure from formula and spectra.
- **Definitions.** `def:b1:structure-spectroscopy:absorbance` (absorbance,
  molar absorption coefficient, Beer–Lambert law re-founded as a
  definition-level statement); `:conjugation` (conjugated system,
  chromophore, absorption maximum); `:wavenumber` (wavenumber,
  transmittance, fingerprint region); `:chemical-shift` (chemical shift,
  shielding, equivalent protons); `:integration`; `:coupling` (spin–spin
  coupling, coupling constant, multiplet); harvested `prop:…:n-plus-one`
  (n + 1 rule); `:unsaturation` (degree of unsaturation).
- **Ownership.** Map owner (coupling, multiplet, conjugation). Re-founds g11
  `absorbance`, g11 `infrared`, g12 `proton-nmr`. Not taken: ¹³C NMR,
  DEPT, MS (Y2), pulses/2D/relaxation (Y3), HOMO/LUMO (Y2 — UV told with
  "the gap between the highest filled and lowest empty levels").
  *Shielding* here is nuclear shielding; ch. 2's term is *screening* (no
  homograph).
- **Statements.** `prop:…:shift-field-independent` (proof from the
  definition); `prop:…:n-plus-one` with binomial intensities (proof by
  counting spin states); `prop:…:unsaturation-formula` (proof by counting
  H); Beer–Lambert (physics, used).
- **Methods.** `met:…:solve-structure`.
- **Figures.** F `uv-polyenes`; F `ir-spectra` (ethanol, propanone,
  ethanoic acid — parts a–c); F `nmr-spectra` (ethyl ethanoate,
  ethanol, the problem's ester); S splitting tree (Pascal) for a quartet
  and a triplet; S IR correlation chart (bands at ledger ranges); AI
  carrots and tomatoes (carotenoid colours); P an NMR spectrometer (to
  find).
- **Ledger.** `uv:` λmax (and ε) of buta-1,3-diene, hexa-1,3,5-triene,
  β-carotene (source to secure); `ir:` band positions from NIST WebBook
  JCAMP of ethanol, propanone, ethanoic acid, ethyl ethanoate, the
  problem's ester; `nmr:` δ and J of ethyl ethanoate, ethanol,
  1-bromopropane, the problem's ester (SDBS/HMDB/nmrshiftdb2).
- **Weekend problem — "The pineapple molecule".** I combustion analysis →
  empirical formula, molar mass from a given MS-free datum (vapour
  density as data), degree of unsaturation; II IR (ester C=O, no O–H);
  III ¹H NMR: four signals, integrals, multiplicities, J; IV the structure
  ethyl butanoate and checking it against every peak. **Named number:
  molar mass of the unknown, 116 g/mol.** 26 questions.

## Ch. 18 — Electronic Effects and Reactive Intermediates — `electronic-effects`

- **Hook.** Trifluoroacetic acid is ten thousand times stronger than
  acetic acid, though the acidic O–H is three bonds away from the
  fluorines.
- **Recall.** \cref{ch:b1:periodicity}, \cref{ch:b1:lewis-resonance-vsepr},
  \cref{ch:b1:predominant-reaction}; prose: Book 1 curly arrows,
  nucleophiles and electrophiles.
- **Sections.** 1 Inductive effects. 2 Mesomeric effects. 3 Breaking a
  bond: homolysis, heterolysis; carbocations, carbanions, radicals. 4
  Nucleophiles, electrophiles, leaving groups. 5 Acidity and basicity of
  organic species.
- **Definitions.** `def:b1:electronic-effects:inductive` (inductive
  effect); `:mesomeric` (mesomeric effect, donor group, acceptor group);
  `:cleavage` (homolysis, heterolysis); `:intermediates` (reactive
  intermediate, carbocation, carbanion, radical); `:carbon-class` (class
  of a carbon: primary, secondary, tertiary); `:curly-arrow` (curly arrow,
  half-headed arrow); `:nucleophile` (nucleophile, electrophile,
  nucleophilicity, leaving group).
- **Ownership.** Map owner. Re-founds g12 `curly-arrows` (curly arrow,
  nucleophile, electrophile). Hyperconjugation and aromaticity (Y2) prose
  only.
- **Statements.** `prop:…:carbocation-order` (with allylic/benzylic;
  reasoning); `prop:…:inductive-pka` (chloroacetic series, ledger);
  `prop:…:mesomeric-pka` (phenol vs ethanol, nitrophenols);
  `prop:…:nucleophilicity-basicity` (correlation and its exceptions).
- **Methods.** `met:…:curly-arrows` (rules for drawing them).
- **Figures.** S resonance structures carboxylate, phenoxide, p-nitrophenoxide,
  amide; S pKa bar chart of the chloroacetic series (inline from ledger);
  S geometries of carbocation, radical, carbanion; S curly-arrow
  conventions; no AI.
- **Ledger.** `pka:` ethanoic (reuse), chloro-, dichloro-, trichloro-,
  trifluoroethanoic, ethanol, methanol, phenol, 2-, 3-, 4-nitrophenol,
  water-as-acid convention note (IUPAC-PKA).
- **Weekend problem — "Why trifluoroacetic acid is so strong".** I the
  inductive series; II mesomeric stabilisation of carboxylates vs
  alkoxides; III nitrophenols (ortho/meta/para, mesomeric vs inductive);
  IV a predominant-reaction calculation with TFA. **Named number:
  Ka(CF₃COOH)/Ka(CH₃COOH) ≈ 10⁴** (computed from the ledger). 24 q.

## Ch. 19 — Nucleophilic Substitution — `nucleophilic-substitution`

- **Hook.** Two bottles of 2-bromobutane, one optically pure: one
  reaction inverts it, another scrambles it.
- **Recall.** \cref{ch:b1:elementary-steps}, \cref{ch:b1:stereochemistry-in-depth},
  \cref{ch:b1:electronic-effects}, \cref{ch:b1:intermolecular-forces-solvents}.
- **Sections.** 1 The substitution and its partners. 2 SN2: kinetics,
  mechanism, inversion. 3 SN1: kinetics, carbocation, racemisation. 4
  What decides: substrate, nucleophile, leaving group, solvent.
- **Definitions.** `def:b1:nucleophilic-substitution:substitution`
  (nucleophilic substitution, substrate); `:sn2` (SN2 mechanism, Walden
  inversion); `:sn1` (SN1 mechanism, racemisation, solvolysis);
  `:stereospecific` (stereospecific reaction — not in the map, earliest
  rule).
- **Ownership.** Map owner (SN1, SN2).
- **Statements.** `prop:…:sn2-law` (proof from the elementary step);
  `prop:…:sn1-law` (proof from RDS/steady state); `prop:…:sn2-inversion`;
  `prop:…:sn1-stereo`; `prop:…:substrate`; `prop:…:leaving-group`
  (weak conjugate base); `prop:…:solvent`.
- **Methods.** `met:…:choose-mechanism`.
- **Figures.** S SN2 with `\chemmove` and Walden inversion (Cram); F
  `energy-profiles` part d (SN2 one hump vs SN1 two humps); S SN1 with
  planar carbocation, attack on both faces; S decision table; no AI.
- **Ledger.** GHS of the halogenoalkanes used (PubChem); no real relative
  rates printed (qualitative, or invented data in exercises).
- **Weekend problem — "Solvolysis of tert-butyl chloride".** I order from
  conductimetric data (first order); II k, half-life; III mechanism,
  stereochemistry with a chiral tertiary analogue; IV k at two
  temperatures → E_a. **Named number: activation energy of the
  solvolysis ≈ 90 kJ/mol** (from the problem's data). 25 questions.

## Ch. 20 — β-Elimination — `elimination`

- **Hook.** The same bromide gives an ether with sodium ethoxide at room
  temperature and an alkene when heated.
- **Recall.** \cref{ch:b1:nucleophilic-substitution},
  \cref{ch:b1:stereochemistry-in-depth}.
- **Sections.** 1 E2: kinetics and mechanism. 2 Anti-periplanar geometry
  and stereospecificity. 3 E1. 4 Regioselectivity: Zaitsev. 5
  Substitution or elimination?
- **Definitions.** `def:b1:elimination:elimination` (β-elimination, E2
  mechanism, E1 mechanism); `:periplanar` (anti-periplanar,
  syn-periplanar); `:selectivity` (regioselective, stereoselective
  reaction — earliest rule); harvested `prop:…:zaitsev` (Zaitsev's rule).
- **Ownership.** Map owner (E1, E2, Zaitsev). Hofmann elimination of
  ammonium salts (Y2 `amines`) not named.
- **Statements.** `prop:…:e2-law`, `prop:…:e1-law` (proofs);
  `prop:…:anti` (stereospecific E2, proof by Newman); `prop:…:cyclohexane-e2`
  (trans-diaxial requirement); `prop:…:zaitsev`; `prop:…:sn-vs-e` (table:
  base strength/bulk, temperature, substrate).
- **Methods.** `met:…:predict-alkene` (which H, which geometry).
- **Figures.** S E2 in Newman, anti-periplanar, with `\chemmove`; S E1;
  S E2 on a cyclohexane chair (diaxial H and Br); S SN/E decision chart;
  no AI.
- **Ledger.** GHS of bases/solvents named (PubChem).
- **Weekend problem — "Menthyl and neomenthyl chlorides".** I chairs of
  the two isomers; II which conformer has an axial Cl and anti H; III
  products of each (Zaitsev vs the only available anti H); IV rates from
  conformer fractions (equilibrium constants given). **Named number: the
  rate ratio k(neomenthyl)/k(menthyl)** (computed from the data). 24 q.

## Ch. 21 — Organomagnesium Reagents — `organomagnesium`

- **Hook.** Joining two carbon skeletons is the heart of synthesis; in 1900
  a young chemist found a reagent that does it in one flask.
- **Recall.** \cref{ch:b1:electronic-effects}, \cref{ch:b1:periodicity}
  (electronegativity of Mg vs C), \cref{ch:b1:lewis-resonance-vsepr}.
- **Sections.** 1 Preparing a Grignard reagent (conditions, apparatus). 2
  A strong base and a nucleophile: polarity inversion. 3 Additions to
  aldehydes, ketones and CO₂. 4 Building carbon skeletons (working
  backwards from an alcohol — without the Year 2 term *retrosynthesis*).
- **Definitions.** `def:b1:organomagnesium:organometallic` (organometallic
  compound, organomagnesium compound, Grignard reagent); `:umpolung`
  (polarity inversion).
- **Ownership.** Map owner (Grignard). Not taken: Grignard on esters/acyl
  derivatives (Y2 `acyl-substitution`), epoxide opening (Y2
  `alkene-redox`), retrosynthesis/disconnection/synthon (Y2).
- **Statements.** `prop:…:base` (reacts with any acidic H, proof via pKa
  scale); `prop:…:carbonyl-addition` (classes of alcohols obtained);
  `prop:…:co2`.
- **Methods.** `met:…:prepare` (with `inthelab`); `met:…:plan-alcohol`.
- **Figures.** S apparatus: three-neck flask, condenser + drying tube,
  dropping funnel, stirrer — needs style pics; S addition mechanism and
  hydrolysis with `\chemmove`; S solvation of RMgX by two ether molecules;
  P Victor Grignard (`File:Victor Grignard.jpg`, PD) in `history` (1900,
  Nobel 1912).
- **Ledger.** `ghs:` diethyl ether, bromobenzene, magnesium (PubChem).
- **Weekend problem — "Triphenylmethanol".** I preparing PhMgBr
  (quantities, why anhydrous, biphenyl side product); II addition to
  benzophenone, mechanism; III work-up; IV yield from the masses, and the
  alternative from CO₂ to benzoic acid. **Named number: yield of
  triphenylmethanol, in %** (from the given masses). 25 questions.

## Ch. 22 — Alcohols: Activating the OH Group — `alcohol-activation`

- **Hook.** OH⁻ is a terrible leaving group, yet alcohols are the most
  common starting materials: how do chemists make them react?
- **Recall.** \cref{ch:b1:nucleophilic-substitution},
  \cref{ch:b1:elimination}, \cref{ch:b1:predominant-reaction}.
- **Sections.** 1 Alcohols as acids: alkoxides. 2 The Williamson ether
  synthesis. 3 Activating OH: protonation, sulfonate esters. 4 Conversion
  to halides. 5 Acid-catalysed dehydration and ether formation.
- **Definitions.** `def:b1:alcohol-activation:alkoxide`;
  `:williamson` (Williamson ether synthesis); `:sulfonate` (sulfonate
  ester, tosylate, mesylate); `:dehydration` (dehydration of an alcohol).
- **Ownership.** Map owner (Williamson, sulfonate ester).
- **Statements.** `prop:…:alcohol-acidity` (ledger pKa); `prop:…:tosylation-retention`
  then SN2 inversion (proof by bond counting); `prop:…:hx-by-class`;
  `prop:…:ether-vs-alkene` (temperature).
- **Methods.** `met:…:williamson-choice` (which half carries the halide).
- **Figures.** S Williamson mechanism; S tosylation (retention) → SN2
  (inversion) on a stereocentre; S dehydration E1 with carbocation; S
  ether vs alkene vs temperature scheme; no AI.
- **Ledger.** `pka:` methanol, ethanol, propan-2-ol, 2-methylpropan-2-ol
  (IUPAC-PKA); `ghs:` sodium hydride, tosyl chloride, conc. sulfuric acid
  (PubChem).
- **Weekend problem — "Two roads to an ether".** I MTBE by Williamson: the
  two disconnections (in plain words) and why one fails (E2); II
  tosylate route from an optically active alcohol: configurations; III
  acid dehydration of 2-methylbutan-2-ol: alkenes, Zaitsev; IV masses and
  yield. **Named number: mass of MTBE from 10.0 g of 2-methylpropan-2-ol
  at the given yield** (computed). 24 questions.

## Ch. 23 — Carbonyls: Nucleophilic Additions, Acetals and Protection — `acetals-protection`

- **Hook.** Glucose in water is mostly a ring: its aldehyde has added to
  its own alcohol.
- **Recall.** \cref{ch:b1:organomagnesium}, \cref{ch:b1:extent-q-and-k}
  (Q/K: removing a product); prose: Book 1 protecting groups.
- **Sections.** 1 The carbonyl as an electrophile; acid activation. 2
  Hydrates and hemiacetals. 3 Acetals: mechanism, equilibrium, Dean–Stark.
  4 Protecting and deprotecting.
- **Definitions.** `def:b1:acetals-protection:hemiacetal` (hemiacetal,
  acetal); `:activation` (electrophilic activation of a carbonyl);
  `:protecting-group` (protecting group, protection, deprotection).
- **Ownership.** Map owner (acetal, protecting group). Re-founds g12
  `synthesis-strategy` (protecting group). Not taken: imines/enamines (Y2
  `amines`), choosing protecting groups in a route (Y2 `retrosynthesis`),
  sugars as biomolecules (Y2) — glucose only as the hook. "Shifting an
  equilibrium" (Y2) is avoided: the Dean–Stark argument is written with Q
  and K.
- **Statements.** `prop:…:acetal-mechanism`; `prop:…:dean-stark` (removing
  water keeps Q < K, proof); `prop:…:acetal-stability` (stable to bases,
  nucleophiles, hydrides; cleaved by aqueous acid).
- **Methods.** `met:…:protect` (protect → react → deprotect).
- **Figures.** S Dean–Stark apparatus — needs style pic; S acetalisation
  mechanism with `\chemmove` (two lines); S protection sequence; S
  glucose open chain ⇌ ring (chemfig); no AI.
- **Ledger.** `ghs:` toluene, ethane-1,2-diol, PTSA (PubChem).
- **Weekend problem — "A Grignard reagent that carries an aldehyde".**
  I why 4-bromobutanal cannot be turned into a Grignard reagent; II
  protection as a cyclic acetal, Dean–Stark; III the Grignard addition to
  propanone; IV deprotection and the final product; masses. **Named
  number: volume of water collected in the Dean–Stark trap at full
  conversion, ≈ 1.8 mL** (computed for the given amount). 25 questions.

## Ch. 24 — Oxidation and Reduction in Organic Chemistry — `organic-redox`

- **Hook.** Wine left open turns to vinegar; a ketone and an alcohol differ
  by two hydrogen atoms and two electrons.
- **Recall.** \cref{ch:b1:nernst} (oxidation numbers),
  \cref{ch:b1:acetals-protection}, \cref{ch:b1:organomagnesium}.
- **Sections.** 1 Oxidation levels of carbon. 2 Oxidising alcohols. 3
  Reducing carbonyls with hydrides (NaBH₄, LiAlH₄). 4 Selectivity.
- **Definitions.** `def:b1:organic-redox:oxidation-level`;
  `:hydride-donor` (hydride donor, complex metal hydride);
  `:chemoselective` (chemoselective reaction — earliest rule).
- **Ownership.** Map owner (oxidation level, hydride reduction). Not taken:
  alkene oxidations (Y2 `alkene-redox`), catalytic hydrogenation (Y2).
- **Statements.** `prop:…:on-of-carbon` (proof by ON rules);
  `prop:…:alcohol-oxidation` (primary → aldehyde → acid, secondary →
  ketone, tertiary no; proof by oxidation level and the carbinol H);
  `prop:…:hydride-scope` (NaBH₄ vs LiAlH₄).
- **Methods.** `met:…:balance-organic-redox` (half-equations with C).
- **Figures.** S oxidation-level ladder of the one-carbon family (CH₄ →
  CO₂) with ON; S NaBH₄ mechanism with `\chemmove`; S chemoselectivity
  map (which reagent reduces which group); AI wine barrels / a cellar.
- **Ledger.** `ghs:` NaBH₄, LiAlH₄, CrO₃ (PubChem); Book 1's
  `ghs:K2Cr2O7` cited read-only.
- **Weekend problem — "From cyclohexanol to nylon's adipic acid".** I
  oxidation levels of every carbon; II the nitric-acid oxidation equation
  (C₆H₁₂O + 2 HNO₃ → C₆H₁₀O₄ + N₂O + 2 H₂O) and electrons exchanged; III a
  greener route (H₂O₂) balanced; IV masses. **Named number: mass of N₂O
  formed per tonne of adipic acid by the nitric route, ≈ 0.30 t**
  (stoichiometric). 24 questions.

## Ch. 25 — Alkenes and Alkynes: Electrophilic Additions — `electrophilic-additions`

- **Hook.** Bromine water is decolourised instantly by an alkene: the
  oldest test for a double bond is a reaction mechanism.
- **Recall.** \cref{ch:b1:electronic-effects}, \cref{ch:b1:elementary-steps}
  (Hammond), \cref{ch:b1:stereochemistry-in-depth}.
- **Sections.** 1 The C=C π bond as a nucleophile. 2 Adding HX:
  Markovnikov, carbocations, rearrangements. 3 Adding water. 4 Adding X₂:
  halonium ions and anti addition. 5 Alkynes: additions and acetylides.
- **Definitions.** `def:b1:electrophilic-additions:electrophilic-addition`;
  harvested `prop:…:markovnikov` (Markovnikov's rule);
  `:rearrangement` (carbocation rearrangement); `:halonium` (halonium
  ion, anti addition, syn addition); `:hydration` (hydration of an
  alkene); `:acetylide` (terminal alkyne, acetylide ion).
- **Ownership.** Map owner (electrophilic addition, Markovnikov,
  halonium). Not taken: hydroboration, epoxidation, dihydroxylation,
  cleavage (Y2), radical additions (Y3), keto–enol tautomerism (Y2 —
  alkyne hydration told with a pointer), cationic rearrangements
  beyond 1,2-shifts (Y3).
- **Statements.** `prop:…:markovnikov` (empirical + modern form, proof via
  carbocation stability and Hammond); `prop:…:anti-addition` ((E)-but-2-ene
  → meso, (Z) → racemic, proof by drawing); `prop:…:acetylide-acidity`
  (qualitative unless sourced).
- **Methods.** `met:…:predict-addition`.
- **Figures.** S HBr addition with `\chemmove`; F `energy-profiles` part e
  (two carbocation routes); S bromonium anti addition (3D Cram); S
  rearrangement of 3,3-dimethylbut-1-ene with HCl; P Markovnikov
  (`File:VladimirMarkovnikov.jpg`, PD) in `history` (1870); AI ripening
  fruit (ethene, everyday) optional.
- **Ledger.** `ghs:` bromine (PubChem).
- **Weekend problem — "Two butenes and bromine".** I Z/E but-2-ene,
  CIP; II bromonium mechanism; III products of each: meso vs racemic,
  how many stereoisomers; IV optical rotation of each product and a
  yield. **Named number: specific rotation of the dibromide from
  (E)-but-2-ene: 0° (meso)**, plus the mass obtained. 24 questions.

## Ch. 26 — Hydrogen and the s-Block — `s-block`

- **Hook.** The world's lithium comes from salt flats and hard rock; it
  becomes the heart of every phone.
- **Recall.** \cref{ch:b1:periodicity}, \cref{ch:b1:nernst},
  \cref{ch:b1:precipitation}.
- **Sections.** 1 Hydrogen and the hydrides. 2 The alkali metals
  (properties, reaction with water as a teacher demonstration, production).
  3 Sodium compounds in industry (NaOH, Na₂CO₃ by the Solvay process). 4
  The alkaline-earth metals (Mg, Ca; the lime cycle). 5 Lithium.
- **Definitions.** `def:b1:s-block:hydride` (hydride: saline, covalent,
  metallic); `:families` (alkali metal, alkaline-earth metal);
  `:oxide-character` (basic oxide, acidic oxide, amphoteric oxide).
- **Ownership.** Map owner (hydrides, s-block terms). Re-founds g10
  `electron-shells` families. Industrial electrolysis analysed with i–E
  curves is Y2: the Downs and chlor-alkali cells are told, not modelled.
- **Statements.** `prop:…:reducing-power` (low IE, very negative E°);
  `prop:…:solvay` (overall equation, proof by summing steps);
  `prop:…:lime-cycle`.
- **Methods.** `met:…:mass-balance` (flow sheet mass balances).
- **Figures.** S Solvay process flow sheet; S lime cycle; S
  production-by-country bar chart of lithium (USGS, inline from ledger);
  P sodium under oil (`File:Chunks of sodium metal in mineral oil.jpg`,
  CC BY-SA 2.5); P Salar de Atacama ponds (`File:Salar de Atacama Lithium
  salt ponds 2018.jpg`, PD); P flame colours (`File:Coloured flames of
  methanol solutions of metal salts and compounds.jpg`, CC BY-SA 4.0,
  chemistry check of each colour); AI soda-ash plant.
- **Ledger.** `usgs:` lithium (world, top producers), soda ash, magnesium
  metal, lime (USGS-MCS latest); `solub:Li2CO3`, `solub:CaOH2`
  (IUPAC-NIST-SDS); reuse `ie:`, `eo:`, `ks:Mg(OH)2`.
- **Weekend problem — "Lithium from brine".** I brine composition and
  evaporation; II removing Mg²⁺ with lime (Ks); III precipitating Li₂CO₃
  with soda ash (solubility, temperature as data); IV mass balance.
  **Named number: mass of Li₂CO₃ per cubic metre of brine** (computed
  from given data). 24 questions.

## Ch. 27 — The p-Block I: Boron, Carbon and Nitrogen Groups — `p-block-13-15`

- **Hook.** Half the nitrogen in a human body has passed through an
  ammonia plant.
- **Recall.** \cref{ch:b1:crystals-ionic-covalent} (allotropes, silicon),
  \cref{ch:b1:s-block} (oxide character), \cref{ch:b1:nernst}.
- **Sections.** 1 Group 13: boron, aluminium (amphoteric hydroxide, Bayer
  process). 2 Group 14: carbon oxides and carbonates, silicon, silica,
  silicates. 3 Group 15: nitrogen, ammonia (Haber–Bosch), nitric acid
  (Ostwald). 4 Phosphorus and phosphates. 5 Trends down the groups.
- **Definitions.** `def:b1:p-block-13-15:oxoacid`; `:inert-pair`
  (inert-pair effect); `:nitrogen-fixation`.
- **Ownership.** Earliest-rule terms (not in the map). Not taken:
  equilibrium shifts and optimisation of Haber–Bosch (Y2
  `equilibrium-shifts`), Ellingham carbothermal reduction (Y2), aluminium
  electrolysis (Y2), zeolites (Y3).
- **Statements.** `prop:…:nitrogen-ladder` (ON −3 to +5);
  `prop:…:bayer` (amphoterism, proof from ch. 11); `prop:…:silicate-units`.
- **Methods.** `met:…:ostwald-balance` (chained equations).
- **Figures.** S nitrogen ON ladder with species; S Haber–Bosch → Ostwald
  chain; S SiO₄ tetrahedron and chain silicate; S P₄ tetrahedron, B(OH)₃;
  P bauxite (`File:Pisolitic bauxite (Alcoa Bauxite Mine, Arkansas, USA)
  1.jpg`, CC BY 2.0), quartz (`File:Quartz Crystal Cluster
  (2932215981).jpg`, CC BY 2.0), white/red phosphorus (`File:White
  phosphorus, containing a small amount of red phosphorus.jpg`, CC BY 3.0),
  borax (`File:Borax crystals.jpg`, PD); P Fritz Haber (`File:Fritz
  Haber.png`, PD) in `history`; AI fertiliser spreading on a field.
- **Ledger.** `usgs:` nitrogen (ammonia), phosphate rock, bauxite and
  alumina, silicon, boron; `pka:` boric, nitric (strong), phosphoric
  (reuse).
- **Weekend problem — "From air to fertiliser".** I N₂ and its triple bond;
  II Haber–Bosch stoichiometry; III Ostwald: three equations, ON of N;
  IV ammonium nitrate and mass balances. **Named number: mass of nitric
  acid obtainable per tonne of ammonia, ≈ 3.7 t** (complete conversion).
  25 questions.

## Ch. 28 — The p-Block II: Oxygen, Halogens and Noble Gases — `p-block-16-18`

- **Hook.** Sulfuric acid is the most produced chemical in the world;
  its output once measured a nation's industry.
- **Recall.** \cref{ch:b1:lewis-resonance-vsepr}, \cref{ch:b1:e-ph-diagrams}
  (chlorine disproportionation), \cref{ch:b1:elementary-steps} (catalysis).
- **Sections.** 1 Oxygen and ozone; peroxides. 2 Sulfur, its oxides and
  sulfuric acid (contact process). 3 The halogens: trends, hydrogen
  halides, oxoacids of chlorine. 4 Noble gases and their compounds.
- **Definitions.** `def:b1:p-block-16-18:chalcogen`; `:halogen` (halogen
  — re-founds Book 1 families); `:interhalogen`.
- **Ownership.** Earliest-rule terms. Not taken: O₂ paramagnetism from MOs
  (Y2), stratospheric ozone chemistry (Y3 `environmental-toxicology`,
  `photochemistry`) — prose only.
- **Statements.** `prop:…:halogen-oxidising-order` (E°); `prop:…:sulfuric-strength`
  (first strong, second pKa — ledger); `prop:…:contact-steps`.
- **Methods.** `met:…:contact-balance`.
- **Figures.** S contact-process flow sheet; S VSEPR shapes SO₂, SO₃, SF₆,
  XeF₂, XeF₄, ClF₃; S halogen trend chart (E°, from ledger); P sulfur
  mining (`File:Sulfur mining in Kawah Ijen - Indonesia - 20110608.jpg`,
  CC BY-SA 4.0); P bromine (`File:Bromine-ampoule.jpg`, CC BY 3.0); P
  iodine (`File:Iodine crystals, 99.9% purity.jpg`, CC BY 3.0); P
  chlorine (`File:Chlorine ampoule.jpg`, CC BY-SA 3.0); AI public
  swimming pool (chlorination).
- **Ledger.** `usgs:` sulfur, iodine, fluorspar, bromine (if covered);
  `pka:` HSO₄⁻, HClO (reuse), HF (reuse); reuse `eo:` halogens.
- **Weekend problem — "One tonne of sulfur".** I combustion of S, ON;
  II catalytic oxidation SO₂ → SO₃ (catalyst role, ch. 9); III absorption
  in H₂SO₄ (why not water), oleum; IV mass balance and the second
  acidity. **Named number: mass of H₂SO₄ from one tonne of sulfur ≈ 3.06
  t.** 24 questions.

## Ch. 29 — Lab Techniques I: Safety, Measurement and Separation — `lab-techniques-1`

- **Hook.** Two students measure the same melting point and find 134 °C
  and 136 °C: are they in agreement, and is the product pure?
- **Recall.** \cref{ch:b1:intermolecular-forces-solvents},
  \cref{ch:b1:titration-methods}; prose: Book 1 extraction, recrystallisation,
  TLC, yield.
- **Sections.** 1 Hazards: GHS pictograms, H and P statements, safety data
  sheets, waste. 2 Measurement and uncertainty (type A, type B,
  comparing with a reference). 3 Separating: extraction, filtration,
  recrystallisation, simple distillation. 4 Identifying and checking
  purity: TLC, melting point, refractometry.
- **Definitions.** `def:b1:lab-techniques-1:hazard` (hazard, risk);
  `:ghs` (hazard pictogram, signal word, hazard statement, precautionary
  statement, safety data sheet); `:uncertainty` (measurement uncertainty,
  standard uncertainty, type A evaluation, type B evaluation, expanded
  uncertainty, relative uncertainty); `:z-score` (normalised deviation —
  earliest rule, Y2 `measurement-statistics` recalls it);
  `:partition-coefficient` (partition coefficient — **contested** with
  Y2 `chromatography`); `:recrystallisation`; `:retention-factor`.
- **Ownership.** Map owner (lab safety, GHS, uncertainty). Re-founds g10
  `chemical-species` (TLC, retention factor) and g10 `synthesis-yield`
  (recrystallisation). Not taken: confidence intervals, regression,
  propagation as a theory, limits of detection (Y2): the quadrature rule
  for sums and products is `\admitted` with a pointer; fractional
  distillation and azeotropes (Y2) prose only.
- **Statements.** `prop:…:type-a` u = s/√n (admitted, Y2); `prop:…:type-b`
  rectangular a/√3 (proof by integral); `prop:…:combine` (admitted);
  `prop:…:multiple-extractions` (proof: $(1+KV_o/V_a)^{-n}$).
- **Methods.** `met:…:read-sds`; `met:…:report-result`; `met:…:recrystallise`;
  `met:…:tlc`; `met:…:melting-point`.
- **Figures.** S GHS grid (nine `\ghs` with meanings); F
  `type-a-uncertainty` (histogram + Gaussian; part b rectangular); S
  simple distillation — needs style pics; S Büchner filtration — needs
  style pics; S TLC plate with Rf construction (`tlcplate`); S
  recrystallisation steps (erlenmeyer, funnel); P Kofler bench
  (`File:Koflerbank.jpg`, CC BY-SA 3.0); P Abbe refractometer (`File:Abbe
  refractometer.jpg`, PD); AI teaching laboratory, students in goggles and
  coats (lab scene).
- **Ledger.** `ghs:` ethanol, propanone, dichloromethane, ethoxyethane,
  cyclohexane, conc. HCl, NaOH, ethanoic anhydride, salicylic acid,
  aspirin (PubChem); `mp:` aspirin, acetanilide, benzoic acid (PubChem /
  NIST WebBook); `nD:` water, ethanol (source to secure).
- **Weekend problem — "Purifying aspirin".** I hazards of the reagents
  (pictograms, H/P); II recrystallisation: solvent choice, yield; III
  melting point: type A from repeated readings, type B from the bench
  graduation, combined; IV comparison with the reference and TLC.
  **Named number: the normalised deviation z between the measured and
  reference melting points** (computed; verdict "compatible" if z < 2).
  25 questions.
