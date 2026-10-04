"""Book 2 (University Year 1) -- ar (Arabic). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_ar.py.

Curated by the ar Book 2 agent (2026-10-04) from this edition's own harvest
(`--terms`) and the frequency and chapter-set censuses against the English
twin -- not translated from book2_en.py, not seeded from book1_ar.py (whose
plurals point at Book 1 labels).

Arabic homographs found by the harvest and the censuses, each handled below:
قوي/ضعيف (acid strength / any strong bond, weak interaction), جزيئية
(molecularity / the adjective "molecular": الصيغة الجزيئية، القوى بين
الجزيئية), تكافؤ (equivalence / valence: ثنائي التكافؤ), التناسب
(comproportionation / "بالتناسب مع", proportional to), الدورة (a period
of the table / a cycle: دورة الجير، تُعاد إلى الدورة), الفئة (a block /
a GHS hazard category: الفئة 2), الشبكة (a lattice / a platinum gauze),
المعايرة (a titration / calibrating a melting-point bench), الحجب
(screening, ch. 2 / NMR shielding, ch. 17), إماهة (hydration of an alkene,
ch. 25 / of ions, ch. 28), استوائي (a cyclohexane bond / the equatorial
positions of a trigonal bipyramid), خطر (hazard / the signal word «خطر» and
the GHS08 pictogram's name «خطر صحي»).
"""

STOP = set()
NO_CAPITAL = set()

# Arabic forms most plurals and duals by internal change or by endings that
# no tail rule reaches (lang_ar.py: WORD_TAIL is empty). The plural and dual
# forms this book uses for its most frequent multi-word terms are declared
# here, each pointing at the Book 2 target its singular already reaches; the
# article and the one-letter prefixes are added by HEAD.
EXTRA = {
    # lone and bonding pairs, Lewis and resonance structures, bonds
    "أزواج حرة": "def:b1:lewis-resonance-vsepr:lewis",
    "زوجًا حرًا": "def:b1:lewis-resonance-vsepr:lewis",
    "زوجان حران": "def:b1:lewis-resonance-vsepr:lewis",
    "زوجين حرين": "def:b1:lewis-resonance-vsepr:lewis",
    "أزواج رابطة": "def:b1:lewis-resonance-vsepr:lewis",
    "زوجان رابطان": "def:b1:lewis-resonance-vsepr:lewis",
    "زوجًا رابطًا": "def:b1:lewis-resonance-vsepr:lewis",
    "بنى لويس": "def:b1:lewis-resonance-vsepr:lewis",
    "بنيتي لويس": "def:b1:lewis-resonance-vsepr:lewis",
    "بنيتا لويس": "def:b1:lewis-resonance-vsepr:lewis",
    "روابط تساهمية": "def:b1:lewis-resonance-vsepr:lewis",
    "بنى رنين": "def:b1:lewis-resonance-vsepr:resonance",
    "بنيتا رنين": "def:b1:lewis-resonance-vsepr:resonance",
    "بنيتي رنين": "def:b1:lewis-resonance-vsepr:resonance",
    "شحنات شكلية": "def:b1:lewis-resonance-vsepr:formal-charge",
    "عزوم ثنائي القطب": "def:b1:lewis-resonance-vsepr:dipole",
    "جزيئات قطبية": "def:b1:lewis-resonance-vsepr:dipole",
    "روابط هيدروجينية": "def:b1:intermolecular-forces-solvents:hbond",
    "رابطتان هيدروجينيتان": "def:b1:intermolecular-forces-solvents:hbond",
    "رابطتين هيدروجينيتين": "def:b1:intermolecular-forces-solvents:hbond",
    "مذيبات قطبية": "def:b1:intermolecular-forces-solvents:solvent-classes",
    "مذيبات بروتونية": "def:b1:intermolecular-forces-solvents:solvent-classes",
    "مذيبات لابروتونية": "def:b1:intermolecular-forces-solvents:solvent-classes",
    # crystals
    "مواقع بينية": "def:b1:crystals-metals:site",
    "مواقع ثمانية الأوجه": "def:b1:crystals-metals:site",
    "مواقع رباعية الأوجه": "def:b1:crystals-metals:site",
    # equilibrium, kinetics
    "كسور مولية": "def:b1:extent-q-and-k:composition",
    "كسور كتلية": "def:b1:extent-q-and-k:composition",
    "ضغوط جزئية": "def:b1:extent-q-and-k:composition",
    "تراكيز مولية": "def:b1:extent-q-and-k:composition",
    "متغيرات مكثفة": "def:b1:extent-q-and-k:variables",
    "متغيرات ممتدة": "def:b1:extent-q-and-k:variables",
    "متغيرين ممتدين": "def:b1:extent-q-and-k:variables",
    "متغيرين مكثفين": "def:b1:extent-q-and-k:variables",
    "حفّاز": "def:b1:elementary-steps:catalyst",
    "حفّازًا": "def:b1:elementary-steps:catalyst",
    "حفّازات": "def:b1:elementary-steps:catalyst",
    "خطوات أولية": "def:b1:elementary-steps:elementary-step",
    "طاقات التنشيط": "def:b1:rate-laws:activation-energy",
    # acids, redox, complexes, precipitation
    "أحماض قوية": "def:b1:predominant-reaction:strong-acid",
    "أحماض ضعيفة": "def:b1:predominant-reaction:strong-acid",
    "قواعد قوية": "def:b1:predominant-reaction:strong-acid",
    "قواعد ضعيفة": "def:b1:predominant-reaction:strong-acid",
    "حمضًا قويًا": "def:b1:predominant-reaction:strong-acid",
    "حمضًا ضعيفًا": "def:b1:predominant-reaction:strong-acid",
    "مخططات الغلبة": "def:b1:predominant-reaction:predominance",
    "مخططات التوزيع": "def:b1:predominant-reaction:predominance",
    "أمفوليتات": "def:b1:predominant-reaction:ampholyte",
    "أعداد أكسدة": "def:b1:nernst:oxidation-number",
    "جهود معيارية": "def:b1:nernst:electrode-potential",
    "جهود الأقطاب": "def:b1:nernst:electrode-potential",
    "معقدات": "def:b1:complexation:complex",
    "جداءات الذوبانية": "def:b1:precipitation:solubility-product",
    # organic
    "متماكب فراغي": "def:b1:stereochemistry-in-depth:isomers",
    "متماكبًا فراغيًا": "def:b1:stereochemistry-in-depth:isomers",
    "متماكبان فراغيان": "def:b1:stereochemistry-in-depth:isomers",
    "متماكبين فراغيين": "def:b1:stereochemistry-in-depth:isomers",
    "متماكب بنيوي": "def:b1:stereochemistry-in-depth:isomers",
    "متماكبان بنيويان": "def:b1:stereochemistry-in-depth:isomers",
    "متماكبين بنيويين": "def:b1:stereochemistry-in-depth:isomers",
    "متماكب مرآوي": "def:b1:stereochemistry-in-depth:enantiomers",
    "متماكبًا مرآويًا": "def:b1:stereochemistry-in-depth:enantiomers",
    "متماكبان مرآويان": "def:b1:stereochemistry-in-depth:enantiomers",
    "متماكبين مرآويين": "def:b1:stereochemistry-in-depth:enantiomers",
    "متماكب لامرآوي": "def:b1:stereochemistry-in-depth:enantiomers",
    "متماكبًا لامرآويًا": "def:b1:stereochemistry-in-depth:enantiomers",
    "متماكبان لامرآويان": "def:b1:stereochemistry-in-depth:enantiomers",
    "متماكبين لامرآويين": "def:b1:stereochemistry-in-depth:enantiomers",
    "أسهم منحنية": "def:b1:electronic-effects:curly-arrow",
    "سهمًا منحنيًا": "def:b1:electronic-effects:curly-arrow",
    "محبات للنواة": "def:b1:electronic-effects:nucleophile",
    "محبًا للنواة": "def:b1:electronic-effects:nucleophile",
    "محبات للإلكترونات": "def:b1:electronic-effects:nucleophile",
    "محبًا للإلكترونات": "def:b1:electronic-effects:nucleophile",
    "مجموعات مغادرة": "def:b1:electronic-effects:nucleophile",
    "كاتيونات كربونية": "def:b1:electronic-effects:intermediates",
    "كاتيونًا كربونيًا": "def:b1:electronic-effects:intermediates",
    "أنيونات كربونية": "def:b1:electronic-effects:intermediates",
    "جذور حرة": "def:b1:electronic-effects:intermediates",
    "وسائط تفاعلية": "def:b1:electronic-effects:intermediates",
    "ألكوكسيدات": "def:b1:alcohol-activation:alkoxide",
    "إسترات السلفونات": "def:b1:alcohol-activation:sulfonate",
    "أسيتالات": "def:b1:acetals-protection:hemiacetal",
    "أنصاف الأسيتالات": "def:b1:acetals-protection:hemiacetal",
    "مجموعات حماية": "def:b1:acetals-protection:protecting-group",
    "مستويات أكسدة": "def:b1:organic-redox:oxidation-level",
    "ثوابت الاقتران": "def:b1:structure-spectroscopy:coupling",
    "متعددات الخطوط": "def:b1:structure-spectroscopy:coupling",
    "تكاملات": "def:b1:structure-spectroscopy:integration",
    # inorganic, lab
    "أكاسيد حمضية": "def:b1:s-block:oxide-character",
    "أكاسيد قاعدية": "def:b1:s-block:oxide-character",
    "أكاسيد مذبذبة": "def:b1:s-block:oxide-character",
    "هيدريدات": "def:b1:s-block:hydride",
    "أخطار": "def:b1:lab-techniques-1:hazard",
    "عدم يقين": "def:b1:lab-techniques-1:uncertainty",
    # indefinite construct-state (idafa) forms: the harvest only has the
    # definite "عدد الأكسدة", "قانون السرعة", ...
    "عدد أكسدة": "def:b1:nernst:oxidation-number",
    "قانون سرعة": "def:b1:rate-laws:order",
    "ثابت سرعة": "def:b1:rate-laws:order",
    "قوانين السرعة": "def:b1:rate-laws:order",
    "قوانين سرعة": "def:b1:rate-laws:order",
    "قانوني سرعة": "def:b1:rate-laws:order",
    "ثوابت السرعة": "def:b1:rate-laws:order",
    "ثوابت سرعة": "def:b1:rate-laws:order",
    "ثابتي السرعة": "def:b1:rate-laws:order",
    "إلكترونات تكافؤ": "def:b1:quantum-numbers:configuration",
    "إلكترون تكافؤ": "def:b1:quantum-numbers:configuration",
    "عزم ثنائي قطب": "def:b1:lewis-resonance-vsepr:dipole",
    "ثنائي قطب رابطة": "def:b1:lewis-resonance-vsepr:dipole",
    "طاقة تنشيط": "def:b1:rate-laws:activation-energy",
    "عدم يقين معياري": "def:b1:lab-techniques-1:uncertainty",
    "نقطة نهاية": "def:b1:titration-methods:titration",
    "نقطة تكافؤ": "def:b1:titration-methods:titration",
    "مستويات طاقة": "def:b1:quantum-numbers:energy-level",
    "طاقة تأين أولى": "def:b1:periodicity:ionisation-energy",
    "عدم تناسب": "def:b1:e-ph-diagrams:disproportionation",
    "إعادة تبلور": "def:b1:lab-techniques-1:recrystallisation",
    "مخطط غلبة": "def:b1:predominant-reaction:predominance",
    "كلمة تنبيه": "def:b1:lab-techniques-1:ghs",
    "زمن نصف تفاعل": "def:b1:rate-laws:half-life",
    "جهد قطب": "def:b1:nernst:electrode-potential",
    "جهد خلية": "def:b1:nernst:cell",
    "تشكّلان منحرفان": "def:b1:stereochemistry-in-depth:conformations",
    "آلية تفاعل": "def:b1:elementary-steps:elementary-step",
    "هيدريدات فلزية": "def:b1:s-block:hydride",
    "نزع ماء": "def:b1:alcohol-activation:dehydration",
    "منطقة تخميل": "def:b1:e-ph-diagrams:corrosion-domains",
    "مانح هيدريد": "def:b1:organic-redox:hydride-donor",
    "سرعة تفاعل": "def:b1:rate-laws:rate",
    "درجة تفكك": "def:b1:predominant-reaction:dissociation",
    "خارج تفاعل": "def:b1:extent-q-and-k:quotient",
    "إستر سلفونات": "def:b1:alcohol-activation:sulfonate",
    "مكثفة": "def:b1:extent-q-and-k:variables",
    "ممتدة": "def:b1:extent-q-and-k:variables",
    # single forms the census found missing against English
    "أحماض متعددة البروتونات": "def:b1:predominant-reaction:polyprotic",
    "تأثير الأيون المشترك": "def:b1:precipitation:common-ion",
    "متآصلات": "def:b1:crystals-metals:allotropy",
    "هيدروكسيدات مذبذبة": "def:b1:precipitation:amphoteric-hydroxide",
    "معامل توزيعه": "def:b1:lab-techniques-1:partition-coefficient",
}

DROP = {
    # bare adjectives: "حمض قوي" / "قاعدة ضعيفة" keep their links, but "رابطة
    # قوية", "تآثرات ضعيفة", "قاعدة قوية جدًا" must not point at acid strength.
    # STOP would fall through to the chapter-local map.
    "قوي", "قوية", "قويًا", "ضعيف", "ضعيفة", "ضعيفًا",
    # the adjective "molecular" (الصيغة الجزيئية، بين الجزيئية) swamps the
    # molecularity of ch. 9; "جزيئيتها" keeps the link.
    "جزيئية",
}
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across
# a source line break must still be protected. An optional
# (?:\\omterm\{[^{}]*\}\{)? lets a pattern see through a link already placed
# on the previous word.
EXTRA_PROTECT = [
    # "proportional to" (بالتناسب مع), not the comproportionation of ch. 14
    r"بالتناسب",
    r"التناسب(?=\s+مع)",
    # a cycle, not a period of the table: the lime cycle (ch. 26), "recycled"
    r"دورة(?=\s+الجير)",
    r"(?<=إلى\s)الدورة",
    r"(?<=و)الدورة(?=\s+بمجملها)",
    r"الدورة(?=\s+بمجملها)",
    # a GHS hazard category (الفئة 2), not a block of the table
    r"الفئة(?=\s+\d)",
    # a platinum--rhodium gauze (ch. 27), not a crystal lattice
    r"شبكة(?=\s+(?:من\s+)?(?:ال)?بلاتين)",
    # calibrating a bench or a certificate, not a titration (ch. 29)
    r"معايرة(?=\s+(?:\\omterm\{[^{}]*\}\{)?المنصة)",
    r"(?<=شهادة\s)معايرة",
    r"(?<=ب)معايرة(?=\s+(?:\\omterm\{[^{}]*\}\{)?المنصة)",
    # NMR shielding (ch. 17), not the screening of ch. 2
    r"(?<=إزالة\s)الحجب",
    r"(?<=إزالةً\s)للحجب",
    r"(?<=أُزيل\s)الحجب",
    r"(?<=أزال\s)الحجب",
    r"(?<=يزيل\s)الحجب",
    r"(?<=تزيل\s)الحجب",
    r"(?<=معامل\s)الحجب",
    # hydration of ions (ch. 28), not of an alkene
    r"إماهة(?=\s+(?:\\omterm\{[^{}]*\}\{)?أيونات)",
    # VSEPR positions of a trigonal bipyramid (ch. 28), not cyclohexane bonds
    r"(?<=المواضع\s)الاستوائية",
    # the signal word (ch. 29) and the GHS08 pictogram's name
    r"(?<=\\emph\{)خطر(?=\})",
    r"خطر(?=\s+صحي)",
    # a catalytic cycle (ch. 9), not a period of the table
    r"دورة(?=\s+حفزية)",
    # a covalent NETWORK of tetrahedra (ch. 27), not the defined lattice
    r"شبكة(?=\s+تساهمية)",
    r"(?<=و)شبكة(?=\s+\\ce)",
    # "a complicated structure", not a complex (ch. 13)
    r"معقد(?=\s+البنية)",
    # "measures the progress of the reaction" (ch. 23), not the extent
    r"(?<=يقيس\s)تقدم",
    # the GHS03 pictogram caption "oxidising", not the redox couple
    r"(?<=\\footnotesize\s)مؤكسد",
    # NMR deshielding: "removes the shielding from" (ch. 17)
    r"الحجب(?=\s+عن)",
    # "more/less electronegative" and "an electronegative group": the
    # adjective, not the electronegativity of ch. 2 (as in English)
    r"(?<=أكثر\s)كهرسلبية",
    r"(?<=الأكثر\s)كهرسلبية",
    r"(?<=أقل\s)كهرسلبية",
    r"(?<=الأقل\s)كهرسلبية",
    r"(?<=أضعف\s)كهرسلبية",
    r"(?<=العناصر\s)كهرسلبية",
    r"(?<=مجموعة\s)كهرسلبية",
    r"(?<=ذرة\s)كهرسلبية",
    r"(?<=ذرات\s)كهرسلبية",
    r"(?<=الذرات\s)الكهرسلبية",
    # valence, not the equivalence of a titration (ch. 15): ثنائي التكافؤ،
    # طبقة التكافؤ، عدم تكافؤ
    r"(?<=طبقة\s)التكافؤ",
    r"(?<=طبقات\s)التكافؤ",
    r"(?<=لطبقات\s)التكافؤ",
    r"(?<=طبقات\s)تكافؤ",
    r"(?<=ثنائي\s)التكافؤ",
    r"(?<=ثلاثي\s)التكافؤ",
    r"(?<=أحادي\s)التكافؤ",
    r"(?<=الثنائي\s)التكافؤ",
    r"(?<=الثلاثي\s)التكافؤ",
    r"(?<=للثنائي\s)التكافؤ",
    r"(?<=توزيع\s)التكافؤ",
    r"(?<=عدم\s)تكافؤ",
    # chapter and section titles that carry a \texorpdfstring (nested
    # braces): the linker's own heading mask stops at the first inner brace,
    # and a link in a title reaches the running header and the TOC
    r"\\(?:chapter|section)\*?\{(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*\}",
    # key names inside the periodic-table macro's options
    r"\\omperiodictable\[[^\]]*\]",
    # chemfig arrow labels: \arrow{->[label][label]}
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
]
