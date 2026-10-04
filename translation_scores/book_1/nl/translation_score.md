# Translation score — Chemistry Book 1 · Dutch (`nl`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 1 (School Chemistry, Grades 1–12) |
| **Language** | Dutch (`nl`) |
| **Quality bar** | **native school prose** — Dutch chemistry as a Dutch or Flemish pupil reads it, from the first school year (short sentences, *je*) to the last (the register of a pre-university chemistry course). English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **Register references measured before drafting** | the **English** canon (content) and the shipped **Dutch biology editions** (`../one-biology-book/parts/*/nl/`, 96/100): informal *je/jouw*, imperative and interrogative exercise stems, *Weekendprobleem*, *Deel I*, *Probleem: …*, `Hoofdstuk \ref{…}` in solution headers, `` ``…'' `` quotes, decimal points kept in prose and mathematics |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-04 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 49 chapters + 49 solution twins = **98 files**, `frontmatter/preface.nl.tex`, `frontmatter/image-credits.nl.tex`, a curated `tools/term_config/book1_nl.py`, the defined-term link layer, the Dutch index keys, the overfull and figure sweeps, and this score |

## Verdict in one line

A Dutch Book 1 that reads as one school chemistry course written in Dutch —
*voorwerp* and *materiaal* in year 1, *beginstoffen* and *reactieproducten* in
year 7, *kloppende reactievergelijking*, *voortgangstabel*, *beperkende
beginstof*, *equivalentiepunt*, *halveringstijd*, *zuur-basekoppel* later —
with every structural, build, prose and chemistry gate green on a forced build
of **0 errors / 0 undefined / 0 overfull / 0 nullfont / 0 invalid-in-math**,
**444 pages**, **98/98 files in the `.fls`**.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Counted over all 98 files against their twins, all exact: **665 `exercise`**, **42 `problem`**, **707 `\begin{solution}`**, **112 `[resume]`**, **260 `omfigure`**, **137 `tikzpicture`**, **25 `axis`**, **495 `\node`**, **123 `\includegraphics`**, **184 `definition`**, **115 `proposition`**, **65 `method`**, **155 `example`**, **52 `proof`**, **72 `remark`**, **47 `recall`**, **29 `inthelab`**, **15 `history`**, **23 `safety`**, **1054 `\item`**, **1352 `\label`** (set diff 0/0), **142 `\cref`**, **49 `\ref`**, **369 `\emph`**, **301 `\index`** (301 distinct keys; no two English keys collapse onto one Dutch key), **2196 `\qty`**, **141 `\num`**, **2267 `\ce`**, **128 `\chemfig`**, **77 `\ghs`**, **186 `% ledger:`**. Every file was written through `tools/id_apply.py` (math, chem, draw, img, label, env, emph, index censuses). A per-file census of every numeral against the English twin leaves only spelled-out years and the "Year 1/2 volume" ordinals |
| Terminology | **96** | The Dutch school vocabulary throughout: *mengen, oplossen, opgeloste stof, oplosmiddel, verzadigde oplossing, zeven, bezinken, afschenken, filtreren, filtraat, indampen, branddriehoek, onomkeerbare verandering, grondstof, erts, zuivere stof, homogeen/heterogeen mengsel, aantoningsreactie, blanco, kalkwater, knalgasproef, beginstoffen, reactieproducten, reactieschema, kloppende reactievergelijking, coëfficiënt, harsidentificatiecode, thermoplast/thermoharder, atoomnummer, massagetal, isotoop, tribune-ion, neerslag, periodiek systeem, abundantie, dunnelaagchromatografie, eluens, retentiefactor, schil/subschil, valentie-elektron, rompelektron, duet- en octetregel, vrij/bindend elektronenpaar, lewisstructuur, constante van Avogadro, molaire massa, molair volume, stamoplossing, verdunningsfactor, ijkreeks, maatkolf, voortgangstabel, beperkende beginstof, verwarmen onder terugvloeiing, vacuümfiltratie, herkristallisatie, rendement, absorbantie, wet van Lambert-Beer, ijklijn, elektronegativiteit, partiële lading, vanderwaalsbinding, waterstofbrug, solvatatie/hydratatie, amfifiel, micel, karakteristieke groep, skeletformule, golfgetal, vingerafdrukgebied, oxidator/reductor, halfreactie, redoxkoppel, titrant, equivalentiepunt, molaire verbrandingsenergie, bindingsenergie, chemische verschuiving, integratiecurve, multiplet, n+1-regel, weergave volgens Cram, asymmetrisch koolstofatoom, enantiomeren, diastereomeren, gestaffeld/eclips, gebogen pijl, carbokation, reactie-intermediair, afschrikken, kinetische factor, halveringstijd, katalysator, reactiequotiënt, evenwichtsconstante, oxoniumion, amfolyt, zuurconstante, predominantiediagram, omslagtraject, bufferoplossing, pH-metrische en conductometrische titratie, wet van Kohlrausch, halfcel, zoutbrug, celspanning, constante van Faraday, beschermende groep, atoomeconomie, groene chemie, repeterende eenheid, polymerisatiegraad*. Dutch IUPAC names throughout (*ethaanzuur, propaan-2-ol, ethylethanoaat, but-2-een, hexaan-1,6-diamine, benzeen-1,4-dicarbonzuur*). Minus four for one Flemish-leaning choice (*ionaire vaste stof*, grade 11) and a handful of terms where the Netherlands and Flanders differ and one form had to be chosen |
| Register / tone | **97** | Informal *je* throughout (403 *je/jouw* forms; **0** *u/uw*); imperative and interrogative exercise stems as in the biology editions (*Bereken*, *Leg uit*, *Schrijf … op*, *Waarom …?*); short paratactic sentences in years 1–6, the pre-university register in years 10–12. *Weekendprobleem* ×42, *Deel I–IV* ×154 (= English *Part* ×154) |
| Accuracy / sense | **96** | Every chapter re-read against its twin; every weekend problem and every solution chain recomputed from the English data before drafting (see *Canon findings*). Two local wordings deviate deliberately from a defective English sentence and are listed below; nothing else adds, drops or softens content |
| Typography / mechanics | **97** | `` ``…'' `` quotes (94 pairs, 0 straight quotes); decimal points kept; `\qty`/`\unit`/`\num` arguments all ASCII (scripted check: 0 non-ASCII); `\text{}` in mathematics translated (58/58, census below); line-edge sweeps (`['’]$`, line-initial punctuation, line-final hyphen) clean outside TikZ code and comments |
| Link layer | **95** | 5,065 links to **174 targets** — **every one of English's 172 targets is reached**, plus two (*donorplaats/acceptorplaats*, 13; *verzinken*, 1). 88 % of English's link count, the deficit being structural: Dutch writes *koolstofatoom, natriumionen, watermolecuul* as one word, and `lang_nl` refuses to link inside a compound by design (atom 319 vs 620, ion 211 vs 409, molecule 301 vs 439). `--unwrap --apply` then `--apply` is idempotent; the dry run prints **links to insert: 0** |
| Build cleanliness | **99** | Forced `latexmk -g`: 0 `!`, 0 undefined, **0 overfull** (16 → 0, all by rewording or hyphenation hints, never by `\sloppy`), 0 nullfont, 0 invalid-in-math; `.fls` lists all 98 edition files and both front-matter files |

## Figures

Every figure label whose Dutch text is ≥ 15 % and ≥ 4 characters longer than
the English (79 labels, scripted) was rendered and inspected, plus every page
those figures share. Eleven collisions were found and fixed by shortening or
re-breaking the Dutch label (TikZ geometry untouched, except `font=\footnotesize`
on the three titration-flask labels): the Venn heading of grade 1, the
chromatography rod label (grade 7), the ion-formation arrows (*geeft / krijgt
1 e⁻*, grade 9), the carbon-cycle labels (grade 8), the volumetric-flask and
recrystallisation step labels (grade 10), the absorbance legend that was
clipped at the axis edge (grade 11), the iodine-extraction label (grade 11),
the titration flasks (grade 11), the conformation labels (grade 12), the
catalysis energy profile (grade 12), and the *(katalysator)* boxes of the
ibuprofen routes (grade 12).

## `!draw` opt-outs (English line numbers)

`\foreach` label lists translated (byte-compared by the draw census):
grade-4/02 158–159 · grade-5/01 95–96, 105–106, 139–140 · grade-5/02 148–149 ·
grade-7/01 335 · grade-8/03 133 · grade-9/02 53–55, 168, 227–229 · grade-9/03
67–70 · grade-9/04 38 · grade-10/04 294–297 · grade-11/01 42–45 · grade-11/04
161–162 · grade-11/05 125–128 · grade-11/06 144–151 · grade-12/01 88–95,
183–184 · grade-12/07 197–201 · grade-12/08 142–145 · grade-12/11 312, 316.
Node text the census cannot blank (an `at` coordinate with nested parentheses,
`($(a.south)!0.5!(b.south)$)`): grade-8/01 151, 153 · grade-11/03 247–248.
A translated `xticklabels=` / `yticklabels=` line added beside ASCII symbolic
coordinates (precautionary): grade-4/01 134 · grade-11/09 244–245 (an `xbar`
chart, so `yticklabels`) · grade-12/11 231.

## Link census

*Frequency census* against English, per target: no target is reached more than
twice English's count except the four where Dutch uses the defined word where
English uses a bare synonym that English never harvested —
*reactievergelijking* (43 vs 19: English writes "equation", Dutch writes the
defined word), *coëfficiënt* (14 vs 2), *halveringstijd* (26 vs 11, plural
included), *donorplaats/acceptorplaats* (13 vs 0: English's term is
"electron-donor site", which its own prose never repeats).

*Chapter-set census* (Dutch links in chapters English never links): every
survivor read; all are the defined sense (*grondstoffen* as feedstocks in
grade 12, *molaire massa's*, *beginstof*, *mengt* as "mixes with").

Before curation the two censuses found these Dutch collisions, all curated in
`tools/term_config/book1_nl.py` with their evidence:
* the isomer letters **Z/E** plus the Dutch tail became *een*, *en*, *zes*,
  *Zn* — **184 false links** in the uncurated run;
* **zeven** — the sieving of grade 3 against the number seven (seven
  molecules, seven codes, the halogens have seven valence electrons);
* **rendement** — the efficiency of a spirit-burner heating (grade 11);
* **branden** — a lamp that lights up and a corrosive that burns the skin;
* **groep** — linked only before a number (the periodic-table group);
* **coëfficiënt** — the conductivity coefficient λᵢ;
* **hydratatie** — of ethene (an addition), not of ions.
The English STOP choices were mirrored where the Dutch word carries the same
everyday sense (*oplossing, materiaal, voorwerp, periode, symbool, additie,
substitutie, capaciteit*).

## `\text{}` census (course + solutions)

58 English / 58 Dutch; every English `\text{}` content has its Dutch
counterpart (*(oxidatie)*, *atoomeconomie*, *verbroken bindingen*, *verkregen*,
*stam*, *verdund*, *opgeloste stof*, …); `Ox`, `Red`, `ester`, `water`,
`alcohol` are kept as the same symbols or Dutch words.

## Samples (Dutch, with verdict)

1. **grade 3, decanting** — «~Een mengsel van water en een vaste stof die
   niet oplost, kun je laten staan: de vaste stof zakt langzaam naar de bodem.
   Dat heet \emph{bezinken}. Als alles bezonken is, kun je het heldere water
   erboven voorzichtig in een ander bakje gieten, terwijl de vaste stof
   achterblijft: dat is \emph{afschenken}.~» → **native**: the two school
   verbs, *je*, short clauses for an eight-year-old.
2. **grade 8, conservation of mass** — «~Er gaat niets verloren en er wordt
   niets gemaakt; materie verandert alleen van vorm.~» → **native**.
3. **grade 11, redox** — «~Het woord betekende vroeger ``zich verbinden met
   zuurstof''; nu betekent het iets algemeners en nuttigers: het afstaan van
   elektronen.~» → **native**.
4. **grade 12, equilibrium** — «~Een dichte fles bruisend water houdt
   maandenlang zijn prik; open verliest ze die in een middag.~» → **native**:
   *prik* is the word a Dutch reader uses for the fizz.
5. **grade 12, green chemistry** — «~Eén groen kenmerk maakt nog geen groen
   proces.~» → **native**, idiomatic close to the English punch line.

## Canon findings (reported, not repaired in English)

1. `parts/grade-7/solutions/01-identifying-substances.tex` 58–59 (exo:12):
   calls breathed-out air "a blank … known to contain carbon dioxide" — that is
   a **positive control**, contradicting the book's own definition of a blank
   (`parts/grade-7/01-identifying-substances.tex` 37–39: a sample known *not*
   to contain the species, which must stay negative). The Dutch stem and
   solution say *controleproef* (control test), which is true of both.
2. `parts/grade-11/05-functional-groups.tex` 256–259 (exo:11) asks "Which
   **two** families have a carbonyl group with an oxygen or nitrogen atom on
   the same carbon?"; the solution (`solutions/05-functional-groups.tex`
   66–68) answers "**three**, in fact, with the esters". Translated as
   written.
3. `parts/grade-10/solutions/03-lewis-and-shape.tex` 82 (exo:15, ozone): the
   single-bonded oxygen carries `\charge{0=\:,180=\:,270=\:}` — the lone pair
   at 180° is drawn **on the O–O bond** (rendered and confirmed); it belongs at
   90°. The structure also shows no formal charges.
4. `parts/grade-12/solutions/01-proton-nmr.tex` 125 (problem q9): "a \ce{CH3}
   bonded to the C=O carbon or to the **ring** oxygen" — none of the candidate
   esters has a ring; the oxygen meant is the ester oxygen. Dutch: *het
   zuurstofatoom van de estergroep*.
5. `parts/grade-12/04-reaction-rates.tex` 48–50 (inthelab): \qty{10.0}{mL}
   poured into about \qty{50}{mL} of ice water is "diluted **five** times";
   by the book's own convention (exo:14 of the same chapter, 5 mL into 45 mL =
   ×10) that is six. Translated as written.
6. Minor, visual: `parts/grade-12/03-curly-arrows.tex` 43 — the lone pairs
   of `\charge{90=\:,0=\:,270=\:}{Br}` sit on the two-letter symbol;
   `parts/grade-10/solutions/03-lewis-and-shape.tex` 82 and the neighbouring
   HCN/HCHO answers put a lone pair beside the sentence's own colon
   ("N⁚: two groups"), which reads as stray dots.

## Tool and gate findings

* **Linker, single-letter terms × Dutch tail.** `\emph{Z}` / `\emph{E}` are
  harvested as terms; `lang_nl.WORD_TAIL = (?:e?[ns])?` then matches *een*,
  *en*, *zes*, *Zn* (184 false links). Worked round in `book1_nl.py`
  (EXTRA_PROTECT); the general fix is to apply no tail to a one-character
  term.
* **EXTRA_PROTECT look-arounds are not wrap-stable.** A protect pattern whose
  context word is itself a term (*halogenen zeven*, *zeven moleculen*) matches
  on the first `--apply` but not on the second, once the neighbour is wrapped
  in `\omterm{…}{…}`: the dry run printed 2 instead of 0. Fixed in the config by
  admitting an optional `\omterm` wrapper in the look-ahead; worth a line in
  `translation_instruction.md`.
* **`tools/check_orphan_lines.py` does not strip trailing `%` comments**: the
  English `\clearpage % keeps the heading with the problem box …` line, copied
  verbatim, fired gate 10 in grade 9 (and would in grade 10). The Dutch files
  carry the comment translated; the gate should ignore comments.
* **`id_apply` NODE_TEXT** cannot blank node text whose `at` coordinate holds
  nested parentheses (`($(a.south)!0.5!(b.south)$)`), so translating such a
  node costs `!draw` (grade-8/01, grade-11/03).
* **Run file `!draw` list incomplete**: the sites above that are not in
  `sources/TRANSLATION_BOOKS_1-2.md` (grade-4/02, grade-8/01, grade-8/03,
  grade-9/02, grade-10/04, grade-11/03, -04, -05, -06, grade-12/01 88–95,
  grade-12/07). grade-11/09 244 is a `yticklabels` (an `xbar` chart), not an
  `xticklabels`.
* **Allow-list entries appended** to `ALLOWED_BY_LANG["nl"]` in
  `tools/check_latin_prose.py` (append-only, with comments): *in, water, ppm,
  proton, neutron, nucleon* (condenser labels *water in/uit*, "316 ppm in
  1959", the title *Proton, neutron, nucleon* — Dutch spelt as English) and
  *lamp, detector, display, thermometer, red, amine, amide* (spectrophotometer
  and burner labels, the reductant symbol of Ox/Red, the title *Amine, amide*).

## Why not 100

* **Five canon defects** are reproduced or locally worded round, not repaired
  in English; two Dutch sentences (findings 1 and 4) deliberately say the true
  thing rather than mirror the English slip.
* **Link coverage is 88 %** of English's count, by construction of Dutch
  compounding; a second pass could add more EXTRA plurals and inflected forms.
* **Twenty-nine `!draw` ranges**: each is the documented pattern, but each is a
  place where only the rendered PDF, not the census, guards the figure.
* **One shared file extended** (`check_latin_prose.py`, thirteen words).
