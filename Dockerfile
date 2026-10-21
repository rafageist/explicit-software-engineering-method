# Reproducible build environment for the ESEM manuscript.
# Mirrors .github/workflows/build-pdf.yml so that local and CI builds use the same toolchain.
#
#   docker build -t esem-build .
#   docker run --rm -v "$PWD":/work -w /work esem-build make check pdf
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_BREAK_SYSTEM_PACKAGES=1 \
    PUPPETEER_CACHE_DIR=/opt/puppeteer

RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates git make python3 python3-pip nodejs npm \
        pandoc wkhtmltopdf poppler-utils \
        texlive-xetex texlive-latex-recommended texlive-latex-extra \
        texlive-fonts-recommended texlive-lang-spanish lmodern \
        fonts-liberation libnss3 libatk1.0-0t64 libatk-bridge2.0-0t64 libcups2t64 \
        libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 \
        libgbm1 libasound2t64 libpango-1.0-0 libcairo2 \
    && rm -rf /var/lib/apt/lists/*

COPY scripts/requirements.txt /tmp/requirements.txt
RUN npm install -g @mermaid-js/mermaid-cli@11.4.2 \
    && python3 -m pip install --no-cache-dir -r /tmp/requirements.txt \
    && chmod -R a+rX /opt/puppeteer

RUN git config --system --add safe.directory /work
