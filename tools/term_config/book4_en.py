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
EXTRA = {
    # the definition names "volume of activation", the prose says "activation
    # volume" (ch. 19 l. 100, 459): English never reached its own definition
    # (Spanish Book 4 agent, 2026-10-06)
    "activation volume": "def:b3:complex-mechanisms:activation-volume",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across
# a source line break must still be protected.
EXTRA_PROTECT = [
    # "indistinguishable" of a symmetry operation (a configuration
    # indistinguishable from the original / from itself, ch. 4): everyday sense,
    # not quantum indistinguishability (coordinator, 2026-10-07, from the hi agent)
    r"indistinguishable(?=\s+from\s+(?:the\s+original|itself))",
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
    # "indistinguishable" in its everyday sense (an orientation of the
    # symmetry-number argument; two sums numerically equal), not the
    # quantum-indistinguishability definition (Portuguese Book 4 agent, 2026-10-06)
    r"indistinguishable(?=\s+(?:from\s+the\s+(?:sum|starting)|orientation))",
    # chemfig settings and arrow labels
    r"\\setchemfig\{[^{}]*\}",
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
]
