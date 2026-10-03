.PHONY: all clean distclean venv test figdata gates

PY := .venv/bin/python

all:
	latexmk

clean:
	latexmk -c

distclean:
	latexmk -C
	rm -rf build

# The Python side: tools/chem.py (balance gate, molar masses) and the
# figure-data scripts. System python3 has no numpy, and this machine's
# python3 has no ensurepip, hence the bootstrap through the user's pip.
venv:
	python3 -m venv --without-pip .venv
	pip --python $(PY) install -r requirements.txt

# Y=<year> scopes test and figdata to one year (what a book writer runs while
# another book is being written in the same tree): make test Y=bachelor-1
test:
	$(PY) -m pytest -q $(if $(Y),tests/test_chem.py tests/test_gates.py $(wildcard tests/$(Y)),tests)

# Regenerate every figure table under figdata/out/ -- must leave no diff.
figdata:
	@d=figdata/$(Y); [ -d "$$d" ] || { echo "  (no $$d)"; exit 0; }; \
	for f in $$(find "$$d" -name '*.py' ! -name 'test_*' ! -name '_*' | sort); do \
	  echo "  $$f"; $(PY) $$f || exit 1; done

# Every chapter-level gate over every year (tools/gates.sh <year> for one).
gates:
	@for y in $$(ls parts); do bash tools/gates.sh $$y || exit 1; done
