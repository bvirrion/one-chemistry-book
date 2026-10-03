# Book 3 (University Chemistry, Year 2) — chapter briefs

Phase A plan, 2026-10-02. Year `parts/bachelor-2`, label prefix `b2`, entry
`one_chemistry_book_3_university_year_2.tex`. 35 chapters in outline order.
Binding rules: `sources/BATCH_BOOKS_1-4.md` (read it first). Term list:
`DEFINITIONS.md`. State, projection and traps: `PROGRESS.md`.

## Conventions for every chapter

- **Register (PC\* depth).** Laws are `theorem`/`proposition` with a Year-2
  derivation: partial derivatives and exact differentials (thermodynamics:
  $\Delta_r X = (\partial X/\partial\xi)_{T,p}$, Schwarz, Euler's identity for
  homogeneous functions, Gibbs–Helmholtz), determinants and eigenvalues
  (LCAO 2×2, Hückel n×n), simple separable ODEs (reactors, diffusion layer,
  Clausius–Clapeyron), first-order Taylor expansions (propagation of
  uncertainty, perturbation of two levels), least squares by partial
  derivatives. Anything else gets `\admitted` and a prose pointer ("derived
  in the Year 3 volume", "treated in more advanced courses" when the series
  never proves it).
- **Recall boxes.** Book 2 is cited in prose only ("the Year 1 volume, on
  …"), Book 1 as "the school volume" or "Book 1 (grade 12)", physics as
  "from physics" (first and second laws, entropy, heat capacities, Fick's
  law, the wavefunction as a probability amplitude). `\cref{ch:b2:…}` only
  inside this book. Never `\cref` across volumes.
- **Definitions.** `\emph{term}\index{term}` only inside a `definition`, only
  for a term this book owns (see `DEFINITIONS.md`). A term owned by Book 2 is
  used plainly (recall box when it matters); a term owned by Book 4 is used
  plainly with "treated in the Year 3 volume". Named laws this book owns
  (Hess's law, Kirchhoff's law, Raoult's and Henry's laws, van 't Hoff
  equation, lever rule, Hückel's rule, 18-electron rule, Carothers equation)
  follow Book 2's precedent (Nernst equation, Markovnikov's rule): the name is
  `\emph{}\index{}`-ed in its own theorem — **pending a sync ruling** (report
  point 9); if refused, they get a one-line `definition` naming the law
  before the theorem.
- **Calibration.** 12 exercises (4★, 5★★, 3★★★), one weekend problem of 22–28
  questions in Parts I–IV, the last question (or its answer) printing a named
  number. Target ~11 pp per chapter (≈ 9 body + 2 solutions): Book 2 landed
  at 7.6 + 1.6 and −13.8 %; this book writes every derivation in full, a
  worked example after each substantial statement, an `inthelab` box where a
  procedure exists, and ~4 schematics per chapter.
- **Tags.** **S** schematic (TikZ / chemfig / modiagram / tikz-3dplot /
  pgfplots of a formula), **F** figdata curve (`figdata/bachelor-2/<name>.py`
  + `tests/bachelor-2/test_<name>.py`), **AI** illustration (everyday,
  industrial or lab scene only, JPEG), **P** photograph (Commons, licence
  re-verified through the API before insertion). "(found)" = file exists on
  Commons with the licence shown (checked 2026-10-02); "(to find)" = search
  in Phase B.
- **Ledger.** Ids prefixed by kind; new prefixes for this book: `dfh:`
  `s0:` (CODATA key values / JANAF / WebBook, `_g`, `_l`, `_cr`, `_aq`
  suffixes), `janafH:` (H°(T)−H°(298) rows), `janafG:` (ΔfG° at T),
  `cp:`, `dfus:`, `tfus:`, `tb:`, `antoine:`, `azeo:`, `eut:`, `dhyd:`,
  `d0:`, `pe:`, `lf:`, `c13:`, `ms:`, `mass:`, `iso:` (existing prefix),
  `tg:`, `rot:` (existing prefix), `who:`, `iai:`, `usgs:` (existing
  prefix). Grep all ledgers before minting; cite Book 1/2 rows read-only
  (`dfg:` NBS-82 rows, `re:`, `ie:`, `ea:`, `geo:`, `pka:`, `iso:`, `ghs:`,
  `const:` …).
- **Planned sources** (keys for `sources/ledger/book3.md`):
  CODATA-KEY (Cox, Wagman, Medvedev 1989, CODATA Key Values for
  Thermodynamics, online table — reachable, checked), JANAF (NIST-JANAF 4th
  ed., `janaf.nist.gov/tables/*.txt` — reachable), NBS-82 (Wagman et al.
  1982, scanned; only where CODATA/JANAF lack a species; Book 2's `dfg:`
  rows reused read-only), WEBBOOK-THERMO (gas/condensed thermochemistry,
  reaction thermochemistry: hydrogenation enthalpies), WEBBOOK-PHASE
  (Antoine parameters, Tb, ΔfusH, ΔvapH), WEBBOOK-DIAT (Huber–Herzberg
  diatomic constants: re, D0), WEBBOOK-IEMOL (ionisation energies), WEBBOOK-MS
  (EI mass spectra), WEBBOOK-IR, NIST-SOLDER (NIST Metallurgy, phase
  diagrams of solder systems: Pb–Sn, Bi–Sn, Ag–Sn, Cu–Sn invariant points —
  reachable), SANDER-2023 (Sander, Compilation of Henry's law constants v5,
  Atmos. Chem. Phys. 2023, CC BY), IUPAC-PKA (digitised pKa dataset, as Book
  2), CIAAW-ISO (isotopic compositions), NIST-AWIC (atomic weights and
  isotopic compositions: exact masses), NIST-ASD (lines), NMRSHIFTDB (13C and
  1H shifts, open), PUBCHEM / PUBCHEM-GHSSUM (GHS, optical rotation, mp, bp),
  IUPAC-NIST-SDS (solubility data series: mutual solubilities, NaCl–water),
  USGS-MCS2026, IAI (International Aluminium Institute statistics: smelting
  energy intensity), WHO-DWQ (Guidelines for drinking-water quality, 4th ed.:
  lead guideline value), COMMONS (photographs).

---

## Ch. 1 — Enthalpies of Reaction — `reaction-enthalpy`

- **Hook.** A camping-gas cartridge under a pan: a few grams of butane bring
  a litre of water to the boil, and the blue flame is far hotter than the
  boiling water. How much heat does a reaction release, and how hot can its
  flame get, computed before anything is lit?
- **Recall.** From physics: the first law $\Delta U = W + Q$, enthalpy $H =
  U + pV$, $Q_p = \Delta H$ for a monobaric change, heat capacities $C_p =
  (\partial H/\partial T)_p$, $H$ of a perfect gas independent of $p$. Year
  1 volume: extent $\xi$, stoichiometric numbers $\nu_i$, standard state and
  $p^\circ = \qty{1}{bar}$ (owned there). School volume (grade 11):
  exothermic, endothermic, bond energies.
- **Sections.** 1 Reaction quantities ($H(T,p,\xi)$; $\Delta_r H =
  (\partial H/\partial \xi)_{T,p}$; heat exchanged at constant $T$, $p$;
  exothermic, endothermic). 2 Standard reaction enthalpy, standard
  reference states of the elements, standard enthalpies of formation, Hess's
  law. 3 Computing $\Delta_r H^\circ$: formation enthalpies, bond enthalpies,
  the Born–Haber cycle and lattice enthalpy. 4 Temperature: Kirchhoff's law.
  5 Adiabatic reactions and measurement: flame temperature; the bomb
  calorimeter ($\Delta_r U$ versus $\Delta_r H$).
- **Definitions.** `def:b2:reaction-enthalpy:reaction-quantity` (reaction
  quantity, reaction enthalpy); `:standard-reaction-enthalpy` (standard
  reaction quantity, standard reaction enthalpy); `:exothermic`
  (exothermic, endothermic, athermic — **re-found** g11 `reaction-energy`);
  `:formation` (standard reference state of an element, standard enthalpy
  of formation); `:bond-enthalpy` (bond dissociation enthalpy, mean bond
  enthalpy — **re-found** g11 "bond energy"); `:lattice-enthalpy` (lattice
  enthalpy); `:flame-temperature` (adiabatic flame temperature).
  Named-law statements: `thm:…:hess` (Hess's law), `thm:…:kirchhoff`
  (Kirchhoff's law).
- **Ownership check.** Map owner (enthalpy of reaction, Hess's law); S1 left
  *standard state* to the Year 1 volume (recalled, not defined) and gave this
  chapter *standard enthalpy of formation* and *Hess's law*. Re-founds g11
  (exothermic, endothermic, bond energy). Takes nothing from Book 2's
  harvest (no thermochemistry term there) nor from Book 4 (partition
  functions, statistical heat capacities: pointer). *Lattice enthalpy* is
  not in the map and Book 2 ch6 did not define it: earliest need, claimed
  (report point 2).
- **Statements.** `prop:…:qp` heat received at constant $T,p$: $Q =
  \int\Delta_r H\,\dd\xi = \Delta_r H\,\Delta\xi$ when $\Delta_r H$ is
  constant (proof: $\dd H = (\partial H/\partial\xi)\dd\xi$ at fixed $T,p$);
  `prop:…:ideal` $\Delta_r H \approx \Delta_r H^\circ$ for perfect gases and
  condensed phases (proof: $H_m$ of a perfect gas independent of $p$;
  condensed phases weakly dependent); `thm:…:hess` (proof: $H$ a state
  function, path through the elements); `prop:…:formation-sum`
  $\Delta_r H^\circ = \sum_i\nu_i\Delta_f H_i^\circ$ (proof);
  `prop:…:bond-estimate` gas-phase estimate from bond enthalpies, with its
  error on real data; `thm:…:kirchhoff` $\dd\Delta_r H^\circ/\dd T =
  \Delta_r C_p^\circ$ (proof: Schwarz on $H(T,\xi)$); `prop:…:bomb`
  $\Delta_r H = \Delta_r U + \Delta\nu_{\text{gas}}RT$ (proof);
  `prop:…:flame` adiabatic isobaric reaction: $\xi\Delta_r H^\circ(T_0) +
  \int_{T_0}^{T_f} C_p(\text{final system})\,\dd T = 0$ (proof: two-step
  path, $H$ a state function).
- **Methods.** `met:…:hess-cycle`; `met:…:born-haber`;
  `met:…:flame-temperature`; `met:…:calorimetry` (water equivalent of a
  calorimeter, then $\Delta_r H$).
- **Figures.** S enthalpy ladder for the combustion of methane (elements at
  0, reactants, products, $\Delta_f H^\circ$ arrows); S Born–Haber cycle of
  NaCl (level ladder: sublimation, dissociation, ionisation, electron
  attachment, lattice); S two-step path in the $(\xi, T)$ plane for the
  flame temperature; S bomb calorimeter cross-section (bomb, water bath,
  `stirrer`, `thermometer` pics, ignition wire); F `flame-temperature`
  (enthalpy of the products versus $T$ from JANAF increments, horizontal line
  $-\xi\Delta_r H^\circ$, intersection = $T_{\text{ad}}$; butane in air and in
  oxygen); F `thermo-data` (table of every printed $\Delta_r H^\circ$,
  $\Delta_r S^\circ$, $\Delta_r G^\circ$ of chapters 1–4); AI camping stove
  under a pan, blue flame (hook; check the flame colour); P G. H. Hess
  (`File:Portrait of Professor of Chemistry German Ivanovich Hess.jpg`, CC
  BY-SA 4.0, found) in a `history` box (1840); P Marcellin Berthelot
  (`File:Marcellin Berthelot.jpg`, PD, found) in the calorimetry `history`.
- **Ledger.** `dfh:`/`s0:` CODATA-KEY for \ce{H2O(l)}, \ce{H2O(g)},
  \ce{CO2}, \ce{CO}, \ce{O2}, \ce{N2}, \ce{H2}, \ce{NaCl(cr)}, \ce{Na(g)},
  \ce{Cl(g)}, \ce{HCl(g)}, \ce{NH3(g)}; butane, propane, methane, octane
  from WEBBOOK-THERMO (reuse Book 1's `dfh:C8H18`, `dfh:CO2`, `dfh:H2O-l`
  read-only where they match the consensus value, else report);
  `janafH:` $H^\circ(T)-H^\circ(298)$ of \ce{N2}, \ce{CO2}, \ce{H2O(g)},
  \ce{O2} at 300–3000 K (every 100 K: flame script); reuse `ie:Na`,
  `ea:Cl`, `be:` rows read-only.
- **Exercises palette.** $\Delta_r H^\circ$ from formation enthalpies (★);
  exo/endo and heat per kilogram of fuel (★); $\Delta_r U$ from a bomb
  measurement (★); a Hess cycle for an unmeasurable reaction (C → CO) (★);
  bond-enthalpy estimate versus tables (★★); Kirchhoff to 1000 K (★★);
  Born–Haber for KCl and the lattice enthalpy (★★); calorimeter water
  equivalent then a neutralisation enthalpy (★★); fuel value of hydrogen
  versus methane per kg and per litre (★★); flame temperature with constant
  $C_p$ versus with JANAF tables (★★★); Kirchhoff with $C_p(T) = a + bT$
  (★★★); why the flame of a fuel in oxygen is hotter but not proportionally
  (★★★).
- **Weekend problem — "The camping-gas cartridge".** I the fuel: combustion
  of butane, $\Delta_r H^\circ$ from formation enthalpies, energy per gram;
  II the measurement: bomb calorimetry of butane, $\Delta_r U$ to
  $\Delta_r H$; III the flame: adiabatic flame temperature in air with
  constant $C_p$, then with the tabulated enthalpy increments; IV the pan:
  energy to boil water, efficiency, litres per cartridge. **Named number:
  the adiabatic flame temperature of butane in air, ≈ 2.3 × 10³ K
  (computed in `flame-temperature.py`).** 25 questions.

## Ch. 2 — Entropy and Free Energy of Reaction — `reaction-free-energy`

- **Hook.** A sports cold pack: squeeze it, ammonium nitrate dissolves, and
  the pack goes cold. A change that absorbs heat runs on its own; the
  enthalpy alone cannot decide which way a reaction goes.
- **Recall.** From physics: the second law, entropy as a state function,
  $\dd S = \delta Q/T + \delta S_{\text{created}}$ with $\delta
  S_{\text{created}} \geq 0$, $\dd U = T\dd S - p\dd V$ for a closed
  non-reacting system. \cref{ch:b2:reaction-enthalpy}. Year 1 volume: $Q$,
  $K^\circ$ and the direction of evolution, admitted there "from the second
  law" (now derived over chapters 2–4).
- **Sections.** 1 Standard molar entropies and the third law (Nernst's
  principle, the promise of Book 2 ch13's history box). 2 Reaction entropy
  (signs, $\Delta\nu_{\text{gas}}$, the entropy of elimination — Book 2 ch20
  promise). 3 Gibbs energy of a reacting system: $G = H - TS$, $\dd G = V\dd
  p - S\dd T + \Delta_r G\,\dd\xi$. 4 The evolution criterion (created
  entropy $= -\Delta_r G\,\dd\xi/T$). 5 $\Delta_r G^\circ(T)$:
  $\Delta_r G^\circ = \Delta_r H^\circ - T\Delta_r S^\circ$, the Ellingham
  approximation, Gibbs–Helmholtz, inversion temperatures.
- **Definitions.** `def:b2:reaction-free-energy:standard-entropy` (standard
  molar entropy); `:reaction-entropy` (reaction entropy, standard reaction
  entropy); `:gibbs-energy` (Gibbs energy); `:reaction-gibbs` (reaction Gibbs
  energy, standard reaction Gibbs energy); `:exergonic` (exergonic,
  endergonic); `:ellingham-approximation` (Ellingham approximation);
  `:inversion-temperature` (inversion temperature).
- **Ownership check.** Map owner (entropy of reaction, $\Delta_r G$,
  evolution criterion). No Book 1 notion re-found (Book 1 has no entropy).
  Book 2 harvest: nothing thermodynamic is taken. Book 4: statistical
  entropy, partition functions (pointer only, "the Year 3 volume
  counts the microstates"). *Ellingham approximation* and *inversion
  temperature* are not in the map: earliest need (ch2; ch6 recalls).
- **Statements.** `thm:…:third-law` (entropy of a perfect crystal → 0 as
  $T \to 0$; `\admitted`, statistical origin in the Year 3 volume);
  `prop:…:absolute-entropy` $S^\circ(T) = \int_0^T C_p^\circ/T\,\dd T +
  \sum\Delta_{\text{trs}}H^\circ/T_{\text{trs}}$ (proof); `prop:…:sign-rule`
  sign of $\Delta_r S^\circ$ from $\Delta\nu_{\text{gas}}$ (argued, with its
  exceptions); `prop:…:dG` $\dd G = V\dd p - S\dd T + \Delta_r G\,\dd\xi$
  (proof from $G = H - TS$ and the physics identity);
  `prop:…:g-h-s` $\Delta_r G = \Delta_r H - T\Delta_r S$ (proof);
  `thm:…:evolution` at fixed $T$, $p$, no work other than expansion,
  $\Delta_r G\,\dd\xi \leq 0$, equality at equilibrium (proof: second law,
  $T\delta S_{\text{created}} = -\Delta_r G\,\dd\xi$);
  `prop:…:gibbs-helmholtz` $\dd(\Delta_r G^\circ/T)/\dd T = -\Delta_r
  H^\circ/T^2$ (proof); `prop:…:entropy-t` $\dd\Delta_r S^\circ/\dd T =
  \Delta_r C_p^\circ/T$ (proof, Schwarz on $G$).
- **Methods.** `met:…:delta-g-standard` ($\Delta_r G^\circ(T)$ from tables in
  the Ellingham approximation; when to go beyond it); `met:…:entropy-sign`.
- **Figures.** F `standard-entropy` ($S^\circ(T)$ of water from 0 to 500 K:
  Debye-$T^3$ start (admitted), plateaus and jumps at fusion and boiling, from
  JANAF $C_p$ and transition enthalpies; test: $S^\circ(\ce{H2O},\text{l},
  298) =$ CODATA within 1 J/(K mol)); F `gibbs-extent` ($G(\xi)$ of
  \ce{N2O4 <=> 2NO2} at 298 K: minimum at $\xi_{\text{eq}}$, tangent slope
  $\Delta_r G$); S $\Delta_r H^\circ$ and $T\Delta_r S^\circ$ lines versus
  $T$ crossing at the inversion temperature of \ce{CaCO3}; S the four
  sign cases ($\Delta_r H$, $\Delta_r S$) as a 2 × 2 chart; AI a sports
  cold pack squeezed in a first-aid kit (hook); P J. W. Gibbs
  (`File:Josiah Willard Gibbs -from MMS-.jpg`, PD, found) in a `history`
  box (1876).
- **Ledger.** `s0:` CODATA-KEY (\ce{H2O} l and g, \ce{CO2}, \ce{O2},
  \ce{N2}, \ce{H2}, \ce{NH3}, \ce{CaO}); \ce{CaCO3}(cr, calcite),
  \ce{NH4NO3}(cr) and its aqueous ions from NBS-82 (page in the row) or
  JANAF; `janafH:`/`cp:` for ice, liquid water, steam; \ce{N2O4}/\ce{NO2}
  from JANAF; `tfus:`/`tb:` water (reuse Book 2 rows).
- **Exercises palette.** Sign of $\Delta_r S^\circ$ for six reactions (★);
  $\Delta_r S^\circ$ and $\Delta_r G^\circ(298)$ from tables (★); exergonic
  or not (★); entropy of vaporisation of water at its boiling point (★);
  inversion temperature of a decomposition (★★); $\Delta_r G^\circ$ at 1000 K
  in the Ellingham approximation versus JANAF (★★); why eliminations win at
  high temperature (Book 2 promise) (★★); the cold pack: $\Delta_r H^\circ >
  0$, $\Delta_r G^\circ < 0$ (★★); Gibbs–Helmholtz from two values of
  $\Delta_r G^\circ$ (★★); $G(\xi)$ of an ideal gas reaction and its
  minimum (★★★); $\Delta_r S^\circ(T)$ with a constant $\Delta_r C_p^\circ$
  (★★★); the third law and a residual entropy (CO in its crystal) (★★★).
- **Weekend problem — "The lime kiln".** I data: $\Delta_r H^\circ$ and
  $\Delta_r S^\circ$ of \ce{CaCO3 -> CaO + CO2}; II $\Delta_r G^\circ(T)$ in
  the Ellingham approximation, the sign at 298 K and at 1300 K;
  III the decomposition temperature under 1 bar of \ce{CO2} and the
  evolution criterion; IV the kiln's balance: heat per tonne of lime, \ce{CO2}
  per tonne. **Named number: the temperature above which limestone
  decomposes under 1 bar of carbon dioxide, ≈ 1.1 × 10³ K.** 24 questions.

## Ch. 3 — Chemical Potential and Mixtures — `chemical-potential`

- **Hook.** In winter, salt spread on a road melts ice at −10 °C, and the
  coolant of a car engine neither freezes nor boils. A dissolved substance
  changes the temperatures at which its solvent freezes and boils, and by
  an amount that does not depend on what it is.
- **Recall.** \cref{ch:b2:reaction-free-energy} ($G$, $\Delta_r G$, the
  evolution criterion); Year 1 volume: activities written as recipes
  ($p/p^\circ$, $c/c^\circ$, 1), mole fraction, partial pressure,
  miscibility; Book 2 promises: activity coefficients and ionic strength,
  limits of Kohlrausch's law, the lowering of a melting point by a solute.
- **Sections.** 1 Partial molar quantities (definition, Euler's identity,
  Gibbs–Duhem). 2 Chemical potential ($\dd G = V\dd p - S\dd T + \sum\mu_i\dd
  n_i$; equilibrium between phases; matter flows towards lower $\mu$;
  $\Delta_r G = \sum\nu_i\mu_i$). 3 Ideal systems: perfect gas, ideal
  mixture (Raoult), ideal dilute solution (Henry); the activity as the
  quantity in $\mu = \mu^\circ + RT\ln a$; $\Delta_r G = \Delta_r G^\circ +
  RT\ln Q$. 4 Real mixtures: activity coefficients, ionic strength, the
  Debye–Hückel limiting law, Kohlrausch's square-root law. 5 Colligative
  properties: boiling-point elevation, freezing-point depression, osmotic
  pressure.
- **Definitions.** `def:b2:chemical-potential:partial-molar` (partial molar
  quantity, partial molar volume); `:chemical-potential` (chemical
  potential, standard chemical potential); `:ideal-mixture` (ideal mixture,
  ideal dilute solution); `:activity-coefficient` (activity coefficient);
  `:ionic-strength` (ionic strength); `:colligative` (colligative property,
  cryoscopic constant, ebullioscopic constant); `:osmotic-pressure`
  (semipermeable membrane, osmotic pressure). Named-law statements:
  `thm:…:raoult` (Raoult's law), `prop:…:henry` (Henry's law, Henry
  constant).
- **Ownership check.** Map owner (chemical potential, partial molar
  quantity, Raoult, Henry). Book 2 owns *activity*, *mole fraction*,
  *partial pressure*, *miscible*: recalled; the chapter proves that the
  Year-1 recipes for $a$ follow from $\mu$ but does not redefine *activity*.
  Book 4: none (fugacity is a remark, not defined). *Ionic strength*,
  *osmotic pressure*, *colligative property* not in the map: earliest need.
- **Statements.** `thm:…:euler` $X = \sum n_i\bar X_i$ (proof: $X$
  homogeneous of degree 1 in the $n_i$, Euler's identity);
  `prop:…:gibbs-duhem` $\sum n_i\dd\mu_i = 0$ at fixed $T,p$ (proof);
  `thm:…:phase-equilibrium` a constituent present in two phases is at
  equilibrium iff its chemical potentials are equal, and otherwise passes to
  the phase of lower $\mu$ (proof from the evolution criterion);
  `prop:…:mu-gas` $\mu = \mu^\circ + RT\ln(p_i/p^\circ)$ (proof:
  $(\partial\mu/\partial p)_T = \bar V = RT/p$); `thm:…:raoult` $p_i = x_i
  p_i^*$ for an ideal mixture (proof: equal $\mu$ in liquid and vapour);
  `prop:…:henry` $p_i = k_{H,i}x_i$ for a dilute solute; `prop:…:delta-g-q`
  $\Delta_r G = \Delta_r G^\circ + RT\ln Q$ (proof);
  `prop:…:debye-huckel` $\log\gamma_\pm = -A|z_+z_-|\sqrt I$ (`\admitted`,
  ionic-atmosphere model beyond this course); `prop:…:kohlrausch-sqrt`
  $\Lambda = \Lambda^\circ - K\sqrt c$ (`\admitted`, same origin);
  `thm:…:cryoscopy` $\Delta T_f = K_f\,b$ with $K_f = RT_f^{*2}M/\Delta_{\text{fus}}
  H$ (proof: equal $\mu$, Gibbs–Helmholtz, linearisation);
  `prop:…:ebullioscopy` (same proof); `thm:…:osmosis` $\Pi = cRT$ (proof).
- **Methods.** `met:…:activity-reference` (choosing the reference state:
  gas, solvent (Raoult), solute (Henry), pure solid); `met:…:molar-mass`
  (molar mass by cryoscopy or osmometry).
- **Figures.** F `raoult-henry` (partial and total pressures over a binary
  mixture: ideal straight lines; a positive deviation from a Margules model,
  with the Raoult tangent at $x \to 1$ and the Henry tangent at $x \to 0$);
  S tangent construction of partial molar volumes on a $V_m(x)$ curve (model
  curve); S $\mu(T)$ of solid, pure liquid and solution (the lowered liquid
  line moves the crossing: freezing-point depression); S osmosis in a `utube`
  with a semipermeable membrane and the pressure head; AI salt spreader on a
  wintry road (hook); P F.-M. Raoult (`File:François-Marie Raoult.jpg`, PD,
  found) in a `history` box (1882–1887).
- **Ledger.** `dfus:`/`tfus:` water (CODATA/JANAF), $K_f$ computed; `henry:`
  \ce{CO2} and \ce{O2} in water (SANDER-2023); Book 1's `sea:` rows
  read-only (seawater freezing); bp and molar mass of ethane-1,2-diol
  (PubChem); `p*:` vapour pressure of water at 25 °C (JANAF or WebBook).
- **Exercises palette.** Partial molar volume by the tangent (★); Raoult:
  vapour pressure over a sugar solution (★); Henry: \ce{CO2} in a soda
  bottle at 4 bar (★); $\Delta_r G$ from $\Delta_r G^\circ$ and $Q$ (★);
  Gibbs–Duhem: from one partial molar volume to the other (★★); freezing
  point of seawater (★★); molar mass of a protein by osmometry (★★);
  osmotic pressure of physiological saline (★★); ionic strength and
  $\gamma_\pm$ at $10^{-2}$ mol/L (★★); the Henry constant of a Margules
  mixture from the model (★★★); why the solute must be non-volatile and
  insoluble in the solid (★★★); boiling-point elevation measured with a
  0.01 K thermometer: the smallest detectable molality (★★★).
- **Weekend problem — "The radiator in winter".** I the coolant as an ideal
  mixture of water and ethane-1,2-diol: vapour pressure (Raoult); II the
  cryoscopic law derived and $K_f$ of water from its enthalpy of fusion;
  III freezing point of a 30 % coolant in the dilute model and its limits;
  IV boiling-point elevation and the pressure cap. **Named number: the mass
  fraction of ethane-1,2-diol that keeps the coolant liquid down to −20 °C
  in the ideal-mixture model, w ≈ 0.44** (computed with $\ln x_{\text{w}}$,
  not the dilute linearisation, which gives less). 24 questions.

## Ch. 4 — Equilibrium Constants and Shifts — `equilibrium-shifts`

- **Hook.** An ammonia plant runs at about 450 °C and 200 bar. At room
  temperature the equilibrium is far more favourable; why heat it, and why
  press it so hard?
- **Recall.** \cref{ch:b2:reaction-free-energy}, \cref{ch:b2:chemical-potential}
  ($\Delta_r G = \Delta_r G^\circ + RT\ln Q$); Year 1 volume: $K^\circ$, $Q$,
  the law of mass action and the direction of evolution (admitted there),
  progress tables; Book 2 promised the rate–yield compromise for ammonia and
  sulfur trioxide.
- **Sections.** 1 $K^\circ$ from $\Delta_r G^\circ$; the Year-1 laws derived.
  2 Temperature: the van 't Hoff equation and its integration. 3 Variance:
  counting intensive parameters, the phase rule. 4 Shifting an equilibrium
  (temperature, pressure, adding a constituent, adding an inert gas;
  Le Chatelier's principle as a corollary, and the case where adding a
  reactant shifts backwards; a phase disappearing ends the equilibrium).
  5 Optimising a synthesis: ammonia (yield versus rate, recycle, purge),
  sulfur trioxide (staged beds with cooling between them).
- **Definitions.** `def:b2:equilibrium-shifts:variance` (independent
  intensive parameter, variance); `:shift` (shift of an equilibrium);
  `:moderation` (Le Chatelier's principle — as a named statement after the
  proven propositions); `:single-pass` (single-pass conversion, recycle,
  purge). Named-law statement: `thm:…:vant-hoff` (van 't Hoff equation).
- **Ownership check.** Map owner (van 't Hoff, variance). Book 2 owns
  $K^\circ$, $Q$, *equilibrium state*, *quantitative reaction*, *phase*,
  *intensive variable*: recalled; Book 2 deliberately avoided "shift"
  language, leaving it here. Book 4 ch11 recalls van 't Hoff from partition
  functions. *Single-pass conversion*/*recycle*/*purge* not in the map
  (ch5 recalls them). No Book 1 re-found (g12 *equilibrium constant* is
  Book 2's re-found).
- **Statements.** `thm:…:k-from-g` $\Delta_r G^\circ = -RT\ln K^\circ$
  (proof: $\Delta_r G = 0$ at equilibrium); `cor:…:mass-action` the law of
  mass action and the direction rule of the Year 1 volume (proof:
  $\Delta_r G = RT\ln(Q/K^\circ)$ and the evolution criterion);
  `thm:…:vant-hoff` $\dd\ln K^\circ/\dd T = \Delta_r H^\circ/(RT^2)$ (proof:
  Gibbs–Helmholtz); `prop:…:integrated` (two-temperature form, Ellingham
  approximation); `thm:…:phase-rule` $v = c + 2 - \varphi$ with $c = n -
  r - s$ (proof: count variables and relations; examples);
  `prop:…:temperature` raising $T$ favours the endothermic direction (proof:
  sign of $\dd\ln K^\circ/\dd T$); `prop:…:pressure` raising $p$ favours fewer
  gas molecules (proof: $Q \propto p^{\Delta\nu_{\text{g}}}$);
  `prop:…:adding` adding a constituent at fixed $T$, $V$ or $T$, $p$:
  sign of $\partial\ln Q/\partial n_j$ (proof; the \ce{N2} counter-example in
  ammonia synthesis at constant $p$); `prop:…:inert` inert gas at fixed $V$
  (no effect) and at fixed $p$ (as a pressure drop) (proof);
  `prop:…:le-chatelier` (statement and limits, as a corollary).
- **Methods.** `met:…:k-at-t`; `met:…:variance`; `met:…:predict-shift`
  (compute $Q$ just after the change and compare with $K^\circ$).
- **Figures.** F `vant-hoff` part a ($\ln K^\circ$ versus $1/T$ for
  ammonia synthesis from JANAF $\Delta_f G^\circ(T)$; slope $-\Delta_r
  H^\circ/R$), part b (equilibrium mole fraction of \ce{NH3} versus $T$ at 1,
  50, 200 and 300 bar, stoichiometric feed), part c (conversion–temperature
  chart of \ce{SO2} oxidation: equilibrium curve and adiabatic lines of three
  beds); S $Q$/$K^\circ$ arrow after a perturbation; S flow sheet of an
  ammonia loop (compressor, converter, condenser, recycle, purge); AI an
  ammonia plant at night (hook); P F. Haber (`File:Fritz Haber.png`, PD,
  found) and C. Bosch (`File:Carl Bosch.jpg`, PD, found) in a `history` box;
  P H. Le Chatelier (`File:La Sorbonne. M. le professeur H. Le Chatelier,
  membre de l'Institut.jpg`, CC BY-SA 4.0, found) in a second `history`.
- **Ledger.** `janafG:` $\Delta_f G^\circ$ of \ce{NH3(g)} at 298, 400, 500,
  600, 700, 800 K, of \ce{SO2(g)} and \ce{SO3(g)} at 298, 600, 700, 800,
  900 K; `dfh:` \ce{NH3}, \ce{SO2}, \ce{SO3}, \ce{NO} (CODATA-KEY/JANAF);
  reuse Book 2 `haber:T`, `haber:p` read-only.
- **Exercises palette.** $K^\circ$ from $\Delta_r G^\circ$ (★); $K^\circ$ at
  another temperature (★); variance of four systems (★); direction of a
  shift with $T$ and $p$ (★); \ce{NO} in an engine: why hot flames make it
  (★★); the esterification of the Year 1 volume driven by excess and water
  removal (★★); inert gas at constant $p$ in a dissociation (★★); variance
  with a stoichiometric constraint (★★); $\Delta_r H^\circ$ from two
  measured $K^\circ$ (★★); adding \ce{N2} to an ammonia equilibrium at
  constant $p$ (★★★); the end of an equilibrium when a solid vanishes (★★★);
  staged \ce{SO2} conversion with cooling (★★★).
- **Weekend problem — "The ammonia loop".** I $K^\circ(T)$ from data and
  $\Delta_r H^\circ$; II the equilibrium at 723 K and 200 bar, stoichiometric
  feed, perfect gases; III shifts with $T$, $p$ and the argon of the air;
  IV the loop: single-pass conversion, recycle ratio and purge.
  **Named number: the equilibrium mole fraction of ammonia at 723 K and
  200 bar, x ≈ 0.26 in the perfect-gas model (first estimate from
  JANAF; recomputed in `vant-hoff.py`).** 25 questions.

## Ch. 5 — Continuous Reactors and Industrial Processes — `continuous-reactors`

- **Hook.** In the laboratory a reaction runs for an hour in a flask and is
  stopped; a plant makes the same product day and night in a tank that
  never empties, fed at one end and drained at the other. How large must
  the tank be, and how is it kept from overheating?
- **Recall.** Year 1 volume: rates, rate laws, integrated laws, Arrhenius;
  \cref{ch:b2:reaction-enthalpy} (heat of reaction),
  \cref{ch:b2:equilibrium-shifts} (single-pass conversion, recycle); from
  physics: balances of an open system.
- **Sections.** 1 From batch to continuous (the batch reactor as Year 1
  knew it; flow rates, steady operation). 2 The continuous stirred-tank
  reactor (mole balance; conversion and residence time for orders 1 and 2).
  3 The plug-flow reactor (balance on a slice; comparison; cascades of tanks
  tending to a plug flow). 4 Heat balance and safety (adiabatic temperature
  rise; heat generated versus heat removed; multiple steady states; thermal
  runaway). 5 From protocol to plant (scale-up: surface over volume,
  selectivity of consecutive reactions, separation and recycle).
- **Definitions.** `def:b2:continuous-reactors:reactors` (batch reactor,
  continuous reactor, continuous stirred-tank reactor, plug-flow reactor);
  `:residence-time` (residence time); `:conversion` (conversion);
  `:selectivity` (selectivity); `:adiabatic-rise` (adiabatic temperature
  rise); `:runaway` (thermal runaway).
- **Ownership check.** Not in the map; earliest need. *Conversion* is
  distinct from Book 2's *final fractional extent* and *yield* (recalled and
  contrasted). Book 2's *steady-state approximation* is not used as a word
  for a reactor ("steady operation", plain). Book 4: none.
- **Statements.** `prop:…:batch` batch reactor laws recalled in the
  reactor's language; `prop:…:cstr-balance` $F_{A,0} - F_A + r_A V = 0$
  (proof: balance in steady operation); `thm:…:cstr` $X = k\tau/(1 + k\tau)$
  (order 1) and the order-2 root (proof); `thm:…:pfr` $X = 1 - e^{-k\tau}$
  (proof: balance on a slice, separable ODE); `prop:…:compare` plug flow
  needs a smaller volume for any positive order (proof:
  $1 - e^{-x} \geq x/(1+x)$; the $1/r$ area chart); `prop:…:cascade` $N$
  tanks: $X = 1 - (1 + k\tau/N)^{-N} \to 1 - e^{-k\tau}$ (proof);
  `prop:…:adiabatic` $\Delta T_{\text{ad}} = (-\Delta_r H)c_{A,0}X/(\rho c_p)$
  (proof: energy balance); `prop:…:steady-states` steady states are the
  intersections of the S-shaped generation curve and the removal line;
  stability from the slopes (argued, `\admitted` for the linear stability
  analysis); `prop:…:consecutive` A→B→C: maximum of B in a plug flow at
  $\tau = \ln(k_2/k_1)/(k_2 - k_1)$ and in a tank at $\tau = 1/\sqrt{k_1k_2}$
  (proof).
- **Methods.** `met:…:size-reactor` (volume for a target conversion);
  `met:…:heat-balance` (cooling duty, runaway check).
- **Figures.** S the three reactors (batch flask, stirred tank with inlet,
  outlet and stirrer, tube with a slice $\dd V$); F `reactors` part a
  (conversion versus $k\tau$: one tank, two and five tanks, plug flow),
  part b (heat generated and removed versus $T$: one or three steady
  states), part c ($1/r$ versus $X$: the areas that give $\tau$); S
  surface-to-volume scale-up sketch (vessel scaled ×10 in volume); AI a
  chemical plant with stirred-tank reactors and pipe racks (hook).
- **Ledger.** Saponification of ethyl ethanoate: $k$ at 25 °C and $E_a$
  (NIST chemical kinetics database, else exercise data, said so);
  $\Delta_r H^\circ$ of the saponification from formation enthalpies
  (WEBBOOK/NBS-82); reuse `cp:water`, `rho:water` read-only.
- **Exercises palette.** Residence time from volume and flow (★); conversion
  in one tank (★); plug-flow volume for 90 % (★); adiabatic rise of a
  dilute exothermic reaction (★); tank versus tube for order 2 (★★); three
  tanks in series (★★); cooling duty of a tank (★★); scale-up: why a
  1000-L reactor cools worse than a 1-L flask (★★); conversion of a
  reversible reaction in a tank (★★); best residence time for an
  intermediate (★★★); steady states of an exothermic tank (★★★); the
  danger of a cooling failure (time to runaway) (★★★).
- **Weekend problem — "Soap in a tank".** I the kinetics of ethyl
  ethanoate saponification (second order, equimolar feed); II sizing one
  stirred tank for 90 % conversion; III the same duty in a plug-flow tube and
  in a cascade of three tanks; IV heat: adiabatic rise and cooling duty.
  **Named number: the volume of the single stirred tank that converts 90 %
  of the ester at the given feed, V ≈ (computed, a few m³).** 24 questions.

## Ch. 6 — Ellingham Diagrams and Metallurgy — `ellingham`

- **Hook.** A blast furnace turns red rock into liquid iron with coke and
  hot air; no furnace of that kind will ever make aluminium. Which metals
  can carbon win from their oxides, and at what temperature?
- **Recall.** \cref{ch:b2:reaction-free-energy} (Ellingham approximation),
  \cref{ch:b2:equilibrium-shifts} (variance, a phase disappearing);
  Year 1 volume: oxidation numbers, basic and acidic oxides; school volume:
  ores.
- **Sections.** 1 The Ellingham diagram (reactions written for one mole of
  \ce{O2}; straight lines; slopes; breaks at changes of state). 2 Reading
  it: domains of the metal and of its oxide; the equilibrium oxygen
  pressure; which metal reduces which oxide. 3 Carbon and carbon monoxide
  (the three carbon lines, the Boudouard equilibrium, why carbon reduces
  almost every oxide when hot enough). 4 The blast furnace (zones,
  reactions, the role of CO). 5 Other routes: aluminothermy, the Kroll
  process, hydrometallurgy of zinc (roasting, leaching, cementation;
  electrowinning in \cref{ch:b2:batteries-electrolysis}).
- **Definitions.** `def:b2:ellingham:diagram` (Ellingham diagram);
  `:oxygen-pressure` (equilibrium oxygen pressure of an oxide);
  `:boudouard` (Boudouard equilibrium); `:metallurgy` (pyrometallurgy,
  hydrometallurgy, roasting, leaching, cementation); `:aluminothermy`
  (aluminothermic reduction).
- **Ownership check.** Not in the map apart from the chapter; earliest
  need. Book 1 *ore* recalled; Book 2 oxides recalled. Book 4: none.
- **Statements.** `prop:…:line` straight line of slope $-\Delta_r S^\circ$,
  about $+0.2$ kJ K⁻¹ for metal + \ce{O2} → oxide (proof); `prop:…:break`
  the slope changes at a change of state of a reactant or product (proof:
  jump of $\Delta_r S^\circ$ by $\Delta_{\text{trs}}H/T_{\text{trs}}$);
  `thm:…:domains` the metal is stable below its line, the oxide above, for
  $RT\ln(p_{\ce{O2}}/p^\circ)$ read on the same axis (proof: $\Delta_r G =
  \Delta_r G^\circ - RT\ln(p_{\ce{O2}}/p^\circ)$); `prop:…:reduction` a metal
  reduces an oxide whose line lies above its own (proof: difference of two
  reactions); `prop:…:carbon` the \ce{C}/\ce{CO} line falls with $T$
  ($\Delta\nu_{\text{gas}} = +1$) (proof); `prop:…:boudouard` variance and
  composition of the \ce{CO}–\ce{CO2} gas over carbon versus $T$ (proof:
  $K^\circ(T)$, quadratic in $x_{\ce{CO}}$).
- **Methods.** `met:…:read-ellingham` (stability, reductions, crossing
  temperatures); `met:…:choose-reductant`.
- **Figures.** F `ellingham` part a (lines of \ce{Ag2O}, \ce{Cu2O},
  \ce{NiO}, iron oxides, \ce{ZnO}, \ce{Cr2O3}, \ce{SiO2}, \ce{TiO2},
  \ce{Al2O3}, \ce{MgO}, \ce{CaO}; \ce{C}/\ce{CO}, \ce{C}/\ce{CO2},
  \ce{CO}/\ce{CO2}, \ce{H2}/\ce{H2O}; breaks at the boiling points of Zn and
  Mg), part b (Boudouard: $x_{\ce{CO}}$ versus $T$ at 1 bar); S blast furnace
  cross-section (zones, gas and solid flows, main reactions; temperatures
  only as sourced); S zinc flow sheet (roasting, leaching, cementation,
  electrowinning); AI tapping a blast furnace, molten iron in a runner
  (industrial scene; check colours and protective gear); P a real blast
  furnace (to find, e.g. Landschaftspark Duisburg-Nord); P thermite rail
  welding (to find).
- **Ledger.** `janafG:` $\Delta_f G^\circ$ at 298, 1000, 1500, 2000 K of the
  oxides above, \ce{CO}, \ce{CO2}, \ce{H2O(g)}; `dfh:`/`s0:` for the
  Ellingham-approximation lines (CODATA-KEY/JANAF); `tb:Zn`, `tb:Mg`,
  `tfus:` of the metals (WebBook/PubChem); `usgs:` pig iron and zinc world
  production 2025 (USGS-MCS2026).
- **Exercises palette.** Write the line of \ce{2Zn + O2 -> 2ZnO} (★); read
  the diagram: which metals reduce \ce{Cr2O3} (★); equilibrium oxygen
  pressure of silver oxide at 500 K (★); slope sign of the carbon lines (★);
  thermite: $\Delta_r G^\circ$ and why it is self-heating (★★); temperature
  at which carbon reduces \ce{ZnO} (★★); why zinc leaves the furnace as
  vapour (★★); the Boudouard composition at 1000 K (★★); \ce{H2} as
  reductant of \ce{WO3} (★★); the Kroll process from chloride lines given
  (★★★); variance in the blast furnace's lower zone (★★★); cementation of
  copper by zinc: $K^\circ$ from potentials (★★★).
- **Weekend problem — "Zinc by fire".** I the lines of \ce{ZnO} and of
  \ce{C}/\ce{CO}, with the break at zinc's boiling point; II the crossing
  temperature and the variance of \ce{ZnO + C -> Zn(g) + CO}; III the
  condenser: why zinc vapour reoxidises with \ce{CO2} and how it is
  quenched; IV energy per tonne. **Named number: the lowest temperature at
  which carbon reduces zinc oxide under 1 bar, T ≈ 1.2 × 10³ K.**
  25 questions.

## Ch. 7 — Binary Liquid–Vapour Diagrams and Distillation — `liquid-vapour-diagrams`

- **Hook.** A copper still turns wine into a spirit, and a refinery column
  splits crude oil into a dozen cuts; yet no distillation, however long the
  column, takes ethanol beyond about 96 %.
- **Recall.** \cref{ch:b2:chemical-potential} (Raoult, ideal mixture),
  \cref{ch:b2:equilibrium-shifts} (variance); Year 1 volume: simple
  distillation (lab chapter), miscible liquids; school volume: distillation,
  hydrodistillation.
- **Sections.** 1 Ideal mixtures: isothermal $(p, x)$ and isobaric $(T, x)$
  diagrams, bubble and dew curves from Raoult and Antoine. 2 Reading a
  diagram: variance, the lever rule, heating a mixture step by step. 3 Real
  mixtures and azeotropes (positive and negative deviations; the
  Gibbs–Konovalov theorem). 4 Fractional distillation (the column, theoretical
  plates, the staircase, Fenske's minimum; what an azeotrope does to it).
  5 Partly miscible and immiscible liquids (miscibility gap, heteroazeotrope,
  steam distillation).
- **Definitions.** `def:b2:liquid-vapour-diagrams:binary-diagram` (binary
  diagram, isobaric diagram, isothermal diagram); `:bubble-dew` (bubble
  curve, dew curve, bubble point, dew point); `:azeotrope` (azeotrope,
  positive azeotrope, negative azeotrope); `:fractional-distillation`
  (fractional distillation, theoretical plate, reflux ratio);
  `:miscibility-gap` (miscibility gap, heteroazeotrope); `:steam-distillation`
  (steam distillation). Named-law statement: `thm:…:lever` (lever rule).
- **Ownership check.** Book 2's "used but not defined" list points
  fractional distillation and azeotrope here. Book 1 *distillation* and
  *hydrodistillation*, Book 2 *miscible* recalled, not redefined. *Steam
  distillation* is distinct from Book 1's hydrodistillation (steam injected
  versus boiled with water; the remark says so). Book 4: none.
- **Statements.** `prop:…:ideal-curves` bubble line straight in $(p, x)$, dew
  curve a hyperbola (proof); `prop:…:richer` the vapour is richer in the
  more volatile component (proof); `prop:…:variance` a binary in two
  phases has variance 2, hence 1 at fixed $p$: the compositions of both
  phases are fixed by $T$ (proof); `thm:…:lever`
  (proof: mass balance); `thm:…:konovalov` at an extremum of $T(x)$ or
  $p(x)$, vapour and liquid have the same composition (proof from
  Gibbs–Duhem at fixed $T$, partial; `\admitted` for the isobaric case);
  `prop:…:fenske` minimum number of plates at total reflux, $N_{\min} =
  \ln[(x_D/(1-x_D))((1-x_B)/x_B)]/\ln\alpha$ for constant relative volatility
  $\alpha$ (proof by stepping plate to plate); `prop:…:azeotrope-limit` a
  column cannot cross an azeotrope (proof from the staircase);
  `prop:…:steam` two immiscible liquids boil when $p_1^* + p_2^* = p$, below
  both boiling points; distillate mass ratio $m_1/m_2 = p_1^*M_1/(p_2^*M_2)$
  (proof).
- **Methods.** `met:…:read-diagram` (from a point: phases, compositions,
  amounts); `met:…:predict-distillation` (what distils first, what remains,
  with and without an azeotrope).
- **Figures.** F `liquid-vapour` part a (benzene–toluene isobaric diagram at
  1.013 bar from Raoult + NIST Antoine, heating path and a tie line), part b
  (the same pair, isothermal at 80 °C), part c (positive azeotrope: model
  fitted to the sourced ethanol–water azeotrope), part d (negative
  azeotrope, model), part e (water–immiscible organic: steam distillation
  temperature), part f (staircase of plates for benzene–toluene); S a
  distillation column (plates, downcomers, reflux drum, reboiler); S
  laboratory fractional distillation with the shared pics (`rbflask`,
  `heatingmantle`, a Vigreux column drawn in the figure, `stillhead`,
  `thermometer`, `liebig`, `adapter`); AI copper pot stills in a distillery
  (hook); P refinery distillation columns (to find).
- **Ledger.** `antoine:` benzene, toluene, water, ethanol, and the organic of
  the steam-distillation example (WEBBOOK-PHASE, with T ranges); reuse
  `bp:` rows of Book 2 (water, ethanol, cyclohexane…) read-only; `azeo:`
  ethanol–water azeotrope composition and temperature at 1 atm (source to
  secure; else the model is presented as a model and the 96 % stays
  qualitative); `sol:` mutual solubility of water and butan-1-ol
  (IUPAC-NIST-SDS) for the miscibility gap.
- **Exercises palette.** Read the benzene–toluene diagram (★); bubble point of
  an equimolar mixture by Raoult (★); lever rule (★); variance of three
  situations (★); dew point by iteration (★★); what a simple distillation of
  a 50 % mixture gives (★★); azeotrope: what each end of a column delivers
  (★★); steam distillation: temperature and mass ratio of an essential oil
  (★★); heteroazeotrope reading (★★); Fenske plates for a sharper cut
  (★★★); the isothermal diagram from the isobaric one (★★★); Gibbs–Konovalov
  from Gibbs–Duhem (★★★).
- **Weekend problem — "A column for benzene and toluene".** I the isobaric
  diagram from Antoine and Raoult (a few points computed); II a flash: the
  lever rule at 95 °C; III the column at total reflux: relative volatility,
  Fenske, minimum plates for 95 % products; IV what changes for a pair with an
  azeotrope. **Named number: the minimum number of theoretical plates to
  separate benzene and toluene into 95 % products, N_min ≈ 6.5 (computed
  from the mean relative volatility).** 25 questions.

## Ch. 8 — Binary Solid–Liquid Diagrams — `solid-liquid-diagrams`

- **Hook.** Tin melts at 232 °C and lead at 327 °C, but the old solder of
  electricians melts at about 183 °C, below both; salt on a road melts ice
  only down to about −21 °C.
- **Recall.** \cref{ch:b2:chemical-potential} (cryoscopy),
  \cref{ch:b2:equilibrium-shifts} (variance),
  \cref{ch:b2:liquid-vapour-diagrams} (binary diagrams, lever rule); Year 1
  volume: metallic bonding, alloys (substitutional, interstitial), crystal
  types; Book 2 promised the phase diagrams of alloys.
- **Sections.** 1 Thermal analysis: cooling curves of a pure substance and of
  mixtures; variance on each segment. 2 Total miscibility in the solid:
  the lens (Cu–Ni), the lever rule, cored crystals. 3 No miscibility in the
  solid: the simple eutectic; the liquidus as a cryoscopic curve
  (Schröder–van Laar); the eutectic point. 4 Partial miscibility (Pb–Sn,
  the solid solutions and the eutectic) and defined compounds (congruent
  melting, a diagram split in two). 5 Uses: solders and low-melting alloys,
  de-icing, crystallising a salt.
- **Definitions.** `def:b2:solid-liquid-diagrams:cooling-curve` (thermal
  analysis, cooling curve); `:liquidus` (liquidus, solidus);
  `:solid-solution` (solid solution); `:eutectic` (eutectic point,
  eutectic mixture); `:defined-compound` (defined compound, congruent
  melting).
- **Ownership check.** Not in the map; earliest need (Book 2 promise). Book 2
  *substitutional alloy*, *crystal* recalled. Book 4: none.
- **Statements.** `prop:…:plateaus` a pure substance and a eutectic freeze
  at constant $T$ (variance 0 at fixed $p$) (proof); `thm:…:schroder` liquidus
  of a component A that crystallises pure from an ideal liquid: $\ln x_A =
  -\frac{\Delta_{\text{fus}}H_A}{R}\left(\frac1T - \frac1{T_A^*}\right)$
  (proof: equal $\mu$ of pure solid A and of A in the liquid; generalises
  the cryoscopic law); `cor:…:eutectic` the eutectic is where the two
  liquidus curves meet (proof); `prop:…:lens` ideal solid and liquid
  solutions give a lens (admitted from the same argument applied to both
  phases; computed in figdata); `prop:…:plateau-length` the eutectic plateau
  lasts in proportion to the amount of eutectic liquid (proof: heat balance
  at constant removal rate).
- **Methods.** `met:…:diagram-from-curves` (building a diagram from cooling
  curves); `met:…:read-solid-liquid` (phases, compositions, amounts along a
  cooling path).
- **Figures.** F `solid-liquid` part a (Cu–Ni lens from the ideal model with
  ledger melting points and enthalpies of fusion), part b (simple eutectic
  benzene–naphthalene from Schröder–van Laar), part c (cooling curves: pure,
  off-eutectic, eutectic), part d (Bi–Sn ideal-liquid prediction versus the
  assessed eutectic); S Pb–Sn diagram drawn through the sourced invariant
  points (NIST), regions labelled, a cooling path at 40 % Sn; S a diagram with
  a defined compound (generic A–B with AB₂, two eutectics); AI soldering a
  circuit board (hook); P micrograph of a lamellar Pb–Sn eutectic (to find).
- **Ledger.** `tfus:`/`dfus:` Cu, Ni, Sn, Pb, Bi, benzene, naphthalene
  (WEBBOOK-PHASE / JANAF); `eut:` Pb–Sn and Bi–Sn eutectic temperature and
  composition, Pb–Sn solubility limits (NIST-SOLDER); `eut:` NaCl–water
  eutectic (IUPAC-NIST-SDS, else EXCLUDED and the hook says "about −21 °C"
  only if sourced).
- **Exercises palette.** Read the lens (★); lever rule at 1300 °C (★);
  variance on a plateau (★); cooling curve of a pure metal (★); eutectic
  temperature of an ideal pair by computation (★★); cooling path of a
  hypo-eutectic alloy (★★); de-icing limit with the NaCl–water eutectic
  (★★); defined compound: read compositions (★★); zone refining principle
  from a lens (★★); Schröder–van Laar derivation (★★★); identifying a
  compound's formula from its maximum (★★★); plateau durations from a
  recorded curve (★★★).
- **Weekend problem — "Solder".** I the Pb–Sn diagram from the NIST
  invariant points; II cooling a 40 % tin solder: phases, compositions, lever
  rule at 200 °C and just above the eutectic; III a lead-free solder: the
  Bi–Sn eutectic predicted by the ideal-liquid model; IV comparison with the
  assessed diagram and the choice of solder. **Named number: the eutectic
  temperature of Bi–Sn predicted by the ideal-liquid model (computed),
  against the assessed 139 °C.** 25 questions.

## Ch. 9 — Thermodynamics of Electrochemical Cells — `cell-thermodynamics`

- **Hook.** A hydrogen fuel-cell bus: each cell of its stack gives at most
  1.23 V, and no fuel cell, however perfect, turns all of the energy of its
  hydrogen into electrical work. Both numbers come from tables of Gibbs
  energies.
- **Recall.** Year 1 volume: cells, half-cells, anode, cathode, salt bridge,
  cell voltage, electrode potential, standard potential, the Nernst
  equation (admitted there, "derived in the Year 2 volume"), $\log K$ from
  potentials; \cref{ch:b2:reaction-free-energy},
  \cref{ch:b2:chemical-potential}; school volume (grade 12): the Faraday
  constant and electrolysis.
- **Sections.** 1 Electrical work and the Faraday constant. 2 $\Delta_r G =
  -nFE$ for a cell working reversibly; the inequality for a real cell;
  maximum electrical work. 3 The Nernst equation derived; standard potentials
  from Gibbs energies of formation; combining potentials as adding
  $\Delta_r G^\circ$. 4 Temperature: the temperature coefficient,
  $\Delta_r S^\circ$ and $\Delta_r H^\circ$ from cell data; the thermodynamic
  efficiency of a fuel cell. 5 Concentration cells (voltage, poles, when
  they stop; pH and membrane potentials as examples).
- **Definitions.** `def:b2:cell-thermodynamics:faraday` (Faraday constant —
  **re-found** g12 `cells-and-electrolysis`); `:temperature-coefficient`
  (temperature coefficient of a cell); `:efficiency` (thermodynamic
  efficiency of a fuel cell); `:concentration-cell` (concentration cell).
- **Ownership check.** Map owner ($\Delta_r G = -nFE$, concentration cell;
  re-founds g12). S1 gave the cell vocabulary and the Nernst equation to
  the Year 1 volume: recalled, the theorem is re-derived but its name is not
  re-indexed. Book 4: Butler–Volmer (not used).
- **Statements.** `prop:…:charge` charge passed $= nF\,\Delta\xi$ (proof);
  `thm:…:delta-g-nfe` reversible cell: $\Delta_r G = -nFE$; real cell:
  electrical work delivered $\leq -\Delta_r G\,\Delta\xi$ (proof: first and
  second laws with electrical work); `thm:…:nernst-derived` (proof from
  $\Delta_r G = \Delta_r G^\circ + RT\ln Q$ against the hydrogen electrode,
  conventions $\Delta_f G^\circ(\ce{H+}) = 0$, electrons not counted);
  `prop:…:standard-potential` $E^\circ = -\Delta_r G^\circ/(nF)$ of the
  half-reaction written against \ce{H2} (proof); `prop:…:combining`
  (re-proved as additivity of $\Delta_r G^\circ$); `prop:…:entropy`
  $\Delta_r S^\circ = nF\,\dd E^\circ/\dd T$, $\Delta_r H^\circ = -nF(E^\circ -
  T\,\dd E^\circ/\dd T)$ (proof); `prop:…:efficiency` maximum efficiency
  $\Delta_r G^\circ/\Delta_r H^\circ$, compared with Carnot's (proof);
  `prop:…:concentration-cell` $U = (RT/nF)\ln(c_2/c_1)$ (proof).
- **Methods.** `met:…:e-from-gibbs` (a standard potential from tables);
  `met:…:cell-data` (from $E$ and $\dd E/\dd T$ to $\Delta_r G$, $\Delta_r S$,
  $\Delta_r H$ and the heat released by a working cell).
- **Figures.** S a cell as a thermodynamic system receiving electrical work
  (signs); F `cell-thermodynamics` part a ($E^\circ(T)$ of the
  hydrogen–oxygen cell, liquid and gaseous water, from CODATA/JANAF), part b
  (efficiency $\Delta_r G^\circ/\Delta_r H^\circ$ versus $T$ against a Carnot
  curve); S bar chart of $\Delta_r H^\circ$, $\Delta_r G^\circ$,
  $T\Delta_r S^\circ$ of the fuel cell; S concentration cell with the
  electrochemistry pics (`electrode`, `saltbridge`, `meter`); AI a fuel-cell
  bus at a hydrogen filling station (hook); P M. Faraday (`File:M Faraday Th
  Phillips oil 1842.jpg`, PD, found) in a `history` box (laws of
  electrolysis, 1834).
- **Ledger.** CODATA-KEY rows of ch1–2 reused (\ce{H2O}, \ce{H2}, \ce{O2});
  `janafG:` \ce{H2O(g)} at 298–400 K; Book 2's `dfg:` rows read-only (Zn,
  Cu, Ag, Cl couples); Book 1's `emf:Daniell` read-only; `const:F` shared.
- **Exercises palette.** $E^\circ$ of the hydrogen–oxygen cell from
  $\Delta_f G^\circ$ (★); charge and mass for 1 A h (★); $\Delta_r G$ of the
  Daniell cell (★); concentration-cell voltage (★); $\Delta_r S^\circ$ from
  a measured temperature coefficient (★★); heat released by a working cell
  (★★); $E^\circ(\ce{Fe^3+}/\ce{Fe})$ by adding Gibbs energies (★★); the
  silver chloride electrode from $\Delta_f G^\circ$ (★★); maximum work from
  a zinc anode (★★); efficiency of a methanol fuel cell (★★★); a cell whose
  voltage rises with temperature (★★★); a concentration cell as a pH sensor
  (★★★).
- **Weekend problem — "The fuel-cell bus".** I $E^\circ$ of the
  hydrogen–oxygen cell from Gibbs energies of formation; II temperature:
  $\Delta_r S^\circ$, $\dd E^\circ/\dd T$, the cell at 80 °C; III the real
  cell at 0.70 V: efficiency and heat released per mole of hydrogen; IV the
  tank. **Named number: the electrical energy delivered by 5.0 kg of
  hydrogen at 0.70 V per cell, ≈ 93 kW h.** 25 questions.

## Ch. 10 — Current–Potential Curves — `current-potential-curves`

- **Hook.** Zinc is plated from an acidic solution, although the E–pH
  diagram of the Year 1 volume says that zinc should reduce the acid to
  hydrogen. A diagram says what may happen; a current says how fast.
- **Recall.** Year 1 volume: electrode potential, reference electrode,
  Nernst, E–pH diagrams and their stated limit ("a diagram tells what is
  possible, not how fast"); \cref{ch:b2:cell-thermodynamics}; from physics:
  diffusion and Fick's law.
- **Sections.** 1 An electrode out of equilibrium: the current measures the
  rate of the half-reaction; anodic and cathodic currents; the
  three-electrode set-up. 2 Fast and slow systems; overpotential. 3 Mass
  transport: the diffusion layer, limiting currents, the steady-state wave of a
  fast system. 4 Solvent and electrode: water's electroactivity window and
  its walls, which depend on the electrode material. 5 Reading curves:
  several waves, predicting the reactions at an imposed potential or
  current.
- **Definitions.** `def:b2:current-potential-curves:ie-curve` (current–potential
  curve, anodic current, cathodic current); `:electroactive` (electroactive
  species); `:set-up` (working electrode, counter electrode);
  `:overpotential` (overpotential, threshold potential); `:fast-slow` (fast
  system, slow system); `:limiting-current` (diffusion layer, limiting
  current); `:window` (electroactivity window, solvent wall).
- **Ownership check.** Map owner (i–E curve, overpotential, fast/slow
  system). Book 2 owns *reference electrode*, *electrode potential*:
  recalled. Book 4 owns Butler–Volmer, Tafel, voltammetry: slow-system shapes
  are drawn as a model and the kinetics is `\admitted` with "the Year 3
  volume derives the shape of the rising part". Physics owns diffusion.
- **Statements.** `prop:…:current-rate` $i = nF\,\dd\xi/\dd t$, sign
  convention (proof); `prop:…:zero-current` a fast system with both forms
  present is at its Nernst potential when no current flows (argued);
  `thm:…:limiting` $i_{\lim} = nFADc/\delta$ (proof: steady linear profile
  in the diffusion layer, surface concentration zero);
  `thm:…:wave` fast system: $E = E_{1/2} + \frac{RT}{nF}\ln
  \frac{i_{\lim,c} - i}{i - i_{\lim,a}}$ with signed limiting currents and
  $E_{1/2} = E^\circ + \frac{RT}{nF}\ln(D_{\text{red}}/D_{\text{ox}})$ (same layer thickness for both forms) (proof:
  Nernst at the surface + linear fluxes in the layer); `cor:…:half-wave` $E_{1/2} =
  E^\circ$ for equal diffusion coefficients; `prop:…:plateau` plateau heights
  proportional to concentrations (amperometric analysis);
  `prop:…:window` the window of water is set by the two walls, each shifted
  from its Nernst potential by an overpotential that depends on the
  electrode (argued; values as sourced or as a model).
- **Methods.** `met:…:sketch-ie` (sketch the curves of a solution from
  $E^\circ$, fast/slow, concentrations, the walls); `met:…:read-ie` (what
  happens at an imposed potential; at an imposed current).
- **Figures.** S three-electrode cell with the electrochemistry pics
  (`beaker`, three `electrode`s, `meter` for V and A, a potentiostat box);
  S concentration profile in the diffusion layer; F `ie-curves` part a (fast
  couple with both forms: two plateaus, zero current at the Nernst
  potential), part b (only the reduced form present), part c (slow system:
  separated branches, overpotentials), part d (water on platinum and on a
  metal of high hydrogen overpotential, model), part e (plateau versus
  concentration); AI an electroplating line in a workshop (hook); P
  Jaroslav Heyrovský (to find) in a `history` box (polarography, 1922).
- **Ledger.** Standard potentials from Book 2 rows (read-only);
  diffusion coefficients and layer thickness are model values of the
  figure (said in the caption, no row); hydrogen overpotentials on metals
  only if an open primary source is found (else qualitative, EXCLUDED).
- **Exercises palette.** Signs of currents at the two electrodes of a cell
  (★); limiting current from $D$, $\delta$, $c$ (★); identify fast and slow
  systems on curves (★); the half-wave potential (★); read a two-wave curve
  (★★); what is deposited at an imposed potential (★★); window of water in
  acid and in base (★★); amperometric titration endpoint (★★); the effect of
  stirring on a plateau (★★); derive the wave equation (★★★); a reaction
  that runs although thermodynamics says it should be overtaken (zinc and
  hydrogen) (★★★); choosing an electrode for an oxidation beyond the water
  wall (★★★).
- **Weekend problem — "An oxygen probe for a river".** I the cathode of an
  amperometric oxygen sensor (\ce{O2} reduction, slow, at a potential on its
  plateau); II the limiting current across the membrane, proportional to
  the dissolved oxygen; III calibration in air-saturated water (Henry's law
  from \cref{ch:b2:chemical-potential}); IV a river sample. **Named number:
  the dissolved-oxygen concentration of the sample in mg/L (exercise data,
  computed from the current ratio).** 25 questions.

## Ch. 11 — Batteries, Fuel Cells and Electrolysis — `batteries-electrolysis`

- **Hook.** Making one aluminium drinks can costs as much electricity as
  several hours of a laptop; recycling it costs a few per cent of that. The
  difference is an electrolysis cell running at about 4 V and 300 kA.
- **Recall.** \cref{ch:b2:cell-thermodynamics},
  \cref{ch:b2:current-potential-curves}; school volume: electrolysis,
  accumulators; Book 2 promised the aluminium electrolysis and the alkali
  metals from molten chlorides.
- **Sections.** 1 Spontaneous reactions read on i–E curves: a single beaker
  (mixed potential; zinc in acid, slow alone, fast in contact with copper).
  2 Cells delivering current: $U = E_+ - E_- - \eta_a - |\eta_c| - RI$;
  Daniell, alkaline, lead–acid and lithium-ion cells; capacity and specific
  energy. 3 Fuel cells (proton-exchange membrane cell, voltage losses).
  4 Electrolysis: minimum voltage, overpotentials, ohmic drop; faradaic
  efficiency; energy per kilogram. 5 Industrial electrolyses: zinc
  electrowinning (why zinc beats hydrogen on zinc), chlorine and sodium
  hydroxide (membrane cell), aluminium (Hall–Héroult), sodium (molten
  chloride).
- **Definitions.** `def:b2:batteries-electrolysis:mixed-potential` (mixed
  potential — moved from ch12 inside this book, earliest need);
  `:battery` (primary cell, accumulator — **re-found** g12, specific
  energy); `:fuel-cell` (fuel cell); `:electrolysis` (electrolysis —
  **re-found** g12, electrolyser); `:faradaic-efficiency` (faradaic
  efficiency, specific energy consumption).
- **Ownership check.** Not in the map's seed except as recalls; re-founds
  g12 *electrolysis*, *accumulator* (Book 1 owns them at school level;
  Book 2 did not define them). *Mixed potential* was given to this book's
  ch12 by S1; it is needed first here (report point 8). Book 4:
  electrode kinetics (pointer only).
- **Statements.** `prop:…:mixed` a metal with two couples settles where
  $i_a(E) = -i_c(E)$ (proof: no net current); `prop:…:delivering` voltage of
  a cell delivering current (proof from the curves); `prop:…:electrolysis-voltage`
  $U \geq (E_a - E_c) + \eta_a + |\eta_c| + RI$ (proof);
  `prop:…:faraday-mass` $m = \eta_F MIt/(nF)$ (proof; Faraday's law
  re-derived); `prop:…:energy` energy per kilogram $= nFU/(\eta_F M)$
  (proof); `prop:…:minimum-voltage` thermodynamic minimum $\Delta_r G/(nF)$
  for a forced reaction (proof).
- **Methods.** `met:…:predict-electrolysis` (which reaction at each
  electrode, from superposed curves); `met:…:operating-point` (operating
  voltage of a cell or electrolyser).
- **Figures.** F `ie-curves` part f (mixed potential of zinc in acid,
  without and with copper contact), part g (electrolysis of acidic zinc
  sulfate: zinc deposits before hydrogen on a zinc cathode), part h
  (operating point of a battery); S lead–acid accumulator; S lithium-ion cell
  (graphite, layered oxide, \ce{Li+} shuttle on charge and discharge); S
  Hall–Héroult cell cross-section (carbon anodes, cryolite bath, liquid
  aluminium, cathode block); S membrane chlor-alkali cell; AI aluminium
  smelter potroom (hook); P C. M. Hall (`File:Charles Martin Hall
  1880s.jpg`, PD, found) and P. Héroult (`File:PaulHeroult.jpg`, PD, found)
  in a `history` box (1886); P Volta's pile (`File:VoltaBattery.JPG`, CC
  BY-SA 3.0, found) in a second `history` box (1800).
- **Ledger.** Book 2 `dfg:` rows read-only for $E^\circ$ (Zn, Cu, Pb,
  \ce{PbO2}, \ce{SO4^2-}); `dfg:PbSO4_cr`, `dfg:HSO4-_ao` if missing (NBS-82);
  `janafG:` \ce{Al2O3}, \ce{CO2} at 1250 K (minimum voltage of the
  Hall–Héroult cell); `iai:` primary aluminium smelting energy intensity
  (IAI, latest year); `usgs:` world aluminium and zinc production 2025
  (USGS-MCS2026).
- **Exercises palette.** Read a mixed potential (★); mass of zinc deposited
  in an hour at 500 A (★); voltage of a lead–acid cell from $E^\circ$ (★);
  capacity in A h of a given mass of lithium (★); faradaic efficiency from
  a deposited mass (★★); energy per kilogram of zinc (★★); a battery's voltage
  falls with current: internal resistance (★★); products of the
  electrolysis of brine (★★); molten sodium chloride (★★); why zinc can be
  plated from acid (curves) (★★★); minimum voltage of the Hall–Héroult cell
  from $\Delta_r G^\circ$ at 1250 K (★★★); a fuel cell and an electrolyser in
  a loop: round-trip efficiency (★★★).
- **Weekend problem — "One tonne of aluminium".** I the cell reaction
  \ce{2Al2O3 + 3C -> 4Al + 3CO2} and its thermodynamic minimum voltage;
  II charge and time per tonne at 300 kA; III energy at 4.1 V and 94 %
  faradaic efficiency, compared with the IAI figure; IV carbon consumed and
  \ce{CO2} emitted per tonne. **Named number: the electrical energy per
  kilogram of aluminium, ≈ 13 kW h/kg.** 26 questions.

## Ch. 12 — Corrosion and Protection — `corrosion`

- **Hook.** A drop of salt water left on clean steel: after a day the metal
  is pitted at the centre of the drop and the rust has formed in a ring near
  its edge, where the oxygen is. Corrosion is a cell that nobody built.
- **Recall.** Year 1 volume: E–pH diagrams, immunity, corrosion and
  passivation domains ("whether a coat protects is a kinetic matter, treated
  in the Year 2 volume"); \cref{ch:b2:current-potential-curves},
  \cref{ch:b2:batteries-electrolysis} (mixed potential); school volume:
  corrosion, rust, galvanising.
- **Sections.** 1 Wet corrosion as a short-circuited cell: uniform
  corrosion, corrosion potential and current. 2 Differential corrosion: two
  metals in contact (galvanic corrosion), one metal in two environments
  (differential aeration, crevices, the water line). 3 Passivation: the
  curve with its passive plateau; stainless steels. 4 Protection: coatings
  (paint, zinc, tin), cathodic protection by sacrificial anodes and by
  imposed current, inhibitors.
- **Definitions.** `def:b2:corrosion:uniform` (uniform corrosion, corrosion
  potential, corrosion current); `:differential` (differential corrosion,
  galvanic corrosion, differential aeration); `:passivation` (passivation,
  passive film); `:protection` (cathodic protection, sacrificial anode,
  impressed-current protection).
- **Ownership check.** S1: this chapter owns *passivation* (the phenomenon)
  and *differential corrosion*; *mixed potential* moved to ch11. Book 2 owns
  the three domains (recalled). Book 1 owns *corrosion*, *rust*,
  *galvanising* (used, not redefined).
- **Statements.** `prop:…:rate` corrosion rate from $i_{\text{corr}}$, as a
  mass loss and as a thickness per year (proof); `prop:…:galvanic` two
  metals in contact: the one with the lower corrosion potential becomes the
  anode and corrodes faster, the other is protected (proof: superposed
  curves, a single mixed potential); `prop:…:aeration` the less aerated zone
  is anodic (proof: oxygen limiting current and Nernst);
  `prop:…:passivity` the passive plateau and its breakdown (argued; curve as
  a model); `prop:…:anode-life` lifetime of a sacrificial anode $t =
  \eta mnF/(MI)$ (proof).
- **Methods.** `met:…:diagnose` (find anode and cathode in a corrosion
  situation); `met:…:choose-protection`.
- **Figures.** F `ie-curves` part i (Evans diagram: iron oxidation and
  diffusion-limited oxygen reduction; corrosion potential and current), part
  j (iron coupled to zinc and to copper), part k (active–passive–transpassive
  curve, model); S Evans drop cross-section (anodic centre, cathodic rim,
  rust ring, current lines); S cathodic protection of a buried pipe:
  sacrificial anode and imposed current; S a scratch in galvanised and in
  tinned steel; AI rust streaks on a steel bridge (hook); P Statue of
  Liberty's copper patina (`File:Statue of Liberty 7.jpg`, PD, found);
  P sacrificial anodes on a hull or a galvanised surface (to find).
- **Ledger.** Book 2 `dfg:`-based potentials read-only (Fe, Zn, Cu, Mg,
  Al); reuse Book 2 `sol:O2` and `ph:seawater` read-only.
- **Exercises palette.** Corrosion rate from a current density (★); which
  metal corrodes in a couple (★); differential aeration in a crevice (★);
  galvanised versus tinned steel scratched (★); corrosion current read on an
  Evans diagram (★★); zinc anode lifetime (★★); magnesium versus zinc anodes
  in soil and sea water (★★); imposed current for a buried pipe (★★); the
  water line of a pile in the sea (★★); passive stainless steel and chloride
  pitting (★★★); a copper fitting on a steel pipe: current and rate
  (★★★); over-protection and hydrogen (★★★).
- **Weekend problem — "Protecting a pipeline".** I a bare steel pipe in wet
  soil: corrosion current and wall loss per year; II choice of the anode
  metal from the potentials; III design: current demand of the coated pipe,
  anode mass for twenty years; IV the impressed-current alternative and the
  limits of over-protection. **Named number: the mass of magnesium anodes for
  twenty years of protection (exercise data, computed).** 24 questions.

## Ch. 13 — Atomic Orbitals: Shapes, Energies and Sizes — `atomic-orbitals`

- **Hook.** A hydrogen atom has no edge: its electron can be found at any
  distance from the nucleus, yet the atom has a size, and sodium is twice as
  wide as chlorine. What the Year 1 volume called an orbital by its three
  quantum numbers is, here, a function with a shape.
- **Recall.** Year 1 volume: quantum numbers, atomic orbital as the state
  $(n, l, m_l)$, shells and subshells, screening and effective nuclear
  charge (qualitative), configurations, the hydrogen levels $-E_R/n^2$; from
  physics: the wavefunction and $|\psi|^2$ as a probability density.
- **Sections.** 1 The wavefunctions of the hydrogen atom: $\psi_{nlm} =
  R_{nl}(r)Y_{lm}(\theta, \varphi)$, normalisation, probability density.
  2 The radial part: radial distribution, most probable radius, radial nodes.
  3 The angular part: real orbitals s, p, d; angular nodes; the sign of a
  lobe. 4 Many-electron atoms: Slater's rules, orbital energies and radii.
  5 Using them: ionisation energies, the 4s/3d order, sizes along a period
  and down a group.
- **Definitions.** `def:b2:atomic-orbitals:wavefunction` (wavefunction,
  probability density); `:radial-angular` (radial part, angular part);
  `:radial-distribution` (radial distribution function, most probable
  radius); `:node` (nodal surface, radial node, angular node); `:slater`
  (Slater's rules); `:orbital-energy` (orbital energy, orbital radius).
- **Ownership check.** S1: *atomic orbital*, *screening*, *effective nuclear
  charge* belong to the Year 1 volume (recalled); this chapter owns
  *wavefunction*, *radial part*, *angular part*, *radial distribution*,
  *nodal surface*, *Slater's rules*. Book 4 owns the Schrödinger equation
  (formal) and model systems: the hydrogen functions are `\admitted` with
  "solved in the Year 3 volume". No Book 1 notion re-found.
- **Statements.** `thm:…:hydrogen` table of $R_{nl}$ ($n \leq 3$) and of the
  real angular functions (`\admitted`, Year 3); `prop:…:normalised`
  $\int_0^\infty P_{1s}\,\dd r = 1$ (proof, integration by parts);
  `prop:…:most-probable` $r_{\max} = n^2a_0/Z$ for $l = n - 1$, $a_0/Z$ for 1s
  (proof by derivation); `prop:…:nodes` $n - l - 1$ radial and $l$ angular
  nodes (checked on the table; general case admitted); `prop:…:mean-radius`
  $\langle r\rangle_{1s} = 3a_0/(2Z)$ (proof); `prop:…:slater-energy`
  $\varepsilon \approx -E_R Z^{*2}/n^{*2}$, radius $n^{*2}a_0/Z^*$ (model,
  `\admitted`); `prop:…:ionisation` first ionisation energy as a difference
  of Slater energies (method + comparison with measured values).
- **Methods.** `met:…:slater` (computing $Z^*$); `met:…:draw-orbital`
  (sketch from $n, l, m_l$: nodes, lobes, signs).
- **Figures.** F `atomic-orbitals` part a (radial distributions 1s, 2s, 2p,
  3s, 3p, 3d for $Z = 1$), part b ($R_{2s}$ and $R_{3s}$ changing sign), part
  c (dot-density picture of 1s and 2s, deterministic sampling), part d
  ($Z^*$ and Slater radius of the valence orbital along period 2 and down
  group 1); S real orbitals s, p, d with lobes and signs (orbital-lobe pics,
  report point 4); S Slater's grouping chart; P E. Schrödinger
  (`File:Erwin Schrödinger (1933).jpg`, PD, found) in a `history` box (1926).
  No AI (nothing here can simply be seen).
- **Ledger.** `const:a0`, `const:RyhcEV` (shared); Book 2 `ie:` rows
  read-only for the comparison; Slater's rules are a model (cite Slater 1930
  in the chapter comment, no number about a substance).
- **Exercises palette.** Quantum numbers and nodes of 3p, 4d (★); $r_{\max}$
  of 2p (★); probability inside $a_0$ for 1s (★); sketch $3d_{xy}$ (★); $Z^*$
  of a 2p electron of oxygen (★★); 4s or 3d first? $Z^*$ for iron (★★);
  first ionisation energies of Li and Na by Slater versus measured (★★);
  sizes: why \ce{Na} is larger than \ce{Cl} (★★); orthogonality of 1s and
  2s (★★); normalise $R_{2p}$ (★★★); $\langle r\rangle$ of 1s and the most
  probable radius compared (★★★); the angular node of $p_z$ and its
  plane (★★★).
- **Weekend problem — "Where is the electron?".** I the 1s function:
  normalisation, most probable and mean radii; II the probability of finding
  the electron beyond a radius; III 2s and 2p: nodes and maxima of the
  radial distributions; IV Slater: $Z^*$ and energies for C, N, O and the
  comparison with measured ionisation energies. **Named number: the
  probability of finding the 1s electron of hydrogen farther than $2a_0$,
  $13\,\mathrm e^{-4} \approx 0.238$.** 25 questions.

## Ch. 14 — Molecular Orbitals of Diatomic Molecules — `diatomic-mos`

- **Hook.** Liquid oxygen poured between the poles of a strong magnet hangs
  there; liquid nitrogen runs straight through. A Lewis structure of \ce{O2}
  pairs every electron and cannot explain it.
- **Recall.** \cref{ch:b2:atomic-orbitals}; Year 1 volume: Lewis structures,
  σ and π bonds (descriptive), hybridisation and its stated limit ("molecular
  orbital theory, in the Year 2 volume"), unpaired electrons.
- **Sections.** 1 LCAO: two identical orbitals; the 2 × 2 secular system,
  overlap, Coulomb and resonance integrals; bonding and antibonding levels
  and functions. 2 Overlap and symmetry: σ and π orbitals; zero overlap by
  symmetry; the three conditions for an interaction. 3 Homonuclear diatomics
  of period 2 (with and without s–p mixing), bond order, magnetism (\ce{O2},
  \ce{N2}, \ce{F2}, \ce{B2}, \ce{C2}; \ce{O2+}, \ce{O2-}, \ce{O2^2-}).
  4 Heteronuclear diatomics: unequal energies, polarised orbitals (HF, CO,
  NO); the lone pair of CO on carbon. 5 Bond order, length and energy.
- **Definitions.** `def:b2:diatomic-mos:lcao` (molecular orbital, LCAO);
  `:integrals` (overlap integral, Coulomb integral, resonance integral,
  secular determinant); `:bonding` (bonding orbital, antibonding orbital,
  nonbonding orbital); `:sigma-pi` (σ orbital, π orbital); `:bond-order`
  (bond order); `:magnetism` (paramagnetic, diamagnetic).
- **Ownership check.** Map owner (LCAO, bonding/antibonding MO, bond order);
  S1 gave this chapter the MO terms *σ orbital*, *π orbital* while *σ bond*,
  *π bond*, *hybridisation* stay with the Year 1 volume (recalled).
  *Paramagnetic*/*diamagnetic*: not in the map, Book 4 ch18 treats magnetic
  susceptibility and moments — earliest need claimed here, contested low
  (report point 2). HOMO/LUMO stay with ch17 (plain words "highest occupied
  level" before).
- **Statements.** `thm:…:homonuclear` $E_\pm = (\alpha \pm \beta)/(1 \pm S)$
  and $\psi_\pm = (\varphi_A \pm \varphi_B)/\sqrt{2(1\pm S)}$ (proof: 2 × 2
  secular determinant); `prop:…:asymmetry` the antibonding level rises more
  than the bonding one falls (proof, $S > 0$); `thm:…:heteronuclear` for
  $\alpha_A \neq \alpha_B$, $S$ neglected: $E_\pm = \bar\alpha \mp \sqrt{\Delta^2/4 +
  \beta^2}$, the bonding orbital weighted on the lower atom (proof: eigenvalues
  and eigenvectors of a symmetric 2 × 2 matrix); `prop:…:symmetry` orbitals
  of opposite symmetry with respect to a plane containing the axis have zero
  overlap (proof: odd integrand); `prop:…:bond-order` $b = (n_b - n_a)/2$;
  `prop:…:sp-mixing` the inversion of the σ and π levels from \ce{B2} to
  \ce{N2} (argued from the 2s–2p gap; `\admitted` quantitatively).
- **Methods.** `met:…:build-diagram` (MO diagram of a diatomic);
  `met:…:fill` (fill, bond order, unpaired electrons, magnetism).
- **Figures.** S modiagram of \ce{H2} and \ce{He2}; S modiagrams of \ce{N2}
  (with mixing) and \ce{O2} (without) side by side; S modiagram of CO (and
  HF); S lobes of σ, σ*, π, π* built from 1s and 2p (orbital-lobe pics);
  F `two-level` part a (exact $E_\pm$ versus $\Delta/|\beta|$ with the
  perturbative limits — reused in ch17); F `diatomics` (bond order against
  bond length and dissociation energy for \ce{O2^{n}} ions and the period-2
  molecules, ledger points); P liquid oxygen held by a magnet (to find; a
  photograph only); P R. Mulliken or F. Hund (to find) in a `history` box.
- **Ledger.** Book 2 `re:` rows read-only (\ce{H2}, \ce{N2}, \ce{O2},
  \ce{F2}, CO, HF); new `re:`/`d0:` for \ce{O2+}, NO, \ce{B2}, \ce{C2},
  \ce{Li2}, \ce{N2+} and $D_0$ of all (WEBBOOK-DIAT); `ie:O2` (Book 2
  read-only), `ie:N2`, `ie:CO` (WEBBOOK-IEMOL); superoxide and peroxide
  bond lengths from crystal structures (COD, as Book 2 did) or EXCLUDED.
- **Exercises palette.** \ce{H2+} and \ce{H2}: energies with $S$ (★); bond
  orders of \ce{He2}, \ce{Li2}, \ce{B2} (★); paramagnetic or not (★); zero
  overlap pairs (★); \ce{N2} versus \ce{N2+} bond length (★★); CO
  isoelectronic with \ce{N2}: polarised orbitals (★★); HF: which orbitals
  interact (★★); the heteronuclear formula with numbers (★★); \ce{C2} and
  its two π bonds (★★); NO and \ce{NO+} (★★★); the sum $E_+ + E_-$ and the
  four-electron destabilisation (★★★); bond energies of \ce{O2^{n}}
  ordered and compared with the ledger (★★★).
- **Weekend problem — "Oxygen and its ions".** I the MO diagram of \ce{O2},
  bond order, magnetism; II \ce{O2+}, \ce{O2-}, \ce{O2^2-}: bond orders and
  predicted lengths against the ledger; III ionisation: which electron
  leaves, why the ion's bond is shorter, dissociation energies; IV the two
  ways of pairing the π* electrons (a low-lying excited state, qualitatively).
  **Named number: the bond order of the dioxygenyl ion \ce{O2+}, 2.5, and its
  measured bond length (ledger, ≈ 112 pm).** 25 questions.

## Ch. 15 — Fragment Orbitals and Polyatomic Molecules — `fragment-orbitals`

- **Hook.** A photoelectron spectrum of water shows four bands, not the two
  "equivalent lone pairs" and two "equivalent bonds" of its Lewis structure;
  methane shows two, not one.
- **Recall.** \cref{ch:b2:diatomic-mos}; Year 1 volume: VSEPR, hybridisation
  as a description, resonance, carbocations (with the promise of the
  "interaction of C–H bonds with the empty orbital, described in the Year 2
  volume").
- **Sections.** 1 The fragment method: two fragments, their orbitals,
  symmetry-adapted combinations (the \ce{H2} pair, the three H of \ce{NH3},
  the four H of \ce{CH4}). 2 Water: the bent molecule from O and \ce{H2}
  fragments; why bent (a Walsh-type argument); its four valence levels.
  3 Methane and ammonia; photoelectron spectra and Koopmans' approximation;
  delocalised orbitals versus localised bonds. 4 Ethene from two \ce{CH2}
  fragments: π and π*, planarity and the barrier to rotation.
  5 Hyperconjugation: carbocation stability and conformations.
- **Definitions.** `def:b2:fragment-orbitals:fragment` (fragment, fragment
  orbital); `:symmetry-adapted` (symmetry-adapted combination);
  `:photoelectron` (photoelectron spectroscopy); `:hyperconjugation`
  (hyperconjugation).
- **Ownership check.** Map owner (fragment orbital, symmetry-adapted
  combination). Book 4 owns *point group*, *symmetry operation*, *character
  table*: here symmetry is argued with mirror planes and rotations in plain
  words, and orbital labels are called names, with "the Year 3 volume derives
  them from group theory". Book 2's *hybridisation*, *VSEPR* recalled.
  *Photoelectron spectroscopy* and *hyperconjugation* not in the map:
  earliest need (Book 2's list sends hyperconjugation here).
- **Statements.** `prop:…:h2-pair` the two combinations $h_1 \pm h_2$
  (proof: unchanged or sign-reversed by the exchange of the H atoms);
  `prop:…:h4` one totally symmetric and three degenerate combinations of
  four tetrahedral H (argued; `\admitted` from group theory);
  `prop:…:interaction-rules` only combinations of the same symmetry interact
  (proof via the zero-overlap proposition of ch14); `prop:…:koopmans`
  ionisation energy ≈ minus the orbital energy (`\admitted`, Year 3
  computational chemistry); `prop:…:bent-water` bending lowers the occupied
  in-plane level (argued); `prop:…:hyperconjugation` stabilisation of a
  carbocation grows with the number of C–H and C–C bonds parallel to the
  empty p orbital (argued with the two-orbital result).
- **Methods.** `met:…:fragment-diagram` (choose fragments, build combinations,
  match symmetry and energy, fill, read).
- **Figures.** S fragment diagram of water (O 2s, 2p against the \ce{H2}
  combinations, energy levels with the shared level pics); S fragment
  diagram of methane; S ethene π and π* from two \ce{CH2}; S hyperconjugation
  (C–H σ lobe beside the empty p of a carbocation); F `photoelectron`
  (schematic band spectra of water and methane at ledger ionisation
  energies — only if the band energies are sourced; else S level diagram
  without numbers).
- **Ledger.** Book 2 `geo:` rows read-only (\ce{H2O}, \ce{NH3}, \ce{CH4},
  \ce{C2H4}); `pe:` vertical ionisation energies of the valence bands of
  \ce{H2O}, \ce{CH4}, \ce{NH3} (source to secure — at risk; first IEs from
  WEBBOOK-IEMOL in any case); ethene torsion barrier (source to secure, else
  qualitative).
- **Exercises palette.** Combinations of two H (★); number of MOs and
  electrons in water (★); photoelectron bands of \ce{CH4} (★); planar
  ethene (★); ammonia's lone pair as its highest level (★★); linear versus
  bent \ce{H2O} (★★); hyperconjugation and the order of carbocations (★★);
  twisted ethene: π overlap at 90° (★★); \ce{BH3} versus \ce{NH3} (★★);
  \ce{H3+} triangle (★★★); allyl from three p orbitals (bridge to Hückel)
  (★★★); \ce{CO2}'s π system from fragments (★★★).
- **Weekend problem — "The shape of water".** I fragments O and \ce{H2}:
  combinations; II the linear molecule's diagram; III bending: which levels
  move and why water is bent; IV the photoelectron spectrum: four bands,
  Koopmans, and what becomes of the "two equivalent lone pairs". **Named
  number: four valence ionisation bands for water, the lowest at ≈ 12.6 eV
  (ledger).** 24 questions.

## Ch. 16 — Hückel Theory and Conjugated Systems — `huckel`

- **Hook.** Three double bonds in a ring of six carbons: adding hydrogen to
  benzene releases about 150 kJ/mol less than three times the value for
  cyclohexene. That missing energy is the stability of an aromatic ring,
  and a determinant computes it.
- **Recall.** \cref{ch:b2:diatomic-mos} ($\alpha$, $\beta$, secular
  determinant), \cref{ch:b2:fragment-orbitals}; Year 1 volume: resonance,
  conjugated system, chromophore, absorption maximum.
- **Sections.** 1 The Hückel method: σ–π separation; approximations ($S =
  0$, $\alpha$, $\beta$ between neighbours, 0 otherwise); the secular
  determinant in $x = (\alpha - E)/\beta$. 2 Linear polyenes: ethene, allyl,
  butadiene, hexatriene; the closed form. 3 What the coefficients give: π
  charges, π bond indices, delocalisation energy. 4 Rings: benzene,
  cyclobutadiene, cyclopentadienyl, tropylium; Frost's circle; Hückel's rule,
  aromatic and antiaromatic. 5 Conjugation and light: the gap narrows with
  length; heteroatoms (a model).
- **Definitions.** `def:b2:huckel:method` (Hückel method); `:indices`
  (π charge, π bond index); `:delocalisation` (delocalisation energy);
  `:aromatic` (aromatic, antiaromatic). Named-law statement:
  `thm:…:huckel-rule` (Hückel's rule).
- **Ownership check.** Map owner (Hückel method, delocalisation energy,
  aromaticity rule). Book 2 owns *conjugated system*, *chromophore*,
  *resonance hybrid*: recalled. Book 1: nothing. Book 4: group theory, SCF
  (pointer).
- **Statements.** `thm:…:polyene` $E_k = \alpha + 2\beta\cos(k\pi/(n+1))$,
  $c_{jk} \propto \sin(jk\pi/(n+1))$ (proof: substitute into $c_{j-1} + xc_j +
  c_{j+1} = 0$ with $c_0 = c_{n+1} = 0$); `thm:…:ring` $E_k = \alpha +
  2\beta\cos(2\pi k/n)$ (proof with $c_j = \mathrm e^{2\mathrm i\pi kj/n}$,
  then real combinations); `cor:…:frost` Frost's circle; `thm:…:huckel-rule`
  a planar monocycle has a closed shell iff it holds $4N + 2$ π electrons
  (proof from the level pattern); `prop:…:trace` $\sum E_k = n\alpha$ (proof:
  trace); `prop:…:alternant` charges equal to 1 in neutral alternant
  hydrocarbons (`\admitted`, Coulson–Rushbrooke; checked numerically);
  `prop:…:gap` the HOMO–LUMO gap of a linear polyene $4|\beta|\sin(\pi/(2(n+1)))$
  falls with $n$ (proof).
- **Methods.** `met:…:huckel` (graph, matrix, determinant, fill, $E_\pi$,
  charges, indices); `met:…:aromaticity` (cyclic, planar, fully conjugated,
  $4N + 2$).
- **Figures.** F `huckel` part a (level diagrams of ethene, allyl, butadiene,
  hexatriene, benzene, cyclobutadiene from computed eigenvalues), part b (gap
  versus chain length), part e (coefficients used for lobe sizes); S
  butadiene's four π orbitals as lobes scaled by coefficients; S Frost's
  circles for \ce{C4H4}, \ce{C5H5-}, \ce{C6H6}, \ce{C7H7+}; S hydrogenation
  enthalpy ladder (cyclohexene ×1, ×2, ×3 versus benzene, ledger); P A.
  Kekulé (to find) in a `history` box (1865).
- **Ledger.** `dhyd:` cyclohexene, cyclohexa-1,3-diene, benzene
  (WEBBOOK-THERMO, reaction data); Book 2 `geo:C6H6.rCC` read-only;
  butadiene bond lengths (CCCBDB); polyene absorption maxima only if sourced
  (Book 2 found none: likely EXCLUDED).
- **Exercises palette.** Allyl cation, radical, anion energies (★); $E_\pi$
  of butadiene (★); aromatic or not: six species (★); Frost's circle of
  \ce{C8H8} (★); delocalisation energy of butadiene (★★); bond indices and
  lengths in butadiene (★★); cyclopentadienyl anion and cation (★★);
  tropylium (★★); trace check on hexatriene (★★); the closed form for
  hexatriene (★★★); cyclobutadiene: triplet and rectangle (★★★); a
  heteroatom in a chain, model parameters (★★★).
- **Weekend problem — "Benzene's missing energy".** I hydrogenation
  enthalpies: the stabilisation of benzene; II Hückel for benzene: determinant,
  levels, $E_\pi$; III delocalisation energy $2|\beta|$ and the value of
  $|\beta|$ matched to experiment; IV hexatriene against benzene, and
  cyclo-octatetraene. **Named number: $|\beta| \approx 75$ kJ/mol, obtained by
  matching benzene's delocalisation energy to its measured stabilisation.**
  25 questions.

## Ch. 17 — Frontier Orbitals and Reactivity — `frontier-orbitals`

- **Hook.** A bottle of cyclopentadiene left on the shelf slowly turns into
  its dimer: two molecules of the same diene join into a bicyclic ring, with
  one stereochemistry only. Two orbitals, one on each molecule, decide it.
- **Recall.** \cref{ch:b2:diatomic-mos} (two-level interaction),
  \cref{ch:b2:huckel} (coefficients, levels); Year 1 volume: nucleophile,
  electrophile, curly arrows, kinetic control, stereospecific,
  regioselective and stereoselective reactions, electrophilic additions.
- **Sections.** 1 Interaction of two orbitals revisited: the stabilisation
  $\approx\beta^2/|\Delta\varepsilon|$; two-electron (stabilising) and
  four-electron (destabilising) interactions. 2 Frontier orbitals: HOMO,
  LUMO; a nucleophile gives from its HOMO, an electrophile takes in its LUMO;
  charge control and orbital control; hard and soft species. 3 Reading
  reactivity: ambident nucleophiles (cyanide, enolates — preview of ch25),
  addition to a carbonyl (the angle of approach), the back-side attack of SN2
  (σ*). 4 The Diels–Alder reaction: diene HOMO and dienophile LUMO; s-cis
  diene; concerted and stereospecific; regioselectivity from the
  coefficients ("ortho–para"); the endo rule; electron demand.
- **Definitions.** `def:b2:frontier-orbitals:frontier` (HOMO, LUMO, frontier
  orbitals); `:control` (charge control, orbital control); `:hard-soft`
  (hard nucleophile, soft nucleophile, hard electrophile, soft electrophile —
  defined as phrases, so that the bare words stay unlinked); `:ambident`
  (ambident nucleophile); `:concerted` (concerted reaction); `:diels-alder`
  (Diels–Alder reaction, diene, dienophile); `:endo` (endo adduct, exo
  adduct, endo rule).
- **Ownership check.** Map owner (HOMO, LUMO, frontier orbitals, Diels–Alder
  in the frontier-orbital view). Book 4 owns *pericyclic reaction* and the
  Woodward–Hoffmann rules: "cycloaddition" appears as a plain word with "the
  Year 3 volume classifies these reactions". *Concerted reaction*,
  *ambident*, hard/soft: not in the map, earliest need (Book 4's pericyclic
  chapter would recall *concerted*) — report point 2.
- **Statements.** `thm:…:perturbation` for $|\beta| \ll |\Delta\varepsilon|$
  the lower level falls by $\approx\beta^2/|\Delta\varepsilon|$ and the upper
  rises as much (proof: Taylor expansion of the exact 2 × 2 eigenvalues);
  `prop:…:four-electron` two filled orbitals repel (proof from the
  asymmetry of ch14); `prop:…:dominant` the dominant interaction is between
  the HOMO of one partner and the LUMO of the other, whichever pair has the
  smaller gap (argued from the theorem); `prop:…:da-stereospecific` the
  dienophile's cis or trans relationship is kept (proof: concerted
  suprafacial approach); `prop:…:da-regio` the new bonds join the atoms with
  the largest coefficients (argued, figdata coefficients);
  `prop:…:endo` the endo adduct forms faster (secondary orbital overlap;
  `\admitted` as an empirical rule with its explanation).
- **Methods.** `met:…:fmo` (frontier-orbital analysis of a reaction);
  `met:…:diels-alder` (drawing a Diels–Alder product: s-cis diene, alignment,
  regiochemistry, endo).
- **Figures.** S two-orbital diagrams with two and with four electrons;
  S butadiene HOMO facing ethene LUMO, lobes scaled by Hückel coefficients;
  S Diels–Alder mechanism (chemfig, three curly arrows with `\chemmove`) and
  endo/exo approaches of cyclopentadiene and maleic anhydride; F `huckel`
  part c (coefficients of a donor-substituted diene and an acceptor-substituted
  dienophile, model parameters stated as a model); F `two-level` (reused,
  part b: exact versus perturbative stabilisation); P O. Diels and K. Alder
  (to find) in a `history` box (1928); `inthelab` box: cracking
  dicyclopentadiene by distillation (described, no figure needed).
- **Ledger.** `ghs:` cyclopentadiene / dicyclopentadiene, maleic anhydride
  (PubChem); `bp:` both (PubChem); `dfh:`/`s0:` of cyclopentadiene (g) and of
  its dimer if available (WEBBOOK-THERMO) for the problem.
- **Exercises palette.** HOMO and LUMO of ethene, allyl anion, butadiene (★);
  hard or soft (★); s-cis or s-trans dienes (★); draw a Diels–Alder adduct
  (★); stabilisation from $\beta$ and $\Delta\varepsilon$ (★★); cyanide on a
  carbocation versus on a haloalkane (★★); regiochemistry with
  1-methoxybutadiene and propenal (★★); endo adduct of cyclopentadiene and
  methyl propenoate (★★); why electron-poor dienophiles react faster
  (★★); stereospecificity with dimethyl fumarate and maleate (★★★); the
  retro-Diels–Alder: entropy at high temperature (★★★); four-electron
  repulsion and the rotation barrier of hydrazine (★★★).
- **Weekend problem — "Cracking cyclopentadiene".** I the dimerisation as a
  Diels–Alder reaction of the diene with itself; endo dimer; II
  thermodynamics: signs of $\Delta_r H^\circ$ and $\Delta_r S^\circ$, why
  heating cracks the dimer, the temperature where $\Delta_r G^\circ = 0$;
  III frontier orbitals: cyclopentadiene with itself versus with maleic
  anhydride (Hückel model gaps); IV the maleic anhydride adduct: endo,
  stereocentres. **Named number: the temperature above which the gas-phase
  retro-Diels–Alder of dicyclopentadiene is favoured, $\Delta_r G^\circ = 0$
  (computed from the ledger; if the dimer's data are missing, the named number
  becomes the number of stereocentres of the endo adduct, 4).** 25 questions.

## Ch. 18 — Transition Metals and Coordination Complexes — `coordination-complexes`

- **Hook.** In 1893 a young chemist explained why, of four cobalt chlorides
  with ammonia, one releases all three of its chloride ions to silver nitrate,
  another two, and two others only one — and why those two differ in colour.
- **Recall.** Year 1 volume: complex, central atom, ligand, polydentate
  ligand, chelate, formation constants; coordination number (general);
  configurations of transition-metal ions ($ns$ lost first); Lewis acid and
  base, dative bond; VSEPR; oxidation numbers; enantiomers.
- **Sections.** 1 The d block: transition elements, oxidation states, $d^n$
  counts. 2 Ligands and denticity: monodentate, bidentate (en, ox),
  hexadentate (edta); ambidentate and bridging ligands. 3 Coordination
  numbers and geometries: 2, 4 (tetrahedral, square planar), 5, 6
  (octahedral); why VSEPR fails. 4 Isomerism: cis/trans, fac/mer, Δ/Λ of
  tris-chelates, linkage and ionisation isomers. 5 Naming, and counting
  electrons: the 18-electron rule (carbonyls, ferrocene) and its limits.
- **Definitions.** `def:b2:coordination-complexes:transition-element`
  (transition element, $d^n$ configuration); `:denticity` (denticity,
  monodentate ligand, bidentate ligand, bridging ligand, ambidentate ligand);
  `:coordination-sphere` (coordination sphere); `:isomers` (fac isomer, mer
  isomer, linkage isomers, ionisation isomers); `:electron-count` (valence
  electron count, 18-electron rule); `:hapticity` (hapticity).
- **Ownership check.** Map owner (denticity, 18-electron rule); S1 left
  *coordination number* (general) to the Year 1 volume — applied here, not
  redefined; *polydentate ligand*, *chelate* recalled. *Hapticity* is wanted
  by Book 4 ch20 (organometallic ligands) too: earliest need here (ferrocene
  and alkene counts), contested low — report point 2. Book 4 owns ligand
  substitution mechanisms, inner/outer sphere electron transfer: the word
  "inner sphere" is not used.
- **Statements.** `prop:…:dn` $d^n$ of $\mathrm M^{m+}$: $n = g - m$, $g$ the
  group number (proof from configurations); `prop:…:isomer-count` two isomers
  for \ce{MA4B2} and for \ce{MA3B3} in an octahedron, a chiral \ce{M(AA)3}
  (proof by enumeration); `prop:…:eighteen` (the rule as an observation,
  explained in \cref{ch:b2:ligand-field}); `prop:…:square-planar` $d^8$ ions of
  the second and third rows are square planar (stated; explained in ch19).
- **Methods.** `met:…:naming` (naming a complex); `met:…:electron-count`
  (ionic counting of a complex's valence electrons).
- **Figures.** S geometries gallery (linear, tetrahedral, square planar,
  trigonal bipyramidal, octahedral; ball and stick, coordination-geometry
  pics of report point 4); S isomers: cis- and trans-\ce{[CoCl2(NH3)4]+},
  fac and mer \ce{[CoCl3(NH3)3]}, Δ and Λ \ce{[Co(en)3]^3+}; S chelating
  ligands (chemfig: en, ox, edta wrapped round a metal); S Werner's table
  (formula, ions per formula unit, chloride precipitated); P A. Werner (to
  find, PD) in a `history` box (1893); P solutions of transition-metal salts
  in a rack (to find; a photograph, not AI: colours are data).
- **Ledger.** Book 2 `gs:` configuration rows read-only; `ghs:` cobalt(II)
  chloride, cisplatin (PubChem).
- **Exercises palette.** $d^n$ of eight ions (★); denticity of five ligands
  (★); name four complexes (★); geometries from formulas (★); isomers of
  \ce{[PtCl2(NH3)2]} (★★); count electrons of \ce{Cr(CO)6}, \ce{Fe(CO)5},
  \ce{Ni(CO)4}, \ce{Mn2(CO)10} (★★); ferrocene (★★); edta and the chelate
  effect, recall of its constant (★★); linkage isomers of nitrite (★★);
  isomers of \ce{[Co(en)2Cl2]+} including enantiomers (★★★); the hexagon and
  the prism models refuted (★★★); an 18-electron count with a hydride and a
  phosphine (★★★).
- **Weekend problem — "Werner's cobalt ammines".** I four compounds
  \ce{CoCl3.nNH3}: silver chloride precipitated, ions per formula; II their
  formulas in square brackets; III the two isomers of
  \ce{[CoCl2(NH3)4]+}: octahedron versus hexagon versus prism; IV optical
  activity of \ce{[Co(en)3]^3+}. **Named number: two isomers of
  \ce{[CoCl2(NH3)4]+} — the octahedron predicts 2, the planar hexagon and the
  trigonal prism 3.** 25 questions.

## Ch. 19 — Ligand Field Theory and Colour — `ligand-field`

- **Hook.** Ruby is red and emerald green, and both owe their colour to the
  same ion, \ce{Cr^3+}, in two different crystals; copper sulfate is blue
  when hydrated and white when not.
- **Recall.** \cref{ch:b2:coordination-complexes} ($d^n$, geometries,
  18-electron rule), \cref{ch:b2:atomic-orbitals} (d-orbital shapes),
  \cref{ch:b2:fragment-orbitals}; Year 1 volume: absorbance, complementary
  colours, unpaired electrons, Hund's rule.
- **Sections.** 1 The crystal-field model: octahedral splitting, $t_{2g}$ and
  $e_g$, $\Delta_o$, the barycentre. 2 High spin and low spin: pairing energy;
  $d^4$–$d^7$; crystal-field stabilisation energy; unpaired electrons.
  3 Other geometries: tetrahedral, square planar ($d^8$). 4 Colour and the
  spectrochemical series: d–d absorption, $\Delta_o$ from the wavelength, the
  colour seen; effects of ligand, charge and row. 5 The ligand field: the
  σ-only MO diagram of an octahedral complex from fragments; π-donor and
  π-acceptor ligands and back-donation; the 18-electron rule explained.
- **Definitions.** `def:b2:ligand-field:crystal-field` (crystal-field model,
  crystal-field splitting); `:spin` (high spin, low spin, pairing energy);
  `:cfse` (crystal-field stabilisation energy); `:d-d` (d–d transition);
  `:spectrochemical` (spectrochemical series); `:ligand-field` (ligand field
  theory); `:pi-ligands` (π-donor ligand, π-acceptor ligand,
  back-donation).
- **Ownership check.** Map owner (ligand field, spectrochemical series,
  high/low spin). Book 4 owns term splitting, Tanabe–Sugano, Jahn–Teller,
  magnetic susceptibility, spin-only moments (pointers; only the count of
  unpaired electrons here). *Back-donation*: Book 4 ch20 lists
  "back-bonding" — contested, earliest need here (π acceptors explain the
  top of the spectrochemical series); proposal: this book defines
  *back-donation*, *π-acceptor*, *π-donor*; Book 4 recalls and develops
  (report point 2).
- **Statements.** `thm:…:barycentre` $e_g$ at $+0.6\Delta_o$, $t_{2g}$ at
  $-0.4\Delta_o$ (proof from the barycentre condition, itself `\admitted`);
  `prop:…:spin-state` low spin iff $\Delta_o > P$ for $d^4$–$d^7$ (proof:
  compare the two energies); `prop:…:cfse` CFSE table (computed);
  `prop:…:tetrahedral` $\Delta_t = \frac49\Delta_o$ (`\admitted`) and
  tetrahedral complexes high spin (argued); `prop:…:colour` $\Delta_o =
  N_Ahc/\lambda_{\max}$ (proof); `prop:…:mo-octahedral` six bonding MOs from
  the ligands, $t_{2g}$ nonbonding, $e_g^*$ antibonding; up to 18 electrons
  fill bonding and nonbonding levels (argued; the orbital names from group
  theory admitted, Year 3); `prop:…:pi-effects` π donors shrink $\Delta_o$, π
  acceptors widen it (proof: two-level interactions of $t_{2g}$ with filled
  or empty ligand π orbitals).
- **Methods.** `met:…:spin-state` ($d^n$, $\Delta_o$ versus $P$ →
  configuration, CFSE, unpaired electrons); `met:…:colour` (absorbed
  wavelength → $\Delta_o$ → colour seen).
- **Figures.** S d orbitals among six point ligands (lobes pointing at or
  between the ligands); S splitting diagrams octahedral, tetrahedral, square
  planar (shared level pics); S high-spin and low-spin $d^6$ with `\omorbs`;
  S colour wheel; S σ-only MO diagram of \ce{ML6} (modiagram or level pics);
  S π interactions of $t_{2g}$ with a π-donor and a π-acceptor; F
  `ligand-field` part a (CFSE versus $d^n$, high and low spin), part b
  (absorption band of a $d^1$ ion, synthetic Gaussian at the ledger maximum —
  only if sourced); P ruby (`File:Ruby cristal.jpg`, PD, found), emerald (to
  find), copper sulfate pentahydrate (`File:Copper sulfate.jpg`, CC BY-SA 3.0,
  found).
- **Ledger.** `lf:` absorption maxima of \ce{[Ti(H2O)6]^3+},
  \ce{[Cr(H2O)6]^3+}, \ce{[Cu(H2O)6]^2+}, ruby and emerald bands (source to
  secure — at risk; else exercise data marked as such and the hook stays
  qualitative); pairing energies are exercise data.
- **Exercises palette.** CFSE of $d^3$ and $d^8$ (★); unpaired electrons of
  \ce{[Fe(H2O)6]^2+} and \ce{[Fe(CN)6]^4-} (★); colour from a wavelength
  (★); order ligands by the series (★); high or low spin from $\Delta_o$ and
  $P$ (★★); tetrahedral \ce{[CoCl4]^2-} blue versus octahedral
  \ce{[Co(H2O)6]^2+} pink (★★); square planar \ce{[Ni(CN)4]^2-} diamagnetic
  (★★); $\Delta_o$ in kJ/mol from an absorption at 500 nm (★★); why
  \ce{Zn^2+} complexes are colourless (★★); the MO count of \ce{[Co(NH3)6]^3+}
  (★★★); CO at the top of the series (★★★); hydration enthalpies and the
  CFSE (two humps, as a reasoning exercise with given data) (★★★).
- **Weekend problem — "Red ruby, green emerald".** I \ce{Cr^3+} ($d^3$) in an
  octahedron: configuration, CFSE, unpaired electrons; II the two absorption
  bands of ruby and the colour transmitted; III emerald: a weaker field, the
  colour shift; IV hydrated and anhydrous copper sulfate. **Named number:
  $\Delta_o$ of \ce{Cr^3+} in ruby from its first absorption band, in
  cm⁻¹ and kJ/mol (≈ 2 × 10⁴ cm⁻¹; ledger or stated data).** 25 questions.

## Ch. 20 — Organometallic Catalysis: Elementary Steps and Cycles — `catalytic-cycles`

- **Hook.** A few milligrams of a palladium salt join two aromatic rings in
  a flask of kilograms; the same metal atom turns over thousands of times. A
  catalytic cycle is a story told in four steps, and each step obeys the
  electron count of the previous chapters.
- **Recall.** \cref{ch:b2:coordination-complexes} (electron count, 18-electron
  rule, hapticity), \cref{ch:b2:ligand-field} (back-donation); Year 1
  volume: catalyst, homogeneous catalysis, elementary step, rate-determining
  step, organometallic compound, oxidation number; school volume:
  catalysis.
- **Sections.** 1 The language: oxidation state, $d^n$ and electron count of
  organometallic complexes; 16-electron complexes and vacant sites.
  2 Ligand exchange; oxidative addition and reductive elimination. 3 Migratory
  insertion and β-hydride elimination; transmetalation. 4 Reading a cycle:
  hydrogenation (Wilkinson's catalyst), hydroformylation, cross-coupling
  (Suzuki, Heck); precatalyst, turnover number and frequency. 5 What a cycle
  teaches: the slow step, selectivity (linear versus branched), the role of
  the ligands.
- **Definitions.** `def:b2:catalytic-cycles:unsaturated` (coordinatively
  unsaturated complex, vacant site); `:ligand-exchange` (ligand exchange);
  `:oxidative-addition` (oxidative addition, reductive elimination);
  `:insertion` (migratory insertion, β-hydride elimination);
  `:transmetalation` (transmetalation); `:cycle` (catalytic cycle,
  precatalyst, turnover number, turnover frequency).
- **Ownership check.** Map owner (oxidative addition, reductive elimination,
  migratory insertion); the map's re-found of g12 *catalysis* was taken by
  the Year 1 volume (*catalyst*, *homogeneous catalysis*): recalled.
  Book 4 ch19 owns substitution mechanisms (dissociative, associative):
  *ligand exchange* is defined as a step, its mechanisms left to the Year 3
  volume — contested low. Book 4 ch21 treats the same industrial processes;
  this chapter reads them only as sequences of steps (report point 9).
- **Statements.** `prop:…:oa` oxidative addition raises the oxidation state
  by 2, the electron count by 2 and the coordination number by 2;
  reductive elimination the reverse (proof by counting); `prop:…:insertion`
  migratory insertion keeps the oxidation state and lowers the count by 2
  (proof); `prop:…:beta-h` β-hydride elimination needs a β hydrogen and a cis
  vacant site (argued); `prop:…:cycle-sum` the overall equation is the sum of
  the steps and the catalyst cancels (proof); `prop:…:tof` TON and TOF
  (definitions applied).
- **Methods.** `met:…:read-cycle` (check every step: type, count, oxidation
  state; sum the steps); `met:…:count-organometallic` (counting with
  hydrides, alkyls, alkenes, CO, phosphines).
- **Figures.** S Wilkinson hydrogenation cycle (the cycle layout of report
  point 4); S hydroformylation cycle (Rh, linear/branched branch); S Suzuki
  and Heck cycles side by side; S gallery of the four elementary steps; AI a
  process-chemistry pilot plant with a glass-lined reactor (hook); P A.
  Suzuki, R. Heck or E. Negishi (to find; CC portraits) in a `history` box
  (Nobel 2010 — said as "awarded in 2010").
- **Ledger.** `ghs:` palladium(II) ethanoate, triphenylphosphine, phenylboronic
  acid (PubChem); no catalytic performance figure printed as fact.
- **Exercises palette.** Oxidation state and count of Vaska's complex before
  and after \ce{H2} adds (★); name the step from before/after structures
  (★); TON from amounts (★); sum a three-step cycle (★); β-H elimination: which
  alkyls can and cannot (★★); a Heck product's geometry (★★); hydroformylation
  of propene: linear and branched aldehydes (★★); why a 16-electron complex
  adds \ce{H2} (★★); the role of the base in a Suzuki coupling (★★); a cycle
  with a wrong step to find (★★★); TOF from a kinetic curve (★★★); designing
  a cross-coupling for a given biaryl (★★★).
- **Weekend problem — "Reading the Suzuki cycle".** I the precatalyst and
  the active Pd(0) complex: counts and oxidation states; II oxidative addition
  of 4-bromotoluene, transmetalation with phenylboronic acid (role of the
  base), reductive elimination; III stoichiometry, yield and turnover number
  at 0.5 mol % palladium; IV side reactions (homocoupling; why β-H elimination
  is absent). **Named number: the turnover number of palladium in the run
  (exercise data, ≈ 1.8 × 10²).** 24 questions.

## Ch. 21 — Oxidation and Reduction of Alkenes — `alkene-redox`

- **Hook.** Two tubes of epoxy glue: an epoxide in one, an amine in the
  other; mixed, the strained three-membered rings open and the paste sets.
  Alkenes are the raw material of such rings, of alcohols placed where
  Markovnikov's rule would not put them, and of the fragments that told
  chemists where a double bond lies.
- **Recall.** Year 1 volume: electrophilic additions, Markovnikov's rule,
  halonium ions, syn and anti addition, hydration, oxidation levels, hydride
  donors, chemoselectivity, meso compounds and racemic mixtures;
  \cref{ch:b2:catalytic-cycles} (hydrogenation cycle).
- **Sections.** 1 Catalytic hydrogenation (heterogeneous metals, Wilkinson's
  catalyst; syn delivery; alkynes to Z-alkenes over a poisoned catalyst).
  2 Hydroboration–oxidation (borane as electrophile; four-centre addition;
  anti-Markovnikov orientation, syn; oxidation with retention). 3 Epoxidation
  and epoxide opening (peroxy acids; stereospecific; opening in base and in
  acid: where and how). 4 Dihydroxylation (osmium tetroxide, cold
  permanganate: syn diols; the epoxide route: anti diols). 5 Oxidative
  cleavage (ozonolysis and its two work-ups, hot permanganate, periodate on
  diols); locating a double bond.
- **Definitions.** `def:b2:alkene-redox:hydrogenation` (catalytic
  hydrogenation); `:hydroboration` (hydroboration, anti-Markovnikov
  orientation); `:epoxide` (epoxide, epoxidation, peroxy acid);
  `:dihydroxylation` (dihydroxylation); `:cleavage` (oxidative cleavage,
  ozonolysis).
- **Ownership check.** Map owner (hydroboration, epoxidation, oxidative
  cleavage). Book 2 owns *syn addition*, *anti addition*, *Markovnikov's
  rule*, *hydration*, *oxidation level*, *hydride donor*,
  *stereospecific reaction*: recalled. Book 4 owns asymmetric hydrogenation
  and epoxidation (pointer) and *adsorption* (the surface step of a
  heterogeneous hydrogenation is described in plain words).
- **Statements.** `prop:…:syn-hydrogenation` (both H on one face; proof from
  the mechanism, Z-alkenes from alkynes); `prop:…:hydroboration-regio` boron
  to the less substituted carbon (argued: sterics and the partial charges of
  the four-centre transition state); `prop:…:retention` C–B → C–OH with
  retention (mechanism); `prop:…:epoxidation` stereospecific, cis alkene →
  cis epoxide (proof: concerted transfer); `prop:…:opening` base: SN2 at the
  less hindered carbon; acid: at the more substituted carbon; both anti
  (argued); `prop:…:diols` syn by \ce{OsO4}, anti by epoxide + water (proof
  with (E)- and (Z)-but-2-ene: meso or racemic); `prop:…:ozonolysis` each
  C=C gives two C=O; work-up decides aldehyde or acid (mechanism admitted
  in its middle steps).
- **Methods.** `met:…:choose-reagent` (table: target function and
  stereochemistry → reagent); `met:…:locate-double-bond` (rebuild an alkene
  from its ozonolysis fragments).
- **Figures.** S hydroboration (four-centre transition state, then
  oxidation) in chemfig; S epoxidation by a peroxy acid with `\chemmove`;
  S epoxide opening in acid and in base; S ozonolysis scheme; S stereo: the
  two diols of (Z)-but-2-ene; AI mixing two-part epoxy glue on a workbench
  (hook); P H. C. Brown (to find) only if free.
- **Ledger.** `ghs:` osmium tetroxide, 3-chloroperbenzoic acid, borane–THF,
  sodium periodate, ozone (PubChem); Book 2 `ghs:KMnO4` read-only.
- **Exercises palette.** Products of 1-methylcyclohexene with six reagents
  (★); hydroboration orientation (★); epoxide from (E)-but-2-ene (★);
  ozonolysis fragments of hex-3-ene (★); diols of (Z)-but-2-ene by two routes
  (★★); acid versus base opening of 2,2-dimethyloxirane (★★); an alkyne to a
  Z-alkene (★★); reconstruct an alkene from its fragments (★★); a two-step
  synthesis of a primary alcohol from a terminal alkene (★★); limonene's two
  double bonds: which reacts first (★★★); trans-cyclohexane-1,2-diol by the
  right route (★★★); a cleavage that reveals a ring (★★★).
- **Weekend problem — "Identifying a terpene".** I limonene's formula,
  degree of unsaturation (Year 1), hydrogen uptake; II ozonolysis fragments
  and the structure; III selective hydroboration–oxidation of the less
  substituted double bond; IV selective epoxidation of the more substituted
  one and the diol. **Named number: the volume of dihydrogen (25 °C, 1 bar)
  absorbed by 1.00 g of limonene, ≈ 364 mL.** 25 questions.

## Ch. 22 — Aromaticity and Electrophilic Aromatic Substitution — `aromatic-substitution`

- **Hook.** Bromine water loses its colour in seconds with an alkene and not
  at all with benzene; yet benzene reacts with bromine when iron(III) bromide
  is added, and comes out with its ring intact. Aromatic rings substitute
  rather than add.
- **Recall.** \cref{ch:b2:huckel} (aromatic, delocalisation energy); Year 1
  volume: electrophilic additions, inductive and mesomeric effects, donor and
  acceptor groups, carbocations, Hammond postulate, Lewis acids, energy
  profiles.
- **Sections.** 1 Substitution, not addition (the cost of losing the
  aromatic ring). 2 The mechanism: Wheland intermediate, loss of a proton,
  energy profile. 3 The reactions: halogenation, nitration, sulfonation
  (reversible), Friedel–Crafts alkylation (rearrangements, polyalkylation)
  and acylation. 4 Substituent effects: activating and deactivating groups;
  ortho/para and meta directors; the halogens. 5 Polysubstituted benzenes:
  combined effects, order of steps, blocking and converting groups.
- **Definitions.** `def:b2:aromatic-substitution:arene` (arene);
  `:seAr` (electrophilic aromatic substitution, Wheland intermediate);
  `:friedel-crafts` (Friedel–Crafts alkylation, Friedel–Crafts acylation,
  acylium ion); `:directing` (activating group, deactivating group,
  ortho/para director, meta director).
- **Ownership check.** Not in the map apart from aromaticity (ch16). Book 2
  owns *donor group*, *acceptor group*, *carbocation rearrangement*,
  *electrophilic addition*: recalled. Book 4: kinetic isotope effects (not
  used as evidence here).
- **Statements.** `prop:…:no-addition` addition would cost the aromatic
  stabilisation (argued with ch16's numbers); `prop:…:mechanism` two steps,
  the first rate-determining (argued; energy profile); `prop:…:directing`
  mesomeric donors direct ortho/para, acceptors meta (proof: Wheland
  resonance structures + Hammond); `prop:…:halogens` halogens deactivate yet
  direct ortho/para (argued: −I against +M); `prop:…:friedel-crafts-limits`
  rearrangements and polyalkylation; acylation stops at one and needs a full
  equivalent of \ce{AlCl3} (argued).
- **Methods.** `met:…:predict-position` (position of substitution, several
  substituents); `met:…:plan-aromatic` (order of introduction of groups).
- **Figures.** S nitration mechanism (nitronium formation and attack, chemfig
  with `\chemmove`); S the three Wheland intermediates of methoxybenzene and
  of nitrobenzene (resonance structures); F `aromatic-profile` (model energy
  profile of a two-step substitution versus an addition, schematic function
  in figdata, as Book 2's profiles); S Friedel–Crafts acylation via the
  acylium ion; AI indigo-dyed fabric in a dye vat (hook — or a modern dye
  works); P C. Friedel (`File:Charles Friedel.jpg`, PD, found) and J. M.
  Crafts (to find) in a `history` box (1877).
- **Ledger.** `ghs:` benzene, bromine, aluminium chloride, nitric acid
  (PubChem; Book 2 `ghs:H2SO4` read-only); nitration isomer distribution of
  toluene only if sourced (else exercise data, said so).
- **Exercises palette.** Nitronium formation (★); product of bromination of
  toluene and of nitrobenzene (★); activating or deactivating (★);
  Friedel–Crafts acylation product (★); why 1-chloropropane gives
  isopropylbenzene (★★); phenol with bromine water (★★); order of steps for
  3-bromonitrobenzene and 4-bromonitrobenzene (★★); acetanilide versus
  aniline in nitration (★★); sulfonation as a blocking group (★★); combined
  effects in 4-methylanisole (★★★); TNT: why the third nitration is hard
  (★★★); a three-step synthesis of 4-nitrobenzoic acid (★★★).
- **Weekend problem — "Nitrating toluene".** I the nitronium ion and the
  mechanism; II ortho, meta, para: resonance arguments and the statistical
  2 : 2 : 1 against the observed ratio (exercise data); III separation of the
  isomers by their melting points; IV mass balance. **Named number: the mass
  of 4-nitrotoluene obtained from 100 g of toluene (exercise data for the
  isomer ratio and conversion).** 25 questions.

## Ch. 23 — Amines and Nitrogen Compounds — `amines`

- **Hook.** Fish smells of trimethylamine; a squeeze of lemon takes the smell
  away, because the amine, now protonated, can no longer evaporate.
- **Recall.** Year 1 volume: Brønsted bases, $\mathrm pK_a$, predominance
  diagrams, nucleophiles, SN2, hemiacetals and acetals, hydride donors,
  Grignard reagents, carbon class; \cref{ch:b2:aromatic-substitution}
  (nitration, reduction of nitro groups); school volume: amines, amides.
- **Sections.** 1 Structure and basicity (classes; $\mathrm pK_a$ of
  ammonium ions; alkyl and aryl effects; amides are not bases; inversion at
  nitrogen). 2 Amines as nucleophiles: alkylation and its excess,
  quaternary ammonium salts, Hofmann elimination; the Gabriel route.
  3 Imines and enamines: nucleophilic addition to the carbonyl, the
  hemiaminal, dehydration; the pH optimum; reductive amination. 4 Diazonium
  salts: diazotisation of aryl amines; Sandmeyer reactions; replacement by
  OH and H; azo coupling and dyes. 5 Nitriles: from cyanide or from a
  diazonium salt; hydrolysis, reduction, Grignard addition.
- **Definitions.** `def:b2:amines:class` (primary amine, secondary amine,
  tertiary amine, quaternary ammonium ion); `:nucleophilic-addition`
  (nucleophilic addition); `:imine` (hemiaminal, imine, enamine);
  `:reductive-amination` (reductive amination); `:diazonium` (diazonium ion,
  diazotisation, Sandmeyer reaction, azo coupling); `:nitrile` (nitrile).
- **Ownership check.** Book 2's list sends imines and enamines here. Book 1
  owns *amine*, *amide* (recalled); Book 2 owns *nucleophile*, *hemiacetal*,
  *acetal*, *carbon class*. *Nucleophilic addition* was used but not defined
  by the Year 1 volume (Grignard, acetals): earliest definition here, low
  risk (report point 2). Book 4 owns heterocycles (pyridine basicity
  recalled from Book 2's `pka:pyridinium` only).
- **Statements.** `prop:…:basicity` alkylamines stronger bases than ammonia,
  aryl amines much weaker, amides not basic (argued: inductive effect,
  solvation, mesomeric delocalisation); `prop:…:polyalkylation` the product
  amine is as nucleophilic as the reagent (argued); `prop:…:imine-ph` imine
  formation is fastest near pH 4–5 (argued from the two steps' needs);
  `prop:…:reductive-amination` the iminium ion is reduced faster than the
  carbonyl (argued); `prop:…:diazonium` aryl diazonium ions are kept at
  0–5 °C, alkyl ones lose \ce{N2} at once (argued); `prop:…:nitrile`
  hydrolysis to the acid via the amide (mechanism completed in ch24).
- **Methods.** `met:…:make-amine` (Gabriel, reductive amination, reduction
  of nitro groups, nitriles and amides); `met:…:diazonium-routes`
  (substitution patterns reached through a diazonium salt).
- **Figures.** S basicity scale ($\mathrm pK_a$ of conjugate acids, ledger
  values); S imine formation mechanism with `\chemmove`; S diazotisation and
  azo coupling to methyl orange (chemfig); S map of a diazonium salt's
  reactions (to ArCl, ArBr, ArCN, ArOH, ArH, Ar–N=N–Ar'); AI a fish stall
  with lemons (hook).
- **Ledger.** `pka:` ammonium, dimethylammonium, trimethylammonium,
  ethanamide (IUPAC-PKA); Book 2 `pka:methylammonium`, `pka:anilinium`,
  `pka:pyridinium` read-only; `ghs:` sodium nitrite, aniline, sodium
  cyanoborohydride, sulfanilic acid (PubChem).
- **Exercises palette.** Classes (★); rank bases (★); imine from
  cyclohexanone and methylamine (★); products of a Sandmeyer series (★);
  which form dominates at pH 7, and extraction by acid (★★); enamine from
  pyrrolidine (★★); reductive amination to benzylamine derivatives (★★);
  nitrile to ketone with a Grignard reagent (★★); Gabriel synthesis of a
  primary amine (★★); 1,3,5-tribromobenzene from aniline (★★★); azo dye
  design (★★★); Hofmann elimination regiochemistry (★★★).
- **Weekend problem — "Making methyl orange".** I sulfanilic acid as a
  zwitterion and its diazotisation (stoichiometry, temperature); II azo
  coupling with N,N-dimethylaniline: position and pH; III methyl orange as an
  indicator: its two forms (recall of the Year 1 volume); IV yield. **Named
  number: the mass of methyl orange obtained from 5.00 g of sulfanilic acid
  at 80 % yield, ≈ 7.56 g.** 25 questions.

## Ch. 24 — Carboxylic Acid Derivatives — `acyl-substitution`

- **Hook.** Olive oil boiled with sodium hydroxide gives soap and glycerol —
  the oldest organic reaction run on purpose. An ester is cut at one bond,
  and always the same one.
- **Recall.** Year 1 volume: electrophilic activation of a carbonyl,
  hemiacetal and acetal mechanisms, Grignard additions, hydride donors and
  their scope, leaving groups, $\mathrm pK_a$, Q/K; \cref{ch:b2:amines}
  (nucleophilic addition, amines); \cref{ch:b2:equilibrium-shifts} (shifting
  an equilibrium); school volume: esters, carboxylic acids, amides.
- **Sections.** 1 The family and its reactivity scale (acyl chlorides,
  anhydrides, esters, acids, amides; leaving group and resonance donation).
  2 Nucleophilic acyl substitution: addition–elimination through a
  tetrahedral intermediate; base and acid catalysis. 3 Esters: Fischer
  esterification (equilibrium, driving it), saponification (irreversible),
  transesterification, lactones. 4 Activated derivatives: acyl chlorides
  from \ce{SOCl2}, anhydrides; amides and esters from them, with a base to
  trap \ce{HCl}. 5 Organometallics and hydrides on derivatives: two
  Grignard additions to an ester; reductions with \ce{LiAlH4}; stopping at
  the aldehyde at low temperature; amides to amines.
- **Definitions.** `def:b2:acyl-substitution:derivative` (carboxylic acid
  derivative, acyl group, acyl chloride, acid anhydride); `:nas`
  (nucleophilic acyl substitution, tetrahedral intermediate);
  `:esterification` (esterification); `:saponification` (saponification);
  `:transesterification` (transesterification); `:lactone` (lactone,
  lactam).
- **Ownership check.** Not in the map. Book 1 owns *ester*, *carboxylic
  acid*, *amide* (recalled); Book 2 owns *electrophilic activation*,
  *leaving group*, *hydride donor*, *Grignard reagent* (recalled). Book 4:
  none.
- **Statements.** `prop:…:reactivity` acyl chloride > anhydride > ester ≈
  acid > amide (argued: leaving-group basicity, +M donation);
  `prop:…:addition-elimination` the mechanism (argued; isotopic evidence in a
  remark); `prop:…:fischer` equilibrium constant near 4 for primary alcohols
  and how to drive it (recall Year 1 and ch4); `prop:…:saponification` the
  final proton transfer makes it complete (proof: combination of constants
  from $\mathrm pK_a$ values); `prop:…:grignard-ester` two additions,
  tertiary alcohol (argued: the ketone is more reactive than the ester);
  `prop:…:hydrides` \ce{LiAlH4} reduces esters, acids and amides,
  \ce{NaBH4} does not; a bulky aluminium hydride at −78 °C stops at the
  aldehyde (argued).
- **Methods.** `met:…:ladder` (converting one derivative into another: down
  the scale is easy, up needs activation); `met:…:nas-mechanism` (drawing
  the mechanism in acid or base).
- **Figures.** S reactivity ladder with the possible conversions; S
  addition–elimination mechanism (base) with `\chemmove`; S Fischer
  esterification (acid, six steps); S saponification of a triglyceride to
  glycerol and soap; S reflux with a Dean–Stark trap (shared pics); AI bars
  of olive-oil soap drying on racks (hook); P M. E. Chevreul (to find, PD) in
  a `history` box (fats and soaps, 1823).
- **Ledger.** Book 2 `pka:ethanoic`, `pka:ethanol` read-only; `ester:berthelot`
  (Book 1/2 row) read-only for the constant; `ghs:` thionyl chloride, ethanoyl
  chloride, lithium aluminium hydride, sodium hydroxide (Book 2 read-only).
- **Exercises palette.** Rank five derivatives (★); products of five
  substitutions (★); equation and masses of a saponification (★); name
  lactones (★); mechanism of an aminolysis (★★); aspirin from salicylic acid
  and ethanoic anhydride (★★); Grignard on ethyl ethanoate (★★); \ce{LiAlH4}
  on a lactone (★★); driving an esterification: excess and water removal
  (★★); amide from an acid via the chloride, with the base (★★★); saponification
  value of a fat (★★★); a nitrile, an ester and an amide in one molecule:
  chemoselective reductions (★★★).
- **Weekend problem — "Biodiesel from frying oil".** I triolein: structure
  and molar mass; II transesterification with methanol: base catalysis,
  mechanism, excess methanol; III free fatty acids and water: saponification
  as a side reaction, why the base is consumed; IV yields per tonne. **Named
  number: the mass of glycerol co-produced per tonne of triolein,
  ≈ 104 kg.** 25 questions.

## Ch. 25 — Enols, Enolates and the Aldol Reaction — `enolates-aldol`

- **Hook.** Every time a cell breaks down glucose, an enzyme cuts a
  six-carbon sugar into two three-carbon pieces: an aldol reaction run
  backwards. Run forwards, the same reaction is the chemist's most used way
  of making carbon–carbon bonds.
- **Recall.** Year 1 volume: $\mathrm pK_a$ and the predominant reaction,
  carbanions, kinetic and thermodynamic control, nucleophilic addition to
  carbonyls, E1 and E2, the hydration of alkynes (an enol rearranging, "a
  process studied in the Year 2 volume"); \cref{ch:b2:frontier-orbitals}
  (ambident nucleophiles), \cref{ch:b2:acyl-substitution} (esters).
- **Sections.** 1 Keto–enol tautomerism (acid and base catalysis; small
  enol content of simple ketones; large for 1,3-dicarbonyl compounds;
  racemisation at the α carbon). 2 Enolates (acidity of α hydrogens; bases:
  alkoxides and lithium diisopropylamide; kinetic and thermodynamic
  enolates; C- versus O-attack). 3 Alkylating enolates (SN2 on primary
  halides; malonic and acetoacetic syntheses with decarboxylation;
  α-halogenation and the haloform reaction). 4 The aldol reaction (addition,
  then dehydration to the enone; crossed aldols and how to control them;
  intramolecular aldols). 5 The Claisen condensation (β-keto esters; the final
  deprotonation that drives it; the intramolecular Dieckmann version).
- **Definitions.** `def:b2:enolates-aldol:tautomerism` (tautomers,
  keto–enol tautomerism, enol); `:enolate` (α carbon, α hydrogen, enolate
  ion); `:kinetic-enolate` (kinetic enolate, thermodynamic enolate);
  `:aldol` (aldol addition, aldol, aldol condensation); `:decarboxylation`
  (decarboxylation, malonic ester synthesis); `:claisen` (Claisen
  condensation, β-keto ester); `:haloform` (haloform reaction).
- **Ownership check.** Book 2's list sends *enol* and *keto–enol tautomerism*
  here. Book 2 owns *carbanion*, *kinetic control*, *thermodynamic control*,
  *dehydration* (recalled). Book 4 owns enzyme kinetics (the hook's enzyme
  is named without kinetics).
- **Statements.** `prop:…:enol-content` (small $K$ for propanone, large for
  pentane-2,4-dione; argued: conjugation and the internal hydrogen bond;
  values as sourced); `prop:…:alpha-acidity` (resonance of the enolate;
  $\mathrm pK_a$ ranges); `prop:…:enolate-control` (LDA at −78 °C gives the
  less substituted enolate, an alkoxide at room temperature the more
  substituted one; argued with Year 1 control); `prop:…:aldol-equilibrium`
  addition reversible, dehydration drives it (argued with $Q$/$K^\circ$);
  `prop:…:claisen-drive` the β-keto ester ($\mathrm pK_a \approx 11$) is
  deprotonated by the alkoxide, which pulls an unfavourable equilibrium
  (proof: product of constants); `prop:…:decarboxylation` β-keto acids and
  malonic acids lose \ce{CO2} on warming through a cyclic transition state
  (argued).
- **Methods.** `met:…:aldol-recognition` (spotting an aldol or enone and
  its two partners — leads to ch28); `met:…:crossed-aldol` (controlling which
  partner gives the enolate).
- **Figures.** S keto–enol interconversion in acid and in base; S enolate
  resonance and its two nucleophilic sites; S aldol addition and
  dehydration with `\chemmove`; S Claisen mechanism; S scale of α-H
  $\mathrm pK_a$ (ledger values, TikZ); AI a perfumer's workbench with small
  bottles (hook alternative, everyday) — or no AI; P L. Claisen
  (`File:Ludwig Claisen.jpg`, CC BY-SA 4.0, found) and A. Borodin (to find,
  PD) in a `history` box (aldol, 1872).
- **Ledger.** `pka:` pentane-2,4-dione, diethyl propanedioate, ethyl
  3-oxobutanoate, propanone (IUPAC-PKA where present; at risk for
  propanone); enol content of propanone and of pentane-2,4-dione (source to
  secure; else qualitative); `ghs:` LDA solution, sodium ethoxide, benzaldehyde
  (PubChem); `rho:` benzaldehyde (PubChem) and Book 2 `rho:acetone` read-only.
- **Exercises palette.** Draw tautomers (★); rank α-H acidities (★); aldol
  of ethanal (★); malonic synthesis of hexanoic acid (★); kinetic and
  thermodynamic enolates of 2-methylcyclohexanone (★★); crossed aldol of
  benzaldehyde and propanone (★★); intramolecular aldol of hexane-2,5-dione:
  which ring (★★); Claisen of ethyl ethanoate (★★); haloform test (★★);
  Dieckmann cyclisation (★★★); why a ketone racemises in base (★★★); a
  two-aldol route to a dienone (★★★).
- **Weekend problem — "Dibenzalacetone".** I the enolate of propanone, and
  why benzaldehyde cannot condense with itself; II the two aldol
  condensations, mechanism; III the (E,E) product and its conjugation (UV,
  recall of the Year 1 volume); IV stoichiometry, limiting reactant, yield.
  **Named number: the mass of dibenzalacetone from the stated volumes at
  75 % yield (computed from ledger densities).** 25 questions.

## Ch. 26 — Conjugated Carbonyls: Michael and Robinson — `conjugate-additions`

- **Hook.** The four rings of a steroid hormone were first put together one
  ring at a time, and the reaction that adds a whole six-membered ring with
  its ketone in one sequence bears the name of the chemist who devised it.
- **Recall.** \cref{ch:b2:enolates-aldol} (enolates, aldol condensation),
  \cref{ch:b2:frontier-orbitals} (charge and orbital control, hard and
  soft), \cref{ch:b2:huckel}; Year 1 volume: Grignard reagents, hydrides,
  kinetic and thermodynamic control, conjugated systems.
- **Sections.** 1 α,β-Unsaturated carbonyl compounds: two electrophilic
  sites (resonance; the LUMO's coefficients). 2 1,2- versus 1,4-addition:
  hard nucleophiles (organolithiums, Grignard reagents, \ce{LiAlH4}) and soft
  ones (cuprates, stabilised enolates, thiols, amines); kinetic and
  thermodynamic control. 3 Michael additions (donors, acceptors, catalytic
  base, mechanism). 4 Organocuprates (preparation, conjugate addition,
  substitution of halides). 5 The Robinson annulation (Michael addition +
  intramolecular aldol + dehydration; the Wieland–Miescher ketone).
- **Definitions.** `def:b2:conjugate-additions:enone` (α,β-unsaturated
  carbonyl compound); `:addition-modes` (1,2-addition, conjugate
  addition); `:michael` (Michael addition, Michael donor, Michael acceptor);
  `:cuprate` (organocuprate); `:robinson` (annulation, Robinson annulation).
- **Ownership check.** Not in the map. Book 2 owns *organometallic
  compound*, *Grignard reagent*, *conjugated system* (recalled). Book 4 ch28
  owns organocatalysis and asymmetric versions (pointer for the proline
  route to the Wieland–Miescher ketone).
- **Statements.** `prop:…:two-sites` the β carbon carries the larger LUMO
  coefficient and a partial positive charge (argued; figdata Hückel model of
  propenal); `prop:…:regio` hard nucleophiles add 1,2 (charge control,
  usually kinetic), soft ones 1,4 (orbital control, keeping C=O, the
  thermodynamic product) (argued); `prop:…:michael` mechanism and catalytic
  base (argued); `prop:…:robinson` the three steps and the cyclohexenone
  formed (proof by drawing the sequence).
- **Methods.** `met:…:predict-mode` (1,2 or 1,4); `met:…:robinson-disconnection`
  (cyclohexenone → Michael donor + methyl vinyl ketone).
- **Figures.** S resonance structures of propenal and LUMO lobes (Hückel
  model); S 1,2 and 1,4 additions of MeLi and of \ce{Me2CuLi} to
  cyclohexenone; S Michael mechanism; S Robinson annulation to the
  Wieland–Miescher ketone (chemfig); F `huckel` part d (propenal model:
  LUMO coefficients); P R. Robinson (to find) in a `history` box (1935).
- **Ledger.** `ghs:` but-3-en-2-one (methyl vinyl ketone: very toxic,
  `safety` box), copper(I) iodide, methyllithium (PubChem).
- **Exercises palette.** 1,2 or 1,4 for four reagents (★); Michael donor or
  acceptor (★); cuprate preparation equation (★); product of diethyl
  propanedioate and but-3-en-2-one (★); 3-methylcyclohexanone by a cuprate
  (★★); thiols as Michael donors (★★); kinetic versus thermodynamic additions
  of cyanide (★★); Robinson product from 2-methylcyclohexane-1,3-dione (★★);
  retrosynthesis of a 1,5-dicarbonyl (★★); why the Michael adduct does not
  revert (★★★); a double Michael addition (★★★); Robinson annulation of
  cyclohexanone: which enolate (★★★).
- **Weekend problem — "The Wieland–Miescher ketone".** I the donor
  (2-methylcyclohexane-1,3-dione): acidity, enolate; II the Michael adduct, a
  triketone; III the intramolecular aldol: which enolate, which ring, the
  dehydration; IV the stereocentre (racemic here; asymmetric versions in the
  Year 3 volume) and the mass balance. **Named number: the mass of
  Wieland–Miescher ketone from 10.0 g of dione at 70 % overall yield
  (computed).** 24 questions.

## Ch. 27 — Wittig and Other C=C Forming Reactions — `wittig`

- **Hook.** A housefly finds a mate by the smell of a hydrocarbon of 23
  carbons with one double bond, in the Z geometry only. To make it, the
  double bond must be put exactly there, and with that geometry.
- **Recall.** \cref{ch:b2:enolates-aldol} (aldol condensation),
  \cref{ch:b2:alkene-redox} (alkynes to Z-alkenes); Year 1 volume: E1, E2,
  Zaitsev's rule, SN2, Grignard reagents and polarity inversion, Z/E
  descriptors; school volume: atom economy.
- **Sections.** 1 Phosphonium salts and ylides (SN2 of triphenylphosphine;
  deprotonation; stabilised and non-stabilised ylides). 2 The Wittig
  reaction (betaine-free mechanism through an oxaphosphetane; the P=O bond as
  driving force; the double bond placed where the C=O was). 3 Stereoselectivity
  (non-stabilised ylides give Z, stabilised ones E). 4 The
  Horner–Wadsworth–Emmons reaction (phosphonates by the Michaelis–Arbuzov
  reaction; E-selective; a water-soluble by-product). 5 Choosing a C=C
  forming method (elimination, aldol condensation, Wittig and HWE, partial
  reduction of alkynes; metathesis in the Year 3 volume).
- **Definitions.** `def:b2:wittig:ylide` (phosphonium salt, phosphonium
  ylide, stabilised ylide); `:wittig` (Wittig reaction, oxaphosphetane);
  `:hwe` (phosphonate, Horner–Wadsworth–Emmons reaction).
- **Ownership check.** Not in the map. Book 2 owns *polarity inversion*,
  *regioselective* and *stereoselective reaction*, *Zaitsev's rule*
  (recalled); Book 1 *atom economy* (recalled in prose). Book 4 owns olefin
  metathesis (pointer).
- **Statements.** `prop:…:ylide-acidity` stabilised ylides from weak bases,
  non-stabilised ones need BuLi (argued with $\mathrm pK_a$ ranges);
  `prop:…:regiospecific` the C=C forms exactly at the former carbonyl,
  unlike an elimination (argued); `prop:…:driving` the P=O bond makes the
  reaction downhill (argued); `prop:…:stereo` Z from non-stabilised, E from
  stabilised ylides (`\admitted` as an observation with the kinetic/thermodynamic
  explanation); `prop:…:hwe` E-selectivity and the phosphate by-product
  (argued).
- **Methods.** `met:…:wittig-disconnection` (split a C=C into a carbonyl and
  an ylide, choose the halide side); `met:…:choose-cc` (table of methods and
  their selectivities).
- **Figures.** S phosphonium salt and ylide (chemfig, resonance); S Wittig
  mechanism through the oxaphosphetane with `\chemmove`; S stereochemical
  outcomes (structures); S HWE to ethyl cinnamate; AI a vitamin-capsule
  production line (hook alternative) — or no AI; P G. Wittig (to find; only
  if free).
- **Ledger.** `ghs:` triphenylphosphine, butyllithium, sodium hydride,
  triethyl phosphite (PubChem).
- **Exercises palette.** Ylide from a halide (★); Wittig product of
  benzaldehyde and the ylide from iodomethane (★); stabilised or not (★);
  HWE product (★); methylenation of cyclohexanone versus elimination routes
  (★★); retro-Wittig of stilbene (★★); geometry with two ylides (★★); atom
  economy of a Wittig step (★★); a Michaelis–Arbuzov reaction (★★); a polyene
  by two Wittig steps (★★★); Wittig versus aldol condensation for an enone
  (★★★); designing a Z-alkene by two routes (★★★).
- **Weekend problem — "A pheromone by Wittig".** I retrosynthesis of
  (Z)-tricos-9-ene into an aldehyde and a phosphonium salt; II the
  non-stabilised ylide and the Z selectivity; III triphenylphosphine oxide:
  mass and atom economy; IV the alternative through an alkyne and a poisoned
  catalyst. **Named number: the mass of triphenylphosphine oxide co-produced
  per gram of pheromone, ≈ 0.86 g.** 24 questions.

## Ch. 28 — Retrosynthesis and Multistep Strategy — `retrosynthesis`

- **Hook.** A target molecule is drawn on the board; nobody knows yet how to
  make it. The chemist works backwards, cutting bonds on paper, until the
  pieces are things that can be bought.
- **Recall.** Every organic chapter of this book (ch21–27); Year 1 volume:
  protecting groups and acetal protection, Grignard reagents and polarity
  inversion, Williamson synthesis, chemoselectivity, oxidation of alcohols
  (with the promise of "milder, anhydrous reagents, described in the Year 2
  volume"); school volume: atom economy.
- **Sections.** 1 Thinking backwards: target, disconnection, synthons,
  synthetic equivalents. 2 One-group disconnections and functional-group
  interconversions (C–O and C–N bonds; C–C by organometallics and enolates;
  the oxidation-level toolbox, including mild oxidations of alcohols to
  aldehydes). 3 Two-group disconnections: 1,3-dioxygenated (aldol),
  1,5-dicarbonyl (Michael), 1,3-dicarbonyl (Claisen), cyclohexenes
  (Diels–Alder), cyclohexenones (Robinson), alkenes (Wittig). 4 Protecting
  groups in a route (choosing them; orthogonal sets; fewer is better).
  5 Judging a route (overall yield, number of steps, selectivity, cost,
  hazard, atom economy).
- **Definitions.** `def:b2:retrosynthesis:analysis` (retrosynthetic
  analysis, target molecule); `:disconnection` (disconnection, synthon,
  synthetic equivalent); `:fgi` (functional-group interconversion);
  `:orthogonal` (orthogonal protecting groups).
- **Ownership check.** Map owner (retrosynthesis, disconnection, synthon).
  Book 2 owns *protecting group*, *protection*, *deprotection*, *polarity
  inversion*; Book 1 *atom economy*: recalled. Book 4 ch30 owns convergent
  and linear strategies, protecting-group economy and total synthesis:
  convergence is mentioned in plain words without a definition.
  *Orthogonal protecting groups* not in the map: earliest need, contested low
  with Book 4 ch30 (report point 2).
- **Statements.** `prop:…:overall-yield` overall yield = product of the step
  yields (proof) and its consequence for long sequences; `prop:…:patterns`
  the table of 1,n-relationships and their natural disconnections (argued;
  1,4 and 1,6 need polarity inversion or a cleavage); `prop:…:mild-oxidation`
  oxidation of a primary alcohol stops at the aldehyde without water
  (argued: no hydrate to oxidise further).
- **Methods.** `met:…:retrosynthesis` (procedure: functional groups, FGI,
  strategic bonds, synthons → reagents, chemoselectivity, forward route);
  `met:…:protect-in-route` (when and what to protect).
- **Figures.** S a retrosynthetic tree with ⇒ arrows (TikZ + chemfig; the
  retrosynthetic-arrow style of report point 4); S synthons and their
  equivalents (acceptor and donor synthons); S map of two-group
  disconnections; S overall yield versus number of steps (pgfplots of the
  formula $\rho^n$); P E. J. Corey (to find) in a `history` box.
- **Ledger.** `ghs:` pyridinium chlorochromate, Dess–Martin periodinane,
  oxalyl chloride (PubChem).
- **Exercises palette.** Disconnect five alcohols (★); name synthons and
  equivalents (★); overall yield of a five-step route (★); a protecting group
  for a ketone during an ester reduction (★); 1,3-diol retrosynthesis (★★);
  a cyclohexene by Diels–Alder (★★); a cyclohexenone by Robinson (★★); two
  routes compared (★★); oxidation of a primary alcohol to the aldehyde: which
  reagent (★★); orthogonal protection in a diol–amine (★★★); a 1,4-dicarbonyl
  (★★★); full plan for a fragrance ketone (★★★).
- **Weekend problem — "Raspberry ketone".** I retrosynthesis of
  4-(4-hydroxyphenyl)butan-2-one: aldol condensation then selective reduction
  of C=C; II is the phenol a problem? protection or not; III an alternative
  route (Heck coupling, from ch20); IV judging: overall yield, steps, atom
  economy. **Named number: the overall yield of the two-step route (85 % and
  92 %), 78 %.** 25 questions.

## Ch. 29 — Polymers: Synthesis, Structure and Properties — `polymer-synthesis`

- **Hook.** Nylon stockings went on sale in 1939; they came from a laboratory
  that had set out to understand how small molecules join into long ones, and
  learnt that a 99 % yield is not enough.
- **Recall.** School volume: polymer, monomer, repeat unit, polymerisation,
  degree of polymerisation, addition and condensation polymers,
  thermoplastics and thermosets; Year 1 volume: radicals and homolysis,
  carbocations and carbanions, steady-state approximation;
  \cref{ch:b2:acyl-substitution} (esters, amides),
  \cref{ch:b2:catalytic-cycles} (insertion; Ziegler–Natta in the Year 3
  volume).
- **Sections.** 1 Polymers re-founded: degree of polymerisation,
  number-average and mass-average molar masses, dispersity. 2 Step-growth
  polymerisation (polyesters, polyamides; the Carothers equation; stoichiometric
  imbalance; the Flory distribution). 3 Chain-growth polymerisation (radical:
  initiation, propagation, termination; rate law by the steady state;
  kinetic chain length; ionic and living polymerisations; copolymers).
  4 Structure: tacticity, crystallinity, glass transition and melting; linear,
  branched, cross-linked chains. 5 Properties and uses: thermoplastics,
  elastomers, fibres, thermosets; recycling (school volume recall).
- **Definitions.** `def:b2:polymer-synthesis:polymer` (polymer, monomer,
  repeat unit, degree of polymerisation — **re-found** g12 `polymers`);
  `:averages` (number-average molar mass, mass-average molar mass,
  dispersity); `:step-chain` (step-growth polymerisation, chain-growth
  polymerisation); `:chain-steps` (initiation, propagation, termination,
  radical initiator); `:chain-length` (kinetic chain length); `:living`
  (living polymerisation); `:copolymer` (copolymer); `:tacticity`
  (tacticity, isotactic, syndiotactic, atactic); `:transitions` (glass
  transition temperature, degree of crystallinity); `:elastomer`
  (elastomer). Named-law statement: `thm:…:carothers` (Carothers equation).
- **Ownership check.** Map owner (chain-growth, step-growth, tacticity,
  glass transition; re-founds g12 polymers). Book 1 *thermoplastic*,
  *thermoset* (g8) recalled. Book 4 ch13 owns *chain reaction*: the steps
  *initiation*, *propagation*, *termination* are needed first here —
  contested (proposal: this book defines the three steps for polymerisation,
  Book 4 defines *chain reaction*, *chain branching*, explosions, and
  recalls the steps). Book 4 ch21 owns Ziegler–Natta (pointer).
- **Statements.** `thm:…:carothers` $\bar X_n = 1/(1 - p)$ (proof: counting
  functional groups); `cor:…:imbalance` $\bar X_n = (1 + r)/(1 + r - 2rp)$
  (proof); `thm:…:flory` most probable distribution, $\bar M_w/\bar M_n = 1 + p$
  (proof: geometric series and their derivatives); `thm:…:radical-rate`
  $R_p = k_p[\mathrm M]\sqrt{fk_d[\mathrm I]/k_t}$ (proof: steady state on the
  radicals, Year 1 tool); `prop:…:chain-length` (proof);
  `prop:…:living` Poisson distribution, $Đ \approx 1 + 1/\bar X_n$ (proof
  sketched; `\admitted` for the distribution).
- **Methods.** `met:…:averages` (compute $\bar M_n$, $\bar M_w$, $Đ$ from a
  sample's fractions); `met:…:classify` (step or chain from the monomer and
  mechanism).
- **Figures.** F `polymer-distributions` part a (Flory mass distributions at
  $p$ = 0.95, 0.98, 0.99), part b ($\bar X_n$ versus $p$), part c (Poisson
  versus Flory at the same $\bar X_n$); S radical polymerisation of styrene
  (initiation, propagation, termination; half-headed arrows); S tacticity of
  polypropene (zig-zag chains with wedges); S modulus versus temperature
  (glassy, transition, rubbery plateau, flow; schematic, labelled as such);
  AI plastic pellets and fibre spinning in a plant (hook or section 5); P
  W. Carothers (`File:Wallace Carothers, in the lab.jpg`, PD, found) in a
  `history` box.
- **Ledger.** Book 1/2 `hist:polyamides-1934`, `hist:nylon-production-1939`,
  `plastics:` rows read-only; `tg:` of polystyrene, poly(methyl methacrylate),
  polyethene, natural rubber (source to secure — at risk; else relative
  statements only); `ghs:` styrene, dibenzoyl peroxide, hexane-1,6-diamine,
  hexanedioic acid (PubChem).
- **Exercises palette.** Repeat units of five polymers (★); step or chain
  (★); $\bar M_n$ from $\bar X_n$ (★); tacticity from a drawing (★); $\bar M_n$
  and $\bar M_w$ of a two-fraction sample (★★); Carothers at 98 % and 99.5 %
  (★★); 1 % excess of one monomer (★★); radical rate when the initiator is
  doubled (★★); glass transition and plasticisers (★★); the Flory
  distribution's dispersity derived (★★★); PET by transesterification
  (★★★); copolymer composition from feed (given reactivity data) (★★★).
- **Weekend problem — "Nylon-6,6 by the kilogram".** I monomers, the nylon
  salt and the 1 : 1 balance; II Carothers: extent needed for a given
  $\bar M_n$; III a 1 % excess of diamine and end-capping; IV the Flory
  distribution: $\bar M_w$, $Đ$, water released per kilogram. **Named number:
  the extent of reaction that gives $\bar M_n = 20$ kg/mol (computed, ≈
  0.994).** 25 questions.

## Ch. 30 — Biomolecules: Amino Acids, Sugars, Lipids and Nucleotides — `biomolecules`

- **Hook.** A sweetener two hundred times sweeter than sugar is two amino
  acids joined by a single amide bond, one of them as its methyl ester; change
  the configuration of either, and the sweetness is gone.
- **Recall.** Year 1 volume: CIP rules, Fischer projections, chirality,
  hemiacetals and acetals, $\mathrm pK_a$ and distribution diagrams,
  amphiphilic molecules; \cref{ch:b2:acyl-substitution} (amides, esters,
  saponification, activation), \cref{ch:b2:amines},
  \cref{ch:b2:retrosynthesis} (protecting groups in a route).
- **Sections.** 1 Amino acids (structure, L configuration, side-chain
  families; zwitterion; isoelectric point; charge versus pH). 2 Peptides (the
  planar peptide bond; coupling with an activating agent and protecting
  groups; solid-phase synthesis in principle). 3 Carbohydrates (aldoses and
  ketoses; D/L; Fischer to Haworth; anomers and mutarotation; glycosides;
  reducing sugars; sucrose, starch, cellulose). 4 Lipids (fatty acids,
  triglycerides, saponification and soaps, phospholipids; micelles named, not
  defined). 5 Nucleotides (bases, nucleosides, nucleotides, the
  phosphodiester backbone, base pairing).
- **Definitions.** `def:b2:biomolecules:amino-acid` (α-amino acid, side
  chain, zwitterion, isoelectric point); `:peptide` (peptide bond, peptide,
  peptide coupling, coupling agent); `:d-l` (D/L descriptors); `:sugar`
  (monosaccharide, aldose, ketose); `:anomer` (Haworth projection, anomeric
  carbon, anomers, mutarotation); `:glycoside` (glycoside, glycosidic bond,
  reducing sugar); `:lipid` (fatty acid, triglyceride, phospholipid);
  `:nucleotide` (nucleobase, nucleoside, nucleotide, phosphodiester bond).
- **Ownership check.** Not in the map. Book 2 owns *Fischer projection*,
  *hemiacetal*, *acetal*, *amphiphilic*, *chiral* (recalled); Book 4 owns
  *micelle* (university) and bioinorganic chemistry (named only). The
  biology series defines some of these words for biology; linking is per
  book, so no clash.
- **Statements.** `prop:…:pi` $\mathrm{pI} = (\mathrm pK_{a1} + \mathrm pK_{a2})/2$
  for a neutral side chain (proof from the distribution); `prop:…:planar`
  the peptide bond is planar with restricted rotation (argued: amide
  resonance); `prop:…:coupling` why protection and activation are both
  needed (argued); `prop:…:mutarotation` equilibrium composition of the
  glucose anomers from the specific rotations (proof: Biot's additivity,
  Year 1); `prop:…:reducing` free hemiacetals reduce, glycosides do not
  (argued); `prop:…:pairing` A–T two hydrogen bonds, G–C three (structures).
- **Methods.** `met:…:charge` (net charge of an amino acid or peptide at a
  given pH); `met:…:haworth` (from Fischer to Haworth); `met:…:peptide`
  (protect, activate, couple, deprotect).
- **Figures.** F `amino-acid-charge` part a (net charge versus pH for
  glycine, aspartic acid, lysine; IUPAC $\mathrm pK_a$), part b (glycine's
  three forms); S peptide-bond resonance and planarity; S glucose: Fischer,
  open chain, Haworth α and β; S saponification of a triglyceride and a soap
  or phospholipid layer schematic; S base pairs A–T and G–C with hydrogen
  bonds (chemfig); AI eggs frying (proteins denaturing) (hook or section 2);
  P E. Fischer (`File:Hermann Emil Fischer c1895.jpg`, PD, found) in a
  `history` box (1891).
- **Ledger.** Book 2 `pka:glycine1`, `pka:glycine2` read-only; `pka:` alanine,
  aspartic acid, glutamic acid, lysine, histidine (IUPAC-PKA); `rot:` specific
  rotations of α- and β-D-glucopyranose and of the equilibrium mixture
  (PubChem, else EXCLUDED and exercise data); `mp:` stearic and oleic acids
  (PubChem).
- **Exercises palette.** Zwitterion of alanine (★); pI of glycine (★); draw
  Ala-Gly (★); D or L from a Fischer projection (★); charge of a tripeptide
  at pH 7 (★★); why a coupling agent (★★); Haworth of fructose (★★); anomer
  proportions from rotations (★★); sucrose is not reducing (★★); saponification
  value of triolein (★★★); a protected dipeptide synthesis plan (★★★);
  complementary strand and hydrogen-bond count (★★★).
- **Weekend problem — "Aspartame".** I the two amino acids and their
  configurations; II acid–base behaviour and charge versus pH (model from the
  amino acids' $\mathrm pK_a$); III synthesis: protection, activation,
  coupling, deprotection, and the α/β problem of aspartic acid; IV hydrolysis
  in a soft drink. **Named number: the mass of methanol released by complete
  hydrolysis of 180 mg of aspartame, ≈ 19.6 mg.** 25 questions.

## Ch. 31 — Chromatography — `chromatography`

- **Hook.** A drop of an energy drink is injected into a steel column no
  longer than a pen; four minutes later a detector reports how much caffeine
  the can holds, to a few per cent.
- **Recall.** Year 1 volume: partition coefficient, retention factor of TLC
  ($R_f$), running a TLC, extraction; \cref{ch:b2:liquid-vapour-diagrams}
  (theoretical plate); school volume: paper and thin-layer chromatography,
  chromatogram, stationary phase, eluent.
- **Sections.** 1 Principle: partition between a stationary and a mobile
  phase; retention time, hold-up time, retention factor $k$; $k = KV_s/V_m$.
  2 Plate theory: Gaussian peaks, plate number from peak widths, plate
  height; band broadening and the van Deemter equation; best flow rate.
  3 Separating two compounds: selectivity factor, resolution, the resolution
  equation, baseline separation. 4 Techniques: column and flash chromatography
  (preparative), gas chromatography (carrier gas, columns, temperature ramps,
  detectors), high-performance liquid chromatography (normal and reversed
  phase, isocratic and gradient elution, UV detection). 5 Quantitative
  analysis: areas, response factors, external calibration, internal standard.
- **Definitions.** `def:b2:chromatography:principle` (chromatography,
  stationary phase — **re-found** g10, mobile phase, elution); `:retention`
  (retention time, hold-up time, retention factor $k$ — **contested
  homonym**, see ownership); `:plates` (plate number, plate height);
  `:separation` (selectivity factor, resolution); `:techniques` (gas
  chromatography, high-performance liquid chromatography, reversed phase,
  gradient elution); `:quantitative` (response factor, internal standard).
- **Ownership check.** Not in the map (partition coefficient is Book 2's,
  recalled). Book 1 owns *stationary phase*, *eluent*, *chromatogram*, *TLC*
  (re-found: *stationary phase*; the others used). **Contested homonym:**
  Book 2 ch29 owns *retention factor* as TLC's $R_f$; the column quantity
  $k = (t_R - t_M)/t_M$ carries the same name in current nomenclature.
  Proposal: this book defines it as "retention factor $k$ of a column",
  harvested under that phrase, with a remark contrasting it with $R_f$;
  alternative if refused: no definition, $k$ named in prose only (report
  point 2). *Theoretical plate* is this book's ch7 (recalled).
- **Statements.** `prop:…:k-and-K` $k = KV_s/V_m$ (proof: time shared
  between phases); `prop:…:retention-time` $t_R = t_M(1 + k)$ (proof);
  `prop:…:plate-number` $N = (t_R/\sigma_t)^2 = 16(t_R/w)^2 =
  5.54(t_R/w_{1/2})^2$ (proof: widths of a Gaussian); `prop:…:van-deemter`
  $H = A + B/u + Cu$, minimum at $u = \sqrt{B/C}$, $H_{\min} = A + 2\sqrt{BC}$
  (equation `\admitted` with the meaning of each term; minimum proved);
  `thm:…:resolution` $R_s = \frac{\sqrt N}{4}\,\frac{\alpha - 1}{\alpha}\,
  \frac{k_2}{1 + k_2}$ (proof from the definitions, equal plate numbers,
  $w = 4\sigma$); `prop:…:internal-standard` amount from area ratios and a
  response factor (proof).
- **Methods.** `met:…:improve-resolution` (act on $N$, $\alpha$, $k$);
  `met:…:internal-standard` (quantification with an internal standard).
- **Figures.** F `chromatogram` part a (two Gaussian peaks at $R_s$ = 0.75,
  1.0, 1.5), part b (van Deemter curve with its three terms), part c (a
  simulated reversed-phase chromatogram for the problem: invented retention
  data, said so); S bands migrating down a column (three snapshots); S gas
  chromatograph (carrier gas, injector, oven with coiled column, detector,
  data system); S HPLC (solvent reservoirs, pump, injector, column, UV cell);
  AI an analytical laboratory with chromatographs (hook); P M. Tsvet
  (`File:Mikhail Tsvet.jpg`, PD, found) in a `history` box (1906).
- **Ledger.** `ghs:` acetonitrile, methanol, hexane (PubChem); no retention
  data printed as facts (all chromatographic numbers are exercise data).
- **Exercises palette.** $t_R$, $t_M$ → $k$ (★); plate number from a peak (★);
  plate height of a column (★); GC or HPLC for five analytes (★); resolution
  of two peaks (★★); plates needed for $R_s = 1.5$ (★★); van Deemter optimum
  (★★); reversed-phase elution order (★★); internal-standard calculation
  (★★); doubling the column length: what $R_s$ gains (★★★); the resolution
  equation derived (★★★); choosing $k$ to save time at fixed $R_s$ (★★★).
- **Weekend problem — "Caffeine in an energy drink".** I reversed phase:
  elution order of caffeine, the internal standard and the sugars; II column
  performance: $N$, $H$, $R_s$ from the chromatogram data; III improving the
  separation (what doubling $N$ does); IV quantification by internal
  standard. **Named number: the mass of caffeine per 250 mL can (exercise
  data, computed).** 25 questions.

## Ch. 32 — Mass Spectrometry and Atomic Spectroscopy — `mass-spec-atomic`

- **Hook.** Fireworks are red with strontium, green with barium, yellow with
  sodium; a mass spectrometer, more modestly, weighs single molecules and
  sorts them by their isotopes.
- **Recall.** Year 1 volume: energy levels and spectral lines, carbocations
  and radicals, degree of unsaturation, absorbance; school volume:
  isotopes, abundance; \cref{ch:b2:chromatography} (GC as an inlet).
- **Sections.** 1 The mass spectrometer: ionisation (electron impact,
  electrospray), analysers (time of flight; quadrupole and magnetic sector
  described), detector; $m/z$. 2 The molecular ion: the nitrogen rule; isotope
  patterns (carbon-13, chlorine, bromine); exact masses and high resolution.
  3 Fragmentation: α-cleavage, acylium ions, alkyl losses, the McLafferty
  rearrangement; the base peak. 4 Atomic spectroscopy: emission and absorption
  lines; flame emission; atomic absorption (hollow-cathode lamp, calibration);
  inductively coupled plasma (emission and mass). 5 Elemental analysis in
  practice (calibration, interferences; detection limits in ch34).
- **Definitions.** `def:b2:mass-spec-atomic:spectrum` (mass spectrometry,
  mass-to-charge ratio, mass spectrum, base peak); `:molecular-ion`
  (molecular ion, fragment ion); `:isotope-pattern` (isotope pattern);
  `:nitrogen-rule` (nitrogen rule); `:exact-mass` (monoisotopic mass,
  high-resolution mass spectrometry); `:fragmentation` (α-cleavage, McLafferty
  rearrangement); `:atomic` (atomic emission spectrometry, atomic absorption
  spectrometry, hollow-cathode lamp, inductively coupled plasma).
- **Ownership check.** Map owner (*molecular ion*). Book 2 owns *energy
  level*, *absorbance*, *degree of unsaturation*, *carbocation*, *radical*
  (recalled); Book 1 *isotope*, *abundance*. Book 4: none (rovibrational and
  electronic spectroscopy are its own).
- **Statements.** `prop:…:time-of-flight` $t = L\sqrt{m/(2zeU)}$ (proof,
  energy conservation from physics); `prop:…:m-plus-one` $I(M+1)/I(M) \approx
  n_C\,a_{13}/a_{12}$ (proof: binomial, first order); `prop:…:halogen-patterns`
  patterns of $n$ Cl and $m$ Br from the binomial expansion (proof);
  `prop:…:nitrogen-rule` an odd nominal mass means an odd number of N (for
  C, H, N, O, S, halogens; proof by parity of valences); `prop:…:resolving`
  resolving power needed to separate two ions (definition applied: CO,
  \ce{N2}, \ce{C2H4} at 28); `prop:…:mclafferty` a γ hydrogen is required
  (argued, six-membered transition state); `prop:…:aas` absorbance
  proportional to the concentration over a range (`\admitted`, recall of
  Beer–Lambert).
- **Methods.** `met:…:read-ms` (molecular ion, isotope pattern, nitrogen rule,
  losses, base peak → hypotheses); `met:…:aas-calibration`.
- **Figures.** F `mass-spectra` part a (isotope clusters of Cl, \ce{Cl2},
  Br, \ce{Br2}, ClBr from ledger abundances), part b (EI spectrum of
  butan-2-one at ledger peaks), part c (spectrum of 1-bromopropane), part d
  (the unknown of the problem); S time-of-flight spectrometer (source,
  acceleration, drift tube, detector); S McLafferty rearrangement with
  half-headed arrows (chemfig); S atomic absorption spectrometer (lamp, flame,
  monochromator, detector); AI fireworks over a city (hook; colours reviewed
  against the ledger lines); P F. W. Aston (`File:Francis William
  Aston.jpg`, PD, found) and G. Kirchhoff, R. Bunsen and H. Roscoe
  (`File:Kirchhoff Bunsen Roscoe.jpg`, PD, found) in `history` boxes.
- **Ledger.** Existing `iso:` rows read-only (\ce{^{12}C}, \ce{^{13}C},
  \ce{^{35}Cl}, \ce{^{37}Cl}); new `iso:` \ce{^{79}Br}, \ce{^{81}Br}, H, N, O, S
  isotopes (CIAAW-ISO); `mass:` exact isotopic masses (NIST-AWIC); `ms:`
  peaks of butan-2-one, 1-bromopropane, pentan-2-one (WEBBOOK-MS); `asd:`
  Na D lines, Sr, Ba, Li, Cu lines (NIST-ASD).
- **Exercises palette.** $m/z$ of ions of given charge (★); nitrogen rule
  (★); Cl or Br from a pattern (★); flame colour to element (★); carbon count
  from $M+1$ (★★); exact masses of CO, \ce{N2}, \ce{C2H4} and the resolving
  power (★★); fragments of pentan-3-one (★★); McLafferty of pentan-2-one
  (★★); AAS calibration and a sample (★★); time of flight of two ions (★★★);
  \ce{CH2Cl2} cluster computed (★★★); ICP-MS isobaric interference
  (★★★).
- **Weekend problem — "An unknown halide".** I the molecular-ion cluster
  with one Cl and one Br; II $M+1$ → number of carbons; III the fragments;
  IV the structure, checked against every peak. **Named number: the computed
  intensity ratio of the $M$, $M+2$ and $M+4$ peaks for one chlorine and one
  bromine, ≈ 3 : 4 : 1 (exactly from the CIAAW abundances).** 25 questions.

## Ch. 33 — Structure Determination: ¹³C NMR, MS and IR Together — `structure-determination`

- **Hook.** A fragrance laboratory receives a vial of an unknown that smells
  of jasmine. A mass spectrum, an infrared spectrum and two NMR spectra later,
  it has a name.
- **Recall.** Year 1 volume: chemical shift, shielding, equivalent protons,
  integration, coupling, multiplets, the $n + 1$ rule, IR wavenumbers and the
  fingerprint region, degree of unsaturation, solving a structure from three
  spectra; \cref{ch:b2:mass-spec-atomic}.
- **Sections.** 1 Carbon-13 NMR: low abundance, decoupling from protons,
  one line per kind of carbon, shift ranges (0–220 ppm), symmetry; why
  intensities are not counts. 2 DEPT: telling \ce{CH3}, \ce{CH2}, CH and
  quaternary carbons apart. 3 Combining techniques: formula (MS, high
  resolution), unsaturation, functional groups (IR), skeleton (¹³C, DEPT),
  connectivity (¹H). 4 Solving unknowns: the method and three worked cases
  (an ester, a ketone, an aromatic). 5 Traps: exchangeable protons,
  overlapping signals, diastereotopic protons, second-order patterns
  (qualitatively).
- **Definitions.** `def:b2:structure-determination:c13` (carbon-13 NMR,
  broadband decoupling, equivalent carbons); `:dept` (DEPT, quaternary
  carbon).
- **Ownership check.** Map owner (¹³C NMR, DEPT). Book 2 owns every ¹H NMR,
  IR and UV term (recalled), *degree of unsaturation*, and *primary/secondary/
  tertiary carbon* (*quaternary carbon* was not defined there: earliest need,
  low risk). Book 4 owns pulse NMR and 2D methods: DEPT's result is used, its
  pulse sequence `\admitted` with "the Year 3 volume explains pulses".
- **Statements.** `prop:…:no-cc-coupling` carbon–carbon couplings are not
  seen (proof: probability that two neighbours are both ¹³C ≈ 1.2 × 10⁻⁴);
  `prop:…:signals` number of lines = number of kinds of carbon (argued from
  symmetry); `prop:…:dept` DEPT-135: CH and \ce{CH3} up, \ce{CH2} down, C
  absent; DEPT-90: CH only (`\admitted`); `prop:…:intensities` decoupled
  line heights are not proportional to carbon counts (argued).
- **Methods.** `met:…:solve` (formula → unsaturation → IR → ¹³C/DEPT → ¹H →
  assemble → check every datum).
- **Figures.** F `nmr-spectra` part a (decoupled ¹³C, DEPT-135 and DEPT-90 of
  butan-2-one), part b (the same for ethyl benzoate), parts c–e (the worked
  unknowns, ¹³C and first-order ¹H at ledger shifts); S ¹³C shift chart
  (ranges by carbon type, ledger); S decision flow chart for unknowns; P a
  high-field NMR magnet (to find; no visible brand) — optional.
- **Ledger.** `c13:` shifts of butan-2-one, ethyl benzoate, benzyl ethanoate
  and the worked unknowns (NMRSHIFTDB); `nmr:` ¹H shifts and $J$ for the same
  (NMRSHIFTDB; reuse Book 2 `nmr:` rows read-only where they exist);
  `ir:` C=O bands (WEBBOOK-IR or Book 2 rows); `ms:` peaks (WEBBOOK-MS);
  `nmrr:` ¹³C ranges for the chart (a cited review or NMRSHIFTDB statistics).
- **Exercises palette.** ¹³C line counts of the xylenes (★); DEPT assignment
  of butan-2-ol (★); shift region of a carbon (★); unsaturation of
  \ce{C8H8O2} (★); \ce{C4H8O} unknown from ¹³C and IR (★★); distinguishing
  pentan-2-one and pentan-3-one (★★); an ester from MS and ¹H (★★);
  1,2- versus 1,4-dichlorobenzene (★★); diastereotopic protons in a
  chiral molecule (★★); a full unknown \ce{C9H10O} (★★★); \ce{C5H10O2}
  isomers sorted (★★★); a misassigned spectrum to correct (★★★).
- **Weekend problem — "Four spectra of jasmine".** I the formula from the
  molecular ion and $M+1$; II the IR carbonyl band and the ester; III ¹³C and
  DEPT: seven lines, one \ce{CH2}; IV ¹H: the benzylic \ce{CH2} singlet and the
  acetyl methyl; the structure, benzyl ethanoate, checked against the
  fragments (m/z 108, 91, 43). **Named number: seven lines in the decoupled
  ¹³C spectrum of benzyl ethanoate, one of them pointing down in DEPT-135.**
  25 questions.

## Ch. 34 — Statistics of Chemical Measurement — `measurement-statistics`

- **Hook.** Two laboratories measure the lead in the same tap water and find
  9.6 and 11.2 µg/L; the guideline value is 10 µg/L. Is the water fit to
  drink, and do the two laboratories even disagree?
- **Recall.** Year 1 volume: measurement uncertainty, standard uncertainty,
  type A and type B evaluations, expanded uncertainty, relative uncertainty,
  normalised deviation (and its promises: Student's coefficient, the general
  propagation rule "with partial derivatives"); school volume: calibration
  line; \cref{ch:b2:mass-spec-atomic} (atomic absorption).
- **Sections.** 1 Repeated measurements as random variables: mean, standard
  deviation, the normal distribution, the standard deviation of the mean.
  2 Confidence intervals: Student's distribution and coefficients; comparing
  a mean with a reference value and two means. 3 Propagation of uncertainty:
  the law with partial derivatives; sums, products, powers. 4 Calibration by
  least squares: the line, residuals, the uncertainty of an interpolated
  concentration; the standard-addition method. 5 Detection, quantification
  and validation: limits of detection and quantification; trueness and
  precision; repeatability and reproducibility; linearity and range.
- **Definitions.** `def:b2:measurement-statistics:dispersion` (experimental
  standard deviation, standard deviation of the mean);
  `:confidence` (confidence interval, confidence level, Student's
  coefficient); `:calibration` (calibration curve — **re-found** g11
  "calibration line", least-squares line, residual); `:standard-addition`
  (standard-addition method); `:limits` (limit of detection, limit of
  quantification); `:validation` (trueness, precision, bias, repeatability,
  reproducibility, method validation). Named-law statement:
  `thm:…:propagation` (law of propagation of uncertainty).
- **Ownership check.** Book 2 ch29 owns *measurement uncertainty*, *standard
  uncertainty*, *type A/B evaluation*, *expanded uncertainty*, *relative
  uncertainty*, *normalised deviation*: recalled, never redefined (the
  propagation theorem completes its admitted combination rule). Book 1 owns
  *calibration line* (re-found as *calibration curve*). **Math level:** the
  batch file puts linear regression in Year 3's mathematics while the outline
  puts calibration by regression here; the least-squares line is derived with
  partial derivatives (a Year-2 tool), the statistics of the fitted
  parameters are `\admitted` (report point 9).
- **Statements.** `thm:…:mean-variance` $\operatorname{var}(\bar x) =
  \sigma^2/n$ for independent repeats (proof: variance of a sum) — proves
  Book 2's admitted $u = s/\sqrt n$; `prop:…:student` $(\bar x - \mu)/(s/\sqrt
  n)$ follows Student's law with $n - 1$ degrees of freedom (`\admitted`);
  `thm:…:propagation` $u^2(y) = \sum(\partial f/\partial x_i)^2u^2(x_i)$ for
  independent inputs (proof: first-order Taylor, variance of a linear
  combination); `cor:…:products` relative uncertainties of a product add in
  quadrature (proof); `thm:…:least-squares` slope and intercept (proof:
  $\partial S/\partial a = \partial S/\partial b = 0$, minimum by the Hessian);
  `prop:…:interpolation` uncertainty of a concentration read on the line
  (`\admitted`); `prop:…:lod` $x_{\text{LOD}} = 3s_{\text{blank}}/b$, $x_{\text{LOQ}}
  = 10s_{\text{blank}}/b$ (argued from the false-positive probability).
- **Methods.** `met:…:confidence-interval`; `met:…:propagate`;
  `met:…:calibrate` (fit, look at residuals, interpolate, report);
  `met:…:standard-addition`.
- **Figures.** F `regression` part a (calibration points with the fitted
  line), part b (residual plot), part c (Student densities for 2, 5 and ∞
  degrees of freedom against the normal law), part d (standard-addition line
  and its intercept), part e (Student coefficients computed, table for the
  text); S two confidence intervals against a limit value (error bars); AI a
  water-testing laboratory (hook); P W. S. Gosset (`File:William Sealy
  Gosset.jpg`, PD, found) in a `history` box (1908).
- **Ledger.** `who:` lead guideline value in drinking water (WHO-DWQ);
  `asd:` the Pb 283.3 nm line (NIST-ASD) for the problem's AAS; Student
  quantiles are mathematics (computed and tested, no row).
- **Exercises palette.** Mean and $s$ of five titrations (★); 95 %
  interval (★); propagation for $c = m/(MV)$ (★); slope and intercept of four
  points (★); comparison of a mean with a certified value (★★); propagation
  for a pH or a logarithm (★★); LOD from ten blanks (★★); standard addition
  (★★); repeatability versus reproducibility from a two-lab study (★★);
  derive the least-squares formulas (★★★); dilution chains: where the
  uncertainty comes from (★★★); the two laboratories of the hook compared
  (★★★).
- **Weekend problem — "Lead in tap water".** I atomic-absorption calibration
  (five standards, least squares, residuals); II three replicate readings of
  the sample → concentration and its confidence interval; III propagation
  through the dilution, limit of detection and of quantification; IV verdict
  against the guideline value. **Named number: the lead concentration of the
  sample with its 95 % interval (exercise data, computed), compared with
  10 µg/L.** 26 questions.

## Ch. 35 — Lab Techniques II: Synthesis and Analysis in Practice — `lab-techniques-2`

- **Hook.** A Grignard reaction fails on a Monday morning: the flask was
  rinsed and not dried. Run again in oven-dried glassware under nitrogen, with
  the halide added drop by drop, it works — and the difference is all in the
  set-up.
- **Recall.** Year 1 volume: lab techniques I (GHS labels, H and P
  statements, extraction, recrystallisation, distillation, TLC, melting point,
  refractometry, uncertainty), Grignard reagents, the organic apparatus;
  \cref{ch:b2:continuous-reactors} (adiabatic rise, runaway),
  \cref{ch:b2:chromatography}, \cref{ch:b2:structure-determination},
  \cref{ch:b2:measurement-statistics}.
- **Sections.** 1 Running a reaction under control: temperature (cooling
  baths, reflux, an internal thermometer), slow addition and the danger of
  accumulation, stirring. 2 Dry conditions and inert atmosphere: drying
  glassware and solvents, nitrogen or argon with a bubbler or balloon, septa
  and syringes (the Schlenk line and glovebox in the Year 3 volume). 3 Work-up:
  quenching, separating acids, bases and neutral compounds by extraction,
  brine, drying agents, filtration, evaporation under reduced pressure.
  4 Purification: flash chromatography (choosing the eluent from TLC,
  loading, fractions); distillation under reduced pressure (boiling point
  versus pressure). 5 Purity and identity: melting range, TLC, GC/HPLC area
  per cent, NMR against impurities, specific rotation; reporting a yield
  corrected for purity.
- **Definitions.** `def:b2:lab-techniques-2:inert` (inert atmosphere);
  `:work-up` (work-up; *quenching* stays Book 1's word); `:acid-base-extraction` (acid–base extraction); `:drying-agent`
  (drying agent); `:flash` (flash chromatography); `:reduced-pressure`
  (distillation under reduced pressure).
- **Ownership check.** Book 2 ch29 owns the lab vocabulary of Year 1
  (*hazard*, *risk*, *safety data sheet*, *partition coefficient*,
  *recrystallisation*, *retention factor*) and *specific rotation*,
  *optical activity* (ch16): recalled. Book 1 owns *quenching*, *heating under
  reflux*, *distillation*, *extraction*. Book 4 owns the Schlenk line,
  glovebox, lab notebook, risk assessment and *enantiomeric excess*
  (pointer; purity here is chemical purity only).
- **Statements.** `prop:…:acid-base-extraction` a carboxylic acid passes into
  aqueous hydrogencarbonate, a phenol only into hydroxide (proof:
  predominance at pH > p$K_a$ + 2 and the partition of neutral species);
  `prop:…:reduced-pressure` boiling point at reduced pressure from
  Clausius–Clapeyron and Trouton's estimate (proof: physics' Clapeyron
  relation integrated, ch3 tools); `prop:…:accumulation` adding faster than
  the reaction consumes stores reagent and a potential temperature rise
  (proof: ch5's adiabatic rise applied to the accumulated amount);
  `prop:…:column-volumes` a compound elutes after about $1/R_f$ column
  volumes (argued).
- **Methods.** `met:…:anhydrous` (setting up a dry reaction under
  nitrogen); `met:…:work-up` (from the reaction flask to the crude product);
  `met:…:flash` (running a flash column); `met:…:purity` (purity and yield
  report).
- **Figures.** S three-neck flask with dropping funnel, condenser, internal
  thermometer, nitrogen inlet and bubbler, in an ice bath (shared pics
  `threeneck`, `dropfunnel`, `condenser`, `thermometer`, `guardtube`); S
  separation scheme of an acid, a phenol, a base and a neutral compound with
  separating funnels (`sepfunnel`); S flash column (silica, sand, eluent,
  fractions, the TLC of the fractions); F `vacuum-boiling` (boiling point
  versus pressure for two liquids, Clausius–Clapeyron with ledger data; test:
  the curve passes through the normal boiling point); AI a synthesis
  laboratory with fume hoods and a rotary evaporator in the background
  (hook; lab scene, no close-up of glassware).
- **Ledger.** `ghs:` ethoxyethane, oxolane (THF), bromobenzene, magnesium
  sulfate, silica gel, dry ice (PubChem; Book 2 `ghs:Mg` etc. read-only);
  `dvap:`/`tb:` of the liquids of the vacuum example (WEBBOOK-PHASE); Book 2
  `pka:benzoic`, `pka:phenol` read-only.
- **Exercises palette.** Choose a cooling bath (★); which layer is aqueous
  (★); how much drying agent (★); eluent from $R_f$ (★); acid–base separation
  of four compounds (★★); boiling point at 20 mbar (★★); accumulated reagent
  and possible temperature rise (★★); purity from an HPLC trace and from an
  ¹H integral (★★); yield corrected for purity (★★); a failed Grignard
  diagnosed (★★★); scale-up of an addition: time needed for a given cooling
  power (★★★); comparing two purification routes (★★★).
- **Weekend problem — "A Grignard done right".** I hazards and the dry set-up
  (ethoxyethane, bromobenzene, magnesium); II controlled addition: reaction
  enthalpy, accumulation, adiabatic rise (exercise data); III work-up:
  ammonium chloride quench, extraction, drying; IV purification by flash
  chromatography and purity by ¹H NMR (residual biphenyl), yield corrected for
  purity. **Named number: the purity-corrected yield of the alcohol (exercise
  data, ≈ 70 %).** 26 questions.

---

## Cross-cutting plans

### figdata scripts (all in `figdata/bachelor-2/`, tests in `tests/bachelor-2/`)

| script | chapters | computes | the test asserts |
|---|---|---|---|
| `_ledger.py` (helper) | all | ledger values by id (copy of Book 2's helper) | — |
| `thermo-data.py` | 1–4, 6, 9 | every printed $\Delta_r H^\circ$, $\Delta_r S^\circ$, $\Delta_r G^\circ$, $K^\circ$ from ledger rows | Hess closure (a cycle sums to 0 within rounding); $\Delta_r G^\circ = \Delta_r H^\circ - T\Delta_r S^\circ$; each printed value pinned; CODATA vs JANAF agreement within 0.5 kJ/mol where both exist |
| `flame-temperature.py` | 1 | product enthalpy versus $T$ (JANAF increments), adiabatic flame temperature of butane and methane in air and in \ce{O2} | energy balance closes at $T_{\text{ad}}$ (residual < 1 J); constant-$C_p$ variant equals its closed form $T_0 - \xi\Delta_r H^\circ/C_p$; $T_{\text{ad}}$(O₂) > $T_{\text{ad}}$(air) |
| `standard-entropy.py` | 2 | $S^\circ(T)$ of water 0–500 K (Debye start, $\int C_p/T$, transition jumps) | $S^\circ$(l, 298.15 K) within 1 J/(K mol) of CODATA; jump at 373.15 K = $\Delta_{\text{vap}}H/T_b$ |
| `gibbs-extent.py` | 2 | $G(\xi)$ of \ce{N2O4 <=> 2NO2} at 298 K | minimum where $Q(\xi) = K^\circ$; numerical $\dd G/\dd\xi$ = $\Delta_r G^\circ + RT\ln Q$ |
| `raoult-henry.py` | 3 | partial pressures of an ideal and a Margules mixture | Raoult slope at $x \to 1$; Henry constant $= p^*\mathrm e^{A}$; Gibbs–Duhem satisfied numerically |
| `vant-hoff.py` | 4 | $\ln K^\circ(1/T)$ of \ce{NH3} synthesis; $x_{\ce{NH3}}(T, p)$; \ce{SO2} conversion chart | slope $= -\Delta_r H^\circ/R$ (within the JANAF variation); $Q(x_{\text{eq}}) = K^\circ$; $x$ increases with $p$, decreases with $T$ |
| `reactors.py` | 5 | conversion versus $k\tau$ (tank, cascades, plug flow); heat generation/removal; $1/r$ chart | $X_{\text{CSTR}} = k\tau/(1 + k\tau)$; $X_{\text{PFR}} = 1 - \mathrm e^{-k\tau}$; cascade → PFR as $N$ grows; three steady states for the chosen parameters |
| `ellingham.py` | 6 | $\Delta_r G^\circ(T)$ per mol \ce{O2} of the oxides and carbon lines; Boudouard composition | each line matches JANAF $\Delta_f G^\circ$ at its tabulated temperatures; slope change at the Zn and Mg boiling points; ZnO/C–CO crossing temperature pinned; Boudouard $Q = K^\circ$ |
| `liquid-vapour.py` | 7 | benzene–toluene isobaric and isothermal diagrams; Margules azeotrope; steam distillation; plate staircase | bubble = dew at the pure boiling points (Antoine); lever rule mass balance; azeotrope where $x = y$ at the extremum; $p_1^* + p_2^* = p$ at the steam temperature; staircase count ≥ Fenske $N_{\min}$ |
| `solid-liquid.py` | 8 | Cu–Ni lens (ideal), benzene–naphthalene and Bi–Sn eutectics (Schröder–van Laar), cooling curves | liquidus meets the pure melting points; eutectic where both liquidus are equal; lever rule; plateau duration ∝ eutectic fraction |
| `cell-thermodynamics.py` | 9 | $E^\circ(T)$ of the \ce{H2}/\ce{O2} cell; efficiency versus $T$ | $E^\circ$(298) = 1.23 V from $\Delta_f G^\circ$; $\dd E^\circ/\dd T = \Delta_r S^\circ/(2F)$; efficiency $= \Delta_r G^\circ/\Delta_r H^\circ$ |
| `ie-curves.py` | 10–12 | steady-state waves, slow-system model, water window, mixed potential, electrolysis, Evans diagram, passivation model | plateaus $= nFADc/\delta$ (∝ $c$); $i = 0$ at the Nernst potential; $E_{1/2} = E^\circ$ for equal $D$; mixed potential where $i_a = -i_c$; no Butler–Volmer/Tafel: the rising branches are Nernst + diffusion or the stated model |
| `atomic-orbitals.py` | 13 | radial functions and distributions $n \leq 3$; dot densities; Slater $Z^*$ and radii | $\int P\,\dd r = 1$; $r_{\max}$(1s) $= a_0$, (2p) $= 4a_0$, (3d) $= 9a_0$; 2s node at $2a_0$; $P(r > 2a_0) = 13\mathrm e^{-4}$; Slater $Z^*$ of C 2p = 3.25, of K 4s = 2.20 |
| `two-level.py` | 14, 17 | exact and perturbative energies of two interacting orbitals | eigenvalues of the 2 × 2 matrix equal the closed form; perturbative error → 0 as $\beta/\Delta \to 0$ |
| `diatomics.py` | 14 | bond order against length and dissociation energy (ledger points) | bond orders from the filled diagrams (O₂ 2, O₂⁺ 2.5, N₂ 3…); length decreases with bond order within the \ce{O2^{n}} series |
| `huckel.py` | 16, 17, 26 | eigenvalues, coefficients, $E_\pi$, charges, bond indices of ethene, allyl, butadiene, hexatriene, benzene, cyclobutadiene, C₅H₅⁻, C₇H₇⁺; model substituted diene, dienophile, propenal | allyl $\alpha \pm \sqrt2\beta$, $\alpha$; butadiene $\alpha \pm 1.618\beta$, $\alpha \pm 0.618\beta$; benzene $\alpha \pm 2\beta$, $\alpha \pm \beta$ (×2); polyene closed form for $n$ = 2…10; ring closed form; trace $= n\alpha$; charges 1 in alternant neutrals; butadiene bond indices 0.894 and 0.447; benzene delocalisation $2\beta$ |
| `ligand-field.py` | 19 | CFSE versus $d^n$, high and low spin | barycentre: weighted sum of shifts zero; CFSE $d^3$ = $-1.2\Delta_o$, $d^6$ low spin = $-2.4\Delta_o + 2P$… |
| `aromatic-profile.py` | 22 | model energy profiles (substitution versus addition) | maxima and minima where stated; Wheland intermediate a local minimum |
| `polymer-distributions.py` | 29 | Flory number and mass distributions; Carothers; Poisson | $\sum$ fractions = 1; $\bar X_n = 1/(1 - p)$; $Đ = 1 + p$; Poisson $Đ \to 1$ |
| `amino-acid-charge.py` | 30 | net charge versus pH; species fractions of glycine | charge 0 at pI $= (\mathrm pK_1 + \mathrm pK_2)/2$; fractions sum to 1; charge → +1/−1 at the extremes |
| `chromatogram.py` | 31 | Gaussian peaks at given $R_s$; van Deemter; the problem's chromatogram | $R_s$ recomputed from the generated peaks; $u_{\text{opt}} = \sqrt{B/C}$, $H_{\min} = A + 2\sqrt{BC}$; $N = 16(t_R/w)^2$ |
| `mass-spectra.py` | 32 | isotope clusters by convolution; synthetic EI spectra at ledger peaks | Cl 100 : 32, Br 100 : 97, Cl₂ 9 : 6 : 1 (from the ledger abundances); cluster sums 1; $M+1$ ≈ 1.1 % per C |
| `nmr-spectra.py` | 33 | ¹³C decoupled + DEPT traces; first-order ¹H multiplets for the unknowns | one line per kind of carbon; DEPT-135 sign = (−1 for CH₂); ¹H integrals ∝ proton counts; multiplet line counts $n + 1$ |
| `regression.py` | 34 | least-squares fit, residuals, Student densities and coefficients, standard addition | slope/intercept equal `numpy.polyfit`; $t_{0.975}$ = 12.706 (1), 2.776 (4), 2.228 (10) to 3 decimals; standard-addition intercept recovered |
| `vacuum-boiling.py` | 35 | boiling point versus pressure | the curve passes through $T_b$ at 1.013 bar; slope from $\Delta_{\text{vap}}H$ |

25 scripts (24 figures + helper). No script prints Python in the book.

### Image plan

- **AI batches** (one per part of the book, ~27 images; `tools/ai_images.py
  --book 3`, detached, grey stubs meanwhile): batch T (thermodynamics, ch1–8:
  camping stove, cold pack, salt spreader, ammonia plant at night, stirred-tank
  plant, blast furnace tapping, copper pot stills, soldering a circuit board —
  8); batch E (electrochemistry, ch9–12: fuel-cell bus, electroplating line,
  aluminium potroom, rusty bridge — 4); batch O (ch20: pilot plant — 1);
  batch R (organic, ch21–30: epoxy glue, indigo dye vat, fish stall with
  lemons, olive-oil soap bars, perfumer's bench, vitamin-capsule line (optional),
  plastic pellets/fibre spinning, eggs frying — 7–8); batch A (ch31–35:
  analytical lab with chromatographs, fireworks, water-testing lab, synthesis
  lab — 4). Every image reviewed for chemistry (flame colours: butane blue;
  firework colours against the ledger lines; molten iron; protective gear).
- **Photographs** (licence re-verified through the Commons API before
  insertion; credits in `images/book3/CREDITS.md` and the Image Credits page).
  Found 2026-10-02 (title, licence): Portrait of Professor of Chemistry German
  Ivanovich Hess.jpg (CC BY-SA 4.0); Marcellin Berthelot.jpg (PD); Josiah
  Willard Gibbs -from MMS-.jpg (PD); François-Marie Raoult.jpg (PD); Fritz
  Haber.png (PD); Carl Bosch.jpg (PD); La Sorbonne. M. le professeur H. Le
  Chatelier, membre de l'Institut.jpg (CC BY-SA 4.0); Jacobus van 't Hoff by
  Perscheid 1904.jpg (PD); M Faraday Th Phillips oil 1842.jpg (PD);
  VoltaBattery.JPG (CC BY-SA 3.0); Charles Martin Hall 1880s.jpg (PD);
  PaulHeroult.jpg (PD); Statue of Liberty 7.jpg (PD); Erwin Schrödinger
  (1933).jpg (PD); Ruby cristal.jpg (PD); Copper sulfate.jpg (CC BY-SA 3.0);
  Charles Friedel.jpg (PD); Ludwig Claisen.jpg (CC BY-SA 4.0); Wallace
  Carothers, in the lab.jpg (PD); Hermann Emil Fischer c1895.jpg (PD); Mikhail
  Tsvet.jpg (PD); Francis William Aston.jpg (PD); Kirchhoff Bunsen
  Roscoe.jpg (PD); William Sealy Gosset.jpg (PD). To find: a blast furnace,
  thermite welding, refinery columns, Pb–Sn eutectic micrograph, sacrificial
  anodes or galvanised spangle, liquid oxygen in a magnet, Mulliken or Hund,
  Kekulé, Werner, a rack of transition-metal salt solutions, emerald, Diels
  and Alder, Heyrovský, Suzuki/Heck/Negishi, J. M. Crafts, Borodin, Chevreul,
  Robinson, Corey, Wittig, H. C. Brown, an NMR magnet without a brand (≈ 25
  candidates, ~15 expected to be free). Commons answers HTTP 429 to quick
  bursts: one query per second.

### Source plan

Ledger-heavy chapters: 1, 2, 4, 6 (thermochemistry: CODATA-KEY and JANAF,
~150 rows), 7–8 (Antoine, fusion data, NIST solder invariants, ~40), 9, 11
(Gibbs energies reused from Book 2, IAI, USGS, ~20), 14 (diatomic constants,
~30), 16 (hydrogenation enthalpies, ~5), 23, 25, 30 ($\mathrm pK_a$, ~20),
32–33 (isotopes, exact masses, MS peaks, ¹³C shifts, ~80), GHS rows across
ch17–35 (~60). Estimate **~450 rows**. Most are fetched directly by script
(JANAF text tables, CODATA HTML, WebBook, NIST ASD, NMRShiftDB, PubChem
PUG-View) — not web searches. **Web-search estimate: ~250** (finding the
at-risk sources: ethanol–water azeotrope, NaCl–water eutectic, ligand-field
bands, photoelectron band energies, enol contents, polymer glass transitions,
the IAI figure, kinetics of ester saponification), within the ~600 per book.
At-risk values are EXCLUDED rather than typed if no primary page is found.
