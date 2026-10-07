"""Book 4 (University Chemistry, Year 3) -- fr (French). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_fr.py.

Curated by the fr Book 4 agent (2026-10-06) from this edition's own harvest
(`--terms`: 670 harvested, 697 linkable) and a concordance of every
single-word term in its French contexts after its definition -- not
translated from book4_en.py. AMBIG_POLICY stays "drop", as in English; no
term is defined twice.

A word is linked only once its definition has been met, so a word used in
another sense BEFORE its definition chapter is safe (ch. 14's "trou de la
couche d'ozone", ch. 18's d-shell "trous", ch. 22's "cristal hôte", ch. 31's
"fabrication des réactifs"). The homographs met AFTER their definition, each
handled below:

  * migration (ch. 15, ionic migration): every later French "migration" is a
    sigmatropic shift (ch. 26, "migration [1,5]-H") or a 1,2-shift (ch. 27),
    which English calls "shift" and never collides on. The bare word is
    dropped; "migration 1,2" keeps its own key and target.
  * sol (ch. 17, a colloidal sol): ch. 32 says "sol" for soil a dozen times
    (and ch. 31 "usage des sols"); the gold sols of ch. 17 and the sol of the
    sol--gel process (ch. 23) keep their links.
  * gel (ch. 17): ch. 22's "gel des porteurs" is carrier freeze-out.
  * trou (ch. 22, the semiconductor hole): ch. 23's glass-network "trous"
    are cavities; the electron--hole pairs of quantum dots stay linked.
  * population (ch. 10, a Boltzmann population): ch. 32's "populations
    denses d'algues" and "population d'essai" are organisms (English masks
    the same two).
  * caractère (ch. 4, the character of a representation): "caractères
    singulet et triplet" (ch. 7), "caractère s" (ch. 29) and the section
    title "Mesurer le caractère vert" (ch. 31) are ordinary words.
  * opérateur (ch. 1, the quantum operator): the laser and UV-lamp operators
    of ch. 5 and ch. 7 and the "opérateurs formés" of solutions 31 are
    people (English masks the same sites).
"""

STOP = set()
NO_CAPITAL = set()
# Forms the harvest cannot derive, each a real occurrence of the notion: the
# short "quasi réversible" French writes for the defined "système quasi
# réversible" (English links "quasi-reversible" the same way), the adjective
# "peroxydable(s)" of the safety boxes for the defined "composé peroxydable",
# and the "gabarit de cuivre" of ch. 25's history box for "synthèse par effet
# de gabarit" (ch. 23's zeolite "gabarit" comes before the definition).
EXTRA = {
    "quasi réversible": "def:b3:electrode-kinetics:reversibility",
    "peroxydable": "def:b3:lab-techniques-3:peroxide",
    "peroxydables": "def:b3:lab-techniques-3:peroxide",
    "gabarit": "def:b3:supramolecular:template",
}
DROP = {"migration", "migrations"}
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# Multi-word patterns use \s+ between words: a phrase wrapped across a source
# line break must still be protected. A look-ahead anchored on a word that is
# itself a term must allow an optional wrapper: (?:\\omterm\{[^{}]*\}\{)?
EXTRA_PROTECT = [
    # chemfig settings and arrow labels: \arrow{->[label][label]}
    r"\\setchemfig\{[^{}]*\}",
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
    # pgfplots tick-label lists (every Book 1-2 edition needed this)
    r"[xy]ticklabels=\{[^{}]*\}",

    # soil (ch. 31-32), not a colloidal sol
    r"\baux\s+sols\b",
    r"\bdu\s+sol\b",
    r"\b[Ss]ols?(?=\s+et\s+sédiments)",
    r"\bdans\s+les\s+sols\b",
    r"\bd'un\s+sol\b",
    r"\bsur\s+le\s+sol\b",
    r"\{sol(?=\\\\)",
    r"\bou\s+le\s+sol\b",
    r"\bUn\s+sol(?=\s+a\s+\$)",
    r"\bdans\s+un\s+sol\b",
    r"\busage\s+des\s+sols\b",
    # carrier freeze-out, not a gel
    r"\bgel\s+des\s+porteurs",
    # cavities of a glass network, not semiconductor holes
    r"\bdans\s+les\s+trous\b",
    # organisms, not Boltzmann populations
    r"\bpopulations?(?=\s+denses)",
    r"\bpopulation\s+d'essai",
    # orbital or ordinary character, not the character of a representation
    r"\bcaractères?\s+(?:singulet|s\b|vert)",
    # people who run a laser, a lamp or a plant, not quantum operators
    r"\bopérateurs?\s+(?:portent|porte)\b",
    r"\bopérateurs\s+formés",
    # the mean of a reaction enthalpy over a range (ch. 11), not a quantum
    # expectation value
    r"\bvaleur\s+moyenne(?=\s+de\s+\$\\Delta_rH)",
]
