"""Book 2 (University Year 1) -- fr (French). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_fr.py.

Curated by the fr Book 2 agent (2026-10-04) from this edition's own harvest
(`--terms`, 391 linkable terms on the same 169 targets as English) and a
census of the harvested words in their French contexts -- not translated
from book2_en.py. AMBIG_POLICY stays "drop", as in English: no term is
defined twice (ch. 9's "intermédiaire réactionnel" and ch. 18's
"intermédiaire réactif" were kept distinct on purpose).

As in English, a word is linked only once its definition has been met, so a
word defined late in one sense is safe in earlier chapters that use it in
another. French homographs met AFTER their definition, each handled below:
fort/faible (acid strength / any strength), groupe (of the periodic table /
of atoms), multiplicité (of a cell / of an NMR signal), hydratation (of an
alkene / of ions), axiale/équatoriale (cyclohexane bonds / VSEPR positions),
protection (protecting group / personal protection), danger (the defined
hazard / the GHS08 pictogram's name and the signal word), motif and réseau
(the crystal's motif and lattice / silicate units and covalent networks),
période (a row of the table / an induction period), bloc (the s/p block / a
block of zinc), quantitative (a reaction / a measurement, a theory).
"""

STOP = {
    # bare adjectives: "acide fort", "base faible" keep their links, but
    # "une liaison forte", "un nucléophile faible" must not point at acid
    # strength
    "fort", "forte", "faible",
}
NO_CAPITAL = set()
# Forms the harvest cannot derive, each a real occurrence of the notion:
# masculine and plural adjectives (the index carries "axiale"), irregular
# plurals (cristal/cristaux), and the short form "moment de liaison" that
# French uses for the defined "moment dipolaire de liaison".
EXTRA = {
    "axial": "def:b1:stereochemistry-in-depth:conformations",
    "axiaux": "def:b1:stereochemistry-in-depth:conformations",
    "équatorial": "def:b1:stereochemistry-in-depth:conformations",
    "équatoriaux": "def:b1:stereochemistry-in-depth:conformations",
    "cristaux": "def:b1:crystals-metals:crystal",
    "cristaux ioniques": "def:b1:crystals-ionic-covalent:ionic-crystal",
    "cristaux covalents": "def:b1:crystals-ionic-covalent:covalent-crystal",
    "cristaux moléculaires": "def:b1:crystals-ionic-covalent:molecular-crystal",
    "niveaux d'oxydation": "def:b1:organic-redox:oxidation-level",
    "moment de liaison": "def:b1:lewis-resonance-vsepr:dipole",
    "moments de liaison": "def:b1:lewis-resonance-vsepr:dipole",
}
# ... and dropped outright: French says "l'acide le plus fort", "la base la
# plus forte", "une faible constante", "un faible avancement" where English
# says "the strongest acid" or "a small constant", so the bare adjectives
# would keep a dozen wrong-sense links in ch. 10 through the per-chapter map
# even when stoplisted.
DROP = {"fort", "forte", "forts", "fortes", "faible", "faibles"}
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across
# a source line break must still be protected.
EXTRA_PROTECT = [
    # Coordinator, 2026-10-04: the zinc anode blocks of ch. 14 are not the
    # periodic-table block; English now protects the same sites.
    r"blocs?(?=\s+gris)",

    # "groupe" is the periodic-table group only before a number (groupe 16,
    # groupes 13 à 15); "groupe méthyle", "groupe OH", "le groupe" stay
    # plain. French puts the modifier after the noun, so the four linkable
    # "groupe ..." terms are excluded by a lookahead.
    r"\b[Gg]roupes?\b(?!\s*~?\d)"
    r"(?!\s+(?:donneurs?|attracteurs?|partants?|protecteurs?)\b)",
    # NMR multiplicity of a signal, not the multiplicity of a cell (ch. 17)
    r"\bmultiplicités?(?=\s+(?:de\s+chaque\s+signal|des\s+signaux|du\s+signal))",
    r"\bapproximatifs,\s+multiplicités",
    # hydration of ions, not of an alkene (ch. 26, 28)
    r"\bhydratation(?=\s+des\s+ions)",
    # VSEPR positions of a trigonal bipyramid, not cyclohexane bonds
    r"\bpositions?\s+(?:axiales?|équatoriales?)",
    # personal protection in the safety chapter, not a protecting group
    r"\bprotection\s+(?:individuelle|des\s+yeux)",
    r"\bexposition,\s+protection",
    r"\bécran\s+de\s+protection",
    # a time period (an induction period), not a row of the table
    r"\bpériodes?\s+d'induction",
    # a block of zinc (a sacrificial anode), not the s/p/d/f block
    r"\bblocs?\s+de\s+zinc",
    # "quantitative" as a kind of theory or measurement, not a reaction
    r"\brendue\s+quantitative",
    r"\bmesure\s+quantitative",
    # the GHS08 pictogram's name and the signal word, not the defined term
    r"\bdanger\s+pour\s+la\s+santé",
    r"\\emph\{Danger\}",
    # key names inside the periodic-table macro's options ("f block=false")
    r"\\omperiodictable\[[^\]]*\]",
    # chemfig arrow labels: \arrow{->[label][label]}
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
    # "réseau" is also a network (of covalent bonds, of hydrogen bonds in
    # ice, of SiO4 tetrahedra), not the crystal lattice of ch. 5
    r"\bréseau(?=\s+(?:covalent|hexagonal|se\s+lit|de\s+\\ce))",
    # silicate structural units, not the motif of a crystal
    r"\b[Mm]otifs?\s+silicatés",
    r"\bmotifs?(?=\s+\\ce)",
    # pgfplots tick labels are code
    r"[xy]ticklabels=\{[^{}]*\}",
]
