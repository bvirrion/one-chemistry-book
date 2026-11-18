# Translation score: One Chemistry Book 2, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 2 (University Year 1), `one_chemistry_book_2_university_year_1_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland textbook usage |
| **Overall score** | **88 / 100**, sampled: 20 passages, seed 1, not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script (all), contact sheets read by eye |
| **Date** | 2026-11-18 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 355 calls (translation, retries and repairs); glossary, infrastructure and coordinator `claude-opus-5-5` (Opus 5.5), one coordinator for the whole physics + chemistry run, no subagents |
| **Canon** | English as committed; no English edit. |
| **Tokens** | Haiku: 355 calls, about $3.0 list price (`draft/pilot-bachelor-1-zh/post.log`, line `all:`). Coordinator: shared with the run; weekly plan (all models) 16 % at this book's close (`sources/TRANSLATION_BOOKS_1-4_ZH.md`) |
| **Scope** | 29 chapters + 29 solution files under `parts/bachelor-1/zh/` and `parts/bachelor-1/solutions/zh/`; glossary `sources/GLOSSARY_BOOK_2_ZH.md`; term config `tools/term_config/book2_zh.py` |

## Verdict

Correct first-year university register (试推导…, 由…给出, 在本阶段). Standard chemistry terms (价层电子对互斥, 杂化轨道,
定域/离域, 偏摩尔量, 速率决定步骤, 过渡态, 亲核取代, 消旋化, 格氏试剂). Weak points: some sentences keep English clause
order, and a few literal turns. No sentence in the sample was wrong in sense.

## Build and gates

- `build/one_chemistry_book_2_university_year_1_zh.pdf`: 269 pp (English 293). XeLaTeX + xeCJK, Fandol.
  Errors 0, undefined 0, overfull 0, nullfont 0, missing character 0. TeX Live 2026.
- `tools/check_translation.sh bachelor-1 zh` and `tools/gates.sh bachelor-1`: PASSED.
- `link_defined_terms.py --book 2 --lang zh --check`: every file matches. 3,318 links to 152 targets (English 2,462 to
  144). Not reached: *CIP* (4 English links) and *multiplicity* (1): Latin + Han terms the CJK linker cannot match.
- `pdfsweep.py` against the French PDF: left, all intended: SHE (the standard hydrogen electrode's symbol) and the GHS
  name.
- `figcheck.py lint`: 0 label collisions; the 51 captioned figures read on contact sheets.

## What was read

- Text: 20 passages (seed 1), the sweep, number and PDF-sweep reports, every gate hit.
- Numbers: every `numtrace.py` difference traced (`draft/zh/numtrace-bachelor-1.log`): number words as digits, "the
  Year 2 volume" → 本科二年级分册, numbers moved across a line by clause reordering; none lost.

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| Run-directory sweep | 229 lines | Latin names (59), short English lines (21), English titles (8), a line doubled across a break (5) | `zh_sweeps.py --run --fix` |
| English `\text{}` subscripts | several kinds | `V_{\text{flask}}`, `[\ce{Fe}]_{\text{dissolved}}`, `d_{\text{front}}` | 容量瓶, 移取, 溶解, 前沿 (fus/vap/trs kept: IUPAC) |
| `鎓` (onium) | all | 硝鎓离子: no TeX Live font has 鎓 (printed nothing) | 硝酰正离子, X正离子; new `onium` sweep rule, series card line |
| Roman numerals Ⅱ/Ⅲ missing | all | 铜(Ⅱ) from Haiku: not in Latin Modern | U+2160–216B declared a CJK class in `onechemistry.sty` and `onephysics.sty` |
| *ortho/meta/para* left in Latin | ch. 18 | `\textit{para} 位` | 邻位/间位/对位; new `omp` sweep rule |
| Stray `=` before a content line | 1 | Haiku's `=` before `\item`: the build failed | new `strayeq` sweep rule, run back over every closed year |
| A line doubled across a break | 2 | ch. 14 line 367, ch. 22 line 348 | removed |
| Overfull inline formula (zh only) | 1 | ch. 11, $\beta_4$ | `\allowbreak` |
| Over-linking / wrong sense | ~700 links | 构型 (also 电子构型, 几何构型), 屏蔽 (screening vs NMR shielding), 保护, 水合, 积分 (an integral), 基元 (inside 基元反应) | `STOP`, `EXTRA_PROTECT` in `book2_zh.py` |
| Coordinator error | 1 | a `\bedta\b` → EDTA replacement hit the ledger IDs in a comment | restored from English |

## Tooling this book added (run back over every later year)

- `zh_sweeps.py`: `foreachsep` (top-level 、/， in `\foreach … in {…}` → `, `), the `legend` rule extended to
  `[xyz]ticklabels`, `strayeq`, `percent` (`5%，` → `5\%，`), `omp`, `onium`.
- `langs/zh_names.py`: about 35 chemistry names (Schröder--van Laar, Lineweaver--Burk, Jahn--Teller, Brunauer…).
- `tools/check_chinese_prose.py`: IUPAC subscripts (fus, vap, trs) and spectroscopy acronyms are not flagged.
- `styles/onechemistry.sty`, `styles/onephysics.sty`: Roman numerals as CJK class.
