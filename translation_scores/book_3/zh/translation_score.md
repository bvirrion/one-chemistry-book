# Translation score: One Chemistry Book 3, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 3 (University Year 2), `one_chemistry_book_3_university_year_2_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland textbook usage |
| **Overall score** | **88 / 100**, sampled: 20 passages, seed 1, not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script (all), contact sheets read by eye |
| **Date** | 2026-11-18 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 494 calls (translation, retries and repairs); glossary, infrastructure and coordinator `claude-opus-5-5` (Opus 5.5), one coordinator for the whole physics + chemistry run, no subagents |
| **Canon** | English as committed; no English edit. |
| **Tokens** | Haiku: 494 calls, about $3.9 list price (`draft/pilot-bachelor-2-zh/post.log`, line `all:`). Coordinator: shared with the run; weekly plan (all models) 16 % at this book's close (`sources/TRANSLATION_BOOKS_1-4_ZH.md`) |
| **Scope** | 35 chapters + 35 solution files under `parts/bachelor-2/zh/` and `parts/bachelor-2/solutions/zh/`; credits `frontmatter/image-credits-book3.zh.tex`; glossary `sources/GLOSSARY_BOOK_3_ZH.md`; term config `tools/term_config/book3_zh.py` |

## Verdict

Correct second-year university register. Standard terms (偏摩尔焓, 低共熔混合物, 能斯特电势, 混合电势, 惠兰德中间体,
哈蒙德假设, 霍纳–沃兹沃思–埃蒙斯反应, 内标, 共振线). Clauses are reordered as Chinese needs. Weak points: some long
sentences in English clause order. No sentence in the sample was wrong in sense.

## Build and gates

- `build/one_chemistry_book_3_university_year_2_zh.pdf`: 341 pp (English 373, French 391). XeLaTeX + xeCJK, Fandol.
  Errors 0, undefined 0, overfull 0, nullfont 0, missing character 0 (18 before the 鏻/鎓 fix below). TeX Live 2026.
- `tools/check_translation.sh bachelor-2 zh` and `tools/gates.sh bachelor-2`: PASSED.
- `link_defined_terms.py --book 3 --lang zh --check`: every file matches. 2,267 links to 193 targets (English 1,811 to
  180). Every English target is reached.
- `pdfsweep.py` against the French PDF: left, all intended: LCAO, CSTR, CFSE, the LOD/LOQ subscripts, and Alexander
  Borodin's name in the credits.
- `figcheck.py lint`: 0 label collisions; the 84 captioned figures read on contact sheets.

## What was read

- Text: 20 passages (seed 1), the sweep, number and PDF-sweep reports, every gate hit.
- Numbers: every `numtrace.py` difference traced (`draft/zh/numtrace-bachelor-2.log`): number words as digits, decades
  (the 1930s → 20 世纪 30 年代), 150 million → 1.5 亿, one lost: ch. 35 "more than 99 %" for benzoate, restored.

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| Characters Fandol lacks | 18 missing | 鏻盐 (phosphonium salt), 咪唑鎓 | 季磷盐, 苄基三苯基氯化磷; 咪唑正离子; `onium` sweep rule extended |
| `\foreach` labels in English | 5 lists | `{0/pure metal, 9/{mixture, one solid first},…}`, colour wheel, acyl derivatives, TLC stages, catalytic-cycle steps | translated by hand |
| chemfig arrow labels in English | 3 | `\arrow{->[proton transfer]}`, `[addition]`, `[elimination]` | 质子转移, 加成, 消除 |
| English `\text{}`/`\mathrm{}` subscripts | ~15 | `\text{gas}`, `\text{heat}`, `\text{eq}`, `T_{\text{ext}}`, `s_{\mathrm{blank}}` | g, 热, 平衡, 外, 空白 (LOD/LOQ kept) |
| English index keys | 11 | `\emph{质谱法}\index{mass spectrometry}` (ch. 32) | key = the Chinese term |
| fac/mer, IUPAC names in English forms | ch. 18 + solutions | `fac 异构体`, `but-1-en-2-ol`; the ligand-naming list taught English endings (-o, -ate) | 面式/经式; 丁-1-烯-2-醇; the list rewritten for Chinese naming (氯, 氰, 某酸) |
| Photo credits and titles | ~12 | `Wikimedia Commons`, `Les Prix Nobel`, `\emph{Studies in Chemical Dynamics}`, *Popular Science Monthly* | 维基共享资源, 诺贝尔奖年鉴, 《化学动力学研究》, 《大众科学月刊》 |
| A line or word left in English | 4 | `given by $…$`, "Explain the lemon", Fenske | removed; 柠檬汁的作用; 芬斯克 |
| Over-linking / wrong sense | ~50 links | 循环 on every catalytic cycle, 片段 on mass-spectrum fragments, 酰基 alone, 自由度 in statistics (ch. 34) | `STOP`, `EXTRA_PROTECT` in `book3_zh.py`, as English protects *variance* |

## Tooling this book added (run back over every later year)

- `zh_sweeps.py` `onium`: also 鎓 alone (吡啶鎓), 鏻 → 磷 (季磷盐), 噁 → 恶, 啰 → 咯; series card and glossaries updated.
- `tools/check_chinese_prose.py`: the credit blanking takes 摄影：, 图片：, 肖像：, 照片来源： and 照片由, over a line
  break, up to ）/。/brace; `\emph{…}\index{English}` pairs fixed by script (key = the Chinese term).
