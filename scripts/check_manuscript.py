"""Consistency checks for the bilingual manuscript.

Run before building or releasing:

    python scripts/check_manuscript.py

Checks that the English and Spanish editions have the same structure and the same
formal content, that formulas are intact, that index files are current, and that
text files carry no byte-order mark. Exits with status 1 if any check fails.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_pdf import LANG_CONFIG, ROOT, language_root, sync_index  # noqa: E402

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
SECTION_NUMBER_RE = re.compile(r"^(\d+(?:\.\d+)*)\b")
FENCE_RE = re.compile(r"^(```|~~~)\s*(\w*)")
DISPLAY_MATH_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
INLINE_MATH_RE = re.compile(r"(?<![\\$])\$(?!\$)(.+?)(?<![\\$])\$(?!\$)")
TEXT_IN_MATH_RE = re.compile(r"\\text(?:it|rm|bf)?\{[^{}]*\}")
OPEN_DECISION_RE = re.compile(r"\bOD-\d+\b")
GLOSSARY_ENTRY_RE = re.compile(r"^- \*\*[^*]+\*\*")
TEXT_SUFFIXES = {".md", ".py", ".tex", ".html", ".yaml", ".yml", ".lua", ".sh", ".json", ".cmd"}

# Files that exist only to drive the build and have no counterpart content.
NON_CHAPTER_FILES = {"00-index.md", "00-indice.md", "00-contents.md", "00-contenidos.md"}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)


def split_code(text: str) -> tuple[str, list[str]]:
    """Return the text outside fenced blocks and the languages of the fenced blocks."""
    prose: list[str] = []
    fences: list[str] = []
    in_fence = False
    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if match:
            if not in_fence:
                fences.append(match.group(2))
            in_fence = not in_fence
            continue
        if not in_fence:
            prose.append(line)
    return "\n".join(prose), fences


def math_segments(prose: str) -> list[str]:
    display = DISPLAY_MATH_RE.findall(prose)
    remaining = DISPLAY_MATH_RE.sub(" ", prose)
    inline: list[str] = []
    for line in remaining.splitlines():
        stripped = re.sub(r"`[^`]*`", "", line)
        inline.extend(INLINE_MATH_RE.findall(stripped))
    return display + inline


def normalize_math(segment: str) -> str:
    """Drop natural-language text inside math so that formulas compare across languages."""
    return re.sub(r"\s+", "", TEXT_IN_MATH_RE.sub(r"\\text{}", segment))


def structure(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    prose, fences = split_code(text)
    headings = []
    for line in prose.splitlines():
        match = HEADING_RE.match(line)
        if match:
            number = SECTION_NUMBER_RE.match(match.group(2))
            headings.append((len(match.group(1)), number.group(1) if number else ""))
    math = math_segments(prose)
    return {
        "headings": headings,
        "fences": fences,
        "math": [normalize_math(m) for m in math],
        "raw_math": math,
        "table_rows": sum(1 for line in prose.splitlines() if line.lstrip().startswith("|")),
        "open_decisions": sorted(set(OPEN_DECISION_RE.findall(prose))),
        "glossary_entries": sum(1 for line in prose.splitlines() if GLOSSARY_ENTRY_RE.match(line)),
    }


def check_text_files(report: Report) -> None:
    tracked = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.split()
    for name in tracked:
        path = ROOT / name
        if path.suffix not in TEXT_SUFFIXES or not path.is_file():
            continue
        data = path.read_bytes()
        if data.startswith(b"\xef\xbb\xbf"):
            report.error(f"{name}: starts with a UTF-8 byte-order mark")
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            report.error(f"{name}: not valid UTF-8")
            continue
        if "\ufffd" in text:
            report.error(f"{name}: contains U+FFFD replacement characters")


def check_language(lang: str, report: Report) -> None:
    config = LANG_CONFIG[lang]
    root = language_root(lang)
    listed = set(config["chapters"])
    missing = [chapter for chapter in config["chapters"] if not (root / chapter).is_file()]
    for chapter in missing:
        report.error(f"src/{lang}/{chapter}: listed in the build but missing")
    for path in sorted(root.glob("*.md")):
        if path.name not in listed and path.name not in NON_CHAPTER_FILES:
            report.error(f"src/{lang}/{path.name}: not listed in the build configuration")
    if not missing and not sync_index(lang, write=False):
        report.error(
            f"src/{lang}/{config['index_file']}: out of date "
            "(run: python scripts/build_pdf.py --write-index)"
        )
    for chapter in config["chapters"]:
        path = root / chapter
        if not path.is_file():
            continue
        for segment in structure(path)["raw_math"]:
            if "?" in segment:
                report.error(f"src/{lang}/{chapter}: '?' inside a formula (corrupted symbol?): ${segment}$")


def compare_editions(report: Report) -> None:
    langs = list(LANG_CONFIG)
    base = langs[0]
    for other in langs[1:]:
        pairs = zip(LANG_CONFIG[base]["chapters"], LANG_CONFIG[other]["chapters"])
        for left, right in pairs:
            left_path = language_root(base) / left
            right_path = language_root(other) / right
            if not (left_path.is_file() and right_path.is_file()):
                continue
            a, b = structure(left_path), structure(right_path)
            label = f"{base}/{left} vs {other}/{right}"
            for key in ("headings", "fences", "table_rows", "open_decisions", "glossary_entries"):
                if a[key] != b[key]:
                    report.error(f"{label}: {key} differ: {a[key]} != {b[key]}")
            if a["math"] != b["math"]:
                missing = [m for m in a["math"] if m not in b["math"]]
                extra = [m for m in b["math"] if m not in a["math"]]
                detail = missing[:3] or extra[:3] or ["order differs"]
                report.error(
                    f"{label}: formulas differ ({len(a['math'])} vs {len(b['math'])}); e.g. {detail}"
                )


def main() -> int:
    report = Report()
    check_text_files(report)
    for lang in LANG_CONFIG:
        check_language(lang, report)
    compare_editions(report)
    for message in report.errors:
        print(f"error: {message}")
    if report.errors:
        print(f"{len(report.errors)} problem(s) found.")
        return 1
    print("Manuscript checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
