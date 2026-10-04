# Translation score — Chemistry Book 2 · Brazilian Portuguese (`pt`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 2 (University Chemistry, Year 1 — year `bachelor-1`, labels `b1`) |
| **Language** | Brazilian Portuguese (`pt`), one variety throughout |
| **Quality bar** | **native academic prose**: a Brazilian first-year university chemistry course as it is written and taught. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **References measured before drafting** | the **English** canon (content); the shipped **Portuguese Book 1** of this repo (`parts/grade-*/pt/`) for series terminology (*CCD*, *banco de Kofler*, *salmoura*, *barrilha*, *cal virgem*, *grupo protetor*, *ponto de fusão* in the laboratory); the Portuguese **Biology Book 3** for the register (imperative *você* stems); the **French** Book 2 as a same-book sense reference |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95: **met** |
| **Date** | 2026-10-04 |
| **Scope** | A full first translation written directly at native register (no machine draft): 29 chapters and 29 solution twins, **58 files**. Also the Portuguese image-credits page, a curated `tools/term_config/book2_pt.py`, the defined-term link layer, Portuguese index keys, the overfull and per-figure sweeps, and this score |

## Verdict in one line

This Portuguese Book 2 reads as a Brazilian first-year chemistry course: the
vocabulary of Brazilian university chemistry (*avanço da reação*, *reação
predominante*, *diagrama potencial–pH*, *célula unitária*, *número de
coordenação*, *aproximação do estado estacionário*, *desproporcionamento*,
*titulação de retorno*, *deslocamento químico*, *incerteza-padrão*), the
imperative *você* exercise stem, Brazilian spelling (*próton*, *elétron*,
*íon*, *hidrogênio*, *seção*, *fator*), and every structural, chemistry, prose
and link gate green on a forced build: **0 errors / 0 undefined / 0 overfull /
0 nullfont**.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | All 58 files mirror their 58 twins. Counts (EN = PT): `exercise` 348, `problem` 29, `solution` 377, `[resume]` 87, `omfigure` 148, `tikzpicture` 96, `axis` 47, `\node` 587, `\includegraphics` 49, `\emph` 390, `\index` 364, `\label` 829, `\item` 916, `\qty` 1474, `\num` 67, `\unit` 62. Environments (EN = PT): definition 162, proposition 128, theorem 6, method 52, example 60, proof 109, remark 21, recall 29, inthelab 11, history 11, safety 2, `\admitted` 19, `% ledger:` comments 150. The `\label` set diff is 0. `\cref` 214 against 221 and `\ref` 36 against 29: the seven section references were rewritten as `Seção~\ref{…}` (see "Gate / tool bugs"). Every file was written through `tools/id_apply.py` |
| Chemistry fidelity | **99** | `\ce` 3432 = 3432, `\chemfig` 101 = 101, `\schemestart` 23 = 23, `\ghs` 16 = 16, byte-identical in order (gate 12, chemistry twin: OK on 58 files). `check_ce_balance.py`: 125 + 148 equations, 0 problems. Never `!chem`. Arrow labels translated through the census's word-only blanking: `->[lenta]`, `->[rápida]`, `->[heterólise]`, `->[piridina]`, `->[(majoritário)]`, `->[migração 1,2]` |
| Terminology | **96** | Brazilian university usage, settled per chapter and kept in one glossary: *níveis de energia*, *caixas quânticas*, *carga nuclear efetiva*, *blindagem*, *estrutura de Lewis*, *híbrido de ressonância*, *número estérico*, *célula unitária*, *compacidade*, *habitabilidade*, *tipo sal-gema / blenda / fluorita*, *avanço da reação*, *taxa de avanço final*, *quociente de reação*, *meia-vida*, *método do isolamento*, *etapa determinante da velocidade*, *aproximação do estado estacionário*, *reação predominante*, *solução equivalente*, *efeito nivelador*, *escala de pL*, *eletrodo padrão de hidrogênio*, *potencial padrão*, *desproporcionamento / comproporcionamento*, *domínio de passivação*, *titulação de retorno*, *faixa de viragem*, *lei de Kohlrausch*, *representação de Cram*, *cadeira / inversão do anel*, *dextrogira / levogira*, *poder rotatório específico*, *deslocamento químico*, *blindagem magnética*, *regra do n + 1*, *grau de insaturação*, *efeito mesomérico*, *inversão de Walden*, *solvólise*, *antiperiplanar*, *regra de Zaitsev*, *inversão de polaridade*, *alcóxido*, *síntese de Williamson de éteres*, *éster sulfonato*, *hemiacetal*, *grupo protetor*, *nível de oxidação*, *reação quimiosseletiva*, *íon halônio*, *rearranjo de carbocátion*, *hidreto salino*, *efeito do par inerte*, *composto inter-halogênio*, *palavra de advertência*, *frase de precaução*, *ficha de dados de segurança*, *incerteza-padrão*, *avaliação do tipo A / B*, *incerteza expandida*, *desvio normalizado*, *fator de retenção*. All 364 `\index{}` keys are Portuguese; every accented key carries an ASCII sort key; the 5 keys identical to English are true cognates (*acetal*, *hemiacetal*, *axial*, *equatorial*, *radical*) |
| Register / tone | **97** | The exercise stem is the Brazilian imperative: *Calcule* ×203, *Escreva* ×127, *Dê* ×56, *Explique* ×51, *Desenhe* ×44, *Mostre* ×37, *Deduza* ×19, *Compare* ×15, *Verifique* ×15, *Expresse* ×14, *Proponha* ×12, *Balanceie* ×12. 0 *tu*, 0 *vós*; *você* only where English addresses the reader (7). A script sweep for European-Portuguese markers (*facto, equipa, ecrã, registo, contacto, acção, objecto, electr-, secção, protões, iões, catião, -génio, fenómeno, estar a + infinitive*) over course **and** solutions finds 0 outside code. House forms: `Problema de fim de semana --- …`, `Parte I --- …`, solution headers `\section*{Capítulo \ref{…} --- título}`. Cross-volume references read *o Livro 1 (ano 10)* and *o volume do 2.º ano*; no programme is ever named |
| LaTeX hygiene | **99** | Forced build (`latexmk -g`, inside the memory-capped `systemd-run` scope): **0 errors, 0 undefined, 0 overfull, `Missing character` 0, 0 `invalid in math mode`**, **300 pages** (English 293). `.fls`: **58** Portuguese sources. 0 TeX accent escapes, valid UTF-8, 0 straight quotes in prose, no line starting on `. , ; : ) ? !`, no line-end hyphen. Six overfull boxes from the first build were cleared by rewording (never with `%`): `pt/06` comparison table, `pt/11` zincate proof, `pt/28` contact-process box, solutions 10, 20 and 21. No orphaned heading at a page foot |
| Cross-refs / rule compliance | **98** | Labels, solution keys, `[resume]`, math spans (with the exceptions listed below), image paths and `% ledger:` comments are byte-identical to English. No programme, curriculum, country or university name in visible text. No English source, preface or other edition was touched. Shared file edited: `tools/check_latin_prose.py`, one reasoned `pt` allow-list entry, reported. No repo-wide git command, no commit |
| Figures | **96** | All TikZ / pgfplots / chemfig code is byte-identical except two `!draw` ranges (below). Only node text, axis labels, legends, tick labels, table cells and captions were localized. **Per-figure check:** the 78 pages carrying the 90 figures whose drawing text was translated were rendered one page per figure at 130 dpi and read. **Fifteen collisions were found and fixed**, all by label text only (line breaks, size, wording), never by moving a coordinate: the two hydration-shell captions (ch. 4), "tangente em t = 0" (ch. 8), "barreira" and "B (estado estacionário tracejado)" (ch. 9), "inversão" and the polarimeter sample (ch. 16), the colour-wheel labels (ch. 17), "(majoritário)" (ch. 22, by a longer arrow via `\setchemfig`), the 1,2-shift label (ch. 25, likewise), the Haber–Bosch and Pt–Rh boxes (ch. 27), the contact-process "parte volta" (ch. 28), and "entrada de água" / "manta aquecedora" (ch. 29). Every fix was re-rendered and re-read |
| Solutions | **97** | All 348 exercise solutions and 29 weekend-problem solutions present. Every number in ch. 1–29 was recomputed while translating (the Solvay, Bayer, contact and Ostwald balances, MTBE, the Grignard yields, the adipic-acid electron count, the lithium brine, the uncertainty budgets of ch. 29 including the 32-portion limit of exercise 10). Multi-line math spans keep their English line breaks, as `id_apply`'s math census requires. Gate 11 (problem numbering) green |
| Defined-term links (`\omterm`) | **95** | **2588 links over 146 distinct targets**, against English's **2470 over 144**. **Every target English links is reached** (0 missed); Portuguese also reaches two English never links, both in the defined sense (*blindagem* ×2 in ch. 2, *efeito nivelador* ×2). `book2_pt.py` was curated from this edition's own harvest (392 terms on the same targets as English; 444 linkable after the irregular plurals), never seeded. `--apply` run twice changes nothing; the plain dry run reports **links to insert: 0** |
| MT-artifact freedom | **96** | Gate 10 (orphan lines): **0**. Gate 9 (twin prose comparison): **0 blocking findings**, 27 advisory one-word findings, all read: eponyms (*Lyman, Balmer, Paschen, Fischer, Cram, Pauling*), cognates (*bases, linear, acetal, axial, equatorial, syn, anti, gauche*), symbols (`(mol/L)`, `δ (ppm)`) and the abbreviations *inv / ret* (*inversão / retenção*). The `\text{}` census over course and solutions leaves only symbols or Portuguese words identical to English. Four English subscripts the census cannot see were translated after application: `\mathrm{dissolved}` → `dissolvido` (sol. 11), `V_{\mathrm{flask}}/V_{\mathrm{aliquot}}` → `V_{\text{balão}}/V_{\text{alíquota}}` (sol. 15), `d_{\mathrm{front}}` → `d_{\mathrm{frente}}` (ch. 29, node and caption) |

**Overall: 96.** The weighting favours terminology, register, link curation and MT-artifact freedom; structure and build are gated mechanically.

## Gate output summary

```
bash tools/check_translation.sh bachelor-1 pt ............ TRANSLATION GATE: PASSED
  gates 1-8, 10, 11, 13 .... green (completeness, structure, hygiene, UTF-8,
                             orphan lines 0, problem numbering, ce balance)
  gate 9 ................... no multi-word findings; 27 one-word (advisory, cognates)
  gate 12 .................. chemistry twin gate: OK (58 files)
python3 tools/check_latin_prose.py parts/bachelor-1/pt parts/bachelor-1/solutions/pt  rc 0
python3 tools/check_orphan_lines.py  parts/bachelor-1/pt parts/bachelor-1/solutions/pt  0

forced build build/one_chemistry_book_2_university_year_1_pt.log (grep -a)
  '^!' 0 · undefined 0 · Overfull 0 · Missing character 0
  'invalid in math mode' 0 · pages 300 (EN 293) · .fls pt sources 58

python3 tools/link_defined_terms.py --book 2 --lang pt     -> links to insert: 0
\index 364 = 364 · \label set diff 0 · \qty 1474 = 1474 · \ce 3432 = 3432
```

## The link layer: what the censuses found

Portuguese homographs met **after** their definition, each handled in
`book2_pt.py` with its evidence:

- ***forte / fraco / fraca*** (acid strength / any strength): stoplisted **and dropped**, as the French edition does: a stoplisted bare adjective still falls through the per-chapter map of ch. 10.
- ***grupo*** links only before a number; the four linkable *grupo …* terms put the modifier after the noun and are excluded by a lookahead.
- ***ligante*** is both a LIGAND (ch. 12) and the adjective "bonding" of the VSEPR table of ch. 28 (*domínios ligantes*, *6 ligantes*): masked there. English has two words; Portuguese one.
- ***rede*** is both the crystal LATTICE and a NETWORK (the hydrogen-bond network of ice, the covalent network of graphite and silica): the network uses are masked, as English links only "lattice".
- ***blindagem*** is screening (ch. 2) and, inside the ch. 17 proof, NMR shielding (*fator de blindagem*): masked there; the NMR term *blindagem magnética* keeps its own target.
- ***nós*** (lattice nodes) vs the pronoun (*para nós*, ch. 16): masked.
- ***atividade*** in *perda da atividade* (optical activity, ch. 19), ***multiplicidade*** of an NMR signal, ***hidratação dos íons***, ***posições axiais / equatoriais*** (VSEPR), ***proteção*** in its personal-protection senses, ***período de indução***, ***blocos de zinco***, *quantitativa* as the adjective of a theory or a measurement, ***perigo à saúde*** and `\emph{Perigo}` (pictogram name, signal word), and the GHS03 caption ***oxidante*** (a hazard class, not the redox oxidant): masked.

Forms the harvest cannot derive, added to `DERIVED` and kept only where the
form occurs in this edition: the irregular plurals in *-ção → -ções*, *-al →
-ais*, *-el → -eis*, *-il → -is*, *-em → -ens* (*ligações de hidrogênio* ×50,
*cristais*, *configurações*, *potenciais padrão*, *variáveis intensivas*…); the
singulars of the terms defined in the plural (*enantiômero*,
*diastereoisômero*, *estereoisômero*, *parâmetro de rede*, *nó*); the gender
forms *hidrofílica / hidrofóbica*, *cúbico de faces centradas*, *hexagonal
compacto*; and the short form *etapa determinante* that Portuguese uses for the
defined *etapa determinante da velocidade* (English writes the full term).

No target exceeds English by more than 1.4×. The largest positive differences
are all the defined sense: *enantiômero(s)* +17 (the singular, which English
never matches), *eletronegatividade(s)* +11 and *atividade(s)* +11 (Portuguese
repeats the noun where English uses a pronoun), *ligações de hidrogênio* +8.

## Samples (Portuguese, with verdict)

1. **ch. 7**, the reaction quotient: «o produto das atividades dos produtos dividido pelo dos reagentes, cada uma elevada à potência de seu coeficiente estequiométrico». **Native.**
2. **ch. 22**, Williamson: «Volumoso do lado do alcóxido, pequeno do lado do haleto.» **Native.** A verbless closing maxim, as a Brazilian teacher sums up.
3. **ch. 26**, the opening: «Todo celular, notebook e carro elétrico leva uma bateria cujas cargas positivas são transportadas por íons lítio.» **Native** and Brazilian (*celular*, *notebook*).
4. **ch. 27**, Haber: «a química que alimenta metade da humanidade e a química que mata estão separadas pelas escolhas dos químicos». **Native.**
5. **ch. 29**, the opening: «uma medida só vale algo com sua incerteza, e uma comparação só com uma regra». **Native.** The parallel *só … com* with the verb elided.

## Edits outside the patch applier (recorded)

- **`!draw` ranges, two:**
  - `bachelor-1/16`, EN line 199: the carvone `\foreach` labels, *hortelã / alcaravia*.
  - `bachelor-1/17`, EN line 68: the colour-wheel `\foreach`, *vermelho, laranja, amarelo, verde, azul, violeta* (each later wrapped in `\footnotesize` against a collision).
- **Two `\setchemfig` arrow lengths** (outside any `\schemestart`, so the chemistry census is unchanged): `pt/22` a `\setchemfig{arrow coeff=1.8}` line before the second dehydration scheme, `pt/25` `arrow coeff=1.2` added to the existing `\setchemfig`. Both make room for the translated arrow label.
- **Post-apply edits inside math spans, four sites:** `solutions/pt/11` `\mathrm{dissolvido}`, `solutions/pt/15` `\text{balão}/\text{alíquota}`, `pt/29` `d_{\mathrm{frente}}` ×2.
- **Section references, seven sites:** `\cref{sec:…}` → `Seção~\ref{sec:…}` in `pt/11` (×4), `pt/14`, `pt/27` and `solutions/pt/11`, because cleveref prints the English "Section" (tool bug below).
- **Overfull clearing:** six overfull boxes cleared by rewording: `pt/06` table (*muito duro, fusão difícil* / *mole, fusão fácil*), `pt/11` zincate proof, `pt/28` *parte volta*, solutions 10, 20 and 21.

## Suspected English-canon defects (reported, not fixed)

1. `parts/bachelor-1/09-elementary-steps.tex`, line 240 (layout): the node `B (steady state dashed)` at `(axis cs:0.8,0.06)` crosses curve A in the right panel; visible in the English PDF, p. 85, and in Portuguese (reduced to `\footnotesize`, still crossing).
2. No content slip was found: every number of the 29 chapters and their solutions was recomputed during translation. The defects the French agent reported earlier (the `day` unit, `\ce{aA -> products}`, "42 times", "more than 2.7 V") are already corrected in the canon this edition was translated from.

## Gate / tool bugs met

- **`styles/onechemistry.sty`, no `\crefname{section}`.** Around line 976 every cleveref name is localized through `\omname…` except `section`, so `\cref{sec:…}` prints the English word **"Section"** in every edition (seen in `pt` p. 95 and p. 121 before the workaround; the same seven `\cref{sec:…}` sit untouched in `fr`, `es`, `nl`, `hi`). This edition wrote `Seção~\ref{…}` instead; the shared fix is a `\crefname{section}{\omnameSection}{…}` pair and one string per language file.
- **`tools/check_latin_prose.py`, `ALLOWED_BY_LANG["pt"]`, appended with a reason:** *butan*, *ol* — the IUPAC name `\cip{S}-butan-2-ol` in the ch. 22 tosylation scheme, spelt identically in Portuguese (the `es` and `fr` agents listed the same two). Not reworded.

## Why not 100

- **Two `!draw` ranges and two `\setchemfig` changes** leave those figures guarded only by the rendered PDF (all re-rendered and read).
- **Seven `\cref` → `\ref` rewrites** depart from the English macro to work round a shared style gap.
- **Link density is +5 %** against English (2588 vs 2470), mostly singulars and repeated nouns English never matches; every high-ratio target was read.
- **Register is measured, not perfect.** The stems, the variety markers and the Brazilian spelling were audited by script; a few long proofs still follow the English sentence boundaries more closely than a Brazilian author would.
