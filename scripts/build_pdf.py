from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

AUTHOR = "Rafael Rodr\u00edguez Ram\u00edrez"

DOCS_ROOT = ROOT / "src"
COVER_ART_FALLBACK = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw=="

LANG_CONFIG = {
    "en": {
        "title": "Explicit Software Engineering Method",
        "subtitle": "A normative method for engineering accountability, traceability, and diagnosable failure",
        "cover_template": "00-cover.html",
        "cover_art": "cover.png",
        "contents_file": "00-contents.md",
        "index_file": "00-index.md",
        "index_title": "Index",
        "include_index": True,
        "header_tex": "pandoc-header.tex",
        "chapters": [
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
        ],
        "pdf_basename": "Explicit-Software-Engineering-Method",
    },
    "es": {
        "title": "M\u00e9todo Expl\u00edcito de Ingenier\u00eda de Software",
        "subtitle": (
            "Un m\u00e9todo normativo para la responsabilidad ingenieril, "
            "la trazabilidad y el fallo diagnosticable"
        ),
        "cover_template": "00-portada.html",
        "cover_art": "portada.png",
        "contents_file": "00-contenidos.md",
        "index_file": "00-indice.md",
        "index_title": "\u00cdndice",
        "include_index": False,
        "header_tex": "pandoc-header-es.tex",
        "chapters": [
            "prologo.md",
            "el-problema.md",
            "1-por-que-un-metodo.md",
            "2-de-software-a-producto.md",
            "3-reglas-normativas.md",
            "4-relacion-con-estandares.md",
            "5-ortogonalidad.md",
            "6-fallo-como-resultado-del-metodo.md",
            "7-formalizacion.md",
            "glosario.md",
        ],
        "pdf_basename": "Metodo-Explicito-de-Ingenieria-de-Software",
    },
}
SUPPORTED_LANGS = tuple(LANG_CONFIG.keys())

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


def generate_index(
    doc_root: Path,
    chapters: list[str],
    index_file: str,
    index_title: str,
) -> None:
    lines = [f"# {index_title}", ""]
    for chapter in chapters:
        path = doc_root / chapter
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
    (doc_root / index_file).write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


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
    template_path: Path,
    title: str,
    subtitle: str,
    version: str,
    generated_at: str,
    art_image: str,
    output_path: Path,
) -> None:
    template = template_path.read_text(encoding="utf-8")
    html = (
        template.replace("{{TITLE}}", title)
        .replace("{{VERSION}}", version)
        .replace("{{SUBTITLE}}", subtitle)
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


def resolve_cover_art(output_dir: Path, doc_root: Path, cover_art: str) -> str:
    candidates = [
        doc_root / cover_art,
        ROOT / cover_art,
        ROOT / "build" / cover_art,
        ROOT / "scripts" / "build" / cover_art,
    ]
    for source in candidates:
        if not source.is_file():
            continue
        destination = output_dir / cover_art
        if source.resolve() != destination.resolve():
            shutil.copyfile(source, destination)
        return cover_art
    return COVER_ART_FALLBACK


def language_root(lang: str) -> Path:
    return DOCS_ROOT / lang


def build_pdf_for_language(lang: str) -> None:
    config = LANG_CONFIG[lang]
    doc_root = language_root(lang)
    if not doc_root.is_dir():
        raise FileNotFoundError(f"Missing language directory: {doc_root}")
    generate_index(
        doc_root,
        config["chapters"],
        config["index_file"],
        config["index_title"],
    )

    output_root = ROOT / "build"
    output_root.mkdir(exist_ok=True)
    output_dir = output_root / lang
    output_dir.mkdir(exist_ok=True)
    raw_version = read_manifest_version()
    version = sanitize_version(raw_version)
    output_pdf = output_root / f"{config['pdf_basename']}_{version}.pdf"
    header_tex = ROOT / "scripts" / config.get("header_tex", "pandoc-header.tex")

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    env = os.environ.copy()
    mermaid_binary(env)
    art_image = resolve_cover_art(output_dir, doc_root, config["cover_art"])
    cover_html = output_dir / config["cover_template"]
    generate_cover_html(
        doc_root / config["cover_template"],
        config["title"],
        config["subtitle"],
        raw_version,
        generated_at,
        art_image,
        cover_html,
    )
    cover_pdf = output_dir / "00-cover.pdf"
    render_cover_pdf(cover_html, cover_pdf)
    cover_include = output_dir / "00-cover.tex"
    write_cover_include_tex(cover_include, cover_pdf)

    resource_path = os.pathsep.join([str(doc_root), str(ROOT)])
    cmd = [
        "pandoc",
        "--from",
        "markdown+tex_math_dollars+raw_tex",
        "--standalone",
        "--include-before-body",
        str(cover_include),
        "--pdf-engine=xelatex",
        "--metadata",
        f"title={config['title']}",
        "--metadata",
        f"author={AUTHOR}",
        "--metadata",
        f"date={generated_at}",
        "--include-in-header",
        str(header_tex),
        "--filter",
        "pandoc-mermaid",
        "--resource-path",
        resource_path,
        "-o",
        str(output_pdf),
    ]

    cmd.append(str(doc_root / config["contents_file"]))
    if config.get("include_index", True):
        cmd.append(str(doc_root / config["index_file"]))

    cmd += [str(doc_root / chapter) for chapter in config["chapters"]]

    subprocess.run(cmd, check=True, env=env)


def parse_args() -> list[str]:
    parser = argparse.ArgumentParser(description="Build PDFs for the method documentation.")
    parser.add_argument(
        "--lang",
        action="append",
        choices=SUPPORTED_LANGS,
        help="Language to build. Repeatable. Defaults to all supported languages.",
    )
    args = parser.parse_args()
    return args.lang or list(SUPPORTED_LANGS)


def main() -> None:
    for lang in parse_args():
        build_pdf_for_language(lang)


if __name__ == "__main__":
    main()
