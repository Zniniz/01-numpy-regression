PY ?= python3

.PHONY: run test

run:
	$(PY) src/main.py

test:
	$(PY) -m pytest -q tests
