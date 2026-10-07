"""Book 3 (University Chemistry, Year 2) -- en. Curation only; the rules
live in tools/termlink/.

A term is linked once its definition has been met, so a word defined late in
one sense is safe in earlier chapters (work-up: ch. 21's "oxidising work-up"
precedes the definition of ch. 35). What remains are the uses AFTER the
definition in another sense, masked below.
"""

STOP = {
    # ch. 15's fragment method: the bare word is used later for ozonolysis
    # fragments (ch. 21), synthons (ch. 28), mass-spectrum fragments (ch. 32-33)
    # and pieces of a structure; "fragment orbital(s)" keeps its link.
    "fragment", "fragments", "Fragment", "Fragments",
}
NO_CAPITAL = set()
EXTRA = {
    # the definition "Enolates" harvests only "enolate ion"; the bare noun, used
    # ~130 times in ch. 25-28, never linked (Arabic Book 3 agent, 2026-10-06)
    "enolate": "def:b2:enolates-aldol:enolate",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# Multi-word patterns use \s+ between words: a phrase wrapped across a source
# line break must still be protected.
EXTRA_PROTECT = [
    # statistical variance (ch. 29, 34), not the variance of a system (ch. 4)
    r"\bvariances?\b(?=\s+\$\\sigma)",
    r"[Vv]ariance\s+of\s+a\s+(?:sum|linear|Poisson)",
    r"sum\s+of\s+the\s+variances",
    r"mean\s+and\s+variance",
    # propagation of uncertainty (ch. 34), not a chain-propagation step (ch. 29)
    r"[Pp]ropagation(?=\s+(?:of\s+(?:the\s+)?uncertaint|rule))",
    # initiation of a Grignard reaction (ch. 35), not radical initiation (ch. 29)
    r"before\s+initiation",
    r"an\s+initiation\s+failure",
    # chromatographic selectivity (ch. 31), not a reactor's selectivity (ch. 5)
    r"Selectivity(?=:\s+the\s+factor)",
    r"levers:\s+the\s+selectivity",
    # the R_f of a TLC plate (Year 1's retention factor), not the column's k
    r"retention\s+factor\s+\$R_f\$",
    # spectral resolution (ch. 32-33), not the chromatographic resolution (ch. 31)
    r"than\s+the\s+resolution",
    r"[Hh]igh-resolution(?!\s+mass)",
    # chemfig arrow labels: \arrow{->[label][label]}
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
]
