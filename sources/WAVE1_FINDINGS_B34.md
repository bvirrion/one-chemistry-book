# Wave 1 findings — Book 3 fr, nl, es, pt and Book 4 fr, nl (2026-10-06)

Read after `sources/TRANSLATION_BOOKS_3-4.md` (and the Books 1–2 WAVE files it
lists); where they disagree, this file wins.

## Delivered (coordinator re-measured each on its own forced build)

| | pages | `\omterm` links | targets | 0/0/0, nullfont | `.fls` | score |
|---|---:|---:|---:|---|---:|---:|
| Book 3 en | 373 | 1,733 | 179 | 0 | — | — |
| Book 3 fr | 391 | 1,816 | 184 | yes, 0 | 70 | 96 |
| Book 3 nl | 387 | 1,638 | 180 | yes, 0 | 70 | 96 |
| Book 3 es | 389 | 1,781 | 183 | yes, 0 | 70 | 96 |
| Book 3 pt | 381 | 1,785 | 182 | yes, 0 | 70 | 96 |
| Book 4 en | 405 | 1,632 | 252 | 17 (baseline) | — | — |
| Book 4 nl | 424 | 1,538 | 259 | yes, 17 | 66 | 96 |
| Book 4 fr | 431 | 1,778 | 258 | yes, 17 | 66 | 96 |

Every edition reaches every English target. Dutch is lower in links because it
welds compounds the linker cannot enter (*gaschromatografie*,
*standaardvormingsgibbsenergie*): that is the language, not a defect. Targets
the editions reach and English never links (all checked, all correct sense):
*molécula objetivo / doelmolecuul* (retrosynthesis), *ventana*, formation
enthalpy, equilibrium shift; Book 4 nl *schrödingervergelijking*, activation
volume, chiral auxiliary, agostic interaction, spin crossover.

**The two French editions are the same-book sense twins for waves 2–3**
(Book 3 fr: `parts/bachelor-2/fr/`; Book 4 fr: `parts/bachelor-3/fr/`).

## English canon fixes (applied 2026-10-06, carried into every delivered edition)

All verified against the book's own numbers or chemistry before editing; no
line count changed. **Translate what is in the canon now.**

Book 3 (`bachelor-2`):

1. `solutions/11` problem item 7: carbon "pays about a third of the work" →
   "nearly half" (1.03/2.21 = 0.47).
2. `solutions/20` exercise 8: "18 with seven coordination positions" → "six".
3. `solutions/15` item 24: `$\boldsymbol{four}$` (an English word in math
   italic) → `\textbf{four}` — write `\textbf{<your word>}`.
4. `10-current-potential-curves` l.64–65: `\emph{counter electrode}` newline
   `\index{counter electrode}, which` printed "electrode ," — now joined.
   **General rule: never let a space or line break precede `\index{…}` when
   punctuation follows it** (LaTeX swallows the space only before a word).
   Check: `python3 -c "import re,glob;[print(f,t[:m.start()].count(chr(10))+1) for f in glob.glob('parts/bachelor-[23]/**/<lang>/*.tex',recursive=True) for t in [open(f).read()] for m in re.finditer(r'(?<=[^\s%])\s+\\\\index\{(?:[^{}]|\{[^{}]*\})*\}[,.;:)!?]',t)]"`
5. `32-mass-spec-atomic` exercise 8: pentan-3-one "shows no peak at 58" →
   "shows only a small peak at 58" (the solution explains its ¹³C peak).
6. `solutions/07` item 12: 0.456 → 0.455 (the solution's own item 4).
7. `solutions/01`: item 11 0.28 % → 0.29 %; 334.6 → 334.5 kJ at three sites
   (items 12, 13, 15 — the exact chain, not the rounded 55.5 mol).
8. `solutions/03` item 10: "about 1 % per 3 K" → "about 2 % per 3 K"
   (ΔCp(fus) ≈ 37.5 J/(K mol): 1.9 %).
9. `14-diatomic-mos` l.423: bond orders "2.5 and 2 against 3 and 2" →
   "2.5 and 2.5 against 3 and 2" (O₂⁺ is 2.5).
10. `23-amines` l.203–204: a line ending "(1,3,5-" printed
    "1,3,5- tribromobenzene"; the name is now on one line.
11. `solutions/17` exercise 4: the C≡N is "on one of the two ring carbons
    formed from the dienophile", not "next to" one.
12. `solutions/34` items 5 and 10: s_y/x printed as 0.00102 (was 0.0010) and
    "0.104 × 0.730" (was 0.102, which gives 0.075, not the printed 0.076).

Book 4 (`bachelor-3`):

13. `12-rate-theories` l.386: Unicode "sp³ to sp²" → `sp$^3$ to sp$^2$`
    (the hi/ar faces lack ² and ³).
14. `17-colloids` l.308: "1 nm to 1 \textmu m" → `\qty{1}{nm} to \qty{1}{\micro m}`.
15. `08-advanced-nmr` l.437–438: "two-" at a line end printed "two- dimensional".
16. `02-many-electron-atoms` l.396: A = 11.46 → **11.47** cm⁻¹ (17.20 × 2/3).
17. `solutions/08` weekend problem item 11 was garbled; now "Coupled methyls,
    hence two `\ce{CH3}` on adjacent carbons (a `\ce{CH3-CH3}` unit):
    impossible here." (the `\ce` sequence changed: gate 12 expects it).
18. `02-many-electron-atoms` l.363: carbon's interval ratio 1.64 → **1.65**
    (27.0/16.4; the solution already says 1.65).
19. `06-rovibrational-spectroscopy` l.290 and exercise 7 (l.456): R(0)
    2905.57 → **2905.58**. The band was built with ν₀ = 2885.31, so R(0) =
    2905.575; with .57, R(0) − P(2) = 62.63 contradicted the printed 62.64.
20. `solutions/10` exercise 1: "the numbers of oscillators holding 0, 1, 2, 3, 4
    quanta" → "the quanta held by the four oscillators, largest first" (the
    tuples are four numbers, one per oscillator).
21. `solutions/15` exercise 12 and problem item 13: b²S_xx 203.9 → **203.5**
    (0.919² × 241); the results 0.104 and 1.076 are unchanged.

Reported and NOT changed: Book 3 ch. 30 exercise 10 repeats ch. 24 exercise 11
(saponification value of triolein) — a repetition, not an error.

## Tool fixes during wave 1 (all lenient: they can only accept more)

- **Mixed scheme arrow labels** (`[then \ce{H2O}]`, `[\ce{H+} or \ce{HO-}]`,
  Book 4 `[singlet $\ce{CH2}…$]`): `id_apply` and gate 12 now compare only
  their `\ce{}` and `$…$` parts — **the words are prose: translate them.**
  Before, gates 10 and 12 contradicted each other there.
- **Arrow labels holding a brace group with brackets** (`[{[3,3]}, then]`,
  Book 4 ch. 29 EN 409) are now parsed; their words are prose.
- **`check_orphan_lines.py` (gate 10)** skips `\pgfplotsset`/`\tikzset`/
  `\setchemfig` bodies (pgf keys like "every axis plot" were flagged), and now
  checks a single `.tex` file instead of silently scanning nothing (exit 2 on
  an unusable path).
- **`id_apply`'s `NODE_TEXT`** now also blanks `\node at (x,y) [left] {text}`
  (options after the coordinate) — no `!draw` needed for those.

- **`check_orphan_lines.py`** gates *and*, *so*, *its* too (an untranslated
  "so" and "and" passed every gate in Book 4 fr; the census then found a live
  "so" in the shipped Book 1 French, now fixed), and skips `\chemmove` bodies
  (TikZ `controls … and …`).
- **Never run the linker or `id_apply` on a file while your build is running**:
  a build read a half-written chapter and died (Book 4 fr).

Known, not yet fixed (work around, report if it costs you): gate 9's word
tokeniser is ASCII-only (*Schröder* reads as *Schr* + *der*; three editions
allow-listed *van*, *der*); gate 9's duplicate-line class flags two legitimately
identical English solution lines (Book 4 solutions/05 items 13–14); gate 12
prints only the first divergence per file.

## Term-layer lessons

- **French homograph found by the chapter-set census**: *indices de liaison*
  is both the diatomic bond order (Book 3 ch. 14) and the Hückel π bond index
  (ch. 16, `def:b2:huckel:indices`); four ch. 16 links pointed at ch. 14.
  Check how YOUR language names the Hückel bond index.
- Homographs every Book 3 edition masked: *variance* (phase rule vs
  statistics), *propagation*, *initiation*, *selectivity*, *resolution*,
  *residue*, the TLC R_f, bare *fragment* (stoplisted as in English).
- High density that is NOT a collision: Book 4 *coverage* (nl 22 vs 4),
  *anharmonic*, *saddle*, *notebook*, *total synthesis*; Book 3 *metallurgy*
  (*lixiviación*), Kirchhoff's law.
- **An `EXTRA_PROTECT` pattern that consumes a `$` silently masks the whole
  following math span** and its links vanish with no error (Dutch Book 4):
  use a look-ahead for the `$`.
- Every Latin edition followed Book 2's house forms (Dutch lower-case eponym
  compounds: *diels-alderreactie*, *baeyer-villigeroxidatie*; orbital symbol
  first: *$\pi^*$-orbitaal*).

## Drawing code

`!draw` ranges every Book 3 Latin edition needed: 08/61, 19/240, 20/131–135,
23/187–188, 24/201, 31/78 (the run file's list was complete). Book 4 (nl):
05/271, 08/315, 09/77, 22/126, 24/106, 26/179, 33/413 from the list, plus
07/171–173 and 14/128 (labels moved to clear collisions) and 26/288–306
(now unnecessary after the `NODE_TEXT` fix). Figures that collided after
translation and were fixed by text only: B3 ch. 32 drift-tube label, ch. 35
extraction/wash labels, ch. 29 modulus-curve labels; B4 ch. 7 Franck–Condon,
ch. 14 funnel, ch. 31 LCA box. Orphaned weekend-problem headings: B3 ch. 13 and
21 in French (`\clearpage` + `\enlargethispage`). **Render and look at every
figure page whose text you translated.**
