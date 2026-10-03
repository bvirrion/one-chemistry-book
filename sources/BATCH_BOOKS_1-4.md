# Rolling batch: One Chemistry Books 1–4, English (started 2026-10-02)

The four books are written in this one working tree, **one agent per book,
at most two agents at a time, on a rolling basis** (user ruling 2026-10-02):
Books 1 and 2 start together; when a book lands and the main session has
verified and reconciled it, the next book takes its slot — Book 3 first, then
Book 4. This file is owned by the main session; book agents read it and never
edit it.

| Book | Entry file | Years (`parts/…`) | Label prefixes | Ledger | Linker policy | Chapters to write |
|---|---|---|---|---|---|---|
| 1 Grades 1–12 | `one_chemistry_book_1_school.tex` | `grade-1` … `grade-12` | `g1`–`g12` | `sources/ledger/book1.md` | `nearest-preceding` | 46 (3 pilots done) |
| 2 University Year 1 | `one_chemistry_book_2_university_year_1.tex` | `bachelor-1` | `b1` | `sources/ledger/book2.md` | `drop` | 29 |
| 3 University Year 2 | `one_chemistry_book_3_university_year_2.tex` | `bachelor-2` | `b2` | `sources/ledger/book3.md` | `drop` | 35 |
| 4 University Year 3 | `one_chemistry_book_4_university_year_3.tex` | `bachelor-3` | `b3` | `sources/ledger/book4.md` | `drop` | 33 |

Note the offset: **Book 2 is `bachelor-1` / `b1`**, Book 3 `bachelor-2` /
`b2`, Book 4 `bachelor-3` / `b3`.

## Read before anything

1. `../CLAUDE.md` (workspace), `../book_style.md` (the family style — read
   Visuals and Quality gates twice), this repo's `CLAUDE.md`,
   `CONTRIBUTING.md`, `OUTLINE.md` (chapter list of record and the
   notion-ownership map), `sources/SERIES_DEFINITIONS.md`, and this file.
2. **The three Book 1 pilots, approved by the user as the reference** for
   register, density, the recall / inthelab / history / safety boxes, `\ce`
   and chemfig use, glassware pics and figure style:
   `parts/grade-2/01-mixing-and-dissolving.tex`,
   `parts/grade-7/02-atoms-and-molecules.tex`,
   `parts/grade-11/07-redox.tex` (and their `solutions/` twins).
3. University agents also read one Year-1 chapter of each sister series for
   the theorem-with-derivation register:
   `../one-biology-book/parts/bachelor-1/13-enzymes.tex` and
   `../one-physics-book/parts/bachelor-1/22-first-law.tex`.
4. `styles/onechemistry.sty`'s chemistry section (boxes, `\ghs`, atom styles,
   glassware pics and their arguments) — use what exists before inventing.

## User rulings in force

- One subagent per book; never per-chapter agents. No review pause: syncs are
  internal to the main session; agents write straight through after them.
- The Book 1 pilots are approved as they are.
- Series conventions (2026-10-01): pure chemistry (states of matter, density,
  heat, radioactivity are physics — used as known, never taught); `\ce`
  everywhere; exact drawings (chemfig / TikZ / glassware pics / modiagram),
  **AI images for everyday, industrial and lab-scene pictures only**; curves
  from tested Python; a sourced data ledger; synthetic spectra; **no printed
  Python exercises**; one lab-techniques chapter per university book plus
  `inthelab` boxes; **no experiment ever proposed for home**; GHS `safety`
  boxes; prépa methods taught in English (progress table, predominant
  reaction, Q/K°, E–pH, i–E); concours-style *original* weekend problems;
  method sheets (`method` environments) and short `history` boxes; **no
  oral-exam ("colle") question lists**.
- Printed text never names a programme, a country, a university or an exam.
  Provenance lives in comments and `sources/` only.
- Never use the user's e-mail address anywhere: not in a User-Agent, a
  request or a file. If a source asks for one, use another source.

## Calibration (binding; `tools/check_exercise_calibration.py` enforces it)

| Band | Exercises per chapter | Weekend problem | Pages per chapter |
|---|---|---|---|
| grades 1–5 | 10–11, mostly ★, never decreasing | none | ~7 |
| grades 6–9 | exactly 12, never decreasing | one, 10–14 questions, Parts I–III | ~9 |
| grades 10–12 | exactly 15: 5★, 6★★, 4★★★ in order | one, 18–22 questions, Parts I–IV, ending on a named number | ~11 |
| bachelor 1–3 | exactly 12: 4★, 5★★, 3★★★ in order | one, 22–28 questions, Parts I–IV, ending on a named number | ~11.5 |

Targets: Book 1 ~500 pp, Book 2 ~340, Book 3 ~400, Book 4 ~380 (schematics
count; illustrations and photographs come on top and make chapters longer, as
they should).

**University register.** Laws are `theorem` / `proposition` with a derivation
at the year's mathematics level; what is not derived gets `\admitted` and a
prose pointer to where it is proved ("derived in the Year 3 volume" — prose,
never `\cref`). Each standard technique is a `method`. Classic experiments
may be told in a `history` box.

**Math level guard.**
- Book 1: whole numbers only in grades 1–3; fractions from grade 4;
  percentages from grades 6–7; powers from grade 8 (scientific notation in
  grade 9); proportionality throughout high school; derivatives only from
  grade 11, a rate written as a derivative only in grade 12; `log10` and
  `exp` **only in grade 12** (pH = −log, pKa, first-order half-life) — the
  grade-9 pH scale is qualitative (one step per tenfold dilution).
- Year 1 (Book 2): derivatives, first-order linear ODEs, exp/ln, small linear
  systems, complex numbers for the s/p/d angular talk only if needed.
- Year 2 (Book 3): adds determinants and eigenvalues (Hückel), partial
  derivatives and exact differentials (thermodynamics), simple separable PDEs.
- Year 3 (Book 4): adds the operators and eigenproblems of quantum chemistry,
  group representations, statistics up to linear regression.

## Ownership rules (in force at all times)

1. **Write only your own files:**
   - `parts/<your years>/` (chapters, `solutions/`, `part.tex` only if a
     comment needs it — the `\ominput` list is frozen);
   - `figdata/<your year>/` and `tests/<your year>/`;
   - `images/book<N>/` (incl. `CREDITS.md`, `ai/PROMPTS.md`);
   - `sources/book<N>/` (`BRIEFS.md`, `DEFINITIONS.md`, `PROGRESS.md`,
     `FIGCHECK.md`, scratch notes) and `sources/ledger/book<N>.md`;
   - `tools/term_config/book<N>_en.py`;
   - `frontmatter/image-credits-book<N>.tex` (Book 1:
     `frontmatter/image-credits.tex`);
   - your entry file, only if unavoidable (report it).
2. **Never edit** another book's files. Defects you find there go in your
   report with file:line and the fix.
3. **`styles/onechemistry.sty` is append-only**, and only when unavoidable:
   append at the end under a `% Book <N>:` comment; never change or reorder
   existing lines; re-read the file just before editing (the other agent
   appends too); prefix new macros or scope them clearly; build your book
   right after. Prefer asking at the sync (Phase A report) over appending.
4. **Do not edit** `tools/` (except your term config), `Makefile`,
   `latexmkrc`, `pytest.ini`, `figdata/_table.py`, `OUTLINE.md`,
   `CONTRIBUTING.md`, any `CLAUDE.md`, `THEME.md`, `frontmatter/` pages that
   are not yours, `styles/lang/`, `sources/data_ledger.md`,
   `sources/SERIES_DEFINITIONS.md`, `requirements.txt`, `.venv`, `.github/`,
   or this file. If a tool is buggy or a shared value is missing, report it
   and work around it locally if you can; new traps go in your
   `PROGRESS.md`.
5. **Git is read-only**: `git status`, `git diff`, `git log`. Never
   `checkout`, `stash`, `reset`, `clean`, `restore`, `add` or `commit` — a
   repo-wide checkout once destroyed a whole batch of shared uncommitted work
   in the sister series. Nothing in this repo is committed yet: this working
   tree is the only copy.
6. **Build only your own entry file**: `latexmk <entry>` (with `-g` after
   creating a new chapter file — a failed `\IfFileExists` records nothing in
   the `.fls`). Never a bare `latexmk`, `make` or `make gates`; never two
   `latexmk` on your entry at once; never a short timeout around it (a killed
   run corrupts `.aux`/`.toc`: recover by deleting your entry's
   `.aux .toc .out .fdb_latexmk` in `build/`).
7. **Scoped checks only:** `bash tools/gates.sh <your year>`;
   `make test Y=<your year>`; `make figdata Y=<your year>`;
   `python3 tools/link_defined_terms.py --book <N>`. The gates scope
   duplicate labels and PNG checks to your year/book; if a check still fails
   on a path that is not yours, note it and carry on.
8. **Cross-book references are prose only** ("the Year 2 volume", "Book 1"),
   never `\cref` into another book.
9. **Terms**: follow `sources/SERIES_DEFINITIONS.md`. Before each chapter's
   definitions, grep the harvest of the books already written (command in
   that file). A university book re-founds a Book 1 notion only where the map
   says so, and never defines a notion another university book owns.
10. **Figure renders and image work** go to your own scratch directory:
    `/tmp/claude-1000/-home-bvirrion-repositories-one-course/b9a6f211-cc8e-4713-b734-e61467fa9bb3/scratchpad/book<N>/`.
    Check the running header of every render (it names the book).

## Resource limits (user rule, binding from the first command)

The machine is the user's laptop (22 logical cores, 19 GB RAM, WSL2), shared
with their own work and the other agent.
- Every process under ~1.5 GB RSS and one core; BLAS threads 1
  (`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1`); no multiprocessing, no
  `make -j`; one heavy job per agent at a time.
- Long jobs under `nice -n 19` **and** a cgroup cap:
  `systemd-run --user --scope -q -p MemoryHigh=2G -p MemoryMax=4G <cmd>`.
- `latexmk` only when a chapter is ready, under `nice -n 10`.
- Check `free -g` before anything heavy; leave alone every process that is
  not yours.

## Sources and the ledger

- **A model's memory is not a source.** Every number about a real substance
  (pKa, E°, ΔfH°, S°, Ks, β, bond energy, solubility, IR band, ¹H/¹³C shift,
  coupling constant, abundance, melting point used as data, industrial
  tonnage, GHS pictograms) has a row in `sources/ledger/book<N>.md` with a
  source key from that file's Sources table and an access date; the chapter
  cites it with `% ledger: <id>[, <id>]` (free text only after `(` or `;`).
  `tools/check_ledger.py` (gate 9) checks every id. Ids are unique across all
  ledgers: grep `sources/data_ledger.md sources/ledger/` before minting one,
  and cite another book's row read-only rather than duplicating it.
- Shared rows (complete CIAAW-2024 atomic weights, SI/CODATA constants) are
  in `sources/data_ledger.md` — read-only. Missing a constant? Report it.
- Values invented for an exercise are data of the exercise and need no row;
  values presented as facts about the world do. Computed numbers (molar
  masses, pH, yields) are computed — `tools/molar_mass.py`, or a `figdata/`
  script — never typed from memory.
- Fetch primary pages directly: NIST Chemistry WebBook, NIST-JANAF, CIAAW,
  IUPAC (Gold Book, data series), PubChem (GHS section), SDBS/NIST spectra,
  USGS Mineral Commodity Summaries for industrial figures, Wikimedia Commons
  API for photographs. Wikipedia `?action=raw` is a map to primary
  references, not a source. Never fill a row from a search snippet.
- **Search budget**: the session's 5,000 web searches are shared; plan
  ~600 per book and keep a running count in `PROGRESS.md`.

## Figures and images

- Schematics: ~4 per chapter (the old budget; it does not shrink because a
  chapter is illustrated). Apparatus from the glassware pics (`\pic[transform
  shape]` inside a scaled picture — gate 6b); molecules with chemfig or the
  atom styles; mechanisms with chemfig `@{node}` + `\chemmove` curly arrows;
  crystal cells with `tikz-3dplot`; MO diagrams with `modiagram` (both
  preloaded).
- **Curves are computed**: titration, distribution, E–pH, kinetics, spectra,
  phase diagrams, i–E — a script `figdata/<year>/<name>.py` whose curve lives
  in functions, writing `figdata/out/<year>-<name>.dat` via
  `figdata/_table.py` (`write_table`), read by `\addplot table`; and a test
  `tests/<year>/test_<name>.py` asserting the defining points (pH at
  half-equivalence = pKa, V_eq = C·V/C′, an E–pH boundary at its Nernst
  potential, integrals proportional to proton counts…). Spectra are
  synthetic, built at ledger positions. `make figdata Y=<year>` must leave
  no diff in `figdata/out/`.
- **AI illustrations**: `python3 tools/ai_images.py --book <N> batch.txt
  --work <your scratch>/ai` run **detached** (it sleeps 30 min on a usage
  limit; the two agents share one Codex limit — expect waits, put grey stubs
  meanwhile, never block on it; don't wait with `pgrep -f ai_images.py`).
  Everyday scenes, industrial plants, lab scenes only — never glassware
  close-ups, molecules or anything a reader could measure. JPEG only
  (`ls images/book<N>/ai/*.png` empty). Each image is reviewed for chemical
  accuracy (flame colours, rust, glassware, safety gear) before insertion;
  reject and regenerate if wrong. Prompts logged in `PROMPTS.md` with the
  model.
- **Photographs**: public domain or CC only, licence verified through the
  Commons API (`prop=imageinfo&iiprop=extmetadata`) with a User-Agent that
  carries **no e-mail**; a row in `images/book<N>/CREDITS.md` and an item on
  the Image Credits page; attribution-required licences credited at the
  caption's end. Portraits of named chemists and historic documents, real
  specimens and real plants — never a generated stand-in for a real person
  or object.
- **Every figure is checked on its own page at 130 dpi** (find its page with
  `pdftotext`, render with `pdftoppm -png -r 130 -f P -l P -singlefile`),
  twice: layout (no label on a label, line or arrow; nothing outside its
  box; caption clear of the drawing; no letters inside an AI image) and
  **chemistry** (curly arrows from electron-rich to electron-poor; lone
  pairs and formal charges right; VSEPR angles; stereo descriptors match the
  drawing; peaks at ledger positions; equivalence where the formula puts it;
  E–pH lines at their slopes; arrows of a cycle in the right sense). One line
  per figure in `sources/book<N>/FIGCHECK.md`
  (`ch | figure | page | layout ok/fixed | chemistry ok/fixed | note`).
  Never from a contact sheet.

## Agent lifecycle

**Phase A — plan, no prose; report, then stop.**
Write `sources/book<N>/BRIEFS.md` — per chapter: sections; definitions
(term, label, owner checked against `SERIES_DEFINITIONS.md` / the outline
map); recall boxes; planned figures tagged *schematic / figdata / AI /
photo*; ledger needs; the weekend problem's story and its named final number.
Also `sources/book<N>/DEFINITIONS.md` (the term list, one row per term with
chapter and label) and `sources/book<N>/PROGRESS.md` (state, page
projection, search count, traps). Then return the **Phase A report**:

1. Paths written; the entry file still builds 0/0/0.
2. **Re-founded terms** (Book 1 notions you will define again) and
   **contested terms** (anything not in the outline's map that another
   university book might also claim), with your case for each.
3. **Terms you use but do not define**, with their owner.
4. **Style-file needs** (packages, macros, pics) — the main session adds them
   at the sync rather than you appending.
5. **figdata scripts** planned (name, what they compute, the test's defining
   points).
6. **Image plan**: AI batch sizes per part/grade, photograph list with the
   Commons file names you intend to verify.
7. **Source plan**: the ledger-heavy chapters and your search estimate.
8. **Chapter changes** proposed (split, merge, reorder) with the reason.
   Default: none — the outline's numbering is what other books point to.
9. **Defects** found in the pilots, the tooling or the outline.

**Sync (main session).** Merge your map into `SERIES_DEFINITIONS.md`, rule on
collisions, make the style-file additions, write "Sync decisions" below, and
resume you with `SendMessage`. Book 1's sync checks the in-volume ownership
map; university syncs check against the books already written (their real
harvest) and the frozen maps of the books in flight.

**Phase B — write, in outline order.** Per chapter, the cycle:
1. ledger rows first;
2. course text: a concrete hook scene; 3–5 sections; every environment
   titled and labelled `<type>:<yr>:<slug>:<name>`; new terms as
   `\emph{term}\index{term}` inside a `definition`, **only in the owner
   chapter**; a `recall` box when a notion owned earlier is used; derive
   what the level allows, `\admitted` otherwise; `` ``…'' `` quotes, never
   `"`; `\dots`, never `...`; `\ce` for every formula and equation, balanced
   (gate 6; a deliberate skeleton carries `% ce-unbalanced-ok`);
3. exercises and the weekend problem at the band's calibration (gate 10);
   mix computation, reasoning, figure reading, orders of magnitude; no
   exercise asks the reader to try anything;
4. solutions: one `\begin{solution}{key}` per `exo:`/`pb:` in order, problem
   answers `\textbf{1.}`…; every number computed (`tools/molar_mass.py`,
   your figdata, a calculator script in your scratch dir) and **each answer
   re-read against its own question** — past runs shipped answer
   permutations, an answer contradicting its own question's data, and a
   question asking about the wrong object; gate 5 cannot see these;
5. figures (above), with their FIGCHECK lines;
6. `latexmk <entry>`, then `bash tools/gates.sh <year>`; fix to 0/0/0 and
   green before the next chapter.

**Checkpoints.** Every 10 chapters (Book 1: also at the end of each grade),
write a page projection in `PROGRESS.md`. A projection more than 15 % under
target means chapters are being compressed: restore depth before going on.
`PROGRESS.md` must always let a **fresh agent resume your book** from it
alone (chapter status table, open items, conventions you settled) — Book 1's
46 chapters may outlive one context.

**Phase C — finish.**
1. Term links: `python3 tools/link_defined_terms.py --book <N> --unwrap
   --apply`, then `--apply`. Curate `tools/term_config/book<N>_en.py` for the
   chemistry homographs — *solution* (a mixture vs the exercise solutions),
   *table*, *group*, *period*, *family*, *shell*, *base*, *cell*, *charge*,
   *yield*, *phase*, *indicator*, *element*, *compound*, *bond*, *species*,
   *reduction* (also "a reduction in cost"), *mole* — with `STOP`/`DROP`/
   `EXTRA_PROTECT` after checking each target, and watch the
   **capitalised-harvest trap** (a display that opens its sentence is
   harvested capitalised; `STOP`/`DROP` match case-sensitively). Never write
   `\omterm` by hand, never inside `\ce{}`, `\qty{}` or a figure. The
   idempotence dry run over the wrapped tree must print `links to insert: 0`.
2. The full per-figure double-check again over **every** figure (the links
   move text), FIGCHECK complete: one line per `omfigure` / `includegraphics`.
3. Re-read every solution against its question once more.

**Phase D — report** to the main session: pages vs target and chapter count;
counts of schematics, figdata scripts and tests, AI images, photographs,
ledger rows, term links and distinct targets; gate results (`gates.sh` for
each of your years, `make test Y=…`, `make figdata Y=…` no diff, the log
0/0/0, the idempotence dry run); EXCLUDED facts (a value you could not
source and therefore did not print); defects found in other books or the
tooling; new traps and calibration for the shared docs.

## Book notes

**Book 1** — continue from the pilots, grade 1 → grade 12, skipping the three
written chapters. Each notion taught once (the outline's Book 1 map); grades
1–5 short, warm, illustration-rich, whole numbers first. figdata: absorption
spectra and Beer–Lambert line (g11 `absorbance`), synthetic IR spectra (g11
`infrared`), ¹H NMR spectra (g12 `proton-nmr`), kinetics curves (g12
`reaction-rates`), pH-metric and conductimetric titrations (g12), distribution
diagrams (g12 `buffers-predominance`). Photographs to verify: Lavoisier,
Mendeleev and his 1869 table, Avogadro, Pasteur (tartrate crystals story), a
native ore, a copper patina. One AI batch per grade. Linker: `book1_en.py`
is already curated for the pilots; extend it.

**Book 2 (bachelor-1)** — the Year 1 foundation Books 3–4 build on, so its
definitions are the series' Year-1 vocabulary. Crystal cells in
`tikz-3dplot` (FCC/BCC/HCP, sites, NaCl/CsCl/ZnS/CaF₂ with exact
compactness and coordination); Newman, Cram and chair drawings; mechanisms
with `\chemmove`. figdata: exact acid–base titration curves (direct,
polyacid, successive), potentiometric curve, E–pH diagrams of water, iron,
copper, zinc (boundaries tested against Nernst), pL predominance diagrams,
integrated rate laws, energy profiles, synthetic UV/IR/¹H NMR with
multiplets. Ch. 26–28 (the elements) are ledger-heavy (industrial processes,
tonnages: USGS); ch. 29 is the lab chapter (GHS, H/P statements, type A/B
uncertainty, extraction/recrystallisation/distillation/TLC/melting
point/refractometry).

**Book 3 (bachelor-2)** — starts when Book 2 lands; read Book 2's actual
chapters and harvest before Phase A. NIST/JANAF thermodynamic rows; Hückel
energies and coefficients computed in figdata (numpy eigenvalues, tested);
MO diagrams with `modiagram`; binary phase diagrams and i–E curves computed
(i–E treated qualitatively: Butler–Volmer is Year 3's).

**Book 4 (bachelor-3)** — starts in the next free slot; checked against
Book 2's harvest and Book 3's frozen map (or harvest). Character tables cite
a standard source; partition functions, powder XRD patterns, model-system
levels, small minimal-basis HF illustrations computed in tested figdata. No
Python printed.

## Sync decisions

(Written by the main session after each Phase A report; binding.)

### S1 — Book 2 (2026-10-02)

1. **Definitions.** Book 2's map is granted as claimed, with the rulings in
   `sources/SERIES_DEFINITIONS.md`, "Sync S1 — Book 2": the re-founds of
   *yield*, *molar concentration* and *carbon class* are added; every
   contested term goes to Book 2 by the earliest-need rule, with the
   later-book split written there (e.g. *atomic orbital* is Book 2's
   quantum-number-labelled state, while Book 3 owns *wavefunction* and the
   radial and angular parts). *Micelle* stays with Book 4: Book 2 draws it
   and names it without a definition.
2. **Harvester rule, for all books.** `\index{}` appears only beside the
   `\emph{}` of a term the chapter owns, inside a `definition`, and nowhere
   else. (From Book 2's report: any `\emph`+`\index` pair, and any multi-word
   `\index` in a statement, becomes a link target.)
3. **Recall boxes across volumes** cite the other book in prose ("Book 1,
   grade 12", "the Year 1 volume"); `\cref` only inside the same book.
   `CONTRIBUTING.md` is updated.
4. **Style file, added by the main session** (end of
   `styles/onechemistry.sty`, block "Chemistry additions, Book 2 sync"):
   - `\cip{R}` → *(R)*, because `\R` is ℝ;
   - the units `\debye` and `\ppm`;
   - `\omorbs{ud,u,}`, quantum boxes with half-arrows;
   - the pgfplots styles `omprofile` (energy profiles: axes left and
     bottom, no ticks, `clip=false`; labels are written in the chapter) and
     `omeph` (pH 0–14 with a light grid).

   **Book 2 builds the drawing pics itself**, as one appended block headed
   `% Book 2 (shared pics):` at the end of the style file. That block holds:
   - `omnewman` and `omchair` (with the anchors you specified);
   - the crystal helpers `omcube`, `omhexprism`, `cellA`, `cellB` and
     `cellsite` (`\usetikzlibrary{3d}` if needed);
   - the electrochemistry pics `saltbridge`, `electrode`, `meter`, `probe`
     and `stirrer`;
   - the organic apparatus `threeneck`, `dropfunnel`, `guardtube`,
     `deanstark`, `stillhead`, `thermometer`, `liebig` (or a rotation-safe
     `condenser`), `adapter`, `heatingmantle`, `buchner` and `filterflask`.

   Rules for the block:
   - Build these early, as needed, in one place.
   - Each pic is documented in the block's comment, in the style of the
     existing glassware comment (origin, size, arguments).
   - Check every pic on a rendered test page in your scratch before using
     it.
   - Never change the existing pics. They are shared: Book 1 and Books 3–4
     will reuse them.
5. **Ledger.** Computing E°, Ks, β and the E–pH boundaries from NBS-82
   ΔfG° rows (Wagman et al. 1982, J. Phys. Chem. Ref. Data 11, suppl. 2,
   fetched from NIST) in tested figdata scripts is **accepted**, on these
   conditions:
   - each ΔfG° is a ledger row with its table page;
   - the chapter's printed E° and Ks come from the script, never typed;
   - the test compares each computed value against an independent open
     compilation where one exists (tolerance stated);
   - a directly measured value from an open primary source is preferred
     where one is reachable (IUPAC stability-constant reports, the IUPAC
     digitised pKa dataset under CC BY 4.0);
   - anything unsourced goes on the EXCLUDED list.

   The `_ledger.py` reader helper in `figdata/bachelor-1/` is fine.
6. **Preface.** The sentence on parts is now neutral ("In the first book
   each school year is a part …; each university book is one year …").
7. **Chapter numbering** is unchanged. The search estimate (~350) is
   accepted.

### S1b — Book 1 (2026-10-02)

1. **Definitions.** Book 1's map (`sources/book1/DEFINITIONS.md`: 300 terms
   in 183 definitions) is granted, and its proposals C1–C15 are accepted as
   written:
   - "solution" has one owner, g2. g6 defines *solute*, *solvent* and
     *aqueous solution*.
   - g4 owns *burning* and *combustion*; g8 owns *complete* and *incomplete
     combustion*.
   - g5 owns *chemical change*; g7 owns *chemical reaction*, *reactant* and
     *product*. g8 owns conservation and balancing.
   - g10 owns *extraction*; g11 owns the polarity explanation and *micelle*.
     Book 1 defines *micelle*; Book 4 keeps the university ownership.
   - g9 `inside-the-atom` owns *chemical element*.
   - "family", "group" and "period" are STOPped outside their owners.
   - The g12 `pH = -log` definition carries no new `\emph{pH}`.
   - g10 owns *distillation*.

   The 21 new first-use terms are granted.
2. **Notation, series-wide: hydroxide is `\ce{OH-}`** (the English convention
   and the outline's), never `HO-`. H⁺ is used up to grade 11; `\ce{H3O+}` is
   introduced in grade 12 and used in Books 2–4.
3. **Style file, added by the main session** (block "Book 1 sync" at the end
   of `styles/onechemistry.sty`):
   - `circuitikz`, loaded `[european,siunitx]`;
   - the atom styles `aF`, `aBr`, `aI`, `aP`, `aMg`, `aCa`, `aK`, `aAl`, and
     the generic `aX={colour}{size}`;
   - **`\omperiodictable[keys]`**: 118 cells; `colour=metals|blocks|families`;
     `legend`; `highlight={…}`; `values={Sym/val,…}`; `upto=`; `f block=`;
     `numbers=`. Read its comment block. It was checked on a rendered page.
4. **Glassware pics.** They are split by first owner; names are unique
   series-wide.
   - **Book 2's block** builds `heatingmantle`, `stillhead`, `thermometer`,
     a rotation-safe `liebig`/`condenser`, `adapter`, `buchner`,
     `filterflask`, `meter` (a box with a label argument; Book 1's "meterbox"
     is this pic), `probe` (Book 1's "phprobe"), `stirrer` (with its bar),
     `saltbridge` and `electrode`, and also `threeneck`, `dropfunnel`,
     `guardtube`, `deanstark`, `omnewman`, `omchair` and the crystal
     helpers.
   - **Book 1's block** (`% Book 1 (shared pics):`) builds `volflask`,
     `pipette`, `gradcyl`, `cuvette`, `condcell`, `bunsen`, `gasjar`,
     `deliverytube`, `trough`, `evapdish`, `utube` (an electrolysis U-tube),
     `balance` (no digits) and `stand` (with a clamp).
   - **Before building any pic, grep the style file for its name.** If you
     need a pic from the other book's list before it exists, build it in
     your own block under **that name and the interface written here**, and
     say so in your `PROGRESS.md`. The other agent then reuses it and does
     not redefine it (a second `\tikzset` definition would override the
     first silently).
   - Both blocks are append-only. Re-read the file before each append.
5. **Pilot defects.** Book 1 owns these files and fixes them in Phase B:
   - g7 problem: print the ledger's 16 % for oxygen in breathed-out air, or
     add a sourced row for 17 %.
   - g11 solution 16: add the H statements to `ghs:K2Cr2O7` from PubChem
     (H350 if listed), or soften the sentence to what the row supports.
6. **Content rulings.**
   - The g11 absorbance is defined operationally (no logarithm before
     grade 12).
   - "Air is matter" (g4) stays chemical: a mixture of gases, with mass taken
     as known from physics.
   - The candle-in-a-jar "one fifth" interpretation is kept out.
   - Limiting ionic conductivities: an open primary source if one is
     reachable, otherwise EXCLUDED, with a generic, unvalued example.
7. **Plans accepted:**
   - the AI plan (~89 images, one batch per grade);
   - the photograph list (each re-verified before insertion);
   - the search estimate (~350);
   - no chapter changes;
   - the g11 `titration` built on the permanganate titration promised by
     the redox pilot.

### S2 — Book 3 (2026-10-02)

1. **Definitions.** Book 3's map is granted as claimed; the rulings are in
   `SERIES_DEFINITIONS.md`, "Sync S2". All eight contested terms go to
   Book 3 by earliest need; Book 4 is told what it keeps. The hydrogenation,
   hydroformylation and cross-coupling split: Book 3 = cycles of elementary
   steps, Book 4 = industrial processes.
2. **Named laws** may be indexed in their theorem/proposition (Hess,
   Kirchhoff, Raoult, Henry, van 't Hoff, lever rule, Hückel's rule,
   Carothers…), owner chapter only. `CONTRIBUTING.md` is updated.
3. **Math level, Year 2:** least-squares regression is derived with partial
   derivatives (ch34); the statistics of the fitted parameters are
   admitted. The batch file's "statistics up to regression" for Year 3
   means inference beyond that.
4. **Style file, added by the main session** (block "Book 3 sync", checked
   on a rendered page):
   - pgfplots styles `omphase`, `omie`, `omellingham`, `omchrom`, `omms`,
     `omnmr` (x reversed) and `omir`;
   - TikZ curve styles `omliquidus`, `omsolidus`, `tieline`, `omanodic`,
     `omcathodic` and `omwall`;
   - `omretro` (the retrosynthetic arrow);
   - catalytic-cycle styles `cyclenode`, `cyclearc`, `cyclein`, `cycleout`
     and `cyclelabel`;
   - **series-wide: thin-space thousands in pgfplots tick labels.** Book 2's
     IR axes printed "4,000"; they are fixed by this on the next rebuild.

   **Book 3 builds the drawing pics itself**, as one appended block headed
   `% Book 3 (shared pics):`:
   - `omlevel` with `omcorr`;
   - the orbital lobes `omlobe`, `oms`, `omp`, `omdxy`, `omdx2y2` and
     `omdz2`;
   - the coordination geometries `omoctahedron`, `omtetrahedron`,
     `omsquareplanar` and `omtbp`;
   - `\omcycle` if you want the macro (the styles above are enough
     otherwise);
   - `chromcolumn`, `bubbler` and `septum`;
   - the series modiagram defaults (`\setmodiagram`).

   Each pic is documented, checked on a rendered page, and never changes an
   existing line. Book 4 will reuse them.
5. **Placement inside Book 3** is as proposed: mixed potential in ch11, the
   Ellingham approximation in ch2, HOMO/LUMO in ch17.
6. **Ledger:** compute bond enthalpies from CODATA/JANAF (not Book 1's
   textbook rows). Reuse Book 2's `dfg:` rows read-only. The "at risk" list
   is EXCLUDED or turned into exercise data, as proposed.
7. **Defects fixed by the main session:**
   - `CONTRIBUTING.md`'s `HO-` example;
   - the stale status in `CLAUDE.md`;
   - the even-page running header wrapping on Contents/Index pages
     (`\om@splitmark`; series-wide, all books).
   - Gate 7's "programme" stays: write "temperature ramp".


### S3 — Book 4 (2026-10-02)

1. **Definitions.** Book 4's map is granted as claimed (rulings in
   `SERIES_DEFINITIONS.md`, "Sync S3"). The hydrogen atom is solved in ch1
   (paying Book 3's pointer), PES in ch3, Debye length in ch15, the free
   carbene in ch20, inference on fitted parameters in ch12/15/33 — accepted.
2. **Style file, added by the main session** (block "Book 4 sync", checked
   on a rendered page):
   - `omchartable{group}{class colspec}{headers}`, a math-mode `array`
     whose every row ends with `\\`;
   - `\termsym{S}{L}{J}`, `\kv{X}{site}{charge}`, and the units `\hartree`
     and `\bohr`;
   - TikZ styles `omstate`, `omvib`, `omabs`, `omfluo`, `omphos`,
     `omnonrad`, `omisc`, `omfishhook`, `ompath`, `omsaddle` and
     `omtsforbidden`; `omscan=<pos>` for scan arrows;
   - pgfplots styles `omts`, `ompes` (viridis; contours prepared by
     figdata) and `omcv`;
   - the TikZ library `decorations.pathreplacing` (braces).

   **Book 4 builds** the crystallographic glyphs (`omtwofold`, `omtwoone`,
   `omthreefold`, `omfourfold`, `omsixfold`, `ominv`, `ommirror`,
   `omglide`, `omgenpos`, `omstereo`, `omup` and `omdown`) in one
   appended block, `% Book 4 (shared pics):`.

   **Book 3 was asked** to give `omp` a signed coefficient and a rotation,
   to add `omdxz`/`omdyz`, `omcorrforbidden` and `omsymlabel`, and to give
   `omlevel` a length. Book 4 reuses them and does not redefine them.
3. **Minimal-basis benchmarks:** test the code on the classic benchmark
   (H2 at 1.4 a0, -1.1167 Eh, S12 = 0.6593; HeH+ with zeta_He = 2.0925,
   -2.8607 Eh); print the standard-basis (BSE) values and say which is
   which.
4. **Fixed by the main session:** the stale `omcube` comment in Book 2's
   pic block is marked superseded (use `omcubeo`/`omhexprismo`).
5. **Resource rule (user, max two agents):** Book 4 was resumed only after
   Book 1's FIGCHECK send-back reported.


## Reconciliation to-do

(Main session; collected as books land.)

- **2026-10-02 20:00:** both agents stopped at 14:47 on the weekly usage
  limit (Book 1 at 40/49 chapters, Book 2 at 25/29 plus 26–27 drafted) and
  were resumed after the reset.
- **Main-session spot-check (snapshot of 363 pp / 272 pp):**
  - every finished year passed its gates; 906 ledger rows resolve;
  - Book 1, g11 titration problem: the answers were recomputed and are
    correct;
  - Book 2, ch10 problem: 21 of 22 answers are correct; **answer 16 gives
    pH 12.7 where the correct value is 12.57** (sent back);
  - figures checked: Book 1 Lewis structures, VSEPR models, wedges and the
    periodic table are fine. Book 2 carvone (R)/(S) is correct (CIP
    re-derived). Book 2 E–pH of iron has a label crossing a boundary, and
    the Book 2 FCC/BCC view projects the body diagonal onto a face diagonal.
    Both of these were marked clean in FIGCHECK, so both were sent back
    with a request to re-check projected geometry.
- Typography note: Book 1 p. 121 shows `\flushbottom` stretch (white space
  between a method and the next section, next to a full-width table).
  This is series-wide behaviour of the book class, left as it is.
- **Book 2 landed (2026-10-02, ~22:00) and was verified by the main
  session:**
  - forced build 0/0/0, 293 pp (-13.8 % against 340, inside the 15 % band;
    the thinnest are the organic chapters 20 and 22-25 at 6 pp: a candidate
    for a later enrichment pass, not padding);
  - `gates.sh bachelor-1` OK; `check_ledger` OK (986 rows); `make test
    Y=bachelor-1` 107 passed; `make figdata Y=bachelor-1` reproduces all 56
    outputs byte for byte; linker dry run 0;
  - FIGCHECK covers every figure (174 rows for 148 omfigure environments);
  - solutions recomputed by hand and found right: ch10 problem (after its
    fix) and the whole ch29 problem (z = 0.60);
  - 15 figures inspected on their pages, all right in layout and chemistry,
    except the ch25 HBr/propene profile, whose dashed curve crossed the
    legend: the legend now sits below the axis.
- **Ledger fixes by the main session in Book 2:**
  - `bp:Ar` took the WebBook's outlier, 87.5 K (Streng 1971); it now holds
    the other WebBook entry, 87.28 K, so argon prints as -185.9 degC;
  - `bp:CH4` was the WebBook's 13-value *average*, 111 +- 2 K, printed as
    -162.1 degC with false precision; it now uses PubChem's -161.50 degC,
    printed as -161.5;
  - the text, the problem data and solution 16 of ch4 follow.
  - **Trap for every book:** when the WebBook lists several values, take
    the consensus one, not the first; never print more digits than the
    row's uncertainty.
- **Tooling, fixed in the shared linker:** `tools/termlink/protect.py` now
  masks `\omperiodictable[...]` options, chemfig `\arrow{...}[...]`,
  `\chemmove{...}` and `\omorbs{...}` for every book. Book 2 had found
  links breaking the build inside the first two. Book 2's local masks are
  now redundant but harmless.
- **Book 1 landed (2026-10-02, ~22:15)** at 432 pp (-14 %, inside the
  band), with 5,776 term links. Verified by the main session:
  - all twelve `gates.sh grade-N` pass; `check_ledger` OK; the linker dry
    run prints 0; figdata for grades 8 and 10-12 reproduces byte for byte;
    `pytest tests` passes 139;
  - two problems recomputed and found right: g10 airbag, 101 g of NaN3 at
    V_m = 24.1; g12 phone battery, 1.03 g of Li at M = 6.9.

  Problems found:
  - **A plain `latexmk` failed**: 17 g12 AI images were missing, while the
    agent built through a scratch `build.sh` that supplied placeholders.
    - Fixed: the new `tools/ai_stubs.py` makes grey stubs in the repo, and
      `ai_images.py` regenerates any JPEG under 20 kB.
    - `gates.sh` warns while stubs remain, and a book is not finished while
      it carries one.
    - The old g12 batch and its waiter were killed (the waiter would have
      run a duplicate batch) and one batch was restarted:
      `scratchpad/book1/ai/log-g12b.txt`. The main session reviews and
      FIGCHECKs those 17 images when they land.
  - **FIGCHECK coverage was short** by about 25 figures in grades 6-12, and
    by the three pilots. This was sent back to the Book 1 agent.
  - **Figure-local helper macros** (`\irpanel`, `\nmrpanel`, `\cube`, ...)
    are defined inside their `omfigure`/`tikzpicture`. This is allowed now
    (`CONTRIBUTING.md`), and `protect.py` masks `\setchemfig{}` and
    `\irpanel{}`.
  - **The even-page running header wraps** "Book 1: School Chemistry --" onto
    two lines on the contents and index pages. Book 2 and biology Book 1
    show it too. It is a shared style defect, open for the main session.
- **Book 4 launched (Phase A)** in Book 1's slot. Books 3 and 4 will be
  synced together.
- **Book 1 closed (2026-10-03, ~00:30, main session):**
  - FIGCHECK send-back: 74 rows added, 11 defects fixed (two in the pilots:
    "methane molecules are burning"; Dalton's nationality).
  - The 17 g12 AI images landed and were reviewed by the main session. Two
    were rejected and regenerated:
    - `g6-orange-juice`: the pulp was invisible;
    - `g12-wine-lab`: the burette held wine; the titrant is colourless.
  - Page checks:
    - ch44 (g12.7) said ants *sting* to inject methanoic acid. Wood ants
      have no functional sting, so the hook, caption and problem title now
      say ants defend themselves with methanoic acid.
    - Three images were capped in height; one of them had stranded a
      section heading.
  - Final: 432 pp, 0/0/0, every gate green, no stubs, links idempotent,
    thin-space thousands throughout.
- **Book 3 landed (2026-10-03, ~18:00)** at 373 pp (-6.7 %), with 1,733
  links, 188 figures, 23 AI images and 40 photos. Verified by the main
  session:
  - forced build 0/0/0, no comma thousands; gates OK; ledger OK (1,908
    rows); link dry run 0; figdata byte-stable; 129 tests passed;
    FIGCHECK covers every figure;
  - ch9 problem recomputed, all 25 answers right.

  Problems found:
  - The agent's post-link figure pass used 6-up contact sheets, which the
    rules forbid. The main session's sample of 15 figures, each on its own
    page, found 3 collisions: the ch5 Semenov label, the ch11 chlor-alkali
    labels, and the ch11 zinc i-E label. **Sent back for a full 130-dpi
    per-figure recheck.**
  - Book 1 ledger: `rho:water` was 0.9950 g/cm3 (HSDB, wrong at 25 degC).
    It is now 0.99705 (IAPWS-95, WEBBOOK-FLUID). Book 2 ch23 printed
    0.995 g/mL; it now prints 0.997. Book 1 prints only "1.0 g", which is
    unchanged.
  - The Book 3 entry file sets `\raggedbottom`. The series-wide decision is
    open (move it into the style file at the end, rebuild all four books,
    re-gate).
- **Book 4 landed (2026-10-03, ~19:00)** at 405 pp (+6.6 %, the only book
  over target), with 1,632 links, 199 figures, 20 AI images, 22 photos and
  64 figdata scripts. Verified by the main session:
  - forced build 0/0/0; gates OK; ledger OK; link dry run 0; figdata
    byte-stable; 188 tests passed;
  - ch6 problem recomputed, all 24 answers right; ch28 and ch31 named
    numbers right;
  - 7 sampled figures right in chemistry; one layout defect (ch18
    Tanabe-Sugano labels crossed by grey curves).

  Sent back for two passes:
  - a 130-dpi per-figure recheck: its Phase C pass had been 72 dpi, with
    "suspects" only at higher resolution;
  - a full solutions re-read: the agent's own recommendation, since none
    had been done.

  **Reconciliation items:**
  - Book 2 `epsr:H2O` 78.54 (NBS C514, 1951) against IAPWS 78.4 (Book 4
    `eps:H2O.25C`). Fix at the end: Book 3's colligative figdata reads
    that row, so wait until Book 3's recheck is done.
  - An orphaned problem heading when a one-page problem box does not fit
    (Book 4 worked round it with `\clearpage`). Look at making `problem`
    breakable series-wide.
  - Gate 7 now matches `programmes?\b`, so "temperature-programmed" no
    longer trips it.
  - `\raggedbottom` is now in the Book 3 and Book 4 entry files. Decide
    series-wide.
- **Book 3 closed (2026-10-03, ~19:15).**
  - The 130-dpi per-figure recheck fixed the 3 collisions the main session
    found, plus 35 more defects.
  - Three of those were chemistry errors:
    - ch17: the Diels-Alder LUMO lobes were out of phase while labelled
      "in phase";
    - ch9: the concentration-cell voltmeter had + on the anode;
    - ch22: nitric acid was drawn without its formal charges.
  - The main session checked all three on their pages.
  - Final: 373 pp, 0/0/0.
- **Reconciliation done by the main session (2026-10-03):**
  - `epsr:H2O` (Book 2): 78.54 (NBS C514, 1951) replaced by IAPWS 78.4,
    agreeing with Book 4.
    - Book 2 ch4 now prints 78.4.
    - Solution 8: 78.4/1.89 = 41, so "41 times weaker".
    - Book 3's Debye-Hueckel A (0.5099) still prints as 0.51; its test
      passes.
  - `\raggedbottom` moved into `onechemistry.sty`, series-wide. Books 1
    and 2 rebuild 0/0/0 with unchanged page counts (432, 293), and Book 1
    p. 121's stretched gap is gone.

