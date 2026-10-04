# Wave 1 findings — Book 1 fr, nl, es, pt (2026-10-04)

Read this after `sources/TRANSLATION_BOOKS_1-2.md`; where they disagree, this
file wins.

## What wave 1 delivered (coordinator re-measured each on a forced `-g` build)

| | pages | `\omterm` links | targets | 0 err / 0 undef / 0 overfull / nullfont 0 | `.fls` | score |
|---|---:|---:|---:|---|---:|---:|
| en | 432 | 5,775 | 172 | yes | — | — |
| fr | 451 | 6,012 | 173 | yes | 98 | 96 |
| nl | 444 | 5,064 | 174 | yes | 98 | 96 |
| es | 447 | 5,964 | 173 | yes | 98 | 96 |
| pt | 440 | 5,887 | 172 | yes | 98 | 96 |

Every edition reaches every English target. Dutch is lower in links because
it welds compounds (*koolstofatoom*) that the linker does not link inside;
that is the language, not a defect.

## English canon fixes (applied 2026-10-04, carried into fr/nl/es/pt)

All of them were reported independently by two to four agents and verified
against the book's own model before editing. No line count changed. Every
wave-2 agent starts from the corrected canon; translate what is there now.

1. g7/01 exo 12 and its solution: breathed-out air is a positive **control**,
   not a "blank" (the chapter defines a blank as a negative). Now "control
   test".
2. g10/01 exo 12 and the weekend problem's item on evaporating the
   cyclohexane: linalool's boiling point (198 °C) was used by the solutions but
   printed nowhere. Now in both stems.
3. "(ledger)" was printed in visible text (g11/04, g11/06, g12/01): removed.
   The ledger is an internal sourcing tool; never mention it in prose.
4. g11/02 weekend problem: H₂Se's boiling point is already in °C, so "Express
   both in degrees Celsius" became "Express the first".
5. g11/05 exo 11: "which two families" (the solution answered three) became
   "which families"; the solution now ends "three families."
6. g12 solutions/01 problem item 9: "the ring oxygen" (the candidates are
   open-chain esters) became "the ester oxygen".
7. g12 solutions/03: "a positive carbon is left" became "a positive charge is
   left".
8. g12/04 exo 1: "a stronger acid attacks zinc faster" (the answer is
   concentration, and "stronger" means something else in this book) became
   "a more concentrated acid".
9. g12 solutions/07 problem item 4: the pKa scale is vertical, so "Left of
   ethanoic acid" became "Below".
10. g12 solutions/09 problem item 20: "an acidity of 6.0 degrees" (jargon the
    problem never uses) became `\qty{6.0}{\percent}`.
11. g12/04 quenching box: 10 mL into "about 50 mL" is ×6, not the "diluted
    five times" the text says; now "about 40 mL".
12. g10 solutions/03 exo 15: ozone's right-hand oxygen had a lone pair drawn
    ON its bond (`180=\:`); now `90=\:`.
13. g12/03 polarity figure: bromine's lone pairs touched the glyph; now
    `\charge{90:2pt=\:,0=\:,270:2pt=\:}{Br}`.
14. g12/06 equilibrium figure: the "equilibrium: 2/3 mol" label was clipped by
    the legend; now anchored below the dashed line.

Reported and NOT changed: the Dutch agent's "N⁚:" (a lone pair beside the
sentence's colon in g10 solutions/03) — cosmetic, and the rewording would cost
more than it buys. Wave-2 agents may reword their own sentence around it.

## Tool fixes since the run file was written

- **Periodic-table legend** (`\omperiodictable[legend]`) was hard-coded English
  in the style file. It is now `\omnamePTmetal` … `\omnamePTnoble` in
  `styles/lang/<lang>.tex`. The coordinator wrote the hi, ar and id wording;
  **the Book 1 agent of that language checks it and owns those lines.** Never
  pass legend keys in the macro's options (frozen by the chem census).
- `check_orphan_lines.py` ignores trailing `%` comments (all four agents
  translated `\clearpage % …` comments to get past it; no need).
- `id_apply.py` NODE_TEXT handles `at (…)` with one nested level of
  parentheses, so `\node at ($(a)+(0,1)$) {label}` no longer forces `!draw`.
- `tools/gates.sh` no longer reports every label as duplicated once an edition
  exists (it now scans the English canon only).

## The full list of drawing-code text (supersedes the run file's list)

Translating these costs `@@ N-M !draw` on that range (English line numbers;
every wave-1 agent needed about 29 such ranges):

- `\foreach` label lists: g4/02 158; g5/01 95, 105, 139; g5/02 148;
  g7/01 335; g8/03 133 (contains "OTHER"); g9/02 53–62, 168, 227–229;
  g9/03 67–70; g9/04 38; g11/01 42–45; g11/06 144–151; g12/01 88–98, 183;
  g12/07 197–201; g12/08 142–145; g12/11 312, 315–317.
- `\cube{…}` macro text arguments: g10/04 294–297.
- Node text no longer needing `!draw` after the NODE_TEXT fix: g8/01 151–158,
  g11/03 247–248, g11/04 161–165, g11/05 125–133 — try without first.
- pgfplots string keys (blanked by the census, translate freely): g4/01 134,
  g11/09 243–244 (`yticklabels` on an `xbar` chart), g12/11 230–231.

## Term-link lessons (all four editions hit some of these)

- **Single-letter terms.** `\emph{E}`/`\emph{Z}` (isomer descriptors) are
  harvested; with a plural tail they matched *een, en, zes, Zn* (Dutch, 184
  false links), *Es* (Spanish), the conjunction *e* (Portuguese). STOP or
  protect bare E and Z from the start.
- **`EXTRA_PROTECT` patterns are joined into ONE regex**, so a later pattern
  cannot match text an earlier one already consumed: order matters, put the
  longest/most specific first.
- **A look-ahead anchored on a word that is itself a term stops matching once
  that word is wrapped** (already in `translation_instruction.md`; the Dutch
  agent hit it with *zeven moleculen*). Allow `(?:\\omterm\{[^{}]*\}\{)?`.
- **Reagent = reactant** in French (*réactif*), Portuguese (*reagente*) and
  Spanish: the test-reagent uses in g9/02 link to the reactant definition.
  Accepted as the language's own usage; decide for yours.
- **Homograph found by the coordinator in Spanish**: *vaso de precipitados*
  (a beaker) linked to *precipitate*. Look for glassware and equipment names
  built on a chemistry term in your language.
- `wrap.py` skips the self-link inside a term's own definition, so a shorter
  term can match there instead (French *groupe* inside the definition of
  *groupe caractéristique*). Check your multi-word definitions.

## Conventions settled by wave 1

- **Decimal separator: a point, in prose as in `\qty`.** The series sets
  `output-decimal-marker={.}` for every language, so a decimal comma in prose
  would contradict every quantity on the same line.
- **Accented `\index` keys get an ASCII sort key**: `\index{acido@ácido}`,
  otherwise makeindex files them after z. (Latin-script editions; Indonesian
  has no accents.)
- **The preface** says the book was first written in English and translated;
  each Book 1 agent adapted that sentence.
- **Local builds of fr/es/nl have no babel** (`*.ldf` not installed here) and
  hyphenate with English patterns; CI's full TeX Live has babel. Indonesian's
  `bahasai.ldf` IS installed. Not an agent concern, but do not read too much
  into a hyphenation break in a local fr/es/nl PDF.
