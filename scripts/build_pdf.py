from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHAPTERS = [
    "00-index.md",
    "1-why-a-method.md",
    "2-from-software-to-product.md",
    "3-normative-rules.md",
    "4-relation-with-standards.md",
    "5-orthogonality.md",
    "6-failure-as-a-method-outcome.md",
    "7-formalization.md",
]

HEADING_RE = re.compile(r"^(#{1,3})\s+(.*)$")


def generate_index() -> None:
    lines = ["# Index", ""]
    for chapter in CHAPTERS[1:]:
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
    (ROOT / "00-index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def build_pdf() -> None:
    output_dir = ROOT / "build"
    output_dir.mkdir(exist_ok=True)
    output_pdf = output_dir / "Explicit-Software-Engineering-Method.pdf"
    header_tex = ROOT / "scripts" / "pandoc-header.tex"

    cmd = [
        "pandoc",
        "--from",
        "gfm",
        "--standalone",
        "--toc",
        "--toc-depth=3",
        "--pdf-engine=xelatex",
        "--metadata",
        "title=Explicit Software Engineering Method",
        "--include-in-header",
        str(header_tex),
        "--filter",
        "mermaid-filter",
        "--resource-path",
        str(ROOT),
        "-o",
        str(output_pdf),
    ] + [str(ROOT / chapter) for chapter in CHAPTERS]

    env = os.environ.copy()
    env.setdefault("MERMAID_FILTER_FORMAT", "png")
    subprocess.run(cmd, check=True, env=env)


def main() -> None:
    generate_index()
    build_pdf()


if __name__ == "__main__":
    main()
