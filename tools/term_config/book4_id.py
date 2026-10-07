"""Book 4 (University Chemistry, Year 3) -- id (Indonesian). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_id.py.

Curated by the id Book 4 agent (2026-10-07) from this edition's own harvest
(`--terms`) and a census of every linked word in its Indonesian context,
compared target by target with the English links -- not translated from
book4_en.py, not copied from another book's config. AMBIG_POLICY stays
"drop", as in English.

A word is linked only once its definition has been met, so earlier uses in
another sense are safe: the d-electron "lubang" of ch. 18 and ch. 20 precede
the semiconductor hole of ch. 22; the "populasi" of ch. 2-9 precede the
Boltzmann population of ch. 10. Homographs met AFTER their definition, each
handled below:

  * migrasi (the ionic migration of ch. 15's mass-transport definition): the
    bare word is stoplisted. Every later use is another sense -- the
    migratory insertion of ch. 21 ("insersi migrasi"), the 1,2-shift and the
    Beckmann migration of ch. 27, the hydrogen migration of the ch. 26
    solutions -- and English never links bare "migration" at all;
  * operator (the quantum operator, ch. 1) / the people who run a laser or a
    plant (ch. 5, 7 and the ch. 31 solutions);
  * karakter (the character of a representation, ch. 4) / the odd (u)
    character of a d state (ch. 18), the bond-breaking character of an
    interchange (ch. 19), the pi* character of an alkene (ch. 20) and the s
    character of an sp2 nitrogen (ch. 29) -- English links none of these;
  * populasi (the Boltzmann population, ch. 10) / populations of algae, of
    test animals and of birds (ch. 32). The "populasi zat antara" of ch. 28
    and the population inversion of the ch. 18 solutions keep their links,
    as in English;
  * lubang (the semiconductor hole, ch. 22) / the hole in the middle of a
    porphyrin ring (ch. 24).

The bare adjectives "kuat"/"lemah" are not harvested in this book, so no
DROP is needed.
"""

STOP = {
    # ch. 15's ionic migration: see the docstring
    "migrasi", "Migrasi",
}
NO_CAPITAL = set()
EXTRA = {
    # the adjective of the "Diffusion and activation control" definition:
    # only the phrase "reaksi terkendali difusi" is harvested, the prose says
    # "terkendali difusi" / "dikendalikan difusi" (English links
    # "diffusion-controlled" the same five times)
    "terkendali difusi": "def:b3:rate-theories:diffusion",
    "dikendalikan difusi": "def:b3:rate-theories:diffusion",
}
DROP = set()
DERIVED = {
    # plurals by reduplication of the head noun of a multi-word term
    # (lang_id.py: unreachable otherwise), each present in this edition and
    # each in the defined sense
    "faktor Franck--Condon": ["faktor-faktor Franck--Condon"],
    "fungsi eigen": ["fungsi-fungsi eigen"],
    "nilai eigen": ["nilai-nilai eigen"],
    "unsur simetri": ["unsur-unsur simetri"],
    "operasi simetri": ["operasi-operasi simetri"],
    "modus normal": ["modus-modus normal"],
    "puncak silang": ["puncak-puncak silang"],
    "pusat inversi": ["pusat-pusat inversi"],
    "bidang kisi": ["bidang-bidang kisi"],
    "kompleks teraktivasi": ["kompleks-kompleks teraktivasi"],
    "reaksi berosilasi": ["reaksi-reaksi berosilasi"],
    "suku medan ligan": ["suku-suku medan ligan"],
    "fragmen isolobal": ["fragmen-fragmen isolobal"],
    "keadaan triplet": ["keadaan-keadaan triplet"],
}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# Multi-word patterns use \s+ between words: a phrase wrapped across a source
# line break must still be protected. A look-ahead anchored on a word that is
# itself a term must allow an optional wrapper: (?:\\omterm\{[^{}]*\}\{)?
EXTRA_PROTECT = [
    # "indistinguishable" of a symmetry operation (a configuration
    # indistinguishable from the original / from itself, ch. 4): everyday sense,
    # not quantum indistinguishability (coordinator, 2026-10-07, from the hi agent)
    r"tak\s+terbedakan(?=\s+dari\s+(?:dirinya|semula|konfigurasi|aslinya))",
    # chemfig settings and arrow labels: \arrow{->[label][label]}
    r"\\setchemfig\{[^{}]*\}",
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
    # pgfplots tick-label lists (every Book 1-2 edition needed this)
    r"[xy]ticklabels=\{[^{}]*\}",

    # people who run an instrument or a plant, not the quantum operator
    r"operatornya\s+bekerja",
    r"para\s+operatornya",
    r"operator\s+yang\s+terlatih",
    # orbital or mechanistic character, not the character of a representation
    r"karakter\s+ganjil",
    r"karakter\s+pemutusan",
    r"karakter\s+s\b",
    r"karakter(?=\s+\$\\pi)",      # "karakter $\pi^*$": never consume the $
    # organisms, not Boltzmann populations
    r"populasi(?=\s+padat\s+alga)",
    r"setengah\s+populasi",
    r"populasi(?=\s+burung)",
    # the hole of a porphyrin ring, not the semiconductor hole
    r"lubang(?=\s+cincin)",
]
