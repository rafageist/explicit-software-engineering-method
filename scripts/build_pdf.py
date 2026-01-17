from __future__ import annotations

import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TITLE = "Explicit Software Engineering Method"
AUTHOR = "Rafael Rodríguez Ramírez"
SUBTITLE = "A normative method for engineering accountability, traceability, and diagnosable failure"

COVER_FILE = "00-cover.md"
CONTENTS_FILE = "00-contents.md"
INDEX_FILE = "00-index.md"

CHAPTERS = [
    "prologue.md",
    "the-problem.md",
    "1-why-a-method.md",
    "2-from-software-to-product.md",
    "3-normative-rules.md",
    "4-relation-with-standards.md",
    "5-orthogonality.md",
    "6-failure-as-a-method-outcome.md",
    "7-formalization.md",
    "glossary.md",
]
PDF_CHAPTERS = [COVER_FILE, CONTENTS_FILE] + CHAPTERS

HEADING_RE = re.compile(r"^(#{1,3})\s+(.*)$")


def read_manifest_version() -> str:
    manifest_path = ROOT / "manifest.yaml"
    if not manifest_path.is_file():
        raise FileNotFoundError("manifest.yaml is missing. Add a version field.")

    for raw_line in manifest_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.lower().startswith("version:"):
            value = line.split(":", 1)[1].strip()
            if (value.startswith('"') and value.endswith('"')) or (
                value.startswith("'") and value.endswith("'")
            ):
                value = value[1:-1]
            if value:
                return value
    raise ValueError("manifest.yaml is missing a valid version field.")


def sanitize_version(version: str) -> str:
    return "".join(ch if (ch.isalnum() or ch in "._-") else "_" for ch in version)


def generate_index() -> None:
    lines = ["# Index", ""]
    for chapter in CHAPTERS:
        path = ROOT / chapter
        text = path.read_text(encoding="utf-8")
        for line in text.splitlines():
            line = line.lstrip("\ufeff")
            match = HEADING_RE.match(line)
            if not match:
                continue
            level = len(match.group(1))
            title = match.group(2).strip()
            indent = "  " * (level - 1)
            if level == 1:
                lines.append(f"- [{title}]({chapter})")
            else:
                lines.append(f"{indent}- {title}")
        lines.append("")
    (ROOT / INDEX_FILE).write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def generate_cover(version: str, generated_at: str) -> None:
    lines = [
        r"\begin{center}",
        r"\vspace*{0.18\textheight}",
        f"{{\\LARGE\\bfseries {TITLE}\\par}}",
        r"\vspace{0.6cm}",
        f"{{\\Large\\bfseries Version {version}\\par}}",
        r"\vspace{0.4cm}",
        f"{{\\large {SUBTITLE}\\par}}",
        r"\vspace{1cm}",
        "",
        "```mermaid",
        "flowchart TB",
        "    I[Intent] --> D[Decision]",
        "    D --> A[Artifact]",
        "    A --> V[Validation]",
        "    V -.-> I",
        "```",
        "",
        r"\vspace{1cm}",
        f"{{\\large {AUTHOR}\\par}}",
        r"\vspace{0.3cm}",
        f"{{\\small Generated: {generated_at}\\par}}",
        r"\end{center}",
        r"\newpage",
        "",
    ]
    (ROOT / COVER_FILE).write_text("\n".join(lines), encoding="utf-8")


def build_pdf() -> None:
    output_dir = ROOT / "build"
    output_dir.mkdir(exist_ok=True)
    raw_version = read_manifest_version()
    version = sanitize_version(raw_version)
    output_pdf = output_dir / f"Explicit-Software-Engineering-Method_{version}.pdf"
    header_tex = ROOT / "scripts" / "pandoc-header.tex"

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    generate_cover(raw_version, generated_at)
    cmd = [
        "pandoc",
        "--from",
        "gfm+tex_math_dollars+raw_tex",
        "--standalone",
        "--pdf-engine=xelatex",
        "--metadata",
        f"title={TITLE}",
        "--metadata",
        f"author={AUTHOR}",
        "--metadata",
        f"date={generated_at}",
        "--include-in-header",
        str(header_tex),
        "--filter",
        "pandoc-mermaid",
        "--resource-path",
        str(ROOT),
        "-o",
        str(output_pdf),
    ] + [str(ROOT / chapter) for chapter in PDF_CHAPTERS]

    env = os.environ.copy()
    if "MERMAID_BIN" not in env:
        wrapper = (
            ROOT / "scripts" / ("mmdc-wrapper.cmd" if sys.platform.startswith("win") else "mmdc-wrapper.sh")
        )
        env["MERMAID_BIN"] = str(wrapper)
    subprocess.run(cmd, check=True, env=env)


def main() -> None:
    generate_index()
    build_pdf()


if __name__ == "__main__":
    main()
