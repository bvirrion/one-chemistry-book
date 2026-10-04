# Wave 3 findings — Book 2 nl, es, pt, hi (2026-10-04)

Read after the run file and `WAVE1_FINDINGS.md`, `WAVE2_FINDINGS.md`; where
they disagree, this file wins.

## Delivered (coordinator re-measured each on a forced `-g` build)

| Book 2 | pages | `\omterm` links | targets | 0/0/0 | `.fls` | score |
|---|---:|---:|---:|---|---:|---:|
| en | 293 | 2,462 | 144 | yes | — | — |
| fr | 305 | 2,715 | 149 | yes | 58 | 96 |
| nl | 302 | 2,493 | 146 | yes | 58 | 96 |
| es | 304 | 2,591 | 146 | yes | 58 | 96 |
| pt | 300 | 2,587 | 146 | yes | 58 | 96 |
| hi | 287 | 2,670 | 145 | yes | 58 | 96 |

Every edition reaches every English target.

## Shared fixes made during wave 3 — they apply to you

1. **`\cref{sec:…}` printed the English word "Section" in every edition**
   (no `\crefname{section}` in the style). Fixed: `\omnameSection(s)` in each
   `styles/lang/<lang>.tex` (Arabic reference form القسم, Indonesian
   *Subbab*). **Keep `\cref{sec:…}` exactly as English** — never hand-write the
   word plus `\ref`.
2. **A non-Latin scheme arrow label failed gate 12**: `id_apply`'s blanking only
   recognised Latin letters, so `->[मंद]` was compared byte for byte. Fixed: a
   label with any non-ASCII character and no `\` or `$` is blanked too.
   Translate the nine word labels directly (`->[بطيئة]`, `->[lambat]`) — no
   `--force-classes chem`.
3. **δ± inside `\ce` vanished in the Unicode-face editions** (Noto Sans
   Devanagari and Noto Naskh Arabic have no Greek; chemgreek used text Greek):
   the style now selects chemgreek's `default` (math Greek) mapping for hi/ar.
   Expect 0 "Missing character" lines; report any.
4. Part titles' `\textsuperscript` wrapped in `\texorpdfstring` (fr/es/pt
   bookmarks).

## Book 2 English canon changes since wave 2 (translate the current text)

- **Figures (drawing code: copy byte-identically, only node text is yours):**
  `08` tangent label now `anchor=west` at `(axis cs:2,0.12)`; `09` "B (steady
  state dashed)" at `(axis cs:2,0.22)`; `17` both NMR formula labels
  `anchor=north`, centred over an empty stretch; `18` and `25` the worded
  scheme arrows lengthened (`\arrow{->[…]}[,1.5]`), so a longer translated
  label no longer needs abbreviating.
- **Link layer**: the zinc anode *blocks* of ch. 14, "three groups *block* it"
  (ch. 19), an induction *period* (ch. 9), "makes the electron exchange
  *quantitative*" (ch. 13) and "*quantitative* measurement" (ch. 15) no longer
  link. Protect your renderings of the same sites (all four Latin editions and
  Hindi needed it).

## Term-layer lessons from wave 3

- Every agent needed `DROP` (not only `STOP`) for the bare strong/weak
  adjectives (*fort/faible*, *sterk/zwak*, *fuerte/débil*, *forte/fraco*,
  प्रबल/दुर्बल) — STOP falls through to the chapter-local table.
- The repeated homographs of Book 2: **group** (only before a number),
  **block**, **period** (induction period), **network/lattice** (ice, silica),
  **multiplicity** (NMR vs cell), **activity** (optical vs thermodynamic),
  **hydration** (ions vs alkene), **axial/equatorial positions** (VSEPR vs
  chair), **protection** (protecting group vs personal), **quantitative**.
- Plurals the matcher cannot derive were added through `DERIVED` by every
  agent (Hindi: 138 forms, Spanish: 33). Arabic broken plurals need `EXTRA` or
  `DERIVED` from the start (the Arabic Book 1 agent's list is in
  `tools/term_config/book1_ar.py`).
- Two agents' `EXTRA_PROTECT` look-aheads broke on a second `--apply` once the
  neighbouring word was linked: allow an optional `\omterm{…}{` in them.

## Drawing code in Book 2

`!draw` was needed only for `16` EN line 199 (carvone `\foreach`) and `17` EN
line 68 (colour wheel). Orphaned weekend-problem headings at a page foot
(chapters 10, 15, 16, 26 in various editions) were fixed with a `\clearpage`
on a blank line before the heading — check yours on the rendered page.
