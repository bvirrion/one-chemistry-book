# Translation score: One Chemistry Book 1, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 1 (grades 1–12), `one_chemistry_book_1_school_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland textbook usage |
| **Overall score** | **88 / 100**, sampled: 24 passages, seed 1 (2 per grade), not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script (all), contact sheets read by eye |
| **Date** | 2026-11-18 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 374 calls (translation, retries and repairs); glossary, infrastructure and coordinator `claude-opus-5-5` (Opus 5.5), one coordinator for the whole physics + chemistry run, no subagents |
| **Canon** | English as committed; no English edit. |
| **Tokens** | Haiku: 374 calls, about $2.5 list price (per year in `draft/pilot-grade-*-zh/post.log`, line `all:`). Coordinator: shared with the run; weekly plan (all models) 14 % at this book's close (`sources/TRANSLATION_BOOKS_1-4_ZH.md`) |
| **Scope** | 49 chapters + 49 solution files under `parts/grade-{1..12}/zh/` and `parts/grade-{1..12}/solutions/zh/`; glossary `sources/GLOSSARY_BOOK_1_ZH.md`; term config `tools/term_config/book1_zh.py` |

## Verdict

Natural mainland schoolbook Chinese: warm, short sentences in the young grades (两种液体也可以混合, 糖浆与水用肉眼已无法
分辨), the plain textbook register from grade 7 (气体 X 能使带火星的木条复燃, 能使澄清石灰水变浑浊 — the standard
school phrasing). Chemistry terms are the standard ones (均相/非均相, 限量反应物, 交错式/重叠式构象, 盐桥, 滴定剂). Weak
points: a few literal turns (沸腾温度 where 沸点 is usual), some long sentences in English clause order. No sentence in the
sample was wrong in sense.

## Build and gates

- `build/one_chemistry_book_1_school_zh.pdf`: 407 pp (English 432, French 451). XeLaTeX + xeCJK, Fandol.
  Errors 0, undefined 0, overfull 0, nullfont 0, missing character 0. TeX Live 2026.
- `tools/check_translation.sh grade-N zh` and `tools/gates.sh grade-N`: PASSED for N = 1…12.
- `link_defined_terms.py --book 1 --lang zh --check`: every file matches. 7,109 links to 170 targets (English 5,773 to
  172). The surplus (+23 %, as in the physics books) is real occurrences: Chinese repeats 原子, 电子, 分子, 溶解 where
  English uses a pronoun. Not reached or under-reached: one-character terms the CJK linker cannot link (醛 aldehyde,
  酮 ketone, 酶 enzyme: 51 English links), and *oxidation/reduction* (氧化/还原 are dropped: they sit inside compound
  names, 二氧化碳, 氧化铜, and made 80 wrong links); `Z 异构体` and `pH 试纸` (Latin + Han, ~10 occurrences) do not link.
- `pdfsweep.py` against the French PDF: 3 English-only word types left, all intended (HDPE, LDPE, *One Physics Book*).
- `figcheck.py lint`: 0 label collisions; the 78 captioned figures read on contact sheets.

## What was read

- Text: 24 passages (seed 1), the sweep, number and PDF-sweep reports, every gate hit.
- Numbers: every `numtrace.py` difference traced (`draft/zh/numtrace-grade-*.log`): number words written as digits
  (three water molecules → 3 个水分子, Twelve electrons → 12 个电子), 460 million tonnes → 4.6 亿吨, a number repeated
  for clarity (不会超过 7, 低于 6.1 为 \ce{CO2}); none lost.

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| `\foreach` / symbolic-axis / macro labels in English | ~20 lists | `{0/{a blanket: no oxygen}/1,…}`, `{0/singlet/{1},…}`, `{methyl red}`, `\cube{…}{salt\\ …}` | by hand; `xticklabels=`/`yticklabels=`, keys kept |
| English labels `sites.py` does not report | 6 figures | multi-line `\foreach` lists whose items start on the next line, `\cube{…}{water\\…}` | found by `pdfsweep.py`, by hand |
| Naming table built on English endings | 1 table + 1 caption | `\emph{-ol}`, `\emph{-yl \ldots-oate}` | Chinese naming (某醇, 某酸某酯), caption rewritten for 乙酸乙酯 |
| pgfplots legends merged | 2 | `\legend{14 族（\ce{CH4}…）、15 族…}`, `\legend{\qty{100}{mL} 纯水，…}` | `, `; `legend` sweep rule now takes `、` and one brace level |
| Photo credit frames / names | 6 | `Photo GuidoB, CC BY-SA 3.0.`, `Paul Nadar 摄`, `NASA, ESA, J.~Hester and A.~Loll` | 照片：… frame; NOAA/Scripps institute names in Chinese |
| A line or title left in English | 4 | `crystals remain.`, `proportions.`, `[What iron needs to rust]`, `\num{8.36e24}$ molecules.` | `%` / by hand |
| English index key or lost sense | 2 | `\index{functional group}`; `\emph{符号}\index{符号}` (English `symbol of an atom`) | 官能团; 元素符号 |
| Roman numerals Latin Modern lacks | 6 missing chars | 铁（Ⅲ） | 铁（III） |
| Overfull lines (zh only) | 2 | a legend printed as one 147 pt entry; nylon example opening | legend split; sentence reordered |
| Over-linking against English's choices | ~980 links | 溶液 378 → *dissolve*, 元素 131 (English 3), 吸收带 77 (English 3), 氧化 inside compound names | `STOP`/`DROP` in `book1_zh.py`, mirroring `book1_en.py` |
| pgfplots tick labels merged by a full-width comma | 1 | grade 12 ch. 11 `xticklabels={加成，酯化，…}` printed one label (found at chemistry Book 2's close; PDF rebuilt 407 pp, 0/0/0) | `, `; the `legend` sweep rule now covers `[xy]ticklabels` |
| Stray `=` before a content line | 1 | grade 11: Haiku's `=` mark left before `\item`, printed as “=” (found at chemistry Book 2's close; PDF rebuilt 407 pp, 0/0/0) | `strayeq` sweep rule |

## Tooling this book added (run back over every later year)

- `tools/gates.sh`: `zh` excluded from the English duplicate-label scan (every `zh` label was reported duplicated).
- `tools/check_chinese_prose.py`: Latin element names (natrium, ferrum…), sibling series names (One Physics Book) and
  amino-acid codes in dipeptides (Gly--Ala) are not flagged.
- `common.visible()`: TikZ `key=number` and macro names are not words (`amplitude=1pt`, `(\a:0.55)` read as "a").
- `zh_sweeps.py`: `legend` takes `、` and one brace level; `fix_names` leaves photo credits alone (it had turned the
  photographer Stefan Andrej Shambora into 斯特藩 in physics Book 3, restored).
