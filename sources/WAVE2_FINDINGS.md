# Wave 2 findings — Book 1 hi, ar, id and Book 2 fr (2026-10-04)

Read after `sources/TRANSLATION_BOOKS_1-2.md` and `sources/WAVE1_FINDINGS.md`;
where they disagree, this file wins.

## Delivered (coordinator re-measured each on a forced `-g` build)

| | pages | `\omterm` links | targets | 0/0/0, nullfont 0 | `.fls` | score |
|---|---:|---:|---:|---|---:|---:|
| Book 1 en | 432 | 5,773 | 172 | yes | — | — |
| Book 1 hi | 425 | 5,957 | 174 | yes | 98 | 96 |
| Book 1 id | 450 | 6,308 | 174 | yes | 98 | 96 |
| Book 1 ar | 418 | 5,341 | 166 | yes | 98 | 95 |
| Book 2 en | 293 | 2,470 | 144 | yes | — | — |
| Book 2 fr | 305 | 2,716 | 149 | yes | 58 | 96 |

## Book 2 English canon fixes (applied 2026-10-04, carried into Book 2 fr)

Found by the French Book 2 agent, each verified before editing. **Wave 3 and 4
agents translate the corrected text; the French Book 2 edition is your
same-book sense twin.**

1. `solutions/04` exo: "Water weakens the attraction 42 times" → **41**
   (78.4/1.89 = 41.5; problem item 8 of the same chapter already says 41).
2. **"day" inside unit arguments**: `\qty{…}{day^{-1}}` ×6 and
   `\unit{day^{-1}}` ×1 in `08-rate-laws` (course and solutions) → `d^{-1}`.
   The pre-run census whitelisted "day" by mistake.
3. `08-rate-laws` theorem: `\ce{aA -> products}` froze an English word inside
   `\ce`; it is now `$a\mathrm{A} \rightarrow \text{products}$` — translate the
   `\text{}` (the math census blanks it).
4. `26-s-block`: "E° more than 2.7 V below the line of water at pH 7" was false
   (Li 2.63, Na 2.30, K 2.52 V below) → **2.2 V**.
5. `20-elimination` chair figure: the label block touched the equatorial H;
   moved from x = 2.6 to **3.0** (drawing code: copy it byte-identically).
6. Link layer: "made quantitative by the theories" (`08-rate-laws`) linked the
   quantitative-REACTION definition; English now protects it. Protect your own
   rendering.

## Book 1 English canon fixes since wave 1 (carried into every finished edition)

- `grade-12/solutions/11` exo 1, "Hydration:" (of ETHENE, an addition) linked to
  the ion-hydration definition in English and in all four wave-1 editions;
  every config now protects the colon-led head (found by the Indonesian agent).
- `grade-12/02` weekend problem item 14: "Is it chiral as a whole?" → "Is it
  optically active as a whole?" — chirality is a property of molecules, and the
  solution answers about optical activity (found by the Hindi agent).

## Tool fixes since wave 1

- `check_hindi_prose.py` `LATIN_WORD` now includes Latin-1 letters: "Léon Péan"
  no longer splits into the "English" fragments *on* and *an*
  (`check_indonesian_prose.py` imports it).
- `check_indonesian_prose.py` gates the time adverbs *later, earlier, soon,
  meanwhile, afterwards* (an untranslated "later" survived in a figure).
- `check_latin_prose.py` strips `\pgfmathprintnumber[...]` options (the French
  Book 2 agent: *fixed, zerofill, precision* fired the BLOCKING tier on a
  figure with no prose — every Latin edition of Book 2 would have hit it).

## Lessons for the term layer (all four agents)

- **STOP does not reach the chapter-local table.** A STOPped term still links in
  the chapter that defines it. To remove a wrong sense there, use `DROP` (the
  French Book 2 agent needed DROP for bare *fort/forte/faible*: 18 wrong links)
  or an `EXTRA_PROTECT`. STOPping bare "E"/"Z" does nothing; English keeps those
  links and so may you.
- **Self-definition fallback**: inside the definition of a multi-word term, the
  bare head noun links to a *different* definition (Hindi क्रियात्मक समूह → the
  periodic-table समूह; French *groupe caractéristique*). Check every multi-word
  definition's own sentence.
- **`id_apply` does not protect a `% ledger:` line inside a replaced range**:
  the Hindi agent dropped one twice; gate 12 caught it. Keep `% ledger:` lines
  OUT of your ranges.
- Book 2 high-density targets that are NOT collisions (French): *maille*
  (lattice, 79 vs 22), *avancement* (extent, 28 vs 1), *coordinence* (24 vs 7)
  — one word where English writes a phrase or avoids the bare noun.

## Drawing code in Book 2 (from the French Book 2 agent)

- `!draw` needed: `16` EN line 199 (carvone `\foreach` labels), `17` EN line 68
  (colour wheel `\foreach`).
- Scheme arrow labels in chapters 18–25 are translated freely (the `chem` census
  blanks word-only labels); the French agent shortened `->[migration]` in 25.
- Orphaned headings needed a `\clearpage` before §10.4 and before the weekend
  problem of 26 in French; check yours on the rendered page.

## Arabic: right-to-left defects no gate can see (Arabic Book 1 agent)

Arabic Book 1 misses 7 English targets, each one English itself links once or
twice (abundance, Ka, resource, plastic code, complementary colour, ε, organic):
accepted. Its RTL findings, all confirmed on rendered pages with
`pdftotext -bbox` glyph coordinates (judging direction by eye is unreliable):

1. **Statement heads printed their brackets facing outward** — "Exercise
   40.1 )★(" on every exercise, remark and titled definition. FIXED centrally
   in `styles/onechemistry.sty` (Arabic block: amsthm's `\thmhead@plain` writes
   the brackets swapped, because babel never mirrors inside the head box). No
   source change needed.
2. **A redox couple `\ce{Cu^{2+}}/\ce{Cu}` printed reversed** ("Cu/Cu²⁺"): wrap
   the couple in `$…$` (the `\ce` arguments unchanged, so gate 12 stays green).
   Book 2 is full of couples (chapters 13–15): expect many.
3. **Inline chemfig schemes in running text ran right to left**: wrap each in
   `\babelsublr{…}`.
4. **Mixed Arabic/Latin TikZ node text** comes out misordered (pictures are
   forced LTR, and switching a node to RTL reverses digit and Latin runs —
   "316 ppm" → "mpp 613"): `\foreignlanguage{arabic}{…}` around the node text
   plus `\babelsublr{}` around each bare Latin word or number. Latin-only axis
   labels boxed LTR ("pH" printed "Hp").
5. **Inline MATH-mode `\ce{… <=> …}` draws its harpoons over the preceding
   species** in an RTL line: set it in text mode. Book 2 English has about nine
   such sites (b1/11, b1/28 among them).

The recipes are scripts in the Arabic Book 1 agent's scratch folder,
`…/scratchpad/ar1/post.py` (idempotent RTL edits) and `ar1/rtlnode.py` (the
node recipe), with notes in `ar1/PROGRESS.md`: the Arabic Book 2 agent should
read them first.

## Hindi Book 1 notes

- Register by grade, measured: तुम imperatives in grades 1–9, आप in 10–12.
  Book 2 is आप throughout.
- The recall box is now the pronoun-free "पहले से ज्ञात" (fits both registers).
