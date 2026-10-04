"""Book 1 (School Chemistry, Grades 1-12) -- id (Indonesian). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_id.py.

Curated by the id Book 1 agent (2026-10-04) from this edition's own harvest
(`--terms`, 306 terms) and a census of every harvested word in its
Indonesian contexts -- not translated from book1_en.py. AMBIG_POLICY stays
"nearest-preceding" (the bare letters E and Z, and "pH", are defined in one
chapter only and are chapter-local there, as in English).

What the census found, and why each entry below exists:

  * Indonesian keeps apart several words English has to disambiguate:
    "gugus" is the functional group and "golongan" only the periodic-table
    group (every "golongan" in the book, numbered or not, is the table's),
    so "golongan" needs no protection; "penyelesaian" is an exercise's
    solution and "larutan" only the chemist's, and "efisiensi" (not
    "rendemen") is a heating's efficiency, so "rendemen" is always the yield.
  * Stoplisted like their English counterparts, for the same everyday use:
    "larutan" (on nearly every page from grade 2 on; its multi-word terms
    -- larutan berair, larutan jenuh, larutan penyangga, ... -- keep their
    links), "bahan", "benda", "produk", "periode", "lambang", "kapasitas"
    (the capacity of a buffer in grade 12).
  * NOT stoplisted although English stoplists "addition"/"substitution":
    Indonesian writes the titrant's addition as "penambahan" and replacing a
    solvent as "mengganti", so "adisi" and "substitusi" are only ever the
    reaction categories.
  * Short forms the prose uses far more often than the defined phrase, same
    notion and same target: "ikatan rangkap" (the defined term is "ikatan
    rangkap dua"), "pasangan bebas" and "pasangan ikatan" (the defined terms
    spell out "pasangan elektron ...").
  * DERIVE is off for Indonesian, so the affixed verbs of two grade-2/3
    definitions are declared: mencampur -> dicampur, mencampurkan, ...;
    penguapan -> menguap, diuapkan, ... (English links mix/mixes and
    evaporate/evaporates the same way).
  * "kulit" is the skin and a bark as well as the electron shell: the shell
    is linked only through "kulit terluar" and "kulit 1/2/3".
  * Homographs protected below: "pengendapan" is the grade-3 settling of a
    suspension but also a precipitation ("pengendapan perak klorida");
    "larutan asam/basa" is the defined acidic/basic solution but also "a
    solution of <named acid>"; "hidrasi" is the hydration of ions but also
    the hydration of ethene (an addition); "litium-ion" is a battery type.
"""

STOP = {
    # everyday words defined in the early grades, used in their everyday
    # sense ever after; their multi-word terms keep their links.
    "larutan", "bahan", "benda", "produk", "periode",
    # the atom's symbol in its own chapter; a quantity's symbol (n, M, c)
    # everywhere after. "lambang atom" keeps its link.
    "lambang",
    # "kapasitas yang lebih besar" of a buffer (grade 12): only the cell's
    # capacity is defined, and "tetapan Faraday" carries that definition.
    "kapasitas",
    # NOT here: the bare letters "E" and "Z". They are chapter-local terms
    # (defined in the stereochemistry chapter only), and harvest.py applies
    # STOP to the global and nearest-preceding tables but not to the
    # chapter-local one, so a STOP entry would not remove them (the fr
    # edition's "E", "Z" entries have no effect either; DROP would). They are
    # left linked inside that chapter, exactly as in the English edition
    # (Z 8, E 6 links there): "Sisi yang sama: Z" is the definition's use.
}
NO_CAPITAL = set()
EXTRA = {
    # the short form of the defined "ikatan rangkap dua/tiga"
    "ikatan rangkap": "def:g10:lewis-and-shape:multiple-bond",
    # the short forms of "pasangan elektron bebas/ikatan"
    "pasangan bebas": "def:g10:lewis-and-shape:lone-pair",
    "pasangan ikatan": "def:g10:lewis-and-shape:lone-pair",
    # the bare "kulit" is also the skin (every safety box) and a tree's bark,
    # so the electron shell is reached through the phrases that cannot be
    # anything else: the outer shell, and a shell named by its number.
    "kulit terluar": "def:g10:electron-shells:configuration",
    "kulit 1": "def:g10:electron-shells:configuration",
    "kulit 2": "def:g10:electron-shells:configuration",
    "kulit 3": "def:g10:electron-shells:configuration",
    "kulit ketiga": "def:g10:electron-shells:configuration",
    # the affixed verb forms of the defined "mencampur" (DERIVE is off for
    # Indonesian): to mix, mixed, the mixing
    "dicampur": "def:g2:mixing-and-dissolving:mix",
    "dicampurkan": "def:g2:mixing-and-dissolving:mix",
    "mencampurkan": "def:g2:mixing-and-dissolving:mix",
    "campurkan": "def:g2:mixing-and-dissolving:mix",
    "pencampuran": "def:g2:mixing-and-dissolving:mix",
    # ... and of the defined "penguapan": to evaporate, evaporated
    "menguap": "def:g3:separating-mixtures:evaporate",
    "menguapkan": "def:g3:separating-mixtures:evaporate",
    "diuapkan": "def:g3:separating-mixtures:evaporate",
    "uapkan": "def:g3:separating-mixtures:evaporate",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped
# across a source line break must still be protected.
EXTRA_PROTECT = [
    # "larutan asam etanoat" is a solution OF an acid, not the defined
    # "larutan asam" (acidic solution); only the head noun is masked, so the
    # acid's own term ("asam lemah", "asam kuat") still links.
    r"\b[Ll]arutan(?=\s+(?:asam|basa)\s+(?:metanoat|etanoat|klorida|sulfat"
    r"|benzoat|askorbat|karboksilat|lemah|kuat)\b)",
    # a precipitation, not the grade-3 settling of a suspension
    r"\b[Pp]engendapan(?=\s+(?:perak|ini|untuk)\b)",
    # the hydration of ethene (an addition) and the "Hydration:" route of an
    # answer, not the hydration of ions
    r"\b[Hh]idrasi(?=\s+etena\b|:)",
    # a defined word as one half of a hyphenated compound
    r"litium-ion",
    # the data key (first argument) of the infrared chapter's \irpanel
    r"\\irpanel\{[^{}]*\}",
    # chemfig settings: "atom sep=1.5em" is a key, not the word atom
    r"\\setchemfig\{[^{}]*\}",
    # key names inside the periodic-table macro's options
    r"\\omperiodictable\[[^\]]*\]",
    # chemfig arrow labels: \arrow{->[label][label]}
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
    # pgfplots tick labels are code
    r"[xy]ticklabels=\{[^{}]*\}",
]
