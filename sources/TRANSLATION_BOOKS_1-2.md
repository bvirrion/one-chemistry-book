# Translation run — One Chemistry Books 1 and 2 into fr, nl, es, pt, hi, ar, id

The binding run file for the fourteen language editions of Book 1 (School
Chemistry, grades 1–12, `parts/grade-1` … `parts/grade-12`, 49 chapters +
49 solution files = **98 files**) and Book 2 (University Chemistry, Year 1,
`parts/bachelor-1`, 29 + 29 = **58 files**). User request, 2026-10-04: one
subagent per book-and-language edition, batches of at most four.

If you are an edition agent, this file and your brief are your instructions.
Read everything in "Reading list" before you write a line.

## Waves

| Wave | Editions | Notes |
|---|---|---|
| 1 | B1 `fr` `nl` `es` `pt` | first readers of the B1 canon; share gate 9 |
| 2 | B1 `hi` `ar` `id` + B2 `fr` | inherit the fixed B1 canon; B2 `fr` is the first B2 reader and becomes the same-book French sense twin |
| 3 | B2 `nl` `es` `pt` `hi` | inherit the fixed B2 canon and the B2 `fr` twin |
| 4 | B2 `ar` `id` | |

Between waves the coordinator fixes confirmed canon defects and gate bugs,
re-measures the English baselines and writes `sources/WAVE<n>_FINDINGS.md`.
**Every later agent reads every WAVE file that exists when it starts.**

## Reading list (in this order, whole files)

1. `../CLAUDE.md` (workspace root) and `../book_style.md`.
2. `../translation_instruction.md` — **the whole file**. It is the procedure,
   and nearly every paragraph is a defect class some earlier edition shipped.
3. Your language's style card: `../hindi_style_card.md`,
   `../arabic_style_card.md` or `../indonesian_style_card.md`. The Latin four
   have none: use the same language's shipped biology editions (below).
4. `CLAUDE.md` and `CONTRIBUTING.md` of this repo (`one-chemistry-book/`).
5. `../one-biology-book/CLAUDE.md`, section "Language editions" — the most
   recent full translation run of this same toolchain, with its findings.
6. This file, then any `sources/WAVE<n>_FINDINGS.md`.

## Hard rules (quoted from the procedure; all are binding)

1. **You own exactly one edition.** You write only:
   - `parts/<year>/<lang>/*.tex` and `parts/<year>/solutions/<lang>/*.tex` for
     your book's years;
   - `tools/term_config/book<N>_<lang>.py` (a stub is waiting — curate it from
     YOUR edition's harvest, never by translating `book<N>_en.py`, never by
     copying another book's config);
   - `translation_scores/book_<N>/<lang>/translation_score.md`;
   - your entry file's `\bookline` and `\author` lines only, if you want to
     improve the coordinator's wording;
   - Book 1 agents: `frontmatter/preface.<lang>.tex` (shared by every book of
     that language — translate it, and adapt the sentence that says the book
     is "written in English": the edition is not) and
     `frontmatter/image-credits.<lang>.tex`; Book 1 agents also own the four
     chemistry box names in `styles/lang/<lang>.tex` (`\omnameRecall`,
     `\omnameInTheLab`, `\omnameHistory`, `\omnameSafety`, placeholder
     wording now) — change nothing else in that file without reporting it;
   - Book 2 agents: `frontmatter/image-credits-book2.<lang>.tex`.
   The frontmatter files are English stand-ins until you translate them.
2. **Never edit the English canon** (`parts/<year>/*.tex`, `solutions/*.tex`)
   and never another language's files. A canon defect is REPORTED to the
   coordinator, with file, line and your evidence; the coordinator verifies it
   against the book's own model and fixes it between waves. Work around it in
   your edition only if the fix is obvious and local, and say so.
3. **Never run a repo-wide git command** — no `git checkout -- .`,
   `git restore`, `git stash`, `git clean`, `git reset`. On Biology Book 4 one
   such command destroyed every uncommitted change in the repo. To undo your
   own work, rewrite that specific file. **Never commit.** Read-only git
   (`git diff`, `git status`, `git log`) is fine.
4. **Shared tools are shared.** `tools/check_*_prose.py`, `tools/id_apply.py`,
   `tools/check_translation.sh`, `tools/termlink/*`, `styles/*`: report bugs
   instead of editing. The one exception is a per-language allow-list entry
   (`ALLOWED_BY_LANG[<lang>]` in `check_latin_prose.py`; `ALLOWED_WORDS` /
   `NOT_GATED` blocks in your script's own gate), **append-only, with a
   comment giving the reason and your edition**. An agent that rewords correct
   prose to satisfy a gate has found a gate bug: report it.
5. **Scratch files go in your PRIVATE directory**
   `/tmp/claude-1000/-home-bvirrion-repositories-one-course/feac20f7-0cd2-44ca-b426-7fa9b98b173b/scratchpad/<lang><N>/`
   (e.g. `fr1/`, `hi2/`). Four agents share the parent folder; a file named
   `p/07.patch` there will be overwritten by someone else's.
6. **Resource caps** (the machine is the user's 19 GB laptop):
   - every LaTeX build and every long job is wrapped:
     `systemd-run --user --scope -q -p MemoryHigh=3G -p MemoryMax=5G nice -n 19 latexmk -g <entry>.tex`;
   - one build at a time, never `make`, never `make -j`, never a build of a
     book that is not yours; `OMP_NUM_THREADS=1` for anything numeric;
   - prefer `\input`-ing a single chapter into a probe for overfull work
     (seconds) over a full book build (minutes).
7. **Never name a programme** (no "PCSI", "seconde", "ESO", "vwo", …); a
   school-stage noun for the reader's age is fine.
8. **Labels never translate**: `\label`, `\cref`/`\ref` targets,
   `\begin{solution}{key}`, the first argument of `\omterm`, file names,
   image paths, TikZ node names, colours, styles.

## Chemistry conventions for the editions (new in this series)

- **Every `\ce{…}`, `\chemfig{…}`, `\ghs{…}`, `\omperiodictable[…]` and
  `\schemestart…\schemestop` scheme is byte-identical to English**, state
  symbols included: `(aq)`, `(s)`, `(l)`, `(g)` stay as IUPAC writes them in
  every language. `id_apply.py` refuses a write that changes one (class
  `chem`), and `check_translation.sh` gate 12 checks the same on disk after
  every later edit. Never reach for `!chem`.
- **Orbital letters in math stay**: `3\text{d}^{10}`, `4\text{s}^2` are
  notation, not prose, even though the math census blanks `\text{}`.
- **Scheme arrow labels that are words are visible text and are
  translated**: `\arrow{->[slow]}`, `\arrow{->[fast][\ce{-H+}]}`,
  `\arrow{->[pyridine]}`, `\arrow{->[heterolysis]}`, `\arrow{->[1,2-shift]}`
  (all nine sites are in `bachelor-1` chapters 18, 19, 20, 22, 23, 25). The
  `chem` census blanks a label that holds no macro and no `$`, so translating
  it is legal; a label holding `\ce{…}` or math stays frozen. **Settled
  form for a non-ASCII label: see "Probe results" below.**
- **`% ledger: <id>, …` comments are kept on their line**, unchanged: every
  printed number for a real substance is traced to a sourced ledger row
  through them. Gate 12 compares the id multiset with the English twin.
- **Substance names follow the target language's IUPAC usage** (French
  *chlorure de sodium*, *acide éthanoïque*; Spanish *cloruro de sodio*;
  Portuguese *cloreto de sódio*; Dutch *natriumchloride*; Indonesian
  *natrium klorida*; Hindi and Arabic: the established school/university
  chemistry terms of those languages, see your style card and the
  standard references; IUPAC affixes and stereodescriptors such as
  *cis/trans*, *E/Z*, *R/S*, *syn/anti*, *ortho/meta/para*, *tert*, *-ène*
  are written as the target language's chemistry texts write them).
- **The four chemistry boxes** (`recall`, `inthelab[title]`,
  `history[title]`, `safety{pictos}`) carry translatable optional titles; the
  `safety` argument is a list of GHS codes and stays.
- **Glassware `\pic` arguments** (`beaker={…}{…}`, `meter={pH}`, …) are
  colours, levels and symbols: unchanged. Translate only node text.
- **`\foreach` label lists carry visible words and are compared byte for
  byte by `id_apply`'s `draw` census**, so translating one costs an
  `@@ N-M !draw` opt-out on that range (allowed; record each in the score
  file). The lists in this run (file:line in English):
  - `grade-5/01-irreversible-changes.tex` 95, 105, 139
  - `grade-5/02-raw-materials-and-recycling.tex` 148
  - `grade-7/01-identifying-substances.tex` 335
  - `grade-9/03-acids-bases-ph.tex` 67
  - `grade-9/04-metals-acids-corrosion.tex` 38
  - `grade-11/01-absorbance.tex` 42 (colour names in the list: translate the
    visible ones only)
  - `grade-12/01-proton-nmr.tex` 183
  - `grade-12/08-buffers-predominance.tex` 142
  - `grade-12/11-synthesis-strategy.tex` 312, 316
  pgfplots string keys (`xticklabels=`, `symbolic x coords=`) are blanked by
  the census and are translated freely — but **`symbolic x coords` cannot hold
  non-ASCII**: keep the ASCII keys and add a translated `xticklabels=`.
  Translatable keys in this run: `grade-4/01` 134, `grade-11/09` 244,
  `grade-12/11` 231, `bachelor-1/02` 216 (ordinals), `bachelor-1/26` 244
  (country names).

## The pipeline (as in the biology runs)

1. **Write every body through `tools/id_apply.py`** — the translator writes
   only prose, as line-range replacements of the English twin; unnamed lines
   are copied byte-identically, and the write is refused unless labels,
   environments, solution keys, `\emph`/`\index` adjacency, math spans,
   chemistry spans, drawing code, image paths, delimiters and braces match.
   Read its docstring. Line numbers refer to the English file with `\omterm`
   unwrapped (`python3 -c "import sys; sys.path.insert(0,'tools'); import id_apply as a; print(a.unwrap_omterm(open(F).read()))"`).
   **Do not machine-translate**: draft at native register directly.
2. **Build with `-g` every time a translated file has been created since the
   last build**, then check
   `grep -o 'parts/[^ ]*/<lang>/[^ ]*' build/<entry>.fls | sort -u | wc -l`
   equals the files on disk.
3. **Gates**: `bash tools/check_translation.sh <year> <lang>` for every year
   of your book. Gates 1–11 as in biology, plus **12** (chemistry twin:
   `\ce`/`\chemfig`/scheme sequence and `% ledger:` ids) and **13** (every
   reaction balances). Build log: `grep -ac '^!'`, `grep -aci undefined`,
   `grep -ac Overfull` all **0**, `grep -ac nullfont` equal to the English
   baseline (below), `grep -ac 'invalid in math mode'` 0. Use `grep -a`.
4. **Term links**: curate `book<N>_<lang>.py`, then
   `python3 tools/link_defined_terms.py --book N --lang <lang> --unwrap --apply`
   and `--apply`; then the per-target **frequency** and **chapter-set**
   censuses from `translation_instruction.md` (both — each is blind where the
   other sees), the target-set diff against English, the `\index{}` key diff
   against English, the `\text{}` census over **course and solutions**.
   English homograph hot spots to start from: *solution* (of an exercise vs
   the mixture), *table*, *group*, *period*, *family*, *shell*, *base*,
   *cell*, *charge*, *yield*, *phase*, *indicator*, *element*, *compound*,
   *bond*, *species*, *activity*, *configuration*, *hydration*, *reduction*,
   *order*. Your language has its own: find them with the two censuses.
5. **Native pass** until ≥ 95/100: openings, definitions, exercise stems,
   solution headers; **measure the instruction register** of your exercise
   stems against the same language's shipped biology twin before scoring
   (Book 1 against `../one-biology-book/parts/grade-*/<lang>/`, Book 2 against
   `../one-biology-book/parts/bachelor-1/<lang>/`) and convert as a reviewed
   pass, not a regex.
6. **A scripted re-read of every solution against its question**, in your
   language, before you score: the English writing run found 25 and 24
   numerical slips in Books 2 and 4 this way. Report English-canon slips to
   the coordinator; never "fix" a number silently.
7. **Last, measure — do not edit after measuring.** Re-run the line-edge
   sweeps (`['’]\s*$`, `^\s*([.,;:)?!]|~[;:?!])`, `[a-zà-ÿ]-\s*$`) after the
   final file lands, re-link, re-run both censuses, the dry run
   `python3 tools/link_defined_terms.py --book N --lang <lang> | grep 'links to insert'`
   (must print 0), every gate, then the forced build.
8. **Score** to `translation_scores/book_<N>/<lang>/translation_score.md`
   (model: `../one-biology-book/translation_scores/book_5/fr/translation_score.md`).
   Ship only at **≥ 95**.

## Your report to the coordinator (final message)

Pages; `\omterm` links and distinct targets, and the targets English reaches
that you do not (with English's own count for each); every gate's result; the
build-log numbers; the `.fls` count; your score; **every English-canon defect
you suspect** (file, line, evidence); **every gate or tool bug** (including
any allow-list entry you appended, with its reason); every `!draw` range.

## English baselines (measured 2026-10-04, after the pre-run canon fixes)

| | Book 1 | Book 2 |
|---|---:|---:|
| files (body + solutions) | 49 + 49 | 29 + 29 |
| pages (English PDF) | 432 | 293 |
| `\omterm` links | 5,775 | 2,471 |
| distinct link targets | 172 | 144 |
| `\index{}` | 301 | 364 |
| `\emph{}` | 369 | 390 |
| `\qty{}` | 2,196 | 1,474 |
| `\ce{}` | 2,267 | 3,433 |
| `nullfont` in the build log | 0 | 0 |
| linker dry run, links to insert | 0 | 0 |

Targets English itself never links (so not a gap in your edition): Book 1 11,
Book 2 23 definitions — the link census lists them; do not chase them.

## Pre-run canon fixes (coordinator, 2026-10-04)

- 31 line-broken `\index{}` keys joined onto one line in 23 files (gate 5
  would have failed every edition); whitespace-normalised key multiset and the
  `\index` count verified unchanged, no line now starts with punctuation, the
  English link layer still idempotent.
- `\qty{…}{days}` → `\qty{…}{d}` at 5 sites in `bachelor-1/08-rate-laws`
  (course and solutions), as the rest of the series writes it.
- Audited and clean: TeX accent escapes (0), English words in unit arguments
  (0 after the fix), defined-twice terms (0).

## Toolchain added for this run (coordinator, 2026-10-04)

Ported from `one-biology-book`: fonts (`assets/fonts/`, static Arabic and
Devanagari faces), `styles/lang/{fr,nl,es,pt,hi,ar,id}.tex`,
`tools/term_config/lang_*.py`, `id_apply.py`, `check_translation.sh`, the four
prose gates, `check_orphan_lines.py`, `check_term_display_drift.py`; 14 entry
files, registered in `latexmkrc` and `release.yml`; `LANGS` opened for Books
1–2. New for chemistry:

- `id_apply.py` class **`chem`**;
- `tools/check_chem_twin.py` (gate 12) and `check_ce_balance.py` (gate 13) in
  `check_translation.sh`; gate 4's environment census now counts `recall`,
  `inthelab`, `history`, `safety`, `axis` and `tabular` too;
- `check_hindi_prose.py` (inherited by `check_indonesian_prose.py`) and
  `check_arabic_prose.py`: `\ce`, `\chemfig`, `\ghs`, `\chemmove`, `\omorbs`,
  `\setchemfig`, `\polymerdelim`, `\cip`, `\tdplotsetmaincoords` arguments are
  not prose; `\irpanel`/`\nmrpanel` titles are; a chemistry-nomenclature
  allow-list (*cis, trans, syn, anti, meso, ortho, meta, para, tert, endo,
  exo, ene, yne, ane, oic, IUPAC, VSEPR, LCAO, LUMO, HPLC, TLC, NMR, pKa…*);
- `check_latin_prose.py`: chemistry markup stripped before counting words; a
  `\foreach` list whose every field is a number or an xcolor expression is
  not text;
- `check_indonesian_prose.py`: a chemistry block of English words that are
  not Indonesian (*chloride, oxide, ethanol, ammonia, solvent, mixture,
  covalent, …*), validated silent on every shipped biology `id` tree —
  *magnesium*, *aluminium*, *tetrahedral* and *anode* fired there and were
  removed, being Indonesian too.

Every gate was validated on both controls: it fires on an English tree
passed off as a translation, and it is silent on the shipped biology
editions of its language.

## Probe results (scaffolding builds against the still-English bodies)

Built 2026-10-04 with every body still English (so overfull counts there are
English text in another language's typesetting and mean nothing):

- `fr` (pdfTeX, babel french): Book 1 432 pp, Book 2 293 pp, 0 errors,
  0 undefined, nullfont 0. The Latin-script editions need no infrastructure
  change.
- `hi` (XeLaTeX): died "TeX capacity exceeded [main memory size=5000000]" on
  a pgfplots axis — `latexmkrc` raised pdfTeX's memory but not XeTeX's. Fixed
  in `latexmkrc` (same `-cnf-line` limits as pdflatex).
- `ar` (LuaLaTeX, babel `bidi=basic`): **an inline `\ce` equation was laid out
  right to left** — `\ce{2H2 + O2 -> 2H2O}` printed as `2H2O ⟶ O2 + 2H2`,
  arrow still pointing right, i.e. a wrong equation; state-symbol brackets
  mirrored; chemfig schemes ran right to left and lost their arrows. Fixed in
  `styles/onechemistry.sty` (Arabic block after `\omorbs`): every text-mode
  `\ce` is wrapped in `\babelsublr`, every scheme in a babel LTR group closed
  from chemfig's internal `\CF_schemestop`. Verified on a rendered page.
  **Arabic agents: still check one rendered page per chapter that has
  equations — direction bugs never reach the log.**
- After both fixes, every engine builds both books on the English bodies with
  0 errors, 0 undefined, nullfont 0: `hi` Book 1 448 pp / Book 2 305 pp,
  `ar` Book 1 455 pp / Book 2 306 pp; their overfull boxes are all
  `in paragraph` (English prose in a foreign face, which reflows on
  translation). The Book 2 `ar` SN1 page was checked by eye: schemes LTR with
  every arrow, inline equations in order.
- **Settled form for a non-ASCII scheme arrow label**: write the word directly,
  `\arrow{->[lente]}`, `\arrow{->[मंद]}`, `\arrow{->[بطيئة]}` — a chemfig arrow
  label is TikZ node text, typeset in text mode, and all three engines render
  it (probed). Never put non-ASCII inside `\ce{…}`, `\qty{}`, `\unit{}` or
  `\num{}`: those are math mode.
