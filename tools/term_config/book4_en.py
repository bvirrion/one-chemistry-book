"""Book 4 (University Chemistry, Year 3) -- en. Curation only; the rules live
in tools/termlink/.

Every occurrence of a term is linked once its definition has been met. What
remains to mask are the uses after the definition in another sense: the
person who operates an instrument (not the quantum operator), the s or pi
"character" of an orbital or a mechanism (not the character of a
representation), a population of organisms (not the Boltzmann population), a
hole in a network or in a porphyrin (not the semiconductor hole), and the
migration of a group or an atom (not ionic migration in electrode kinetics).
"""

STOP = set()
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across
# a source line break must still be protected.
EXTRA_PROTECT = [
    # people who run an instrument or a plant
    r"the\s+operators?(?=\s+(?:wear|works))",
    r"trained\s+operators",
    # orbital or mechanistic character
    r"(?:triplet|\bs)\s+character",
    r"\)\s+character",
    r"(?<=\^\*\$\s)character",   # "$\pi^*$ character": never consume the $
    r"vector\s+character",
    # organisms, not Boltzmann populations
    r"populations?(?=\s+of\s+microscopic)",
    r"test\s+population",
    # holes in a network or a ring, not semiconductor holes
    r"in\s+the\s+holes?\b",
    r"for\s+the\s+hole\b",
    # migration of a group or an atom, not ionic migration
    r"the\s+migration(?=\s+of\s+a\s+group)",
    r"one\s+migration",
    # chemfig settings and arrow labels
    r"\\setchemfig\{[^{}]*\}",
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
]
