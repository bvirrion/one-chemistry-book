# Translation score — Chemistry Book 1 · French (`fr`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 1 (School Chemistry, Grades 1–12) |
| **Language** | French (`fr`) |
| **Quality bar** | **native school prose at every level** — a French children's science book in grades 1–5, a French collège textbook in grades 6–9, a French lycée chemistry course in grades 10–12. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **Sense / register references measured before drafting** | the **English** canon (content); the shipped French editions of One Biology Book 1–3 (`../one-biology-book/parts/*/fr/`) for typography, the *tu* register of the school years and the **infinitive** exercise stem of the lycée years; the French physics editions for shared physical vocabulary |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-04 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 49 chapters + 49 solution twins = **98 files**; `frontmatter/preface.fr.tex` (shared with Book 2 `fr`) and `frontmatter/image-credits.fr.tex`; the four box names in `styles/lang/fr.tex`; the `\bookline` of `one_chemistry_book_1_school_fr.tex`; a curated `tools/term_config/book1_fr.py`; the defined-term link layer; French index keys with ASCII sort keys; the overfull sweep; a per-figure label check; and this score |

## Verdict in one line

A French Book 1 that reads as one French school chemistry course from the
first year to the last — *tu* and short sentences for the youngest readers,
the impersonal *on* of the collège textbook, the infinitive exercise register
of the lycée (*Calculer*, *Donner*, *Écrire*), French spaced punctuation and
guillemets — with every structural, prose and chemistry gate green over all
twelve years and a forced build of **0 errors / 0 undefined / 0 overfull /
0 nullfont / 0 invalid-in-math**, 451 pages.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, counted over all 98 files against their 98 twins: **665 `exercise`**, **42 `problem`**, **707 `\begin{solution}`**, **112 `[resume]`**, **260 `omfigure`**, **137 `tikzpicture`**, **25 `axis`**, **495 `\node`**, **123 `\includegraphics`**, **369 `\emph`**, **301 `\index`**, **142 `\cref`**, **1352 `\label`**, **1054 `\item`**, **2196 `\qty`**, **2267 `\ce`**, **128 `\chemfig`**, **186 `% ledger:`** comments, and per environment **184 `definition`, 115 `proposition`, 65 `method`, 155 `example`, 52 `proof`, 72 `remark`, 47 `recall`, 29 `inthelab`, 15 `history`, 23 `safety`** — all equal to English. `\label` set diff **0 / 0**. Every file was written through `tools/id_apply.py`, so every unnamed line (mathematics, chemistry, TikZ, image paths, solution keys, ledger comments) is byte-identical to English; a per-exercise and per-solution **number census** against English finds no numeric difference except the "1" of *réaction d'ordre 1* and one "Year 1 volume" rendered *volume de première année d'université* |
| Terminology | **96** | The French school and lycée vocabulary, consistent across the twelve years: *corps pur / mélange homogène / hétérogène*, *soluté, solvant, solution saturée*, *décantation, transvasement, filtration, filtrat*, *triangle du feu, combustible, comburant*, *transformation chimique / physique*, *équation ajustée, coefficient stœchiométrique*, *matière plastique, thermoplastique / thermodurcissable, PEHD / PEBD*, *numéro atomique, nombre de masse, écriture conventionnelle*, *ion spectateur*, *quantité de matière, constante d'Avogadro, masse molaire*, *concentration massique / molaire, solution mère, facteur de dilution, échelle de teintes*, *tableau d'avancement, avancement maximal, réactif limitant, mélange stœchiométrique*, *chromatographie sur couche mince, éluant, rapport frontal*, *schéma de Lewis, doublet liant / non liant*, *liaison polarisée, électronégativité, liaison hydrogène*, *formule brute / semi-développée / topologique*, *groupe caractéristique*, *nombre d'onde, transmittance, empreinte digitale*, *couple oxydant/réducteur, demi-équation*, *solution titrante / titrée, volume à l'équivalence*, *RMN du proton, déplacement chimique, singulet / doublet / triplet / quadruplet, règle des n+1*, *représentation de Cram, carbone asymétrique, énantiomères, diastéréoisomères, forme méso, conformation décalée / éclipsée*, *site donneur / accepteur, flèche courbe, acte élémentaire, intermédiaire réactionnel*, *facteur cinétique, trempe, temps de demi-réaction*, *catalyse homogène / hétérogène, pot catalytique*, *quotient de réaction, taux d'avancement final, sens direct / inverse*, *acide de Brønsted, ion oxonium, ampholyte, produit ionique de l'eau, pKa*, *diagramme de prédominance, zone de virage, solution tampon, relation de Henderson*, *titrage pH-métrique / conductimétrique, loi de Kohlrausch, demi-équivalence*, *pile, demi-pile, pont salin, tension à vide, constante de Faraday*, *chimiosélectivité, groupe protecteur, économie d'atomes, chimie verte, fluide supercritique*, *motif, degré de polymérisation, polymère d'addition / de condensation*. Gas names follow the French school convention (*azote, oxygène* in grade 4; *dioxygène, diazote, dihydrogène* from grade 7); ester names in French order (*éthanoate d'éthyle*); *eau oxygénée à 20 volumes*, *vinaigre à 6 degrés* where French has its own idiom. All 301 `\index{}` keys rewritten in French, singular lemmas, with ASCII sort keys (`electron@électron`) so that accented entries sort under their letter |
| Register / tone | **97** | Measured, not assumed. Grades 1–5: *tu* throughout, imperative 2sg exercise stems. Grades 6–9: impersonal course text (*on*), imperative 2sg stems (*Calcule* ×24, *Regarde* ×19, *Écris* ×18, *Nomme* ×13, *Donne* ×11). Grades 10–12: infinitive stems (*Calculer* ×88, *Donner* ×55, *Écrire* ×51, *Dessiner* ×23, *Expliquer* ×21, *Nommer* ×20, *Vérifier* ×18) and **0** 2sg forms; **0** *vous* anywhere except inside the Rutherford quotation. Box names chosen to fit every year: *Rappel*, *Au laboratoire*, *Histoire des sciences*, *Sécurité* |
| Typography | **97** | French spaced punctuation (`~:` `~;` `~?` `~!`) and guillemets `«~…~»` throughout; the decimal point kept, as the series' siunitx setting does and the shipped French biology editions do; *\textsc{xx}\textsuperscript{e}~siècle*; final sweeps: **0** lines ending on an elision apostrophe, **0** lines opening on punctuation, **0** dangling hyphens, **0** stray English function words outside labels and code |
| Fidelity / accuracy | **96** | Every course paragraph, worked example, exercise and solution was translated against its twin with the numbers recomputed while translating (every grade-11 and grade-12 weekend problem was re-derived: titration of the iron tablet, the ethanol burner, Berthelot's constant and the threefold excess, the vinegar, the blood buffer, the ibuprofen routes, the PET jacket…). Two English slips were rendered with their intended meaning rather than copied (a "stronger acid" that the solution reads as "more concentrated"; "a positive carbon is left on the other carbon"), and the internal word *(ledger)* that leaks into three English proofs is not printed in French; everything else that looks wrong in English is reproduced and reported below |
| Figures | **95** | 575 French figure labels; every label at least 25 % and 6 characters longer than its English twin was located in the PDF and its page rendered and read: **twelve collisions found and fixed** (cork and wood labels, the three extinguished fire triangles, the recycling loop, the carbon cycle, the three metals in acid, the dissolution and recrystallisation step labels, the bond-stretch spring, the bond-energy diagram, two overfull tables). Fixes are shorter or two-line labels; two needed a `!draw` opt-out |
| Links | **95** | **6013 `\omterm` links on 173 targets** against English's **5775 on 172**: every English target is linked (0 missing), plus one (*trempe*, quenching) that English defines but never matches. Dry run over the wrapped tree: **links to insert: 0** |

## Gates

`bash tools/check_translation.sh grade-N fr` for N = 1 … 12: **12 / 12 PASSED**
(structural censuses, duplicate labels, ledger ids, gate 9 twin-comparison
prose gate — no multi-word finding; the advisory one-word tier is
cognates only (*absorbance*, *dissociation*, *conformation*, *enzyme*,
*cation*, *zinc*, *solution*, *ester*, *Gly--Ala*) —, gate 10 orphan lines,
gate 11 problem numbering, gate 12 chemistry twin, gate 13 equation balance).

Build (`latexmk -g`, forced, under the run file's memory cap):
`grep -ac '^!'` **0**, `grep -aci undefined` **0**, `grep -ac Overfull`
**0**, `nullfont` **0**, `invalid in math mode` **0**; **451 pages**; the
`.fls` lists **98** French chapter and solution files = **98** on disk.

## Link layer

`tools/term_config/book1_fr.py` was curated from this edition's own
`--terms` harvest (326 harvested, 321 linkable) and a context census of every
suspicious word — never translated from `book1_en.py`. French homographs that
English does not have, each handled with evidence in the config:

* *groupe* — the periodic-table group only before a number; *groupe
  hydroxyle, groupe d'atomes, groupes d'électrons* stay plain, and the
  linkable *groupe caractéristique / alkyle / protecteur* are excluded by a
  lookahead (French puts the modifier after the noun, so English's
  look-behind cannot be copied);
* *couche* — an oil, sand, zinc or oxide layer against the electron shell;
* *indice* — a clue in grades 2 and 5 and a hint in an exercise, against the
  subscript; and the `indice=n` key of `\polymerdelim`, which the linker
  would otherwise have wrapped;
* *rendement* — the efficiency of the spirit-burner heating against the yield
  of a synthesis;
* *élimination* — removing water or a product against the reaction category;
* *brûler* — a corrosive that burns the skin against a combustion;
* *air* — *ont l'air identiques*; *noyau* — *le noyau terrestre*;
* *E*, *Z* — bare letters; *isomère Z / E* keep their links.

`EXTRA` links *double liaison* / *triple liaison* (French puts the adjective
first at least as often as the defined *liaison double*). The English
STOP list's everyday words (*solution, produit, matériau, objet, symbole*)
are stopped too, after the same check in French.

Target counts that differ most from English, each read: *pile* 31 vs 2
(French says *pile* where English says *cell* once and *battery* elsewhere),
*temps de demi-réaction* 26 vs 11 (French repeats the noun phrase where
English says *it*), *énergie de liaison* 12 vs 1 (English plural
*bond energies* rarely matches its own term), *test caractéristique* 4 vs 16
(English *reagent* links to the test; French *réactif* is one word for reagent
and reactant, resolved nearest-preceding to the reactant).

## Samples (French, with verdict)

1. **Grade 1, sorting materials** — «~Mets quelques objets dans une bassine
   d'eau. Un bloc de bois et un bouchon de bouteille en plastique flottent.~»
   → **native**: the imperative *tu* and the vocabulary of a French CP
   science page.
2. **Grade 9, the corrosion of iron** — «~Le fer ne rouille que lorsque le
   dioxygène et l'eau l'atteignent tous les deux.~» → **native**: *ne… que
   lorsque* is the collège textbook sentence.
3. **Grade 11, the titration remark** — «~On recommence le titrage jusqu'à ce
   que deux résultats concordent à 0.1 mL près environ.~» → **native**: the
   lycée lab register (*concordent à … près*).
4. **Grade 12, the reaction quotient** — «~Si $Q < K$, le système évolue dans
   le sens direct (les produits augmentent) jusqu'à ce que $Q = K$~» →
   **native**: *sens direct / sens inverse* is the French terminale phrase,
   not a calque of *forward*.
5. **Grade 12, hydrogen peroxide** — «~quelle est la concentration d'une eau
   oxygénée «~à 20 volumes~»~?~» → **native**: the French pharmacy label
   itself.

No passage reads as machine translation: the edition was drafted directly in
French against the English twin, line range by line range.

## Canon findings (reported, not fixed)

1. `parts/grade-7/solutions/01-identifying-substances.tex`, exo 12 — the
   "blank" is made with breathed-out air, which contains carbon dioxide: a
   positive control, contradicting the chapter's definition of a blank.
2. `parts/grade-10/01-chemical-species.tex`, exo 12 and the weekend problem
   q9 — linalool's boiling point (198 °C) is used but given nowhere in the
   chapter or the stem.
3. `(ledger)` printed in visible prose: `parts/grade-11/04-organic-skeletons.tex`
   l202, `parts/grade-11/06-infrared.tex` l124, `parts/grade-12/01-proton-nmr.tex`
   l76.
4. `parts/grade-11/02-polarity-and-cohesion.tex` l473–475 — "Express both in
   degrees Celsius" although the second value is already in °C.
5. `parts/grade-11/05-functional-groups.tex` exo 11 — asks for two families;
   the solution answers three.
6. `parts/grade-12/solutions/01-proton-nmr.tex` l125 — "or to the ring
   oxygen": the C4H8O2 candidates are acyclic esters (no ring).
7. `parts/grade-12/solutions/03-curly-arrows.tex` l99–100 — "a positive carbon
   is left on the other carbon" (a positive *charge*).
8. `parts/grade-12/04-reaction-rates.tex` l288 — "a stronger acid attacks zinc
   faster", answered "concentration".
9. `parts/grade-12/solutions/07-ka-and-pka.tex` l99 — "Left of ethanoic acid"
   on a pKa scale drawn vertically.
10. `parts/grade-12/06-equilibrium.tex` l77–84 — the legend (filled white,
    top right) covers the top of the node "equilibrium: 2/3 mol", in English
    too.

## Why not 100

* **Ten defects in the English canon** are reproduced or worked around, not
  repaired, because English is the source of truth.
* **`\omperiodictable` legends stay English** in three figures (grade 9
  ch. 5, grade 10 ch. 2 twice): the macro's legend labels are English
  defaults in `styles/onechemistry.sty`, and the only way to translate them —
  passing legend keys in the macro's options — is frozen by the chemistry
  census and gate 12.
* **Thirty `!draw` opt-outs**, each documented in the run report: each
  is a place where the drawing census no longer guards the figure, and only
  the rendered page does.
* **One shared file extended**: `ALLOWED_BY_LANG["fr"]` in
  `tools/check_latin_prose.py` needed *ion, cation, anion, amine, amide,
  anode, cathode* for three correct French definition titles to pass the
  blocking tier.
* **Link density is +4 %** against English, concentrated in grade 12 where
  French repeats noun phrases (*pile*, *temps de demi-réaction*).
