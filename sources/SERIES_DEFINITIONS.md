# Series definition map — One Chemistry Book

Which book and chapter **owns** each defined term, i.e. carries its
`\emph{term}\index{term}` pair inside a `definition`. Owned by the main
session; book writers read it and never edit it (they report).

Term links are generated **per book**, so a book can only link a term it
defines itself. Hence the two rules:

1. **Book 1** follows `OUTLINE.md`'s Book 1 ownership map: one owner chapter
   per notion inside the volume, never two. Later chapters recall it
   (`recall` box) and use the word without a new `\emph{}\index{}` pair.
2. **Books 2–4 (Years 1–3)**: each notion has exactly **one owner across the
   three university books** (the Years 1–3 table of `OUTLINE.md`). A
   university book may **re-found** a notion that Book 1 owns — define it
   again, rigorously, in the chapter the outline names ("Re-founds (Book 1)"
   column) — because Book 1's definitions do not link inside Book 2. It never
   defines a notion owned by another university book: it uses the owner's
   word with a prose pointer ("defined in the Year 1 volume", or, for a later
   book, "treated in the Year 3 volume"), never a `\cref`.
3. A term not in the outline's map goes to the **earliest chapter of the
   lowest-numbered university book** that needs it; a tie on a contested term
   is settled at a sync by the main session, and the ruling is written below.

Before writing each chapter's definitions, a writer checks the harvest of the
books already written (multi-line):

```sh
perl -0777 -ne 'while(/\\emph\{([^}]*)\}\s*\\index\{([^}]*)\}/g){($t=$2)=~s/\s+/ /g; print "$ARGV\t$t\n"}' parts/bachelor-*/[0-9]*.tex
```

## Seed: the outline's university ownership (2026-10-02)

| Notion | Owner | Re-founds (Book 1) |
|---|---|---|
| quantum numbers, electron configurations | B2 ch. 1 `quantum-numbers` | g10 `electron-shells` |
| electronegativity scales, periodic trends, polarisability | B2 ch. 2 `periodicity` | g11 `polarity-and-cohesion` (electronegativity) |
| formal charge, resonance, VSEPR, dipole moment | B2 ch. 3 `lewis-resonance-vsepr` | g10 `lewis-and-shape` |
| Keesom/Debye/London forces, solvent descriptors | B2 ch. 4 `intermolecular-forces-solvents` | g11 `polarity-and-cohesion`, `dissolution` |
| lattice, unit cell, compactness, interstitial site | B2 ch. 5 `crystals-metals` | — |
| ionic/covalent/molecular crystal types, radius ratio | B2 ch. 6 `crystals-ionic-covalent` | — |
| extent, activity, Q, K°, intensive/extensive variables | B2 ch. 7 `extent-q-and-k` | g10 `reaction-progress-table`, g12 `equilibrium` |
| rate, order, half-life, Arrhenius law | B2 ch. 8 `rate-laws` | g12 `reaction-rates` |
| elementary step, molecularity, steady-state approximation | B2 ch. 9 `elementary-steps` | g12 `curly-arrows`, `catalysis` |
| predominant reaction, levelling, polyprotic acids | B2 ch. 10 `predominant-reaction` | g12 `ka-and-pka`, `buffers-predominance` |
| solubility product, existence domain | B2 ch. 11 `precipitation` | g6 `solutions-and-solubility` (solubility) |
| complex, ligand (first meaning), formation/dissociation constants | B2 ch. 12 `complexation` | — |
| electrode potential, Nernst equation | B2 ch. 13 `nernst` | g11 `redox` |
| E–pH diagram, disproportionation | B2 ch. 14 `e-ph-diagrams` | — |
| titration types, equivalence (rigorous) | B2 ch. 15 `titration-methods` | g11 `titration`, g12 `ph-conductivity-titrations` |
| CIP rules, R/S, conformations, optical activity | B2 ch. 16 `stereochemistry-in-depth` | g12 `stereochemistry` |
| coupling constant, multiplet, conjugation (UV–vis) | B2 ch. 17 `structure-spectroscopy` | g11 `infrared`, g12 `proton-nmr` |
| inductive/mesomeric effects, nucleophile, electrophile, leaving group | B2 ch. 18 `electronic-effects` | g12 `curly-arrows` |
| SN1, SN2 | B2 ch. 19 `nucleophilic-substitution` | — |
| E1, E2, Zaitsev | B2 ch. 20 `elimination` | — |
| Grignard reagent | B2 ch. 21 `organomagnesium` | — |
| Williamson synthesis, sulfonate ester | B2 ch. 22 `alcohol-activation` | — |
| acetal, hemiacetal, protecting group | B2 ch. 23 `acetals-protection` | g12 `synthesis-strategy` (protecting group) |
| oxidation level of carbon, hydride reduction | B2 ch. 24 `organic-redox` | — |
| electrophilic addition, Markovnikov rule, halonium | B2 ch. 25 `electrophilic-additions` | — |
| hydride (inorganic), s-block terms | B2 ch. 26 `s-block` | — |
| GHS hazard terms, H/P statements, type A/B uncertainty | B2 ch. 29 `lab-techniques-1` | — |
| enthalpy of reaction, Hess's law, standard state | B3 ch. 1 `reaction-enthalpy` | g11 `reaction-energy` |
| entropy of reaction, ΔrG, evolution criterion | B3 ch. 2 `reaction-free-energy` | — |
| chemical potential, partial molar quantity, Raoult, Henry | B3 ch. 3 `chemical-potential` | — |
| van 't Hoff, variance | B3 ch. 4 `equilibrium-shifts` | — |
| ΔrG = −nFE, concentration cell | B3 ch. 9 `cell-thermodynamics` | g12 `cells-and-electrolysis` |
| i–E curve, overpotential, fast/slow system | B3 ch. 10 `current-potential-curves` | — |
| atomic orbital, radial/angular part, effective nuclear charge | B3 ch. 13 `atomic-orbitals` | — |
| LCAO, bonding/antibonding MO, bond order | B3 ch. 14 `diatomic-mos` | — |
| fragment orbital, symmetry-adapted combination | B3 ch. 15 `fragment-orbitals` | — |
| Hückel method, delocalisation energy, aromaticity rule | B3 ch. 16 `huckel` | — |
| HOMO, LUMO, frontier orbitals, Diels–Alder (FMO view) | B3 ch. 17 `frontier-orbitals` | — |
| denticity, coordination number, 18-electron rule | B3 ch. 18 `coordination-complexes` | — |
| ligand field, spectrochemical series, high/low spin | B3 ch. 19 `ligand-field` | — |
| oxidative addition, reductive elimination, migratory insertion | B3 ch. 20 `catalytic-cycles` | g12 `catalysis` |
| hydroboration, epoxidation, oxidative cleavage | B3 ch. 21 `alkene-redox` | — |
| chain-growth/step-growth polymerisation, tacticity, glass transition | B3 ch. 29 `polymer-synthesis` | g12 `polymers` |
| retrosynthesis, disconnection, synthon | B3 ch. 28 `retrosynthesis` | — |
| ¹³C NMR, DEPT, molecular ion | B3 ch. 32–33 `mass-spec-atomic`, `structure-determination` | — |
| Schrödinger equation (formal), model systems | B4 ch. 1 `quantum-model-systems` | — |
| point group, symmetry operation, character table | B4 ch. 4 `point-groups` | — |
| space group, Bragg's law, reciprocal lattice | B4 ch. 9 `x-ray-diffraction` | — |
| partition function, Boltzmann distribution | B4 ch. 10 `partition-functions` | — |
| transition-state theory, Eyring equation | B4 ch. 12 `rate-theories` | — |
| Michaelis–Menten, chain reaction | B4 ch. 13 `complex-kinetics` | — |
| Butler–Volmer, Tafel, cyclic voltammetry | B4 ch. 15 `electrode-kinetics` | — |
| Woodward–Hoffmann rules, pericyclic reaction | B4 ch. 26 `pericyclic` | — |
| E-factor, life-cycle assessment (green metrics) | B4 ch. 31 `green-industrial` | g12 `synthesis-strategy` (atom economy) |

The rows are the outline's, condensed; the outline is authoritative where they
differ. Each sync below adds the terms the Phase A maps claim.

## Rulings at the syncs

(Written by the main session; binding.)

### Sync S1 — Book 2 (2026-10-02)

Book 2's map (`sources/book2/DEFINITIONS.md`, ~330 rows) is granted as
claimed, with these rulings. The earliest-need rule decides every contested
term: a Year-1 chapter that cannot be written without a word owns it, and the
later book uses it with a prose pointer ("defined in the Year 1 volume").

**Re-founds added to the map (Book 1 owns them in Book 1; Book 2 re-founds):**
*yield* (B2 ch7), *molar concentration* (B2 ch7), *carbon class* —
primary/secondary/tertiary (B2 ch18).

**Contested terms, ruled for Book 2** (the seed row's later owner keeps only
what is listed after the dash):
- *standard state* → B2 ch7 (K° needs it). — B3 ch1 uses it; owns *standard
  enthalpy of formation*, *Hess's law*.
- *coordination number* → B2 ch5, general meaning (number of nearest
  neighbours). — B3 ch18 applies it to complexes without redefining; owns
  *denticity*, *18-electron rule*.
- *atomic orbital* → B2 ch1, as the one-electron state labelled by
  (n, l, m_l), shapes shown qualitatively. — B3 ch13 owns *wavefunction*,
  *radial part*, *angular part*, *radial distribution*, *nodal surface*.
- *screening* and *effective nuclear charge* → B2 ch2, qualitative. — B3 ch13
  owns *Slater's rules* (the computation).
- *Lewis acid*, *Lewis base*, *dative bond* → B2 ch3.
- *σ bond*, *π bond*, *hybridisation* → B2 ch3, descriptive. — B3 ch14 owns
  the MO terms (*σ orbital*, *π orbital*, *bonding/antibonding orbital*).
- *transition state*, *Hammond postulate*, *kinetic control*,
  *thermodynamic control* → B2 ch9. — B4 ch12 owns *activated complex*,
  *transition-state theory*, *Eyring equation*.
- *homogeneous catalysis*, *heterogeneous catalysis* → B2 ch9 (re-founds
  Book 1 g12). — B4 ch16 owns *adsorption*, *physisorption*, *chemisorption*.
- *polydentate ligand*, *chelate* → B2 ch12. — B3 ch18 owns *denticity*.
- *anode*, *cathode*, *half-cell*, *salt bridge*, *cell voltage* → B2 ch13
  (re-founds Book 1 g12).
- *immunity domain*, *corrosion domain*, *passivation domain* → B2 ch14
  (thermodynamic). — B3 ch12 owns *passivation* (the phenomenon), *differential
  corrosion*, *mixed potential*.
- *Fischer projection* → B2 ch16. *partition coefficient* → B2 ch29.
- *micelle* stays with B4 ch17 (*colloids*): Book 2 draws and names it in
  ch4, no definition.
- Low-risk claims granted: *stereospecific* (ch19), *regioselective*,
  *stereoselective* (ch20), *chemoselective* (ch24), *degree of
  unsaturation* (ch17), *normalised deviation* (ch29), *carbocation
  rearrangement* (ch25), *organometallic compound* (ch21), *basic / acidic /
  amphoteric oxide* (ch26).

**Harvester rule (all books, from Book 2's report).** `tools/termlink/harvest.py`
turns any `\emph{}\index{}` pair — and any multi-word `\index{}` in a
statement — into a link target, wherever it sits. So: `\index{}` appears
**only** beside the `\emph{}` of a term the chapter defines and owns, inside a
`definition`. Never index a notion your book does not own, and never put an
`\index` in a theorem, remark or example.

### Sync S1b — Book 1 (2026-10-02)

Book 1's in-volume map (`sources/book1/DEFINITIONS.md`) is granted with its
proposals C1–C15 (see the batch file, "S1b"). Inside Book 1, Book 2's
re-founded terms (multiplet, Cram representation, conformation, elementary
step, intermediate, donor/acceptor site, protecting group) are Book 1's to
define as well, at the Book 1 level: linking is per book. *Micelle* is
defined in Book 1 (g11) and, at the university level, by Book 4 only.

### Sync S2 — Book 3 (2026-10-02)

Book 3's map (`sources/book3/DEFINITIONS.md`, 421 terms, checked by script
against the real Book 1 and Book 2 harvests) is granted as claimed, with:

**Re-founds added** (Book 1 owners, Book 2 did not define them):
*exothermic*/*endothermic* and *mean bond enthalpy*/*bond dissociation
enthalpy* (ch1); *Faraday constant* (ch9); *accumulator*, *electrolysis*
(ch11); *stationary phase* (ch31); *calibration curve* (ch34); *polymer*,
*monomer*, *repeat unit*, *degree of polymerisation* (ch29).

**Contested terms, ruled for Book 3 by earliest need.** In each, Book 4
keeps what follows the dash and recalls the rest in prose:
- *retention factor* k of a column (ch31). A remark says that the Year 1
  volume's TLC R_f is the *retardation factor* of current nomenclature;
  Book 2's term stands in Book 2. — No Book 4 claim.
- *back-donation*, *π-donor ligand*, *π-acceptor ligand* (ch19). — Book 4
  ch20 does **not** define *back-bonding*; it recalls back-donation and
  develops it (carbonyls, phosphines, alkenes, the isolobal analogy).
- *initiation*, *propagation*, *termination*, *radical initiator* (ch29).
  — Book 4 ch13 keeps *chain reaction*, *chain branching*, *explosion
  limits*; ch27 keeps the radical-chain terms specific to synthesis.
- *hapticity* (ch18). — Book 4 ch20 recalls it.
- *paramagnetic*, *diamagnetic* (ch14). — Book 4 ch18 keeps *magnetic
  susceptibility*, *spin-only moment*.
- *concerted reaction* (ch17). — Book 4 ch26 keeps *pericyclic reaction*,
  *cycloaddition*, *electrocyclic*, *sigmatropic*.
- *ligand exchange*, as an elementary step (ch20). — Book 4 ch19 keeps
  *dissociative* / *associative mechanism*, *trans effect*.
- *orthogonal protecting groups* (ch28). — Book 4 ch30 keeps *convergent*
  / *linear synthesis*, *protecting-group economy*.
- Low-risk claims granted: *lattice enthalpy* (ch1); *Ellingham
  approximation*, *inversion temperature* (ch2); *ionic strength*,
  *osmotic pressure*, *colligative property* (ch3); *conversion*,
  *selectivity*, *thermal runaway* (ch5); *nucleophilic addition* (ch23);
  *quaternary carbon* (ch33); *photoelectron spectroscopy* (ch15).

**Content split B3 ch20 / B4 ch21:** Book 3 reads hydrogenation,
hydroformylation and cross-coupling as cycles of elementary steps; Book 4
recalls the cycles and treats the industrial processes (conditions,
selectivity, Monsanto/Cativa, metathesis, Ziegler–Natta).

**Named laws (amends the S1 harvester rule).** A named law or rule may carry
its `\emph{name}\index{name}` in the theorem or proposition that states it
(as Book 2 does for the Nernst equation, Markovnikov's rule, Kohlrausch's
law), in its owner chapter only. The rule otherwise stands: no `\index`
outside the statement that owns the term, never in a box, remark or example.

### Sync S3 — Book 4 (2026-10-02)

Book 4's map (`sources/book4/DEFINITIONS.md`, 678 terms in 359 labels,
checked by script against the Book 1 and Book 2 harvests and Book 3's frozen
S2 map: only the five intended re-founds collide) is granted as claimed.

**Re-founds added:** *enzyme* (Book 1 g12 → B4 ch13), *micelle* (g11 → ch17,
already granted), *atom economy*, *green chemistry* (g12 → ch31),
*greenhouse gas* (g8 → ch32).

**Contested-low terms, granted to Book 4** (none is in Book 3's map):
*operator*, *eigenfunction*, *eigenvalue* (ch1; Book 3 uses matrix
eigenvalues without defining them); *electron density* (ch3; Book 3 keeps
*probability density*); *projection operator* (ch5; Book 3 keeps
*symmetry-adapted combination*); *electrochemically reversible /
quasi-reversible / irreversible system* (ch15, with a remark linking them to
Book 3's fast and slow systems); *chelate effect* (ch25); *hard/soft acid*,
HSAB (ch24); *surface tension* (ch17); the partition coefficients of ch32
(beside Book 2's *partition coefficient*); *spectroscopic dissociation
energy* (ch6, distinct from Book 3's bond dissociation enthalpy).
*Back-bonding* is **not** defined (S2): Book 4 owns *synergic bonding*, the
*Dewar–Chatt–Duncanson model*, *isolobal analogy* and recalls back-donation.

**Homographs kept apart by phrase** (never index the bare word): order /
class of a point group, reduction formula, transmission probability vs
coefficient, chemical vs NMR relaxation time, fluorescence quencher,
kinetically inert complex, kinetic resolution vs resolution of a racemate
(Kagan's s unindexed: Book 3 owns *selectivity factor*), oxide glass.

