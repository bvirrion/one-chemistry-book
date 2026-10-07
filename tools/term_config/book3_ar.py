"""Book 3 (University Chemistry, Year 2) -- ar (Arabic). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_ar.py.

Curated by the ar Book 3 agent (2026-10-06) from this edition's own harvest
(`--terms`) and the frequency and chapter-set censuses against the English
twin -- not translated from book3_en.py, not seeded from another book's config
(the plurals below point at Book 3 labels only).

Arabic homographs found by the harvest and the censuses, each handled below:
شظية (a fragment of the fragment-orbital method, ch. 15 / a mass-spectrum
fragment, ch. 32), ميز (chromatographic resolution, ch. 31 / the resolving
power of a mass analyser or of an NMR spectrum, ch. 32-33), الانتقائية
(a reactor's selectivity, ch. 5 / stereo-, regio- and chemoselectivity, ch.
17 and 21 / the chromatographic selectivity factor, ch. 31), تحويل (the
conversion X of a reactor, ch. 5 / "converting A into B", everywhere), تشتت
(a polymer's dispersity, ch. 29 / statistical dispersion, ch. 34), the chain
steps بدء / انتشار (initiation and propagation of a chain polymerisation, ch.
29 / the start of a Grignard reaction, ch. 35, longitudinal diffusion along a
column, ch. 31, propagation of uncertainty, ch. 34), تكامل الرنين (the Hückel
resonance integral / an NMR integral, «تكاملات الرنين المغناطيسي»).
"""

STOP = {
    # ch. 15's fragment: linked in its own chapter only (the chapter-local
    # map); a mass-spectrum fragment (ch. 32-33) must not point at it. The
    # compound "مدار الشظية" and its plurals (EXTRA) keep their links.
    "شظية", "الشظية",
}
NO_CAPITAL = set()

# Arabic forms most plurals and duals by internal change or by endings that
# no tail rule reaches (lang_ar.py: WORD_TAIL is empty). The plural, dual and
# indefinite forms this book uses are declared here, each pointing at the
# Book 3 target its singular already reaches; the article and the one-letter
# prefixes are added by HEAD, on every word.
EXTRA = {
    # thermodynamics of mixtures and phase diagrams
    "معاملات نشاطية": "def:b2:chemical-potential:activity-coefficient",
    "محلولًا صلبًا": "def:b2:solid-liquid-diagrams:solid-solution",
    "محلولان صلبان": "def:b2:solid-liquid-diagrams:solid-solution",
    "محلولين صلبين": "def:b2:solid-liquid-diagrams:solid-solution",
    "محاليل صلبة": "def:b2:solid-liquid-diagrams:solid-solution",
    "منحنيات تبريد": "def:b2:solid-liquid-diagrams:cooling-curve",
    "أطباق نظرية": "def:b2:liquid-vapour-diagrams:fractional-distillation",
    # the standard reaction Gibbs energy, as Arabic phrases it in ch. 6
    "طاقة جيبس القياسية لتفاعل": "def:b2:reaction-free-energy:reaction-gibbs",
    "طاقة جيبس القياسية لتفاعله": "def:b2:reaction-free-energy:reaction-gibbs",
    "طاقة جيبس القياسية لتفاعلها": "def:b2:reaction-free-energy:reaction-gibbs",
    "طاقة جيبس قياسية": "def:b2:reaction-free-energy:reaction-gibbs",
    # electrochemistry
    "فرط جهد": "def:b2:current-potential-curves:overpotential",
    # orbitals
    "مدارات جزيئية": "def:b2:diatomic-mos:lcao",
    "مدارًا جزيئيًا": "def:b2:diatomic-mos:lcao",
    "مداران جزيئيان": "def:b2:diatomic-mos:lcao",
    "مداراته الجزيئية": "def:b2:diatomic-mos:lcao",
    "مدارات رابطة": "def:b2:diatomic-mos:bonding",
    "مداران رابطان": "def:b2:diatomic-mos:bonding",
    "مدارين رابطين": "def:b2:diatomic-mos:bonding",
    "مدارًا رابطًا": "def:b2:diatomic-mos:bonding",
    "مداراته الرابطة": "def:b2:diatomic-mos:bonding",
    "مدارات مضادة للربط": "def:b2:diatomic-mos:bonding",
    "مدارًا مضادًا للربط": "def:b2:diatomic-mos:bonding",
    "مدارات غير رابطة": "def:b2:diatomic-mos:bonding",
    "مداران غير رابطين": "def:b2:diatomic-mos:bonding",
    "مدارين غير رابطين": "def:b2:diatomic-mos:bonding",
    "مدارًا غير رابط": "def:b2:diatomic-mos:bonding",
    "تكاملات الرنين": "def:b2:diatomic-mos:integrals",
    "تكامل رنين": "def:b2:diatomic-mos:integrals",
    "تكاملات كولوم": "def:b2:diatomic-mos:integrals",
    "مدارات شظية": "def:b2:fragment-orbitals:fragment",
    "مدارات شظيتين": "def:b2:fragment-orbitals:fragment",
    "مدارات شظايا": "def:b2:fragment-orbitals:fragment",
    "تركيبان متكيفان مع التناظر": "def:b2:fragment-orbitals:symmetry-adapted",
    "تركيبين متكيفين مع التناظر": "def:b2:fragment-orbitals:symmetry-adapted",
    "تراكيب متكيفة مع التناظر": "def:b2:fragment-orbitals:symmetry-adapted",
    "عطرية": "def:b2:huckel:aromatic",
    # reactivity and complexes
    "محبات للنواة قاسية": "def:b2:frontier-orbitals:hard-soft",
    "محبات للنواة لينة": "def:b2:frontier-orbitals:hard-soft",
    "محبات للإلكترونات قاسية": "def:b2:frontier-orbitals:hard-soft",
    "محبات للإلكترونات لينة": "def:b2:frontier-orbitals:hard-soft",
    "محبًا للنواة قاسيًا": "def:b2:frontier-orbitals:hard-soft",
    "محبًا للنواة لينًا": "def:b2:frontier-orbitals:hard-soft",
    "محبًا للإلكترونات قاسيًا": "def:b2:frontier-orbitals:hard-soft",
    "محبًا للإلكترونات لينًا": "def:b2:frontier-orbitals:hard-soft",
    "محب للنواة قاسٍ": "def:b2:frontier-orbitals:hard-soft",
    "محب للإلكترونات قاسٍ": "def:b2:frontier-orbitals:hard-soft",
    "عالية السبين": "def:b2:ligand-field:spin",
    "منخفضة السبين": "def:b2:ligand-field:spin",
    "متماكبي الارتباط": "def:b2:coordination-complexes:isomers",
    "متماكبا الارتباط": "def:b2:coordination-complexes:isomers",
    "تبادل ربائط": "def:b2:catalytic-cycles:ligand-exchange",
    "تبادل ربيطة": "def:b2:catalytic-cycles:ligand-exchange",
    "كوبرات عضوية": "def:b2:conjugate-additions:cuprate",
    # carbonyl chemistry, biomolecules, polymers
    "تصبّن": "def:b2:acyl-substitution:saponification",
    "تصبين": "def:b2:acyl-substitution:saponification",
    "أنومير": "def:b2:biomolecules:anomer",
    "أنوميران": "def:b2:biomolecules:anomer",
    "أنوميرين": "def:b2:biomolecules:anomer",
    "أحماض دهنية": "def:b2:biomolecules:lipid",
    "ثلاثيات غليسريد": "def:b2:biomolecules:lipid",
    "فوسفوليبيدات": "def:b2:biomolecules:lipid",
    "فوسفوليبيدية": "def:b2:biomolecules:lipid",
    "نوكليوتيدات": "def:b2:biomolecules:nucleotide",
    "نوكليوزيدات": "def:b2:biomolecules:nucleotide",
    "إيلاستومرات": "def:b2:polymer-synthesis:elastomer",
    "درجة حرارة تحوله الزجاجي": "def:b2:polymer-synthesis:transitions",
    # analysis
    "أنماط نظائرية": "def:b2:mass-spec-atomic:isotope-pattern",
    "نمطه النظائري": "def:b2:mass-spec-atomic:isotope-pattern",
    "بواقٍ": "def:b2:measurement-statistics:calibration",
    "بواقي": "def:b2:measurement-statistics:calibration",
    "بواقيه": "def:b2:measurement-statistics:calibration",
    "مستقيم المعايرة": "def:b2:measurement-statistics:calibration",
}

DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# Multi-word patterns use \s+ between words: a phrase wrapped across a source
# line break must still be protected. A look-ahead anchored on a word that is
# itself a term allows an optional wrapper: (?:\\omterm\{[^{}]*\}\{)?
EXTRA_PROTECT = [
    # the resolving power of a mass analyser or an NMR spectrum (ch. 32-33),
    # not the chromatographic resolution of ch. 31
    r"(?<=قدرة\s)ميز",
    r"(?<=قدرة\s)الميز",
    r"(?<=قدرات\s)الميز",
    r"(?<=عالي\s)الميز",
    r"(?<=تام\s)الميز",
    # stereo-, regio- and chemoselectivity (ch. 17, 21) and the
    # chromatographic selectivity factor (ch. 31), not a reactor's selectivity
    r"الانتقائية(?=\s+(?:فراغيًا|موضعيًا|الكيميائية))",
    r"الانتقائية(?=:\s+العامل)",
    r"(?<=الأخرى:\s)الانتقائية",
    # "converting A into B", not a reactor's conversion X (ch. 5)
    r"تحويل(?=\s+(?:[^\s.،؛:]+\s+){0,3}إلى\s)",
    r"(?<=قابلة\s)للتحويل",
    # statistical dispersion (ch. 34), not a polymer's dispersity (ch. 29)
    r"تشتت(?=\s+(?:قياسين|\$s\$|قراءات))",
    r"(?<=إلى\s)التشتت(?=،)",
    # diffusion along a column (ch. 31) and propagation of uncertainty
    # (ch. 34), not chain propagation (ch. 29)
    r"الانتشار(?=\s+(?:على\s+طول|والتبادل))",
    r"انتشار(?=\s+(?:الارتياب|عامة))",
    # the start of a Grignard reaction (ch. 35), not chain initiation (ch. 29)
    r"بدء(?=\s+التفاعل)",
    r"(?<=في\s)البدء",
    r"(?<=قبل\s)البدء",
    r"البدء(?=\s+عند)",
    r"(?<=إخفاق\s)البدء",
    # NMR integrals, not the Hückel resonance integral
    r"تكاملات?\s+الرنين(?=\s+المغناطيسي)",
    # chapter and section titles that carry a \texorpdfstring (nested
    # braces): the linker's heading mask stops at the first inner brace
    r"\\(?:chapter|section)\*?\{(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*\}",
    # chemfig settings and arrow labels: \arrow{->[label][label]}
    r"\\setchemfig\{[^{}]*\}",
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
    # pgfplots tick-label lists
    r"[xy]ticklabels=\{[^{}]*\}",
]
