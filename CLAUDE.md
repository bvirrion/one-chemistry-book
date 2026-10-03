# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A series of **four** LaTeX chemistry books built from **one shared `parts/`
tree**, one entry file per book at the repo root, and a single style file.
Structure, theme and tooling mirror `one-biology-book` (scaffolded from it on
2026-10-02): same One Course brand, environments, label conventions,
term-link engine.

**All four books are written in English (2026-10-02/03), uncommitted:**

| Book | Entry file | Years | Ch. | Pages | Figures | AI | Photos | Ledger rows | Links | figdata |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 Grades 1–12 | `one_chemistry_book_1_school.tex` | `grade-1`…`grade-12` | 49 | 432 | 260 | 102 | 23 | 229 | 5,775 | 10 |
| 2 University Year 1 | `one_chemistry_book_2_university_year_1.tex` | `bachelor-1` | 29 | 293 | 148 | 20 | ~30 | 635 | 2,471 | 20 |
| 3 University Year 2 | `one_chemistry_book_3_university_year_2.tex` | `bachelor-2` | 35 | 373 | 188 | 23 | ~40 | 490 | 1,733 | 27 |
| 4 University Year 3 | `one_chemistry_book_4_university_year_3.tex` | `bachelor-3` | 33 | 405 | 199 | 20 | ~22 | 286 | 1,632 | 64 |

(+ 113 shared ledger rows in `sources/data_ledger.md`: 1,908 in all.) Note the
offset: **Book 2 is `bachelor-1` / `b1`**, Book 3 `bachelor-2`, Book 4
`bachelor-3`. Every book builds 0/0/0, every `gates.sh` year is green, every
figure has its own FIGCHECK row (`sources/book<N>/FIGCHECK.md`, checked one
page per figure at 130 dpi), every link run is idempotent, and `make figdata`
leaves no diff.

- **Book 1 never repeats itself**: every notion has exactly one owner chapter
  (the ownership map is at the end of `OUTLINE.md`); a later chapter that
  needs it opens with a `recall` box and only adds what is new.
- **Books 2–4** are together the full licence de chimie with the prépa
  (PCSI, PC/PC\*) programmes inside it. A term has one owner across the three
  (`sources/SERIES_DEFINITIONS.md`, with every sync ruling); a university
  book may re-found a Book 1 notion.

**How it was written:** one subagent per book, at most two at a time,
rolling (user ruling 2026-10-02: Books 1+2, then Book 3 in Book 2's slot,
then Book 4). Each agent did Phase A (briefs, definition map) → main-session
sync → write → links and per-figure recheck → report; the main session
verified every book itself (recomputed problems, sampled figures) and sent
back what fell short. The binding rules and every sync/reconciliation note
are in `sources/BATCH_BOOKS_1-4.md`; per-book working notes in
`sources/book<N>/PROGRESS.md` (traps, EXCLUDED facts).

Pure chemistry: states of matter, density, heat and radioactivity belong to
One Physics Book. Content follows the old French programmes (provenance in
`sources/outline_sources.md` and the `part.tex` comments) **but the printed
books never name a programme, a country or a university**.

`OUTLINE.md` is the chapter list of record. `CONTRIBUTING.md` holds the
authoritative conventions; `THEME.md` the cover brand; the workspace-root
`book_style.md` the cross-subject rules. Read them before writing.

## Build

```sh
make                                        # latexmk, all four books into build/
latexmk one_chemistry_book_1_school.tex     # one book
L=build/one_chemistry_book_1_school.log
grep -ac '^!' $L; grep -aci undefined $L; grep -ac Overfull $L    # 0 / 0 / 0
```

pdflatex via `latexmkrc` (raised pdfTeX memory; the per-file engine dispatch
for future `_hi`/`_ar` editions is kept). Build with `-g` after creating a new
chapter file (a failed `\IfFileExists` records nothing in the `.fls`).

## Python tools

System `python3` has no numpy and no `ensurepip`; the repo venv is made with
`make venv` (`python3 -m venv --without-pip` + the user's `~/.local/bin/pip
--python`). `requirements.txt` pins numpy and pytest.

- `tools/chem.py` — parser for mhchem formulas and equations (standard
  library only, so the gates run under system `python3`).
- `tools/check_ce_balance.py <dir|file>` — every `\ce{...}` with an arrow
  must conserve atoms and charge; `% ce-unbalanced-ok` on the `\ce{` line
  exempts a deliberate skeleton. Unreadable expressions fail too.
- `tools/molar_mass.py <formula>...` — molar masses from the ledger's `aw:`
  rows; the book prints atomic weights to 0.1 g/mol (half-up).
- `tools/check_ledger.py [paths]` — the ledger gate. Shared rows (the complete
  CIAAW-2024 `aw:` table, SI/CODATA `const:`) are in `sources/data_ledger.md`;
  each book's rows in `sources/ledger/book<N>.md`. Every `% ledger: <id>, …`
  id must resolve to exactly one row; ids unique across files, each row with
  a source key and an access date.
- `tools/check_exercise_calibration.py parts/<year>` — the band's exercise
  count, star ramp and weekend-problem length (placeholders skipped).
- `tools/gates.sh <year>` — the chapter-level gates for one year
  (exo/pb ↔ solution, duplicate labels, `\end{..>`, `...`, straight quotes,
  problem numbering, equation balance, glassware pics in scaled pictures,
  home-experiment / curriculum words, PNG illustrations, ledger ids, exercise
  calibration). Duplicate labels and PNGs are reported for the year's own
  labels and book only, so a book in progress never fails another's gate.
  `make gates` runs every year.
- `tools/check_pic_scaling.py` — a picture-level `scale=` moves a `\pic` but
  does not scale its drawing; in a scaled picture every pic needs
  `\pic[transform shape]` (found on the grade-2 pilot: a sand layer twice as
  wide as its beaker, invisible to every other gate).
- `tools/ai_images.py --book N batch.txt --work <scratch>` — Codex image
  batches (scratch cwd, stdin closed, JPEG transcode, `PROMPTS.md` log,
  30-min sleep on a usage limit). Run it detached; it generates, it does not
  review. Do not wait on it with `pgrep -f ai_images.py` (the waiting shell
  matches itself).
- `figdata/<year>/<figure>.py` → `figdata/out/<year>-<figure>.dat` for
  pgfplots (helper `figdata/_table.py`: `write_table`, fixed number format);
  each with a test `tests/<year>/test_<figure>.py` (`pytest.ini` uses
  `--import-mode=importlib`, so basenames may repeat across years).
  `make figdata` must leave no diff; `make test` runs the tests; both take
  `Y=<year>` to run one year only.
- `tools/link_defined_terms.py --book N` — the term linker, copied from
  biology; `tools/termlink/protect.py` additionally masks `\ce{}`,
  `\chemfig{}` and `\ghs{}` arguments (two brace levels). Configs in
  `tools/term_config/book<N>_en.py`. Workflow: `--unwrap --apply`, then
  `--apply`; a plain dry run over the wrapped tree must print
  `links to insert: 0`.
- `tools/check_problem_numbering.py` — from biology.

## Traps met while writing (Books 1–2, 2026-10-02)

- **3D drawings: check the projected geometry, not only the labels.** At
  some `\tdplotsetmaincoords` views a cube's body diagonal projects onto a
  face diagonal, and the hidden vertex is not the one the pic assumes
  (`omcube`/`omhexprism` dashed the wrong edges for 0<θ<90, 90<φ<180).
  Cubic cells use view 60/100 with `omcubeo` and depth-sorted atoms; the HCP
  prism needs 70/113.
- **Count the bonds of a chemfig ring** (`*6(...)` with five bonds drew a
  five-membered hemiacetal); leave space after `\schemestop` when a scheme
  has substituents below it.
- **The term linker wraps words inside macro arguments that are code**
  (`\omperiodictable[f block=false]`, `\arrow{->[label]}`), which breaks the
  build: `protect.py` now masks those; add a mask there for any new macro
  whose options or arguments contain ordinary words.
- **Rounding from rounded intermediates** is the commonest solution slip
  (Book 2's independent re-read found 25); compute the chain once, round
  at the end.
- **Ledger: take the consensus value**, not the first entry a database
  lists, and never print more digits than the source's uncertainty (Book 2
  had argon from a 1971 outlier and methane to 0.1 K from a ±2 K average).
- `until ! pgrep -f "<cmd>"` matches the waiting shell itself: wait on a PID.

## Traps met while writing (Books 3–4, 2026-10-03)

- **The per-figure check means one page per figure at 130 dpi — never a
  contact sheet, never "72 dpi plus suspects".** Books 3 and 4 each tried
  the shortcut. A main-session sample found collisions in about one figure
  in five to seven, and the full rechecks then fixed 38 (Book 3) and 28
  (Book 4) defects. Four of them were chemistry, not layout:
  - Diels–Alder FMO lobes out of phase while labelled "in phase";
  - a concentration-cell voltmeter with + on the anode;
  - nitric acid without its formal charges;
  - a double-layer potential plotted positive for a negative metal.
- **Re-read every solution against its question, with a script.** Book 4's
  re-read found 24 slips:
  - a standard error that ignored the intercept–slope covariance;
  - S_xx miscomputed;
  - a "residuals below 1 %" that was false;
  - chains of rounded intermediates.
- **`tools/ai_images.py` writes relative to the cwd:** launch it from the
  repo root.
- **pgfplots and chemfig traps:**
  - A chemfig formula starting `[M]` is read as an angle ("Unknown function
    M").
  - A TikZ node name with a decimal (`oa-1.25`) breaks pgf.
  - `\pgfplotsset` inside a picture is local.
  - `booktabs` and the `groupplots` library are not loaded.
  - Thin legend lines look black at 130 dpi: zoom to 300 dpi before
    "fixing" a colour.
- **A figdata helper named `_stat.py`** is shadowed by Python's built-in
  `_stat`.
- **A weekend-problem box that fills a page** does not break under its
  section heading, so the heading is orphaned. Book 4 worked round it with
  `\clearpage` plus `\enlargethispage`. Check for an orphaned "Problem:"
  heading at a page foot.
- **Sources:**
  - ATcT, the IUPAC Gold Book/PAC, RSC and Johnson Matthey sit behind
    Cloudflare.
  - The WebBook has no formation enthalpies for most alkyl radicals.
  - The Burcat file's tert-butyl entry is garbled; Tsang's value is quoted
    beside it.
  - HSDB's water density at 25 °C (0.9950) is wrong: use IAPWS-95
    (0.99705).
  - NBS C514's 78.54 for water's permittivity is superseded by IAPWS 78.4.

## Style file additions (`styles/onechemistry.sty`)

- `mhchem` (v4) and `chemfig` (`\setchemfig` sizes are series-wide).
- `\ghs[height]{GHS0n}` — GHS pictograms, included directly from TeX Live's
  `ghsystem/pictures/*.pdf`. **The `ghsystem` package itself is NOT loaded**:
  its release calls `\chemmacros_load_module:n`, absent from the installed
  chemmacros, and the preamble dies.
- Boxes `recall`, `inthelab[title]`, `history[title]`, `safety{pictos}` —
  unnumbered, no labels, never a defined term inside.
- Atom styles for ball-and-stick models (`aH`, `aC`, `aN`, `aO`, `aCl`, `aS`,
  `aNa`, `bond`) — draw bonds `on background layer` between `.center`s.
- Glassware pics (`beaker`, `erlenmeyer`, `testtube`, `rbflask`, `condenser`,
  `burette`, `funnel`, `sepfunnel`, `hotplate`, `tlcplate`), origin at the
  bottom centre, liquids clipped to the outline; see the comment block in the
  style file for sizes and arguments.

## Architecture and conventions (as in biology)

Labels `<type>:<year>:<chapter-slug>:<name>`, year prefixes `g1`–`g12`,
`b1`–`b3`; `\cref` only, never across books. Exercises: grades 1–5 10–11, no
problem; grades 6–9 12 + a ~12-question weekend problem (Parts I–III);
grades 10–12 exactly 15 (5★/6★★/4★★★) + a ~20-question problem (Parts I–IV)
ending on a named number. Every `exo:`/`pb:` has one `\begin{solution}{key}`
(problem answers `\textbf{N.}` inside it). AI illustrations are JPEG
(`images/book<N>/ai/`, prompts in `PROMPTS.md`), photographs with
`CREDITS.md` and the Image Credits page. Placeholder solutions files carry a
line of text: a run of bare `\section*` stubs cannot break across pages and
reported a 400 pt overfull `\vbox`.

**Never commit.** Leave the working tree for the user.
