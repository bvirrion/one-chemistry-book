"""Book 2 (University Year 1) -- id (Indonesian). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_id.py.

Curated by the id Book 2 agent (2026-10-04) from this edition's own harvest
(`--terms`: 519 linkable terms on the same 169 targets as English) and a
census of the harvested words in their Indonesian contexts -- not translated
from book2_en.py. AMBIG_POLICY stays "drop", as in English: no term is
defined twice.

As in English, a word is linked only once its definition has been met, so a
word defined late in one sense is safe in earlier chapters that use it in
another (hidrasi of ions in ch. 2 and 4, of alkenes from ch. 25; kompleks
logam in ch. 9, the complex of ch. 12; hidrida in ch. 22 and 24, the binary
hydrides of ch. 26). What the census found after the definitions:

  * "kuat"/"lemah" are harvested bare from the strong/weak acid definition,
    and Indonesian uses them for every strength ("ikatan yang kuat",
    "nukleofil lemah", "basa yang sangat kuat"): dropped outright, as the fr
    edition drops fort/faible. "asam kuat", "basa lemah", ... keep their
    links.
  * Indonesian keeps apart what English must disambiguate: "golongan" is
    the periodic-table group and "gugus" the group of atoms, so "golongan"
    is linked wherever it names the table's column, numbered or not (English
    links "group" only before a number because its "group" is also the
    methyl group). Only four uses mean a CLASS (of solids, of compounds, the
    most reactive metals), protected below. Likewise the translation wrote
    "masa induksi" (induction period) and "bongkah seng" (block of zinc), so
    "periode" and "blok" need no protection at all.
  * "tingkat oksidasi" is only the defined oxidation level of a carbon: the
    inert-pair passages of ch. 27 say "keadaan oksidasi" (oxidation state).
  * Homographs met AFTER their definition, each protected below: the NMR
    multiplicity of a signal (ch. 17) is not a cell's multiplicity; the
    hydration of ions (ch. 28) is not an alkene's; the VSEPR positions of a
    trigonal bipyramid (ch. 28) are not cyclohexane bonds; "dibuat
    kuantitatif oleh teori-teori" (ch. 8) is not a quantitative reaction;
    the signal word \\emph{Bahaya} and the GHS08 pictogram's name "bahaya
    kesehatan" (ch. 29) are not the defined hazard.
"""

STOP = set()
NO_CAPITAL = set()
# Short forms the prose uses for the same notion as the defined "pasangan
# elektron bebas / ikatan" (English links every "lone pair" and "bonding
# pair"): the VSEPR tables and bond-counting sentences say "pasangan bebas",
# "pasangan ikatan", and "a lone pair" is "sepasang elektron bebas".
EXTRA = {
    "pasangan bebas": "def:b1:lewis-resonance-vsepr:lewis",
    "pasangan ikatan": "def:b1:lewis-resonance-vsepr:lewis",
    "sepasang elektron bebas": "def:b1:lewis-resonance-vsepr:lewis",
}
# bare adjectives harvested from "asam kuat / basa lemah": see the docstring
DROP = {"kuat", "lemah"}
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across
# a source line break must still be protected.
EXTRA_PROTECT = [
    # "golongan" as a CLASS, not the periodic-table group
    r"\b[Gg]olongan(?=\s+(?:padatan|senyawa)\b)",
    r"\b[Gg]olongan-golongan(?=\s+itu\b)",
    r"\bgolongan(?=\s+logam\s+yang\s+paling\s+reaktif)",
    # NMR multiplicity of a signal, not the multiplicity of a cell (ch. 17)
    r"\bmultiplisitas(?=\s+(?:\(banyaknya|setiap\s+sinyal))",
    r"kira-kira,\s+multiplisitas",
    # hydration of ions, not of an alkene (ch. 28)
    r"\bhidrasi(?=\s+ion)",
    # VSEPR positions of a trigonal bipyramid, not cyclohexane bonds
    r"\bposisi\s+(?:aksial|ekuatorial)",
    # "made quantitative by the theories" (ch. 8), not a quantitative reaction
    r"\bkuantitatif(?=\s+oleh\s+teori)",
    # the signal word and the GHS08 pictogram's name, not the defined hazard
    r"\\emph\{Bahaya\}",
    r"\\footnotesize\s+bahaya\s+kesehatan",
    r"seru,\s+bahaya\s+kesehatan",
    # key names inside the periodic-table macro's options ("f block=false")
    r"\\omperiodictable\[[^\]]*\]",
    # chemfig arrow labels: \arrow{->[label][label]}
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
    # chemfig settings: "atom sep=2em" is a key
    r"\\setchemfig\{[^{}]*\}",
    # pgfplots tick labels are code
    r"[xy]ticklabels=\{[^{}]*\}",
]
