"""Book 1 (School Chemistry, Grades 1-12) -- en. Curation only; the rules
live in tools/termlink/.

One volume for twelve years, written so that it never repeats itself: each
notion has one owner chapter. AMBIG_POLICY stays "nearest-preceding" all the
same, because a word can be defined twice in two different senses (an
everyday "solution" in grade 2, the chemist's solution in grade 6).

Curate for the chemistry homographs before adding anything else: solution
(of an exercise), table, group, period, family, shell, base, cell, charge,
yield, phase, indicator, element, compound, bond, species.
"""

STOP = {
    # the atom's symbol in its own chapter; a quantity's symbol (n, M, c)
    # everywhere after. The phrase "symbol of an atom" keeps its link.
    "symbol", "symbols",
    # everyday words defined in the early grades, used in their everyday
    # sense ever after ("a solution of the exercise", "a cleaning product",
    # "the material of a bottle", "a family of compounds", "a period of
    # time"); their multi-word terms keep their links ("aqueous solution",
    # "property of a material", "chemical family").
    "solution", "solutions", "material", "object", "product", "products",
    "family", "period",
    # reaction categories of the curly-arrows chapter: "the addition of the
    # titrant", "a substitution of one solvent by another". "Addition
    # polymer" keeps its link.
    "addition", "substitution",
    # "the capacity of a buffer", "heat capacity": only the cell's capacity
    # is defined, and it is used in its own chapter.
    "capacity",
}
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped
# across a source line break must still be protected.
EXTRA_PROTECT = [
    # "group" is the periodic-table group only before a number (group 1,
    # groups 13 to 18); "functional group", "methyl group", "acid group"
    # stay plain. The linkable "... group" terms are excluded.
    r"(?<!functional )(?<!protecting )(?<!alkyl )"
    r"(?<!Functional )(?<!Protecting )(?<!Alkyl )"
    r"\b[Gg]roups?\b(?!\s*~?\d)",
    # the hydration of an alkene (an addition), not the hydration of ions
    r"hydration(?=\s+of\s+ethene)",
    # a defined word as one half of a hyphenated compound
    r"breath-alcohol", r"lithium-ion", r"sweet-solvent", r"coal-burning",
    # the data key (first argument) of the infrared chapter's \irpanel
    r"\\irpanel\{[^{}]*\}",
    # chemfig settings: "atom sep=1.5em" is a key, not the word atom
    r"\\setchemfig\{[^{}]*\}",
    # key names inside the periodic-table macro's options
    r"\\omperiodictable\[[^\]]*\]",
    # chemfig arrow labels: \arrow{->[label][label]}
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
]
