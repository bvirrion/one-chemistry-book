"""Book 1 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-4_ZH.md) before the translation existed, from the
English and French configs' choices; refined at the book's close against the link census (pilot_translation/census.py).
Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han text, so a word that is also part of a common
compound or an everyday verb must be stopped or dropped here. One-character terms are never linked.
"""

# result names are never terms (the French NOT_A_TERM, in Chinese)
NOT_A_TERM = ("定理", "引理", "不等式", "公式", "判据", "准则", "原理", "恒等式", "法则", "定律", "悖论", "问题")

STOP = {
    # as book1_en.py: everyday words defined early and used in their everyday sense after
    # (solution, material, object, product, family, period, addition, substitution, capacity, symbol)
    "溶液", "材料", "物体", "符号", "生成物", "产物", "周期", "加成", "取代", "容量",
    # words every chemistry sentence carries, which English links only as a phrase
    # (化学式: English links "subscript"; 元素: "chemical element" 3 times; 吸收带: "fingerprint region")
    "化学式", "元素",
}
DROP = {
    # 氧化/还原 sit inside compound names (二氧化碳, 氧化铜): 80 wrong links in the first pass
    "氧化", "还原",
    # 吸收带 in the infrared chapter: 77 links against English's 3 (English links only "fingerprint region")
    "吸收带",
}
INDEX_CJK = True    # index-only keys are terms too (harvest.py, physics zh Book 3)
EXTRA = {"Z 异构体": "def:g12:stereochemistry:z-e", "E 异构体": "def:g12:stereochemistry:z-e"}          # manual {term: label}, added at the book's close (index-only keys have no space in Chinese)
NO_CAPITAL = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 20
EXTRA_PROTECT = []
