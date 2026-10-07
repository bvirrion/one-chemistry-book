# Translation score — Chemistry Book 3 · French (`fr`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 3 (University Chemistry, Year 2 — year `bachelor-2`, labels `b2`) |
| **Language** | French (`fr`) |
| **Quality bar** | **native academic prose**: a French second-year university chemistry course as it is written and taught. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **References measured before drafting** | the **English** canon (content); the shipped **French Book 2** (`parts/bachelor-1/fr/`) and its glossary of index keys (series terminology, infinitive stems, solution headers, cross-volume phrasing); `sources/TRANSLATION_BOOKS_3-4.md`, `sources/TRANSLATION_BOOKS_1-2.md`, `sources/WAVE{1,2,3}_FINDINGS.md`, the workspace `translation_instruction.md` |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95: **met** |
| **Date** | 2026-10-06 |
| **Scope** | A full first translation written directly at native register (no machine draft): 35 chapters and 35 solution twins, **70 files**, every body through `tools/id_apply.py`. Also the French image-credits page, a curated `tools/term_config/book3_fr.py`, the defined-term link layer, French index keys, the overfull, figure and page-break sweeps, and this score |

## Verdict in one line

This French Book 3 reads as a French second-year (PC / L2) chemistry course: *grandeur de réaction*, *enthalpie libre*, *variance* and *règle des phases*, *RPAC / réacteur en écoulement piston*, *diagramme d'Ellingham*, *courbes intensité–potentiel* with *mur du solvant* and *potentiel mixte*, *CLOA*, *méthode de Hückel*, *ESCC*, *aldolisation / crotonisation*, *annélation de Robinson*, *ylure*, *IGF*, *CPG / CLHP*, *HEPT*, *incertitude-type*, *ajouts dosés*, the infinitive exercise register and French spaced punctuation. Every gate is green on a forced build: **0 errors / 0 undefined / 0 overfull / 0 nullfont / 0 Missing character / 0 invalid in math mode**.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | All 70 files mirror their twins. Counts (EN = FR): `exercise` 420, `problem` 35, `solution` 455, `[resume]` 105, `omfigure` 188, `tikzpicture` 160, `axis` 84, `\node` 585, `\includegraphics` 64, `\emph` 429, `\index` 417 (per file equal), `\cref/\Cref` 195, `\label` 1025 (set diff 0), `\item` 1170, `\qty` 1858, `\num` 21, `\unit` 107. Environments (EN = FR): definition 197, proposition 176, theorem 37, method 76, example 36, proof 202, history 26, safety 14, recall 35, `\admitted` 17, `% ledger:` 174. Additions: two `\clearpage` + `\enlargethispage` page breaks (below) |
| Chemistry fidelity | **99** | `\ce` 2102 = 2102, `\chemfig` 102 = 102, `\schemestart` 30 = 30, `\ghs` 60 = 60, byte-identical in order (gate 12 OK on 70 files). `check_ce_balance.py`: 129 + 70 equations, 0 problems. Never `!chem`. Word-only arrow labels translated (*addition syn*, *addition*, *élimination*, *transfert de proton*, *chauffage*, *aldolisation*, *base*/*Michael*), and — after the coordinator's gate fix — the mixed labels too (`[\ce{H+} ou \ce{HO-}]`, `[puis \ce{H2O}]`) |
| Terminology | **96** | Standard French L2 series, consistent with Book 2 fr (*état standard de référence*, *loi de Hess / Kirchhoff*, *température de flamme adiabatique*, *valeur en eau*, *troisième principe*, *critère d'évolution*, *grandeur molaire partielle*, *coefficient d'activité*, *propriété colligative*, *paramètre intensif indépendant*, *principe de Le Chatelier*, *conversion par passage / recyclage / purge*, *temps de passage*, *emballement thermique*, *aluminothermie*, *équilibre de Boudouard*, *grillage / lixiviation / cémentation*, *conodale*, *règle des moments*, *hétéroazéotrope*, *entraînement à la vapeur*, *fuseau*, *composé défini / fusion congruente*, *rendement faradique*, *contre-électrode*, *potentiel de demi-vague*, *anode sacrificielle*, *règles de Slater*, *intégrale de résonance*, *déterminant séculaire*, *spectroscopie photoélectronique*, *cercle de Frost*, *HOMO/LUMO* (glossed *HO/BV*), *rétrodonation*, *série spectrochimique*, *addition oxydante*, *insertion migratoire*, *précatalyseur*, *TON/TOF*, *ion halogénonium*, *peroxyacide*, *coupure oxydante*, *intermédiaire de Wheland*, *orienteur ortho/para*, *amination réductrice*, *couplage azoïque*, *substitution nucléophile acyle*, *intermédiaire tétraédrique*, *tautomérie céto–énolique*, *énolate cinétique / thermodynamique*, *synthèse malonique*, *réaction haloforme*, *condensation de Claisen*, *ylure stabilisé*, *oxaphosphétane*, *synthon / équivalent synthétique*, *groupes protecteurs orthogonaux*, *polymérisation par étapes / en chaîne*, *amorçage / terminaison*, *dispersité*, *tacticité*, *transition vitreuse*, *zwitterion (amphion)*, *ose*, *carbone anomère*, *massif isotopique*, *coupure α*, *réarrangement de McLafferty*, *découplage large bande*, *justesse / fidélité / répétabilité / reproductibilité*, *limite de détection / quantification*, *atmosphère inerte*, *agent desséchant*, *ampoule de coulée*, *rampe de Schlenk*). All 417 `\index{}` keys are French; every accented key carries an ASCII sort key |
| Register / tone | **97** | Infinitive stems (body): *Calculer* ×273, *Donner* ×98, *Écrire* ×89, *Expliquer* ×55, *Proposer* 25, *Comparer* 25, *Représenter* 25, *Montrer* 19, *Prévoir* 16, *Tracer* 13, *Dessiner* 11. Script audit over course and solutions: **0 *vous***, 0 tutoiement (three conditional *-vous* questions found and made impersonal). House forms as in Book 2: `Problème du week-end --- …`, `Partie I --- …`, `\section*{Chapitre \ref{…} --- …}`; cross-volume *le volume de première / troisième année*, *le volume scolaire*, *(données de l'exercice)* |
| LaTeX hygiene | **99** | Forced build through the shared wrapper: 0 / 0 / 0, `nullfont` 0, Missing character 0, invalid in math 0, **391 pages** (English 373). `.fls`: **70** French sources, 0 English chapter files. 0 TeX accent escapes; spaced punctuation 2244 `~:`, 1327 `~;`, 561 `~?`, 31 guillemet pairs. Line edges swept after the last edit (no elision apostrophe, punctuation or hyphen at a line edge). Twelve overfull boxes of the first build cleared by rewording (never `%`), checked by single-chapter probes |
| Cross-refs / rule compliance | **99** | Labels, `\cref` targets, solution keys, `[resume]`, math spans, image paths and `% ledger:` comments byte-identical to English. No programme, curriculum, country or university named. Shared files touched: only the append-only `ALLOWED_BY_LANG["fr"]` entry in `tools/check_latin_prose.py` (below). No repo-wide git command, no commit |
| Figures | **95** | Drawing code byte-identical except six `!draw` ranges (below). After the first build every figure whose labels grew was rendered at 110–130 dpi and read: four defects fixed by shorter labels — the TOF tube label touching "grilles, U" (ch. 32), the acid–base extraction boxes (hyphenated "ben-zoïque", the NaHCO₃ wash label on the box edge; ch. 35), the modulus curve crossing "plateau caoutchoutique" and "écoulement" (now *plateau élastique*, *s'écoule*; ch. 29). Two weekend problems whose box fills a page had orphaned their heading (ch. 13, 21): `\clearpage` + `\enlargethispage{3\baselineskip}` |
| Solutions | **97** | All 420 exercise and 35 problem solutions present; every number of ch. 20–35 recomputed while translating (Suzuki TON/TOF, limonene H₂ volume, nitrotoluene masses, methyl orange, biodiesel per tonne, dibenzalacetone, Wieland–Miescher, muscalure atom economy, raspberry-ketone atom economies, nylon Carothers chain, aspartame, caffeine HPLC, Pb least squares and s_x0, Grignard purity-corrected yield) — no numeric canon slip found in 20–35. Gate 11 green |
| Defined-term links (`\omterm`) | **95** | **1816 links over 184 targets** vs English **1733 over 179**; **every target English reaches is reached**; French also reaches *domaine d'électroactivité*, *aluminothermie*, *déplacement d'équilibre*, *enthalpie standard de formation*, *groupes protecteurs orthogonaux*. `book3_fr.py` curated from this edition's harvest (427 terms, same 204 targets as English), never seeded. Dry run: **links to insert: 0** |
| MT-artifact freedom | **95** | Gate 10: 0. Gate 9: 0 blocking; one-word tier read in full (*Argument*, *fus/trs/vap/corr*, *Variance*, *Peptides*, *Dihydroxylation*, *potentiostat*… all French). A wider sweep of lines identical to English found three orphans the gates miss (an "and" in ch. 2, "oxygen." and "methanol." after the last answer of solutions 10 and 30): fixed |

**Overall: 96.**

## Gate output summary

```
bash tools/check_translation.sh bachelor-2 fr ..... TRANSLATION GATE: PASSED
  gate 9 .... no multi-word findings (one-word tier advisory, read)
  gate 10 ... orphan English lines: 0
  gate 12 ... chemistry twin gate: OK (70 files)
forced build (shared wrapper): pages 391, errors 0, undefined 0, overfull 0,
  nullfont 0, Missing character 0, invalid in math mode 0; .fls fr files 70
python3 tools/link_defined_terms.py --book 3 --lang fr -> links to insert: 0
check_ce_balance: 129 + 70 equations, 0 problems
```

## The link layer

Homographs met after their definition, masked in `book3_fr.py` (each documented there): *fragment* (stoplisted; *orbitale de fragment*, *ion fragment* keep links), *variance* (statistical, ch. 29/34), *propagation* (of uncertainty), *amorçage* (a Grignard start), *sélectivité* (chromatographic), *résolution* (resolving power, high-resolution MS, NMR, solving a structure), *résidu* (amino-acid and reaction residues), *nombre de plateaux* (a distillation column in solutions 07), and — found by the coordinator's chapter-set census — *indices de liaison* in ch. 16 (the Hückel π bond indices, which had linked 4 times to ch. 14's diatomic bond order; now masked, as English links neither; the bond-order target now matches English, 31 links, ch. 14 and its solutions only). `EXTRA`: *nœuds radiaux*, *plateaux théoriques* (irregular plurals), bare *conversion(s)* (as English links it), *nombre de plateaux* / *hauteur de plateau* (ch. 31 plate number). Every risky target's contexts were read after linking.

## Edits outside the patch applier (recorded)

- **`!draw` ranges, six:** 08 EN 61 (cooling-curve `\foreach` labels); 19 EN 240 (colour-wheel names, keys untouched); 20 EN 131–135 (cycle step names); 23 EN 187–188 (*à chaud*, *activé*); 24 EN 201 (reactivity ladder); 31 EN 78 (*début, plus tard, fin*).
- **Post-apply text edits:** solutions/15 item 24 `\textbf{quatre}` (canon now `\textbf{four}`); the coordinator's canon edits mirrored (solutions/11 item 7, solutions/20 ex. 8, solutions/07 item 12, ch. 10 index adjacency, ch. 32 ex. 8, solutions/15; then solutions/01 items 11–15, solutions/03 item 10, ch. 14 l. 423 bond orders; ch. 23's *1,3,5-tribromobenzène* was already on one line); the mixed arrow labels 25/31, 26/94, 26/100 translated after the gate fix; the temporary comments on the `\pgfplotsset` lines 32/161 and 33/124 removed once gate 10 learned to skip those bodies; three orphan lines removed; three *vous* questions made impersonal; ch. 17 two `\index{}` joined to their `\emph{}`.
- **Overfull clearing by rewording:** ch. 3 (Euler proof), 5 (series-reaction proof), 16, 28 (two-group table cells), solutions 14, 20 (`\-` hints in *4-méthoxy\-phényl\-boronique*), 21, 25 (×2), 27, 29 (×2).
- **Layout:** `\clearpage` + `\enlargethispage{3\baselineskip}` before the weekend problems of ch. 13 and 21.

## Suspected English-canon defects (reported)

1. `parts/bachelor-2/solutions/17-frontier-orbitals.tex`, ex. 4 (lines 21–23): the CN position was misleading; now fixed in the canon ("on one of the two ring carbons formed from the dienophile") and mirrored: *l'un des deux carbones du cycle issus du diénophile*.
2. Arrow labels mixing `\ce{}` and words (25/31 *or*, 26/94, 100 *then*): now handled by the gate fix; a canon form `[1. \ce{CH3Li}][2. \ce{H2O}]` (as ch. 21 l. 263) would avoid the word altogether.
3. Subscripts in `\mathrm{}` (*theo, caf, ref, opt, lim, acc, ad, eq*) kept as abbreviations in French; *blank, LOD, LOQ* translated (*blanc, LD, LQ*).

## Gate / tool bugs met

- `tools/check_orphan_lines.py`: `\pgfplotsset{…}` key lines outside a drawing environment (32/149–153, 33/116–118) read as prose (*every*). Fixed by the coordinator during the run.
- `tools/id_apply.py` / `check_chem_twin.py` (before today's fix): a mixed `\ce` + word arrow label was frozen whole, so gates 10 and 12 could not both pass.
- `tools/check_latin_prose.py`: the `Schröder` tokeniser split (already reported by pt). **Allow-list appended** to `ALLOWED_BY_LANG["fr"]`: *endo, exo* (Diels–Alder `\foreach` keys, 17/308), *zwitterion* (legend 30/76, the French term), *van, der* (title "Schröder--van Laar", 08/198).

## Why not 100

- Local TeX Live has no French hyphenation: the line breaks (and the overfull rewording) were tuned under English patterns; CI will hyphenate differently.
- Six `!draw` ranges and four shortened figure labels are guarded only by the rendered PDF.
- Link density +5 % against English, from French single-word forms (*conversion*, *enthalpie libre*, *indice de liaison*).
- Register audited by script; some long proofs still follow the English sentence boundaries.

## Coordinator addendum (2026-10-07)

The bare noun of the "Enolates" definition (`def:b2:enolates-aldol:enolate`) was
linked once in English and in this edition, because only the "enolate ion"
phrase was harvested; the Arabic edition exposed it. An `EXTRA` entry was added
here and in English (79 links). This edition now has **1893 links over 185
targets** (English 1,811 over 180); gates, dry run (0) and chapter-set census
re-checked. Later canon fixes carried in by the coordinator are listed in
`sources/WAVE1_FINDINGS_B34.md` and `WAVE2_FINDINGS_B34.md`. Score unchanged.
