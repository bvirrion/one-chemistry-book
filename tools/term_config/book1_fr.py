"""Book 1 (School Chemistry, Grades 1-12) -- fr (French). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_fr.py.

Curated by the fr Book 1 agent (2026-10-04) from this edition's own harvest
(`--terms`) and a census of every harvested word in its French contexts --
not translated from book1_en.py. AMBIG_POLICY stays "nearest-preceding": a
word can be defined twice in two senses ("mélange" is the verb's noun in
grade 2 and the chemist's mixture from grade 6; "réactif" is the test's
reagent and the reaction's reactant, both in grade 7).

French homographs found by the census, each handled below: solution (of an
exercise / everyday), produit (a cleaning product), matériau, objet,
symbole (of a quantity), groupe (of atoms / of the periodic table), couche
(a layer of oil, sand, oxide / an electron shell), indice (a clue, a hint /
a subscript), rendement (a heating efficiency / a synthesis yield),
élimination (removing water / the reaction category), brûler (a corrosive
burns the skin / a fuel burns), air (avoir l'air / the air), noyau (the
Earth's core / the nucleus).
"""

STOP = {
    # everyday words defined in the early grades and used in their everyday
    # sense ever after ("la solution de l'exercice", "un produit ménager",
    # "le matériau d'une bouteille"); their multi-word terms keep their
    # links ("solution aqueuse", "propriété d'un matériau", "produit brut").
    "solution", "solutions", "matériau", "objet", "produit", "produits",
    # the atom's symbol in its own chapter; a quantity's symbol (n, M, c)
    # everywhere after. "symbole d'un atome" keeps its link.
    "symbole",
    # the bare letters of the Z/E definition: "isomère Z" and "isomère E"
    # keep their links; a lone capital letter is not a term.
    "E", "Z",
}
NO_CAPITAL = set()
# French says "double liaison" at least as often as the defined
# "liaison double" (the adjective may come first): same notion, same target.
EXTRA = {
    "double liaison": "def:g10:lewis-and-shape:multiple-bond",
    "doubles liaisons": "def:g10:lewis-and-shape:multiple-bond",
    "triple liaison": "def:g10:lewis-and-shape:multiple-bond",
    "triples liaisons": "def:g10:lewis-and-shape:multiple-bond",
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
    # Coordinator, 2026-10-04 (found by the Indonesian Book 1 agent): the
    # capitalised, colon-led head of g12 solutions/11 exo 1 is the hydration of
    # ETHENE (an addition), not the hydration of ions it linked to.
    r"Hydratation(?=~?:)",
    # "groupe" is the periodic-table group only before a number (groupe 1,
    # groupes 13 à 18); "groupe hydroxyle", "groupe d'atomes", "groupes
    # d'électrons" stay plain. French puts the modifier after the noun, so the
    # linkable "groupe ..." terms are excluded by a lookahead.
    r"\b[Gg]roupes?\b(?!\s*~?\d)"
    r"(?!\s+(?:caractéristiques?|alkyles?|protecteurs?)\b)",
    # ... and inside the definition of "groupe caractéristique" itself, where
    # the linker skips the self-link and would fall back to the bare
    # "groupe" (the periodic-table sense): the head noun is masked there.
    r"\bun\s+groupe(?=\s+caractéristique\s+forment)",
    # "couche": an oil, sand, zinc or oxide layer, not an electron shell
    r"\bfines?\s+couches?\b",
    # "indice": a hint in an exercise; and the key of \polymerdelim
    r"\(Indice\b",
    r"\\polymerdelim\[[^\]]*\]",
    # "rendement": the efficiency of a heating, not a synthesis yield
    r"\b[Rr]endement(?=\s+(?:du\s+chauffage|\$20\.9))",
    # "élimination de l'eau / d'un produit": removing it, not an elimination
    r"\b[ÉéEe]limination\s+d(?:'|e\b|u\b|es\b)",
    # a corrosive "brûle la peau et les yeux": not a combustion
    r"\bbrûl(?:e|ent|er)\s+(?:la\s+peau|les\s+yeux)",
    # "ont l'air identiques": seem, not the air
    r"\bont\s+l'air\b",
    # the Earth's core, not an atomic nucleus
    r"\bnoyau\s+terrestre\b",
    # pgfplots tick labels are code
    r"[xy]ticklabels=\{[^{}]*\}",
    # the data key (first argument) of the infrared chapter's \irpanel
    r"\\irpanel\{[^{}]*\}",
    # chemfig settings: "atom sep=1.5em" is a key, not a word
    r"\\setchemfig\{[^{}]*\}",
    # key names inside the periodic-table macro's options
    r"\\omperiodictable\[[^\]]*\]",
    # chemfig arrow labels: \arrow{->[label][label]}
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
]
