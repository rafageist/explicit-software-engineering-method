from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TITLE = "Explicit Software Engineering Method"
AUTHOR = "Rafael Rodríguez Ramírez"
SUBTITLE = "A normative method for engineering accountability, traceability, and diagnosable failure"

COVER_TEMPLATE = "00-cover.html"
COVER_ART = "cover.png"
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
PDF_CHAPTERS = [CONTENTS_FILE] + CHAPTERS

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


def require_command(command: str) -> None:
    if shutil.which(command) is None:
        raise FileNotFoundError(f"Required command not found: {command}")


def mermaid_binary(env: dict[str, str]) -> str:
    if "MERMAID_BIN" in env:
        return env["MERMAID_BIN"]
    wrapper = ROOT / "scripts" / ("mmdc-wrapper.cmd" if sys.platform.startswith("win") else "mmdc-wrapper.sh")
    env["MERMAID_BIN"] = str(wrapper)
    return env["MERMAID_BIN"]


def generate_cover_html(
    version: str,
    generated_at: str,
    art_image: str,
    output_path: Path,
) -> None:
    template = (ROOT / COVER_TEMPLATE).read_text(encoding="utf-8")
    html = (
        template.replace("{{TITLE}}", TITLE)
        .replace("{{VERSION}}", version)
        .replace("{{SUBTITLE}}", SUBTITLE)
        .replace("{{AUTHOR}}", AUTHOR)
        .replace("{{GENERATED_AT}}", generated_at)
        .replace("{{ART_IMAGE}}", art_image)
    )
    output_path.write_text(html, encoding="utf-8")


def render_cover_pdf(html_path: Path, output_pdf: Path) -> None:
    require_command("wkhtmltopdf")
    subprocess.run(
        [
            "wkhtmltopdf",
            "--page-size",
            "A4",
            "--margin-top",
            "0",
            "--margin-right",
            "0",
            "--margin-bottom",
            "0",
            "--margin-left",
            "0",
            "--enable-local-file-access",
            str(html_path),
            str(output_pdf),
        ],
        check=True,
    )


def write_cover_include_tex(output_path: Path, cover_pdf: Path) -> None:
    output_path.write_text(
        f"\\includepdf[pages=1,pagecommand={{\\thispagestyle{{empty}}}}]{{{cover_pdf.as_posix()}}}\n",
        encoding="utf-8",
    )


def resolve_cover_art(output_dir: Path) -> str:
    source = ROOT / COVER_ART
    if not source.is_file():
        return "none"
    destination = output_dir / COVER_ART
    if source.resolve() != destination.resolve():
        shutil.copyfile(source, destination)
    return f"url('{COVER_ART}')"


def build_pdf() -> None:
    output_dir = ROOT / "build"
    output_dir.mkdir(exist_ok=True)
    raw_version = read_manifest_version()
    version = sanitize_version(raw_version)
    output_pdf = output_dir / f"Explicit-Software-Engineering-Method_{version}.pdf"
    header_tex = ROOT / "scripts" / "pandoc-header.tex"

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    env = os.environ.copy()
    mermaid_binary(env)
    art_image = resolve_cover_art(output_dir)
    cover_html = output_dir / "00-cover.html"
    generate_cover_html(raw_version, generated_at, art_image, cover_html)
    cover_pdf = output_dir / "00-cover.pdf"
    render_cover_pdf(cover_html, cover_pdf)
    cover_include = output_dir / "00-cover.tex"
    write_cover_include_tex(cover_include, cover_pdf)
    cmd = [
        "pandoc",
        "--from",
        "markdown+tex_math_dollars+raw_tex",
        "--standalone",
        "--include-before-body",
        str(cover_include),
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

    subprocess.run(cmd, check=True, env=env)


def main() -> None:
    generate_index()
    build_pdf()


if __name__ == "__main__":
    main()
