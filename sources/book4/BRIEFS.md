# Book 4 (University Chemistry, Year 3) — chapter briefs

Phase A plan, 2026-10-02. Year `parts/bachelor-3`, label prefix `b3`, entry
`one_chemistry_book_4_university_year_3.tex`. 33 chapters in outline order.
Binding rules: `sources/BATCH_BOOKS_1-4.md` (read it first). Term list:
`DEFINITIONS.md`. State, projection and traps: `PROGRESS.md`.

Checked against: Book 2's real harvest (perl command of
`SERIES_DEFINITIONS.md`, 2026-10-02), Book 1's real harvest (all grades), and
Book 3's frozen map (`sources/book3/DEFINITIONS.md`, granted at Sync S2, with
the S2 rulings in `SERIES_DEFINITIONS.md`). Book 4 is the **last volume**: it
has no forward pointer to another book, and it pays every debt the earlier
volumes left to "the Year 3 volume" (list below).

## Conventions for every chapter

- **Register (Year 3).** Laws are `theorem`/`proposition` with a derivation
  at Year-3 level: operators, commutators and eigenproblems (quantum
  chemistry), group representations and orthogonality (symmetry), partition
  functions, Stirling and Lagrange multipliers (statistical thermodynamics),
  linear stability through the eigenvalues of a Jacobian (oscillations),
  separable PDEs and the error function (diffusion), inference on fitted
  parameters (standard errors of a slope and intercept, t and F tests). What
  is not derived gets `\admitted` with "treated in more advanced courses" or
  "established experimentally" — **never** a pointer to another volume of
  this series (there is none after this one). Partial derivations are
  `\begin{proof}[Partial proof]`.
- **Recall boxes** cite Books 1–3 in prose only: "the school volume" or "Book
  1 (grade 12)", "the Year 1 volume, on …", "the Year 2 volume, on …";
  physics as "from physics" (classical mechanics, the Maxwell–Boltzmann
  distribution of speeds, Fick's laws, Poisson's equation, the Fourier
  transform). `\cref{ch:b3:…}` only inside this book (backward, or forward
  inside the book where a later chapter of this volume develops a point).
- **Definitions.** `\emph{term}\index{term}` only inside a `definition`, only
  for a term this book owns (`DEFINITIONS.md`). Named laws this book owns may
  carry their `\emph{}\index{}` in the theorem that states them (Sync S2,
  point 2): Schrödinger equation, Eyring equation, Butler–Volmer equation,
  Tafel equation, Langmuir isotherm, BET isotherm, Bragg's law, Kasha's rule,
  Stern–Volmer equation, Michaelis–Menten equation, Marcus theory's
  cross relation, Woodward–Hoffmann rules, Baldwin's rules, Hill equation,
  Kelvin equation, Young's equation, Gibbs adsorption isotherm. A term owned
  by Book 2 or Book 3 is used plainly, with a recall box when it matters.
  **Homographs to keep apart** (each defined only as the phrase on the
  right): spin *multiplicity* (vs Book 2's cell multiplicity), *order of a
  point group* (vs kinetic order), *class of symmetry operations* (vs carbon
  class), *reduction formula* (vs redox reduction), *spectroscopic term*
  (never bare "term"), *microstate* only in ch10 (ch2 says "determinant" or
  "arrangement"), *transmission probability* (tunnelling, ch1) vs
  *transmission coefficient* (TST, ch12), *chemical relaxation time* (ch13)
  vs *longitudinal/transverse relaxation time* (ch8), *fluorescence
  quencher* (vs Book 1's quenching of a reaction), *kinetically inert
  complex* (vs inert atmosphere, inert gas), *kinetic resolution* (never
  bare "resolution": Book 3 ch31 owns chromatographic resolution), *catalytic
  constant* k_cat (Book 3 owns turnover number/frequency of a catalyst).
- **Calibration.** 12 exercises (4★, 5★★, 3★★★), one weekend problem of 22–28
  questions in Parts I–IV ending on a named number; ~11.5 pp per chapter
  (target ≈ 9.5–10 body + 2 solutions). Books 1–3 landed 13–14 % short: every
  derivation in full, a worked example after each substantial statement, an
  `inthelab` box wherever a procedure exists, a `history` box per chapter, ~4
  schematics per chapter (illustrations and photographs on top).
- **Tags.** **S** schematic (TikZ / chemfig / modiagram / tikz-3dplot /
  pgfplots of a formula); **F** figdata curve or table
  (`figdata/bachelor-3/<name>.py` + `tests/bachelor-3/test_<name>.py`, list in
  `PROGRESS.md`); **AI** illustration (everyday, industrial or lab scene
  only, JPEG, never glassware close-ups or molecules); **P** photograph
  (Commons or NASA, licence re-verified through the API before insertion).
- **No Python printed**, ever: computational chemistry (minimal-basis HF,
  Tanabe–Sugano diagonalisation, CV simulation, LEPS surface) lives in tested
  figdata; the chapter prints the method, the equations and the results.
- **Notation.** Hydroxide `\ce{OH-}`, `\ce{H3O+}`; hartree `E_h`, bohr `a_0`
  (units requested at the sync); term symbols ${}^{2S+1}L_J$ (macro requested);
  Mulliken symbols $a_{1g}$ for orbitals, $A_{1g}$ for states; Schoenflies
  symbols for point groups, Hermann–Mauguin for space groups; IUPAC sign
  convention for currents (anodic positive) in ch15.
- **Ledger.** Ids prefixed by kind; grep all ledgers before minting; cite
  Book 1–3 rows read-only (`re:`, `lat:`, `geo:`, `dip:`, `pka:`, `ie:`,
  `asd:`, `janaf:`, `dfg:`, `ghs:`, `usgs:`, `nmr:`, `ir:`, `const:`, Book
  3's `s0:`, `dfh:`, `c13:`, `mass:`, `iso:`, `who:` …). New prefixes for this
  book: `diat:` (diatomic constants, `diat:HCl.we`), `vib:` (polyatomic
  fundamentals), `lev:` (atomic energy levels), `rotl:` (rotational line
  frequencies), `bse:` (basis-set parameters), `qc:` (published computed
  energies), `ct:` (character tables), `xray:` (X-ray wavelengths), `nuc:`
  (nuclear spins and moments), `kin:` (rate parameters), `fl:` (photophysical
  data), `cmc:`, `st:` (surface tension), `bet:`, `lf:` (ligand-field bands),
  `hb:` (oxygen binding), `iza:` (zeolite frameworks), `gm:` (green metrics),
  `env:` (atmospheric and water data), `gwp:`, `tox:` (LD50 etc.),
  `kow:`, `eg:` (band gaps), `visc:`.
- **Planned sources** (keys for `sources/ledger/book4.md`; reachability
  probed by curl 2026-10-02 where marked ✓): CODATA (shared rows) ✓; NIST-ASD
  (levels and lines) ✓; WEBBOOK-DIAT (Huber–Herzberg constants) ✓; WEBBOOK-VIB
  / NSRDS-NBS39 (Shimanouchi fundamentals); CCCBDB (experimental geometries
  and frequencies, published computed energies) ✓; BSE (Basis Set Exchange,
  STO-3G parameters, from Hehre–Stewart–Pople 1969) ✓; KATZER and SYMOTTER
  (character tables; tables are also checked by the orthogonality test) ✓;
  BILBAO (point-group tables; **timed out** from this machine); COD
  (crystal structures) ✓; NIST-XRAY (X-ray transition energies database:
  Cu Kα); CDMS or NIST-RRF (rotational rest frequencies); JANAF ✓ and
  CODATA-KEY (Book 3's rows read-only); IUPAC-ATMOS (IUPAC Task Group on
  atmospheric chemical kinetic data, datasheets) ✓; NIST-KIN ✓; IAPWS
  (surface tension and viscosity of water); NSRDS-NBS36 (Mukerjee & Mysels,
  CMCs); NIST-SP960 (BET practice guide: N₂ cross-section); CALTECH-MS
  (mineral spectroscopy server: ruby, emerald); IAEA-NUC (nuclear magnetic
  moments, INDC(NDS)-0658); NMRSHIFTDB ✓ / SDBS; PUBCHEM ✓ (GHS, LD50, logP,
  structures); RCSB-PDB ✓ (haemoglobin, myoglobin coordinates); IZA
  (zeolite structure database); JMTR (Johnson Matthey Technology Review,
  open access: Cativa process); NOBEL (Nobel lectures, for history); IPCC-AR6
  (GWP, lifetimes); NOAA-GML (CO₂, CH₄, N₂O means; agency named in the ledger
  only); WHO-DWQ and SANDER-2023 (Book 3 keys, read-only); IUPAC-PKA;
  NSRDS-NBS10 (dipoles, Book 2 key); IEA (ammonia technology roadmap); PMC
  (open-access reviews, one DOI per row); NASA (photographs); COMMONS.
  Unreachable here: Gold Book and IUPAC PAC (Cloudflare 403), Bilbao, JPL
  data evaluation, ioffe.ru — use the alternatives above or EXCLUDE.

## Debts left by Books 2–3 to "the Year 3 volume", and where they are paid

| Promise in Book 2/3 | Paid in |
|---|---|
| hydrogen wavefunctions "solved in the Year 3 volume"; real angular functions | ch1 §4 (rotor → spherical harmonics, real combinations), §5 (hydrogen solved: separation, 1s/2p by substitution, $E_n$) |
| Koopmans' theorem (ionisation energy ≈ −ε) | ch3 §4 |
| orbital labels "derived from group theory" | ch5 §2 |
| SCF, group theory behind Hückel | ch3, ch5 |
| statistical entropy, partition functions | ch10 |
| van 't Hoff from partition functions | ch11 §3 |
| Butler–Volmer, Tafel, voltammetry; shape of slow-system i–E curves | ch15 |
| term splitting, Tanabe–Sugano, Jahn–Teller, susceptibility; MO picture of π effects on Δo | ch18 (term states), ch20 §2 (π effects with symmetry-adapted combinations) |
| ligand substitution mechanisms | ch19 |
| cycloaddition classification, Woodward–Hoffmann | ch26 |
| pulses (DEPT's sequence explained) | ch8 §2–3 |
| asymmetric hydrogenation and epoxidation; asymmetric Robinson/Wieland–Miescher | ch28 |
| olefin metathesis; Ziegler–Natta | ch21 |
| enzyme kinetics | ch13 |
| kinetic isotope effects | ch12 |
| heterocycles (pyridine basicity) | ch29 |
| Schlenk line and glovebox | ch33 |
| inference on fitted parameters (S2 point 3: Year 3 = statistics beyond least squares) | ch12 (standard errors of slope and intercept, Eyring), ch15 (inverse prediction from a calibration), ch33 (t and F tests, outliers) |

---
## Ch. 1 — Quantum Mechanics for Chemists: Model Systems — `quantum-model-systems`

- **Hook.** A row of cyanine-dye solutions, from yellow to blue: the only
  difference between the molecules is the length of their chain. An electron
  "in a box" of that length explains the colour to within a few per cent.
- **Recall (prose).** The Year 1 volume (quantised levels of the hydrogen
  atom, quantum numbers, $E = h\nu$, energy level, ground and excited state);
  the Year 2 volume (wavefunction, probability density, radial and angular
  parts, nodes; the hydrogen functions were admitted there and are solved
  here); from physics: momentum, de Broglie wavelength, the classical
  harmonic oscillator. Mathematics: linear ODEs, eigenvectors (Hückel).
- **Sections.** 1 Operators, eigenvalues and the Schrödinger equation
  (postulates in working form: state, observable ↔ Hermitian operator,
  measured values = eigenvalues, expectation value; commutators and
  simultaneous eigenfunctions). 2 The particle in a box (1D, then 3D and
  degeneracy; the free-electron model of conjugated dyes). 3 The harmonic
  oscillator (ladder-operator solution; zero-point energy; wavefunctions,
  parity, turning points; a diatomic as an oscillator with its reduced
  mass). 4 The rigid rotor (ring rotor solved; $\hat L^2$ eigenvalues
  $l(l+1)\hbar^2$ with spherical harmonics, real combinations $p_x$, $p_y$,
  $d_{xy}$…; degeneracy $2J+1$). 5 The hydrogen atom and tunnelling
  (separation of $r$ and angles; $1s$ and $2p$ solved by substitution, $E_n$;
  rectangular barrier: decay inside, transmission probability; H versus D;
  ammonia inversion; the scanning tunnelling microscope).
- **Definitions.** `def:b3:quantum-model-systems:operator` (operator,
  eigenfunction, eigenvalue); `:hermitian` (Hermitian operator, expectation
  value); `:commutator` (commutator); `:schrodinger` (Hamiltonian operator;
  named law *Schrödinger equation* in `thm:…:schrodinger` — map: Y3 owns
  the formal equation); `:degenerate` (degenerate levels, degeneracy);
  `:box` (particle in a box, free-electron model); `:oscillator` (harmonic
  oscillator, force constant, reduced mass, zero-point energy); `:ladder`
  (ladder operators); `:rotor` (rigid rotor, spherical harmonics);
  `:tunnelling` (tunnelling, transmission probability).
- **Ownership check.** Map: Y3 owns the Schrödinger equation (formal) and the
  model systems. Book 2 owns *energy level*, *ground state*, *excited state*,
  *atomic orbital*, quantum numbers: recalled. Book 3 owns *wavefunction*,
  *probability density*, *radial/angular part*, *nodal surface*, *radial
  node*: recalled, never redefined (the chapter says "the wavefunction of the
  Year 2 volume is now the solution of an eigenproblem"). *Operator*,
  *eigenvalue*, *degeneracy*, *force constant*, *reduced mass* are not in
  any map nor in the Book 2/3 harvests: earliest need. No Book 1 notion
  re-founded.
- **Statements.** `thm:…:hermitian-real` eigenvalues of a Hermitian operator
  are real, eigenfunctions of distinct eigenvalues orthogonal (proof);
  `thm:…:schrodinger` (time-independent equation as the eigenproblem of
  $\hat H$; stationary states, admitted as a postulate with its
  justification); `prop:…:commuting` commuting operators share
  eigenfunctions (proof, non-degenerate case); `thm:…:box` $E_n =
  n^2h^2/8mL^2$, $\psi_n$ (proof); `prop:…:box-3d` separation and
  degeneracy of the cubic box (proof); `prop:…:free-electron`
  $\lambda = 8mcL^2/[h(N+1)]$ for a dye with $N$ π electrons (proof);
  `thm:…:oscillator` $E_v = (v+\tfrac12)h\nu$ by ladder operators (proof
  from $[\hat x,\hat p] = \iu\hbar$); `prop:…:oscillator-functions`
  $\psi_0$, $\psi_1$, $\psi_2$ (Hermite) by substitution, parity (proof);
  `thm:…:ring` $E_m = m^2\hbar^2/2I$ (proof); `thm:…:rotor`
  $E_J = J(J+1)\hbar^2/2I$, degeneracy $2J+1$ (`\admitted`, treated in more
  advanced courses, checked by substitution of $Y_{1,0}$ and $Y_{1,\pm1}$);
  `prop:…:real-harmonics` real combinations and their Cartesian forms
  (proof); `thm:…:hydrogen` $E_n = -hcR_\infty\,\mu/m_e\,/n^2$ (partial
  proof: radial equation, $1s$ and $2p$ solved by substitution, general $n$
  admitted); `prop:…:barrier` decay $\eu^{-\kappa x}$ inside a barrier and
  $T \approx 16\varepsilon(1-\varepsilon)\eu^{-2\kappa a}$ for a thick barrier
  (partial proof: matching conditions written, the algebra admitted).
- **Methods.** `met:…:one-dimensional` (setting up and solving a 1D
  problem: potential, boundary conditions, quantisation, normalisation);
  `met:…:expectation` (computing an expectation value by symmetry and
  integration).
- **Boxes.** `history` Schrödinger 1926 and the four papers; `inthelab`
  measuring λmax of a dye series and fitting the box length.
- **Figures.** F `particle-in-box` (ψₙ and |ψₙ|² for n = 1–4 stacked at their
  energies; part b: predicted versus measured λmax of three cyanine dyes);
  F `harmonic-oscillator` (parabola, levels, ψ₀–ψ₃ and the classical
  turning points); S rotor ladder with degeneracies 1, 3, 5, 7 and the
  first spherical-harmonic lobes (Book 3's orbital pics); F `tunnelling`
  (transmission probability versus energy for H and D through the same
  barrier, log scale); S hydrogen radial functions $R_{10}$, $R_{21}$ from the
  solved equations (plotted by pgfplots from the formula); AI a row of
  coloured dye vials on a lab bench (lab scene); P Schrödinger (Commons,
  1933 Nobel portrait, PD — verify).
- **Ledger.** Shared `const:` (h, c, me, a0, Eh, Rinf, u); λmax of three
  symmetric cyanine dyes (PubChem/vendor data sheets or PhotochemCAD; **at
  risk** — else EXCLUDED and the dye example becomes β-carotene with a
  sourced λmax); `diat:HCl.we`, `diat:H2.we` (WebBook, shared with ch6);
  ammonia inversion frequency (NIST-RRF); proton mass `const:mp`.
- **Exercises palette.** Box energies for an electron in 0.5 and 1 nm;
  degeneracies of the cubic box; commutator $[\hat x,\hat p_x]$ and
  $[\hat L_z, \hat x]$; expectation values ⟨x⟩, ⟨x²⟩ in the box; zero-point
  energies of H₂ and D₂; oscillator selection of parity; rotor levels and
  degeneracies of HCl; normalising a trial function; tunnelling ratio H/D;
  free-electron prediction for hexatriene; Hermiticity of $\hat p$.
- **Weekend problem — "How long is a dye?"** I the free-electron model of a
  polymethine (box length from bond lengths, N π electrons, HOMO→LUMO);
  II predicted λmax for three dyes against the measured values; III a
  refined box (end corrections, effective length fitted from one dye);
  IV the oscillator and the rotor of the same molecule's C–C stretch and
  end-over-end rotation (orders of magnitude: electronic ≫ vibrational ≫
  rotational). **Named number: the effective box extension δ (pm) that
  reproduces the measured λmax of the middle dye** (computed in figdata).
  24 questions.

## Ch. 2 — Many-Electron Atoms and Term Symbols — `many-electron-atoms`

- **Hook.** In 1895 helium's spectrum looked like that of two different
  elements, "orthohelium" and "parahelium", which never exchanged light.
  The two families are the triplet and singlet states of one atom: spin and
  the Pauli principle at work.
- **Recall.** Year 1 volume: quantum numbers, configurations, Pauli, Hund,
  Klechkowski, unpaired electrons; Year 2 volume: orbital energies, Slater's
  rules; \cref{ch:b3:quantum-model-systems} (operators, hydrogen, rotor,
  angular momentum).
- **Sections.** 1 Spin and spin-orbitals ($s = \tfrac12$, α and β,
  $\hat S^2$, $\hat S_z$). 2 Indistinguishable electrons and the Slater
  determinant (exchange symmetry, antisymmetry, Pauli as a theorem). 3 Helium:
  Coulomb and exchange (1s2s singlet and triplet, first-order energies,
  $\Delta E = 2K$; ortho/para helium). 4 Russell–Saunders coupling and term
  symbols (L, S, J; counting arrangements; terms of $p^2$, $p^3$, $d^2$;
  closed shells contribute nothing). 5 Hund's rules and spin–orbit coupling
  (ground terms; Landé interval rule; the sodium D doublet; atomic selection
  rules; heavy atoms and jj coupling, qualitatively).
- **Definitions.** `def:b3:many-electron-atoms:spin-orbital` (spin-orbital);
  `:indistinguishable` (indistinguishable particles, antisymmetric
  wavefunction); `:slater` (Slater determinant); `:exchange` (exchange
  integral); `:singlet-triplet` (singlet state, triplet state);
  `:russell-saunders` (Russell–Saunders coupling, total orbital angular
  momentum quantum number, total spin quantum number, total angular
  momentum quantum number); `:term` (spectroscopic term, spin multiplicity,
  term symbol); `:spin-orbit` (spin–orbit coupling, fine structure).
- **Ownership check.** Map: Y1 owns quantum numbers and configurations;
  Y3 `many-electron-atoms` recalls them. Book 2 owns *spin quantum number*,
  *unpaired electron*, and states the Pauli principle and Hund's rule as
  propositions (no index): this chapter proves Pauli from antisymmetry and
  states Hund's rules *for terms* without re-indexing either name. The word
  "level" (a ${}^{2S+1}L_J$ of given J) is used plainly, never indexed: Book
  2's *energy level* and this book's "level of theory" would collide. Book 3's
  *Coulomb integral* (Hückel α) is not used for the two-electron $J$, which
  is called "the electron-repulsion integral" without definition.
  "Microstate" is avoided here (ch10 owns it).
- **Statements.** `thm:…:pauli` an antisymmetric function vanishes when two
  electrons share a spin-orbital (proof: equal columns); `prop:…:helium`
  $E(^1S) - E(^3S) = 2K$ at first order (proof); `prop:…:closed-shell`
  $L = S = 0$ for a filled subshell (proof by counting $M_L$, $M_S$);
  `prop:…:count` number of arrangements $\binom{2(2l+1)}{N}$ (proof);
  `prop:…:hund-terms` Hund's rules for the ground term (`\admitted`,
  established experimentally; rationale from exchange); `prop:…:lande`
  $E(J) - E(J-1) = AJ$ (proof from $\hat{\mathbf L}\cdot\hat{\mathbf S}$);
  `prop:…:selection-atoms` ΔS = 0, ΔL = 0, ±1, ΔJ = 0, ±1 (not 0→0)
  (`\admitted`; ΔS = 0 proved in ch7).
- **Methods.** `met:…:terms` (terms of a configuration with the $M_L$/$M_S$
  table: $p^2$ → ³P, ¹D, ¹S); `met:…:ground-term` (ground term and level
  from a box diagram, more/less than half full).
- **Boxes.** `history` the two heliums and Pauli's exclusion principle
  (1925); `inthelab` resolving the sodium D doublet with a grating.
- **Figures.** S the $M_L$/$M_S$ table of $p^2$ (tabular with marks);
  F `atomic-levels` (level diagram of carbon $2p^2$: configuration → terms →
  levels at NIST energies, and of helium 1s2s/1s2p singlets and triplets;
  test: positions equal ledger values, Landé ratio for ³P); S sodium 3s/3p
  levels with the D1/D2 transitions; S vector model of L and S coupling to J
  (precession cones, schematic); P helium discharge tube or helium
  spectrum (Commons, licence to verify); AI none.
- **Ledger.** `lev:` rows from NIST ASD: He 1s2s ³S₁, ¹S₀, 1s2p ³P, ¹P₁; C
  2p² ³P₀,₁,₂, ¹D₂, ¹S₀; N 2p³ ⁴S, ²D, ²P; Na 3p ²P₁/₂, ²P₃/₂ (and the D1/D2
  lines); ground levels of Ti²⁺, V³⁺, Cr³⁺, Fe²⁺, Ni²⁺ (for ch18); He
  ionisation energies (Book 2 `ie:` if present, else `lev:`).
- **Exercises palette.** Determinant of Li 1s²2s; why no two electrons in
  one spin-orbital; terms of $d^2$ and $p^4$; ground terms of O, N, Ti²⁺,
  Fe³⁺, Co²⁺; Landé ratios for C; number of arrangements of $d^3$; allowed
  transitions in sodium; K from the He singlet–triplet gap; levels of a
  ²D term; why ⁴S is the ground term of N.
- **Weekend problem — "Two heliums".** I spin-orbitals and the two
  determinants of 1s2s; II exchange: from the NIST 1s2s ³S–¹S gap, the
  exchange integral K; III terms of carbon and nitrogen, Landé check against
  NIST; IV ground terms and levels of the transition-metal ions of ch18.
  **Named number: the exchange integral K(1s,2s) of helium, in eV** (half the
  ¹S–³S gap; computed from `lev:` rows). 25 questions.

## Ch. 3 — Computational Chemistry: Hartree–Fock and DFT — `computational-chemistry`

- **Hook.** HeH⁺, made in the first minutes of the expanding Universe and
  detected in a planetary nebula only in 2019, was "known" decades earlier
  from a calculation: a computer can describe a molecule nobody has put in a
  bottle.
- **Recall.** \cref{ch:b3:quantum-model-systems} (operators, hydrogen),
  \cref{ch:b3:many-electron-atoms} (Slater determinant, exchange); Year 2
  volume: LCAO, overlap/Coulomb/resonance integrals, secular determinant,
  Hückel method; Year 1 volume: ionisation energy.
- **Sections.** 1 Born–Oppenheimer and the potential energy surface
  (separating nuclei and electrons; PES; stationary points; optimisation;
  harmonic frequencies from the Hessian). 2 The variational principle
  (theorem; helium with an effective ζ; linear variation gives the secular
  equations, and Hückel as a special case). 3 Basis sets (Slater versus
  Gaussian functions; contraction; STO-3G; split valence, polarisation,
  diffuse functions; the basis-set limit). 4 Hartree–Fock (the energy of a
  determinant; the Fock operator; Roothaan–Hall $FC = SC\varepsilon$; the
  SCF loop; Koopmans' theorem; the correlation energy; RHF H₂ dissociates
  wrongly). 5 Density-functional theory and what a calculation can and cannot
  tell (Hohenberg–Kohn, Kohn–Sham, functionals; typical accuracies of
  geometries, frequencies, energies; computed versus measured).
- **Definitions.** `def:b3:computational-chemistry:born-oppenheimer`
  (Born–Oppenheimer approximation); `:pes` (potential energy surface,
  stationary point, equilibrium geometry, geometry optimisation); `:basis`
  (basis set, minimal basis set, Slater-type orbital, Gaussian-type orbital,
  contracted Gaussian function); `:split-valence` (split-valence basis set,
  polarisation function, diffuse function); `:hartree-fock` (Hartree–Fock
  method, Fock operator, self-consistent field); `:correlation` (electron
  correlation, correlation energy); `:dft` (electron density,
  density-functional theory, exchange–correlation functional, Kohn–Sham
  orbitals). Named-law statements: `thm:…:variational` (variational
  principle), `thm:…:koopmans` (Koopmans' theorem).
- **Ownership check.** Not in the map except as the outline chapter; none of
  these terms in Book 2/3 harvests or maps. Book 3 owns *LCAO*, *secular
  determinant*, *overlap/Coulomb/resonance integral*, *Hückel method*,
  *photoelectron spectroscopy*: recalled. *Potential energy surface* is
  placed here (earliest need in this book; ch12 recalls it and adds the
  saddle point and minimum energy path).
- **Statements.** `thm:…:variational` $\langle\phi|\hat H|\phi\rangle \ge E_0$
  (proof by expansion); `prop:…:helium-zeta` ζ = 27/16, $E = -(27/16)^2 E_h$
  (proof); `prop:…:linear-variation` linear trial functions give
  $\det(H - ES) = 0$ (proof); `prop:…:hessian` harmonic frequencies from the
  eigenvalues of the mass-weighted Hessian (partial proof; links ch5);
  `thm:…:roothaan` Roothaan–Hall equations (partial proof: stationarity of
  the closed-shell energy with orthonormality constraints, Lagrange);
  `thm:…:koopmans` $I_i \approx -\varepsilon_i$ (proof at frozen orbitals);
  `prop:…:rhf-dissociation` the RHF H₂ wavefunction at large R is half ionic
  (proof in the minimal basis); `thm:…:hohenberg-kohn` (`\admitted`, treated
  in more advanced courses).
- **Methods.** `met:…:scf` (the SCF procedure, step by step);
  `met:…:read-calculation` (convergence, frequencies: all real → minimum,
  one imaginary → transition structure; comparing with experiment);
  `met:…:choose-level` (method and basis for a question and a budget).
- **Boxes.** `history` HeH⁺ from calculation to detection (1925 discovery in
  the lab, 2019 astronomical detection); `inthelab` a computational workflow
  (build, optimise, frequencies, single point) as a lab procedure.
- **Figures.** F `minimal-basis-hf` (RHF/STO-3G energy of H₂ versus R, with
  the exact-ish experimental Morse curve from ledger $D_e$, $\omega_e$, $r_e$;
  part b: HeH⁺ SCF energy per iteration; part c: STO-1G/2G/3G fits to the 1s
  Slater function); S SCF flowchart (`shapes.geometric`); S a schematic 2D
  PES with two minima and a saddle (contours drawn analytically); S
  hierarchy of methods and basis sets (cost versus accuracy, qualitative);
  AI a computing cluster room (industrial scene).
- **Ledger.** `bse:H.sto3g`, `bse:He.sto3g` (exponents and coefficients,
  BSE, citing Hehre–Stewart–Pople 1969); `qc:H2.hf.sto3g`, `qc:HeHp.hf.sto3g`
  (published RHF/STO-3G energies: CCCBDB computed data, else a textbook
  value with its source **at risk**); He total energy from the two ionisation
  energies (NIST ASD, computed in figdata); `diat:H2.De` or D0 + ωe (WebBook);
  `re:H2` (Book 2, read-only); HeH⁺ detection 2019 (Nature paper metadata,
  DOI); CCCBDB experimental versus HF geometries of H₂O (Book 2 `geo:` rows).
- **Exercises palette.** Variational energy of H with a Gaussian trial
  (−0.424 Eₕ, computed); a polynomial trial in the box; ζ for He⁺-like ions;
  counting basis functions of benzene in STO-3G and 6-31G(d); cost scaling
  N⁴; Koopmans for N₂ against its photoelectron spectrum (Book 3 data
  read-only, or EXCLUDED); reading an output with one imaginary frequency;
  BO and isotopes (H₂ and D₂ share one PES); correlation energy of He;
  choosing a functional; why RHF fails for H₂ at 3 Å.
- **Weekend problem — "HeH⁺, the first molecule".** I the STO-3G basis for H
  and He from the ledger; II the integrals at R = 1.4632 a₀ (given from the
  figdata table: S, T, V, two-electron); III two SCF cycles by hand, the
  orbital energies and the total energy; IV dissociation to He + H⁺ and the
  proton affinity of He at this level against its experimental value
  (if sourced). **Named number: the RHF/STO-3G total energy of HeH⁺ at
  1.4632 a₀** (computed by the figdata; the code is tested on the classic
  minimal-basis benchmark — H₂ at 1.4 a₀, −1.1167 Eₕ, and HeH⁺ with
  ζ_He = 2.0925, −2.8607 Eₕ — and the printed standard-basis value
  (ζ_He = 1.69, BSE) against CCCBDB if listed there). 26 questions.

## Ch. 4 — Symmetry and Point Groups — `point-groups`

- **Hook.** A snowflake turned by 60° looks unchanged; so does a benzene
  molecule. Symmetry decides, before any calculation, whether a molecule has
  a dipole, whether it is chiral, and (ch5) which of its vibrations a
  spectrometer will see.
- **Recall.** Year 1 volume: VSEPR shapes, dipole moment, chirality,
  stereogenic centres, cubic cells; Year 2 volume: symmetry argued in words
  for fragment orbitals.
- **Sections.** 1 Symmetry operations and elements (E, Cₙ, σ (v, h, d), i,
  Sₙ; powers; products; S₁ = σ, S₂ = i). 2 Groups (axioms; point group;
  order; multiplication table of C₂ᵥ and C₃ᵥ; classes; subgroups).
  3 Assigning a point group (flowchart; worked: H₂O, NH₃, BF₃, CH₄, SF₆,
  benzene, staggered and eclipsed ethane, allene, CHFClBr, trans-N₂F₂,
  linear molecules C∞ᵥ/D∞ₕ; the cube and methane). 4 Consequences: polarity
  and chirality (theorems). 5 Representations and character tables
  (matrices of operations on (x, y, z); characters; irreducible
  representations; the layout of a character table; Mulliken symbols;
  reading C₂ᵥ, C₃ᵥ, D₃ₕ, T_d, O_h).
- **Definitions.** `def:b3:point-groups:operation` (symmetry operation,
  symmetry element); `:rotation` (proper rotation axis, principal axis);
  `:mirror` (mirror plane, vertical mirror plane, horizontal mirror plane,
  dihedral mirror plane); `:inversion` (centre of inversion); `:improper`
  (improper rotation axis); `:point-group` (point group, order of a point
  group); `:class` (class of symmetry operations, subgroup); `:schoenflies`
  (Schoenflies symbol); `:representation` (matrix representation,
  character); `:irrep` (irreducible representation, character table,
  Mulliken symbol).
- **Ownership check.** Map: Y3 `point-groups` owns *point group*, *symmetry
  operation*, *character table*. Book 3 owns *symmetry-adapted combination*
  (words only there): not touched here. Book 2 owns *chiral*, *dipole moment*,
  *polar molecule*: recalled. "Group" alone is never defined (Book 2's
  periodic group; phrase *point group* only); "order" and "class" are
  defined only as the phrases above.
- **Statements.** `prop:…:closure` the symmetry operations of a molecule
  form a group (proof); `prop:…:fixed-point` all elements meet in one point
  (proof via centre of mass); `thm:…:polar` a molecule can be polar only in
  C₁, Cₛ, Cₙ, Cₙᵥ (proof: μ invariant); `thm:…:chiral` a molecule is chiral
  iff it has no improper axis (proof both ways); `prop:…:class-characters`
  operations of one class have equal characters (proof by trace);
  `prop:…:irrep-count` number of irreps = number of classes, Σd² = h
  (`\admitted`; proved from orthogonality in ch5); `prop:…:direct-sum`
  block-diagonal matrices reduce a representation (proof).
- **Methods.** `met:…:assign` (the flowchart, with examples);
  `met:…:matrices` (matrix of an operation acting on x, y, z).
- **Boxes.** `history` Schoenflies 1891 and crystallographic groups;
  `inthelab` a molecular-model kit as the tool for finding elements.
- **Figures.** S symmetry elements drawn on H₂O, NH₃, BF₃ and CH₄
  (tikz-3dplot ball-and-stick with planes and axes); S methane in a cube
  (`omcubeo`, C₃, C₂/S₄ axes); S stereographic projections of C₂ᵥ, C₃ᵥ, D₃ₕ
  (style need); S assignment flowchart (`shapes.geometric`); S character
  tables of C₂ᵥ and C₃ᵥ (character-table layout, style need); P a snowflake
  (Bentley 1902, PD — verify); AI everyday objects with symmetry (a
  three-bladed fan, a hexagonal nut, a starfish).
- **Ledger.** `ct:C2v`, `ct:C3v`, `ct:D3h`, `ct:Td`, `ct:Oh`, `ct:D6h`,
  `ct:C2h`, `ct:D2h`, `ct:C4v`, `ct:D4h` (KATZER / SYMOTTER, with the test
  that parses each printed table and checks orthogonality and Σd² = h);
  molecular geometries read-only from Book 2 `geo:` rows (shapes only).
- **Exercises palette.** Elements of ethene, XeF₄, PCl₅, cyclohexane chair
  (D₃d), ferrocene staggered/eclipsed, 1,3,5-trichlorobenzene; multiplication
  table of C₂ₕ; matrices of C₃ about z; order and classes of D₃ₕ; polarity and
  chirality predictions; twisted biphenyl (D₂) is chiral; S₄ in a
  tetrahedral molecule without a mirror; subgroup chains Oₕ → D₄ₕ → C₄ᵥ on
  substitution.
- **Weekend problem — "Substituting methane".** I the 24 operations of CH₄
  located in a cube, classes; II the point groups of CH₃Cl, CH₂Cl₂, CHCl₃,
  CHFClBr, CH₂FCl; III polarity and chirality of each from the theorems; IV
  counting the distinct dichloro and trichloro isomers of methane and of
  benzene from the operations (orbit counting, argued). **Named number: the
  order of T_d, h = 24, checked as Σd² = 1 + 1 + 4 + 9 + 9.** 22 questions.

## Ch. 5 — Group Theory Applied — `group-theory-applied`

- **Hook.** Carbon dioxide traps the Earth's heat while nitrogen and oxygen,
  which make up 99 % of the air, do not. Which vibrations a molecule can use
  to absorb infrared light is a question of symmetry.
- **Recall.** \cref{ch:b3:point-groups}; Year 2 volume: fragment orbitals,
  symmetry-adapted combinations, MO diagrams of H₂O, NH₃, CH₄; Year 1
  volume: IR spectroscopy, wavenumber, polarisability.
- **Sections.** 1 Reducing a representation (the great orthogonality theorem,
  admitted; the reduction formula, proved; worked: the H 1s set of NH₃
  = A₁ + E). 2 Symmetry-adapted orbitals (projection operator; the H₂O,
  NH₃ and CH₄ sets; the σ set of an octahedral ML₆ = A₁g + E_g + T₁ᵤ, for
  ch18 and ch20; the orbital labels of the Year 2 volume derived).
  3 Vibrational modes (Γ₃ₙ from unshifted atoms; subtracting translations and
  rotations; H₂O 2A₁ + B₂; NH₃ 2A₁ + 2E; CH₄ A₁ + E + 2T₂; CO₂ through D₂ₕ;
  internal-coordinate representations: Γ(stretch)). 4 Selection rules (direct
  products; the vanishing-integral theorem; IR active ⇔ x, y, z; Raman
  active ⇔ quadratic functions; mutual exclusion). 5 Applications: counting
  CO stretches of carbonyl complexes (cis/trans, fac/mer), electronic
  transitions allowed by symmetry (bridge to ch7 and ch18).
- **Definitions.** `def:b3:group-theory-applied:reducible` (reducible
  representation, totally symmetric representation); `:direct-product`
  (direct product); `:projection` (projection operator); `:normal-mode`
  (normal mode); `:activity` (IR active, Raman active). Named statements:
  `thm:…:reduction` (reduction formula), `prop:…:mutual-exclusion`
  (mutual exclusion rule).
- **Ownership check.** Book 3 owns *symmetry-adapted combination*,
  *fragment orbital*: used and recalled; the projection operator is the new
  tool that builds them. Book 2 owns *wavenumber*, *polarisability*,
  *fingerprint region*: recalled. Map: "MOs → Y3 `group-theory-applied`
  recalls" — this chapter recalls the MO terms and adds the group theory.
- **Statements.** `thm:…:great-orthogonality` (`\admitted`, treated in more
  advanced courses; checked numerically on C₃ᵥ); `cor:…:characters`
  orthogonality of characters and Σd² = h (proof from the theorem);
  `thm:…:reduction` $n_i = \frac1h\sum_c g_c\,\chi(c)\chi_i(c)$ (proof);
  `prop:…:projection` the projected function transforms as $\Gamma_i$
  (partial proof); `prop:…:gamma-3n` χ(R) = (unshifted atoms) × (1 + 2cos θ
  ± …) (proof); `prop:…:mode-count` 3N − 6 (3N − 5) vibrations (proof
  from Γ₃ₙ); `thm:…:vanishing-integral` (proof: the integral is invariant
  under every operation); `cor:…:ir-raman` (proof from the theorem with the
  dipole and polarisability components); `prop:…:mutual-exclusion` (proof
  from g/u parity).
- **Methods.** `met:…:reduce` (reduction with a table); `met:…:salc`
  (projection operator in practice); `met:…:vibrations` (Γ_vib and IR/Raman
  counts); `met:…:co-count` (CO stretches of a carbonyl complex).
- **Boxes.** `history` Wigner and Bethe bring group theory to chemistry
  (1929–31); `inthelab` an IR and a Raman spectrometer side by side.
- **Figures.** S normal modes of H₂O (three arrows diagrams with a₁, a₁,
  b₂) and of CO₂ (four modes); S the NH₃ hydrogen combinations a₁, e with
  lobes (Book 3's `oms` pic); S MO diagram of H₂O with the derived labels
  (Book 3's `omlevel`/`omcorr`); F `reduction` (computed table: Γ₃ₙ and its
  reduction for H₂O, NH₃, CH₄, CO₂(D₂ₕ), BF₃, XeF₄, SF₆, IR/Raman counts —
  printed as a table read by the chapter; test: counts and results); F
  `co2-spectra` (synthetic IR and Raman spectra of CO₂ gas at ledger
  positions: IR bands at ν₂, ν₃ only, Raman at the ν₁/2ν₂ dyad; test: no IR
  band at ν₁); AI none.
- **Ledger.** `vib:CO2.nu1`…`nu3` and the Fermi dyad (NSRDS-NBS39 / CCCBDB);
  `vib:H2O.*`, `vib:NH3.*`, `vib:CH4.*` (same source); CO stretch
  frequencies of one cis/trans pair or fac/mer pair (open literature, **at
  risk**; else exercise data clearly presented as a measured spectrum of
  "a complex").
- **Exercises palette.** Reduce given representations of C₂ᵥ, C₃ᵥ, D₄ₕ;
  Γ_vib of SO₂, BF₃, XeF₄, CH₂Cl₂; IR/Raman counts for SF₆ (only T₁ᵤ IR) and
  for C₂H₂; SALCs of the F 2p_z set of BF₃; mutual exclusion in trans-N₂F₂;
  cis versus trans ML₄(CO)₂ by IR; fac versus mer; symmetry of the water
  bend; is the 2349 cm⁻¹ band of CO₂ allowed (yes, Σᵤ⁺); direct products
  E × E in C₃ᵥ.
- **Weekend problem — "Cis or trans? A carbonyl complex read by its
  spectrum".** I point groups of cis- and trans-[ML₄(CO)₂], fac- and
  mer-[ML₃(CO)₃]; II Γ_CO and its reduction for each; III IR and Raman
  counts; IV assignment of a measured spectrum (data of the problem) and a
  check by the Raman bands. **Named number: the number of IR-active CO
  stretches of the mer isomer, 3 (against 2 for fac).** 23 questions.

## Ch. 6 — Rotational and Vibrational Spectroscopy — `rovibrational-spectroscopy`

- **Hook.** Radio telescopes in a high desert "hear" carbon monoxide in a
  cold cloud between the stars at 115.27 GHz: the molecule's first
  rotational line, from which its bond length and the cloud's temperature
  follow.
- **Recall.** \cref{ch:b3:quantum-model-systems} (rotor, oscillator,
  reduced mass); \cref{ch:b3:group-theory-applied} (selection rules); Year 1
  volume: IR, wavenumber, polarisability, bond lengths.
- **Sections.** 1 Rotational spectra (rotational constant; gross selection
  rule: a permanent dipole; ΔJ = ±1; lines at 2B(J+1); bond length from B;
  centrifugal distortion; intensities: degeneracy × Boltzmann, J_max;
  isotopologues). 2 Vibrations of real bonds (anharmonicity; the Morse
  potential and its levels; fundamental, overtones, hot bands; $D_e$, $D_0$;
  Birge–Sponer). 3 Rovibrational bands (P and R branches, no Q for a ¹Σ
  diatomic; combination differences give B₀ and B₁ and α_e; the H³⁵Cl/H³⁷Cl
  doublets). 4 Raman spectroscopy (Rayleigh, Stokes, anti-Stokes;
  polarisability selection rule; rotational Raman ΔJ = 0, ±2, spacing 4B,
  first line at 6B; N₂'s intensity alternation; vibrational Raman).
  5 Polyatomic molecules (linear, symmetric-top and asymmetric-top rotors,
  qualitatively; group frequencies through ch5).
- **Definitions.** `def:b3:rovibrational-spectroscopy:rotational-constant`
  (rotational constant, isotopologue); `:selection` (gross selection rule,
  specific selection rule); `:centrifugal` (centrifugal distortion
  constant); `:anharmonic` (anharmonicity constant, fundamental transition,
  overtone, hot band); `:morse` (Morse potential); `:dissociation`
  (spectroscopic dissociation energy); `:branches` (P branch, Q branch, R
  branch, band origin); `:raman` (Raman scattering, Rayleigh scattering,
  Stokes line, anti-Stokes line); `:rotor-types` (symmetric top, asymmetric
  top, spherical top).
- **Ownership check.** Not in the map apart from the chapter. Book 2 owns
  *wavenumber*, *polarisability*; Book 3 owns *bond dissociation enthalpy*
  (298 K, molar): the spectroscopic $D_0$/$D_e$ (per molecule, 0 K, from
  levels) is a different quantity, named by the phrase *spectroscopic
  dissociation energy* and contrasted in a remark.
- **Statements.** `prop:…:rotational-lines` $\tilde\nu = 2B(J+1)$ (proof);
  `prop:…:jmax` $J_{\max} \approx \sqrt{kT/2hcB} - \tfrac12$ (proof);
  `prop:…:centrifugal` lines with $-4D(J+1)^3$ (admitted form);
  `prop:…:morse-levels` $G(v) = \omega_e(v+\tfrac12) - \omega_e x_e(v+\tfrac12)^2$
  (`\admitted` for the Morse potential, treated in more advanced courses;
  checked numerically); `cor:…:de` $D_e = \omega_e^2/4\omega_e x_e$ and
  $D_0 = D_e - G(0)$ (proof); `prop:…:birge-sponer` (proof);
  `thm:…:combination-differences` (proof); `prop:…:raman-classical`
  sidebands at $\nu_0 \pm \nu_{\text{vib}}$ when α varies with the coordinate
  (proof by a product of cosines); `prop:…:rotational-raman` lines at
  $6B, 10B, \dots$ from the exciting line (proof).
- **Methods.** `met:…:bond-length` (B → I → r); `met:…:combination`
  (analysing a rovibrational band); `met:…:birge-sponer`.
- **Boxes.** `history` Raman and Krishnan, 1928; `inthelab` a gas cell in an
  FTIR spectrometer: resolution needed to split H³⁵Cl/H³⁷Cl.
- **Figures.** F `rotational-spectrum` (CO absorption lines at 30 K and
  300 K with Boltzmann × (2J+1) intensities; part b: N₂ rotational Raman
  with 2:1 alternation; test: spacing 2B, J_max, spacing 4B, first line 6B,
  alternation ratio); F `morse-levels` (Morse and harmonic curves of HCl with
  levels, $D_e$, $D_0$ marked; Birge–Sponer plot; test: level formula,
  $D_e = \omega_e^2/4\omega_e x_e$, number of bound levels); F `rovib-band`
  (HCl fundamental with P/R branches and the ³⁵/³⁷ doublets; test: band
  origin gap, combination differences recover B₀, B₁); S Raman energy scheme
  (virtual level, Rayleigh/Stokes/anti-Stokes arrows; Jablonski-style
  levels); P an array of radio antennas in a high desert (Commons, ESO,
  CC BY 4.0 — verify; attribution at caption end).
- **Ledger.** `diat:CO.Be`, `.ae`, `.we`, `.wexe`, `diat:HCl.*` (H³⁵Cl:
  Be, αe, ωe, ωexe, De-centrifugal), `diat:N2.Be`, `diat:H2.*`, `diat:I2.*`
  (WebBook Huber–Herzberg); `rotl:CO.1-0` (115.271 GHz; CDMS or NIST-RRF);
  isotope masses (`aw:`/Book 3 `mass:` rows, read-only); ³⁵Cl/³⁷Cl abundance
  (Book 3 `iso:` or CIAAW, read-only).
- **Exercises palette.** r(CO) from B; ¹³CO line shift; HCl and DCl
  rotational lines; J_max at 300 K; anharmonic constants from fundamental
  and first overtone; De and D0 of HCl; Birge–Sponer extrapolation from
  given ΔG; which molecules have pure rotational / Raman spectra (H₂, HCl,
  CO₂, CH₄, SF₆); rotational Raman of N₂; rovibrational line positions;
  intensity of a hot band at 1000 K.
- **Weekend problem — "Listening to a cold cloud".** I the CO J = 1←0 line:
  B₀, I and r₀; II line intensities of J = 1←0, 2←1, 3←2 (problem data) and
  the excitation temperature; III the ¹³CO lines and the isotope ratio;
  IV the CO fundamental band in the infrared, anharmonicity and $D_0$.
  **Named number: r₀(CO) = 113.1 pm from the 115.271 GHz line** (computed;
  contrasted with $r_e$ from Book 2's `re:CO`). 25 questions.

## Ch. 7 — Electronic Spectroscopy and Photophysics — `electronic-spectroscopy`

- **Hook.** A glass of tonic water under a black-light lamp glows blue: the
  quinine absorbs invisible ultraviolet and gives it back as visible light,
  a few nanoseconds later and a little redder.
- **Recall.** Year 1 volume: absorbance, Beer–Lambert, molar absorption
  coefficient, chromophore, conjugated system; Year 2 volume: HOMO, LUMO,
  π→π*; \cref{ch:b3:many-electron-atoms} (singlet, triplet),
  \cref{ch:b3:group-theory-applied} (vanishing integral),
  \cref{ch:b3:rovibrational-spectroscopy} (vibrational levels, Morse).
- **Sections.** 1 Electronic transitions and selection rules (transition
  dipole moment; oscillator strength and the integrated band; spin rule;
  Laporte rule; symmetry; n→π*, π→π*, charge-transfer transitions).
  2 The Franck–Condon principle (vertical transitions, Franck–Condon factors,
  vibronic progressions, band shapes; the iodine B←X spectrum). 3 Fates of an
  excited state: the Jablonski diagram (vibrational relaxation, internal
  conversion, intersystem crossing, fluorescence, phosphorescence; Kasha's
  rule; mirror-image rule; Stokes shift). 4 Kinetics of excited states
  (rate constants, lifetime, radiative lifetime, quantum yields; Stern–Volmer
  quenching; static versus dynamic quenching; energy transfer in outline).
  5 Applications (fluorimetry and its sensitivity; time-resolved
  measurement; fluorescent probes; phosphorescent emitters).
- **Definitions.** `def:b3:electronic-spectroscopy:transition-dipole`
  (transition dipole moment, oscillator strength); `:vibronic` (vibronic
  transition, vibronic progression, Franck–Condon factor);
  `:charge-transfer` (charge-transfer transition); `:jablonski` (Jablonski
  diagram); `:radiationless` (vibrational relaxation, internal conversion,
  intersystem crossing); `:luminescence` (luminescence, fluorescence,
  phosphorescence, Stokes shift); `:lifetime` (excited-state lifetime,
  radiative lifetime); `:quantum-yield` (quantum yield, fluorescence quantum
  yield); `:quencher` (fluorescence quencher, dynamic quenching, static
  quenching). Named statements: `thm:…:franck-condon` (Franck–Condon
  principle), `thm:…:laporte` (Laporte rule), `prop:…:kasha` (Kasha's
  rule), `thm:…:stern-volmer` (Stern–Volmer equation).
- **Ownership check.** Book 2 owns *absorbance*, *molar absorption
  coefficient*, *chromophore*, *conjugated system*, *absorption maximum*;
  Book 3 owns *HOMO*, *LUMO*: recalled. Book 1 owns "quenching" in the
  kinetic sense (stopping a reaction) in Book 1 only; this book defines only
  the phrases *fluorescence quencher*, *dynamic/static quenching*. Ligand-to-
  metal and metal-to-ligand charge transfer are ch18's; the generic
  *charge-transfer transition* is defined here (earliest need). *Quantum
  yield* defined here for any process that follows absorption; ch14 uses it
  for reactions without redefining.
- **Statements.** `prop:…:intensity` absorption intensity ∝ |μ_fi|²
  (`\admitted`, from time-dependent perturbation theory, treated in more
  advanced courses); `prop:…:oscillator-strength` $f \approx 4.32\times10^{-9}
  \int\varepsilon\,\dd\tilde\nu$ (admitted constant, used); `thm:…:spin-rule`
  ΔS = 0 (proof: μ does not act on spin, spin functions orthogonal);
  `thm:…:laporte` g↔u only in a centrosymmetric molecule (proof via ch5);
  `thm:…:franck-condon` intensity ∝ |⟨χ_v'|χ_v''⟩|² (proof under BO and the
  Condon approximation); `prop:…:displaced` Poisson progression for
  displaced equal oscillators (`\admitted`, checked in figdata);
  `prop:…:kasha` (statement, established experimentally);
  `prop:…:quantum-yield` $\Phi_F = k_r/(k_r + k_{nr}) = k_r\tau$ (proof from
  first-order kinetics); `thm:…:stern-volmer` $I_0/I = \tau_0/\tau = 1 +
  k_q\tau_0[Q]$ (proof).
- **Methods.** `met:…:assign-band` (n→π* versus π→π* from ε, solvent shift,
  vibronic structure); `met:…:relative-yield` (relative quantum yield with a
  standard, refractive-index correction); `met:…:stern-volmer` (plotting
  and reading quenching data).
- **Boxes.** `history` Stokes 1852 names fluorescence after fluorite;
  `inthelab` time-correlated single-photon counting; `safety` UV lamps
  (eye protection; no GHS pictogram: a remark, not a `safety` box, if no
  substance is involved).
- **Figures.** S Jablonski diagram (S₀, S₁, S₂, T₁ with vibrational
  sublevels; straight radiative and wavy non-radiative arrows — style need);
  F `franck-condon` (two displaced Morse/harmonic curves, a vertical arrow,
  and the computed progression of Franck–Condon factors as a stick spectrum
  for S = 0.5, 1, 2; test: Σ = 1, maximum near S); F `photophysics`
  (absorption and emission bands of a model molecule: mirror image, Stokes
  shift; part b: fluorescence decays with and without quencher on a log
  scale, and the Stern–Volmer line; test: slope k_qτ₀, lifetimes); S a
  potential-energy diagram showing intersystem crossing between S₁ and T₁
  curves; AI tonic water glowing under a UV lamp in a dim room (everyday);
  P fluorite fluorescing under UV light (Commons — verify).
- **Ledger.** Iodine B and X state constants (`diat:I2.*`, WebBook) for the
  Franck–Condon example; quinine sulfate fluorescence quantum yield and
  lifetime (PhotochemCAD / open IUPAC data, **at risk** — else the hook stays
  qualitative and the problem uses data of the problem); anthracene
  absorption/emission maxima (PhotochemCAD, **at risk**); viscosity of water
  (IAPWS, `visc:H2O.25C`, shared with ch12).
- **Exercises palette.** Allowed or forbidden (spin, Laporte) for listed
  transitions; f from a Gaussian band (ε_max, width); FC: which vibronic band
  is strongest for a large/small displacement; Jablonski rates → Φ_F, Φ_ISC;
  τ_r from τ and Φ_F; Stern–Volmer from intensities; k_q compared with the
  diffusion limit (forward pointer inside the book to ch12); Stokes shift in
  cm⁻¹ and eV; relative quantum yield computation; static versus dynamic
  quenching from τ data; phosphorescence lifetime orders of magnitude.
- **Weekend problem — "Why tonic water glows".** I absorption of quinine at
  the lamp's wavelength (Beer–Lambert with problem data); II the Jablonski
  diagram of quinine and its yields (problem data for τ, Φ); III quenching
  by chloride ions (a Stern–Volmer series given as measured data); IV is the
  quenching diffusion-controlled? (k_q against $8RT/3\eta$ with the IAPWS
  viscosity). **Named number: the ratio k_q / k_d for chloride quenching of
  quinine** (computed from the problem's data and the ledger viscosity).
  24 questions.

## Ch. 8 — NMR in Depth: Pulses, Relaxation and 2D — `advanced-nmr`

- **Hook.** A hospital MRI scanner and a chemistry NMR spectrometer are the
  same physics: protons precessing in a strong field, tipped by a radio
  pulse, and relaxing at rates that depend on their surroundings.
- **Recall.** Year 1 volume: chemical shift, shielding, equivalent protons,
  integration, coupling constant, multiplets; Year 2 volume: ¹³C NMR,
  broadband decoupling, DEPT (whose sequence was admitted there);
  \cref{ch:b3:many-electron-atoms} (spin angular momentum); the Boltzmann
  factor from physics (populations; developed in \cref{ch:b3:partition-functions}).
- **Sections.** 1 Nuclear spins in a field (I, γ; Zeeman levels; Larmor
  frequency; populations and sensitivity ∝ γ³B₀²; the common nuclei).
  2 Pulses and the FID (net magnetisation; rotating frame; B₁ pulses and
  flip angles; the FID and its Fourier transform; signal averaging; how
  DEPT edits by polarisation transfer, in outline). 3 Relaxation (T₁,
  inversion recovery, choosing the recycle delay; T₂, linewidth, spin echo;
  the nuclear Overhauser effect). 4 Two-dimensional NMR (the 2D principle;
  COSY, HSQC, HMBC, NOESY; a strategy for solving a structure).
  5 Other nuclei and dynamics (¹⁹F, ³¹P; chemical exchange and coalescence;
  the MRI image and contrast in outline).
- **Definitions.** `def:b3:advanced-nmr:nuclear-spin` (nuclear spin quantum
  number, gyromagnetic ratio); `:larmor` (Larmor frequency); `:magnetisation`
  (net magnetisation, rotating frame); `:pulse` (radiofrequency pulse, flip
  angle); `:fid` (free induction decay); `:relaxation` (longitudinal
  relaxation time, transverse relaxation time); `:echo` (spin echo);
  `:noe` (nuclear Overhauser effect); `:two-d` (two-dimensional spectrum,
  cross peak, diagonal peak); `:cosy` (COSY), `:hsqc` (HSQC), `:hmbc`
  (HMBC), `:noesy` (NOESY); `:coalescence` (coalescence temperature).
- **Ownership check.** Map: Y3 owns pulse NMR and 2D; Y2 owns ¹³C NMR, DEPT;
  Book 3 owns *broadband decoupling*, *equivalent carbons*, *DEPT*: recalled,
  not redefined (DEPT's pulse logic is explained in a remark). Book 2 owns
  *chemical shift*, *shielding*, *coupling constant*, *multiplet*,
  *integration*: recalled. "Relaxation time" appears only in the two
  phrases above (ch13 owns *chemical relaxation time*).
- **Statements.** `prop:…:zeeman` $E_m = -m\gamma\hbar B_0$, $\nu_0 =
  \gamma B_0/2\pi$ (proof); `prop:…:populations` $\Delta N/N \approx
  \gamma\hbar B_0/2kT$ (proof, Boltzmann); `prop:…:precession` dM/dt = γM×B
  (`\admitted` from physics; solved: precession at ω₀); `prop:…:flip-angle`
  θ = γB₁t_p (proof in the rotating frame); `thm:…:lorentzian` the Fourier
  transform of a decaying cosine is a Lorentzian of FWHM 1/(πT₂) (proof by
  integration); `prop:…:inversion-recovery` $M_z(t) = M_0(1 - 2\eu^{-t/T_1})$,
  null at $T_1\ln 2$ (proof from the Bloch equation); `prop:…:averaging`
  S/N ∝ √N (proof from independent noise, Year 2 statistics recalled);
  `prop:…:noe-distance` NOE ∝ r⁻⁶ (`\admitted`); `prop:…:coalescence`
  $k_c = \pi\Delta\nu/\sqrt2$ (`\admitted`).
- **Methods.** `met:…:t1` (measuring T₁ and setting a quantitative recycle
  delay ≥ 5T₁); `met:…:solve-2d` (¹H → HSQC → COSY → HMBC → NOESY).
- **Boxes.** `history` Bloch and Purcell 1946, Ernst's Fourier and 2D NMR;
  `inthelab` shimming, locking and tuning a probe; `safety` strong magnetic
  fields (no GHS pictogram: a remark).
- **Figures.** S rotating-frame vectors before and after a 90° and a 180°
  pulse (tikz-3dplot); S pulse-sequence diagrams (90°–acquire, inversion
  recovery, spin echo, COSY 90°–t₁–90°–t₂); F `nmr-fid` (a two-line FID and
  its spectrum; test: lines at the offsets, FWHM = 1/πT₂); F `nmr-relaxation`
  (inversion-recovery curve and T₂ decay; test: null at T₁ ln 2); F `nmr-2d`
  (COSY and HSQC maps of the problem's ester built at ledger shifts; test:
  COSY cross peaks only between ³J-coupled pairs, HSQC peaks at bonded
  H/C pairs); P a high-field NMR magnet (Commons — verify); AI an MRI
  scanner room (hospital scene).
- **Ledger.** `nuc:` spin and γ (or μ) of ¹H (CODATA γ_p shared), ¹³C, ¹⁵N,
  ¹⁹F, ³¹P (IAEA-NUC); natural abundances (Book 3 `iso:` rows read-only, or
  CIAAW); ¹H and ¹³C shifts of the problem's ester (isopentyl ethanoate or
  ethyl butanoate: Book 2 `nmr:` ¹H rows read-only, ¹³C from NMRShiftDB/SDBS
  or Book 3 `c13:` rows); a water T₁ value (**at risk**; else data of the
  exercise).
- **Exercises palette.** Larmor frequencies at 9.4 and 14.1 T; population
  excess at 300 K; relative sensitivity ¹³C/¹H at natural abundance; 90°
  pulse length from B₁; linewidth → T₂; inversion-recovery null → T₁;
  reading a COSY; assigning an HSQC; NOE distances; coalescence rate and
  ΔG‡ (Eyring, forward in this book to ch12, or given formula).
- **Weekend problem — "An ester from a banana, solved in two dimensions".**
  I 1D ¹H and ¹³C/DEPT data (recall); II COSY connectivity of the two spin
  systems; III HSQC and HMBC across the ester oxygen; IV quantitative ¹³C:
  T₁ of the slowest carbon and the recycle delay. **Named number: the
  minimum recycle delay for a quantitative ¹³C spectrum, 5 T₁ of the
  carbonyl carbon (problem data)**. 24 questions.

## Ch. 9 — Crystallography and X-ray Diffraction — `x-ray-diffraction`

- **Hook.** In 1913 W. L. Bragg read the structure of rock salt from spots
  on a photographic plate: no "NaCl molecule" exists, only a lattice.
  Every structure in this book was found the same way.
- **Recall.** Year 1 volume: lattice, node, motif, unit cell, lattice
  parameters, multiplicity, FCC, BCC, structure types, compactness, density
  from the cell; \cref{ch:b3:point-groups} (symmetry operations).
- **Sections.** 1 Crystal systems and Bravais lattices (lattice symmetry; the
  crystallographic restriction; centring P, I, F, C, R; the 7 systems and 14
  lattices). 2 Lattice planes and the reciprocal lattice (Miller indices;
  interplanar spacings; reciprocal vectors; d = 1/|G|). 3 Diffraction
  (Bragg's law; the Laue condition; the Ewald sphere). 4 Intensities and
  symmetry (structure factor; atomic scattering factors; systematic
  absences of I and F lattices; NaCl versus KCl; screw axes and glide planes
  and their absences; space groups, the symbol P2₁/c, Wyckoff positions,
  asymmetric unit). 5 Powder and single-crystal methods (powder patterns;
  indexing a cubic pattern; Scherrer size; single crystal: the phase problem,
  solution and refinement in outline, R factor; CIF files and open
  databases).
- **Definitions.** `def:b3:x-ray-diffraction:crystal-system` (crystal
  system, Bravais lattice, lattice centring); `:miller` (lattice plane,
  Miller indices, interplanar spacing); `:reciprocal` (reciprocal lattice);
  `:ewald` (Ewald sphere); `:structure-factor` (atomic scattering factor,
  structure factor); `:absence` (systematic absence); `:space-group` (screw
  axis, glide plane, space group, asymmetric unit, Wyckoff position);
  `:powder` (powder diffraction pattern); `:refinement` (phase problem,
  R factor). Named statement: `thm:…:bragg` (Bragg's law).
- **Ownership check.** Map: Y3 owns space groups, diffraction, Bragg's law,
  reciprocal lattice. Book 2 owns *lattice*, *node*, *motif*, *unit cell*,
  *lattice parameters*, *multiplicity*, *coordination number*, *compactness*,
  structure-type names: recalled. Book 3: none.
- **Statements.** `thm:…:restriction` only 1-, 2-, 3-, 4-, 6-fold axes in a
  lattice (proof: the trace 1 + 2cos θ is an integer); `prop:…:spacing`
  cubic and orthorhombic $d_{hkl}$ (proof); `thm:…:bragg` $2d\sin\theta =
  n\lambda$ (proof); `prop:…:laue` Laue condition ⇔ Bragg (proof with the
  reciprocal lattice); `prop:…:structure-factor` $F_{hkl} = \sum_j f_j
  \eu^{2\pi\iu(hx_j+ky_j+lz_j)}$ and I ∝ |F|² (partial proof: path
  differences; kinematic approximation admitted); `prop:…:absences-I`,
  `prop:…:absences-F` (proofs); `prop:…:screw-absence` 2₁ along b: 0k0 with
  k odd absent (proof); `prop:…:friedel` |F_hkl| = |F₋h₋k₋l| (proof);
  `prop:…:scherrer` $L = K\lambda/(\beta\cos\theta)$ (`\admitted`).
- **Methods.** `met:…:index-cubic` (indexing a cubic powder pattern from
  sin²θ ratios); `met:…:z-from-density` (Z from cell and density); `met:…:
  read-space-group` (reading P2₁/c and its general positions).
- **Boxes.** `history` von Laue 1912, the Braggs 1913; `inthelab` a powder
  diffractometer; `safety` X-ray radiation (a remark).
- **Figures.** S Bragg construction (two planes, incident/diffracted rays,
  path difference); S 2D reciprocal lattice with a set of planes, G and the
  Ewald circle; S the 14 Bravais lattices (small tikz-3dplot cells, one
  table-figure, `omcubeo` views); F `xrd-powder` (computed patterns of NaCl
  and KCl with Cu Kα (f ≈ Z stated); part b: Cu (F) and W (I) with their
  absences; part c: Scherrer broadening for 10/50/200 nm; test: 2θ from
  Bragg and the ledger lattice parameters, allowed hkl sets, KCl odd
  reflections ≈ 0 with f(K⁺) = f(Cl⁻)); S crystallographic projection of
  P2₁/c (general positions with ±, commas, the 2₁, glide and inversion
  symbols — style need); P W. L. Bragg (Commons, PD — verify); AI a powder
  diffractometer in a lab (lab scene).
- **Ledger.** `xray:CuKa1`, `xray:CuKa2` (NIST-XRAY); `lat:NaCl`, `lat:Cu`,
  `lat:W`, `lat:Si` (Book 2, read-only); `lat:KCl`, `lat:KBr`, `lat:TiO2.a`,
  `.c` (COD, new); one molecular crystal's space group and cell (aspirin or
  benzoic acid, COD); densities read-only (Book 1 `rho:` rows).
- **Exercises palette.** d-spacings of cubic planes; Bragg angles of Cu (111)
  and (200); index a BCC pattern (Cr); Z of KCl from density; reciprocal
  lattice of a 2D rectangular lattice; why no fivefold axis (and a remark on
  quasicrystals); Scherrer size of a nanopowder; structure factor of CsCl
  (sum/difference); absences of a C-centred lattice; reading P2₁2₁2₁ (chiral
  molecules crystallise in Sohncke groups — remark).
- **Weekend problem — "Which white powder?"** I a computed powder pattern
  (from figdata) of an unknown cubic salt: d-spacings; II indexing → F
  lattice; III lattice parameter, density from the cell, identity among
  NaCl, KCl, KBr; the very weak odd lines; IV crystallite size from a line
  width. **Named number: the lattice parameter a refined from the
  high-angle (420) line, compared with the ledger value** (computed).
  24 questions.

## Ch. 10 — Statistical Thermodynamics: Partition Functions — `partition-functions`

- **Hook.** Ludwig Boltzmann's tomb in Vienna carries one line, $S = k\log W$:
  entropy counts the ways molecules can share energy. This chapter turns
  spectroscopic constants into standard entropies that agree with
  calorimetry to a few tenths of a joule.
- **Recall.** Year 2 volume: Gibbs energy, standard molar entropy, chemical
  potential, the second law (from physics); \cref{ch:b3:quantum-model-systems}
  (box, oscillator, rotor levels); \cref{ch:b3:rovibrational-spectroscopy}
  (B, ω_e, symmetry of homonuclear molecules).
- **Sections.** 1 Microstates and the Boltzmann distribution (N particles,
  levels, statistical weight; Stirling; maximising ln W with Lagrange
  multipliers; β = 1/kT identified). 2 The molecular partition function
  (meaning; populations; factorisation for independent modes). 3 The four
  contributions (translational $V/\Lambda^3$; rotational $kT/\sigma hcB$ and
  the symmetry number; vibrational, exact geometric sum; electronic, from
  degeneracies and low-lying levels). 4 From partition functions to
  thermodynamics (U, the canonical partition function Q = qᴺ/N!, S, A, p,
  G; $S = k\ln W$; the Sackur–Tetrode equation; statistical versus
  calorimetric standard entropies).
- **Definitions.** `def:b3:partition-functions:microstate` (microstate,
  statistical weight); `:boltzmann` (Boltzmann distribution, population);
  `:partition-function` (molecular partition function); `:canonical`
  (canonical partition function); `:thermal-wavelength` (thermal
  wavelength); `:symmetry-number` (symmetry number);
  `:characteristic-temperature` (characteristic rotational temperature,
  characteristic vibrational temperature); `:statistical-entropy`
  (statistical entropy). Named statement: `thm:…:sackur-tetrode`
  (Sackur–Tetrode equation).
- **Ownership check.** Map/seed: Y3 owns *partition function*, *Boltzmann
  distribution*. Book 3 owns *standard molar entropy*, *Gibbs energy*,
  *chemical potential*: recalled and computed, not redefined. Book 2 owns
  *configuration* (stereo) and *electron configuration*: the word
  "configuration" is avoided for distributions ("distribution of the
  molecules over the levels").
- **Statements.** `thm:…:boltzmann` $n_i/N = g_i\eu^{-\varepsilon_i/kT}/q$
  (proof: Stirling + Lagrange; β identified by comparison with the ideal gas,
  partial); `prop:…:factorisation` (proof); `prop:…:q-trans` (proof: sum →
  integral); `prop:…:q-rot` high-temperature limit and σ (proof of the
  integral; σ justified in ch11); `prop:…:q-vib` (proof); `prop:…:q-elec`
  (definition-based); `thm:…:internal-energy` $U - U(0) = NkT^2\,\partial\ln
  q/\partial T$ (proof); `prop:…:canonical` $Q = q^N/N!$ for an ideal gas
  (partial proof: indistinguishability); `thm:…:entropy` $S = k\ln Q + (U -
  U(0))/T$ and $S = k\ln W$ (partial proof); `thm:…:sackur-tetrode` (proof);
  `prop:…:modes-entropy` rotational and vibrational molar entropies (proof).
- **Methods.** `met:…:populations` (populations of levels from spectroscopic
  constants); `met:…:standard-entropy` (S° of a gas from its constants).
- **Boxes.** `history` Boltzmann 1877 and the tomb; `inthelab` third-law
  (calorimetric) entropies: heating from near 0 K, adding transition
  entropies.
- **Figures.** F `boltzmann-populations` (rotational populations of HCl and
  N₂ at 100, 300 and 1000 K as bars; vibrational populations of I₂ and N₂;
  test: Σ = 1, J_max, ratio formula); F `partition-functions` (q_rot exact
  sum versus $T/\sigma\theta_r$; q_vib versus T for N₂, Cl₂, I₂; test:
  limits); F `sackur-tetrode` (statistical S° of Ar, N₂, Cl₂, HCl, CO
  against the ledger values, printed as a table; test: agreement within
  0.5 J K⁻¹ mol⁻¹, CO's residual excluded in ch11); S a "Boltzmann
  staircase" (levels with population bars at two temperatures); P
  Boltzmann's tomb (Commons — verify licence).
- **Ledger.** S°(298.15 K) of Ar, N₂, Cl₂, HCl, CO (Book 3 `s0:` rows from
  CODATA-KEY if present, read-only; else new rows); B, ω_e of N₂, Cl₂, HCl,
  CO, I₂ (`diat:`); O₂ ground-state degeneracy and NO ²Π splitting
  (WebBook); Cl ²P₃/₂–²P₁/₂ splitting (`lev:Cl`, NIST ASD); masses (`aw:`).
- **Exercises palette.** Weights of distributions of 4 quanta over 4
  oscillators; population ratio of two levels; q_trans of Ar in 1 dm³;
  θ_rot and q_rot of N₂ and HCl; q_vib of I₂ and N₂ at 298 K; q_elec of NO
  and Cl; U of a monatomic gas; S° of Ar (Sackur–Tetrode); rotational S of
  HCl; the most populated J; when is the high-temperature limit good.
- **Weekend problem — "Counting the entropy of nitrogen".** I translational
  entropy of N₂ at 298.15 K, 1 bar (Sackur–Tetrode); II rotational entropy
  (σ = 2); III vibrational and electronic contributions; IV comparison with
  the calorimetric value and the third law. **Named number: S°(N₂, 298.15 K)
  computed from spectroscopic constants, ≈ 191.6 J K⁻¹ mol⁻¹** (figdata,
  tested against the ledger). 24 questions.

## Ch. 11 — Statistical Thermodynamics Applied — `statistical-thermo-applied`

- **Hook.** Liquid hydrogen stored in a tank slowly boils away even in a
  perfect thermos: its molecules exist as two nuclear-spin isomers, and the
  slow conversion of one into the other releases heat.
- **Recall.** \cref{ch:b3:partition-functions}; Year 2 volume: $K^\circ$
  from $\Delta_r G^\circ$, the van 't Hoff equation, heat capacities and
  standard entropies; \cref{ch:b3:many-electron-atoms} (antisymmetry).
- **Sections.** 1 Heat capacities of gases (equipartition from the
  classical limit; the vibrational Einstein function; freezing out of
  modes; N₂, Cl₂, CO₂ against JANAF). 2 Nuclear-spin statistics (exchange
  symmetry of the total wavefunction; ortho and para hydrogen, weights 3:1;
  equilibrium ratio versus T; heat capacity of normal and equilibrium H₂;
  the symmetry number justified; residual entropy of CO and of ice).
  3 Equilibrium constants from partition functions ($K$ from standard
  molar partition functions and $\Delta E_0$; I₂ ⇌ 2I against JANAF;
  H₂ + D₂ ⇌ 2HD → 4; the van 't Hoff equation recovered). 4 Isotope
  effects (equilibrium isotope effects from zero-point energies; isotopic
  fractionation; δ notation; the oxygen-isotope thermometer, qualitatively).
- **Definitions.** `def:b3:statistical-thermo-applied:spin-isomers` (ortho
  hydrogen, para hydrogen); `:residual-entropy` (residual entropy);
  `:isotope-effect` (equilibrium isotope effect, fractionation factor,
  δ value). Named statement: `thm:…:equipartition` (equipartition theorem —
  index the name, owner chapter, S2 point 2).
- **Ownership check.** Book 3 owns *van 't Hoff equation*, *Le Chatelier's
  principle*: recalled and re-derived, not re-indexed. Book 1 owns
  *isotope* (g9): recalled. Book 3 owns `iso:` data. *Isotopologue* is ch6's.
  Heat capacity is physics' and Book 3's working quantity: used, never
  defined.
- **Statements.** `thm:…:equipartition` ½kT per quadratic term (proof from
  the classical limit of q); `prop:…:cv-vib` Einstein function (proof);
  `thm:…:spin-statistics` weights (2I+1)(I+1) : (2I+1)I for odd:even J
  (H₂, fermions; D₂, bosons; `\admitted` symmetry postulate, consequences
  proved); `prop:…:ortho-para` equilibrium para fraction (proof);
  `prop:…:residual` $S_0 = k\ln W_0$; CO: R ln 2; ice: R ln(3/2) (proof,
  Pauling count); `thm:…:k-from-q` $K = \prod(q_J^\circ/N_A)^{\nu_J}
  \eu^{-\Delta_r E_0/RT}$ (proof from $\mu_J$); `prop:…:hd` K → 4 at high T
  (proof with σ); `prop:…:vant-hoff-stat` (proof that the statistical K
  obeys van 't Hoff); `prop:…:zpe-isotope` EIE from ZPE differences (proof).
- **Methods.** `met:…:cv` (heat capacity of a gas from its modes);
  `met:…:k-stat` (computing K from spectroscopic data).
- **Boxes.** `history` Bonhoeffer and Harteck isolate para-hydrogen (1929);
  `inthelab` an ortho–para converter (iron oxide catalyst) in a hydrogen
  liquefier; `safety` hydrogen (`\ghs{GHS02}\ghs{GHS04}`, PubChem).
- **Figures.** F `heat-capacity` (C_V,m/R of N₂, Cl₂ and H₂ (normal and
  equilibrium) versus T; test: limits 3/2, 5/2, 7/2 and the H₂ rotational
  anomaly); F `ortho-para` (equilibrium para fraction of H₂ and ortho
  fraction of D₂ versus T; test: 25 % para at high T, → 100 % at 0 K); F
  `equilibrium-constant-stat` (log K of I₂ ⇌ 2I versus 1/T, statistical line
  and JANAF points; H₂ + D₂ ⇌ 2HD; test: agreement with JANAF within 0.05 in
  log K, K → 4); S ice proton disorder (2D hydrogen-bond network obeying the
  ice rules, with the Pauling count); AI a liquid-hydrogen storage tank at
  an industrial site.
- **Ledger.** `diat:H2.*`, `diat:D2.*`, `diat:HD.*`, `diat:I2.*` (WebBook;
  D₀(I₂)); `lev:I` (²P₁/₂ at 7603 cm⁻¹, NIST ASD); JANAF log Kf of I(g) and
  C_p of N₂, Cl₂ (JANAF); latent heat of vaporisation of H₂ (WebBook phase
  data) for the problem; CO calorimetric entropy (**at risk**: Clayton &
  Giauque 1932 not open; else only the computed R ln 2 with "close to the
  measured gap" EXCLUDED); ice residual entropy measured (**at risk**, same
  treatment); GHS of H₂ (PubChem).
- **Exercises palette.** C_V of CO₂ (3N − 5 modes) at high T; Einstein
  function at T = θ_v; para fraction at 77 K and 20 K; D₂ ortho/para 2:1;
  K for H₂ + D₂ at 300 K; residual entropy of N₂O and of a crystal of
  CH₃D; EIE for H/D exchange between two molecules; δ¹⁸O shifts; C_p of Cl₂
  at 298 K versus JANAF; vibrational contribution to S° of I₂.
- **Weekend problem — "Storing liquid hydrogen".** I ortho/para weights,
  the 3:1 ratio at room temperature and the equilibrium at 20 K; II the
  heat released by ortho → para conversion per kilogram (J = 1 → 0); III
  comparison with the latent heat of vaporisation: boil-off; first-order
  uncatalysed conversion (problem k) and the tank's loss after a week;
  IV the catalyst and the heat capacity of normal versus equilibrium
  hydrogen. **Named number: the ratio (conversion heat)/(latent heat) for
  normal hydrogen, about 1.2: conversion alone could evaporate the whole
  tank** (computed). 25 questions.

## Ch. 12 — Theories of Reaction Rates — `rate-theories`

- **Hook.** Swapping the hydrogens of a drug's two methoxy groups for
  deuterium slows its metabolism enough to change the dose: the first
  deuterated medicine was approved in 2017. Why does a heavier isotope react
  more slowly, and by how much?
- **Recall.** Year 1 volume: rate constant, Arrhenius law, activation
  energy, pre-exponential factor, elementary step, transition state, energy
  profile, reaction coordinate, Hammond postulate; Year 2 volume: ionic
  strength, activity coefficient, Debye–Hückel limiting law, least-squares
  line, residual; \cref{ch:b3:computational-chemistry} (PES),
  \cref{ch:b3:partition-functions}, \cref{ch:b3:statistical-thermo-applied}
  (K from q, ZPE); from physics: Maxwell–Boltzmann speeds, Fick's law.
- **Sections.** 1 Collision theory (collision frequency; cross-section;
  energy threshold; k(T); the steric factor; comparison with measured A
  factors). 2 Potential energy surfaces (the collinear H + H₂ surface; the
  saddle point; the minimum energy path; early and late barriers, Polanyi's
  rules). 3 Transition-state theory (activated complex in quasi-equilibrium;
  the reaction-coordinate mode; the Eyring equation from partition
  functions; activation enthalpy, entropy and Gibbs energy; the Eyring plot
  with parameter uncertainties; $E_a = \Delta H^\ddagger + RT$ (solution),
  interpretation of ΔS‡). 4 Kinetic isotope effects (primary from zero-point
  energies; secondary; tunnelling and anomalously large KIEs). 5 Reactions in
  solution (diffusion control, Smoluchowski; cage effect; activation
  control; the kinetic salt effect).
- **Definitions.** `def:b3:rate-theories:collision` (collision
  cross-section, steric factor); `:saddle` (saddle point, minimum energy
  path); `:activated-complex` (activated complex); `:tst`
  (transition-state theory, transmission coefficient); `:activation`
  (Gibbs energy of activation, enthalpy of activation, entropy of
  activation); `:kie` (kinetic isotope effect, primary kinetic isotope
  effect, secondary kinetic isotope effect); `:diffusion` (diffusion-
  controlled reaction, activation-controlled reaction, cage effect);
  `:salt` (kinetic salt effect). Named statement: `thm:…:eyring` (Eyring
  equation).
- **Ownership check.** Map/S1: Y3 owns *activated complex*, *transition-state
  theory*, *Eyring equation*; Book 2 owns *transition state*, *Hammond
  postulate*, *energy profile*, *reaction coordinate*, *activation energy*,
  *pre-exponential factor*: recalled. Book 3 owns *ionic strength*, *activity
  coefficient*, *least-squares line*, *residual*, *confidence interval*:
  recalled; the standard errors of fitted parameters are this book's
  (S2 point 3). *Potential energy surface* is ch3's (recalled).
- **Statements.** `thm:…:collision` $k = \sigma\bar v_{\text{rel}}N_A
  \eu^{-E_0/RT}$ (proof from the Maxwell–Boltzmann distribution, admitted
  from physics, and the line-of-centres threshold, partial); `thm:…:eyring`
  $k = \kappa\,(k_BT/h)\,K^{\ddagger}$ and its thermodynamic form (proof:
  partition functions, separation of the reaction-coordinate vibration);
  `prop:…:ea-dh` $E_a = \Delta H^\ddagger + RT$ in solution (proof);
  `prop:…:slope-uncertainty` standard errors of slope and intercept
  $s_b^2 = s^2/\sum(x_i - \bar x)^2$ (proof, independent errors);
  `prop:…:primary-kie` $k_H/k_D \approx \exp[hc(\tilde\nu_H - \tilde\nu_D)/
  2kT]$ (proof from ZPE lost in the TS); `prop:…:smoluchowski` $k_d =
  4\pi N_A(D_A + D_B)R^*$, and $k_d \approx 8RT/3\eta$ with Stokes–Einstein
  (partial proof: diffusion from physics); `prop:…:bronsted-bjerrum`
  $\log k = \log k_0 + 2Az_Az_B\sqrt I$ (proof from TST and Debye–Hückel).
- **Methods.** `met:…:eyring-plot` (ΔH‡, ΔS‡ with their standard errors by
  least squares); `met:…:kie` (measuring a KIE by competition);
  `met:…:mechanism-evidence` (what ΔS‡, KIE and salt effects say).
- **Boxes.** `history` Eyring, Evans and Polanyi, 1935; `inthelab` a
  temperature-jacketed UV cell for an Eyring study.
- **Figures.** F `pes-collinear` (LEPS model surface for H + H₂ as a contour
  map with the saddle and the minimum energy path — `contour prepared`; test:
  symmetric saddle, asymptote = the ledger Morse curve of H₂, barrier > 0);
  F `eyring` (two Eyring plots of problem data with fitted lines and
  confidence bands; test: regression recovers ΔH‡, ΔS‡); F `kie` (k_H/k_D
  versus T for C–H, N–H, O–H stretches; test: value from the formula, → 1 at
  high T); S energy profile with the ZPE levels of C–H and C–D in the
  reactant and the TS (why the primary KIE); S collision geometry
  (cross-section disk πd²); AI tablets of a medicine on a pharmacy shelf
  (everyday).
- **Ledger.** `diat:H2.*` (Morse parameters for the LEPS asymptotes; the
  Sato parameter is a model constant, stated as such); `kin:NO+O3.A`,
  `.EaR` (IUPAC-ATMOS) and NO/O₃ collision diameters (**at risk**, else
  EXCLUDED and the comparison made with a stated model cross-section);
  `vib:CH4.nu1`, `vib:CD4.nu1` or C–H/C–D stretches (NSRDS-NBS39);
  `visc:H2O.25C`, `visc:hexane.25C` (IAPWS / WebBook fluid data); H + H₂
  barrier height from an accurate surface (**at risk**: open paper, else
  EXCLUDED); deuterated-drug approval year (open review, PMC; drug named by
  its INN only).
- **Exercises palette.** Collision-theory k for NO + O₃ and its steric
  factor; ΔH‡ and ΔS‡ from two rate constants; Ea versus ΔH‡; sign of ΔS‡
  for associative and dissociative steps; maximum primary KIE for O–H/O–D at
  298 K; a KIE of 40 means tunnelling; diffusion limits in water and
  hexane; salt effect sign for ion pairs of each charge type; reading an
  early/late barrier on a PES; standard error of ΔH‡ from the slope's.
- **Weekend problem — "A heavier medicine".** I ZPE of C–H and C–D
  stretches from the ledger (reduced masses); II the maximum primary KIE at
  37 °C; III half-lives of the H and D drugs when the C–H cleavage is
  rate-determining (problem clearance data); IV an Eyring analysis of
  measured k(T) for both compounds (problem data) with standard errors: is
  ΔΔH‡ equal to the ZPE difference? **Named number: the predicted ratio of
  half-lives t½(D)/t½(H) at 37 °C** (computed). 25 questions.

## Ch. 13 — Complex Kinetics: Chains, Enzymes and Oscillations — `complex-kinetics`

- **Hook.** A beaker that turns colourless, amber, blue, colourless again,
  for minutes on end, or spirals that travel across a dish: the
  Belousov–Zhabotinsky reaction seemed to violate thermodynamics until its
  mechanism was written down.
- **Recall.** Year 1 volume: mechanism, elementary step, rate-determining
  step, pre-equilibrium and steady-state approximations, catalyst; Year 2
  volume: initiation, propagation, termination, radical initiator, kinetic
  chain length (polymers), least-squares line; Book 1 (grade 12): enzyme;
  \cref{ch:b3:rate-theories} (TST, diffusion limit).
- **Sections.** 1 Chain reactions (chain carriers; the H₂ + Br₂ rate law
  derived; inhibition by HBr; the chain length of a chain reaction).
  2 Branching chains and explosions (branching factor; the critical
  condition; H₂/O₂ explosion limits qualitatively; thermal versus chain
  explosions). 3 Unimolecular reactions (Lindemann–Hinshelwood; the fall-off
  curve; why "unimolecular" reactions need collisions). 4 Enzyme kinetics
  (Michaelis–Menten by the steady state; k_cat, K_M, k_cat/K_M; the diffusion
  ceiling; fitting: Lineweaver–Burk versus nonlinear least squares;
  competitive, uncompetitive and mixed inhibition). 5 Autocatalysis,
  oscillations and fast reactions (autocatalysis and the logistic law;
  Lotka–Volterra; the Brusselator and the stability of a steady state by
  the eigenvalues of its Jacobian; the BZ reaction; stopped flow,
  temperature jump and the relaxation time, flash photolysis).
- **Definitions.** `def:b3:complex-kinetics:chain` (chain reaction, chain
  carrier); `:branching` (chain branching, explosion limits); `:lindemann`
  (Lindemann mechanism, fall-off region); `:enzyme` (enzyme, active site,
  enzyme–substrate complex); `:michaelis` (Michaelis constant, maximum
  rate, catalytic constant, specificity constant); `:inhibition`
  (competitive inhibition, uncompetitive inhibition, mixed inhibition,
  inhibition constant); `:autocatalysis` (autocatalytic reaction);
  `:oscillating` (oscillating reaction, limit cycle); `:relaxation`
  (relaxation method, chemical relaxation time); `:fast` (stopped-flow
  method, flash photolysis). Named statement: `thm:…:michaelis-menten`
  (Michaelis–Menten equation).
- **Ownership check.** Seed/S2: Y3 owns *Michaelis–Menten*, *chain reaction*,
  *chain branching*, *explosion limits*; Book 3 owns *initiation*,
  *propagation*, *termination*, *radical initiator*, *kinetic chain length*:
  recalled (the H₂ + Br₂ steps are named with Book 3's words). *Enzyme*
  **re-founds** Book 1 (g12); Books 2–3 did not define it. Book 3 owns
  *turnover number/frequency* of a catalyst: k_cat is called the *catalytic
  constant* (a remark says biochemists call it the enzyme's turnover
  number). Book 2's *substrate* (SN chemistry) is not redefined; "the enzyme's
  substrate" is used plainly. Book 3's *residual*, *least-squares line*:
  recalled.
- **Statements.** `thm:…:hbr` $v = k[\ce{H2}][\ce{Br2}]^{1/2}/(1 +
  k'[\ce{HBr}]/[\ce{Br2}])$ (proof); `prop:…:branching` explosion when the
  branching rate exceeds termination (proof from the linear ODE);
  `thm:…:lindemann` $k_{\text{uni}} = k_1k_2[M]/(k_{-1}[M] + k_2)$ and its
  limits (proof); `thm:…:michaelis-menten` (proof, steady state; the
  rapid-equilibrium variant as a remark); `prop:…:lineweaver` (proof);
  `prop:…:inhibition-laws` the three apparent K_M and V_max (proofs);
  `prop:…:logistic` (proof); `thm:…:lotka-volterra` conserved quantity, closed
  orbits (proof); `prop:…:hopf` the Brusselator's steady state loses
  stability when B > 1 + A² (proof by the Jacobian's eigenvalues);
  `prop:…:relaxation-time` $1/\tau = k_1 + k_{-1}([A]_e + [B]_e)$ for
  A + B ⇌ C (proof by linearisation).
- **Methods.** `met:…:steady-state-chain` (rate law of a chain mechanism);
  `met:…:mm-fit` (K_M and V_max by nonlinear least squares, with the
  Lineweaver–Burk plot as a diagnostic only); `met:…:inhibition-type`;
  `met:…:stability` (linear stability of a steady state).
- **Boxes.** `history` Bodenstein's HBr (1906) and Belousov's rejected
  manuscript (1951); `inthelab` a stopped-flow apparatus; `safety`
  bromine (`\ghs{GHS05}\ghs{GHS06}\ghs{GHS09}`, PubChem).
- **Figures.** F `chain-kinetics` (numerical integration of the H₂ + Br₂
  mechanism against the steady-state law; test: agreement after the
  induction period); F `lindemann` (fall-off curve log k versus log[M];
  test: limits k∞ and k₀[M]); F `michaelis-menten` (v versus [S] with no,
  competitive and uncompetitive inhibitor; Lineweaver–Burk lines; test:
  v(K_M) = V_max/2, the competitive lines meet on the 1/v axis); F
  `oscillations` (Brusselator time series and limit cycle; Lotka–Volterra
  orbits; test: Hopf boundary, conserved quantity, period); F
  `chemical-relaxation` (T-jump signal and its exponential; test: τ formula);
  S chain cycle diagram (propagation loop with the carriers); S stopped-flow
  apparatus (syringes, mixer, observation cell, stop syringe); P BZ
  reaction spirals (Commons — verify).
- **Ledger.** Mostly data of the problems. Sourced facts: k_cat/K_M of a
  near-perfect enzyme (carbonic anhydrase or triosephosphate isomerase,
  PMC review, **at risk**); the water-neutralisation rate constant (Eigen;
  **at risk**, else EXCLUDED); GHS of Br₂ (PubChem).
- **Exercises palette.** Rate law of a given chain mechanism; inhibition by
  product; branching criterion; Lindemann half-pressure; K_M and V_max from
  initial rates; inhibitor type from Lineweaver–Burk lines; K_i from apparent
  K_M; specificity constant against the diffusion limit; logistic
  half-time; stability of a steady state from a 2×2 Jacobian; T-jump
  relaxation time.
- **Weekend problem — "An enzyme, an inhibitor and a dose".** I initial
  rates (problem data) → K_M, V_max by least squares with standard errors;
  II a competitive inhibitor: apparent K_M at three concentrations → K_i;
  III fraction of activity left at given [I] and [S]; IV pre-steady-state
  stopped-flow trace: a burst and k_cat. **Named number: the inhibitor
  concentration giving 90 % inhibition at [S] = K_M, 18 K_i** (derived, then
  computed with the fitted K_i). 24 questions.

## Ch. 14 — Photochemistry — `photochemistry`

- **Hook.** Vision begins when one photon bends one molecule: retinal turns
  from 11-cis to all-trans in less than a picosecond. The same rules —
  one photon, one excited molecule, then competition between fates — govern
  sunscreens, smog and the ozone layer.
- **Recall.** \cref{ch:b3:electronic-spectroscopy} (Jablonski diagram,
  quantum yield, quencher, intersystem crossing, lifetimes); Year 1 volume:
  radical, homolysis, Z/E; Year 2 volume: concerted reaction, HOMO/LUMO,
  catalytic cycle; \cref{ch:b3:complex-kinetics} (chains).
- **Sections.** 1 Light as a reagent (Grotthuss–Draper and Stark–Einstein;
  photon flux; absorbed rate $I_0(1 - 10^{-A})$; the quantum yield of a
  reaction; actinometry; Φ > 1 means a chain: H₂ + Cl₂). 2 Photochemical
  reactions (E/Z photoisomerisation and the photostationary state; retinal;
  photodissociation; [2+2] photocycloaddition, whose orbital reason is in
  \cref{ch:b3:pericyclic}; Norrish type I and II; photoreduction of
  benzophenone). 3 Photosensitisation (triplet–triplet energy transfer and
  the energy condition; singlet oxygen and photodynamic therapy; photoredox
  catalysis with a ruthenium complex in outline). 4 Photochemistry of the
  atmosphere (the Chapman mechanism and the ozone layer; catalytic ozone
  destruction by Cl/ClO and NO/NO₂; polar stratospheric clouds and the
  ozone hole; the troposphere: the NO₂/NO/O₃ photostationary state, OH as
  the atmosphere's oxidant, photochemical smog).
- **Definitions.** `def:b3:photochemistry:photon-flux` (photon flux,
  chemical actinometer); `:photoisomerisation` (photoisomerisation,
  photostationary state); `:photolysis` (photolysis, photolysis rate
  constant); `:norrish` (Norrish type I reaction, Norrish type II reaction);
  `:sensitisation` (photosensitiser, photosensitisation, triplet energy
  transfer, singlet oxygen); `:photoredox` (photoredox catalysis);
  `:chapman` (Chapman mechanism, ozone layer); `:ozone-depletion` (ozone
  depletion, reservoir species); `:smog` (photochemical smog). Named
  statement: `prop:…:stark-einstein` (Stark–Einstein law).
- **Ownership check.** Not in the map apart from the chapter. Book 3 owns
  *catalytic cycle*, *concerted reaction*: recalled ("ozone destruction is a
  catalytic cycle in the Year 2 volume's sense"). *Quantum yield* is ch7's
  (recalled). *Cycloaddition* is ch26's (forward \cref inside this book).
  Book 1's *greenhouse gas* is re-founded in ch32, not here.
- **Statements.** `prop:…:stark-einstein` (statement; primary quantum yields
  sum to 1, proof from ch7's kinetics); `prop:…:rate` $v = \Phi I_{abs}$
  with $I_{abs} = I_0(1 - 10^{-A})$ (proof); `prop:…:pss`
  $[Z]/[E] = \varepsilon_E\Phi_{E\to Z}/(\varepsilon_Z\Phi_{Z\to E})$ (proof);
  `prop:…:sensitisation-condition` triplet transfer is fast when
  $E_T(\text{donor}) > E_T(\text{acceptor})$ (argued, `\admitted`
  quantitatively); `thm:…:chapman` steady-state [O₃] (proof);
  `prop:…:catalytic-destruction` chain length of the ClOₓ cycle (proof);
  `prop:…:leighton` $[\ce{O3}] = j[\ce{NO2}]/(k[\ce{NO}])$ (proof).
- **Methods.** `met:…:actinometry` (ferrioxalate actinometry);
  `met:…:photochemical-rate` (rate of a photoreaction from lamp power,
  absorbance and Φ).
- **Boxes.** `history` Ciamician's "photochemistry of the future" (1912) and
  the ozone-hole discovery (1985); `inthelab` a photoreactor with a
  filtered mercury lamp; `safety` UV radiation (remark) and benzophenone
  (PubChem GHS).
- **Figures.** S S₀/S₁ potential curves of an alkene along the twist angle,
  with the funnel to the ground state; S Norrish II mechanism (chemfig,
  `\chemmove`) and a [2+2] photocycloaddition; F `photostationary` (E/Z
  composition versus time under irradiation at two wavelengths; test: the
  pss formula); F `ozone-chemistry` (Chapman steady state and the effect of
  a Cl chain; part b: daytime O₃ from the NO₂/NO ratio; test: steady states
  equal the ODE long-time limits, Leighton relation); S the Chapman and ClOₓ
  cycles as reaction-cycle diagrams (Book 3's cycle styles); P the Antarctic
  ozone hole (NASA, PD — verify); AI a city under photochemical smog seen
  from a hill (everyday).
- **Ledger.** Rate constants of O + O₂ + M, O + O₃, Cl + O₃, ClO + O, NO +
  O₃ (IUPAC-ATMOS, `kin:` rows); O₂ and O₃ dissociation thresholds from
  D₀ (WebBook / JANAF, computed); ferrioxalate quantum yield (**at risk**:
  IUPAC technical report not reachable; else the actinometer is described
  with "a calibrated quantum yield" and the number is data of the
  exercise); ozone column of ~300 Dobson units (NASA/WMO page, **check**);
  retinal isomerisation time (**at risk**, else "within a picosecond" only
  if a source supports it); GHS of benzophenone.
- **Exercises palette.** Photons per second from a 100 mW lamp at 365 nm;
  Φ of a reaction from moles converted; Φ = 10⁴ ⇒ chain; pss composition;
  Norrish II products of 2-hexanone; sensitiser choice from triplet energies
  (problem data); [O₃]/[O] steady state; Cl chain length; Leighton relation
  at noon; wavelength threshold for O₂ photolysis from D₀.
- **Weekend problem — "Making and unmaking the ozone layer".** I photon
  thresholds for O₂ and O₃ from the ledger dissociation energies; II the
  Chapman steady state with the IUPAC rate constants and given photolysis
  rates; III the Cl/ClO cycle: rate of ozone loss, chain length; IV the
  reservoirs (HCl, ClONO₂) and polar clouds. **Named number: the number of
  ozone molecules one chlorine atom destroys before it is captured in a
  reservoir** (computed from the problem's rates). 25 questions.

## Ch. 15 — Electrode Kinetics and Electroanalysis — `electrode-kinetics`

- **Hook.** A drop of blood on a strip, five seconds, a number: the glucose
  meter is an electrochemical cell whose current, not voltage, measures a
  concentration.
- **Recall.** Year 1 volume: electrode potential, standard potential,
  Nernst equation, reference electrode, half-cell; Year 2 volume:
  current–potential curves, anodic/cathodic current, working and counter
  electrodes, overpotential, fast and slow systems, diffusion layer,
  limiting current, activity coefficient, ionic strength, calibration
  curve, standard-addition method, limit of detection;
  \cref{ch:b3:rate-theories} (TST); from physics: Fick's laws, capacitors.
- **Sections.** 1 The electrode–solution interface (the double layer:
  Helmholtz, Gouy–Chapman, Stern; capacitance; charging current). 2 Electron
  transfer kinetics (Butler–Volmer from TST with a transfer coefficient;
  exchange current; charge-transfer resistance at small η; Tafel at large η;
  the slow-system curve of the Year 2 volume derived). 3 Mass transport
  (migration, diffusion, convection; supporting electrolyte; the Cottrell
  equation by solving Fick's second law; the rotating disk in outline;
  steady-state limiting current). 4 Cyclic voltammetry (the experiment; the
  reversible wave: E½, ΔE_p ≈ 57/n mV, i_p ∝ √v (Randles–Ševčík); quasi- and
  irreversible waves; diagnosing coupled chemical steps; ferrocene as an
  internal reference). 5 Electroanalytical methods (amperometry and
  biosensors; anodic stripping voltammetry; pulse methods; potentiometry with
  ion-selective electrodes, Nikolsky; coulometry; inverse prediction from a
  calibration with its uncertainty).
- **Definitions.** `def:b3:electrode-kinetics:double-layer` (electrical
  double layer, Helmholtz layer, diffuse layer, Debye length, double-layer
  capacitance);
  `:exchange` (exchange current density, transfer coefficient, standard
  rate constant); `:charge-transfer` (charge-transfer resistance, Tafel
  slope); `:transport` (migration, convection, supporting electrolyte);
  `:chronoamperometry` (chronoamperometry); `:cv` (cyclic voltammetry,
  voltammogram, peak potential, peak current); `:reversibility`
  (electrochemically reversible system, quasi-reversible system,
  electrochemically irreversible system); `:amperometry` (amperometry,
  biosensor); `:stripping` (anodic stripping voltammetry); `:ise`
  (ion-selective electrode, selectivity coefficient); `:coulometry`
  (coulometry). Named statements: `thm:…:butler-volmer` (Butler–Volmer
  equation), `cor:…:tafel` (Tafel equation), `thm:…:cottrell` (Cottrell
  equation), `prop:…:randles-sevcik` (Randles–Ševčík equation),
  `prop:…:nikolsky` (Nikolsky equation).
- **Ownership check.** Map/seed: Y3 owns Butler–Volmer, Tafel, cyclic
  voltammetry. Book 3 owns *i–E curve*, *overpotential*, *fast/slow system*,
  *working/counter electrode*, *diffusion layer*, *limiting current*,
  *electroactive species*, *calibration curve*, *standard-addition method*,
  *limit of detection*: recalled; the standard-addition procedure is a
  `met:` here, unindexed. *Electrochemically reversible/irreversible* are
  defined by the dimensionless rate parameter (Matsuda–Ayabe), a new and
  sharper notion than Book 3's phenomenological fast/slow (a remark links
  them). Book 2 owns *electrode potential*, *reference electrode*, *Nernst
  equation*; Book 3 owns *Faraday constant* (re-found).
- **Statements.** `thm:…:butler-volmer` (proof from TST with a linear split
  of the free-energy change); `cor:…:linear` $R_{ct} = RT/(nFi_0)$ (proof);
  `cor:…:tafel` (proof); `prop:…:debye-length` $\kappa^{-1} =
  \sqrt{\varepsilon RT/2F^2I}$ (proof: linearised Poisson–Boltzmann, a 1D
  ODE; Poisson's equation from physics); `prop:…:double-layer` capacitance
  of the Gouy–Chapman layer (`\admitted`, its low-potential limit
  ε/κ⁻¹ proved); `thm:…:cottrell` $i = nFAc\sqrt{D/\pi t}$ (proof: the erf
  profile verified to solve Fick's law and its conditions);
  `prop:…:randles-sevcik` $i_p = 0.4463\,nFAc\sqrt{nFvD/RT}$ (`\admitted`
  constant, the √v law proved by scaling; checked by the figdata
  simulation); `prop:…:delta-ep` (`\admitted`, checked numerically);
  `prop:…:nikolsky` (proof from the membrane potential with two ions,
  partial); `prop:…:inverse-prediction` uncertainty of a concentration read
  from a calibration line (proof, first order).
- **Methods.** `met:…:tafel-analysis`; `met:…:cv-diagnosis` (reversible,
  quasi-reversible, EC: from ΔE_p, i_pa/i_pc, i_p ∝ √v);
  `met:…:standard-addition` (with stripping, unindexed);
  `met:…:three-electrode` (setting up a measurement).
- **Boxes.** `history` Heyrovský's polarograph (1922); `inthelab` polishing a
  glassy-carbon electrode and degassing with argon; `safety` mercury-free
  electrodes; lead standard solutions (PubChem GHS).
- **Figures.** S double-layer model (Helmholtz plane, diffuse layer,
  potential profile); F `butler-volmer` (i versus η for α = 0.3, 0.5, 0.7
  and the Tafel plot; test: slope RT/(αnF) ln 10, low-η slope 1/R_ct); F
  `cottrell` (concentration profiles at four times; i versus t^{-1/2}; test:
  erf profile, slope); F `cyclic-voltammetry` (simulated CVs by finite
  differences at four scan rates, inset i_p versus √v, and a quasi-reversible
  wave; test: ΔE_p within 57–60 mV for n = 1, i_p ∝ √v within 1 %, E½ =
  E°′); S a three-electrode cell with potentiostat (style pics `electrode`,
  `probe`, circuitikz); F `standard-addition` (stripping peaks of a sample
  with three additions and the extrapolated line; test: x-intercept = −c₀);
  AI a person using a blood-glucose meter (no digits on the display).
- **Ledger.** Mostly data of the problems. Sourced: Pb guideline value in
  drinking water (Book 3 `who:` row read-only); ferrocene diffusion
  coefficient or ferricyanide D (**at risk**; else problem data); glucose
  oxidase reaction stoichiometry (no number); GHS of Pb(NO₃)₂, K₃[Fe(CN)₆]
  (PubChem).
- **Exercises palette.** i₀ and α from a Tafel plot; R_ct; Tafel slope for
  α = 0.5; Cottrell: D from i√t; Randles–Ševčík i_p for given data;
  diagnosis of three CVs; ISE error from an interferent; coulometric
  determination of a mass; stripping with standard additions; charging
  current versus scan rate; uncertainty of an inverse prediction.
- **Weekend problem — "The glucose strip".** I the enzyme, the mediator and
  the electrode reaction (balanced); II chronoamperometry: Cottrell slope →
  D of the mediator (problem data); III the calibration line, its standard
  errors, the concentration of a blood sample and its uncertainty; IV
  interferents (ascorbate) and how a CV at the strip shows them. **Named
  number: the sample's glucose concentration in mmol L⁻¹ with its standard
  uncertainty** (computed). 25 questions.

## Ch. 16 — Surfaces, Adsorption and Heterogeneous Catalysis — `surfaces-catalysis`

- **Hook.** Under a car, a ceramic honeycomb thinly coated with a few grams
  of platinum, palladium and rhodium removes most of the CO, unburnt fuel and
  NOₓ from the exhaust, on its surface only.
- **Recall.** Year 1 volume: catalyst, homogeneous and heterogeneous
  catalysis, FCC packing; Year 2 volume: conversion, selectivity,
  turnover frequency, Le Chatelier; \cref{ch:b3:x-ray-diffraction} (Miller
  indices), \cref{ch:b3:rate-theories} (Eyring),
  \cref{ch:b3:partition-functions}.
- **Sections.** 1 Adsorption (physisorption and chemisorption; dissociative
  chemisorption; the (111) and (100) faces and their sites; coverage).
  2 Isotherms (Langmuir, derived kinetically and statistically; dissociative
  and competitive Langmuir; the isosteric enthalpy; BET and the specific
  surface area). 3 Kinetics of surface reactions (Langmuir–Hinshelwood and
  Eley–Rideal; rate laws and their limits; apparent activation energy;
  turnover frequency per site; the Sabatier principle and volcano plots).
  4 Industrial catalysts (ammonia on promoted iron; SO₂ oxidation on V₂O₅;
  the three-way converter and its λ window; zeolite cracking; support,
  dispersion, poisoning, sintering). 5 Looking at surfaces (temperature-
  programmed desorption; X-ray photoelectron spectroscopy; the scanning
  tunnelling microscope).
- **Definitions.** `def:b3:surfaces-catalysis:adsorption` (adsorption,
  adsorbate, adsorbent, desorption); `:physi-chemi` (physisorption,
  chemisorption); `:coverage` (fractional coverage, monolayer);
  `:isosteric` (isosteric enthalpy of adsorption); `:surface-area` (specific
  surface area); `:mechanisms` (Langmuir–Hinshelwood mechanism, Eley–Rideal
  mechanism); `:sabatier` (Sabatier principle, volcano plot); `:catalyst-
  design` (catalyst support, promoter, catalyst poison, metal dispersion,
  sintering); `:tpd` (temperature-programmed desorption). Named statements:
  `thm:…:langmuir` (Langmuir isotherm), `thm:…:bet` (BET isotherm).
- **Ownership check.** S1: Y3 ch16 owns *adsorption*, *physisorption*,
  *chemisorption*; Book 2 owns *catalyst*, *homogeneous/heterogeneous
  catalysis*; Book 3 owns *turnover frequency*, *conversion*, *selectivity*,
  *photoelectron spectroscopy*: recalled (XPS is "photoelectron spectroscopy
  with X-rays", no new definition).
- **Statements.** `thm:…:langmuir` θ = Kp/(1 + Kp) (proof by kinetics; a
  second proof by statistical thermodynamics); `prop:…:dissociative`
  θ ∝ √p at low p (proof); `prop:…:competitive` (proof); `prop:…:isosteric`
  $(\partial\ln p/\partial T)_\theta = -\Delta_{ads}H/RT^2$ (proof);
  `thm:…:bet` (proof by summing layers); `prop:…:lh-rate` and `prop:…:
  er-rate` (proofs), maximum of the LH rate (proof);
  `prop:…:apparent-ea` $E_{a,app} = E_a + \Delta_{ads}H$ (proof).
- **Methods.** `met:…:bet-area` (specific surface area from a nitrogen
  isotherm); `met:…:mechanism-from-rate` (LH or ER from pressure
  dependences); `met:…:dispersion` (metal dispersion and particle size from
  H₂ chemisorption).
- **Boxes.** `history` Langmuir 1916–18 and the Haber–Bosch catalyst
  screening; `inthelab` a BET measurement at 77 K; `safety` nickel and
  platinum-group catalysts: pyrophoric reduced metals (PubChem GHS for Raney
  nickel).
- **Figures.** S physisorption/chemisorption potential curves with the
  precursor state and dissociation; S top views of FCC(111) and (100) with
  atop, bridge and hollow sites; F `langmuir-bet` (Langmuir isotherms at two
  temperatures; a BET isotherm and its linear form; test: θ = ½ at p = 1/K,
  linear BET recovers v_m and c); F `surface-rates` (LH rate versus p_A for
  three p_B with its maximum; ER rate; test: maximum at K_Ap_A = 1 + K_Bp_B);
  S a qualitative volcano plot (no values); P a catalytic-converter
  honeycomb (Commons — verify); AI an ammonia synthesis plant (industrial).
- **Ledger.** N₂ cross-sectional area 0.162 nm² (NIST-SP960; **check
  reachability**); ammonia production (Book 2 `usgs:` row if present, else
  USGS-MCS); three-way catalyst metals and λ window (open review, **at
  risk**: else qualitative); GHS of Raney nickel and V₂O₅ (PubChem).
- **Exercises palette.** Langmuir K from two points; dissociative
  adsorption of H₂; competitive adsorption of CO and O₂; isosteric enthalpy
  from two isotherms; BET area from data; LH or ER from kinetics; apparent
  Ea; TOF from rate and dispersion; poisoning by sulfur (site blocking);
  Sabatier reasoning with adsorption energies.
- **Weekend problem — "Measuring a catalyst".** I a nitrogen isotherm
  (problem data) and the BET plot → v_m, c; II the specific surface area
  with the ledger cross-section; III H₂ chemisorption → dispersion and the
  mean Pt particle size (spherical model, Pt density read-only from a
  ledger row); IV a hydrogenation rate on that catalyst → TOF per surface
  atom. **Named number: the mean platinum particle diameter in nm**
  (computed). 24 questions.

## Ch. 17 — Interfaces, Surfactants and Colloids — `colloids`

- **Hook.** Mayonnaise is oil dispersed as droplets in a little water and
  vinegar, held there by the lecithin of egg yolk; whisk it wrong and it
  splits. Milk, fog, paint and blood are the same kind of matter.
- **Recall.** Year 1 volume: amphiphilic, hydrophilic, hydrophobic, London
  interaction, relative permittivity; Book 1 (grade 11): the micelle at the
  school level; Year 2 volume: chemical potential, ionic strength, activity;
  \cref{ch:b3:surfaces-catalysis} (adsorption),
  \cref{ch:b3:electrode-kinetics} (double layer, Debye length).
- **Sections.** 1 Interfaces and surface tension (surface Gibbs energy;
  Laplace pressure; wetting and Young's equation; the Kelvin equation and
  Ostwald ripening). 2 Surfactants and micelles (classes; the Gibbs
  adsorption isotherm and surface excess; the critical micelle
  concentration; aggregation number; the packing parameter: spheres,
  cylinders, bilayers; detergency). 3 Colloids (dispersed phase and medium;
  sols, emulsions, foams, gels, aerosols; the Tyndall effect; Brownian
  motion, from physics). 4 Colloidal stability (the Debye length recalled
  from \cref{ch:b3:electrode-kinetics}; zeta potential; DLVO; Schulze–Hardy; steric
  stabilisation; coagulation and flocculation). 5 Colloids at work
  (emulsifiers and HLB; foams and antifoams; water clarification with
  aluminium salts; stabilising nanoparticles).
- **Definitions.** `def:b3:colloids:surface-tension` (surface tension);
  `:wetting` (contact angle, wetting); `:surfactant` (surfactant, anionic
  surfactant, cationic surfactant, non-ionic surfactant); `:surface-excess`
  (surface excess concentration); `:micelle` (micelle, critical micelle
  concentration, aggregation number); `:packing` (packing parameter);
  `:colloid` (colloid, dispersed phase, dispersion medium, sol, emulsion,
  foam, gel, aerosol); `:tyndall` (Tyndall effect); `:zeta` (zeta potential); `:stability` (coagulation, flocculation, critical
  coagulation concentration, steric stabilisation); `:ripening` (Ostwald
  ripening); `:hlb` (hydrophilic–lipophilic balance). Named statements:
  `thm:…:young` (Young's equation), `thm:…:kelvin` (Kelvin equation),
  `thm:…:gibbs-adsorption` (Gibbs adsorption isotherm),
  `prop:…:schulze-hardy` (Schulze–Hardy rule).
- **Ownership check.** S1/S1b: Book 4 owns *micelle* at university level
  (**re-founds** Book 1 g11); Book 2 owns *amphiphilic*, *hydrophilic*,
  *hydrophobic*, *London interaction*, *relative permittivity*: recalled.
  Book 3 owns *ionic strength*, *chemical potential*, *activity
  coefficient*, *glass transition*: recalled. *Electrical double layer* is
  ch15's (recalled). *Gel* here is the colloid; ch23's *sol–gel process*
  uses it. *Surface tension* is not owned by any chemistry book (physics
  uses it as known): defined here as a surface Gibbs energy.
- **Statements.** `prop:…:laplace` Δp = 2γ/r (proof by virtual work);
  `thm:…:young` γ_SV = γ_SL + γ_LV cos θ (proof by energy minimisation);
  `thm:…:kelvin` $\ln(p/p^*) = 2\gamma V_m/(rRT)$ (proof from μ);
  `thm:…:gibbs-adsorption` $\Gamma = -(1/RT)\,\dd\gamma/\dd\ln c$ (proof from
  the Gibbs–Duhem relation of the interface); `prop:…:cmc-break` (argued
  from μ constancy above the CMC); `prop:…:packing` shape from v/(a₀l)
  (proof by geometry); `thm:…:dlvo` (`\admitted` forms of both terms, combined and
  analysed); `prop:…:schulze-hardy` CCC ∝ z⁻⁶ (partial proof).
- **Methods.** `met:…:cmc` (CMC from surface tension or conductivity
  breaks); `met:…:surface-excess` (area per molecule from a γ–ln c
  slope); `met:…:coagulant-dose` (choosing a coagulant dose).
- **Boxes.** `history` Tyndall (1869) and Zsigmondy's ultramicroscope;
  `inthelab` measuring surface tension with a du Noüy ring; `safety` sodium
  dodecyl sulfate (PubChem GHS).
- **Figures.** F `surfactant-cmc` (γ versus log c with the break; conductivity
  versus c with the break; test: Gibbs slope → Γ, break at the CMC); F `dlvo`
  (interaction energy versus distance at three ionic strengths; test: Debye
  length formula, barrier disappearing above a threshold); S micelle and
  packing shapes (cone → sphere, truncated cone → cylinder, cylinder →
  bilayer); S a drop on a surface with the three tensions and θ; S charged
  particle with Stern layer, slipping plane and ζ; P Tyndall effect: a laser
  beam through a colloid (Commons — verify); AI mayonnaise being whisked in a
  kitchen (everyday).
- **Ledger.** `st:H2O.25C` surface tension of water (IAPWS release); CMC of
  SDS, CTAB, Triton-type non-ionic (NSRDS-NBS36, `cmc:` rows; **check
  reachability**); water permittivity (Book 2 `epsr:H2O`, read-only);
  aggregation number of SDS (same source, **at risk**); Hamaker constants
  (**at risk**, else model values stated as such); GHS of SDS, aluminium
  sulfate (PubChem).
- **Exercises palette.** Laplace pressure in a 1 µm bubble; Kelvin vapour
  pressure of a 10 nm droplet; contact angle from three tensions; surface
  excess and area per molecule; CMC from data; packing parameter of SDS
  and of a double-chain lipid; Debye lengths of 0.01 M NaCl and MgSO₄;
  Schulze–Hardy ratios Na⁺ : Ca²⁺ : Al³⁺; HLB of a non-ionic surfactant;
  Ostwald ripening direction.
- **Weekend problem — "Clearing muddy water with alum".** I clay particles
  as a negative colloid; the Debye length of river water from given ion
  concentrations; II the DLVO barrier at that ionic strength; III
  Schulze–Hardy: Al³⁺ against Na⁺ and Ca²⁺; IV the alum dose per cubic metre
  to reach the CCC (problem CCC), and the hydrolysis that also flocculates.
  **Named number: the minimum mass of Al₂(SO₄)₃ per cubic metre of water**
  (computed with `tools/molar_mass.py`). 24 questions.

## Ch. 18 — Electronic Spectra and Magnetism of Complexes — `complex-spectra-magnetism`

- **Hook.** Ruby is red and emerald is green, yet both owe their colour to
  the same ion, Cr³⁺, a few per cent of it in an aluminium oxide or a
  beryllium silicate. A slightly weaker ligand field is the whole difference.
- **Recall.** Year 2 volume: transition element, dⁿ configuration,
  crystal-field splitting, high and low spin, pairing energy, CFSE, d–d
  transition, spectrochemical series, ligand field theory, paramagnetic,
  diamagnetic; \cref{ch:b3:many-electron-atoms} (terms, Hund),
  \cref{ch:b3:group-theory-applied} (reduction, direct products),
  \cref{ch:b3:electronic-spectroscopy} (spin and Laporte rules,
  charge-transfer transitions), \cref{ch:b3:partition-functions} (Boltzmann).
- **Sections.** 1 From free-ion terms to ligand-field terms (characters of
  the rotation group; the splitting of S, P, D, F, G in O_h; weak- and
  strong-field limits; correlation diagrams; the hole formalism and the
  tetrahedral inversion). 2 Tanabe–Sugano diagrams (Racah parameters;
  reading d³ and d⁸; Δ_o and B from two bands; the nephelauxetic effect;
  spin-forbidden sharp lines). 3 Intensities and charge transfer (relaxing
  the Laporte rule by vibronic coupling and by the absence of a centre;
  LMCT and MLCT bands: permanganate, chromate, [Ru(bpy)₃]²⁺; ruby versus
  emerald; ruby's red emission). 4 The Jahn–Teller effect (the theorem;
  Cu²⁺ and high-spin Mn³⁺ elongations; split bands). 5 Magnetism (molar
  susceptibility; the Curie law from Boltzmann populations; the effective
  moment; the spin-only formula; orbital contributions of T terms; spin
  crossover as a thermal equilibrium; ferro- and antiferromagnetic coupling
  in outline; the Evans NMR method).
- **Definitions.** `def:b3:complex-spectra-magnetism:ligand-field-term`
  (ligand-field term); `:correlation` (correlation diagram); `:racah` (Racah
  parameters); `:tanabe-sugano` (Tanabe–Sugano diagram); `:nephelauxetic`
  (nephelauxetic effect, nephelauxetic ratio); `:vibronic-coupling`
  (vibronic coupling); `:ct` (ligand-to-metal charge transfer,
  metal-to-ligand charge transfer); `:susceptibility` (magnetic
  susceptibility, molar susceptibility); `:curie` (Curie constant);
  `:moment` (effective magnetic moment, spin-only moment, orbital
  contribution); `:spin-crossover` (spin crossover); `:cooperative`
  (ferromagnetism, antiferromagnetism). Named statements:
  `thm:…:jahn-teller` (Jahn–Teller theorem), `thm:…:curie` (Curie law).
- **Ownership check.** Map: Y3 owns term splitting, Tanabe–Sugano,
  Jahn–Teller, susceptibility, spin-only moment (S1/S2). Book 3 owns
  *crystal-field splitting*, *high/low spin*, *pairing energy*, *CFSE*,
  *d–d transition*, *spectrochemical series*, *ligand field theory*,
  *paramagnetic*, *diamagnetic*, *π-donor/π-acceptor ligand*,
  *back-donation*: recalled. *Correlation diagram* is defined here in the
  general sense (states of two limits joined by symmetry); ch26 uses the
  phrase *orbital correlation diagram* (its own definition, the longer
  phrase wins in the linker). *Spin multiplicity* and *spectroscopic term*
  are ch2's.
- **Statements.** `prop:…:rotation-characters` χ_L(α) =
  sin((L + ½)α)/sin(α/2) (`\admitted`, treated in more advanced courses);
  `thm:…:term-splitting` the splitting table S → A₁g, P → T₁g, D → E_g +
  T₂g, F → A₂g + T₁g + T₂g, G → A₁g + E_g + T₁g + T₂g (proof by reduction);
  `prop:…:hole` dⁿ and d¹⁰⁻ⁿ have inverted splittings; O_h dⁿ ↔ T_d d¹⁰⁻ⁿ
  (proof); `prop:…:d3-bands` for d³: ν₁ = Δ_o and the two ⁴T₁g energies from a
  2×2 matrix (proof), giving Δ_o and B from two bands; `prop:…:intensity-
  order` spin-forbidden ≪ Laporte-forbidden < tetrahedral < CT (argued from
  ch7); `thm:…:jahn-teller` (`\admitted`, treated in more advanced courses;
  consequences derived); `thm:…:curie` χ = C/T with C ∝ g²S(S+1) (proof for
  S = ½ from Boltzmann, general case admitted); `prop:…:spin-only`
  μ_eff = 2√(S(S+1)) μ_B = √(n(n+2)) μ_B (proof); `prop:…:orbital-
  contribution` A and E ground terms quench the orbital moment, T terms do
  not (argued); `prop:…:crossover` high-spin fraction and T½ = ΔH/ΔS
  (proof).
- **Methods.** `met:…:split-term` (splitting a free-ion term in O_h);
  `met:…:read-ts` (assigning bands and extracting Δ_o, B, β from a
  Tanabe–Sugano diagram); `met:…:evans` (moment from the Evans shift).
- **Boxes.** `history` Tanabe and Sugano 1954, Jahn and Teller 1937;
  `inthelab` Evans method in an NMR tube with a coaxial insert; `safety`
  potassium dichromate and chromate (PubChem GHS, carcinogen).
- **Figures.** F `tanabe-sugano` (d³ and d⁸ diagrams by full diagonalisation
  of the dⁿ ligand-field and electron-repulsion matrices with C/B fixed;
  vertical lines for ruby and emerald at their fitted Δ_o/B; test: free-ion
  term energies at Δ = 0 (³F, ³P = 15B; ⁴F, ⁴P = 15B), the d³ ν₁ = Δ_o,
  high-field slopes); S correlation diagram d² weak → strong field (the
  Book 3 `omlevel`/`omcorr` pics); S Jahn–Teller elongation: d-orbital
  levels e_g → a₁g + b₁g, t₂g → b₂g + e_g, with the octahedron (Book 3's
  `omoctahedron` pic); F `curie` (χT versus T for a Curie paramagnet and a
  spin-crossover compound; χ versus 1/T; test: χT constant, T½ = ΔH/ΔS);
  P a ruby and an emerald crystal (Commons, real specimens — verify); AI
  none.
- **Ledger.** Free-ion Racah B of Cr³⁺, V³⁺, Ni²⁺ computed from NIST ASD
  term energies (`lev:` rows, barycentres computed in figdata, tested);
  absorption-band positions of ruby and emerald (CALTECH-MS spectra, `lf:`
  rows, **check**); [Ni(H₂O)₆]²⁺ and [Cr(H₂O)₆]³⁺ bands (open source **at
  risk**, else problem data presented as "a measured spectrum"); ruby R-line
  wavelength 694.3 nm (open source, **check**); `const:muB` shared; GHS of
  K₂Cr₂O₇ (Book 1/2 `ghs:` read-only).
- **Exercises palette.** Splitting of D, F, G terms; ground terms and their
  O_h splitting for d¹–d⁹; d⁸ Ni²⁺ three bands; Δ_o and B of a d³ complex
  from two bands; nephelauxetic ratios; intensity ranking (MnO₄⁻, [Mn(H₂O)₆]²⁺,
  [CoCl₄]²⁻, [Co(H₂O)₆]²⁺); Jahn–Teller predictions for d⁹, high-spin d⁴,
  low-spin d⁷; spin-only moments; orbital contribution of high-spin Co²⁺ in
  O_h versus T_d; Curie constant from χT; Evans method computation.
- **Weekend problem — "One ion, two gems".** I Cr³⁺ d³: ground term ⁴F and
  its O_h splitting; II the two spin-allowed bands of ruby and of emerald
  (ledger) assigned on the d³ Tanabe–Sugano diagram; III Δ_o, B and the
  nephelauxetic ratio against the free-ion B computed from NIST levels;
  IV the spin-forbidden ²E_g → ⁴A₂g emission of ruby and why it is sharp and
  slow. **Named number: Δ_o(ruby) − Δ_o(emerald) in cm⁻¹** (computed from
  the ledger bands; the colour difference in one number). 25 questions.

## Ch. 19 — Reaction Mechanisms of Complexes — `complex-mechanisms`

- **Hook.** [Cr(H₂O)₆]³⁺ keeps a given water ligand for days; [Cu(H₂O)₆]²⁺
  swaps one a billion times a second. The same reaction, ligand exchange,
  spans more than fifteen powers of ten — and the d-electron count predicts
  where each ion sits.
- **Recall.** Year 2 volume: complexes, denticity, bridging ligand, fac/mer,
  ligand exchange (as an elementary step), CFSE, high and low spin; Year 1
  volume: mechanisms, steady state, rate-determining step;
  \cref{ch:b3:rate-theories} (Eyring, ΔS‡), \cref{ch:b3:electrode-kinetics}
  (electron transfer at an electrode), \cref{ch:b3:complex-spectra-magnetism}.
- **Sections.** 1 Lability and inertness (Taube's criterion; the water-
  exchange scale; ligand-field activation energies; activation volumes as a
  probe). 2 Substitution mechanisms (dissociative, associative, interchange;
  rate laws; the Eigen–Wilkins mechanism; base hydrolysis by the
  conjugate-base mechanism; stereochemistry of octahedral substitution).
  3 Square-planar substitution and the trans effect (associative path; the
  two-term rate law; the trans-effect series; trans influence versus trans
  effect; synthesis of cis- and trans-[PtCl₂(NH₃)₂]). 4 Electron transfer
  (outer and inner sphere; Taube's chromium–cobalt experiment; self-exchange;
  the Franck–Condon restriction). 5 Marcus theory (intersecting parabolas;
  reorganisation energy, inner and outer; ΔG‡ = (λ + ΔG°)²/4λ; the cross
  relation; the inverted region, predicted 1956 and observed 1984).
- **Definitions.** `def:b3:complex-mechanisms:labile` (labile complex,
  kinetically inert complex); `:activation-volume` (volume of activation);
  `:mechanisms` (dissociative mechanism, associative mechanism, interchange
  mechanism); `:eigen-wilkins` (Eigen–Wilkins mechanism, outer-sphere
  complex); `:conjugate-base` (conjugate-base mechanism); `:trans-effect`
  (trans effect, trans influence); `:electron-transfer` (outer-sphere
  electron transfer, inner-sphere electron transfer, self-exchange
  reaction); `:reorganisation` (reorganisation energy); `:inverted`
  (inverted region). Named statements: `thm:…:marcus` (Marcus equation),
  `thm:…:cross-relation` (Marcus cross relation).
- **Ownership check.** S2: Y3 ch19 keeps *dissociative/associative
  mechanism*, *trans effect*; Book 3 owns *ligand exchange* (the step),
  *bridging ligand*, *denticity*, *fac/mer*, *CFSE*: recalled. "Inert" is
  defined only as the phrase *kinetically inert complex* (ch33's *inert
  atmosphere* is Book 3's). "Outer-sphere complex" and "outer-sphere
  electron transfer" are distinct phrases, both defined here.
- **Statements.** `prop:…:d-a-laws` rate laws of D (saturation) and A
  (second order) mechanisms (proof by steady state); `thm:…:eigen-wilkins`
  $k_{obs} = K_{os}k_i[Y]/(1 + K_{os}[Y])$ (proof); `prop:…:lfae`
  ligand-field activation energies for square-pyramidal TS, d³ and low-spin
  d⁶ largest (proof in Dq units from CFSE tables); `prop:…:pressure`
  $(\partial\ln k/\partial p)_T = -\Delta V^\ddagger/RT$ (proof from TST);
  `prop:…:conjugate-base` rate = kK[complex][OH⁻]/(1 + K[OH⁻]) (proof);
  `prop:…:square-planar` $k_{obs} = k_1 + k_2[Y]$ (proof);
  `thm:…:marcus` (proof from two parabolas); `cor:…:inverted` (proof);
  `thm:…:cross-relation` $k_{12} = \sqrt{k_{11}k_{22}K_{12}f}$ (proof with
  f ≈ 1); `prop:…:outer-reorganisation` λ_o ∝ (1/n² − 1/ε_s) (`\admitted`
  Marcus–Hush form).
- **Methods.** `met:…:diagnose` (D or A from ΔS‡, ΔV‡ and the entering-group
  dependence); `met:…:pt-synthesis` (planning Pt(II) isomers with the
  trans-effect series); `met:…:marcus-estimate` (a cross-reaction rate from
  self-exchange data).
- **Boxes.** `history` Taube's experiment (1953) and Marcus (1956; Closs and
  Miller 1984); `inthelab` ¹⁷O-NMR line broadening to measure water exchange;
  `safety` K₂[PtCl₄] (PubChem GHS, sensitiser).
- **Figures.** F `ligand-field-activation` (computed LFAE in Dq for d⁰–d¹⁰,
  high and low spin, as bars; test: d³ and LS d⁶ maxima, values from the
  CFSE tables); F `marcus` (intersecting parabolas for three ΔG°; ln k versus
  −ΔG° with the inverted region; test: maximum at −ΔG° = λ); S Taube's
  bridged intermediate Co–Cl–Cr (chemfig/TikZ with Book 3's
  `omoctahedron`); S cisplatin and transplatin syntheses by the trans effect
  (chemfig square-planar schemes); S energy profiles of D and A mechanisms
  (intermediate of lower/higher coordination number, Book 2's `omprofile`);
  P Henry Taube or Rudolph Marcus (Commons — verify licence, else none).
- **Ledger.** Water-exchange rate constants of a set of aqua ions (open
  review, **at risk**: if none, the figure becomes the computed LFAE and the
  hook gives orders of magnitude only with a source); self-exchange rate
  constants for Fe³⁺/²⁺ and a ruthenium couple (**at risk**, else problem
  data); E° values read-only from Book 2's computed rows; GHS of K₂[PtCl₄] and
  cisplatin (PubChem).
- **Exercises palette.** Labile or inert by dⁿ and spin; rate law of a given
  mechanism; Eigen–Wilkins saturation; sign of ΔV‡ and ΔS‡ for D and A;
  products of [PtCl₄]²⁻ + 2NH₃ and [Pt(NH₃)₄]²⁺ + 2Cl⁻; trans influence from
  bond lengths (problem data); inner versus outer sphere evidence; Marcus
  ΔG‡ for given λ, ΔG°; cross relation numerically; the inverted region
  with an example.
- **Weekend problem — "Making cisplatin, not transplatin".** I square-planar
  Pt(II), d⁸ low spin; II a route from K₂[PtCl₄] through [PtI₄]²⁻ (Dhara's
  method) and the trans effect of I⁻ versus NH₃, each step justified; III the
  aquation of cisplatin, first order (problem rate constant): half-life and
  fraction aquated after 2 h at 37 °C; IV the chloride-dependent equilibrium
  in blood plasma versus inside a cell (problem chloride concentrations).
  **Named number: the ratio of the aqua-complex fraction inside the cell to
  that in plasma at equilibrium** (computed). 25 questions.

## Ch. 20 — Organometallic Chemistry: Bonding and Ligands — `organometallic-bonding`

- **Hook.** In 1951 an orange, air-stable powder of formula FeC₁₀H₁₀ made no
  sense to its discoverers: iron bonded to two carbon rings by all ten
  carbons at once. Ferrocene opened modern organometallic chemistry.
- **Recall.** Year 1 volume: organometallic compound, Grignard reagents;
  Year 2 volume: 18-electron rule, valence electron count, hapticity,
  π-acceptor and π-donor ligands, back-donation, oxidative addition and the
  other elementary steps, fragment orbitals;
  \cref{ch:b3:group-theory-applied} (CO stretches, SALCs),
  \cref{ch:b3:complex-spectra-magnetism} (moments).
- **Sections.** 1 Electron counting and oxidation states (neutral-ligand and
  ionic methods; dⁿ; the 16-electron square-planar complexes). 2 Carbonyls
  and phosphines (making carbonyls (Mond); σ donation and π back-donation as
  synergic bonding; ν(CO) as a probe: isoelectronic series, terminal and
  bridging CO; the octahedral complex's π interactions and Δ_o derived with
  symmetry-adapted combinations; phosphines: Tolman cone angle and
  electronic parameter). 3 π ligands (alkenes and the Dewar–Chatt–Duncanson
  model; Zeise's salt; allyl, dienes, arenes; cyclopentadienyl and the
  metallocenes; the MO diagram of ferrocene, qualitatively). 4 Carbenes,
  carbynes and metal–metal bonds (Fischer and Schrock carbenes; N-heterocyclic
  carbenes; the quadruple bond of [Re₂Cl₈]²⁻ and its δ component). 5 The
  isolobal analogy (CH₃ ↔ Mn(CO)₅, CH₂ ↔ Fe(CO)₄, CH ↔ Co(CO)₃; the
  tetrahedrane Co₃(CO)₉CH; agostic interactions).
- **Definitions.** `def:b3:organometallic-bonding:carbonyl` (metal carbonyl,
  terminal carbonyl, bridging carbonyl); `:synergic` (synergic bonding);
  `:tolman` (Tolman cone angle, Tolman electronic parameter); `:dcd`
  (Dewar–Chatt–Duncanson model, metallacyclopropane); `:metallocene`
  (metallocene, sandwich compound); `:carbene` (carbene, carbene complex,
  Fischer carbene, Schrock carbene, N-heterocyclic carbene); `:carbyne`
  (carbyne complex); `:delta` (δ bond, quadruple bond); `:isolobal`
  (isolobal fragments, isolobal analogy); `:agostic` (agostic interaction).
- **Ownership check.** S2: Book 3 owns *hapticity*, *back-donation*,
  *π-acceptor*, *π-donor*, *18-electron rule*, *valence electron count*;
  Book 2 owns *organometallic compound*: all recalled; *back-bonding* is not
  defined. *Carbene* (the free species) is defined here, its earliest need
  in this book; ch27 recalls it and owns *singlet/triplet carbene*,
  *carbenoid*, *cyclopropanation*. Electron-counting conventions are a
  `met:` (unindexed).
- **Statements.** `prop:…:co-frequency` ν(CO) falls as back-donation rises
  (argued from the MO of CO; ledger evidence); `prop:…:pi-delta` π-acceptor
  ligands raise Δ_o, π donors lower it (proof with the t₂g SALCs of O_h — the
  Year 2 volume admitted it); `prop:…:dcd` alkene C–C lengthens and the
  substituents bend back (argued); `prop:…:ferrocene` 18 electrons and the
  e₂, a₁, e₁ ordering (qualitative MO, argued with D₅d SALCs);
  `prop:…:quadruple` σ²π⁴δ² from d–d overlaps and the eclipsed geometry
  (proof by symmetry); `prop:…:isolobal` (argued from frontier fragment
  orbitals).
- **Methods.** `met:…:count` (count, oxidation state, dⁿ, both ways);
  `met:…:isolobal` (predicting a structure by isolobal replacement).
- **Boxes.** `history` ferrocene 1951–52 and the Mond process (1890);
  `inthelab` handling Ni(CO)₄-free carbonyls under a fume hood; `safety`
  nickel tetracarbonyl (PubChem GHS: acute toxicity, carcinogen).
- **Figures.** S M–CO σ donation and π back-donation with orbital lobes
  (Book 3's `omp`, `omdxy`); S Dewar–Chatt–Duncanson for an alkene; S
  ferrocene (3D sandwich drawing) and its qualitative MO diagram (Book 3's
  `omlevel`/`omcorr` or modiagram); S Re–Re δ bond (two d_xy lobes face to
  face, eclipsed Cl₄ squares); S the isolobal series (fragment drawings);
  F `co-stretch` (ν(CO) of an isoelectronic series against metal charge,
  ledger points, if sourced; test: values equal the ledger); P ferrocene
  crystals (Commons — verify); AI none.
- **Ledger.** `vib:CO` free CO fundamental (WebBook, `diat:CO.we` and ωexe →
  ν₀ computed); ν(CO) of [V(CO)₆]⁻, Cr(CO)₆, [Mn(CO)₆]⁺, Ni(CO)₄ (open
  sources **at risk**; CCCBDB may list Cr(CO)₆ and Ni(CO)₄); Tolman
  parameters (**at risk**, else qualitative with problem data); Re–Re
  distance in K₂[Re₂Cl₈]·2H₂O (COD, **check**); ferrocene geometry (COD or
  CCCBDB); GHS of Ni(CO)₄, ferrocene (PubChem).
- **Exercises palette.** Counts for Fe(CO)₅, Mn₂(CO)₁₀, CpMo(CO)₃H, Zeise's
  anion, Cr(η⁶-C₆H₆)(CO)₃, Cp₂ZrCl₂; ordering ν(CO) in a series; IR count of
  fac/mer carbonyls (ch5); cone angle and reactivity; Fischer or Schrock from
  reactivity; isolobal partners; δ bond order and the effect of rotating to
  staggered; agostic evidence; 18-electron rule exceptions.
- **Weekend problem — "Sandwiches".** I counts of ferrocene, cobaltocene,
  nickelocene and the ferrocenium cation; II the qualitative MO diagram and
  the unpaired electrons of each; spin-only moments; III redox: why
  cobaltocene is a strong reductant (19 e) and ferrocene a reference
  couple (ch15); IV isolobal replacement and a CO-substituted derivative's
  IR count (ch5). **Named number: the spin-only moment of nickelocene,
  2.83 μ_B** (computed, two unpaired electrons). 24 questions.

## Ch. 21 — Homogeneous Catalysis in Industry — `homogeneous-catalysis`

- **Hook.** Most of the world's acetic acid is made from methanol and carbon
  monoxide in a few large plants, each on a rhodium or iridium catalyst
  dissolved at a concentration of a few millimoles per litre that turns over
  many thousands of times an hour.
- **Recall.** Year 2 volume: oxidative addition, reductive elimination,
  migratory insertion, β-hydride elimination, transmetalation, catalytic
  cycle, precatalyst, TON, TOF, catalytic hydrogenation, the hydroformylation
  and cross-coupling cycles, tacticity, chain-growth polymerisation,
  conversion, selectivity, Le Chatelier; \cref{ch:b3:organometallic-bonding}
  (counting, carbonyls, carbenes), \cref{ch:b3:complex-kinetics}
  (saturation kinetics), \cref{ch:b3:point-groups} (C₂ and C_s).
- **Sections.** 1 Hydrogenation (Wilkinson's catalyst, its cycle and
  kinetics; selectivity; the asymmetric versions in
  \cref{ch:b3:asymmetric-synthesis}). 2 Carbonylation processes
  (hydroformylation: cobalt versus rhodium–phosphine, linear/branched ratio,
  conditions; Monsanto and Cativa acetic acid: rhodium/iodide and
  iridium/iodide cycles, rate-determining oxidative addition of MeI, the
  water–gas shift side reaction, why iridium won). 3 Olefin metathesis (the
  Chauvin mechanism through a metallacyclobutane; Schrock and Grubbs
  catalysts; ring-closing, ring-opening polymerisation, cross metathesis;
  driving the equilibrium by ethylene loss). 4 Palladium cross-coupling
  (Heck, Suzuki–Miyaura, Negishi, Sonogashira as industrial tools; ligand
  effects; scale and palladium removal). 5 Polymerisation catalysis
  (Ziegler–Natta catalysts; the Cossee–Arlman mechanism; metallocene
  single-site catalysts and tacticity control by symmetry; molar-mass
  distribution of a single-site catalyst).
- **Definitions.** `def:b3:homogeneous-catalysis:hydroformylation`
  (hydroformylation, linear-to-branched ratio); `:carbonylation`
  (carbonylation); `:metathesis` (olefin metathesis, metallacyclobutane,
  ring-closing metathesis, ring-opening metathesis polymerisation, cross
  metathesis); `:chauvin` (Chauvin mechanism); `:cross-coupling`
  (cross-coupling reaction, Heck reaction, Suzuki–Miyaura coupling);
  `:ziegler-natta` (Ziegler–Natta catalyst, Cossee–Arlman mechanism,
  single-site catalyst).
- **Ownership check.** S2 split: Book 3 ch20 reads hydrogenation,
  hydroformylation and cross-coupling as cycles (no definition of those
  process names in its map); Book 4 ch21 treats the industrial processes and
  owns their names. Book 3 owns every elementary-step term, *catalytic
  cycle*, *TON*, *TOF*, *tacticity*, *isotactic*, *syndiotactic*,
  *dispersity*, *living polymerisation*: recalled. Map: Ziegler–Natta is
  "recalled in Y3 `homogeneous-catalysis`" from Y2 polymers; the catalyst
  terms are new here.
- **Statements.** `prop:…:wilkinson-rate` saturation in H₂ and inhibition by
  PPh₃ (proof by pre-equilibria); `prop:…:monsanto-rate` rate = k[Rh][MeI],
  zero order in CO and MeOH (proof from the rds); `prop:…:metathesis-
  equilibrium` ring closing is driven by the entropy of ethylene release
  (proof with K and the gas removed); `prop:…:tacticity-symmetry` C₂ →
  isotactic, C_s → syndiotactic (argued with the site symmetry of ch4);
  `prop:…:schulz-flory` a single-site catalyst gives Đ → 2 (proof from a
  constant propagation/transfer ratio).
- **Methods.** `met:…:read-cycle` (count electrons and oxidation states at
  each step, find the resting state and the rds); `met:…:choose-coupling`
  (partners, catalyst and base for a given bond).
- **Boxes.** `history` Ziegler and Natta (1950s), Chauvin, Grubbs and Schrock
  (2005); `inthelab` a Suzuki coupling under nitrogen and palladium
  scavenging; `safety` methyl iodide and carbon monoxide (PubChem GHS).
- **Figures.** S Wilkinson cycle (Book 3's cycle styles, chemfig species,
  electron counts); S Monsanto and Cativa cycles side by side; S Chauvin
  mechanism (chemfig, metallacyclobutane); S Suzuki–Miyaura cycle; S
  Cossee–Arlman insertion and C₂ versus C_s metallocenes with the polymer
  stereochemistry; F `schulz-flory` (molar-mass distribution of a single-site
  polymer, number and mass fractions; test: Đ → 2); AI a large chemical plant
  at dusk (industrial).
- **Ledger.** Cativa/Monsanto conditions and catalyst performance (JMTR,
  Jones 2000, **check**); acetic acid world capacity (**at risk**, else not
  printed); polyethylene production (**at risk**); GHS of MeI, CO, Pd(OAc)₂
  (PubChem).
- **Exercises palette.** Electron counts along the Wilkinson cycle;
  hydroformylation products of propene and their ratio; Monsanto rate law;
  RCM ring sizes and ethylene; Heck product (E) and regiochemistry; Suzuki
  disconnection of a biaryl drug fragment; tacticity from catalyst symmetry;
  TON and TOF of a plant (problem data); ROMP of norbornene; Đ of a
  single-site polymer.
- **Weekend problem — "From methanol to vinegar on an iridium cycle".** I
  the Cativa cycle with counts and oxidation states; II the rate law and
  the rds; promoters; III a plant's production rate and catalyst inventory
  (problem data) → TON per year, TOF; IV CO lost to the water–gas shift:
  selectivity on CO and CO₂ emitted per tonne. **Named number: the
  iridium catalyst's turnover frequency in h⁻¹** (computed from the
  problem's data). 24 questions.

## Ch. 22 — Solid-State Chemistry: Bands, Defects and Semiconductors — `solid-state`

- **Hook.** A solar panel on a roof and the LED in a lamp are the same kind
  of crystal — silicon or a III–V compound — with a few impurity atoms per
  million deliberately added, and a band gap that sets their colour.
- **Recall.** Year 1 volume: crystal, metallic bond, ionic and covalent
  crystals, interstitial sites, alloys; Year 2 volume: MOs, Hückel method,
  resonance integral; \cref{ch:b3:x-ray-diffraction} (reciprocal lattice),
  \cref{ch:b3:partition-functions} (Boltzmann, statistical entropy);
  Year 1 volume: Nernst equation (for the oxygen sensor).
- **Sections.** 1 From orbitals to bands (the Hückel chain of N atoms solved;
  a band of width 4|β|; density of states; s and p bands; filling and the
  Fermi level; metals, semiconductors, insulators). 2 Semiconductors
  (intrinsic carriers and their temperature dependence; direct and indirect
  gaps; n- and p-doping; the mass-action law; the p–n junction, LEDs and
  solar cells in outline; pigment colours from gaps). 3 Point defects
  (Schottky and Frenkel defects; equilibrium concentrations from the
  configurational entropy; Kröger–Vink notation; colour centres).
  4 Non-stoichiometry (Fe₁₋ₓO; defect equilibria with the oxygen pressure;
  conductivity ∝ p(O₂)^{±1/n}). 5 Ionic conductors (hopping and its
  Arrhenius law; solid electrolytes: yttria-stabilised zirconia, β-alumina,
  α-AgI; lithium-ion conductors).
- **Definitions.** `def:b3:solid-state:band` (energy band, band gap,
  valence band, conduction band); `:fermi` (density of states, Fermi
  level); `:classes` (semiconductor, insulator); `:carriers` (intrinsic
  semiconductor, charge carrier, hole); `:gap-types` (direct band gap,
  indirect band gap); `:doping` (dopant, n-type semiconductor, p-type
  semiconductor, donor level, acceptor level); `:junction` (p–n junction);
  `:defects` (point defect, Schottky defect, Frenkel defect); `:kroger-vink`
  (Kröger–Vink notation); `:colour-centre` (colour centre);
  `:non-stoichiometric` (non-stoichiometric compound); `:ionic-conductor`
  (ionic conductor, solid electrolyte).
- **Ownership check.** Not in the map apart from the chapter. Book 2 owns
  *metallic bond*, *covalent/ionic crystal*, *interstitial site*,
  *substitutional/interstitial alloy*, *donor group*/*acceptor group*
  (organic; different phrases from *donor/acceptor level*); Book 3 owns
  *resonance integral*, *Hückel method*, *fuel cell*: recalled. "Hole" is a
  homograph risk (a plain word): defined as the phrase in the definition
  only, `STOP` outside ch22 if the linker over-links.
- **Statements.** `thm:…:chain` eigenvalues α + 2β cos(kπ/(N+1)) of the
  Hückel chain (proof) and the band as N → ∞ (proof); `prop:…:filling`
  half-filled band → metal (argued); `thm:…:intrinsic` $n_i =
  \sqrt{N_cN_v}\,\eu^{-E_g/2kT}$ (proof from Boltzmann tails, effective
  densities admitted); `prop:…:mass-action` np = n_i² (proof);
  `thm:…:schottky` $n_S/N = \eu^{-\Delta H_S/2kT}$ (proof by maximising
  G with the configurational entropy); `prop:…:frenkel` (proof);
  `prop:…:brouwer` σ ∝ p(O₂)^{1/n} (proof by mass action);
  `prop:…:ionic-arrhenius` σT = A eu^{−E_a/kT} (partial proof: hopping).
- **Methods.** `met:…:kroger-vink` (writing a defect equation with site,
  mass and charge balance); `met:…:doping` (carrier concentrations of a doped
  semiconductor).
- **Boxes.** `history` the transistor (1947) and the Czochralski method;
  `inthelab` growing a silicon crystal by the Czochralski method; `safety`
  silane and arsine are mentioned without procedures (remark).
- **Figures.** F `band-chain` (Hückel chain levels for N = 2, 4, 8, 16, 64
  converging to a band, with the density of states; test: eigenvalues, band
  width 4|β|); S band diagrams of a metal, a semiconductor and an insulator
  with the Fermi level; S donor and acceptor levels in the gap; F
  `semiconductor-carriers` (ln n_i versus 1/T for Si and Ge; the three
  regimes of an n-doped crystal; test: slope −E_g/2k, saturation at N_D);
  S Schottky and Frenkel defects in 2D NaCl and AgCl lattices; S the
  zirconia oxygen sensor; AI rooftop solar panels (everyday); P a silicon
  boule (Commons — verify).
- **Ledger.** Band gaps of Si, Ge, GaAs, GaN, ZnO at 300 K and N_c, N_v of Si
  (`eg:` rows; ioffe.ru unreachable — open alternative to find, **at
  risk**); Schottky formation enthalpy of NaCl (**at risk**); YSZ
  composition (problem data); α-AgI transition temperature (PubChem, **check**);
  lattice data read-only (`lat:` rows).
- **Exercises palette.** Band width and levels of a 6-atom chain; how many
  electrons fill a band; n_i ratio Si/Ge at 300 K; electrons and holes in
  P-doped Si; Fermi-level shift; Schottky fraction of NaCl at 800 K (problem
  ΔH); Kröger–Vink for CaCl₂ in NaCl and Y₂O₃ in ZrO₂; x in Fe₁₋ₓO from a
  measured density; σ(T) Arrhenius fit; LED wavelength from a gap.
- **Weekend problem — "The oxygen sensor in an exhaust pipe".** I Y₂O₃ in
  ZrO₂: Kröger–Vink equation, vacancy concentration per mol % (computed);
  II ionic conductivity Arrhenius from problem data, the operating
  temperature; III the Nernst voltage of the cell (4 e⁻) against the
  oxygen pressure; IV lean and rich exhaust (problem p(O₂)) and the switch
  at the stoichiometric point. **Named number: the sensor voltage in rich
  exhaust at 700 °C** (computed). 25 questions.

## Ch. 23 — Inorganic Materials and Nanomaterials — `inorganic-materials`

- **Hook.** A block of silica aerogel, 99 % air, holds a flower above a
  Bunsen flame: a glass made from a gel, dried without letting it collapse.
  Materials chemistry decides structure first, then properties.
- **Recall.** Year 1 volume: crystal structure types, interstitial sites,
  allotropes, graphite and diamond; Year 2 volume: phase diagrams, glass
  transition temperature, polymers, specific surface area (this book,
  \cref{ch:b3:surfaces-catalysis}); \cref{ch:b3:x-ray-diffraction},
  \cref{ch:b3:solid-state}, \cref{ch:b3:colloids} (sol, gel),
  \cref{ch:b3:point-groups} (I_h of C₆₀), \cref{ch:b3:quantum-model-systems}.
- **Sections.** 1 Synthesis routes (the ceramic method and diffusion-
  limited growth; precursor methods; sol–gel: alkoxide hydrolysis and
  condensation, xerogels and aerogels; hydrothermal and solvothermal
  synthesis; chemical vapour deposition). 2 Ceramics and glasses (oxide
  ceramics; the perovskite structure and the tolerance factor; ferroelectric
  BaTiO₃; oxide glasses: network formers and modifiers, Zachariasen's rules,
  ion-exchange strengthening). 3 Porous solids: zeolites and MOFs
  (aluminosilicate frameworks, Löwenstein's rule, cation exchange, shape
  selectivity; metal–organic frameworks: nodes and linkers, reticular
  design, surface areas, gas storage and capture). 4 Nanoparticles (surface
  fraction and magic clusters; size effects; plasmon colours of gold;
  quantum dots as particles in a sphere). 5 Carbon nanomaterials
  (fullerenes and Euler's twelve pentagons; nanotubes and their (n, m)
  index; graphene).
- **Definitions.** `def:b3:inorganic-materials:ceramic-method` (ceramic
  method); `:sol-gel` (sol–gel process, xerogel, aerogel); `:hydrothermal`
  (hydrothermal synthesis, solvothermal synthesis); `:cvd` (chemical
  vapour deposition); `:ceramic` (ceramic); `:perovskite` (perovskite
  structure, tolerance factor); `:ferroelectric` (ferroelectric);
  `:glass` (oxide glass, network former, network modifier); `:zeolite`
  (zeolite, molecular sieve, shape selectivity); `:mof` (metal–organic
  framework, secondary building unit, reticular synthesis); `:pores`
  (micropore, mesopore, macropore); `:nano` (nanomaterial, nanoparticle);
  `:quantum-dot` (quantum dot); `:plasmon` (surface plasmon resonance);
  `:carbon` (fullerene, carbon nanotube, graphene). Named statement:
  `prop:…:lowenstein` (Löwenstein's rule).
- **Ownership check.** Not in the map apart from the chapter. Book 2 owns
  the structure-type names, *allotrope*, *covalent crystal*; Book 3 owns
  *glass transition temperature*, *polymer*, *solid solution*, *eutectic*:
  recalled. *Sol*, *gel*, *colloid* are ch17's; *specific surface area*
  ch16's; *point defect* ch22's. "Glass" is defined only as *oxide glass*
  (glassware is everywhere else in the series).
- **Statements.** `prop:…:parabolic` product-layer thickness x² = kt (proof
  from a flux ∝ 1/x); `prop:…:tolerance` Goldschmidt t = (r_A + r_O)/
  [√2(r_B + r_O)] and its range (proof of the ideal value from cube
  geometry); `prop:…:lowenstein` (statement, established experimentally;
  consequence Si/Al ≥ 1 proved); `prop:…:exchange-capacity` capacity of a
  zeolite from its formula (proof); `prop:…:magic` N(n) = (10n³ + 15n² +
  11n + 3)/3 for cuboctahedral clusters and the surface fraction (proof by
  counting shells); `thm:…:quantum-dot` confinement energy ∝ 1/R² (proof:
  particle in a sphere, ground state sin(kr)/r); `prop:…:euler` a fullerene
  has exactly 12 pentagons (proof from Euler's formula);
  `prop:…:nanotube` metallic when n − m ≡ 0 mod 3 (`\admitted`, treated in
  more advanced courses).
- **Methods.** `met:…:route` (choosing a synthesis route for a target
  solid); `met:…:zeolite-formula` (Si/Al, cation content and capacity).
- **Boxes.** `history` Kroto, Curl and Smalley's C₆₀ (1985) and the Lycurgus
  cup; `inthelab` a sol–gel silica coating and a hydrothermal autoclave;
  `safety` tetraethyl orthosilicate and nanopowders (PubChem GHS; a remark on
  inhalation).
- **Figures.** S sol–gel chemistry (hydrolysis and condensation of Si(OR)₄,
  chemfig) and the network; S perovskite ABO₃ cell (`omcubeo`, BO₆
  octahedron, depth-sorted atoms); S Zachariasen's 2D drawing of a crystal
  versus a glass network with modifier cations; S a zeolite framework
  (sodalite cage/LTA schematic) and a MOF node + linker schematic; F
  `nanoparticle-size` (surface-atom fraction versus N for magic clusters;
  confinement energy versus R for a model quantum dot; test: N(n) formula,
  fractions, 1/R² law); S graphene sheet with the (n, m) chiral vector; P
  silica aerogel (NASA, PD — verify); P the Lycurgus cup (Commons — verify
  licence); AI a hydrothermal autoclave or quartz-growing plant (industrial).
- **Ledger.** Shannon radii (Book 2 `rion:` rows read-only; new ones from the
  Shannon database for Ba²⁺, Ti⁴⁺, Sr²⁺ if missing); zeolite A formula,
  framework density and window (IZA, `iza:LTA`); MFI pore size (`iza:MFI`);
  MOF-5 composition (PubChem/COD, surface area **at risk**); aerogel density
  (NASA page, **check**); C₆₀ structure (PubChem/COD); GHS of TEOS (PubChem).
- **Exercises palette.** Parabolic growth times; balanced sol–gel equations;
  tolerance factors of SrTiO₃, BaTiO₃, CaTiO₃ (Shannon radii); Zachariasen
  roles of SiO₂, B₂O₃, Na₂O, CaO; Si/Al and exchange capacity of a zeolite;
  surface fraction of a 5 nm particle; quantum-dot colour versus size;
  pentagons and hexagons of C₇₀; metallic or semiconducting (n, m); MOF area
  per gram in football pitches.
- **Weekend problem — "Softening water with zeolite A".** I the formula
  Na₁₂[(AlO₂)₁₂(SiO₂)₁₂]·27H₂O: molar mass, Si/Al, Löwenstein; II the
  theoretical Ca²⁺ exchange capacity; III hardness of a tap water (problem
  data) and the mass of zeolite per wash; IV the 0.41 nm window (IZA) and
  shape selectivity: why Ca²⁺ enters and a surfactant does not. **Named
  number: the theoretical exchange capacity of anhydrous zeolite A in mmol
  of Ca²⁺ per gram** (computed with `tools/molar_mass.py`). 24 questions.

## Ch. 24 — Bioinorganic Chemistry — `bioinorganic`

- **Hook.** Our blood is red with iron; that of a horseshoe crab turns blue
  in air, with copper. Life chose a handful of metals for jobs no organic
  group can do: carrying O₂, splitting water, fixing nitrogen.
- **Recall.** Year 2 volume: α-amino acids, side chains, peptides,
  nucleobases and nucleotides, coordination complexes, ligand field,
  high/low spin, hard and soft nucleophiles; Year 1 volume: complexation
  constants, pL; \cref{ch:b3:complex-spectra-magnetism},
  \cref{ch:b3:complex-mechanisms} (Marcus, cisplatin aquation),
  \cref{ch:b3:complex-kinetics} (Michaelis–Menten), \cref{ch:b3:advanced-nmr}
  (T₁).
- **Sections.** 1 Metals in biology (essential elements; choosing a metal:
  hard and soft acids, the Irving–Williams series; metalloproteins,
  cofactors). 2 Oxygen transport (haem; iron(II) high spin out of the plane,
  low spin in the plane on binding O₂; Fe(III)–superoxide description;
  cooperativity, the Hill equation and plot; myoglobin versus haemoglobin;
  CO poisoning; haemocyanin and haemerythrin). 3 Metalloenzymes (carbonic
  anhydrase: a zinc-bound hydroxide; cytochrome P450 and its iron-oxo
  "compound I"; nitrogenase's FeMo cofactor in outline; vitamin B₁₂'s Co–C
  bond). 4 Electron transfer and energy (cytochromes, iron–sulfur clusters,
  blue copper proteins and the entatic state; photosynthesis: the
  Mn₄CaO₅ cluster and the Kok cycle; respiration's cytochrome c oxidase).
  5 Metals in medicine (cisplatin and its DNA adduct; carboplatin and
  oxaliplatin; gadolinium MRI contrast agents and relaxivity; chelation
  therapy).
- **Definitions.** `def:b3:bioinorganic:metalloprotein` (metalloprotein,
  metalloenzyme, cofactor); `:hsab` (hard acid, soft acid, hard and soft
  acid–base principle); `:irving-williams` (Irving–Williams series);
  `:haem` (porphyrin, haem); `:cooperativity` (cooperative binding, Hill
  coefficient); `:entatic` (entatic state); `:fes` (iron–sulfur cluster);
  `:blue-copper` (blue copper protein); `:oec` (oxygen-evolving complex);
  `:metallodrug` (metallodrug); `:contrast` (contrast agent, relaxivity);
  `:chelation-therapy` (chelation therapy). Named statement:
  `thm:…:hill` (Hill equation).
- **Ownership check.** Not in the map apart from the chapter. Book 3 owns
  *hard/soft nucleophile/electrophile* (phrases): the Lewis-acid phrases
  *hard acid*, *soft acid* and the HSAB principle are new (contested low:
  different phrases, same family; recall box cites Book 3). Book 3 owns
  *α-amino acid*, *side chain*, *peptide*, *nucleobase*, *nucleotide*; Book 2
  owns *complex*, *ligand*, *chelate*, *polydentate ligand*: recalled.
  Book 2 owns *pL scale*.
- **Statements.** `thm:…:hill` θ = pⁿ/(p₅₀ⁿ + pⁿ) for fully cooperative
  binding, and the Hill plot (proof); `prop:…:hyperbola` one site:
  θ = p/(p₅₀ + p) (proof); `prop:…:haldane` [HbCO]/[HbO₂] = M p(CO)/p(O₂)
  (proof by competition); `prop:…:irving-williams` (statement, established
  experimentally; rationale from CFSE and radii); `prop:…:carbonic-anhydrase`
  k_cat/K_M close to the diffusion limit (argued with ch12/13);
  `prop:…:kok` four photons per O₂ (proof from the electron count);
  `prop:…:relaxivity` 1/T₁ = 1/T₁,₀ + r₁[Gd] (definition-based).
- **Methods.** `met:…:hill-plot`; `met:…:choose-chelator` (pM and selectivity
  of a chelating drug).
- **Boxes.** `history` Perutz's haemoglobin structure (1959) and Rosenberg's
  cisplatin (1965); `inthelab` measuring an oxygen-binding curve with a
  spectrophotometer; `safety` cisplatin (PubChem GHS).
- **Figures.** F `oxygen-binding` (Mb and Hb saturation curves, the Hill
  plot, the shift with pH; test: θ(p₅₀) = ½, slope n at θ = ½); S haem side
  view: Fe out of plane (deoxy, HS) and in plane (oxy, LS) with the proximal
  histidine; S carbonic anhydrase cycle (chemfig, Zn–OH₂/Zn–OH, Book 3's
  cycle styles); S the Kok cycle S₀ → S₄; S cisplatin's 1,2-GG
  intrastrand cross-link (chemfig, schematic); P a horseshoe crab (Commons —
  verify) and/or a haemoglobin ribbon render from a PDB entry (Commons,
  licence to verify).
- **Ledger.** p₅₀ and n of Hb and Mb (open review in PMC, **at risk**, else
  problem data); M for CO (**at risk**, else problem data); Fe out-of-plane
  displacement in deoxy/oxy Hb computed from PDB coordinates (RCSB-PDB
  entries, **check**: a computed row citing the entries); haemoglobin
  concentration and molar mass (open source, **at risk**); WHO guideline
  values for Pb read-only (Book 3); GHS of cisplatin, EDTA (PubChem).
- **Exercises palette.** Hill coefficient from two saturations; O₂ delivered
  between lungs and tissues; CO poisoning with M; Irving–Williams ordering;
  hard/soft pairing predictions; Fe–S cluster mixed valence; electrons and
  photons for O₂ evolution; cisplatin aquation and binding sites; relaxivity
  calculation; chelator selectivity from pM.
- **Weekend problem — "How much oxygen does blood deliver?"** I Hill curves
  of Hb and Mb (problem or ledger p₅₀, n); saturations at 13 kPa and 5 kPa;
  II O₂ delivered per litre of blood (problem [Hb], four sites, molar mass);
  III the Bohr shift (problem p₅₀ at lower pH) and exercise; IV carbon
  monoxide at a given ppm with M (problem value): lost capacity. **Named
  number: litres of O₂ delivered per minute at rest for a cardiac output of
  5 L min⁻¹** (computed). 24 questions.

## Ch. 25 — Supramolecular Chemistry — `supramolecular`

- **Hook.** In 1962 Charles Pedersen found, by accident, a cyclic polyether
  that dissolved potassium permanganate in benzene, turning it purple: the
  ring wraps the K⁺ ion and hides its charge. Chemistry beyond the molecule
  began with that purple benzene.
- **Recall.** Year 1 volume: intermolecular forces, hydrogen bond, solvation,
  hydrophobic, complexes and formation constants, chelate; Year 2 volume:
  chemical potential, Gibbs energy, least-squares fitting;
  \cref{ch:b3:advanced-nmr} (fast exchange), \cref{ch:b3:rate-theories}
  (Eyring), \cref{ch:b3:partition-functions} (translational entropy).
- **Sections.** 1 Non-covalent interactions (ion–dipole, hydrogen bonds,
  π stacking, cation–π, halogen bonds, the hydrophobic effect; typical
  energies). 2 Molecular recognition (host, guest, complementarity,
  preorganisation; association constants; enthalpy–entropy compensation;
  the chelate and macrocyclic effects; crowns, cryptands and selectivity by
  size). 3 Measuring binding (NMR titration in fast exchange; UV–visible
  titration; Job's method; isothermal titration calorimetry; fitting the
  exact 1:1 isotherm). 4 Hosts (crown ethers, cryptands, cyclodextrins,
  calixarenes, cucurbiturils; applications). 5 Self-assembly and molecular
  machines (template synthesis of catenanes; rotaxanes; metal-directed cages;
  hydrogen-bonded networks; molecular switches and motors).
- **Definitions.** `def:b3:supramolecular:supramolecular` (supramolecular
  chemistry, host, guest, host–guest complex); `:recognition` (molecular
  recognition, complementarity, preorganisation); `:interactions` (π
  stacking, cation–π interaction, halogen bond, hydrophobic effect);
  `:macrocyclic` (chelate effect, macrocyclic effect); `:hosts` (crown ether,
  cryptand, cryptate, cyclodextrin, calixarene); `:itc` (isothermal titration
  calorimetry); `:job` (Job plot); `:template` (template synthesis);
  `:self-assembly` (self-assembly); `:interlocked` (mechanically interlocked
  molecule, rotaxane, catenane); `:machine` (molecular machine).
- **Ownership check.** Not in the map apart from the chapter. Book 2 owns
  *hydrogen bond*, *London/Keesom/Debye interaction*, *hydrophobic*,
  *complex*, *chelate*, *overall formation constant*: recalled (the
  association constant is "a formation constant in the Year 1 volume's
  sense"). *Chelate effect* is in no map nor harvest (Book 2 ch12 and Book 3
  ch18 do not define it): earliest need in this book is here; contested low
  (report point 2). *Hydrophobic effect* is a new phrase beside Book 2's
  adjective.
- **Statements.** `prop:…:fast-exchange` δ_obs = x_free δ_free + x_bound
  δ_bound (proof); `thm:…:isotherm` exact 1:1 bound fraction (proof: the
  quadratic); `prop:…:job` maximum at x = n/(n + m) for HₙGₘ (proof);
  `prop:…:chelate-entropy` the chelate effect is largely entropic (argued
  with translational entropy counts from ch10); `prop:…:compensation`
  (statement, established experimentally); `prop:…:itc` heat per injection
  (proof from the bound amount).
- **Methods.** `met:…:nmr-titration` (K from an NMR titration by nonlinear
  least squares); `met:…:job`; `met:…:itc` (reading an ITC isotherm).
- **Boxes.** `history` Pedersen, Lehn and Cram (1987 Nobel); Sauvage,
  Stoddart and Feringa (2016); `inthelab` an NMR titration; `safety` crown
  ethers (PubChem GHS: toxic).
- **Figures.** F `binding-titration` (NMR titration curves for K = 10², 10³,
  10⁴ L mol⁻¹; Job plots for 1:1 and 1:2; test: isotherm, x_max); S
  18-crown-6 with K⁺ (chemfig) and [2.2.2]cryptand with K⁺; S a
  cyclodextrin truncated cone with a guest; S Sauvage's copper(I) template
  synthesis of a catenane (TikZ rings); S rotaxane and catenane cartoons;
  P a molecular model or Pedersen portrait (Commons — verify; optional);
  AI none.
- **Ledger.** log K of K⁺ and Na⁺ with 18-crown-6 in methanol (open source,
  **at risk**: else problem data); cavity diameters (**at risk**, else no
  numbers); edta and ethylenediamine/ammonia constants for the chelate
  effect read-only from Book 2 (`logb:` rows) or new from NEA-TDB / IUPAC
  (if reachable); GHS of 18-crown-6, KMnO₄ (PubChem; Book 1/2 rows
  read-only).
- **Exercises palette.** Interaction types in given complexes; ΔG° from K;
  K⁺/Na⁺ selectivity from two K; Job plot reading; NMR titration fit; chelate
  versus monodentate K (Book 2 data); ITC → ΔH, ΔS; template logic; rotaxane
  shuttling barrier from coalescence (ch8) and Eyring (ch12); cyclodextrin
  solubilisation of a drug.
- **Weekend problem — "Purple benzene".** I K⁺ + 18-crown-6: the complex,
  its size match; II extraction of KMnO₄ into benzene with the crown (problem
  distribution constants): fraction extracted; III an NMR titration (problem
  data) → K by least squares, with its standard error; IV phase-transfer
  catalysis: why a catalytic amount suffices. **Named number: the fraction of
  permanganate extracted into the organic phase at the problem's crown
  concentration** (computed). 24 questions.

## Ch. 26 — Pericyclic Reactions — `pericyclic`

- **Hook.** Sunlight on skin opens a ring of 7-dehydrocholesterol in a
  fraction of a second; body heat then moves one hydrogen across seven atoms
  to give vitamin D₃. Two pericyclic steps, one photochemical and one
  thermal, each with a stereochemistry dictated by orbital symmetry.
- **Recall.** Year 2 volume: Hückel coefficients of polyenes, aromatic and
  antiaromatic, HOMO, LUMO, frontier orbitals, concerted reaction,
  Diels–Alder reaction, diene, dienophile, endo rule;
  \cref{ch:b3:point-groups} (C₂, σ), \cref{ch:b3:photochemistry} (excited
  states, [2+2] photocycloaddition), Year 1 volume: Z/E, CIP.
- **Sections.** 1 Four families (electrocyclic reactions, cycloadditions,
  sigmatropic rearrangements, cheletropic and ene reactions; [m+n] and
  [i,j] notations; supra- and antarafacial). 2 Electrocyclic reactions
  (conrotatory and disrotatory; the HOMO-terminus analysis; thermal 4n con,
  4n+2 dis; photochemical reversed; stereospecific products; the vitamin D
  ring opening). 3 Orbital correlation diagrams (symmetry elements kept along
  the path: C₂ for con, σ for dis; S/A classification; ground-state
  correlation and forbidden crossings; state correlation for the
  photochemical case). 4 Cycloadditions ([4+2] supra/supra allowed; [2+2]
  thermally forbidden suprafacially, photochemically allowed; ketenes and
  [π2s + π2a]; 1,3-dipolar cycloadditions). 5 Sigmatropic rearrangements and
  the general rule ([1,5]-H suprafacial, [1,7]-H antarafacial; [3,3] Cope and
  Claisen through chairs; the generalised Woodward–Hoffmann rule; aromatic
  Hückel and Möbius transition states).
- **Definitions.** `def:b3:pericyclic:pericyclic` (pericyclic reaction);
  `:families` (electrocyclic reaction, cycloaddition, sigmatropic
  rearrangement, cheletropic reaction, ene reaction); `:rotation-modes`
  (conrotatory, disrotatory); `:faciality` (suprafacial, antarafacial);
  `:orbital-correlation` (orbital correlation diagram); `:state-correlation`
  (state correlation diagram); `:dipolar` (1,3-dipole, 1,3-dipolar
  cycloaddition); `:cope-claisen` (Cope rearrangement, Claisen
  rearrangement); `:mobius` (aromatic transition state, Möbius transition
  state). Named statement: `thm:…:woodward-hoffmann` (Woodward–Hoffmann
  rules).
- **Ownership check.** Map/S2: Y3 owns *pericyclic reaction*, the
  Woodward–Hoffmann rules, *cycloaddition*, *electrocyclic*, *sigmatropic*;
  Book 3 owns *concerted reaction*, *Diels–Alder reaction*, *diene*,
  *dienophile*, *endo/exo adduct*, *endo rule*, *HOMO*, *LUMO*, *aromatic*,
  *Hückel's rule*: recalled. *Claisen rearrangement* differs from Book 3's
  *Claisen condensation* (different phrase). *Correlation diagram* (general)
  is ch18's; this chapter owns the longer phrases.
- **Statements.** `thm:…:electrocyclic` thermal 4n electrons conrotatory,
  4n + 2 disrotatory (proof from the signs of the HOMO's terminal
  coefficients, Hückel sine formula); `prop:…:photo-electrocyclic`
  reversal under light (proof with the singly occupied LUMO);
  `prop:…:correlation` conservation of orbital symmetry along a C₂ or σ
  path (argued, ground state); `thm:…:cycloaddition` [m + n] supra/supra
  thermally allowed iff m + n = 4q + 2 (proof from the HOMO–LUMO phases);
  `prop:…:sigmatropic-h` [1,j]-H shifts (proof by the same analysis);
  `thm:…:woodward-hoffmann` a thermal pericyclic reaction is allowed iff the
  number of (4q+2)_s and (4r)_a components is odd (partial proof: consistent
  with all cases above; general proof treated in more advanced courses);
  `prop:…:aromatic-ts` Hückel TS aromatic with 4n + 2, Möbius with 4n
  electrons (argued, equivalent to the rule).
- **Methods.** `met:…:components` (drawing components and counting them);
  `met:…:predict-stereo` (stereochemistry of an electrocyclic or [3,3]
  product); `met:…:correlation-diagram` (building one).
- **Boxes.** `history` Woodward and Hoffmann (1965), Fukui; `inthelab` a
  Claisen rearrangement under reflux in a high-boiling solvent; `safety`
  1,3-butadiene (PubChem GHS).
- **Figures.** F `polyene-mo` (Hückel coefficients of ethene, allyl,
  butadiene, hexatriene, used to scale lobes in the S figures; test: signs,
  node counts, C₂/σ parities); S conrotatory and disrotatory closures of
  butadiene and hexatriene with HOMO lobes (Book 3's `omp` pic); S orbital
  correlation diagram butadiene ⇄ cyclobutene for the dis (σ) and con (C₂)
  paths, two panels (Book 3's `omlevel`/`omcorr`, S/A labels); S [4+2] and
  [2+2] supra/supra phase matching; S Cope and Claisen chair transition
  states (chemfig); S the vitamin D sequence: 7-DHC → previtamin D₃ (hν,
  conrotatory) → vitamin D₃ ([1,7]-H, antarafacial); AI a person in sunlight
  on a terrace (everyday).
- **Ledger.** Little: structures of 7-dehydrocholesterol, previtamin D₃,
  vitamin D₃ (PubChem); a Cope or Claisen activation barrier only as problem
  data; GHS of butadiene (PubChem).
- **Exercises palette.** Classify a dozen reactions; predict con/dis and the
  product of trans-3,4-dimethylcyclobutene; photochemical hexatriene closure;
  build the hexatriene correlation diagram; [4+2] versus [2+2]; [3,3] stereo
  through a chair; [1,5]-H shifts in substituted cyclopentadienes; count
  components (ketene + alkene); Möbius counting for an 8-electron TS;
  1,3-dipolar regiochemistry from FMO coefficients.
- **Weekend problem — "Sunlight, skin and vitamin D".** I the photochemical
  6π ring opening of 7-dehydrocholesterol: conrotatory, the Z geometry of
  previtamin D₃; II the thermal [1,7]-H shift: antarafacial, allowed (count
  the components); III side photoproducts by conrotatory re-closure in the
  other sense and by E/Z isomerisation; IV kinetics of the thermal step
  (problem k) and the time to convert 90 % at 37 °C. **Named number: the
  time to convert 90 % of previtamin D₃ at body temperature** (computed
  from the problem's first-order rate constant). 24 questions.

## Ch. 27 — Radicals, Carbenes and Rearrangements — `radicals-carbenes`

- **Hook.** The pyrethrum daisy makes insecticides with a three-membered
  ring; chemists make the same cyclopropanes in one step with a carbene, a
  carbon that has only six electrons.
- **Recall.** Year 1 volume: radical, homolysis, half-headed arrow,
  carbocation, carbocation rearrangement, nucleophile, leaving group; Year 2
  volume: initiation, propagation, termination, radical initiator, peroxy
  acid, lactone, lactam, imine, oxime-like condensations;
  \cref{ch:b3:complex-kinetics} (chain reactions),
  \cref{ch:b3:organometallic-bonding} (carbenes as ligands),
  \cref{ch:b3:many-electron-atoms} (singlet and triplet),
  \cref{ch:b3:rate-theories} (Hammond and selectivity).
- **Sections.** 1 Radical chain reactions in synthesis (radical structure
  and stability from computed bond dissociation enthalpies; selectivity of
  chlorination versus bromination; tin hydride and silane chains:
  dehalogenation, Barton–McCombie deoxygenation; anti-Markovnikov HBr
  addition). 2 Radical cyclisations (5-exo preference; Baldwin's rules; the
  radical clock and competition kinetics). 3 Carbenes (singlet and triplet
  ground states; generation from diazo compounds, by α-elimination
  (dichlorocarbene) and as carbenoids (Simmons–Smith); stereospecific
  cyclopropanation by singlets and the Skell test; C–H insertion; rhodium
  carbenoids). 4 Rearrangements to electron-deficient carbon (Wagner–Meerwein
  shifts, the pinacol rearrangement, migratory aptitude). 5 Rearrangements to
  electron-deficient N and O (Beckmann and caprolactam; Baeyer–Villiger
  regiochemistry and retention; Hofmann and Curtius through isocyanates;
  Wolff through a ketene; nitrenes).
- **Definitions.** `def:b3:radicals-carbenes:radical-clock` (radical
  clock); `:cyclisation` (exo cyclisation, endo cyclisation);
  `:carbene-states` (singlet carbene, triplet carbene); `:carbenoid`
  (carbenoid); `:cyclopropanation` (cyclopropanation); `:nitrene` (nitrene);
  `:shift` (1,2-shift); `:pinacol` (pinacol rearrangement); `:migratory`
  (migratory aptitude); `:beckmann` (Beckmann rearrangement); `:baeyer`
  (Baeyer–Villiger oxidation); `:curtius` (isocyanate, Curtius
  rearrangement, Hofmann rearrangement); `:wolff` (ketene, Wolff
  rearrangement). Named statement: `prop:…:baldwin` (Baldwin's rules).
- **Ownership check.** S2: Book 3 owns *initiation*, *propagation*,
  *termination*, *radical initiator*, *kinetic chain length*; this chapter
  keeps the radical terms specific to synthesis (*radical clock*, exo/endo
  cyclisation). Book 2 owns *radical*, *homolysis*, *half-headed arrow*,
  *carbocation rearrangement*: recalled (the 1,2-shift is the mechanism of
  Book 2's rearrangement, named here). Book 3 owns *peroxy acid*, *lactone*,
  *lactam*, *imine*, *endo adduct*/*endo rule* (Diels–Alder): "endo" here is
  only in the phrases *exo/endo cyclisation*. *Carbene* is ch20's
  (recalled). *Ketene* and *isocyanate* are in no map or harvest: earliest
  need here.
- **Statements.** `prop:…:bde` bond dissociation enthalpies of C–H bonds
  from enthalpies of formation of radicals (computed, sourced);
  `prop:…:halogenation-selectivity` relative rates from ΔBDE and the
  Hammond postulate (argued, computed ratios); `prop:…:clock` product ratio
  [cyclised]/[direct] = k_c/(k_H[R₃SnH]) (proof); `prop:…:baldwin` (statement
  with its stereoelectronic rationale; established experimentally);
  `prop:…:skell` singlet carbenes add stereospecifically, triplets do not
  (argued); `prop:…:beckmann-anti` the group anti to the leaving group
  migrates (argued); `prop:…:bv-retention` migration with retention and
  aptitude tertiary > secondary ≈ aryl > primary > methyl (argued,
  established experimentally).
- **Methods.** `met:…:radical-chain` (designing a tin-free radical reduction
  or cyclisation: concentrations, initiator, temperature);
  `met:…:rearrangement` (predicting the product of a rearrangement).
- **Boxes.** `history` Gomberg's triphenylmethyl radical (1900) and the
  caprolactam route to nylon-6; `inthelab` slow addition by syringe pump to
  keep a reagent's concentration low; `safety` tributyltin hydride and
  diazomethane (PubChem GHS; diazomethane described, never as a procedure).
- **Figures.** S the tin-hydride dehalogenation chain (chemfig with
  half-headed `\chemmove` arrows); S 5-exo versus 6-endo transition states
  of the 5-hexenyl radical; S singlet and triplet carbene orbital occupations
  (sp² and p boxes, `\omorbs`); S Skell's stereochemical test (chemfig); S
  Beckmann and Baeyer–Villiger mechanisms (chemfig, `\chemmove`); F
  `radical-clock` (product ratio versus [Bu₃SnH] and the linear inverse plot;
  test: slope k_H/k_c); F `bde` (C–H BDEs of methane, ethane, propane (2°),
  isobutane (3°), toluene computed from WebBook enthalpies of formation, as
  a table/bar chart; test: values equal the formula); P pyrethrum daisies
  (Commons — verify); AI none.
- **Ledger.** Gas-phase ΔfH° of CH₃•, C₂H₅•, i-C₃H₇•, t-C₄H₉•, PhCH₂•, H• and
  the parent alkanes (WebBook / JANAF / CODATA-KEY, Book 3 rows read-only
  where present); 5-hexenyl cyclisation rate constant (**at risk**, else
  problem data); caprolactam production (**at risk**, else not printed);
  GHS of Bu₃SnH, AIBN, mCPBA (PubChem).
- **Exercises palette.** Monochlorination and monobromination ratios of
  propane and isobutane; a tin-hydride reduction plan; radical-clock
  computation; Baldwin classification of six ring closures; carbene spin
  and stereochemistry; Simmons–Smith product; pinacol product and migratory
  aptitude; Beckmann products of the two oximes of 2-methylcyclohexanone;
  Baeyer–Villiger of cyclohexanone and of acetophenone; Curtius to an amine
  and to a carbamate.
- **Weekend problem — "Two rings from cyclohexanone".** I the oxime, its E/Z
  isomers; II the Beckmann rearrangement to caprolactam (anti migration,
  ring expansion), balanced; III the Baeyer–Villiger oxidation to
  ε-caprolactone, mechanism and retention; IV 2-methylcyclohexanone in both
  rearrangements: regiochemistry by migratory aptitude versus by oxime
  geometry. **Named number: the mass of caprolactam from one tonne of
  cyclohexanone at the problem's step yields** (computed with
  `tools/molar_mass.py`). 25 questions.

## Ch. 28 — Asymmetric Synthesis — `asymmetric-synthesis`

- **Hook.** L-DOPA, used against Parkinson's disease, was the first drug made
  on an industrial scale by asymmetric catalysis (1970s): a few milligrams of
  a chiral rhodium complex make kilograms of one enantiomer.
- **Recall.** Year 1 volume: chirality, enantiomers, diastereomers, racemic
  mixture, specific rotation, CIP rules, stereoselective and stereospecific
  reactions; Year 2 volume: catalytic hydrogenation, epoxidation,
  dihydroxylation, imines, enamines, enolates, aldol, Robinson annulation,
  chromatography; \cref{ch:b3:rate-theories} (Eyring),
  \cref{ch:b3:homogeneous-catalysis} (Wilkinson's cycle),
  \cref{ch:b3:point-groups} (C₂).
- **Sections.** 1 Measuring enantiopurity (ee, er, de; optical purity and
  its pitfalls; chiral chromatography; NMR with chiral solvating agents and
  Mosher esters). 2 Topicity and stereoselective additions (homotopic,
  enantiotopic, diastereotopic groups and faces; Re and Si faces; the
  Felkin–Anh model and chelation control). 3 Strategies (chiral pool; chiral
  auxiliaries (Evans); resolution of racemates; kinetic resolution and its
  selectivity; dynamic kinetic resolution). 4 Asymmetric catalysis with
  metals (er from ΔΔG‡; C₂-symmetric ligands; Knowles and Noyori
  hydrogenations; Sharpless epoxidation of allylic alcohols and
  dihydroxylation; non-linear effects in outline). 5 Organocatalysis
  (enamine and iminium activation; the proline-catalysed aldol and the
  Hajos–Parrish/Wieland–Miescher ketone; chiral Brønsted acids).
- **Definitions.** `def:b3:asymmetric-synthesis:ee` (enantiomeric excess,
  enantiomeric ratio, diastereomeric excess, optical purity);
  `:selective` (enantioselective reaction, diastereoselective reaction);
  `:topicity` (homotopic, enantiotopic, diastereotopic); `:faces`
  (prochiral, Re face, Si face); `:felkin` (Felkin–Anh model, chelation
  control); `:chiral-pool` (chiral pool); `:auxiliary` (chiral auxiliary);
  `:resolution` (resolution of a racemate, kinetic resolution, dynamic
  kinetic resolution); `:asymmetric-catalysis` (asymmetric catalysis, chiral
  ligand); `:sharpless` (Sharpless epoxidation); `:organocatalysis`
  (organocatalysis, enamine catalysis, iminium catalysis). Named statement:
  `thm:…:kagan` (Kagan equation).
- **Ownership check.** Map: Y1 owns stereochemistry, Y3 recalls it in
  `asymmetric-synthesis`. Book 2 owns *chiral*, *enantiomers*,
  *diastereomers*, *racemic mixture*, *specific rotation*, *stereoselective*,
  *stereospecific*; Book 3 owns *catalytic hydrogenation*, *epoxidation*,
  *dihydroxylation*, *imine*, *enamine*, *enolate*, *aldol*, *resolution*
  (chromatographic), *selectivity factor* (chromatographic): recalled. The
  kinetic-resolution ratio s is introduced inside the definition of
  *kinetic resolution* without its own index (Book 3's "selectivity
  factor" is a different notion). Batch note: Book 2 avoided *enantiomeric
  excess* for Year 3 — it is defined here.
- **Statements.** `prop:…:ee-er` ee = (er − 1)/(er + 1) (proof);
  `thm:…:er-ddg` er = exp(ΔΔG‡/RT) for two competing paths with equal
  prefactors (proof from Eyring); `thm:…:kagan` s = ln[(1 − c)(1 − ee)]/
  ln[(1 − c)(1 + ee)] (proof from two first-order consumptions);
  `prop:…:dkr` yield → 100 % when racemisation is fast (proof);
  `prop:…:felkin` (model, `\admitted`, established experimentally);
  `prop:…:c2` a C₂-symmetric catalyst halves the number of diastereomeric
  transition states to consider (proof by the symmetry operation).
- **Methods.** `met:…:ee-chromatogram` (ee from peak areas, with response
  factor); `met:…:re-si` (assigning Re/Si faces); `met:…:mosher` (configuration
  from Mosher ester shifts, outline); `met:…:strategy` (choosing pool,
  auxiliary, resolution or catalysis).
- **Boxes.** `history` Knowles, Noyori, Sharpless (2001) and List,
  MacMillan (2021); `inthelab` a chiral HPLC analysis; `safety` tert-butyl
  hydroperoxide (PubChem GHS).
- **Figures.** F `kinetic-resolution` (ee of recovered substrate and of
  product versus conversion for s = 2, 10, 50; test: Kagan equation, ee →
  100 % at high conversion); F `er-ddg` (ee versus ΔΔG‡ at −78, 0 and 25 °C;
  part b: a chiral chromatogram synthesised from two peaks; test: er =
  exp(ΔΔG‡/RT), areas → ee); S Re and Si faces of acetophenone (chemfig/3D);
  S Felkin–Anh Newman projection (Book 2's `omnewman`) with the nucleophile's
  Bürgi–Dunitz approach; S Sharpless mnemonic square; S proline enamine aldol
  transition state (chemfig); AI an active-pharmaceutical-ingredient plant
  (industrial).
- **Ledger.** L-DOPA process ee and date (open review / Nobel lecture of
  Knowles, NOBEL, **check**); specific rotation of one compound for an
  optical-purity exercise (PubChem, **at risk**); Sharpless ee typical (**at
  risk**, else problem data); GHS of TBHP, Ti(OiPr)₄ (PubChem).
- **Exercises palette.** ee ↔ er ↔ ΔΔG‡ conversions; ee from HPLC areas; the
  ΔΔG‡ needed for 99 % ee at −78 and 25 °C; Re/Si assignments; diastereotopic
  protons in an NMR spectrum; Felkin–Anh product; Evans auxiliary alkylation
  product; s from a resolution experiment; Sharpless product prediction
  with each tartrate; a proline aldol step.
- **Weekend problem — "The L-DOPA route".** I the prochiral enamide, its
  faces and the (S)-amino acid formed; II ee 95 % at 25 °C → ΔΔG‡; III
  recrystallisation raising the ee (problem solubilities); IV the
  alternative by kinetic resolution: the s needed for 95 % ee of the
  remaining substrate at 55 % conversion, and its yield ceiling. **Named
  number: ΔΔG‡ = RT ln 39 ≈ 9.1 kJ mol⁻¹ for 95 % ee at 25 °C** (computed).
  24 questions.

## Ch. 29 — Heterocyclic Chemistry — `heterocycles`

- **Hook.** A cup of coffee holds caffeine (two fused nitrogen rings), its
  aroma dozens of furans, pyrazines and pyrroles; most of the drugs on a
  pharmacy shelf contain at least one ring with a nitrogen in it.
- **Recall.** Year 2 volume: aromatic, Hückel's rule, arene, electrophilic
  aromatic substitution, Wheland intermediate, activating and directing
  groups, amines and their basicity, imines, enamines, tautomers,
  nucleobases; Year 1 volume: pKa, nucleophile, electrophile, leaving group;
  \cref{ch:b3:pericyclic} ([3,3] for the Fischer synthesis).
- **Sections.** 1 Aromatic heterocycles (pyridine: an in-plane lone pair, a
  π-deficient ring; pyrrole: the lone pair in the π system, a π-excessive
  ring; furan, thiophene; dipoles and basicities; ¹H NMR shifts). 2 Pyridine
  (electrophilic substitution, difficult and at C3; N-oxides; nucleophilic
  aromatic substitution at C2/C4 and the Chichibabin reaction; pyridine and
  DMAP as bases, nucleophiles and ligands). 3 Five-membered rings
  (electrophilic substitution at C2; relative reactivities; acylation,
  Vilsmeier formylation; furan as a Diels–Alder diene; lithiation at C2).
  4 Fused and biological heterocycles (indole and C3; quinoline; purines and
  pyrimidines, their tautomers and base pairing). 5 Making rings (Paal–Knorr,
  Hantzsch pyridine, Fischer indole; heterocycles in drugs; bioisosteres).
- **Definitions.** `def:b3:heterocycles:heterocycle` (heterocycle,
  heteroaromatic compound); `:pi-character` (π-excessive heterocycle,
  π-deficient heterocycle); `:snar` (nucleophilic aromatic substitution,
  Meisenheimer complex); `:chichibabin` (Chichibabin reaction); `:n-oxide`
  (pyridine N-oxide); `:paal-knorr` (Paal–Knorr synthesis); `:hantzsch`
  (Hantzsch pyridine synthesis); `:fischer-indole` (Fischer indole
  synthesis); `:bioisostere` (bioisostere).
- **Ownership check.** Not in the map apart from the chapter (Book 3 ch23
  points pyridine basicity here). Book 3 owns *aromatic*, *arene*, *SEAr*,
  *Wheland intermediate*, directing-group terms, amine classes, *imine*,
  *enamine*, *tautomers*, *nucleobase*: recalled. *Nucleophilic aromatic
  substitution* and *Meisenheimer complex* are in no map nor harvest
  (Book 3 ch22–23 do not define them): earliest need here.
- **Statements.** `prop:…:sextet` six π electrons in pyridine, pyrrole,
  furan, thiophene, imidazole (proof by counting with Hückel's rule);
  `prop:…:basicity` pyridine ≫ pyrrole, and pyrrole protonates on carbon
  (argued with ledger pKa values); `prop:…:pyrrole-c2` attack at C2 gives a
  cation with three resonance structures, at C3 two (proof by drawing);
  `prop:…:pyridine-c3` SEAr at C3 avoids a sextet nitrogen cation (proof);
  `prop:…:snar-positions` SNAr at C2/C4 puts the negative charge on N (proof);
  `prop:…:snar-mechanism` addition–elimination (argued; rate law).
- **Methods.** `met:…:site` (predicting the site of attack on a heterocycle);
  `met:…:disconnect` (disconnecting a heterocycle to its classical synthesis,
  Book 3's retrosynthesis recalled).
- **Boxes.** `history` Fischer's indole synthesis (1883) and Hantzsch (1881);
  `inthelab` a Paal–Knorr pyrrole synthesis with a Dean–Stark trap (Book 2's
  pic); `safety` pyridine and phenylhydrazine (PubChem GHS).
- **Figures.** S π systems of pyridine and pyrrole with the lone pairs (Book
  3's `omp` pic); S resonance structures of the C2 and C3 Wheland cations of
  pyrrole and of pyridine (chemfig); S SNAr on 2-chloropyridine and the
  Chichibabin mechanism (chemfig, `\chemmove`); S Paal–Knorr and Fischer
  indole mechanisms (chemfig, the [3,3] step marked); S a purine–pyrimidine
  base pair (chemfig with hydrogen bonds); F `heterocycle-nmr` (synthetic ¹H
  spectra of pyridine, pyrrole and furan at ledger shifts; test: positions
  and 2:1:2 / 2:2 integrals); AI a cup of coffee with roasted beans
  (everyday).
- **Ledger.** pKa of pyridinium, pyrrolium (C-protonated), imidazolium,
  piperidinium, DMAP-H⁺ (IUPAC-PKA, Book 2 rows read-only where present);
  dipole moments of pyridine, pyrrole, furan, thiophene (NSRDS-NBS10); ¹H
  shifts of pyridine, pyrrole, furan, thiophene (NMRShiftDB / SDBS);
  structures of caffeine, nicotine, sumatriptan (PubChem); GHS of pyridine,
  phenylhydrazine (PubChem).
- **Exercises palette.** π-electron counts of oxazole, thiazole, pyrimidine,
  purine; basicity ranking with ledger pKa; site of SEAr on pyrrole, furan,
  indole, pyridine N-oxide; SNAr on 2- and 3-chloropyridine; Chichibabin
  product; Paal–Knorr products of hexane-2,5-dione with three reagents;
  Hantzsch components of a dihydropyridine drug; Fischer indole
  regiochemistry with butanone; 2-hydroxypyridine/2-pyridone tautomerism.
- **Weekend problem — "Building an indole".** I the phenylhydrazone of
  acetone; II the ene-hydrazine tautomer and the [3,3] step (allowed, chair);
  III rearomatisation, loss of NH₃, the balanced equation; IV butanone: two
  ene-hydrazines, two indoles, which dominates under acid. **Named number:
  the theoretical mass of 2-methylindole from 10.0 g of phenylhydrazine**
  (computed). 24 questions.

## Ch. 30 — Total Synthesis: Strategy and Classic Routes — `total-synthesis`

- **Hook.** The anticancer drug paclitaxel was first isolated from the bark
  of the Pacific yew; stripping enough bark for one patient took several
  trees. Synthesis — total, then partial from a renewable precursor — is how
  such molecules reach patients.
- **Recall.** Year 2 volume: retrosynthetic analysis, target molecule,
  disconnection, synthon, synthetic equivalent, functional-group
  interconversion, orthogonal protecting groups, aldol, Robinson annulation,
  Wittig reaction, Mannich-type iminium chemistry; Year 1 volume:
  protecting group, yield; \cref{ch:b3:asymmetric-synthesis},
  \cref{ch:b3:pericyclic}, \cref{ch:b3:homogeneous-catalysis}.
- **Sections.** 1 Measuring a synthesis (overall yield as a product;
  linear versus convergent; the longest linear sequence; step, atom and redox
  economy; ideality). 2 Protecting groups and their economy (orthogonality
  recalled; the cost of each protection; protecting-group-free syntheses).
  3 Strategic bonds and key ring-forming steps (Diels–Alder, Robinson
  annulation, metathesis, cascades; biomimetic polyene cyclisation).
  4 Landmark routes analysed (Robinson's tropinone, 1917; Corey's
  prostaglandin F₂α through the Corey lactone, 1969; oseltamivir from
  shikimic acid, a chiral-pool industrial route). 5 From discovery to process
  (route scouting, safety, cost, scale; the bridge to
  \cref{ch:b3:green-industrial}).
- **Definitions.** `def:b3:total-synthesis:total` (total synthesis, formal
  synthesis, semisynthesis); `:architecture` (linear synthesis, convergent
  synthesis, longest linear sequence, overall yield); `:economy` (step
  economy, protecting-group economy, ideality); `:cascade` (cascade
  reaction); `:biomimetic` (biomimetic synthesis); `:mannich` (Mannich
  reaction); `:strategic-bond` (strategic bond).
- **Ownership check.** S2: Book 3 owns *orthogonal protecting groups*; Book 4
  ch30 keeps *convergent/linear synthesis*, *protecting-group economy*. Book 3
  owns *retrosynthetic analysis*, *disconnection*, *synthon*, *synthetic
  equivalent*, *FGI*, *target molecule*, *annulation*, *Robinson annulation*,
  *decarboxylation*; Book 2 owns *yield*, *protecting group*: recalled.
  *Mannich reaction* and *strategic bond* are in no map nor harvest (checked
  in Book 3's DEFINITIONS): earliest need here; contested low.
- **Statements.** `prop:…:overall-yield` Y = ∏yᵢ (proof); `prop:…:convergent`
  a convergent route of n steps in two equal branches loses fewer
  yield-factors than a linear one (proof, with numbers); `prop:…:ideality`
  (definition-based ratio, computed for the routes); `prop:…:tropinone`
  the one-pot route as two Mannich reactions and a decarboxylation (argued,
  balanced equation gated).
- **Methods.** `met:…:analyse` (how to read a total synthesis: target,
  disconnections, LLS, key steps, stereocontrol, protecting groups);
  `met:…:count` (counting steps and the LLS from a scheme).
- **Boxes.** `history` Robinson (1917) and Woodward's era; Corey's
  retrosynthetic analysis (1990 Nobel); `inthelab` scaling a step from 1 g to
  1 kg; `safety` sodium azide (PubChem GHS: why azide-free oseltamivir routes
  were sought).
- **Figures.** S Robinson's tropinone synthesis (chemfig, one pot); S Corey's
  prostaglandin retrosynthesis with `omretro` arrows (Book 3's style) and the
  forward key steps; S linear versus convergent trees (TikZ); F
  `overall-yield` (overall yield versus number of steps for 80, 90, 95 % per
  step, linear and convergent; test: product law); S oseltamivir from
  shikimic acid (chemfig, key steps only); P Pacific yew (Commons — verify);
  AI none.
- **Ledger.** Historical facts from Nobel lectures (NOBEL: Robinson 1947,
  Corey 1990) and the original papers' metadata (DOIs); tropinone yields
  (Robinson and later Schöpf: **at risk**, else not printed); paclitaxel
  supply facts (open review, **at risk**); shikimic acid source (open
  review, **check**); GHS of NaN₃ (PubChem).
- **Exercises palette.** Overall yield of 10- and 20-step routes; LLS of a
  given scheme; designing a convergent split; choosing protecting groups for
  a triol (Book 3's orthogonality); identifying strategic bonds; the
  tropinone mechanism step by step; polyene cyclisation stereochemistry
  through chairs; ideality of two routes; cost of a protecting-group pair;
  semisynthesis versus total synthesis for a natural product.
- **Weekend problem — "Tropinone in one pot".** I the three components
  (succinaldehyde, methylamine, acetonedicarboxylic acid) and the balanced
  equation (CO₂ and H₂O released); II the mechanism: iminium, two Mannich
  reactions, two decarboxylations; III comparison with a long linear route
  (problem step yields) → overall yields; IV stereochemistry: tropinone is
  achiral (C_s), its reduction to tropine and pseudotropine.
  **Named number: the ratio of the one-pot yield to the linear route's
  overall yield** (computed from the problem data). 24 questions.

## Ch. 31 — Green Chemistry and Industrial Processes — `green-industrial`

- **Hook.** Ibuprofen used to be made in six steps that threw away more mass
  than they kept; since 1992 a three-step catalytic route turns most of the
  atoms it uses into the product, and its by-product is recovered.
- **Recall.** Book 1 (grade 12): atom economy and green chemistry at school
  level (re-founded here); Year 1 volume: yield; Year 2 volume: reactors,
  conversion, selectivity, residence time, single-pass conversion, recycle,
  purge, adiabatic temperature rise, electrolysers, fuel cells;
  \cref{ch:b3:surfaces-catalysis}, \cref{ch:b3:homogeneous-catalysis},
  \cref{ch:b3:total-synthesis}.
- **Sections.** 1 Measuring greenness (the twelve principles; atom economy;
  E-factor, process mass intensity, reaction mass efficiency and their
  relations; complete versus simple E-factors). 2 Solvents and energy
  (solvent selection guides; water, supercritical CO₂, solvent-free;
  catalysis versus stoichiometric reagents; process intensification and flow
  chemistry). 3 Life-cycle thinking (goal and scope, functional unit, system
  boundary, inventory, impact categories; cradle-to-gate; carbon footprint;
  trade-offs). 4 Major processes and their improvement (ammonia and its
  hydrogen; sulfuric acid as an energy exporter; ethylene oxide by direct
  oxidation versus chlorohydrin; propylene oxide with hydrogen peroxide;
  adipic acid and N₂O abatement; ibuprofen, old and new). 5 Renewable
  feedstocks and biocatalysis (platform molecules from biomass;
  enzymatic steps in drug manufacture; CO₂ as a feedstock: urea and
  methanol; chemical recycling of PET).
- **Definitions.** `def:b3:green-industrial:green-chemistry` (green
  chemistry); `:atom-economy` (atom economy); `:e-factor` (E-factor);
  `:pmi` (process mass intensity); `:rme` (reaction mass efficiency); `:lca`
  (life-cycle assessment, functional unit, system boundary, cradle-to-gate
  assessment); `:carbon-footprint` (carbon footprint); `:intensification`
  (process intensification); `:biocatalysis` (biocatalysis); `:feedstock`
  (renewable feedstock, platform molecule).
- **Ownership check.** Map: Y3 owns green-chemistry metrics, **re-founding**
  Book 1 g12's *atom economy* and *green chemistry*; seed: *E-factor*,
  *life-cycle assessment*. Book 3 owns *conversion*, *selectivity*,
  *residence time*, *reactor* types, *recycle*, *purge*, *single-pass
  conversion*, *thermal runaway*, *electrolyser*, *fuel cell*; Book 2 owns
  *yield*: recalled.
- **Statements.** `prop:…:ae-classes` additions and rearrangements have
  AE = 100 %, substitutions and eliminations less (proof);
  `prop:…:pmi-e` PMI = E + 1 (proof); `prop:…:rme` RME = AE × yield ×
  (stoichiometric factor)⁻¹ (proof); `prop:…:smr` CO₂ per tonne of NH₃ from
  steam-methane reforming stoichiometry (computed, proof by mass balance).
- **Methods.** `met:…:metrics` (computing AE, E, PMI, RME for a route);
  `met:…:solvent-choice` (using a selection guide); `met:…:lca` (setting up
  a comparative LCA).
- **Boxes.** `history` Anastas and Warner's twelve principles (1998) and
  Sheldon's E-factor (1992); `inthelab` replacing dichloromethane in a
  work-up; `safety` ethylene oxide (PubChem GHS).
- **Figures.** F `green-metrics` (AE and E-factor bars of the two ibuprofen
  routes and the two ethylene-oxide routes, computed from
  `tools/molar_mass.py` values; test: AE equals the formula for each
  balanced route); S block flow schemes of the two ibuprofen routes
  (chemfig); S LCA stages and system boundary (TikZ); S ammonia synthesis
  loop with recycle and purge (Book 3's words); AI a modern chemical plant
  (industrial).
- **Ledger.** E-factors by industry sector (Sheldon, open-access paper,
  **check**); ammonia production (USGS-MCS, Book 2 row read-only if present)
  and energy/CO₂ intensity (IEA ammonia roadmap, **check**); solvent-guide
  classes (CHEM21, open access, **check**); GHS of EO, DCM, 2-MeTHF
  (PubChem); world PET and adipic acid figures (**at risk**, else not
  printed).
- **Exercises palette.** AE of named reactions (Diels–Alder, Wittig,
  Gabriel, esterification); E-factor and PMI from a batch record; RME;
  comparing two routes; solvent choice; LCA functional unit for a detergent;
  CO₂ per tonne NH₃ from SMR; AE of EO routes; N₂O from adipic acid per
  tonne; green hydrogen electrolysis energy (Book 3 recalled).
- **Weekend problem — "Ibuprofen: six steps or three?"** I atom economies
  of the two routes (balanced equations, computed molar masses); II
  E-factors with the problem's yields and solvent masses; III the catalysts
  (HF recycled, hydrogenation, palladium carbonylation) and what they change;
  IV waste avoided per year for a given output (problem data). **Named
  number: the atom economy of the three-step route, ≈ 77 %** (computed;
  ≈ 40 % for the six-step route). 24 questions.

## Ch. 32 — Environmental Chemistry and Toxicology — `environmental-toxicology`

- **Hook.** Every summer a satellite photographs green swirls on a large
  lake: an algal bloom fed by phosphate and nitrate from fields and towns,
  which will use up the water's oxygen as it decays.
- **Recall.** Year 1 volume: acid–base, precipitation, complexation, E–pH
  diagrams, partition coefficient, half-life, hazard, risk, GHS; Book 1
  (grade 8): greenhouse gases (re-founded here); Year 2 volume: Henry's law,
  Henry constant, ionic strength, statistics, mass spectrometry and atomic
  spectrometry; \cref{ch:b3:photochemistry} (atmospheric photochemistry),
  \cref{ch:b3:group-theory-applied} and \cref{ch:b3:rovibrational-
  spectroscopy} (IR activity), \cref{ch:b3:surfaces-catalysis} (adsorption).
- **Sections.** 1 The atmosphere (greenhouse gases: why CO₂, CH₄, N₂O and
  H₂O absorb in the infrared and N₂, O₂ do not; global warming potential and
  lifetimes; tropospheric pollutants: NOₓ, SO₂, VOCs, particulate matter;
  acid rain; the pH of clean rain). 2 Natural waters (the carbonate system
  and alkalinity; ocean acidification and carbonate saturation; hardness;
  dissolved oxygen, BOD and COD; eutrophication and the Redfield ratio; metal
  speciation, mercury and arsenic). 3 Soils and sediments (cation exchange
  capacity; sorption of metals and organics, K_d and K_oc; leaching).
  4 Fate of pollutants (partitioning between air, water, soil and biota:
  K_ow, Henry constant, K_oc; bioconcentration, bioaccumulation,
  biomagnification; persistence; persistent organic pollutants; a level-I
  mass balance). 5 Toxicology and regulation (dose–response; LD₅₀, EC₅₀,
  NOAEL, LOAEL; acute and chronic; threshold and non-threshold effects;
  ecotoxicology, PNEC and PEC, the risk quotient; occupational exposure
  limits; registration of chemicals in general terms, no jurisdiction named).
- **Definitions.** `def:b3:environmental-toxicology:greenhouse`
  (greenhouse gas, global warming potential); `:pollutants` (particulate
  matter, acid rain); `:alkalinity` (alkalinity); `:acidification` (ocean
  acidification, saturation state); `:hardness` (water hardness); `:oxygen-
  demand` (biochemical oxygen demand, chemical oxygen demand);
  `:eutrophication` (eutrophication); `:speciation` (chemical speciation);
  `:soil` (cation exchange capacity, soil–water distribution coefficient,
  organic-carbon partition coefficient); `:kow` (octanol–water partition
  coefficient); `:bio` (bioconcentration factor, bioaccumulation,
  biomagnification); `:pop` (persistent organic pollutant); `:dose`
  (dose–response relationship, median lethal dose, median effective
  concentration, no-observed-adverse-effect level, lowest-observed-adverse-
  effect level); `:toxicity` (acute toxicity, chronic toxicity);
  `:ecotoxicology` (ecotoxicology, predicted no-effect concentration,
  predicted environmental concentration, risk quotient); `:oel`
  (occupational exposure limit).
- **Ownership check.** *Greenhouse gas* **re-founds** Book 1 (g8); Books 2–3
  did not define it. Book 2 owns *partition coefficient*, *half-life*,
  *hazard*, *risk*, *safety data sheet*; Book 3 owns *Henry's law*, *Henry
  constant*, *mass spectrometry*, *atomic absorption spectrometry*,
  *inductively coupled plasma*, *limit of detection*: recalled. K_ow and K_oc
  are specific named coefficients (phrases), contested low with Book 2's
  generic *partition coefficient*.
- **Statements.** `prop:…:rain-ph` pH ≈ 5.6 for rain in equilibrium with
  today's CO₂ (proof with Henry and Ka₁; computed from ledger values);
  `prop:…:carbonate-fractions` (proof); `prop:…:alkalinity` (proof of the
  charge-balance form); `prop:…:bod` BOD_t = L₀(1 − e^{−kt}) (proof);
  `prop:…:level-one` equilibrium distribution among compartments (proof by
  mass balance with partition coefficients); `prop:…:bcf-kow` log BCF linear
  in log K_ow (empirical, `\admitted`; regression shown);
  `prop:…:dose-response` log-logistic model and its EC₅₀ (definition-based);
  `prop:…:risk-quotient` (definition-based, with assessment factors).
- **Methods.** `met:…:cod` (the dichromate COD determination, in the lab);
  `met:…:speciation` (speciation diagram of a metal, Book 2's tools);
  `met:…:risk` (environmental risk assessment, step by step).
- **Boxes.** `history` Rachel Carson and DDT (1962), the Minamata disease
  (1956); `inthelab` measuring BOD₅; `safety` potassium dichromate and
  mercury(II) sulfate in the COD test (Book 2 rows / PubChem GHS).
- **Figures.** F `carbonate-system` (distribution of CO₂(aq), HCO₃⁻, CO₃²⁻
  versus pH; the pH of rain versus p(CO₂); test: crossings at pK₁, pK₂,
  pH 5.6); F `dose-response` (log-logistic curves with LD₅₀ and slopes,
  NOAEL/LOAEL marks; test: 50 % at the median dose); F `bod` (BOD curve and
  the oxygen sag below an outfall; test: L₀ asymptote); S nitrogen and
  phosphorus fluxes into a lake (box diagram); S compartments of a level-I
  model (air, water, soil, sediment, fish); P an algal bloom on a lake
  (NASA, PD — verify); AI none.
- **Ledger.** CO₂, CH₄, N₂O global means for a stated year (NOAA-GML, agency
  named only in the ledger); GWP₁₀₀ and lifetimes of CH₄ and N₂O (IPCC-AR6
  WG1); Henry constant of CO₂ (Book 3 `SANDER-2023` row read-only) and pKa₁,
  pKa₂ of carbonic acid (IUPAC-PKA or Book 2 rows read-only); seawater
  carbonate constants (**at risk**: open paper, else freshwater only);
  Redfield ratio (**at risk**: open review); logK_ow of DDT, benzene,
  a PCB (PubChem experimental logP); LD₅₀ of NaCl, caffeine, nicotine
  (PubChem toxicity sections); WHO guideline values for As, Pb, NO₃⁻ (Book 3
  `who:` rows read-only, new rows from WHO-DWQ if missing).
- **Exercises palette.** pH of clean rain; acid rain from a given SO₂ load;
  alkalinity from a titration; the change in [H⁺] for −0.1 pH; hardness in
  mg CaCO₃/L; BOD from data; the limiting nutrient by the Redfield ratio;
  K_d from K_oc and organic carbon; BCF from K_ow; LD₅₀ scaled to body mass;
  PEC/PNEC with an assessment factor; biomagnification along a food chain.
- **Weekend problem — "A pesticide in a lake".** I K_ow, K_oc and the
  partitioning into sediment (problem lake data); II a level-I mass balance
  over air, water, sediment and fish; III first-order degradation and the
  concentration after one year; IV PEC/PNEC with an assessment factor, and
  the fish concentration against a consumption threshold (problem data).
  **Named number: the risk quotient PEC/PNEC** (computed; the conclusion
  follows from whether it exceeds 1). 25 questions.

## Ch. 33 — Lab Techniques III: Research Practice — `lab-techniques-3`

- **Hook.** A bottle of butyllithium solution catches fire if a drop meets
  air; a glovebox keeps oxygen and water below a few parts per million.
  Research chemistry often begins by keeping the atmosphere out.
- **Recall.** Year 1 volume: hazard, risk, pictograms, H and P statements,
  safety data sheets, measurement uncertainty, type A/B evaluations; Year 2
  volume: inert atmosphere, work-up, drying agents, flash chromatography,
  chromatography terms, mass spectrometry, HRMS, monoisotopic mass,
  ¹³C NMR, confidence intervals, Student's coefficient, calibration,
  precision, trueness, bias, repeatability, method validation, adiabatic
  temperature rise; \cref{ch:b3:advanced-nmr}, \cref{ch:b3:x-ray-diffraction},
  \cref{ch:b3:electrode-kinetics}.
- **Sections.** 1 Working without air (the Schlenk line; evacuate–refill
  cycles; cannula transfers; freeze–pump–thaw degassing; dry solvents; the
  glovebox; titrating an organolithium). 2 Characterising a new compound (the
  workflow: purity by TLC/HPLC, HRMS, ¹H/¹³C/2D NMR, IR, melting point,
  elemental analysis, X-ray, optical rotation and ee; purity by quantitative
  NMR with an internal standard). 3 Statistics of a research result (is a
  new yield better? the t-test; comparing precisions, the F-test; outliers
  and why not to delete them; reporting). 4 The notebook, research data and
  the literature (what to record; raw data; electronic notebooks; FAIR data;
  research integrity; primary, secondary and tertiary sources; peer review;
  a paper's structure; supporting information; structure and reaction
  databases; judging a published procedure). 5 Risk assessment of a new
  procedure (hazards and exposure; the hierarchy of controls; scale-up
  thermal hazards; peroxide formers; an emergency plan; a worked
  assessment).
- **Definitions.** `def:b3:lab-techniques-3:air-sensitive` (air-sensitive
  compound, pyrophoric substance); `:schlenk` (Schlenk line, Schlenk flask,
  glovebox); `:cannula` (cannula transfer); `:degassing` (freeze–pump–thaw
  degassing); `:elemental` (elemental analysis); `:qnmr` (quantitative NMR);
  `:tests` (significance test, null hypothesis); `:notebook` (laboratory
  notebook, raw data); `:fair` (FAIR data); `:integrity` (research
  integrity, fabrication, falsification, plagiarism); `:assessment` (risk
  assessment, hierarchy of controls); `:peroxide` (peroxide former);
  `:literature` (primary literature, secondary literature, peer review,
  supporting information).
- **Ownership check.** Map: Y1 owns lab safety, GHS, uncertainty (recalled
  in Y3 `lab-techniques-3`). Book 2 owns *hazard*, *risk*, *hazard
  pictogram*, *signal word*, *H/P statements*, *safety data sheet*,
  *measurement uncertainty*, *type A/B evaluation*; Book 3 owns *inert
  atmosphere*, *work-up*, *drying agent*, *flash chromatography*, *HRMS*,
  *monoisotopic mass*, *internal standard*, *confidence interval*,
  *Student's coefficient*, *precision*, *trueness*, *bias*,
  *repeatability*, *reproducibility*, *method validation*, *adiabatic
  temperature rise*, *thermal runaway*: recalled. *Risk assessment* is a
  new phrase beside Book 2's *risk*; *elemental analysis* and *quantitative
  NMR* are in no map nor harvest (Book 3 ch32/35 do not define them).
- **Statements.** `prop:…:purge-cycles` residual oxygen after n cycles
  (p_min/p₀)ⁿ (proof); `prop:…:qnmr` purity formula (proof);
  `prop:…:mass-fractions` C, H, N mass fractions from a formula (proof;
  computed with `tools/molar_mass.py`); `prop:…:ppm-error` HRMS error in ppm
  (definition-based); `thm:…:t-test` the two-sample t statistic follows
  Student's law under the null hypothesis (`\admitted`, treated in more
  advanced courses; used); `prop:…:f-test` (`\admitted`, used);
  `prop:…:titre` organolithium titre (proof by stoichiometry).
- **Methods.** `met:…:cannula` (a cannula transfer step by step);
  `met:…:characterise` (characterisation checklist); `met:…:compare-means`
  (t-test, step by step); `met:…:notebook` (writing an entry);
  `met:…:risk-assessment` (step by step); `met:…:read-paper`.
- **Boxes.** `history` Wilhelm Schlenk's glassware (1910s); `inthelab` the
  glovebox antechamber cycle; `safety` n-butyllithium and sodium hydride
  (PubChem GHS: pyrophoric, water-reactive).
- **Figures.** S a Schlenk line (manifold, taps, bubbler, cold trap, pump;
  Book 2's `rbflask`, Book 3's `bubbler` and `septum` pics); S a cannula
  transfer between two Schlenk flasks; S a glovebox with antechamber and
  gloves; S the characterisation workflow (flowchart); S the hierarchy of
  controls (inverted pyramid); F `qnmr` (synthetic ¹H spectrum of a sample
  with an internal standard; test: integrals proportional to proton counts,
  purity formula recovers the input); P a Schlenk line (Commons — verify);
  AI a research laboratory with a glovebox (lab scene).
- **Ledger.** GHS of n-BuLi, NaH, diethyl ether, THF (PubChem; peroxide
  former classes); the ±0.4 % elemental-analysis tolerance (journal author
  guidelines, open web page, **check**); FAIR principles paper (Wilkinson et
  al. 2016, Scientific Data, open access); ¹H shift of ferrocene and of a
  qNMR standard (NMRShiftDB / SDBS); masses read-only (Book 3 `mass:`).
- **Exercises palette.** Residual O₂ after three cycles; cannula transfer of
  a volume of BuLi and its moles from a titre; HRMS formula choice from a
  measured mass (ppm); CHN check of a proposed formula; qNMR purity; a
  t-test on two sets of yields; an F-test on two methods; a risk assessment
  of a given procedure (controls chosen); peroxide testing schedule;
  primary or secondary source.
- **Weekend problem — "From flask to paper: a new air-sensitive compound".**
  I the synthesis of ferrocene from FeCl₂ and sodium cyclopentadienide under
  nitrogen: stoichiometry, purge cycles; II characterisation data (problem
  HRMS, ¹H NMR singlet at the ledger shift, CHN computed) and consistency;
  III purity by qNMR (problem integrals and masses) with its uncertainty;
  IV the risk assessment (cracking dicyclopentadiene, NaH) and the CV of the
  product (ch15: a reversible wave). **Named number: the qNMR purity of the
  ferrocene sample, in %, with its standard uncertainty** (computed).
  25 questions.
