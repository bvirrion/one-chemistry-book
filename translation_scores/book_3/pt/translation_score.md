# Translation score — Chemistry Book 3 · Brazilian Portuguese (`pt`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 3 (University Chemistry, Year 2 — year `bachelor-2`, labels `b2`) |
| **Language** | Brazilian Portuguese (`pt`), one variety throughout |
| **Quality bar** | **native academic prose**: a Brazilian second-year university chemistry course as it is written and taught. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **References measured before drafting** | the **English** canon (content); the shipped **Portuguese Book 2** (`parts/bachelor-1/pt/`, `book2_pt.py`, its score) for series terminology and register; Portuguese Book 1 for school-level vocabulary (*CCD*, *salmoura*, *grupo protetor*) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95: **met** |
| **Date** | 2026-10-06 |
| **Scope** | A full first translation written directly at native register (no machine draft), every body through `tools/id_apply.py`: 35 chapters and 35 solution twins, **70 files**. Also the Portuguese image-credits page, a curated `tools/term_config/book3_pt.py`, the link layer, Portuguese index keys, the overfull and per-figure sweeps, and this score |

## Verdict in one line

This Portuguese Book 3 reads as a Brazilian second-year chemistry course
(*grandeza de reação*, *energia de Gibbs de reação*, *aproximação de Ellingham*,
*potencial químico*, *regra das fases*, *curva corrente--potencial*,
*sobretensão*, *CLOA*, *orbitais de fronteira*, *desdobramento do campo
cristalino*, *adição oxidativa*, *substituição nucleofílica acílica*,
*anelação de Robinson*, *ilídeo de fosfônio*, *síntons*, *CLAE*, *incerteza-padrão*),
in the imperative *você* register of Book 2, with every gate green, and a forced build at **0 errors /
0 undefined / 0 overfull / 0 nullfont / 0 Missing character**.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | 70 files mirror their 70 twins. EN = PT: `exercise` 420, `problem` 35, `solution` 455, `omfigure` 188, `tikzpicture` 160, `axis` 84, `\label` 1025, `\item` 1170, definition 197, proposition 176, theorem 37, method 76, example 36, proof 202, `\emph` 429, `\index` 417, `\qty` 1858, `\includegraphics` 64, `% ledger:` 174. `\cref`+`\Cref` 140 = 140 (one `\Cref` became `\cref` mid-sentence in ch. 28). A per-file multiset comparison of **every number** in course and solutions: identical to English everywhere |
| Chemistry fidelity | **98** | `\ce` 2102 = 2102, `\chemfig` 102 = 102, `\schemestart` 30 = 30, `\ghs` 60 = 60. `check_ce_balance.py`: 129 + 70 equations, 0 problems. Arrow labels translated through the word-only blanking (*adição*, *eliminação*, *transferência de próton*, *aquecimento*, *calor*, *aldólica*, *catálise*, *adição syn*). Two **mixed** labels (formula + word) were translated too — `[\ce{H+} ou \ce{HO-}]` (ch. 25) and `[depois \ce{H2O}]` ×2 (ch. 26) — accepted by the corrected gate 12 (it now compares only the `\ce{}` and `$…$` parts of a mixed label) |
| Terminology | **96** | Brazilian university usage, one glossary across 35 chapters, Book 2 renderings kept where they exist (*par não ligante*, *pilha / meia-pilha*, *potencial de eletrodo*, *ponte salina*, *grau de insaturação*, *deslocamento químico*, *reagente de Grignard*, *haloalcano*, *incerteza-padrão / desvio-padrão*, *fator de retenção*, *CCD*). New: *variância*, *parâmetro intensivo independente*, *reator contínuo de tanque agitado / de escoamento pistonado*, *disparo térmico*, *ustulação / lixiviação / cementação*, *curva de bolha / de orvalho*, *heteroazeótropo*, *patamar*, *liquidus / solidus*, *barreira do solvente*, *janela de eletroatividade*, *ânodo de sacrifício*, *proteção por corrente impressa*, *combinação adaptada à simetria*, *retrodoação*, *eliminação de hidreto β*, *ilídeo estabilizado*, *oxafosfetano*, *interconversão de grupos funcionais (IGF)*, *grau de avanço* (p of Carothers), *polimerização viva*, *zwitteríon*, *mutarrotação*, *cromatografia líquida de alta eficiência (CLAE)*, *tempo morto*, *perfil isotópico*, *espectrometria de absorção atômica (EAA)*, *veracidade / viés / repetibilidade / reprodutibilidade*, *tratamento* (work-up). All 417 `\index` keys Portuguese, every accented key with an ASCII sort key, no sort key with two displays |
| Register / tone | **97** | Imperative *você* stem throughout, same distribution as Book 2: *Calcule* ×279, *Dê* ×106, *Escreva* ×89, *Explique* ×55, *Desenhe* ×40, *Compare* ×25, *Encontre* ×23, *Deduza* ×20, *Verifique* ×19, *Mostre* ×19. 0 *tu*, 0 *vós*. European-Portuguese sweep (*facto, equipa, registo, acção, electr-, secção, protões, iões, catião, -génio …*) over course and solutions: 0 outside labels/slugs; *óptica / opticamente* as in Book 2. Decimal point everywhere, `` '' quotes |
| LaTeX hygiene | **99** | Forced build through the shared wrapper (`latexmk -g`, capped scope): **0 errors, 0 undefined, 0 overfull, nullfont 0, Missing character 0, invalid in math mode 0**, **381 pages** (English 373). `.fls`: **70** Portuguese sources. Eleven overfull boxes from the first build cleared by rewording (never `%`), each confirmed in a single-chapter probe: ch. 1, 3, 4 (×2), 8, 10, 28 (table), solutions 18 (discretionary hyphens in three complex names), 21, 23, 32. No line starting on punctuation, no line-end hyphen, no doubled word, no article/gender mismatch before `\cref` |
| Cross-refs / rule compliance | **98** | Labels, solution keys, `[resume]`, image paths and `% ledger:` comments byte-identical. Cross-volume references in prose only (*o volume do 1.º ano*, *o volume do 3.º ano*, *o volume escolar*). No programme or country named. Shared file edited: `tools/check_latin_prose.py`, one appended, reasoned `pt` allow-list entry. No repo-wide git command, no commit, no other edition or English file touched |
| Figures | **95** | Drawing code byte-identical except the six `!draw` ranges and the label edits below. **Per-figure check:** the 134 figures whose drawing text was translated were located (117 pages), rendered one page per figure at 130 dpi and read. **Thirteen collisions fixed**, by label text or size only, never by moving a coordinate: calcite region label (ch. 2), cooling-curve caption (ch. 8), Zn/H₂ note (ch. 11), *retificador* box (ch. 12), CO σ label (ch. 14), Wilkinson centre label (ch. 20), saponification and aldol scheme arrows (ch. 24, 25: `\setchemfig{arrow coeff}` outside the scheme), Robinson *calor* (ch. 26), *escoa* (ch. 29), time-of-flight tube label (ch. 32), acid–base wash labels (ch. 35), and the untranslated axis title *1-bromopropano* (ch. 32). Every fix re-rendered from the final build |
| Solutions | **97** | All 420 exercise and 35 problem solutions present and re-read against their questions while translating; the numbers recomputed where a slip was possible (ch. 4, 7, 11, 20, 23–35 in full). Gate 11 (problem numbering) green |
| Defined-term links (`\omterm`) | **95** | **1785 links over 182 targets**, English **1733 over 179**. **Every target English links is reached (0 missed)**; Portuguese also reaches three English never links, each in the defined sense (*entalpia padrão de formação* ×2, *deslocamento do equilíbrio* ×2, *barreiras do solvente*). No target differs from English by more than +10 (*energias de Gibbs*: English cannot match its own plural "Gibbs energies"). `book3_pt.py` curated from this edition's harvest (418 terms, 0 defined twice, 477 linkable), never seeded; `--apply` twice changes nothing; dry run **links to insert: 0** |
| MT-artifact freedom | **96** | Gate 10 (orphan lines) 0. Gate 9: **0 blocking**, 118 advisory one-word hits all read: subscripts (*fus, trs, vap, corr, cat, Ox/Red*), symbols and units, eponyms (*Raoult, Henry, Wheland, Fenske, Gibbs--Konovalov*), cognates (*ideal, metal, detector, compressor, liquidus, linear, normal, base*). Three real English leftovers found by a separate word scan and fixed (*and* ×2 between formulas, *Haber and Bosch*); `\text{gas}` ×27 → `\text{gás}`, `\text{heat}` → `\text{calor}`, `\mathrm{blank/LOD/LOQ/theo}` → *branco / LD / LQ / teo* |

**Overall: 96.**

## Gate output summary

```
bash tools/check_translation.sh bachelor-2 pt ....... TRANSLATION GATE: PASSED
  gates 1-8, 10, 11, 13 .... green
  gate 9 ................... no multi-word findings; 118 one-word (advisory, read)
  gate 12 .................. chemistry twin gate: OK (70 files)
python3 tools/check_orphan_lines.py ... 0
forced build build/one_chemistry_book_3_university_year_2_pt.log
  errors 0 · undefined 0 · Overfull 0 · nullfont 0 · Missing character 0
  invalid in math mode 0 · pages 381 (EN 373) · .fls pt sources 70
python3 tools/link_defined_terms.py --book 3 --lang pt  -> links to insert: 0
```

## The link layer

Homographs met after their definition, masked in `book3_pt.py`: bare
***fragmento(s)*** stoplisted (ch. 15's method vs ozonolysis, synthon and
mass-spectrum fragments; *orbital de fragmento*, *íon fragmento* keep theirs);
statistical ***variância*** (ch. 29, 34); ***propagação*** of uncertainties and
***iniciação*** of a Grignard (ch. 34, 35); chromatographic ***seletividade***;
***poder de resolução***, high-resolution analysers, spectral and
structure-solving ***resolução*** (ch. 32–33); the TLC ***fator de retenção
$R_f$***; flushing with nitrogen (***antes da purga***); waste
(***menos resíduos***). `DERIVED`: the irregular plurals present in the text
(*orbitais moleculares/ligantes*, *potenciais químicos*, *sobretensões*,
*soluções sólidas*, *nós radiais*, *ordens de ligação* …), the gender forms
(*aromática*, *exotérmico*, *paramagnético*, *isotático* …), and *aldólica /
retroaldólica* for English "aldol" used adjectivally.

## Edits outside the patch applier (recorded)

- **`!draw` ranges, six (six files):** 08/61 (cooling-curve labels), 19/240 (colour wheel), 20/131–135 (cycle step names), 23/187–188 (*a quente*, *ArH ativado*), 24/201 (reactivity ladder), 31/78 (*início, depois, fim*).
- **Post-apply math edits:** `pt/10` `\text{ET}/\text{ER}`; `\text{gas}` → `\text{gás}` (ch. 1, 2, 4, 6 and solutions); `pt/09` `\text{calor}`; `solutions/31` `k_{\mathrm{teo}}`; `pt/34`, `solutions/34` `s_{\mathrm{branco}}`, `x_{\mathrm{LD}}`, `x_{\mathrm{LQ}}`.
- **`\setchemfig{arrow coeff=…}`** before the second scheme of ch. 24 and 25 (outside `\schemestart`; chemistry census unchanged).
- **Coordinator follow-up (2026-10-06), canon edits mirrored:** solutions 11 (*quase metade*), 20 (*seis*), 15 (`\textbf{quatro}`), 32 exo 8 (*apenas um pequeno pico em 58*), solutions 07 (0.455), solutions 01 (0.29 %, 334.5 ×3), solutions 03 (2 % a cada 3 K), 14 (2.5 e 2.5 contra 3 e 2); 10 and 23 already correct in pt; no `\index{}` before punctuation is preceded by a space or line break. The two `\pgfplotsset` lines of 32 and 33 restored to the English layout.

## Suspected English-canon defects (all fixed in the canon by the coordinator and mirrored here)

1. `parts/bachelor-2/solutions/11-batteries-electrolysis.tex` l. 83 (pb item 7): "pays about a third of the work" — 1.03/2.21 = 0.47, nearly half (pt: *quase metade*).
2. `parts/bachelor-2/solutions/20-catalytic-cycles.tex` l. 46–47 (exo 8): "18 with seven coordination positions" — the oxidative-addition product of RhCl(PPh₃)₃ + H₂ is six-coordinate (pt: *seis*).
3. `parts/bachelor-2/solutions/15-fragment-orbitals.tex` l. 116: `$\boldsymbol{four}$` typesets an English word in math italic.
4. `parts/bachelor-2/10-current-potential-curves.tex` l. 64–65: `\emph{counter electrode}` newline `\index{counter electrode},` prints "counter electrode ," (space before the comma).
5. `parts/bachelor-2/32-mass-spec-atomic.tex` exo 8 says pentan-3-one "shows no peak at 58", while `solutions/32` l. 42 explains "its small peak at 58".
6. Minor: `solutions/07` l. 116 (pb item 12) y = 0.456 vs 0.455 elsewhere.

## Gate / tool bugs met (the first two fixed by the coordinator)

- **Gates 12 and 10 conflict on mixed arrow labels.** `id_apply`/`check_chem_twin.py` blank an arrow label only when it carries no macro, so `[\ce{H+} or \ce{HO-}]` and `[then \ce{H2O}]` must stay byte-identical; but kept, `then` is flagged by `check_orphan_lines.py`. A correct translation therefore fails gate 12 on exactly two spans (25/31, 26/94). Proposed fix: in `_blank_arrow_labels`, blank the words outside `\ce{}` in a mixed label and compare only its `\ce{}` parts. (`id_apply` needed `!chem` to write those ranges.)
- **`check_orphan_lines.py`** flags pgf keys (*every node near coord*, *every axis plot*) in `\pgfplotsset` lines outside a `tikzpicture` (32/155, 33/121); worked around by re-breaking the code lines.
- **`check_latin_prose.py` LOWER_WORD is ASCII-only:** "Schröder" is read as "Schr" + "der". Allow-list entry appended for `pt`: *endo, exo, syn, meso, van, der* (the 17 Diels–Alder `\foreach` keys, the 21 node "syn: meso", the 08 title "Schröder--van Laar").

## Why not 100

Six `!draw` files and thirteen figure
label edits are guarded only by the rendered pages (all re-read); and a native
reviewer would still find a few literal turns in the longer proofs.

## Coordinator addendum (2026-10-07)

The bare noun of the "Enolates" definition (`def:b2:enolates-aldol:enolate`) was
linked once in English and in this edition, because only the "enolate ion"
phrase was harvested; the Arabic edition exposed it. An `EXTRA` entry was added
here and in English (79 links). This edition now has **1862 links over 183
targets** (English 1,811 over 180); gates, dry run (0) and chapter-set census
re-checked. Later canon fixes carried in by the coordinator are listed in
`sources/WAVE1_FINDINGS_B34.md` and `WAVE2_FINDINGS_B34.md`. Score unchanged.
