"""Book 3 (University Chemistry, Year 2) -- pt (Brazilian Portuguese). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_pt.py.

Curated by the pt Book 3 agent (2026-10-06) from this edition's own harvest
(`link_defined_terms.py --book 3 --lang pt --terms`: 418 terms harvested,
427 linkable, none defined twice) and a census of the harvested words in
their Portuguese contexts -- not translated from book3_en.py. AMBIG_POLICY
stays "drop", as in English.

As in English, a word is linked only once its definition has been met, so a
word defined late in one sense is safe in earlier chapters that use it in
another ("resolução", the chromatographic resolution of ch. 31, follows the
resolution of a complex into enantiomers in ch. 18; "terminação", the chain
step of ch. 29, follows the "-ato" ending of ch. 18's nomenclature;
"tratamento", the work-up of ch. 35, follows every "tratamento ácido"
before it). Portuguese homographs met AFTER their definition, each handled
below:

  fragmento -> ch. 15's fragment method; the bare word is used later for
               ozonolysis fragments (ch. 21), synthons (ch. 28) and
               mass-spectrum fragments (ch. 32-33): stoplisted, as en does.
               "orbital(is) de fragmento" and "íon fragmento" keep theirs.
  variância -> the variance of a system (ch. 4) and the statistical variance
               of ch. 29 and 34.
  propagação, iniciação -> the chain steps of ch. 29; the propagation of
               uncertainties (ch. 34) and the initiation of a Grignard
               reaction (ch. 35).
  seletividade -> a reactor's selectivity (ch. 5); the chromatographic
               selectivity factor's short form in ch. 31.
  resolução -> the chromatographic resolution (ch. 31); the resolving power
               ("poder de resolução"), a high-resolution analyser and a
               spectrometer's resolution (ch. 32-33), and "a resolução de uma
               estrutura" (solving a structure, ch. 33).
  fator de retenção -> the column's k (ch. 31); the R_f of a TLC plate.
  purga     -> the purge stream of a recycle loop (ch. 4); flushing a flask
               with nitrogen (ch. 35).
  resíduo   -> a least-squares residual (ch. 34); waste (ch. 35).

pt-only work: irregular plurals the per-word tail "(?:e?s)?" cannot make
("-ção" -> "-ções", "-al" -> "-ais", "-el" -> "-eis", "-ol" -> "-óis",
"-ão" -> "-ões"), each kept only where the form occurs in this edition, and
adjectives defined in one gender and used in the other (aromático /
aromática, exotérmica / exotérmico, paramagnética / paramagnético ...).
"""

STOP = {
    # ch. 15's fragment method only; see the docstring
    "fragmento", "fragmentos", "Fragmento", "Fragmentos",
}
NO_CAPITAL = set()
EXTRA = {
    # the bare noun of the "Enolates" definition (only "ion" phrase harvested;
    # coordinator, 2026-10-07, as English and Arabic)
    "enolato": "def:b2:enolates-aldol:enolate",
}
DROP = set()
DERIVED = {
    # irregular plurals, each present in this edition
    "adição de Michael": ["adições de Michael"],
    "adição nucleofílica": ["adições nucleofílicas"],
    "cadeia lateral": ["cadeias laterais"],
    "clivagem $\\alpha$": ["clivagens $\\alpha$"],
    "combinação adaptada à simetria": ["combinações adaptadas à simetria"],
    "condensação aldólica": ["condensações aldólicas"],
    "configuração $d^n$": ["configurações $d^n$"],
    "conversão": ["conversões"],
    "descarboxilação": ["descarboxilações"],
    "desconexão": ["desconexões"],
    "energia orbital": ["energias orbitais"],
    "enol": ["enóis"],
    # en links "aldol" in "aldol reaction", "crossed aldol", "retro-aldol";
    # pt says "reação aldólica", "aldólica cruzada", "retroaldólica"
    "aldol": ["aldólica", "aldólicas", "retroaldólica"],
    "fase móvel": ["fases móveis"],
    "função de onda": ["funções de onda"],
    "grandeza parcial molar": ["grandezas parciais molares"],
    "hemiaminal": ["hemiaminais"],
    "integral de Coulomb": ["integrais de Coulomb"],
    "integral de ressonância": ["integrais de ressonância"],
    "ligação fosfodiéster": ["ligações fosfodiéster"],
    "ligação glicosídica": ["ligações glicosídicas"],
    "ligação peptídica": ["ligações peptídicas"],
    "mistura ideal": ["misturas ideais"],
    "nó radial": ["nós radiais"],
    "orbital $\\pi$": ["orbitais $\\pi$"],
    "orbital $\\sigma$": ["orbitais $\\sigma$"],
    "orbital antiligante": ["orbitais antiligantes"],
    "orbital de fragmento": ["orbitais de fragmento"],
    "orbital ligante": ["orbitais ligantes"],
    "orbital molecular": ["orbitais moleculares"],
    "ordem de ligação": ["ordens de ligação"],
    "parte radial": ["partes radiais"],
    "perfil isotópico": ["perfis isotópicos"],
    "potencial químico": ["potenciais químicos"],
    "reação de Wittig": ["reações de Wittig"],
    "resolução": ["resoluções"],
    "sal de fosfônio": ["sais de fosfônio"],
    "sobretensão": ["sobretensões"],
    "solução diluída ideal": ["soluções diluídas ideais"],
    "solução sólida": ["soluções sólidas"],
    "volume parcial molar": ["volumes parciais molares"],
    # adjectives defined in one gender, used in the other
    "aromático": ["aromática"],
    "antiaromático": ["antiaromática"],
    "exotérmica": ["exotérmico"],
    "endotérmica": ["endotérmico"],
    "paramagnética": ["paramagnético"],
    "diamagnética": ["diamagnético"],
    "isotática": ["isotático"],
    "sindiotática": ["sindiotático"],
    "atática": ["atático"],
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
    r"\bvariâncias?(?=\s+\$\\sigma)",
    r"[Vv]ariância\s+(?:de\s+uma\s+(?:soma|combinação|lei)|da\s+média)",
    r"soma\s+das\s+variâncias",
    r"média\s+e\s+da\s+variância",
    # propagation of uncertainties (ch. 34), not a chain-propagation step
    r"[Pp]ropagação(?=\s+das\s+incertezas)",
    r"regra\s+geral\s+de\s+propagação",
    r"[Ll]ei\s+de\s+propagação",
    # initiation of a Grignard reaction (ch. 35), not radical initiation
    r"antes\s+da\s+iniciação",
    r"falha\s+de\s+iniciação",
    # chromatographic selectivity (ch. 31), not a reactor's selectivity
    r"Seletividade(?=:\s+o\s+fator)",
    r"alavancas:\s+a\s+seletividade",
    # the R_f of a TLC plate (Year 1's retention factor), not the column's k
    r"fator\s+de\s+retenção\s+\$R_f\$",
    # resolving power, high-resolution analysers and spectral resolution
    # (ch. 32-33), solving a structure (ch. 33): not the resolution of ch. 31
    r"[Pp]oder(?:es)?\s+de\s+resolução",
    r"analisador\s+de\s+alta\s+resolução",
    r"que\s+a\s+resolução",
    r"a\s+resolução\s+de\s+uma\s+estrutura",
    # flushing a flask with nitrogen (ch. 35), not the purge of a recycle loop
    r"antes\s+da\s+purga",
    # waste (ch. 35), not a least-squares residual
    r"menos\s+resíduos",
]
