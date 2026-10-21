PYTHON ?= python3
IMAGE ?= esem-build

.PHONY: check index pdf tex docker-image docker-pdf clean

# Consistency checks for the bilingual manuscript (no external tools needed).
check:
	$(PYTHON) scripts/check_manuscript.py

# Regenerate src/*/00-index.md and src/es/00-indice.md from chapter headings.
index:
	$(PYTHON) scripts/build_pdf.py --write-index

# Build both PDFs (requires pandoc, xelatex, wkhtmltopdf, Mermaid CLI).
pdf:
	$(PYTHON) scripts/build_pdf.py

# Build LaTeX sources only (requires pandoc).
tex:
	$(PYTHON) scripts/build_pdf.py --format tex

# Reproducible build in the same toolchain as CI.
docker-image:
	docker build -t $(IMAGE) .

docker-pdf: docker-image
	docker run --rm -v "$(CURDIR)":/work -w /work -e SOURCE_DATE_EPOCH $(IMAGE) make check pdf

clean:
	rm -rf build mermaid-images
