# Translation score — Chemistry Book 2 · Indonesian (`id`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 2 (University Chemistry, Year 1 — year `bachelor-1`, labels `b1`) |
| **Language** | Indonesian (`id`) |
| **Quality bar** | **native academic prose**: a first-year Indonesian university chemistry course (*Kimia Dasar* / *Kimia Fisik* / *Kimia Organik I* register) as it is written and taught. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **References measured before drafting** | the **English** canon (content); the shipped **Indonesian Chemistry Book 1** (`parts/grade-*/id/`) for series terminology and the impersonal *-lah* exercise register; the shipped **Indonesian Biology Book 3** (`../one-biology-book/parts/bachelor-1/id/`) for university register; the **French Book 2** as a sense reference; `sources/TRANSLATION_BOOKS_1-2.md` and `sources/WAVE1-3_FINDINGS.md` |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95: **met** |
| **Date** | 2026-10-04 |
| **Scope** | A full first translation written directly at native register (no machine draft): 29 chapters and 29 solution twins, **58 files**, all written through `tools/id_apply.py`. Also the Indonesian image-credits page, a curated `tools/term_config/book2_id.py`, the defined-term link layer, Indonesian index keys, the overfull and per-figure sweeps, and this score |

## Verdict in one line

An Indonesian Book 2 that reads as a first-year Indonesian university
chemistry course: the vocabulary of Indonesian textbooks (*kemajuan reaksi*,
*kuosien reaksi*, *tetapan kesetimbangan standar*, *tahap penentu laju*,
*reaksi predominan*, *hasil kali kelarutan*, *setengah reaksi*, *diagram
potensial--pH*, *pusat stereogenik*, *pergeseran kimia*, *gugus pergi*,
*pereaksi Grignard*, *biloks*), impersonal *-lah* imperatives, no *kamu/Anda*,
decimal points as in the canon — with every structural, chemistry, prose and
link gate green on a forced build of **0 errors / 0 undefined / 0 overfull /
0 nullfont**.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | All 58 files mirror their 58 twins: `exercise` 348 = 348, `problem` 29 = 29, `solution` 377 = 377, `[resume]` 87 = 87, `omfigure` 296 = 296 (begin+end), `tikzpicture` 192 = 192, `axis` 47 = 47, `\node` 587 = 587, `\includegraphics` 49 = 49, `\emph` 390 = 390, `\index` 364 = 364, `\cref` 221 = 221, `\label` 829 = 829 (set diff 0), `\item` 916 = 916, `\qty` 1475 = 1475, `\num` 67 = 67, `\unit` 62 = 62, `\cip` 132 = 132, `\admitted` 19 = 19; definition 162, proposition 128, proof 109, example 60, method 52 — all equal; `% ledger:` comments 150 = 150, byte-identical |
| Chemistry fidelity | **99** | `\ce` 3432 = 3432, `\chemfig` 101 = 101, all byte-identical in order (gate 12, chemistry twin: OK on 58 files); `check_ce_balance.py` 125 + 148 equations, 0 problems; `% ce-unbalanced-ok` markers kept on their lines. Never `!chem`. Scheme arrow word labels translated through the census's word blanking (`->[lambat]`, `->[cepat]`, `->[heterolisis]`, `->[piridina]`, `->[(utama)]`, `->[pergeseran-1,2]`) |
| Terminology | **96** | Settled per chapter in a running glossary and checked against Indonesian Chemistry Book 1: *penapisan* (Slater) vs *efek perisai* (NMR); *kekompakan*, *keterhunian*, *situs interstisi*, *kubus berpusat muka/badan*, *heksagonal rapat*; *tipe garam batu / sfalerit / fluorit / sesium klorida*; *kemajuan reaksi*, *rasio kemajuan akhir*, *kuosien reaksi*; *hukum laju*, *orde semu*, *waktu paruh*, *sawar*, *keadaan transisi (KT)*, *pendekatan prakesetimbangan / keadaan tunak*; *amfolit*, *efek perataan*, *larutan ekuivalen*; *efek ion senama*, *daerah keberadaan*, *hidroksida amfoter*; *ligan*, *kelat*, *skala pL*; *oksidator/reduktor*, *jembatan garam*, *elektrode hidrogen standar (EHS)*; *daerah imunitas / korosi / pasivasi*; *titrasi balik / berurutan / simultan*, *trayek perubahan warna*; *representasi Cram*, *proyeksi Newman/Fischer*, *aturan CIP*, *konformasi eklips / goyang / anti / gauche*, *kursi*, *pembalikan cincin*; *kopling spin--spin*, *aturan $n+1$*, *derajat ketidakjenuhan*; *efek induktif / mesomeri*, *panah lengkung*, *panah berkepala setengah*, *nukleofilisitas*, *gugus pergi*; *inversi Walden*, *solvolisis*, *anti-periplanar*, *aturan Zaitsev*; *inversi polaritas*, *alkoksida*, *sintesis eter Williamson*, *ester sulfonat*, *hemiasetal*, *gugus pelindung / proteksi / deproteksi*, *perangkap Dean--Stark*; *tingkat oksidasi* (carbon) kept apart from *keadaan oksidasi* (oxidation state, ch. 27); *reaksi kemoselektif*, *ion halonium*, *penataan ulang karbokation*; *hidrida salin / kovalen / metalik*, *oksida basa / asam / amfoter*, *efek pasangan inert*, *fiksasi nitrogen*, *senyawa antarhalogen*, *kalkogen*; GHS: *piktogram bahaya*, *kata sinyal* (*Bahaya* / *Peringatan*), *pernyataan bahaya*, *pernyataan kehati-hatian*, *lembar data keselamatan*; *ketidakpastian baku / diperluas*, *evaluasi tipe A/B*, *deviasi ternormalisasi*, *faktor retensi*, *koefisien partisi*. IUPAC names in Indonesian spelling (*etana-1,2-diol*, *butan-2-on*, *2-metilbut-2-ena*, *asam heksanadioat*). Homographs avoided at the drafting stage: *bongkah seng* (block of zinc), *masa induksi* (induction period), *keadaan oksidasi* (oxidation state). All 364 `\index{}` keys are Indonesian, 0 case duplicates |
| Register / tone | **97** | Impersonal imperatives throughout: *Hitunglah* ×217, *Tuliskan* ×142, *Tentukan* ×63, *Jelaskan* ×54, *Gambarlah* ×51, *Tunjukkan bahwa* ×31, *Nyatakan* ×30, *Turunkan* ×20, *Bandingkan* ×17, *Usulkan*, *Ramalkan*; **0** *kamu / Anda / -mu*. House forms: `\section{Latihan}`, `\section{Soal: …}`, `Soal akhir pekan --- …`, `Bagian I --- …`, solution headers `\section*{Bab \ref{…} --- judul}`; cross-volume references *Buku 1 (kelas 10)*, *jilid sekolah (kelas 12)*, *jilid Tahun 2*; no programme, country or university named |
| LaTeX hygiene | **99** | Forced build (`latexmk -g`, memory-capped `systemd-run` scope): **0 errors, 0 undefined, 0 overfull, `nullfont` 0, 0 `invalid in math mode`**, **305 pages** (English 293); `.fls` **58** Indonesian sources. 11 overfull boxes from the first full build were cleared by re-flowing prose before unbreakable math or `\ce` (ch. 10, 11, 12, 13, 25, solutions 20, 21) and by shortening three figure labels (ch. 2, 28). All files valid UTF-8, 0 TeX accent escapes. Line edges swept after the last edit: no line-end elision, no line-end hyphen, no line starting on punctuation; **0 line-broken `\index{}` keys** (16 found by gate 5 after the last chapter landed, all re-flowed) |
| Cross-refs / rule compliance | **99** | Labels, `\cref` targets, solution keys, `[resume]`, math spans, image paths and `% ledger:` comments byte-identical to English. No English source, preface or other edition touched; no repo-wide git command, no commit. Shared tools edited append-only with reasoned comments (listed below) |
| Figures | **96** | All TikZ / pgfplots / chemfig code byte-identical except the localized text and the re-flows listed here. `!draw` used twice, only for `\foreach` label lists: ch. 16 EN l. 199 (the carvone pair, *mint hijau* / *jintan Belanda*) and ch. 17 EN l. 68 (the colour wheel). Every page carrying a figure with a translated label (115 pages) was rendered at 130 dpi and read one page at a time, after the first build and again after the fixes. **Collisions found and fixed (10):** ch. 3 σ/π overlap legends and the CO₂ dipole label (two lines), ch. 4 hydration-shell captions and the water H-bond label (two lines), ch. 8 tangent label crossing the red tangent (*tangen di t = 0*), ch. 9 steady-state label clipped at the axis (two lines), ch. 12 the three complex-shape labels (two lines), ch. 26 lime-cycle boxes (two lines), ch. 2 isoelectronic-series label and ch. 28 contact-process boxes (overfull figures: *tungku belerang*, *udara,\\S*, *sebagian\\dikembalikan*). One text slip found on a rendered page and fixed (ch. 19: a doubled *gugus pergi* in one sentence) |
| Solutions | **97** | All 348 exercise solutions and 29 weekend-problem solutions present and native. Every number in ch. 21–29 was recomputed while translating (Grignard yields, MTBE, acetal/Dean–Stark, adipic acid/N₂O, lithium brine balance, Solvay, Bayer, Haber–Ostwald, contact process and the 0.010/0.050/0.10 mol/L sulfuric-acid pH, the uncertainty budgets including the 32-portion extraction limit); ch. 1–20 likewise during drafting. Every multi-line math span keeps its exact English line break. Gate 11 (problem numbering) OK on 29 chapters |
| Defined-term links (`\omterm`) | **95** | **2682 links over 144 distinct targets** against English's **2462 over 144** — the identical target set (diff 0 in both directions). `book2_id.py` curated from this edition's own harvest (`--terms`: 519 linkable terms on the same 169 targets as English), never seeded: `DROP` {*kuat*, *lemah*}, three short-form `EXTRA` for the lone/bonding pair, 18 `EXTRA_PROTECT` patterns. `--apply` twice changes nothing; the plain dry run reports **links to insert: 0**. Censuses below |
| MT-artifact freedom | **96** | Gate 8 (Indonesian prose): OK on 58 files and on the credits page. Gate 9 (twin comparison): **0 blocking findings**; 24 advisory one-word findings, all read: eponyms and symbols (*Lyman*, *Balmer*, *Paschen*, *Fischer*, *Cram*, *Pauling*, δ (ppm), [A] (mol/L)), cognates identical in Indonesian (*aluminium*, *linear*, *anode*, *oleum*, *gauche*, *anti*, *Magnesium*, *dinitrogen*), and the abbreviations *inv*/*ret*. Gate 10 (orphan lines): 0. `\text{}` census over course and solutions: every translatable subscript translated (*acuan*, *tinggi/rendah*, *produk/pereaksi*, *berlebih*, *bebas*, *asetal/aldehida*, *setengah sel*, *ruas oksidator/reduktor*, *jarak yang ditempuh noda / garis depan eluen*, `\mathrm{terlarut}`, `\mathrm{labu}`, `\mathrm{alikuot}`, `\mathrm{depan}`); survivors are symbols (*s, p, d, f*, *tot*, *eq*, `\mathrm{org}`, `\mathrm{ref}`, *EHS*) |

**Overall: 96.** Weighted toward terminology, register, link curation and
MT-artifact freedom; structure and build are gated mechanically.

## Gate output summary

```
bash tools/check_translation.sh bachelor-1 id ......... TRANSLATION GATE: PASSED
  indonesian prose gate: OK (58 files)
  latin prose gate: no multi-word findings (24 advisory one-word, read)
  chemistry twin gate: OK (58 files)
check_ce_balance.py ...... 125 + 148 equations, 0 problems
check_problem_numbering .. OK (29 chapters)
check_orphan_lines ....... 0

forced build, build/one_chemistry_book_2_university_year_1_id.log (grep -a)
  '^!' 0 · undefined 0 · Overfull 0 · nullfont 0 · 'invalid in math mode' 0
  pages 305 (English 293) · .fls Indonesian sources 58

python3 tools/link_defined_terms.py --book 2 --lang id      (plain dry run)
  links to insert: 0 across 0 files
\index 364 = 364 · \label set diff 0
```

### The two homograph censuses (after the final link layer)

*Frequency census* (Indonesian ≥ 8 and ≥ 2× English, or |Δ| > 12) — seven
survivors, each read in context, all the defined sense:

| target | EN | ID | why |
|---|---:|---:|---|
| `periodicity:table` | 80 | 104 | *golongan* is only the table's group in Indonesian (the group of atoms is *gugus*), so it links before and after a number; English links *group* only before a number. Four CLASS uses are protected |
| `stereochemistry-in-depth:enantiomers` | 48 | 71 | Indonesian *enantiomer/diastereomer* also reach the adjectival uses English writes as *enantiomeric*, *diastereomeric* |
| `periodicity:electronegativity` | 17 | 30 | the noun *keelektronegatifan(nya)* carries what English writes as the adjective *electronegative* |
| `periodicity:ionisation-energy` | 8 | 17 | *energi ionisasi pertama(nya)* where English varies wording |
| `periodicity:radius` | 6 | 12 | *jari-jari ion / kovalen* is invariable; English *radii* misses its own term |
| `e-ph-diagrams:disproportionation` | 4 | 13 | the noun *disproporsionasi* where English uses the verb *disproportionates* |
| `extent-q-and-k:extent` | 1 | 11 | English writes the bare *extent*; Indonesian keeps *kemajuan reaksi(nya)* |

*Chapter-set census* (Indonesian linking in chapters English never links) —
18 targets, every occurrence read: all the defined sense (e.g. *kelarutan*
of diastereomers in ch. 16, *pereaksi pembatas* in ch. 15 and 21, *larutan
penyangga* in ch. 10 after its definition). One wrong sense found and fixed
in the prose: *tingkat oksidasi* (the carbon's oxidation level, ch. 24) had
been used for the inert-pair "oxidation state" in ch. 27; it now reads
*keadaan oksidasi*.

Homographs handled in `book2_id.py`: *kuat/lemah* (dropped); *golongan* as a
class (ch. 6, 17, 26); *multiplisitas* of an NMR signal (ch. 17); *hidrasi* of
ions (ch. 28); VSEPR *posisi aksial/ekuatorial* (ch. 28); *kuantitatif oleh
teori* (ch. 8); the signal word `\emph{Bahaya}` and the GHS08 name *bahaya
kesehatan* (ch. 29); plus code masks (`\omperiodictable[…]`, `\arrow{…}`,
`\setchemfig{…}`, tick labels).

## Shared-tool edits (append-only, reasoned, reported)

1. `check_indonesian_prose.py` NOT_GATED: *kation-kation*, *karbokation-karbokation* — reduplicated plurals fire ENGLISH_SUFFIX (gate bug: test each half of X-X).
2. `check_indonesian_prose.py` ALLOWED: xcolor names — TIKZ_NODE reads a `\node[aX={green!55!black}…]` option as the label (gate bug).
3. `check_indonesian_prose.py` GENE_SYMBOL: `HIn/In` indicator notation (ch. 15).
4. `check_indonesian_prose.py` ALLOWED: *andes* (*Pegunungan Andes*, -es stem rule → "and").
5. `check_indonesian_prose.py` ATTRIBUTION: *NASA Earth Observatory* (ch. 26 credit).
6. `check_indonesian_prose.py` ATTRIBUTION: *Hi-Res Images of Chemical Elements* (ch. 27 credit, credits page).
7. `check_indonesian_prose.py` GENE_SYMBOL: `(?<=\bI, )At\b` — astatine in the halogen list (ch. 28); "at" deliberately not ALLOWED.
8. `check_latin_prose.py` ALLOWED_BY_LANG `id`: *butan*, *ol* — the node `\cip{S}-butan-2-ol` (ch. 22), same entry as es/fr/pt.

## English-canon defects

None found. Every number of ch. 1–29 was recomputed during drafting; the
WAVE1–3 corrections are already in the canon and were translated as
corrected.
