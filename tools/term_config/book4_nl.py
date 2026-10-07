"""Book 4 (University Chemistry, Year 3) -- nl (Dutch). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_nl.py.

Curated by the nl Book 4 agent (2026-10-06) from this edition's own harvest
(`--terms`) and the frequency and chapter-set censuses against English -- not
translated from book4_en.py, not copied from another book's config.
AMBIG_POLICY stays "drop", as in English: no Dutch term is defined twice.

As in English, a word is linked only once its definition has been met, so a
word defined late in one sense is safe in earlier chapters that use it in
another. Dutch homographs met AFTER their definition, each masked below:
karakter (the character of a representation / the s, d or pi* character of an
orbital, the bond-breaking character of a mechanism), bezetting (a Boltzmann
population / the occupancy of an orbital or of a Fermi level), operator (the
quantum operator / plant operators), gat (the semiconductor hole / a hole in
a d shell or in a ring), migratie (ionic migration / the migration of a group
in a 1,2-shift), sol (the colloid / the first half of "sol-gel").

Dutch has irregular plurals that WORD_TAIL cannot derive (carbeen/carbenen,
micel/micellen, keteen/ketenen, -aan/-anen); the forms that occur, each a real
occurrence of the notion, are listed in EXTRA.
"""

STOP = set()
NO_CAPITAL = set()
EXTRA = {
    "carbenen": "def:b3:organometallic-bonding:carbene",
    "micellen": "def:b3:colloids:micelle",
    "ketenen": "def:b3:radicals-carbenes:wolff",
    "geactiveerde complex": "def:b3:rate-theories:activated-complex",
    "geactiveerde complexen": "def:b3:rate-theories:activated-complex",
    "roterende assenstelsel": "def:b3:advanced-nmr:magnetisation",
    "nucleaire overhausereffect": "def:b3:advanced-nmr:noe",
    "tanabe-suganodiagrammen": "def:b3:complex-spectra-magnetism:tanabe-sugano",
    "isothermen van Langmuir": "thm:b3:surfaces-catalysis:langmuir",
    "heterocycli": "def:b3:heterocycles:heterocycle",
    "hernieuwbare grondstoffen": "def:b3:green-industrial:feedstock",
    "ferro-elektrisch": "def:b3:inorganic-materials:ferroelectric",
    "harde en zachte zuren": "def:b3:bioinorganic:hsab",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# Multi-word patterns use \s+ between words: a phrase wrapped across a source
# line break must still be protected. A look-ahead anchored on a word that is
# itself a term must allow an optional wrapper: (?:\\omterm\{[^{}]*\}\{)?
EXTRA_PROTECT = [
    # "indistinguishable" of a symmetry operation (a configuration
    # indistinguishable from the original / from itself, ch. 4): everyday sense,
    # not quantum indistinguishability (coordinator, 2026-10-07, from the hi agent)
    r"ononderscheidbaar(?=\s+van\s+zichzelf)",
    # orbital or mechanistic character, not the character of a representation
    r"\b[Kk]arakter(?=\s+(?:\$|s\b|van\s+bindingsbreuk))",
    r"\boneven\s+karakter",
    # occupancy of orbitals or of a Fermi level, not a Boltzmann population
    r"\b[Bb]ezetting(?=\s+van\s+de\s+orbitalen)",
    r"\b[Bb]ezetting(?=\s+van\s+een\s+niveau\s+met\s+energie)",
    # people who run a plant, not the quantum operator
    r"\bopgeleide\s+operatoren",
    # a hole in a d shell or in a ring, not the semiconductor hole
    r"\b[Gg]at(?=\s+in\s+(?:\$|het\s+midden))",   # never consume the $
    r"\benige\s+gat\b",
    # the migration of a group, not ionic migration
    r"\béén\s+migratie",
    r"\bmigratie(?=\s+van\s+een\s+groep)",
    r"\bAnti-migratie",
    # the Maxwell-Boltzmann speed distribution (ch. 12), which English does
    # not link to the Boltzmann distribution either
    r"\b[Mm]axwell-boltzmannverdeling",
    # "sol-gel" is one process, not the sol of a colloid
    r"\b[Ss]ol-gel(?!proces)\w*",
    # chemfig settings and arrow labels: \arrow{->[label][label]}
    r"\\setchemfig\{[^{}]*\}",
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
    # pgfplots tick-label lists
    r"[xy]ticklabels=\{[^{}]*\}",
]
