# Wave 2 findings — Book 3 hi, ar, id and Book 4 es, pt (2026-10-06/07)

Read after `sources/TRANSLATION_BOOKS_3-4.md` and `WAVE1_FINDINGS_B34.md`;
where they disagree, this file wins. Written for wave 3 (Book 4 hi, ar, id).

## Delivered (coordinator re-measured each on its own forced build)

| | pages | `\omterm` links | targets | 0/0/0 | Missing char. | `.fls` | score |
|---|---:|---:|---:|---|---:|---:|---:|
| Book 3 hi | 359 | 1,775 | 181 | yes | 3 (baseline) | 70 | 96 |
| Book 3 id | 388 | 1,836 | 184 | yes | 0 | 70 | 96 |
| Book 4 en | 405 | **1,634** | 252 | yes | 17 (baseline) | — | — |
| Book 4 fr | 431 | 1,778 | 258 | yes | 17 | 66 | 96 |
| Book 4 nl | 424 | 1,538 | 259 | yes | 17 | 66 | 96 |
| Book 4 es | 425 | 1,777 | 256 | yes | 17 | 66 | 96 |
| Book 4 pt | 419 | 1,753 | 258 | yes | 17 | 66 | 96 |

| Book 3 ar | 348 | 1,614 | 183 | yes | 3 (baseline) | 70 | 95 |

(Book 3 Arabic delivered after this table was first written; its section
"Arabic Book 3 — right-to-left findings" below is for the Book 4 ar agent.) **All four Book 4
Latin editions are your sense twins** (`parts/bachelor-3/{fr,nl,es,pt}/`);
your own language's Book 3 edition (`parts/bachelor-2/<lang>/`, delivered)
fixes the series terms you share with it.

## Book 4 English canon changes since `WAVE1_FINDINGS_B34.md`

Already in the canon you translate; listed so you know what changed:

1. `14-photochemistry` l.323: "a few parts per million" → "some fifteen parts
   per million" (6×10¹²/4×10¹⁷ = 1.5×10⁻⁵; the solution computes 14 ppm).
2. `30-total-synthesis` l.322–323: the garbled "the area that removes it only
   with its square of the size" → "grows only as the square of the size".
3. Figures (drawing code — copy byte-identically): ch. 11 the "$\frac32$:
   translation" node now sits at the right end of its dotted line
   (`anchor=south east] at (axis cs:2900,1.5)`, the H₂ curve crossed it);
   ch. 29 the pyridine NMR label moved to `(axis cs:7.1,3.0)` (it was clipped at
   the axis edge); ch. 18 the ruby/emerald minipages are `[b]` (labels touched
   the caption).
4. Link layer: English no longer links "indistinguishable" in its everyday
   senses (an orientation, ch. 10 l.246 and solutions l.89; two numerically
   equal sums, l.405) — only l.450 (molecules) and l.603 (quanta) are the
   quantum-indistinguishability definition. **Check yours.** And English now
   reaches `def:b3:complex-mechanisms:activation-volume` through "activation
   volume" (the definition is worded "volume of activation"): English 1,629 →
   1,634 links.
5. Every earlier Book 4 fix (1.65, R(0) = 2905.58, A = 11.47, 203.5, the
   oscillator wording, solutions/08 item 11, sp$^3$, `\qty{1}{\micro m}`,
   "two-dimensional") is listed in `WAVE1_FINDINGS_B34.md`.

## Book 3 English canon changes during wave 2 (carried into every Book 3 edition)

- `03-chemical-potential` l.81: `ylabel shift=10pt` (V̄₁ collided with the
  y-label).
- `solutions/20` exercise 5: benzyl's β carbon "is an aromatic ring carbon that
  carries no hydrogen" (it is the ipso carbon; the old text gave it a hydrogen).

## Style and tool changes during wave 2

- **Arabic: `MOdiagram` drew every MO diagram MIRRORED** (correlation lines
  flying off to the right, "*σ1" for σ*1s, side-by-side diagrams overlapping)
  with a clean log — modiagram's environment is not reached by the tikzpicture
  LTR hook. Fixed centrally in `styles/onechemistry.sty` (Arabic block:
  `env/MOdiagram/before|after` hooks). **No source wrap needed.** Book 4 has no
  `MOdiagram`, but the lesson holds for every drawing environment: check one
  rendered page per figure type with `pdftotext -bbox`.
- **Arabic entries** now carry `\setlength{\emergencystretch}{3em}` (Book 2's
  entry had it; the Books 3–4 entries were derived from English and lost it).
- **Arabic: a bare Latin word inside an Arabic TikZ/pgfplots node renders
  reversed** ("HOMO" → "OMOH"). Recipe, as in the shipped
  `parts/bachelor-1/ar/`: `\foreignlanguage{arabic}{…}` around the node text
  and `\babelsublr{…}` around each Latin word or digit run.
- `check_indonesian_prose.py`: narrow, commented exemptions appended by the
  Book 3 id agent (Gibbs's memoir title, *Popular Science Monthly*, Ox/Red-only
  math subscript runs, a lone `[west]` chemfig anchor). Validated: still fires
  6,679 times on an English tree, silent on every shipped `id` year.
- `check_hindi_prose.py`: `ALLOWED_WORDS` gained `west`, `dibal-h`,
  `icp-oes`, `icp-ms` (Book 3 hi agent). Its `LATIN_WORD` treats hyphenated
  tokens as one English word (*s-cis*, *d--d*, *HOMO--LUMO*): write the house
  form (`s-\textit{cis}`, d–d, "HOMO और LUMO") rather than allow-listing.

## Lessons from the wave-2 editions

- **Index after a line break before punctuation** printed "Curtius ," in
  Spanish ch. 27–28 (its own files): run the `\index` check from
  `WAVE1_FINDINGS_B34.md` after your last edit.
- Spanish found *producto directo* (the uncyclised product of a radical clock,
  ch. 27 l.173) linked to the group-theory **direct product**: a
  translation-only homograph. Look for yours.
- Hindi cleared its overfull boxes with group-local `\emergencystretch` on the
  offending solution or proof; Book 2 had re-flowed instead. Rewording is
  preferred; a local `\emergencystretch` is acceptable when rewording fails.
- **Never edit sources while your build is running** (two editions hit
  spurious "Runaway argument" failures doing so).
- `id_apply` accepts a patch range that swallows a `% ledger:` line (gate 12
  catches it on disk): keep ledger lines out of your ranges.

## Arabic Book 3 — right-to-left findings (for the Book 4 ar agent; read all)

The Arabic Book 3 agent's checking scripts are in its scratch folder
`scratchpad/ar3/` (`brack.py` scans a BUILT PDF for wrong-facing brackets,
`brackscan.py` the sources): copy them into your own `ar4/` and use them.

1. **Brackets face the wrong way at the edge of an Arabic TikZ node or pgfplots
   label** — «(مهبط(» — because the node box resolves to left-to-right and
   babel's `bidi=basic` has no paired-bracket rule. The cure that worked on 52
   nodes in 17 chapters: wrap the node text in `\shortstack{…}` (or
   `\shortstack[r]{…}`, not `[l]`), one `\foreignlanguage{arabic}{…}` per line.
   `tabular` also works but gate 4 counts it. A parenthetical split across `\\`
   lines still breaks: rephrase. **The shipped Book 1 Arabic edition has this
   defect** (p. 85 «فحم متوهج (كربون)», candidates pp. 213, 252, 373); Book 2
   Arabic avoided it by removing edge brackets from nodes.
2. **Latin words and multi-digit numbers inside Arabic node text or bare axis
   labels come out reversed**: `\babelsublr{…}` around each Latin run, the node
   text in `\foreignlanguage{arabic}{…}` (the Book 2 recipe). Wrapping digits in
   `\qty{}` in a figure node also works (the Book 3 edition did it 4 times).
3. **amsthm statement heads garble** when the statement body opens with `\[` or
   `\begin{center}`, or when the head note mixes Latin and math: add a short
   Arabic lead line («لدينا», or a lead sentence) before the display.
4. **A line ending in a standalone «و»** prints detached from the next word
   (233 sites in the first draft of Book 3, no gate sees it): keep «و» attached
   to its word, never at a line end. Sweep with
   `grep -nE '(^|\s)و\s*$' parts/bachelor-3/ar/*.tex parts/bachelor-3/solutions/ar/*.tex`.
5. `lang_ar.py`'s head pattern allows ONE proclitic before ال, so «فبال…»/«وبال…»
   never link: reword or add the form to `EXTRA`/`DERIVED`.
6. «باب» is printed as the chapter name (series-wide babel default, known, left
   for the user).
7. `check_arabic_prose.py` gained allow-list entries (`fac`, `mer`, `edta`,
   `dibal-h`, `icp`, `oes`, `ms`, `dept`, `pubchem`, the `[west]` scheme
   anchor).
8. **Check direction with `pdftotext -bbox`** on one rendered page per figure
   type, every scheme, and every table of numbers. Book 4 has many figures with
   Latin labels (spectra, Jablonski, Tanabe–Sugano, Pourbaix-like plots,
   crystal structures): budget for them.
