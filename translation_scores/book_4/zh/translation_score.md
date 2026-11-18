# Translation score: One Chemistry Book 4, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 4 (University Year 3), `one_chemistry_book_4_university_year_3_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland textbook usage |
| **Overall score** | **88 / 100**, sampled: 20 passages, seed 1, not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script (all), contact sheets read by eye |
| **Date** | 2026-11-18 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 482 calls (translation, retries and repairs); glossary, infrastructure and coordinator `claude-opus-5-5` (Opus 5.5), one coordinator for the whole physics + chemistry run, no subagents |
| **Canon** | English as committed; no English edit. Noted, not fixed: ch. 32's compartment figure writes `C_{soil}` (an English word in italic math), translated `C_{\text{土壤}}` in the Chinese edition |
| **Tokens** | Haiku: 482 calls, about $4.6 list price (`draft/pilot-bachelor-3-zh/post.log`, line `all:`). Coordinator: shared with the run; weekly plan (all models) 16 % at this book's close (`sources/TRANSLATION_BOOKS_1-4_ZH.md`) |
| **Scope** | 33 chapters + 33 solution files under `parts/bachelor-3/zh/` and `parts/bachelor-3/solutions/zh/`; glossary `sources/GLOSSARY_BOOK_4_ZH.md`; term config `tools/term_config/book4_zh.py` |

## Verdict

Correct third-year university register (厄米算符, 本征函数, 势能面, 配分函数, 自旋–自旋弛豫, 生物电子等排体, 罗宾逊成环,
维兰德–米舍尔酮, 化学需氧量, 科研诚信). Weak points: a few long sentences in English clause order. No sentence in the
sample was wrong in sense.

## Build and gates

- `build/one_chemistry_book_4_university_year_3_zh.pdf`: 370 pp (English 405, French 431). XeLaTeX + xeCJK, Fandol.
  Errors 0, undefined 0, overfull 0, nullfont 0; missing character 1, the invisible U+007F the `hi`/`ar` editions of
  this book also log (25 before the fixes below). TeX Live 2026.
- `tools/check_translation.sh bachelor-3 zh` and `tools/gates.sh bachelor-3`: PASSED.
- `link_defined_terms.py --book 4 --lang zh --check`: every file matches. 2,379 links to 279 targets (English 1,632 to
  253). Not reached: *E-factor* (17 English links; `E 因子` is Latin + Han), *Norrish* (2), and three targets English
  links once (*junction*, *BET*, *zeta*). The surplus is mostly correct-sense repetition (吸附, 三重态, 基组).
- `pdfsweep.py` against the French PDF: left, all intended: LCAO and the GHS's English title.
- `figcheck.py lint`: one collision found and fixed (below); the 79 captioned figures read on contact sheets.

## What was read

- Text: 20 passages (seed 1), the sweep, number and PDF-sweep reports, every gate hit.
- Numbers: every `numtrace.py` difference traced (`draft/zh/numtrace-bachelor-3.log`): decades written 20 世纪 N0 年代,
  150 million tonnes → 1.5 亿吨, number words as digits; none lost.

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| Characters the fonts lack | 24 missing | 吡啶鎓, 噁唑, 菲啰啉; `$面式$` (a Han word in math went to Latin Modern) | 吡啶正离子, 恶唑, 菲咯啉; 面式 as text |
| Figure labels expanded or translated against English | 3 figures | Jablonski diagram IC/ISC → 内转换/系间窜越 (collided); `$\to$ HBr` → 溴化氢; metallocene names over their formulas | abbreviations and formula restored; names on their own line |
| `\foreach` labels in English | 9 lists | vibrational modes, pulse sequences, cubic P/I/F, metal/semiconductor/insulator, hazard-control pyramid, Cope/Claisen | translated by hand (an item with 、 braced) |
| English subscripts | 3 | `(\text{ruby})`, `(\text{zeolite})`, `C_{soil}` | 红宝石, 沸石, 土壤 |
| English index keys | 3 | `\index{瑞利 scattering}`, `\index{斯托克斯 line}` | 瑞利散射, 斯托克斯线 |
| Names and words left in Latin | ~12 | Hessian, Brusselator, Sato, Dhara, Simmons--史密斯, *Silent Spring*, `net`, `mean`, *ipso*, "normalisation" | 黑塞, 布鲁塞尔振子, 佐藤, 达拉, 西蒙斯–史密斯, 《寂静的春天》, 净反应, 平均, 本位 |
| fac/mer | ch. 5, 19, 20 | `fac-`, `$fac$` | 面式/经式 |
| Wrong-sense link | 1 | 热带 (hot band) inside 加热带有 | `EXTRA_PROTECT` |
| Index keys copying the term where English indexes another | 3 | ch. 15 `\emph{电化学可逆}\index{电化学可逆}` (English *electrochemically reversible system*) | 电化学可逆体系, 准可逆体系, 电化学不可逆体系 |

## Tooling this book added

- None beyond Book 3's (`onium` extension, credit blanking).
