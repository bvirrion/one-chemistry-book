"""Book 4 (University Chemistry, Year 3) -- es (Spanish). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_es.py.

Curated by the es Book 4 agent (2026-10-06) from this edition's own harvest
(`--terms`, 704 linkable terms) and the frequency and chapter-set censuses of
the Spanish links, line by line against the English link targets -- not
translated from book4_en.py and not copied from another config.
AMBIG_POLICY stays "drop", as in English: no term is defined twice.

A word is linked only once its definition has been met, so a word defined late
in one sense is safe in earlier chapters that use it in another. Spanish
homographs met AFTER their definition, each handled below:
  carácter    the character of a representation (ch. 4) / "carácter s",
              "carácter singlete", "carácter impar", "carácter de ruptura"
  hueco       a hole in a semiconductor (ch. 22) / the hole in a glass network
              or in the porphyrin ring (chs 23-24)
  población   the Boltzmann population (ch. 10) / a test population, an algal
              population (ch. 32)
  sol         a colloid (ch. 17) / the sun (ch. 26)
  operador    a quantum operator (ch. 1) / a laboratory operator (ch. 7)
  producto directo  the direct product of representations (ch. 5) / the
              uncyclised product of a radical clock (ch. 27)
  migración   ionic migration (ch. 15) / a 1,2-shift: the translation avoids
              the noun in the organic chapters, so nothing to protect
  fuerte/débil not terms in this book (only "campo fuerte/débil" in prose).
"""

STOP = set()
NO_CAPITAL = set()
# Forms the harvest cannot reach: the adjective the English links
# ("quasi-reversible", sol. 15) without its noun.
EXTRA = {
    "cuasirreversible": "def:b3:electrode-kinetics:reversibility",
    "cuasirreversibles": "def:b3:electrode-kinetics:reversibility",
}
DROP = set()
# Plurals the tail cannot reach (the accent of a final -ón, -ión, -ácter falls
# in the plural); each kept only because it occurs in this edition.
DERIVED = {
    "anfitrión": ["anfitriones"],
    "carácter": ["caracteres"],
    "cicloadición": ["cicloadiciones"],
    "contribución orbital": ["contribuciones orbitales"],
    "degeneración": ["degeneraciones"],
    "emulsión": ["emulsiones"],
    "evaluación de riesgos": ["evaluaciones de riesgos"],
    "fotoisomerización": ["fotoisomerizaciones"],
    "función de polarización": ["funciones de polarización"],
    "función difusa": ["funciones difusas"],
    "función propia": ["funciones propias"],
    "operación de simetría": ["operaciones de simetría"],
    "población": ["poblaciones"],
    "razón nefelauxética": ["razones nefelauxéticas"],
    "reacción de Mannich": ["reacciones de Mannich"],
    "reacción de acoplamiento cruzado": ["reacciones de acoplamiento cruzado"],
    "reacción electrocíclica": ["reacciones electrocíclicas"],
    "reacción en cadena": ["reacciones en cadena"],
    "reacción enantioselectiva": ["reacciones enantioselectivas"],
    "reacción diastereoselectiva": ["reacciones diastereoselectivas"],
    "reacción oscilante": ["reacciones oscilantes"],
    "reacción pericíclica": ["reacciones pericíclicas"],
    "representación de Job": ["representaciones de Job"],
    "representación irreducible": ["representaciones irreducibles"],
    "tensión superficial": ["tensiones superficiales"],
    "transición de transferencia de carga": ["transiciones de transferencia de carga"],
    "transposición de Cope": ["transposiciones de Cope"],
    "transposición de Curtius": ["transposiciones de Curtius"],
    "transposición sigmatrópica": ["transposiciones sigmatrópicas"],
}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# Multi-word patterns use \s+ between words: a phrase wrapped across a source
# line break must still be protected. A look-ahead anchored on a word that is
# itself a term must allow an optional wrapper: (?:\\omterm\{[^{}]*\}\{)?
EXTRA_PROTECT = [
    # chemfig settings and arrow labels: \arrow{->[label][label]}
    r"\\setchemfig\{[^{}]*\}",
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
    # pgfplots tick-label lists
    r"[xy]ticklabels=\{[^{}]*\}",
    # "carácter" in its ordinary sense, not the character of a representation:
    # s character of a hybrid, singlet/odd/pi* character mixed in, the
    # bond-breaking character of an interchange (chs 7, 18, 19, 20, 29)
    r"\bcarácter(?=\s+(?:singlete|impar|de\s+ruptura|\$\\pi|s\b))",
    # the hole of a glass network or of the porphyrin ring, not a
    # semiconductor hole (chs 23, 24)
    r"(?<=en\s)(?:los|el)\s+huecos?\b",
    r"\bhueco\s+del\s+anillo",
    # a test population and an algal population (ch. 32)
    r"\bpoblación\s+de\s+ensayo",
    r"\bpoblaciones\s+de\s+algas",
    # the sun, not a colloidal sol (ch. 26 and its solutions)
    r"(?<=al\s)sol\b",
    # a laboratory operator wearing goggles (ch. 7)
    r"\boperador(?=\s+trabaja)",
    # the uncyclised reduction product of a radical clock, not the direct
    # product of two representations (ch. 27)
    r"(?<=el\s)producto\s+directo(?=\s+se\s+forman)",
    # "indistinguishable from the starting orientation": the ordinary sense,
    # not the quantum indistinguishability of identical particles (ch. 10)
    r"\bindistinguibles?(?=\s+de\s+la\s+de\s+partida)",
]
