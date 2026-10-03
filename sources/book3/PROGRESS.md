# Book 3 (University Chemistry, Year 2) — progress

Resume file: a fresh agent must be able to continue the book from this file
alone, with `sources/BATCH_BOOKS_1-4.md` (binding rules, read first, including
every "Sync decisions" entry), `BRIEFS.md` (per-chapter plan, figdata table,
image and source plans) and `DEFINITIONS.md` (term list, 421 rows) beside it.

## State

- **Phase B in progress** (sync S2 received 2026-10-02: map granted, all
  contested terms to Book 3, named laws indexed in their theorem, regression
  derived with partial derivatives, style block "Book 3 sync" added; Book 3
  builds its own pics in a `% Book 3 (shared pics):` block — not yet
  written, needed from ch13). Chapters are written in outline order with
  the full cycle; the table below is the truth.
- Build: `scratchpad/book3/build.sh` (ai_stubs, then latexmk under nice and
  the cgroup cap, then E/U/O counts); figures rendered with
  `scratchpad/book3/fig.sh "<phrase in the caption>" <name> [y H]`.
- Ledger rows are added with `scratchpad/book3/addrows.py <file>` (one row
  per line `id | quantity | value | unit | source`). Data helpers:
  `scratchpad/book3/src/janaf.py` (JANAF index + tables, cached),
  `src/wb.py` (WebBook pages/tables), `src/codata.json` (CODATA key values),
  NBS-82 scan at `scratchpad/book2/data/nbs82.pdf` (PDF page = printed page
  + 8).
- AI batch T (ch1–8, 8 images) landed 2026-10-02 and is in
  `images/book3/ai/`; each image is reviewed when inserted.

## Chapter status

| ch | slug | ledger | text | exos/pb | solutions | figures | build+gates | FIGCHECK |
|---|---|---|---|---|---|---|---|---|
| 1 | reaction-enthalpy | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 2 | reaction-free-energy | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 3 | chemical-potential | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 4 | equilibrium-shifts | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 5 | continuous-reactors | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 6 | ellingham | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 7 | liquid-vapour-diagrams | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 8 | solid-liquid-diagrams | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 9 | cell-thermodynamics | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 10 | current-potential-curves | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 11 | batteries-electrolysis | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 12 | corrosion | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 13 | atomic-orbitals | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 14 | diatomic-mos | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 15 | fragment-orbitals | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 16 | huckel | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 17 | frontier-orbitals | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 18 | coordination-complexes | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 19 | ligand-field | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 20 | catalytic-cycles | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 21 | alkene-redox | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 22 | aromatic-substitution | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 23 | amines | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 24 | acyl-substitution | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 25 | enolates-aldol | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 26 | conjugate-additions | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 27 | wittig | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 28 | retrosynthesis | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 29 | polymer-synthesis | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 30 | biomolecules | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 31 | chromatography | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 32 | mass-spec-atomic | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 33 | structure-determination | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 34 | measurement-statistics | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 35 | lab-techniques-2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

Legend: – not started, ✓ done; build+gates means `latexmk` 0/0/0 and
`bash tools/gates.sh bachelor-2` green after that chapter.

## Page projection

Target ~400 pp. Plan: 35 chapters × (≈ 9.0 body + ≈ 2.0 solutions) ≈ 385 pp
+ ≈ 12 pp frontmatter + ≈ 12 pp index ≈ 409 pp. Book 2 measured 7.6 body +
1.6 solutions per chapter and landed −13.8 %: the briefs therefore carry a
fuller section list, a worked example per substantial statement and more
derivations. Checkpoints after ch. 10, 20, 30 and 35: measured pages per
chapter; a projection more than 15 % under 400 (below 340) means chapters are
being compressed — restore depth before going on.

| checkpoint | chapters done | pages | pp/ch | projection | verdict |
|---|---|---|---|---|---|
| Phase A | 0 | 47 (stubs) | – | ~409 | – |
| ch10 | 10 | 158 | 11.1 added per chapter over the stub | 47 + 35 × 11.1 ≈ 436 | on target (+9 %): keep depth, no padding; ch7 was the longest (13 pp) |
| ch20 | 20 | 243 | 9.8 added per chapter over the stub (ch11–20: 8.5, denser orbital chapters) | 47 + 35 × 9.8 ≈ 390 | on target (−2.5 %); watch the organic part for depth |
| ch30 | 30 | 327 | 9.3 added per chapter over the stub (ch21–30: 8.4, the organic chapters) | 47 + 35 × 9.3 ≈ 374 | on target (−6.5 %, above the 340 floor); the five analytical chapters keep full depth (worked examples, figdata spectra) |
| ch35 | 35 | 373 | 9.3 added per chapter over the stub (ch31–35: 9.2) | measured 373 before term linking | on target (−6.7 % against 400; above the 340 floor) |

## Budgets and counts

- Web searches (WebSearch tool): **0 used** (estimate for the book ~250 of
  the ~600 per-book plan; report point 7). Direct fetches by script, not
  counted as searches: CODATA key values page, NIST-JANAF table O-029, NIST
  Pb–Sn solder page, WebBook, NMRShiftDB (reachability checks, 2026-10-02);
  Commons API: 2 batches (~40 file look-ups, one search batch cut by HTTP
  429).
- AI images: 0 (plan ~27 in 5 batches: T, E, O, R, A — see BRIEFS "Image
  plan"). Photographs: 0 (24 candidate files found, ~25 to find).
- Ledger rows: 0 (plan ~450).
- figdata scripts: 0 (plan 24 + helper; table in BRIEFS).

## Conventions settled in Phase A

- Recall boxes cite Book 2 as "the Year 1 volume" and Book 1 as "the school
  volume" in prose; physics as "from physics"; `\cref{ch:b2:…}` only inside
  this book.
- A term owned by Book 2 or Book 4 is never `\emph{}\index{}`-ed and never
  `\index{}`-ed (S1 harvester rule). Book 2's laws re-derived here (Nernst
  equation in ch9, the law of mass action in ch4, $u = s/\sqrt n$ in ch34) get
  their proof, not a new index entry.
- Named laws this book owns: name `\emph{}\index{}`-ed in its own theorem as
  Book 2 did, **pending the sync's ruling** (report point 9).
- Hydroxide `\ce{OH-}`; `\ce{H3O+}` in acid–base; CIP descriptors with
  `\cip{}`; hard/soft defined only as phrases (hard nucleophile …) so the bare
  words stay unlinked; "temperature ramp", never "temperature programme"
  (gate 7).
- Thermodynamic data: CODATA key values first (consensus, with uncertainty),
  JANAF for temperature dependence and species CODATA lacks, NBS-82 only
  through Book 2's `dfg:` rows or for missing aqueous species; every printed
  $\Delta_r X^\circ$, $K^\circ$, $E^\circ$ comes from `thermo-data.py` (or the
  chapter's script) and is pinned by its test.
- i–E curves: fast systems are Nernst at the surface + linear diffusion
  (derived, no kinetics); slow systems are drawn as a stated model with the
  kinetics `\admitted` (Butler–Volmer and Tafel are Book 4's).
- Hückel numbers (energies, coefficients, charges, indices) come from
  `huckel.py` (numpy eigenvalues), never typed; heteroatom parameters are a
  stated model, not data.
- Exercise and problem data invented for the exercise are labelled as such
  when they look like facts (chromatograms, catalyst loadings, currents);
  values presented as facts about the world have ledger rows.

## Pic block (BUILT 2026-10-03, after ch12) — interfaces requested by the main session

Done: `% Book 3 (shared pics):` appended at the end of `styles/onechemistry.sty`
(omlevel, omcorr, omcorrforbidden, omsymlabel, omphasepos/neg, oms, omlobe,
omp, omdxy/xz/yz/x2y2/z2, omligand/ommetal styles, omoctahedron,
omtetrahedron, omsquareplanar, omtbp, chromcolumn, bubbler, septum,
\setmodiagram defaults); each rendered on a test page
(scratch/book3/pictest), tetrahedron re-projected after the first render.
`\omcycle` not built (optional, unused so far).


`% Book 3 (shared pics):` block appended at the end of the style file
(re-read the file first: the Book 4 sync block was appended after the
Book 3 sync block). Book 4 reuses these pics (pericyclic correlation
diagrams, ligand field, Jablonski diagrams), so the interfaces are fixed:
- `omlevel={<electrons: ud|u|d|empty>}{<length cm>}` (length argument
  required), anchors `(-l)`, `(-r)`; styles `omcorr` (dashed correlation
  line), `omcorrforbidden` (dashed, a second look), `omsymlabel` (small S/A
  labels at level ends);
- `omp={<signed coefficient c>}{<angle>}`: lobe size ∝ |c|, phase colour by
  the sign of c, the angle orients the lobe axis (Hückel drawings);
  `omlobe`, `oms` as planned;
- d set: `omdxy`, `omdxz`, `omdyz`, `omdx2y2`, `omdz2`;
- `omoctahedron`, `omtetrahedron`, `omsquareplanar`, `omtbp`;
  `chromcolumn`, `bubbler`, `septum`; `\setmodiagram` defaults;
  `\omcycle` optional. Grep every name before defining; check each on a
  rendered page; document in the block's comment.

## Open items (for the sync, Phase A report)

- Rulings asked: contested terms (retention factor $k$, back-donation /
  π-acceptor, initiation/propagation/termination, hapticity, paramagnetic/
  diamagnetic, concerted reaction, ligand exchange, orthogonal protecting
  groups); re-founds outside the map (Faraday constant, accumulator,
  electrolysis, stationary phase, calibration curve, lattice enthalpy);
  intra-book move of *mixed potential* (ch12 → ch11); named laws harvested
  from their theorems; linear regression in Year 2 (outline) versus Year 3
  (math guard).
- Style-file requests (report point 4): MO-diagram defaults, level pic,
  orbital-lobe pics, coordination-geometry pics, plot styles (phase diagrams,
  i–E, Ellingham, chromatogram, mass spectrum, NMR/IR), catalytic-cycle
  layout, retrosynthetic arrow, chromatography-column and bubbler pics.
- Sources at risk (EXCLUDED if no primary page): ethanol–water azeotrope,
  NaCl–water eutectic, ligand-field absorption bands, photoelectron band
  energies of \ce{H2O}/\ce{CH4}/\ce{NH3}, enol contents, polymer glass
  transitions, hydrogen overpotentials on metals, toluene nitration isomer
  ratios, ester saponification rate constant, ethene torsion barrier.

## Report items collected during Phase B (for the Phase D report)

- AI image to regenerate: b2-22-indigo-vat shows the colour change inverted;
  regenerate as b2-22-indigo-vat-2 in batch A and switch the chapter to it.

- `\raggedbottom` added to the Book 3 entry file only (2026-10-03, ch7):
  in a twoside book an `omfigure` that does not fit stretched the glue above
  it into third-of-a-page gaps; physics sets it series-wide in its sty.
  Suggest the main session decide series-wide in `onechemistry.sty`.
- Ethanol–water azeotrope: sourced only as "95 % by weight" (HSDB via
  PubChem, `azeo:ethanol-water.w`); the temperature is not sourced — the
  diagram is a one-parameter Margules model fitted to the composition and
  labelled "(model)".
- Defects in other books: Book 1 `rho:water` 0.9950 g/cm³ at 25 °C (should be
  ≈ 0.99705); `iso:H2` value is a range.
- WebSearch used: 1 (ethanol–water azeotrope, ch7).

## Traps (Book 3, so far)

- `tools/ai_images.py` writes to `images/book<N>/ai/` relative to the cwd:
  launch it from the repo root (batch E landed in the scratch dir and was
  moved, PROMPTS.md merged).
- chemfig: branches go after the atom (`C(-[2]X)`, never `(-X)C`); a 3-ring
  closed with `?` hooks strikes through a label: use `*3(...)` with a base
  angle, e.g. `\chemfig{[:-60]CH(-[:210]R)*3(-CH(-[:-30]R)-O-)}`.
- mhchem cannot read primes (Ar', L'): write such species in `$\mathrm{...}$`.
- `\admitted` is a whole proof environment: never call it inside a proof.
- `\t` and `\c` are text accents: never use them as `\foreach` variables.
- An Ellingham-type chart with a dozen lines: label at the right end with
  leaders (`clip mode=individual` keeps the nodes outside the axis).

- Commons API returns HTTP 429 to a quick burst of `list=search` queries:
  pace at one query per second, batch titles (≤ 40 per `titles=` call).
- The CODATA key-values page is ISO-8859-1 HTML with "±" uncertainties in
  separate cells: parse by row, keep the uncertainty in the ledger row and
  print no more digits than it allows.
- The NIST solder pages (Pb–Sn …) give the invariant points in an HTML table
  inside a large page; read the table, not the calculated-diagram image.
- From Book 2's PROGRESS (still valid): chemfig has no `\lewis`; mhchem cannot
  read primes; generic species go in math, not `\ce`; `\foreach` in a pgfplots
  axis does not expand `\x` in `axis cs`; a `% ledger:` line holds ids then
  `(` free text; `\label{fig:…}` inside `omfigure` refers to the section;
  never name a macro `\par`; 3D cells: check projected geometry (view 60/100,
  `omcubeo`); count chemfig ring bonds; `\par\vspace{6pt}` after
  `\schemestop`; rounding from rounded intermediates is the commonest
  solution slip; take the consensus value, never more digits than the
  source's uncertainty.

- (ch26-35) chemfig ring closure: a hook `?[a]` written after a branch bonds the
  branch atom, not the ring atom (guanine's N1-H drew H-C6): put the hook first,
  `N?[a](-[:180]H)`. Nested rings attach on the NEXT bond: check with lettered atoms.
- `\pgfplotsset{...}` inside one tikzpicture is local to it: hoist a shared style
  above the pictures. The `groupplots` library and `booktabs` are not loaded.
- `\chemabove{P}{+}` in the middle of a bond chain draws a hyphen bond: write charges
  as superscripts (`Ph_3P^{+}`).
- PubChem GHS: the PUBCHEM-GHSSUM rows use the UNION of pictograms over all GHS
  classification records (checked against Book 2 rows); several inorganic CIDs
  (CuI, MeLi, NaH, PCC) return 404 on the GHS heading: no row, no pictogram claim.
- WebSearch total for Book 3: 6 (ethanol-water azeotrope, NaCl eutectic, O2+ bond
  length, IAI statistics, WHO lead fact sheet, one more in Phase B).

## Phase C (2026-10-03, after ch35)

- Term links: `--unwrap --apply` then `--apply`; 1,733 links (def 1,709, thm 21, prop 3),
  451 linkable terms; plain dry run prints `links to insert: 0`. Curation in
  `tools/term_config/book3_en.py`: STOP for bare "fragment(s)" (ch15 sense vs ozonolysis,
  synthon and mass-spectrum fragments); EXTRA_PROTECT for statistical variance,
  propagation of uncertainty, Grignard initiation, chromatographic vs reactor selectivity,
  TLC R_f vs column k, spectral vs chromatographic resolution, chemfig \arrow labels.
- Full figure re-check: 6-up contact sheets of all 373 pages viewed (no overlap, overflow
  or misplaced figure found beyond those fixed per chapter in FIGCHECK.md).
- Solutions re-read with every number recomputed (ch1-35): 6 slips fixed (ch1 Q11 and
  Q13 rounding, ch2 ex5, ch4 ex5, ch6 problem intercept chain -226.4 -> -226.8 with
  T 1216 -> 1215 K, ch13 ex5 radius 46 -> 47 pm). Named numbers unchanged.
- Final: build 0/0/0, 373 pp; gates OK; ledger OK (1,908 rows); calibration OK;
  `make test Y=bachelor-2` 129 passed; `make figdata Y=bachelor-2` leaves no diff.
