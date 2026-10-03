"""Book 2 (University Chemistry, Year 1) -- en. Curation only; the rules
live in tools/termlink/.

Every occurrence of a term is linked once its definition has been met, so a
word defined late in one sense is safe in an earlier chapter that uses it in
another (configuration: electron configuration in ch. 1-2, the stereo
configuration from ch. 16; hydride: the hydride ion of ch. 24, the binary
hydrides of ch. 26; hydration of ions in ch. 2 and 4, of alkenes in ch. 25).
What remains are the uses AFTER the definition in another sense, masked below.
"""

STOP = {
    # bare adjectives: "strong acid" / "weak base" keep their links, but
    # "a strong bond", "weak interactions" must not point at acid strength
    "strong", "weak",
}
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across
# a source line break must still be protected.
EXTRA_PROTECT = [
    # "group" is the periodic-table group only before a number (group 16,
    # groups 1 and 2); "methyl group", "OH group", "the group" stay plain.
    # The four linkable "... group" terms are excluded by the look-behinds.
    r"(?<!leaving )(?<!protecting )(?<!donor )(?<!acceptor )"
    r"(?<!Leaving )(?<!Protecting )(?<!Donor )(?<!Acceptor )"
    r"\b[Gg]roups?\b(?!\s*~?\d)",
    # optical activity, not the thermodynamic activity (ch. 19)
    r"loss\s+of\s+activity",
    # NMR multiplicity of a signal, not the multiplicity of a cell (ch. 17)
    r"multiplicity(?=\s+of\s+each\s+signal)",
    # hydration of ions, not of an alkene (ch. 28)
    r"hydration(?=\s+of\s+the\s+smaller)",
    # VSEPR positions of a trigonal bipyramid, not cyclohexane bonds
    r"(?:axial|equatorial)(?=\s+positions?)",
    # personal protection in the safety chapter, not a protecting group
    r"(?:eye|personal)\s+protection",
    r"controls\s+and\s+protection",
    r"route,\s+protection",
    # the GHS08 pictogram's name, not the defined term
    r"health\s+hazard(?!s)",
    # key names inside the periodic-table macro's options ("f block=false")
    r"\\omperiodictable\[[^\]]*\]",
    # chemfig arrow labels: \arrow{->[label][label]}
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
]
