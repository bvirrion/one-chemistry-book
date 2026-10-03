# Book 1 — progress (resume file)

**A fresh agent resumes Book 1 from this file alone.** Read first:
`sources/BATCH_BOOKS_1-4.md` (binding rules, incl. the "Sync decisions"
section written after Phase A), then `BRIEFS.md` and `DEFINITIONS.md` in this
directory, then the three pilots. Never commit; git is read-only; build only
`one_chemistry_book_1_school.tex` (`nice -n 10 latexmk …`, `-g` after adding a
chapter file); never bare `make`.

## State

- **Phase:** D (report) delivered 2026-10-02; only open item: the 17 g12 AI pictures. All 49
  chapters written, built and gated, FIGCHECK lines for every figure. Term
  links: `link_defined_terms.py --book 1 --unwrap --apply` then `--apply`
  (5,776 links, 98 files); idempotence dry run prints `links to insert: 0`.
  Config `tools/term_config/book1_en.py`: STOP list of everyday homographs
  (solution, material, object, product, family, period, addition,
  substitution, capacity), EXTRA_PROTECT for group-before-a-number,
  hydration of ethene, four hyphenated compounds, `\irpanel` keys (a link in
  its csname key killed the build) and `\setchemfig` keys ("atom sep" was
  linked: chemfig ignored the key and two overfull boxes appeared).
- **Build:** full Book 1, 434 pp, 0 errors / 0 undefined / 0 overfull (after the FIGCHECK coverage pass: every non-stub figure has its own row).
  17 AI images (all g12) still grey placeholders: batch g12 has been
  sleeping on the Codex usage limit since ~14:00 (log `ai/log-g12.txt`);
  when they land: review each, FIGCHECK line, rebuild.
- **Web searches / fetches used by this agent:** 0 web searches; 4 Commons
  API calls (photo-candidate licences, no e-mail in the User-Agent). Budget
  for the book ~600 (shared 5,000).

## Chapter status (49)

Status values: `todo` · `ledger` (rows in) · `text` · `exos` · `sols` ·
`figs` (FIGCHECK lines) · `built` (0/0/0 + gates green) · `pilot`.

| # | year | file | status | pp (target) | notes |
|---|---|---|---|---|---|
| 1 | grade-1 | 01-materials-around-us | built | 7 | |
| 2 | grade-2 | 01-mixing-and-dissolving | pilot | 7 | approved; 6 AI |
| 3 | grade-3 | 01-separating-mixtures | built | 7 | |
| 4 | grade-4 | 01-air-a-mixture-of-gases | built | 7 | ledger rows air:* exist |
| 5 | grade-4 | 02-what-a-fire-needs | built | 7 | |
| 6 | grade-5 | 01-irreversible-changes | built | 7 | |
| 7 | grade-5 | 02-raw-materials-and-recycling | built | 7 | |
| 8 | grade-6 | 01-pure-substances-and-mixtures | built | 9 | |
| 9 | grade-6 | 02-solutions-and-solubility | built | 9 | |
| 10 | grade-7 | 01-identifying-substances | built | 9 | before atoms: names only, no formulas |
| 11 | grade-7 | 02-atoms-and-molecules | pilot | 9 | approved; Dalton photos |
| 12 | grade-7 | 03-chemical-reactions | built | 9 | |
| 13 | grade-8 | 01-balanced-equations | built | 9 | |
| 14 | grade-8 | 02-combustion-and-fuels | built | 9 | figdata co2-record |
| 15 | grade-8 | 03-plastics | built | 9 | densities: source or EXCLUDE |
| 16 | grade-9 | 01-inside-the-atom | built | 9 | |
| 17 | grade-9 | 02-ions | built | 9 | |
| 18 | grade-9 | 03-acids-bases-ph | built | 9 | pH qualitative (no log) |
| 19 | grade-9 | 04-metals-acids-corrosion | built | 9 | no "oxidation" term |
| 20 | grade-9 | 05-periodic-table-first-look | built | 9 | periodic-table macro |
| 21 | grade-9 | 06-elements-universe-earth | built | 9 | ledger-heavy (~25) |
| 22 | grade-10 | 01-chemical-species | built | 11 | distillation pics |
| 23 | grade-10 | 02-electron-shells | built | 11 | |
| 24 | grade-10 | 03-lewis-and-shape | built | 11 | |
| 25 | grade-10 | 04-the-mole | built | 11 | |
| 26 | grade-10 | 05-concentration-and-dilution | built | 11 | volflask / pipette pics |
| 27 | grade-10 | 06-reaction-progress-table | built | 11 | |
| 28 | grade-10 | 07-synthesis-yield | built | 11 | reflux / Büchner pics |
| 29 | grade-11 | 01-absorbance | built | 11 | figdata absorbance; no log |
| 30 | grade-11 | 02-polarity-and-cohesion | built | 11 | ledger-heavy (~30) |
| 31 | grade-11 | 03-dissolution | built | 11 | |
| 32 | grade-11 | 04-organic-skeletons | built | 11 | |
| 33 | grade-11 | 05-functional-groups | built | 11 | |
| 34 | grade-11 | 06-infrared | built | 11 | figdata infrared |
| 35 | grade-11 | 07-redox | pilot | 11 | approved; 3 AI |
| 36 | grade-11 | 08-titration | built | 11 | MnO4-/Fe2+ (pilot promise) |
| 37 | grade-11 | 09-reaction-energy | built | 11 | ledger-heavy |
| 38 | grade-12 | 01-proton-nmr | built | 11 | figdata proton-nmr |
| 39 | grade-12 | 02-stereochemistry | built | 11 | |
| 40 | grade-12 | 03-curly-arrows | built | 11 | chemmove |
| 41 | grade-12 | 04-reaction-rates | built | 11 | figdata reaction-rates |
| 42 | grade-12 | 05-catalysis | built | 11 | figdata catalysis |
| 43 | grade-12 | 06-equilibrium | built | 11 | figdata equilibrium |
| 44 | grade-12 | 07-ka-and-pka | built | 11 | |
| 45 | grade-12 | 08-buffers-predominance | built | 11 | figdata buffers-predominance |
| 46 | grade-12 | 09-ph-conductivity-titrations | built | 11 | figdata; λ° source risk |
| 47 | grade-12 | 10-cells-and-electrolysis | built | 11 | circuits |
| 48 | grade-12 | 11-synthesis-strategy | built | 11 | |
| 49 | grade-12 | 12-polymers | built | 11 | |

## Page projection (Phase A)

| band | chapters | pp each (incl. solutions) | pp |
|---|---|---|---|
| grades 1–5 | 7 (1 pilot) | ~7 | 49 |
| grades 6–9 | 14 (1 pilot) | ~9 | 126 |
| grades 10–12 | 28 (1 pilot) | ~11 | 308 |
| front matter, part pages, index | — | — | ~30 |
| **total** | 49 | | **~513** (target ~500) |

Pilot actuals (body + solutions, from the 2026-10-02 build): g2 ≈ 5 + 1 pp,
g7 ≈ 7 + 1.5 pp, g11 redox ≈ 8 + 2.5 pp. Checkpoints: after each grade and
every 10 chapters — a projection more than 15 % under target (< 425 pp)
means chapters are being compressed: restore depth.

## Checkpoints

- **End of grade 5 (2026-10-02):** 7 chapters, body pages 6/6/7/5/6/5/6 + about
  1 p of solutions each = ~6.9 pp/chapter (target 7). On track. Book at 134 pp
  with 42 stubs.

- **End of grade 9 (2026-10-02, 21 chapters):** grades 6–9 bodies 5–7 pp +
  ~1.5 pp solutions ≈ 8 pp/chapter (target 9, 11 % under, within the 15 %
  band; the AI pictures still missing will add a little). Book at 214 pp with
  28 stubs; projection ≈ 214 − ~45 (stubs) + 27 × 11 ≈ 470–500 pp.

- **End of grade 10 (2026-10-02, 28 chapters):** g10 bodies 6–9 pp +
  ~2 pp solutions ≈ 9.6 pp/chapter (target 11, ~13 % under, inside the 15 %
  band; 8 AI pictures still grey placeholders of the right size). Book at
  273 pp with 21 stubs; projection ≈ 273 − ~21 + 21 × 10.5 ≈ 470 pp (~6 %
  under 500). g11–12 should run fuller (more worked examples and figures).

- **End of grade 11 (2026-10-02, 37 chapters):** g11 bodies 7–8 pp + ~2 pp
  solutions ≈ 9.5 pp/chapter (target 11, ~14 % under, inside the band).
  Book at 340 pp with 12 stubs; projection ≈ 340 − 12 + 12 × 10.5 ≈ 455 pp
  (~9 % under 500, above the 425 alarm). Grade 12 runs fuller (figdata
  curves, more worked examples) to pull the total up.

- **End of grade 12 (2026-10-02, 49 chapters, book complete):** g12 bodies
  6–8 pp + 1–5 pp solutions ≈ 9 pp/chapter (target 11). Book at 432 pp
  against ~500 (−14 %, inside the 15 % band, above the 425 alarm), with the
  17 g12 AI pictures as placeholders of the final size. Band actuals:
  grades 1–5 ≈ 7, 6–9 ≈ 8, 10–12 ≈ 9.5 pp/chapter.

## Working tools (scratch, not in the repo)

Scratch dir `/tmp/claude-1000/-home-bvirrion-repositories-one-course/b9a6f211-cc8e-4713-b734-e61467fa9bb3/scratchpad/book1/`:
`build.sh [-g]` (latexmk on the Book 1 entry with grey placeholders on
TEXINPUTS for AI images not generated yet; prints err/undef/overfull/pages),
`page.py -r "caption words"` (finds a figure's page and renders it at 130 dpi
into `render/`), `pages.py` (pages per chapter from the toc), `ghs.py CID…`
(PubChem GHS: pictograms + H codes of the ECHA-aggregated record),
`commons.py "File:…" [dest]` (licence/author via the Commons API, download).
If the scratch is lost, these are 20-line scripts: recreate them.
AI batches: `ai/batch-*.txt`, logs `ai/log-*.txt`.

## Conventions settled (Book 1)

- Labels `<type>:g<N>:<slug>:<leaf>`; definition labels as listed in
  `DEFINITIONS.md` (do not rename: the term list and the linker rely on
  them).
- `\ce` everywhere; balanced; skeletons carry `% ce-unbalanced-ok` on the
  `\ce{` line. State symbols (s), (l), (g) from g8, (aq) from g9.
- H⁺ up to grade 11; `\ce{H3O+}` introduced in grade 12. Hydroxide is
  `\ce{OH-}` series-wide (sync S1b ruling).
- "oxygen" for the gas up to g9; "dioxygen" when the atom/molecule distinction
  matters, from g10 (as the g11 pilot does).
- Atomic weights printed to 0.1 g/mol (`tools/molar_mass.py`, book column);
  0.1-rounded weights make C₃H₈ 44.0 and CO₂ 44.0 g/mol.
- Molar volume of a gas at 20 °C and 1 atm: 24.0 L/mol, computed from
  `const:R` (cite `const:R`, `const:atm`); the "20-volume" peroxide
  convention uses 22.4 L/mol (`const:Vm1`).
- No log/exp before g12; g11 absorbance is defined as the instrument's
  reading (a remark points to the grade 12 meaning).
- Forward references in prose: "a later chapter", "the Year 1 volume",
  "a university volume" — never `\cref` across books.
- Weekend problems: g6–9 Parts I–III, 12 questions; g10–12 Parts I–IV,
  ~20 questions, the last question computing the named number in the brief.
- AI images: one batch per grade, `tools/ai_images.py --book 1 <batch> --work
  <scratch>/ai`, detached; grey stubs until reviewed.
- Photo User-Agent: `OneChemistryBook/0.1 (book-writing agent; contact via
  repository)` — never an e-mail.

## Style-file pics (Book 1 block, appended 2026-10-02)

`% Book 1 (shared pics):` at the end of `styles/onechemistry.sty`: volflask,
pipette, gradcyl, cuvette, condcell, bunsen, gasjar, gasjaropen, deliverytube,
trough, evapdish, utube, balance, stand (interfaces documented in the block's
comment; checked on a rendered test page). Book 2's block (above it) supplies
heatingmantle, stillhead, thermometer, liebig, adapter, buchner, filterflask,
meter, probe, stirrer, saltbridge, electrode, threeneck… — reuse, never
redefine. Gotcha: in `\pic[...]` a pic's own `scale=` needs `transform shape`
too (gate 6b flags it otherwise). xcolor: `black!55!18` is an error (a
percentage must be followed by a colour) — use a named colour in loops.

## Open items

- Sync rulings on the contested terms C1–C16 (`DEFINITIONS.md`).
- Style-file additions requested at the sync (glassware pics, circuitikz,
  periodic-table macro, extra atom styles) — see the Phase A report; until
  they land, the chapters needing them (g7 ch3 gas jar, g8 ch2 Bunsen, g9
  ch2 circuit, g9 ch3 pH meter, g9 ch5 table, g10 ch1/5/7, g11 ch1, g12
  ch9/10) can be written with the figure stubbed.
- Ledger sources still to find: crust and human-body abundances (g9 ch6),
  limiting molar ionic conductivities (g12 ch9; EXCLUDE path ready), plastic
  densities (g8 ch3; fallback ready), Mendeleev's eka-silicon predictions
  (g9 ch5), average bond energies (g11 ch9; OpenStax Chemistry 2e table as the
  candidate), esterification K (g12 ch6).
- Pilot nits to report / fix (not mine to change silently): g7 problem prints
  17 % O₂ breathed out while `breath:O2` says 16 (explained in a comment);
  g11 problem solution 16 says GHS08 "causes cancer" — the ledger row has
  only the pictograms (H350 not recorded).

## Traps (new ones go here)

- Ledger ids take ONE colon (`ab:crust-O`, not `ab:crust:O`): check_ledger's
  ID regex.
- `\fpeval` is not available (old kernel): use `\pgfmathtruncatemacro`.
- `\par` must never be a pgfmath macro name; foreach variable `\c` is fine.
- The brace decoration is not loaded (`decorations.pathreplacing`): draw
  bracket lines with `-|`.
- Index overfull vbox "while \output is active": fixed for good in the entry
  file with `\renewcommand{\indexspace}{\par\vskip 8pt plus 4pt minus 4pt\relax}`
  (the biology fix) — entry file edited, to report.
- The gate's word list flags "French" anywhere (e.g. "a French chemist"):
  nationalities of scientists are left out.
- My heredoc chunks sometimes end in a stray `\begin{xxx]` line: run
  `trim.py <file>` (scratch) after appending; gates/builds catch it otherwise.

- Phase A only: none hit yet. Known from the pilots / memory: `ghsystem`
  package must not be loaded; `\pic[transform shape]` in scaled pictures; a
  `center`/tabular as the first thing in a statement sits on its heading line
  — lead in with a sentence; a run of placeholder `\section*` stubs cannot
  break pages; `pgrep -f ai_images.py` matches its own shell.
- The harvester also picks up `\emph{X}\index{X}` **outside** definitions
  (attributed to the preceding statement label): never put such a pair in a
  `recall`, `history`, `inthelab` or `safety` box, nor in a remark.
- A bare `\emph{word}` inside a definition is harvested when its letters
  start with the label leaf (≥ 4 letters): keep incidental emphasis out of
  definitions or choose the leaf accordingly.
