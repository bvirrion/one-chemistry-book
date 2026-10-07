"""Book 3 (University Chemistry, Year 2) -- es (Spanish). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_es.py.

Curated by the es Book 3 agent (2026-10-06) from this edition's own harvest
(`--terms`, 432 lines) and a census of every link in its Spanish context,
target by target against the English link counts -- not translated from
book3_en.py. AMBIG_POLICY stays "drop", as in English: no term is defined
twice.

A word is linked only once its definition has been met, so a word defined
late in one sense is safe in earlier chapters that use it in another. Spanish
homographs met AFTER their definition, each handled below:
  fragmento(s)   the fragment of ch. 15 / ozonolysis, mass-spectrum and
                 retrosynthetic fragments (ch. 21-33): bare word stoplisted,
                 "orbital(es) de fragmento" keeps its link (as in English);
  varianza       the variance of a system (ch. 4) / the statistical variance
                 (ch. 29, 34);
  propagación    a chain-propagation step (ch. 29) / the propagation of
                 uncertainty (ch. 34);
  iniciación     radical initiation (ch. 29) / the start of a Grignard
                 formation (ch. 35);
  selectividad   a reactor's selectivity (ch. 5) / the chromatographic
                 selectivity factor (ch. 31);
  resolución     the chromatographic resolution (ch. 31) / the resolving power
                 of a mass analyser and spectral resolution (ch. 32-33), and
                 "resolución de una estructura" (solving it);
  residuos       the residuals of a calibration (ch. 34) / chemical waste
                 (ch. 35).
"""

STOP = {
    # ch. 15's fragment method; "orbital de fragmento" is a separate term.
    "fragmento", "fragmentos", "Fragmento", "Fragmentos",
}
NO_CAPITAL = set()
# The adjective of "aldol" in its elliptic uses ("una aldólica cruzada", "la
# aldólica intramolecular", "Deshágase la aldólica"), where English links the
# bare word "aldol"; "adición/condensación aldólica" are longer terms and win.
EXTRA = {
    # the bare noun of the "Enolates" definition (only "ion" phrase harvested;
    # coordinator, 2026-10-07, as English and Arabic)
    "enolato": "def:b2:enolates-aldol:enolate",
    "aldólica": "def:b2:enolates-aldol:aldol",
    "aldólicas": "def:b2:enolates-aldol:aldol",
}
DROP = set()
# Plurals the tail cannot reach (the accent of a final -ón, -ión or of
# "orden" moves in the plural) and the other gender of the adjectives the
# definitions print in one gender only; each kept because it occurs.
DERIVED = {
    "orden de enlace": ["órdenes de enlace"],
    "sobretensión": ["sobretensiones"],
    "disolución sólida": ["disoluciones sólidas"],
    "combinación adaptada a la simetría": ["combinaciones adaptadas a la simetría"],
    "paramagnética": ["paramagnético", "paramagnéticos", "paramagnéticas"],
    "diamagnética": ["diamagnético", "diamagnéticos", "diamagnéticas"],
    "exotérmica": ["exotérmico", "exotérmicos", "exotérmicas"],
    "endotérmica": ["endotérmico", "endotérmicos", "endotérmicas"],
    "atérmica": ["atérmico", "atérmicos"],
    "exergónica": ["exergónico", "exergónicos", "exergónicas"],
    "endergónica": ["endergónico", "endergónicos", "endergónicas"],
    "aromático": ["aromática", "aromáticas"],
    "antiaromático": ["antiaromática", "antiaromáticas"],
    "isotáctica": ["isotáctico", "isotácticos"],
    "sindiotáctica": ["sindiotáctico", "sindiotácticos"],
    "atáctica": ["atáctico", "atácticos"],
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
    # pgfplots tick-label lists (every Book 1-2 edition needed this)
    r"[xy]ticklabels=\{[^{}]*\}",

    # statistical variance (ch. 29, 34), not the variance of a system (ch. 4)
    r"\b[Vv]arianzas?\b(?=\s+\$\\sigma)",
    r"[Vv]arianza\s+de\s+(?:una|la)\s+(?:suma|combinación|media)",
    r"suma\s+de\s+las\s+varianzas",
    r"media\s+y\s+la\s+varianza",
    # propagation of uncertainty (ch. 34), not a chain-propagation step
    r"[Pp]ropagación(?=\s+de\s+(?:las?\s+)?incertidumbres?)",
    r"regla\s+general\s+de\s+propagación",
    # the start of a Grignard formation (ch. 35), not radical initiation
    r"antes\s+de\s+la\s+iniciación",
    r"fallo\s+de\s+la\s+iniciación",
    # chromatographic selectivity (ch. 31), not a reactor's selectivity
    r"Selectividad(?=:\s+el\s+factor)",
    r"palancas:\s+la\s+selectividad",
    # the R_f of a TLC plate, not the column's retention factor k
    r"factor\s+de\s+retención\s+\$R_f\$",
    # resolving power and spectral resolution (ch. 32-33), and solving a
    # structure, not the chromatographic resolution of ch. 31
    r"[Pp]oder(?:es)?\s+de\s+resolución",
    r"analizador\s+de\s+alta\s+resolución",
    r"resolución\s+espectral",
    r"resolución\s+de\s+una\s+estructura",
    # chemical waste (ch. 35), not the residuals of a calibration (ch. 34)
    r"menos\s+residuos",
    r"residuos\s+(?:acuosos|de\s+disolventes)",
]
