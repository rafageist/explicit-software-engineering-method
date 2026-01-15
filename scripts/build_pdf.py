from __future__ import annotations

import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TITLE = "Explicit Software Engineering Method"
AUTHOR = "Rafael Rodríguez Ramírez"

INDEX_FILE = "00-index.md"

CHAPTERS = [
    "prologue.md",
    "1-why-a-method.md",
    "2-from-software-to-product.md",
    "3-normative-rules.md",
    "4-relation-with-standards.md",
    "5-orthogonality.md",
    "6-failure-as-a-method-outcome.md",
    "7-formalization.md",
]

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


def build_pdf() -> None:
    output_dir = ROOT / "build"
    output_dir.mkdir(exist_ok=True)
    version = sanitize_version(read_manifest_version())
    output_pdf = output_dir / f"Explicit-Software-Engineering-Method_{version}.pdf"
    header_tex = ROOT / "scripts" / "pandoc-header.tex"

    today = date.today().isoformat()
    cmd = [
        "pandoc",
        "--from",
        "gfm+tex_math_dollars",
        "--standalone",
        "--toc",
        "--toc-depth=3",
        "--pdf-engine=xelatex",
        "--metadata",
        f"title={TITLE}",
        "--metadata",
        f"author={AUTHOR}",
        "--metadata",
        f"date={today}",
        "--include-in-header",
        str(header_tex),
        "--filter",
        "pandoc-mermaid",
        "--resource-path",
        str(ROOT),
        "-o",
        str(output_pdf),
    ] + [str(ROOT / chapter) for chapter in CHAPTERS]

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
