# Translation run — One Chemistry Books 3 and 4 into fr, nl, es, pt, hi, ar, id

The binding run file for the fourteen language editions of Book 3
(University Chemistry, Year 2, `parts/bachelor-2`, 35 chapters + 35 solution
files = **70 files**, prefix `b2`) and Book 4 (University Chemistry, Year 3,
`parts/bachelor-3`, 33 + 33 = **66 files**, prefix `b3`). Mind the offset:
**Book 3 is `bachelor-2`, Book 4 is `bachelor-3`.** User request, 2026-10-06:
one subagent per book-and-language edition, **batches of at most six** (this
replaces the "four at a time" rule of `translation_instruction.md` for this
run only).

If you are an edition agent, this file and your brief are your instructions.
Read everything in "Reading list" before you write a line. The Books 1–2 run
file `sources/TRANSLATION_BOOKS_1-2.md` is the detailed procedure; this file
says what is different for Books 3–4 and **wins where they disagree**.

## Waves

| Wave | Editions | Notes |
|---|---|---|
| 1 | B3 `fr` `nl` `es` `pt` + B4 `fr` `nl` | first readers of both canons; the two French editions become the same-book sense twins |
| 2 | B3 `hi` `ar` `id` + B4 `es` `pt` | inherit both fixed canons and the French twins |
| 3 | B4 `hi` `ar` `id` | each inherits its own language's Book 3 findings (Arabic RTL above all) |

Between waves the coordinator re-measures every delivered edition on its own
forced build, verifies and fixes reported canon defects (propagating each fix
into the editions already delivered), fixes gate bugs, re-measures the English
baselines and writes `sources/WAVE<n>_FINDINGS_B34.md`. **Every agent reads
every findings file that exists when it starts** — the three Books 1–2 files
and any `_B34` file.

## Reading list (in this order, whole files)

1. `../CLAUDE.md` (workspace root) and `../book_style.md`.
2. `../translation_instruction.md` — **the whole file** (it is long; read all
   of it). Nearly every paragraph is a defect class some earlier edition
   shipped; its section "Lessons from the first chemistry translations" is
   about this repository.
3. Your language's style card: `../hindi_style_card.md`,
   `../arabic_style_card.md` or `../indonesian_style_card.md`. The Latin four
   have none: your **own language's Book 2 edition** (below) is your style
   reference.
4. `CLAUDE.md` and `CONTRIBUTING.md` of this repo (`one-chemistry-book/`),
   including its "Language editions" section.
5. `sources/TRANSLATION_BOOKS_1-2.md`, then `sources/WAVE1_FINDINGS.md`,
   `WAVE2_FINDINGS.md`, `WAVE3_FINDINGS.md` — they all apply to you.
6. This file, then any `sources/WAVE<n>_FINDINGS_B34.md`.

## Your reference editions (read before drafting)

- **Your language's Book 2 edition** — `parts/bachelor-1/<lang>/`,
  `parts/bachelor-1/solutions/<lang>/`, `tools/term_config/book2_<lang>.py`
  and `translation_scores/book_2/<lang>/translation_score.md`. Books 2–4 are
  one university course: **a term Book 2 already rendered keeps Book 2's
  rendering** (cross-book term ownership: `sources/SERIES_DEFINITIONS.md`),
  and your register (instruction mood of exercise stems, pronoun, how a
  definition opens, solution headers) is measured against it before scoring.
  If you think a Book 2 rendering is wrong, report it; do not diverge silently.
- **The same book's French edition** (wave 2–3 agents; B3 `fr`, B4 `fr` are
  written in wave 1) — sense and structure reference, not the ceiling.
- Arabic agents: the shipped `parts/bachelor-1/ar/` and `grade-*/ar/` are the
  worked examples of every right-to-left idiom (313 `\babelsublr`, 181
  `\foreignlanguage{arabic}` in Book 2 alone). The Books 1–2 Arabic agents'
  scratch scripts no longer exist; `grep` the shipped sources instead.

## Hard rules (all binding)

1. **You own exactly one edition.** You write only:
   - `parts/<year>/<lang>/*.tex` and `parts/<year>/solutions/<lang>/*.tex`
     for your book's year (`bachelor-2` for Book 3, `bachelor-3` for Book 4);
   - `tools/term_config/book<N>_<lang>.py` (a stub is waiting — curate it from
     YOUR edition's harvest, never by translating `book<N>_en.py`, never by
     copying another book's config; you may and should carry over the
     **language-level** homograph knowledge of `book2_<lang>.py`, re-verified
     against your own harvest, since a seeded entry is another book's
     judgement);
   - `translation_scores/book_<N>/<lang>/translation_score.md`;
   - `frontmatter/image-credits-book<N>.<lang>.tex` (an English stand-in now:
     translate it, keeping every photograph credit, author name and licence
     exactly; model: `frontmatter/image-credits-book2.<lang>.tex`);
   - your entry file's `\bookline` and `\author` lines only, if you want to
     improve the coordinator's wording.
   The preface (`frontmatter/preface.<lang>.tex`) and `styles/lang/<lang>.tex`
   are shared with Books 1–2 and are **not** yours: report anything wrong.
2. **Never edit the English canon** (`parts/<year>/*.tex`, `solutions/*.tex`)
   and never another language's files. A canon defect is REPORTED, with file,
   line and your evidence; the coordinator verifies it against the book's own
   model and fixes it between waves. Work around it in your edition only if
   the fix is obvious and local, and say so.
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
   comment giving the reason and your edition**, placed BEFORE any
   `if __name__ == "__main__"` guard, and run once to confirm it changed the
   output. An agent that rewords correct prose to satisfy a gate has found a
   gate bug: report it.
5. **Scratch files go in your PRIVATE directory**
   `/tmp/claude-1000/-home-bvirrion-repositories-one-course/3842d0ca-1447-4ff8-bf74-685e028c827c/scratchpad/<lang><N>/`
   (e.g. `fr3/`, `ar4/`). Six agents share the parent folder; a file named
   `p/07.patch` there will be overwritten by someone else's. Keep your patch
   files: they are the only record of a chapter before `id_apply` writes it.
6. **Resources** (the machine is the user's 19 GB laptop, six agents at once):
   - **every full-book build goes through the shared wrapper**
     `bash /tmp/claude-1000/-home-bvirrion-repositories-one-course/3842d0ca-1447-4ff8-bf74-685e028c827c/scratchpad/build.sh <entry>`
     — it forces `-g`, holds one of three machine-wide build slots (waiting
     for a free one), caps memory, and prints pages / errors / undefined /
     overfull / nullfont / Missing character / invalid-in-math. A build takes
     several minutes, more when it queues: **run it with
     `run_in_background`**. Never call `latexmk` on a whole book directly,
     never `make`, never build a book that is not yours;
   - for overfull work, `\input` a single chapter into a probe of the book's
     preamble (seconds) instead of rebuilding the book;
   - every other long job: `nice -n 19`, `OMP_NUM_THREADS=1`, one at a time.
7. **Never name a programme** (no "PCSI", "PC*", "licence 3", "L3", "ESO",
   "vwo", …) in visible text; a school-stage noun for the reader's age is
   fine. The part titles come from `styles/lang/<lang>.tex` already.
8. **Labels never translate**: `\label`, `\cref`/`\Cref`/`\ref` targets,
   `\begin{solution}{key}`, the first argument of `\omterm`, file names,
   image paths, TikZ node names, colours, styles.

## Chemistry conventions (as in Books 1–2, plus what is new here)

Everything in the Books 1–2 run file's "Chemistry conventions" section holds:
every `\ce{…}`, `\chemfig{…}`, `\ghs{…}`, `\omperiodictable[…]`, scheme is
byte-identical (state symbols included); `% ledger:` comments stay on their
line and **outside your replaced ranges**; substance names follow the target
language's IUPAC usage; the four chemistry boxes carry translatable titles;
decimal point, never a comma; accented `\index` keys get an ASCII sort key
(`\index{acido@ácido}`); `\cref{sec:…}` stays as English (the lang file
supplies the word); `DROP` (not `STOP`) for bare strong/weak adjectives.

**New notation in Books 3–4 (coordinator, 2026-10-06), and who owns it:**

- `\termsym{3}{P}{2}` (term symbols, 31 in Book 4) and `\kv{V}{O}{…}`
  (Kröger–Vink) are mathematics written in running text, outside every math
  span: `id_apply`'s `chem` census and gate 12 now freeze them like a formula.
- `MOdiagram` (modiagram: `\atom[N]{left}{ 2s = {0;pair}, … }`) is drawing
  code: `id_apply`'s `draw` census compares it, and every prose gate now skips
  it (the hi/ar/id gates fired on *left, pair, up* before). Nothing in it is
  prose; the atom names in `[…]` are element symbols or `\ce{}`.
- `omchartable` (character tables, Book 4 ch. 04) is mathematics: every gate
  skips it. Copy it byte-identically.
- `$\text{\DH}$` is the dispersity symbol Đ (Book 3 ch. 29), not a word:
  keep it.
- `\hartree`, `\bohr` (siunitx units), `\iu`, `\eu` (upright i and e) are
  notation.
- **Unit names inside `\qty`/`\unit`**: the only English word left is the unit
  name `einstein` (a mole of photons, Book 4 ch. 14, 6 sites) — it is a unit
  name, kept as is in every language. Never put a non-ASCII character inside
  `\qty{}`, `\unit{}`, `\num{}` or `\ce{}`.
- `\addlegendentry{…}` and `\legend{…}` are visible text (44 in Book 4, 10 in
  Book 3); `id_apply` blanks them, so translate them freely.

**Scheme arrow labels that are words are translated** (the `chem` census
blanks a label holding no macro and no `$`; a label holding `\ce{}` or math
stays frozen). Book 3: 21/71 *syn addition*; 24/79, 81, 88, 155; 25/164, 172
(*heat, base*); 26/164, 237 (*base*, *Michael*), 243 (*aldol*), 245; 27/78, 84.
Book 4: 14/213 (*via* in a math label: frozen), 219, 226; 23/74, 83;
27/280 (frozen part), 374 (*peroxy acid*, *Baeyer–Villiger*). Write non-ASCII
labels directly (`\arrow{->[addition]}`, `\arrow{->[योग]}`, `\arrow{->[إضافة]}`).

**Drawing-code text** — `\foreach` label lists are compared byte for byte by
`id_apply`'s `draw` census, so translating one costs `@@ N-M !draw` on that
range (allowed; record each in the score file). English file:line:

- Book 3 (`bachelor-2`): 08/61 (*pure metal, mixture, one solid first…*);
  19/240 (colour names — translate the visible `\n` field only, never the
  colour keys); 20/131–135 (cycle step names); 23/187–188 (*warm*,
  *activated*); 24/201 (*acyl chloride, anhydride, ester…*); 31/78 (*start,
  later, end*).
- Book 4 (`bachelor-3`): 05/271 (*symmetric stretch, bend…*); 08/315 (*one
  pulse, inversion recovery, spin echo*); 09/77 (*cubic P/I/F*); 22/126
  (*metal, semiconductor, insulator*); 24/106 (*deoxy, high spin, oxy, low
  spin*); 26/179 (*disrotatory, conrotatory, kept*); 26/362 (*Cope, Claisen*:
  names — usually unchanged); 33/413 (*elimination, substitution…*).
- Not text (leave alone): B3 17/308 (`endo`/`exo` keys — check whether the
  picture prints them), 23/59–66 (formulas), 32/49 and B4 20/363 (colours).
- pgfplots string keys are blanked by the census and translated freely:
  B3 33/67 `yticklabels`; B4 31/114, 122 `xticklabels`. `symbolic x coords`
  cannot hold non-ASCII: keep ASCII keys and add a translated `xticklabels=`.
- TikZ `label={…:TEXT}` text is visible and no gate extracts it: check yours.

## The pipeline (as in Books 1–2)

1. **Write every body through `tools/id_apply.py`** (read its docstring):
   prose only, as line-range replacements of the English twin; unnamed lines
   are copied byte-identically. Line numbers refer to the English file with
   `\omterm` unwrapped. **Do not machine-translate**: draft at native
   university register directly.
2. **Build with the wrapper** (`build.sh`, forced) every time a translated
   file has been created since the last build, then check
   `grep -o 'parts/bachelor-[23]/\(solutions/\)\?<lang>/[^ ]*' build/<entry>.fls | sort -u | wc -l`
   equals the files on disk.
3. **Gates**: `bash tools/check_translation.sh <year> <lang>` (gates 1–13).
   Build: 0 errors, 0 undefined, 0 overfull, nullfont = English baseline (B3 0, B4 17),
   0 "invalid in math mode", "Missing character" = baseline (B3 0, B4 17 for
   the Latin editions; B3 3, B4 23 for hi/ar — see "Probe results").
4. **Term links**: curate `book<N>_<lang>.py`, then
   `python3 tools/link_defined_terms.py --book N --lang <lang> --unwrap --apply`
   and `--apply`; then the **frequency** and **chapter-set** censuses of
   `translation_instruction.md` (both), the target-set diff against English,
   the `\index{}` key diff against English, the `\text{}` census over course
   **and** solutions. Book-3/4 homograph hot spots in English to start from:
   *fragment*, *variance*, *propagation*, *initiation*, *selectivity*,
   *resolution*, *retention*, *character* (of a representation / "π
   character"), *population*, *hole*, *migration*, *order*, *activity*,
   *phase*, *state*, *term*, *band*, *cell*, *field*, *shift*, *coupling*,
   *transition*, *yield*, *control*, *strong/weak* — see
   `tools/term_config/book3_en.py`/`book4_en.py` for how English handled each;
   your language has its own.
5. **Native pass** until ≥ 95/100; **measure the instruction register** of your
   exercise stems against your language's Book 2 edition before scoring.
6. **A scripted re-read of every solution against its question**, in your
   language, before you score. Report English-canon slips; never "fix" a
   number silently.
7. **Last, measure — do not edit after measuring.** Line-edge sweeps
   (`['’]\s*$`, `^\s*([.,;:)?!]|~[;:?!])`, `[a-zà-ÿ]-\s*$`) after the final
   file lands; re-link; both censuses; the dry run
   `python3 tools/link_defined_terms.py --book N --lang <lang> | grep 'links to insert'`
   (must print 0); every gate; then the forced build.
8. **Score** to `translation_scores/book_<N>/<lang>/translation_score.md`
   (model: `translation_scores/book_2/<lang>/translation_score.md`). Ship only
   at **≥ 95**.

## Your report to the coordinator (final message)

Pages; `\omterm` links and distinct targets, and the targets English reaches
that you do not (with English's own count for each); every gate's result; the
build-log numbers; the `.fls` count; your score; **every English-canon defect
you suspect** (file, line, evidence); **every gate or tool bug** (including any
allow-list entry you appended, with its reason); every `!draw` range; any Book 2
rendering you think is wrong.

## English baselines (measured 2026-10-06, after the pre-run canon fixes)

| | Book 3 (`bachelor-2`) | Book 4 (`bachelor-3`) |
|---|---:|---:|
| files (body + solutions) | 35 + 35 | 33 + 33 |
| pages (English PDF) | 373 | 405 |
| `\omterm` links | 1,733 | 1,632 |
| distinct link targets | 179 | 252 |
| definitions (`def:` labels) | 197 | 323 |
| `\index{}` | 417 | 675 |
| `\emph{}` | 429 | 677 |
| `\qty{}` | 1,858 | 1,995 |
| `\ce{}` | 2,102 | 1,657 |
| `nullfont` in the build log | 0 | 17 (see below) |
| linker dry run, links to insert | 0 | 0 |

Definitions English itself never links (Book 3: 18, Book 4: 71) are not gaps
in your edition: the link census lists them; do not chase them.

## Pre-run canon fixes (coordinator, 2026-10-06)

- 38 TeX accent escapes → UTF-8 in Book 3 (`H\"uckel` ×27, `Schr\"oder`,
  `Schr\"odinger`, `H\'eroult`, `Kekul\'e`, `Heyrovsk\'y`, `Sch\"ollkopf`);
  the link layer was unchanged (`--check` clean).
- 119 line-broken `\index{}` keys joined onto one line in 57 files; the whitespace-normalised key multiset and the `\index`
  count verified unchanged per file, no line now starts with punctuation, the
  English link layer still idempotent. **Line numbers moved**: always work
  from the current English file.
- English words frozen inside `\ce{}` removed: the Wilkinson cycle of B3 20
  and B4 21 wrote `(alkene)`, `(alkyl)`, `alkene + H2 -> alkane` inside `\ce`;
  now `RCH=CH2`, `CH2CH2R`, `\ce{RCH=CH2 + H2 -> RCH2CH3}` (balanced).
- English words inside unit arguments removed: `\qty{…}{years}` (B3
  solutions 12, two sites → `4.2~years`, `$… = 34$~years`);
  `cm^3.molecule^{-1}.s^{-1}` (B4 12/515 and 14/565 → `cm^3.s^{-1}` with
  "per molecule" / "concentrations being counted per cm³" in prose).
- "the values of the ledger the band was built from" (B4 06/293, the ledger is
  internal and never named in prose) → "the values the band was built from".
- `\qty{…}{\AA}` → `\qty{…}{\angstrom}` at 8 sites (B4 12/138, 144; 19/509 ×2;
  20/353, 529 ×2, 530): `\AA` is a text accent macro, invalid in siunitx's math
  mode, and the Å was silently dropped from the printed page ("Command \r
  invalid in math mode", exit 0). `\AA` in pgfplots axis labels and running
  text is text mode and correct: keep it there.
- Audited and clean: `\cref`/`\Cref` prefixes all have a `\crefname`
  (`ch, thm, def, ex, exo, met, pb, prop, rem, sec`); linker dry run 0 for
  both books.

## Toolchain changes for this run (coordinator, 2026-10-06)

- Infrastructure: 14 entry files (registered in `latexmkrc` and
  `release.yml`), `LANGS` opened for Books 3–4 in `tools/termlink/books.py`,
  14 term-config stubs (with the chemfig-settings, arrow-label and tick-label
  protect patterns every Books 1–2 edition needed), 14 image-credits
  stand-ins, the edition directories.
- `id_apply.py`: `MOdiagram` joins the `draw` census; `\termsym`/`\kv` join
  the `chem` census (so gate 12 checks them on disk too).
- `check_hindi_prose.py` (and so `check_indonesian_prose.py`),
  `check_arabic_prose.py`, `check_latin_prose.py`, `check_orphan_lines.py`:
  `MOdiagram` is drawing code, `omchartable` is mathematics.
- Validated on a fixture holding every `MOdiagram` and `omchartable` block of
  both books plus `\termsym` and `\DH` sentences in fr/hi/ar/id prose (every
  gate silent; a tampered `\termsym` is caught by gate 12), and the full
  `check_translation.sh` sweep stays green on all 91 shipped Books 1–2
  year × language combinations.

## Probe results (scaffolding builds against the still-English bodies)

**English, forced builds 2026-10-06 (after the fixes above):** Book 3 373 pp,
Book 4 405 pp, both 0 errors / 0 undefined / 0 overfull / 0 "invalid in math
mode"; pdfTeX peaks at ~120 MB.

**Book 4's baseline is `nullfont` 17 and "Missing character" 17, and both are
harmless**: they are the 17 contour levels of the `contour prepared` plot in
chapter 12 (the H + H₂ potential-energy surface), each of which makes pgfplots
set one backtick in nullfont. Nothing is meant to print there. **Gate on
"equal to 17, all of them `` ` `` in nullfont", not on 0** — also for hi/ar,
where any OTHER "Missing character" line is a real loss (a glyph the face
lacks). Book 3's baseline is 0 for both.

**Engine probes against the still-English bodies (2026-10-06)**: every engine
builds both books with 0 errors and 0 undefined — `hi` (XeLaTeX) Book 3 389 pp,
Book 4 425 pp; `ar` (LuaLaTeX) Book 3 389 pp, Book 4 428 pp; peak memory well
under the wrapper's cap. Their overfull boxes (hi 54/48, ar 136/124) are all
`in paragraph` — English prose in a foreign face — and none is `detected at
line`. What the probes found, all fixed before wave 2:

- **Glyphs the Noto faces lack, dropped from the page with exit 0**: `‰`
  (`\textperthousand`, B4 ch. 11) — the style now takes it from Latin Modern
  for hi/ar; `²`/`³` typed as Unicode superscripts in prose (B4 12/386, now
  `sp$^3$`); `\textmu` in prose (B4 17/308, now `\qty{1}{\micro m}`). Never
  type a Unicode superscript, `µ`, `‰` or another symbol in prose: write the
  macro or the math. **Read every "Missing character" line of your log.**
- **The hi/ar "Missing character" baseline is not 0**: Book 3 **3**, Book 4
  **23** — the 17 nullfont backticks above, plus invisible control codes
  (U+000A newline: B3 3, B4 5; one U+007F in B4 ch. 27) that pgfplots/TikZ
  pass to the text face. Any OTHER line (a real glyph) is a defect. The
Latin-script editions use the pdfTeX path the English books use; local TeX
Live has no french/spanish/dutch `.ldf` (Book 1–2 finding), so a local fr/es/nl
build hyphenates with English patterns and CI's overfull count can differ.

## Run complete (2026-10-07)

All fourteen editions delivered and verified by the coordinator's own forced
builds (0 errors / 0 undefined / 0 overfull, baselines as above, `.fls` 70 per
Book 3 edition and 66 per Book 4 edition); `check_translation.sh` green on all
105 year × language combinations of the series; every linker dry run 0. Scores:
96/100 each, Arabic 95 (both books). Per-edition numbers are in the repo
`CLAUDE.md` ("Language editions"); what each wave found in
`WAVE1_FINDINGS_B34.md` and `WAVE2_FINDINGS_B34.md`. Wave 3 (Book 4 hi, ar, id)
needed no findings file of its own: its canon defects (solutions/32 0.083,
solutions/02 2047.98, ch. 4 *indistinguishable* links) and the Arabic
inline-array mirroring were fixed by the coordinator and carried into every
edition, and are recorded in the score-file addenda and the repo `CLAUDE.md`.
