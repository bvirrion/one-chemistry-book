"""Book 4 (University Chemistry, Year 3) -- ar (Arabic). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_ar.py.

Curated by the ar Book 4 agent (2026-10-07) from this edition's own harvest
(`--terms`) and the frequency and chapter-set censuses against the English
twin -- not translated from book4_en.py, not seeded from another book's config
(every EXTRA below points at a Book 4 label).

Arabic homographs found by the harvest and the censuses, each handled in
EXTRA_PROTECT below:
الحمل (convection in electrode kinetics, ch. 15 / the organic load of a river,
ch. 32, and an engine's load, ch. 22 solutions), هجرة (ionic migration, ch. 15 /
the migration of a group in a 1,2-shift or a sigmatropic shift, ch. 26-27),
القلوية (the alkalinity of a water, ch. 32 / the adjective "alkali" in «الفلزات
القلوية», ch. 33), مستوي الانزلاق (a crystallographic glide plane, ch. 9 / the
slipping plane of the electrical double layer, ch. 17), إشغال (the Boltzmann
population of levels, ch. 10 / the occupation of orbitals by electrons, ch.
27), ثقب (a semiconductor hole, ch. 22-23 / the ozone hole, ch. 14). One
homograph was removed from the text instead: «القيمة الذاتية» (eigenvalue)
had been used for "the intrinsic value" of a solubility (ch. 25 solutions) and
now reads «الذوبانية الذاتية».

Arabic forms most plurals, duals and indefinite constructs by internal change
or by endings that no tail rule reaches (lang_ar.py: WORD_TAIL is empty);
those this book uses are declared in EXTRA, each pointing at the target its
singular already reaches. HEAD adds the article and the one-letter proclitics
on every word.
"""

STOP = set()
NO_CAPITAL = set()

EXTRA = {
    # quantum mechanics and atoms
    "مبدِّلين": "def:b3:quantum-model-systems:commutator",
    "مؤثرات السلّم": "def:b3:quantum-model-systems:ladder",
    "درجة انحلال": "def:b3:quantum-model-systems:degenerate",
    "درجة انحلاله": "def:b3:quantum-model-systems:degenerate",
    "درجة انحلالها": "def:b3:quantum-model-systems:degenerate",
    "درجات الانحلال": "def:b3:quantum-model-systems:degenerate",
    "درجات انحلالها": "def:b3:quantum-model-systems:degenerate",
    "مدارات مغزلية": "def:b3:many-electron-atoms:spin-orbital",
    "مدارين مغزليين": "def:b3:many-electron-atoms:spin-orbital",
    "مداران مغزليان": "def:b3:many-electron-atoms:spin-orbital",
    "مدارًا مغزليًا": "def:b3:many-electron-atoms:spin-orbital",
    "دوال منتشرة": "def:b3:computational-chemistry:split-valence",
    "دوالًا منتشرة": "def:b3:computational-chemistry:split-valence",
    # symmetry
    "عناصر التناظر": "def:b3:point-groups:operation",
    "عنصرا التناظر": "def:b3:point-groups:operation",
    "عمليات التناظر": "def:b3:point-groups:operation",
    "عمليتا التناظر": "def:b3:point-groups:operation",
    "تمثيلات غير قابلة للاختزال": "def:b3:point-groups:irrep",
    "تمثيلًا غير قابل للاختزال": "def:b3:point-groups:irrep",
    "جداول المميِّزات": "def:b3:point-groups:irrep",
    "مميِّزات": "def:b3:point-groups:representation",
    "مميِّزاته": "def:b3:point-groups:representation",
    "مميِّزاتها": "def:b3:point-groups:representation",
    "أنماط عادية": "def:b3:group-theory-applied:normal-mode",
    "نمطًا عاديًا": "def:b3:group-theory-applied:normal-mode",
    # spectroscopy
    "نظائر جزيئية": "def:b3:rovibrational-spectroscopy:rotational-constant",
    "نظيرين جزيئيين": "def:b3:rovibrational-spectroscopy:rotational-constant",
    "ثابتا الدوران": "def:b3:rovibrational-spectroscopy:rotational-constant",
    "ثوابت الدوران": "def:b3:rovibrational-spectroscopy:rotational-constant",
    "اهتزازي إلكتروني": "def:b3:electronic-spectroscopy:vibronic",
    "زوايا قلبها": "def:b3:advanced-nmr:pulse",
    "دالة تجزئته القانونية": "def:b3:partition-functions:canonical",
    "حالات مجهرية": "def:b3:partition-functions:microstate",
    # kinetics
    "تفاعلات متسلسلة": "def:b3:complex-kinetics:chain",
    "حجم تنشيط": "def:b3:complex-mechanisms:activation-volume",
    "حجم تنشيطه": "def:b3:complex-mechanisms:activation-volume",
    "محكوم بالانتشار": "def:b3:rate-theories:diffusion",
    "محكومة بالانتشار": "def:b3:rate-theories:diffusion",
    # surfaces and colloids
    "متساويا حرارة لانغموير": "thm:b3:surfaces-catalysis:langmuir",
    "إنضاج أوستفالدي": "def:b3:colloids:ripening",
    # transition-metal and organometallic chemistry
    "حدود مجال الربائط": "def:b3:complex-spectra-magnetism:ligand-field-term",
    "مخططات تانابه--سوغانو": "def:b3:complex-spectra-magnetism:tanabe-sugano",
    "مخططا تانابه--سوغانو": "def:b3:complex-spectra-magnetism:tanabe-sugano",
    "متساوي الفصوص": "def:b3:organometallic-bonding:isolobal",
    "متساوية الفصوص": "def:b3:organometallic-bonding:isolobal",
    "متساويا الفصوص": "def:b3:organometallic-bonding:isolobal",
    "ميتالوسينات": "def:b3:organometallic-bonding:metallocene",
    "مركبات شطيرية": "def:b3:organometallic-bonding:metallocene",
    "كربونيلات فلزية": "def:b3:organometallic-bonding:carbonyl",
    "أحماض قاسية": "def:b3:bioinorganic:hsab",
    "أحماض لينة": "def:b3:bioinorganic:hsab",
    "استرخائيته": "def:b3:bioinorganic:contrast",
    # solids and materials
    "عيوب نقطية": "def:b3:solid-state:defects",
    "عيوب شوتكي": "def:b3:solid-state:defects",
    "عيوب فرنكل": "def:b3:solid-state:defects",
    "ثقوب": "def:b3:solid-state:carriers",
    "ثقبان": "def:b3:solid-state:carriers",
    "خزفيات": "def:b3:inorganic-materials:ceramic",
    "مكوِّنات الشبكة": "def:b3:inorganic-materials:glass",
    "مكوِّنات للشبكة": "def:b3:inorganic-materials:glass",
    "مطعِّمات": "def:b3:solid-state:doping",
    "أقطاب انتقائية للأيونات": "def:b3:electrode-kinetics:ise",
    "عوامل التسامح": "def:b3:inorganic-materials:perovskite",
    "الصول--الهلام": "def:b3:inorganic-materials:sol-gel",
    "جسيمات نانوية": "def:b3:inorganic-materials:nano",
    "مواد نانوية": "def:b3:inorganic-materials:nano",
    # organic chemistry
    "متساير الدوران": "def:b3:pericyclic:rotation-modes",
    "متعاكس الدوران": "def:b3:pericyclic:rotation-modes",
    "دوران متساير": "def:b3:pericyclic:rotation-modes",
    "دوران متعاكس": "def:b3:pericyclic:rotation-modes",
    "مرآويا الموضع": "def:b3:asymmetric-synthesis:topicity",
    "مرآويتا الموضع": "def:b3:asymmetric-synthesis:topicity",
    "لامرآويا الموضع": "def:b3:asymmetric-synthesis:topicity",
    "لامرآويتا الموضع": "def:b3:asymmetric-synthesis:topicity",
    "متكافئا الموضع": "def:b3:asymmetric-synthesis:topicity",
    "متكافئتا الموضع": "def:b3:asymmetric-synthesis:topicity",
    "تفاعلات انتقائية للمتماكبات المرآوية": "def:b3:asymmetric-synthesis:selective",
    "حلقات غير متجانسة": "def:b3:heterocycles:heterocycle",
    "روابط استراتيجية": "def:b3:total-synthesis:strategic-bond",
    "آلات جزيئية": "def:b3:supramolecular:machine",
    # green, environmental and laboratory chemistry
    "مواد أولية متجددة": "def:b3:green-industrial:feedstock",
    "عسره": "def:b3:environmental-toxicology:hardness",
    "مركبات حساسة للهواء": "def:b3:lab-techniques-3:air-sensitive",
    "مواد حساسة للهواء": "def:b3:lab-techniques-3:air-sensitive",
    "مكوِّن للبيروكسيدات": "def:b3:lab-techniques-3:peroxide",
    "مكوِّنان للبيروكسيدات": "def:b3:lab-techniques-3:peroxide",
}

DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# Multi-word patterns use \s+ between words: a phrase wrapped across a source
# line break must still be protected. A look-ahead anchored on a word that is
# itself a term must allow an optional wrapper: (?:\\omterm\{[^{}]*\}\{)?
EXTRA_PROTECT = [
    # an organic load (ch. 32) and an engine load (ch. 22 solutions), not
    # convection (ch. 15)
    r"[وفبكل]?(?:ال)?حمل(?=\s+(?:العضوي|المنخفض))",
    # the migration of a group (ch. 26-27), not ionic migration (ch. 15)
    r"[وفبكل]?هجرة(?=\s+(?:مجموعة|واحدة|ذرة))",
    # "alkali metals", not the alkalinity of a water (ch. 32)
    r"(?<=فلزات\s)القلوية",
    # the slipping plane of the double layer (ch. 17), not a glide plane
    r"[وفبكل]?مستوي\s+الانزلاق(?=\s+خلفها)",
    # electrons occupying orbitals (ch. 27), not a Boltzmann population
    r"[وفبكل]?إشغال(?=\s+المدار)",
    # the ozone hole (ch. 14), not a semiconductor hole
    r"[وفبكل]?(?:ال)?ثقب(?=\s+(?:الأوزون|في\s+السماء))",
    r"(?<=وهذا\s)ثقب",
    # chapter and section titles that carry a \texorpdfstring (nested
    # braces): the linker's heading mask stops at the first inner brace
    r"\\(?:chapter|section)\*?\{(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*\}",
    # chemfig settings and arrow labels: \arrow{->[label][label]}
    r"\\setchemfig\{[^{}]*\}",
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
    # pgfplots tick-label lists (every Book 1-2 edition needed this)
    r"[xy]ticklabels=\{[^{}]*\}",
]
