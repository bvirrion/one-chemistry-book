"""Book 3 (University Chemistry, Year 2) -- id (Indonesian). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_id.py.

Curated by the id Book 3 agent (2026-10-06) from this edition's own harvest
(`--terms`) and a census of the linked words in their Indonesian contexts --
not translated from book3_en.py, not copied from another book's config.
AMBIG_POLICY stays "drop", as in English: no term is defined twice.

A word is linked only once its definition has been met, so a word defined
late in one sense is safe in earlier chapters that use it in another (the
"pengolahan reduktif" of ch. 21 and the "pengolahan asam" of ch. 24-25 precede
the work-up definition of ch. 35). The solutions come after every chapter, so
every word there is past its definition -- and there the work-up sense of
"pengolahan" is the right one. The translation itself kept several English
homograph pairs apart, so they need no protection at all:

  * the variance of a system (ch. 4, "varians") and the statistical variance
    (ch. 29, 34, "variansi");
  * a chain-propagation step (ch. 29, "propagasi") and the propagation of
    uncertainty (ch. 34, "perambatan");
  * a regression residual (ch. 34, "sisaan") and the residues of a reaction
    or of an amino acid ("residu");
  * the drinking-water "treatment" of ch. 34 ("penjernihan") and the work-up
    of ch. 35 ("pengolahan");
  * the recycle stream of ch. 4 ("daur ulang") and the recycling of plastics
    in ch. 29 ("didaur ulang", which the word boundary already keeps apart).

Homographs met AFTER their definition, each handled below:

  * fragmen (ch. 15's fragment method): the bare word is stoplisted -- it
    is used later for ozonolysis fragments (ch. 21), mass-spectrum fragments
    (ch. 32-33) and pieces of a structure; "orbital fragmen" and "ion
    fragmen" keep their links;
  * inisiasi (radical initiation, ch. 29) / the start of a Grignard reaction
    (solutions of ch. 35);
  * selektivitas (of a reactor, ch. 5) / chromatographic selectivity (ch. 31
    and its solutions) and the stereoselectivity of a Wittig ylide (ch. 27);
  * resolusi (chromatographic, ch. 31) / high-resolution mass spectrometry
    and analysers (ch. 32), an NMR resolution (ch. 33);
  * pemutusan (the disconnection of ch. 28) / the cleavage of a ring (ch.
    28's two-group proposition), the breaking of bonds into fragments and
    simple cleavages (ch. 32);
  * presisi (the noun precision, ch. 34) / the same word as an adjective
    ("lebih presisi", precise), which English does not link either.

The bare adjectives "kuat"/"lemah" are not harvested in this book (no
strong/weak definition), so the DROP the run file anticipates is not needed.
"""

STOP = {
    # ch. 15's fragment method: see the docstring
    "fragmen", "Fragmen",
}
NO_CAPITAL = set()
EXTRA = {
    # the bare noun of the "Enolates" definition (only "ion" phrase harvested;
    # coordinator, 2026-10-07, as English and Arabic)
    "enolat": "def:b2:enolates-aldol:enolate",
}
DROP = set()
DERIVED = {}
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

    # the start of a Grignard reaction (solutions of ch. 35), not radical
    # initiation (ch. 29)
    r"kegagalan\s+inisiasi",
    # chromatographic selectivity (ch. 31), the stereoselectivity of a Wittig
    # ylide (ch. 27) -- not a reactor's selectivity (ch. 5)
    r"Selektivitas(?=:\s+faktor)",
    r"lain:\s+selektivitas",
    r"terstabilkan\s+dan\s+selektivitasnya",
    # high-resolution MS and analysers (ch. 32), an NMR resolution (ch. 33):
    # not the chromatographic resolution of ch. 31
    r"resolusi\s+tinggi",
    r"daripada\s+resolusinya",
    # cleavage of a ring, bond breaking into fragments, simple cleavages: not
    # the disconnection of ch. 28
    r"pemutusan\s+cincin",
    r"pemutusan\s+ikatan-ikatan",
    r"pemutusan\s+sederhana",
    # "presisi" as an ADJECTIVE (precise: "lebih presisi", "dapat presisi"),
    # not the defined noun precision of ch. 34 -- English "precise" is not
    # linked either
    r"lebih\s+presisi",
    r"dapat\s+presisi",
]
