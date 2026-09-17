.PHONY: all fetch merge docs shortcuts sign verify release clean

all: fetch merge docs shortcuts verify

fetch:
	python3 scripts/fetch_sources.py

merge:
	python3 scripts/merge.py

docs:
	python3 scripts/generate.py

shortcuts:
	python3 scripts/build_shortcut.py

sign:
	./scripts/sign_all.sh

verify:
	python3 scripts/verify_shortcut.py

# Example: make release VERSION=v1.0.0
release:
	./scripts/release.sh $(VERSION)

clean:
	rm -rf raw __pycache__ scripts/__pycache__ sign.log
