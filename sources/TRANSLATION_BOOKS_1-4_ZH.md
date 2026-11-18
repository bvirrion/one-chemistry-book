# Run file — One Chemistry Book 1–4 in Simplified Chinese (`zh`), pilot method

Scope: Books 1–4 (15 years: grade-1 … grade-12 in Book 1, bachelor-1 … bachelor-3) into Simplified Chinese (mainland), by the pilot method (`../pilot_translation_instruction.md`).
Started 2026-11-18, one run with physics Books 1–5 and chemistry Books 1–4 (run 2 of 2 (after physics; the usage table is kept in the physics run file)).

| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section; glossary and coordinator `claude-opus-5-5` (Opus 5.5) |
|---|---|

Shape (user, 2026-11-18): one coordinator (the main session), no subagents, one session for both series; at most three
years (`run.py` jobs) at once and at most 9 Haiku calls in flight (`--workers 3` each; spare workers go to the last
jobs). **Pause rule for this run: pause and report at +25 points of the weekly plan** from the run's start (9 %, so at
34 %; points before and after a weekly reset are added). Order: physics Books 1–5, then chemistry Books 1–4.

## Usage readings (`claude -p /usage`, all models, current week)

| When | Week used |
|---|---:|
| Run start, 2026-11-18 00:25 | 9 % |
| Chemistry Book 1 closed, 2026-11-18 07:40 | 14 % (physics Books 1–5 closed by then; bachelor-1/2/3 translating) |
| Chemistry Book 2 closed, 2026-11-18 10:15 | 16 % (Books 3–4 at their close, building) |
| Chemistry Books 3–4 closed, run closed, 2026-11-18 10:40 | 16 % (+7 points for the nine books and both ports) |

## Infrastructure (step 0)

- Ported 2026-11-18 from physics/math: `latexmkrc` (`_zh` → XeLaTeX with the raised memory flags, upmendex pinyin
  index), `styles/zh-pinyin.ist`, the `zh` block of `styles/onechemistry.sty` (xeCJK + Fandol, `\crefname{section}` 节,
  `\ifom@chinese\om@unicodefacetrue` so chemgreek takes math Greek: without it δ was missing 96 times), `styles/lang/zh.tex`
  (box names, PT legend, siunitx range/list phrases in `\text{}`), four entry files, preface, CJK term linker, gate 14
  (`check_chinese_prose.py`), `id_apply.py` zh dispatch. Book 2 with English fallbacks: 296 pp, 0/0/0, missing characters 0.
- Glossaries `sources/GLOSSARY_BOOK_{1..4}_ZH.md` (new lines only, ~290/257/400/640), merged after the five physics
  glossaries by `draft/zh/merge_glossary.py N` (1,362 / 1,619 / 2,021 / 2,661 lines), split per year.
- Trial (`draft/zh-trial.sh`): grade-11 ch. 07 (redox, 154 `\ce`) and bachelor-1 ch. 03 (Lewis/VSEPR, 196 `\ce`), run in a
  slot freed from the physics queue (the queue list is cut to physics until the trial ends, then restored).

## Open defects (kept on disk, cleared as fixed)

- None open. (The English placeholder credits pages were translated at 05:32, see below.)

## Per-book log

### Trial results (2026-11-18)

- grade-11 ch. 07 (redox, 154 `\ce`): 10 Haiku calls, $0.08 list, 0 rejected in pass 1. Probe 10 pp, 0 errors, 0 overfull,
  nullfont 0, missing characters 0. Every NUMDIFF is a number word written as a digit (四 → 4 个). Gate: `\text{(氧化)}` in
  a math array → new zh_sweeps rule `textparen` (full-width brackets). Pages read at 60 dpi: `\ce` beside Han, figure node
  text, `inthelab`/`safety` boxes with GHS codes all right.
- English canon note (not fixed, not a translation defect): `\omterm{def:g9:inside-the-atom:nucleus}{electrons}` links
  "electrons" to the nucleus definition (grade-11 ch. 07 and solutions); check whether g9 defines electron there.
- bachelor-1 ch. 03 (Lewis/resonance/VSEPR, 196 `\ce`): 13 calls, $0.10 list, 0 rejected in pass 1. Probe 10 pp, 0/0, nullfont 0,
  missing 0. NUMDIFF: ordinals as Chinese numerals (period 2 → 第二周期, grade 10 → 十年级), standard usage, accepted. Gate:
  plain-text formulas the English writes outside `\ce` (`HCl 1.09, HBr 0.83`) → both gates now skip a word made only of
  element symbols. Pages at 60 dpi: VSEPR definitions, ball-and-stick figures and exercise boxes right.
- Chemistry years appended to the physics queue (`one-physics-book/draft/zh-queue3.list`) after physics bachelor-3.

### Credits pages (2026-11-18 05:32, Haiku 5.5, 4 calls via `draft/zh/credits.sh`)

Installed in `frontmatter/image-credits{,-book2,-book3,-book4}.zh.tex` after reading each against English. Fixed by
hand: authors transliterated in Books 1 and 4 (维尔纳·舍尔曼 → Werner Schellmann; a CC BY attribution keeps the name as
published, as the physics credits do; subjects such as 约翰·道尔顿 stay Chinese); Book 3 left "public domain" and
"Wikimedia Commons" in English (→ 公有领域, 维基共享资源, as the other three) and the GHS's full English name (→
全球化学品统一分类和标签制度（GHS）).

### Chemistry Book 1 (grades 1–12) — closed 2026-11-18 07:40

Model: `claude-haiku-5-5` effort medium, 374 calls, about $2.5; coordinator Opus 5.5. Score 88 (pilot tier), 407 pp
(en 432, fr 451), 0/0/0, missing characters 0, `check_translation.sh` and `gates.sh` green for all 12 grades,
7,109 links / 170 targets (en 5,773 / 172). Score file `translation_scores/book_1/zh/translation_score.md`.

- Every section accepted by Haiku except grade-11 ch. 03 §3 (TikZ code read as English; `common.visible()` fixed,
  saved unchanged). Step 5 (post/repair/post) ran as queue `cmd` lines.
- About 20 `oreach` / symbolic-axis / `\cube` label lists translated by hand; `sites.py` misses a multi-line
  `oreach` list whose items start on the next line and a label passed as a macro argument (`\cube{…}{salt\…}`):
  six figures found only by `pdfsweep.py`. Keep the PDF sweep as the last word on figure text.
- The grade-11 naming table taught English endings (`-ol`, `-yl …-oate`): rewritten for Chinese naming (某醇, 某酸某酯),
  and its caption.
- Two legends merged by Haiku's list separators (、 and ，inside `\qty`): the `legend` sweep rule and the gate's legend
  exemption now take `、` and one brace level (both repos). One more found the same way in physics Book 4 (fixed, rebuilt).
- 铁（Ⅱ）/（Ⅲ）: U+2161/2162 are missing from Latin Modern; written (II)/(III).
- `tools/gates.sh` reported every `zh` label as duplicated (its language list predates `zh`); `zh` added.
- Link calibration (`book1_zh.py`): STOP mirrors `book1_en.py` (溶液, 材料, 物体, 符号, 生成物, 产物, 周期, 加成, 取代,
  容量) plus 化学式, 元素; DROP 氧化/还原 (they sit inside compound names, 二氧化碳, 80 wrong links) and 吸收带.
  One-character terms (醛, 酮, 酶) cannot link; `Z 异构体`, `pH 试纸` (Latin + Han) do not link through `EXTRA` either.

### Chemistry Book 2 (University Year 1) — closed 2026-11-18 10:15

Model: `claude-haiku-5-5` effort medium, 355 calls, about $3.0; coordinator Opus 5.5. Score 88 (pilot tier), 269 pp
(en 293), 0/0/0, missing characters 0, `check_translation.sh` and `gates.sh bachelor-1` green, 3,318 links / 152
targets (en 2,462 / 144). Score file `translation_scores/book_2/zh/translation_score.md`.

- The physics queue script marked bachelor-1 done while sections were still rejected (its running process held the old
  check, see the physics run file): retried by hand.
- New defect classes, each now a `zh_sweeps.py` rule run back over every closed year of both series: `\foreach` lists
  and `[xyz]ticklabels` split on 、/， (`foreachsep`, `legend`); Haiku's `=` mark left before a content line, which
  broke the build here (`strayeq`); `5%，` eating the line as a comment (`percent`); `\textit{para}` (`omp`).
- 鎓 is in no TeX Live font: written X正离子 (硝酰正离子), `onium` rule and a series-card line. Ⅰ–Ⅻ (U+2160–216B)
  declared a CJK class in both style files, so Haiku's 铜(Ⅱ) prints.
- Wrong-sense links stopped in `book2_zh.py`: 屏蔽, 保护, 水合, 积分, 基元 (STOP), 构型 outside stereochemistry
  (`EXTRA_PROTECT`).
- Coordinator slip: a global `EDTA` replacement rewrote ledger ids in a comment; restored from English before the
  ledger gate ran.
- Hits in the closed math `zh` books for the new rules: listed in the physics run file, not fixed.

### Chemistry Book 3 (University Year 2) — closed 2026-11-18 10:40

Model: `claude-haiku-5-5` effort medium, 494 calls, about $3.9; coordinator Opus 5.5. Score 88 (pilot tier), 341 pp
(en 373, fr 391), 0/0/0, missing characters 0, `check_translation.sh` and `gates.sh bachelor-2` green, 2,267 links / 193
targets (en 1,811 / 180). Score file `translation_scores/book_3/zh/translation_score.md`.

- Fandol lacks 鏻 (phosphonium): 18 missing characters at the first build. Written 季磷盐 / 苄基三苯基氯化磷 (the
  trade names), and the `onium` rule now also takes 鎓 alone, 鏻, 噁 and 啰 (see Book 4).
- The ch. 18 naming list taught the English ligand endings (-o, -ate): rewritten for Chinese naming.
- Link calibration: STOP 循环 (the recycle loop vs every catalytic cycle), 片段 (as English stops *fragment*), 酰基;
  `EXTRA_PROTECT` for the statistical 自由度 in ch. 34, as English protects *variance*.
- The prose gate's credit blanking now takes 摄影：, 图片：, 肖像：, 照片来源： and 照片由 over a line break.

### Chemistry Book 4 (University Year 3) — closed 2026-11-18 10:40

Model: `claude-haiku-5-5` effort medium, 482 calls, about $4.6; coordinator Opus 5.5. Score 88 (pilot tier), 370 pp
(en 405, fr 431), 0/0/0, missing characters 1 (the invisible U+007F the `hi`/`ar` editions also log),
`check_translation.sh` and `gates.sh bachelor-3` green, 2,379 links / 279 targets (en 1,632 / 253). Score file
`translation_scores/book_4/zh/translation_score.md`.

- 25 missing characters at the first build: 鎓, 噁 (噁唑, 二噁英), 啰 (菲啰啉) and `$面式$` (a Han word inside math).
- Haiku expanded the Jablonski diagram's IC/ISC into 内转换/系间窜越, which collided (found by `figcheck.py lint`), and
  wrote HBr as 溴化氢 in a scheme: English's abbreviations and formulas restored.
- English canon noted, not fixed: `C_{soil}` in the ch. 32 compartment figure.

## Run closed (2026-11-18 10:40)

All four chemistry books and all five physics books ship in `zh` (pilot tier 88 each), uncommitted. The run took the
weekly plan from 9 % to 16 %: +7 points for nine books and two series ports, against the +25 pause rule. `release.yml`
carries the four `_zh` entries. Lessons in `../pilot_translation_instruction.md` ("Lessons from the physics and
chemistry run"); porting notes in `../translation_instruction.md` (CJK checklist). Not done: the HTML reader.
