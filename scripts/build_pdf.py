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

AUTHOR = "Rafael Rodríguez Ramírez"

DOCS_ROOT = ROOT / "src"
COVER_ART_FALLBACK = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw=="

LANG_CONFIG = {
    "en": {
        "lang": "en-US",
        "title": "Explicit Software Engineering Method",
        "subtitle": "A normative method for engineering accountability, traceability, and diagnosable failure",
        "cover_template": "00-cover.html",
        "cover_art": "cover.png",
        "contents_file": "00-contents.md",
        "index_file": "00-index.md",
        "index_title": "Index",
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
            "8-application-and-evaluation.md",
            "9-worked-examples.md",
            "10-engineering-context.md",
            "references.md",
            "glossary.md",
        ],
        "pdf_basename": "Explicit-Software-Engineering-Method",
    },
    "es": {
        "lang": "es",
        "title": "Método Explícito de Ingeniería de Software",
        "subtitle": (
            "Un método normativo para la responsabilidad ingenieril, "
            "la trazabilidad y el fallo diagnosticable"
        ),
        "cover_template": "00-portada.html",
        "cover_art": "portada.png",
        "contents_file": "00-contenidos.md",
        "index_file": "00-indice.md",
        "index_title": "Índice",
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
            "8-aplicacion-y-evaluacion.md",
            "9-ejemplos-desarrollados.md",
            "10-contexto-de-ingenieria.md",
            "referencias.md",
            "glosario.md",
        ],
        "pdf_basename": "Metodo-Explicito-de-Ingenieria-de-Software",
    },
}
SUPPORTED_LANGS = tuple(LANG_CONFIG.keys())

HEADING_RE = re.compile(r"^(#{1,3})\s+(.*)$")
FENCE_RE = re.compile(r"^(```|~~~)")
MISSING_CHAR_RE = re.compile(r"Missing character", re.IGNORECASE)


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


def build_timestamp() -> datetime:
    """Use SOURCE_DATE_EPOCH, else the commit time of HEAD, else the current time."""
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if not epoch:
        try:
            epoch = subprocess.run(
                ["git", "log", "-1", "--format=%ct"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
        except (OSError, subprocess.CalledProcessError):
            epoch = ""
    if epoch:
        return datetime.fromtimestamp(int(epoch), tz=timezone.utc)
    return datetime.now(timezone.utc)


def render_index(doc_root: Path, chapters: list[str], index_title: str) -> str:
    lines = [f"# {index_title}", ""]
    for chapter in chapters:
        text = (doc_root / chapter).read_text(encoding="utf-8")
        in_fence = False
        for line in text.splitlines():
            if FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
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
    return "\n".join(lines).rstrip() + "\n"


def sync_index(lang: str, write: bool) -> bool:
    """Return True if the committed index matches the chapters; optionally rewrite it."""
    config = LANG_CONFIG[lang]
    doc_root = language_root(lang)
    expected = render_index(doc_root, config["chapters"], config["index_title"])
    index_path = doc_root / config["index_file"]
    current = index_path.read_text(encoding="utf-8") if index_path.is_file() else ""
    if current == expected:
        return True
    if write:
        index_path.write_text(expected, encoding="utf-8")
        return True
    return False


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


def run_pandoc(cmd: list[str], env: dict[str, str]) -> None:
    """Run pandoc, echo its diagnostics, and fail on glyphs missing from the PDF fonts."""
    result = subprocess.run(cmd, env=env, capture_output=True, text=True)
    sys.stderr.write(result.stderr)
    if result.returncode != 0:
        raise subprocess.CalledProcessError(result.returncode, cmd, result.stdout, result.stderr)
    missing = [line for line in result.stderr.splitlines() if MISSING_CHAR_RE.search(line)]
    if missing:
        raise RuntimeError(
            "Characters missing from the PDF fonts:\n" + "\n".join(sorted(set(missing)))
        )


def build_for_language(lang: str, output_format: str) -> None:
    config = LANG_CONFIG[lang]
    doc_root = language_root(lang)
    if not doc_root.is_dir():
        raise FileNotFoundError(f"Missing language directory: {doc_root}")
    if not sync_index(lang, write=False):
        raise RuntimeError(
            f"{config['index_file']} is out of date; run: python scripts/build_pdf.py --write-index"
        )

    output_root = ROOT / "build"
    output_root.mkdir(exist_ok=True)
    output_dir = output_root / lang
    output_dir.mkdir(exist_ok=True)
    raw_version = read_manifest_version()
    version = sanitize_version(raw_version)
    output_file = output_root / f"{config['pdf_basename']}_{version}.{output_format}"
    header_tex = ROOT / "scripts" / config.get("header_tex", "pandoc-header.tex")

    generated_at = build_timestamp().strftime("%Y-%m-%d %H:%M UTC")

    env = os.environ.copy()
    resource_path = os.pathsep.join([str(doc_root), str(ROOT)])
    cmd = [
        "pandoc",
        "--from",
        "markdown+tex_math_dollars+raw_tex",
        "--standalone",
        "--pdf-engine=xelatex",
        "--metadata",
        f"title={config['title']}",
        "--metadata",
        f"author={AUTHOR}",
        "--metadata",
        f"date={generated_at}",
        "--metadata",
        f"lang={config['lang']}",
        "--include-in-header",
        str(header_tex),
        "--lua-filter",
        str(ROOT / "scripts" / "glossary-columns.lua"),
        "--resource-path",
        resource_path,
    ]

    if output_format == "pdf":
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
        cmd += ["--include-before-body", str(cover_include), "--filter", "pandoc-mermaid"]

    cmd += ["-o", str(output_file), str(doc_root / config["contents_file"])]
    cmd += [str(doc_root / chapter) for chapter in config["chapters"]]

    run_pandoc(cmd, env)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build PDFs for the method documentation.")
    parser.add_argument(
        "--lang",
        action="append",
        choices=SUPPORTED_LANGS,
        help="Language to build. Repeatable. Defaults to all supported languages.",
    )
    parser.add_argument(
        "--format",
        choices=("pdf", "tex"),
        default="pdf",
        help="Output format. 'tex' skips the cover and Mermaid rendering (for quick checks).",
    )
    parser.add_argument(
        "--write-index",
        action="store_true",
        help="Regenerate the Markdown index files from chapter headings and exit.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    langs = args.lang or list(SUPPORTED_LANGS)
    if args.write_index:
        for lang in langs:
            sync_index(lang, write=True)
        return
    for lang in langs:
        build_for_language(lang, args.format)


if __name__ == "__main__":
    main()
