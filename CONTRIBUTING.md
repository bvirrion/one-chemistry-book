# Contributing to One Chemistry Book

Thank you for contributing! This document describes the structure of the
project and the conventions that keep the book coherent.

## Project structure

The project is a **series of four books** sharing one style and one `parts/`
tree. Each book has its own entry file at the repository root:

- `one_chemistry_book_1_school.tex` — Book 1, Grades 1–12 in one volume;
- `one_chemistry_book_2_university_year_1.tex` — Book 2, University Year 1;
- `one_chemistry_book_3_university_year_2.tex` — Book 3, University Year 2;
- `one_chemistry_book_4_university_year_3.tex` — Book 4, University Year 3.

`OUTLINE.md` fixes the chapter list of all four books and the
**notion-ownership map**: every notion has exactly one owner chapter. Book 1
never teaches the same notion twice; a later chapter that needs it opens with
a `recall` box pointing to the owner and only adds what is new.

The shared files:

- `styles/onechemistry.sty` — **the only place** where packages are loaded
  and macros/environments are defined. Chapter files must not use
  `\usepackage` or define commands.
  One exception: a drawing helper used by a single figure may be defined
  *inside* that figure's `omfigure` or `tikzpicture` (local scope, e.g.
  `\irpanel`, `\nmrpanel`), never at the top level of a chapter. If its
  argument is a key rather than prose, add a mask for it in
  `tools/termlink/protect.py`.
- `styles/lang/<lang>.tex` — UI strings for each language (`en` for now).
- `frontmatter/` — title page, colophon, preface, image credits.
- `parts/<year>/part.tex` — `\part` via `\omstr{...}` and `\ominput`s.
- `parts/<year>/NN-slug.tex` — English chapter (canonical).
- `parts/<year>/solutions/NN-slug.tex` — English solutions.
- `sources/data_ledger.md` — the shared ledger rows (atomic weights,
  constants); `sources/ledger/book<N>.md` — each book's own rows. Every
  number quoted for a real substance has a row, with its source.

**Cross-volume references:** `\cref` only works within one book. Never
reference a label that lives in another book; name the volume in prose
instead. Inside Book 1, a `\cref` to any grade is fine.

## Building

```sh
make          # runs latexmk (pdflatex), builds every book into build/
make venv     # once: the Python environment for the tools and figure data
make test     # the tools' tests (make test Y=<year>: one year's)
make figdata  # regenerate the figure tables, must leave no diff (Y=<year> too)
bash tools/gates.sh grade-11   # the chapter-level gates for one year
```

A pull request must build with **zero errors**, no undefined references and
no overfull boxes, and pass `tools/gates.sh` for every year it touches.

## Environments

| Environment | Use for |
|---|---|
| `definition` | new notions; put the defined term in `\emph{...}` and `\index{...}` it — `\index` appears nowhere else, except that a named law may be indexed in the theorem/proposition that states it (the term harvester makes every `\emph`+`\index` pair, and any multi-word `\index` in a statement, a link target) |
| `theorem` / `proposition` / `lemma` / `corollary` | laws and results |
| `method` | step-by-step recipes (balancing an equation, a progress table, a titration) |
| `example`, `remark`, `notation` | worked examples, comments |
| `proof` | derivations when useful; otherwise `\admitted` |
| `exercise` | end-of-chapter exercises, difficulty `[$\star$]` to `[$\star\star\star$]` |
| `problem` | weekend multi-part problem set; label `pb:<year>:<slug>:1` |
| `solution` | `\begin{solution}{exo:...}` keyed to the exercise label |

Four unnumbered boxes hold the asides. They carry no label, and never
introduce a defined term:

| Box | Use for |
|---|---|
| `recall` | *You already know*: 3–5 lines recalling a notion owned by an earlier chapter, with a `\cref` to it when it is in the same book; a notion from another volume is cited in prose ("Book 1, grade 12", "the Year 1 volume") |
| `inthelab[title]` | how a procedure is carried out in a laboratory |
| `history[title]` | a short history: who, when, what was found |
| `safety{\ghs{GHS05}...}` | the hazard pictograms of a product (`\ghs{GHS01}`…`\ghs{GHS09}`) and what they mean |

## Chemistry conventions

- **CIP descriptors with `\cip{R}`** (prints *(R)*); `\R` is the real
  numbers. Units `\debye` and `\ppm` exist; quantum boxes are
  `\omorbs{ud,u,}`; plot styles `omprofile` (energy profiles) and `omeph`
  (potential–pH diagrams).
- **Formulas and equations with `\ce{...}`** (mhchem) everywhere — in prose,
  tables, figures and solutions: `\ce{H2O}`, `\ce{Cu^{2+}(aq)}`,
  `\ce{CH4 + 2O2 -> CO2 + 2H2O}`, `\ce{H3O+ + OH- <=> 2H2O}`. Never hand-built
  subscripts. Structural formulas with `\chemfig{...}`.
- **Every equation is balanced** — atoms and charge — and
  `tools/check_ce_balance.py` checks it. An equation left unbalanced on
  purpose (a "balance this" exercise) carries `% ce-unbalanced-ok` on the
  line where its `\ce{` starts.
- **Molar masses and stoichiometry are computed**, with
  `tools/molar_mass.py`, from the ledger's atomic weights. The book quotes
  atomic weights to 0.1 g/mol.
- **Every number about a real substance has a ledger row** — shared rows in
  `sources/data_ledger.md`, a book's own rows in `sources/ledger/book<N>.md`
  — and the chapter cites it in a source comment, `% ledger: <id>, <id>`
  (free text only after `(` or `;`). `tools/check_ledger.py` checks every
  id, and that ids are unique, sourced and dated.
- **Drawings are exact.** Apparatus is built from the glassware pics of the
  style file (`beaker`, `erlenmeyer`, `testtube`, `rbflask`, `condenser`,
  `burette`, `funnel`, `sepfunnel`, `hotplate`, `tlcplate`); molecular models
  from the atom styles (`aH`, `aC`, `aO`, `aN`, `aCl`, `aS`, `aNa`). AI
  illustrations are for everyday scenes only, never for glassware, molecules
  or anything a reader could measure.
- **Curves are computed**: titration curves, spectra, kinetics and
  distribution diagrams come from a tested script `figdata/<year>/<name>.py`
  writing `figdata/out/<year>-<name>.dat` (helper `figdata/_table.py`), which
  pgfplots reads; its test is `tests/<year>/test_<name>.py`. Spectra are
  synthetic, built at ledger positions.
- **No experiment is ever proposed for home.** Procedures are described as
  carried out in a laboratory, by or with a teacher (`inthelab`), and an
  exercise never asks the reader to try something.
- **Pure chemistry**: states of matter, density, heat and radioactivity
  belong to *One Physics Book*; a chapter uses them as known.

## Style rules

1. **Rigor**: state precisely; mark admitted results with `\admitted`.
2. **Concision**: no filler. An example after each substantial definition;
   a `method` box for each standard technique; **many diagrams**.
3. **Exercises**, every one with a full solution, stars never decreasing
   (`tools/check_exercise_calibration.py`):
   - grades 1–5: 10–11 exercises, mostly ★, no weekend problem;
   - grades 6–9: 12 exercises and a weekend problem of 10–14 questions
     (Parts I–III);
   - grades 10–12: exactly 15 exercises (5 ★, 6 ★★, 4 ★★★) and a weekend
     problem of 18–22 questions (Parts I–IV) ending on a named number;
   - university years: exactly 12 exercises (4 ★, 5 ★★, 3 ★★★) and a weekend
     problem of 22–28 questions (Parts I–IV) ending on a named number.
4. **English text** for an international audience; no curriculum or
   country names in student-facing text.
5. Quotation marks are `` ``…'' ``, never the straight `"`.

## Labels

All labels are namespaced: `<type>:<year>:<chapter-slug>:<name>`.

- Chapters: `ch:g11:redox`
- Statements: `def:g11:redox:oxidant`, `prop:...`, `met:...`, `ex:...`
- Exercises: `exo:g11:redox:3`
- Weekend problems: `pb:g11:redox:1`

Year prefixes: `g1`–`g12`, `b1`–`b3`.

Cross-reference with `\cref{...}`, never bare `\ref`.

## Workflow

1. Fork / branch.
2. Write or edit chapter + solutions files.
3. `make`, check the log for errors, undefined references and overfull
   boxes, and run `tools/gates.sh` on the years you touched.
4. Open a pull request.

## Licensing of contributions

One Chemistry Book is free for everyone under the licences in the [README](README.md#license). Contributing
means agreeing to the following.

1. **Same licence in as out.** Your contribution is licensed under the same terms as the part of the
   repository it changes: CC BY-NC-SA 4.0 for book content ([`LICENSE`](LICENSE)), MIT for the
   software — `tools/`, `.github/`, the `Makefile` and the build scripts ([`LICENSE-CODE`](LICENSE-CODE)).
2. **Sign off every commit** with `git commit -s`, which adds a line such as
   `Signed-off-by: Your Name <you@example.com>`. It certifies the
   [Developer Certificate of Origin 1.1](https://developercertificate.org): you wrote the change or
   have the right to submit it. For this project, "the open source license indicated in the file"
   in the certificate means the licences named in point 1.
3. **Relicensing grant.** You grant Benjamin Virrion a perpetual, worldwide, non-exclusive,
   royalty-free and irrevocable right to use, modify and relicense your contribution under other
   terms, including commercial ones (print editions, licences for schools, publishers or companies,
   paid app versions). You keep the copyright in your contribution and may use it as you wish.

**By signing off your commits you certify the DCO and agree to this whole section, including the
relicensing grant in point 3.** Why the grant exists: the books stay free under CC BY-NC-SA for
every reader; the grant only lets the author fund the project through commercial editions without
having to trace and ask every past contributor. Commits without a sign-off cannot be merged.
