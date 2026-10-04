"""Book 2 (University Year 1) -- pt (Brazilian Portuguese). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_pt.py.

Curated by the pt Book 2 agent (2026-10-04) from this edition's own harvest
(`link_defined_terms.py --book 2 --lang pt --terms`: 392 linkable terms on
the same 175 targets as English) and a census of the harvested words in
their Portuguese contexts -- not translated from book2_en.py. AMBIG_POLICY
stays "drop", as in English: no term is defined twice.

As in English, a word is linked only once its definition has been met, so a
word defined late in one sense is safe in earlier chapters that use it in
another ("nós", the orbital nodes of ch. 1, precede the lattice nodes of
ch. 5; "integração" in ch. 8 precedes the NMR integration of ch. 17).
Portuguese homographs met AFTER their definition, each handled below:

  forte/fraco/fraca -> acid strength / any strength ("ligação forte",
               "nucleófilo fraco"): dropped, as fr drops fort/faible.
  grupo     -> the periodic-table group only before a number; the four
               linkable "grupo ..." terms put the modifier after the noun.
  ligante   -> a LIGAND (ch. 12) and the adjective "bonding" ("domínios
               ligantes", "6 ligantes" in the VSEPR table of ch. 28): en has
               two words, pt one. "par(es) ligante(s)" is its own term.
  rede      -> the crystal LATTICE (ch. 5) and a NETWORK (the hydrogen-bond
               network of ice, the covalent network of silica): en has two
               words and links only "lattice".
  blindagem -> screening (ch. 2) and, in ch. 17, the NMR shielding, whose
               own term is "blindagem magnética".
  nós       -> lattice nodes (ch. 5) and the pronoun "nós" ("para nós").
  período, bloco, multiplicidade, hidratação, axial/equatorial, proteção,
  perigo, quantitativa: as in en/fr (an induction period, a block of zinc,
  an NMR signal's multiplicity, hydration of ions, VSEPR positions,
  personal protection, the GHS08 pictogram's name and the signal word,
  "made quantitative").

pt-only work: irregular plurals the optional tail "(?:e?s)?" cannot make
("-ção" -> "-ções", "-al" -> "-ais", "-el" -> "-eis", "-il", "-em" ->
"-ens", "potencial" -> "potenciais"), each kept only where the form occurs
in this edition; the singulars of terms defined in the plural.
"""

STOP = {
    # bare adjectives: "ácido forte", "base fraca" keep their links
    "forte", "fortes", "fraco", "fraca", "fracos", "fracas",
}
NO_CAPITAL = set()
EXTRA = {}
# The bare adjectives would keep wrong-sense links through the per-chapter
# map of ch. 10 even when stoplisted ("o ácido mais forte", "uma constante
# fraca"), as in fr.
DROP = {"forte", "fortes", "fraco", "fraca", "fracos", "fracas"}
DERIVED = {
    # irregular plurals, each present in this edition
    "acetal": ["acetais"],
    "hemiacetal": ["hemiacetais"],
    "adição eletrofílica": ["adições eletrofílicas"],
    "alcino terminal": ["alcinos terminais"],
    "quiral": ["quirais"],
    "aquiral": ["aquirais"],
    "axial": ["axiais"],
    "equatorial": ["equatoriais"],
    "carga formal": ["cargas formais"],
    "configuração": ["configurações"],
    "configuração eletrônica": ["configurações eletrônicas"],
    "conformação": ["conformações"],
    "conformação alternada": ["conformações alternadas"],
    "cristal": ["cristais"],
    "cristal covalente": ["cristais covalentes"],
    "cristal iônico": ["cristais iônicos"],
    "cristal molecular": ["cristais moleculares"],
    "fator pré-exponencial": ["fatores pré-exponenciais"],
    "fração molar": ["frações molares"],
    "fração mássica": ["frações mássicas"],
    "integração": ["integrações"],
    "interação de London": ["interações de London"],
    "ligação $\\sigma$": ["ligações $\\sigma$"],
    "ligação covalente": ["ligações covalentes"],
    "ligação dativa": ["ligações dativas"],
    "ligação de hidrogênio": ["ligações de hidrogênio"],
    "nível de oxidação": ["níveis de oxidação"],
    "ordem global": ["ordens globais"],
    "perfil de energia": ["perfis de energia"],
    "ponto final": ["pontos finais"],
    "potencial padrão": ["potenciais padrão"],
    "potencial de eletrodo": ["potenciais de eletrodo"],
    "pressão parcial": ["pressões parciais"],
    "projeção de Newman": ["projeções de Newman"],
    "radical": ["radicais"],
    "razão de raios": ["razões de raios"],
    "reação regiosseletiva": ["reações regiosseletivas"],
    "semirreação": ["semirreações"],
    "solução equivalente": ["soluções equivalentes"],
    "sítio intersticial": ["sítios intersticiais"],
    "titulação": ["titulações"],
    "titulação direta": ["titulações diretas"],
    "titulação potenciométrica": ["titulações potenciométricas"],
    "variável extensiva": ["variáveis extensivas"],
    "variável intensiva": ["variáveis intensivas"],
    "velocidade inicial": ["velocidades iniciais"],
    "solução-tampão": ["soluções-tampão"],
    # the short form pt uses for the defined "etapa determinante da
    # velocidade" (en: "rate-determining step" throughout)
    "etapa determinante da velocidade": ["etapa determinante",
                                         "etapas determinantes"],
    # terms defined in the plural, used in the singular
    "enantiômeros": ["enantiômero"],
    "diastereoisômeros": ["diastereoisômero"],
    "estereoisômeros": ["estereoisômero"],
    "isômeros constitucionais": ["isômero constitucional"],
    "parâmetros de rede": ["parâmetro de rede"],
    "elétrons de valência": ["elétron de valência"],
    "nós": ["nó"],
    # adjectives defined in one gender, used in the other
    "hidrofílico": ["hidrofílica"],
    "hidrofóbico": ["hidrofóbica"],
    "cúbica de faces centradas": ["cúbico de faces centradas"],
    "hexagonal compacta": ["hexagonal compacto"],
}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across
# a source line break must still be protected.
EXTRA_PROTECT = [
    # Coordinator, 2026-10-04: the zinc anode blocks of ch. 14 are not the
    # periodic-table block; English now protects the same sites.
    r"blocos?(?=\s+cinzentos?)",

    # "grupo" is the periodic-table group only before a number (grupo 16,
    # grupos 13 a 15); "grupo metila", "grupo OH", "o grupo" stay plain.
    # Portuguese puts the modifier after the noun, so the four linkable
    # "grupo ..." terms are excluded by a lookahead.
    r"\b[Gg]rupos?\b(?!\s*~?\d)"
    r"(?!\s+(?:doador(?:es)?|aceptor(?:es)?|de\s+saída|protetor(?:es)?)\b)",
    # "ligante(s)" as the adjective "bonding" of the VSEPR table (ch. 28),
    # not a ligand: "domínios ligantes", "6 ligantes", "sete pares ligantes"
    # is the bonding-pair term and keeps its link.
    r"\bdomínios?\s+ligantes?",
    r"(?<=\d\s)ligantes?",
    # a network, not the crystal lattice: the hydrogen-bond network of ice
    # (ch. 6), the covalent network of graphite and silica (ch. 6, 27)
    r"\brede(?=\s+(?:covalente|aberta|está\s+parcialmente|aparece|"
    r"hexagonal\s+de|tridimensional|de\s+\\ce))",
    # NMR shielding inside the chemical-shift proof (ch. 17), not screening
    r"fator\s+de\s+blindagem",
    # the pronoun "nós" (toward us), not the lattice nodes
    r"\bpara\s+nós\b",
    # NMR multiplicity of a signal, not the multiplicity of a cell (ch. 17)
    r"\bmultiplicidade(?=\s+de\s+cada\s+sinal)",
    # optical activity lost, not the thermodynamic activity (ch. 19)
    r"\bperda\s+da\s+atividade",
    # hydration of ions, not of an alkene (ch. 28)
    r"\bhidratação(?=\s+dos\s+íons)",
    # VSEPR positions of a trigonal bipyramid, not cyclohexane bonds
    r"\bposições?\s+(?:axia(?:l|is)|equatoria(?:l|is))",
    # personal protection in the safety chapters, not a protecting group
    r"\bproteção\s+(?:individual|ocular)",
    r"\bexposição\s+e\s+proteção",
    r"\bvia,\s+proteção",
    r"\btela\s+de\s+proteção",
    # a time period (an induction period), not a row of the table
    r"\bperíodos?\s+de\s+indução",
    # a block of zinc (a sacrificial anode), not the s/p block
    r"\bblocos?\s+de\s+zinco",
    # "quantitativa" as a theory or a measurement, not a reaction
    r"\btornada\s+quantitativa",
    r"\btorna\s+quantitativa",
    r"\bmedida\s+quantitativa",
    # the GHS08 pictogram's name and the signal word, not the defined term
    r"\bperigo\s+à\s+saúde",
    r"\\emph\{Perigo\}",
    # the GHS03 pictogram's caption "oxidante" (en: "oxidising", a hazard
    # class), not the redox oxidant of ch. 13
    r"\\footnotesize\s+oxidante",
    # key names inside the periodic-table macro's options ("f block=false")
    r"\\omperiodictable\[[^\]]*\]",
    # chemfig arrow labels: \arrow{->[label][label]}
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
    # pgfplots tick labels are code
    r"[xy]ticklabels=\{[^{}]*\}",
]
