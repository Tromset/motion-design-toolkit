#!/usr/bin/env python3
"""brAIn auditor — dependency-free (Python >= 3.9 stdlib).

Estimates tokens, reports full-scan vs hub-navigation savings,
finds broken relative links and orphan files.

Exit 0 only when there are 0 broken links and 0 orphan files
(and every non-hidden folder has README.md + brain.yaml).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import deque
from pathlib import Path

# ~4 characters per token is the usual brAIn estimate without a tokenizer.
CHARS_PER_TOKEN = 4.0
SKIP_DIR_NAMES = {
    ".git",
    ".cursor",
    "node_modules",
    "__pycache__",
    ".venv",
    "venv",
    "dist",
    "build",
    ".tox",
    ".pytest_cache",
}
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
# YAML frontmatter on SKILL.md etc. — nav header must follow it.
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
BRAIN_REQUIRED = ("name", "purpose", "parent", "children", "files", "when_to_read")


def is_hidden(path: Path) -> bool:
    return any(part.startswith(".") for part in path.parts)


def should_skip_dir(path: Path) -> bool:
    return path.name in SKIP_DIR_NAMES or path.name.startswith(".")


def iter_brain_dirs(root: Path) -> list[Path]:
    out: list[Path] = []
    stack = [root]
    while stack:
        current = stack.pop()
        out.append(current)
        try:
            children = sorted(current.iterdir(), key=lambda p: p.name)
        except OSError:
            continue
        for child in children:
            if child.is_dir() and not should_skip_dir(child):
                stack.append(child)
    return sorted(out, key=lambda p: str(p))


def iter_brain_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for folder in iter_brain_dirs(root):
        for child in sorted(folder.iterdir(), key=lambda p: p.name):
            if child.is_file() and not child.name.startswith("."):
                files.append(child)
    return files


def estimate_tokens(text: str) -> int:
    if not text:
        return 0
    return max(1, int(round(len(text) / CHARS_PER_TOKEN)))


def file_tokens(path: Path) -> int:
    try:
        return estimate_tokens(path.read_text(encoding="utf-8", errors="replace"))
    except OSError:
        return 0


def extract_links(md_text: str) -> list[str]:
    return [m.group(2).strip() for m in LINK_RE.finditer(md_text)]


def is_external(href: str) -> bool:
    lower = href.lower()
    return (
        lower.startswith("http://")
        or lower.startswith("https://")
        or lower.startswith("mailto:")
        or lower.startswith("tel:")
        or href.startswith("#")
    )


def resolve_link(source: Path, href: str) -> Path | None:
    raw = href.split("#", 1)[0].strip()
    if not raw or is_external(raw):
        return None
    return (source.parent / raw).resolve()


def parse_brain_yaml(path: Path) -> dict[str, object]:
    """Minimal YAML subset reader for the brAIn schema (no PyYAML)."""
    text = path.read_text(encoding="utf-8", errors="replace")
    data: dict[str, object] = {
        "name": None,
        "purpose": None,
        "parent": None,
        "children": [],
        "files": {},
        "when_to_read": {},
        "links": {},
        "_raw": text,
    }
    section: str | None = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if re.match(r"^parent:\s*null\s*$", line):
            data["parent"] = None
            section = None
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m and not line.startswith(" ") and not line.startswith("\t"):
            key, rest = m.group(1), m.group(2).strip()
            section = key
            if key in ("children",) and rest in ("[]", ""):
                data["children"] = []
                if rest == "[]":
                    section = None
            elif key in ("files", "when_to_read", "links") and rest in ("{}", ""):
                data[key] = {}
                if rest == "{}":
                    section = None
            elif key in ("name", "purpose", "parent") and rest:
                data[key] = rest.strip().strip("\"'")
                section = None
            continue
        if section in ("children",) and line.startswith(" "):
            item = line.strip()
            if item.startswith("- "):
                item = item[2:].strip().strip("\"'")
                if item:
                    assert isinstance(data["children"], list)
                    data["children"].append(item)
            continue
        if section in ("files", "when_to_read", "links") and (
            line.startswith(" ") or line.startswith("\t")
        ):
            km = re.match(r"^\s+(.+?):\s*(.*)$", line)
            if km:
                k = km.group(1).strip().strip("\"'")
                v = km.group(2).strip().strip("\"'")
                assert isinstance(data[section], dict)
                data[section][k] = v
    return data


def first_content_block(md_text: str) -> str:
    stripped = FRONTMATTER_RE.sub("", md_text, count=1).lstrip("\n")
    return stripped


def has_nav_header(md_text: str) -> bool:
    body = first_content_block(md_text)
    return body.startswith(">") and "brain.yaml" in body.split("\n", 1)[0]


def collect_markdown_targets(root: Path) -> tuple[list[tuple[Path, str, Path | None]], set[Path]]:
    """Return (link records, resolved local targets)."""
    records: list[tuple[Path, str, Path | None]] = []
    targets: set[Path] = set()
    root_resolved = root.resolve()
    for path in iter_brain_files(root):
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for href in extract_links(text):
            dest = resolve_link(path, href)
            records.append((path, href, dest))
            if dest is None:
                continue
            try:
                dest.relative_to(root_resolved)
            except ValueError:
                continue
            if dest.exists():
                targets.add(dest if dest.is_file() else dest / "README.md")
    return records, targets


def reachable_from_root(root: Path) -> set[Path]:
    root_readme = (root / "README.md").resolve()
    seen: set[Path] = set()
    queue: deque[Path] = deque()
    if root_readme.exists():
        queue.append(root_readme)
    root_resolved = root.resolve()
    while queue:
        current = queue.popleft()
        if current in seen:
            continue
        seen.add(current)
        if not current.exists() or current.suffix.lower() != ".md":
            continue
        text = current.read_text(encoding="utf-8", errors="replace")
        for href in extract_links(text):
            dest = resolve_link(current, href)
            if dest is None or dest in seen:
                continue
            try:
                dest.relative_to(root_resolved)
            except ValueError:
                continue
            if dest.is_dir():
                dest = dest / "README.md"
            if dest.exists():
                queue.append(dest)
    return seen


def rel(root: Path, path: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(path)


def audit(root: Path) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    folders = iter_brain_dirs(root)
    files = iter_brain_files(root)
    token_by_file: dict[Path, int] = {p: file_tokens(p) for p in files}
    total_tokens = sum(token_by_file.values())

    # Rule 1 + 6: every folder has README.md and brain.yaml
    for folder in folders:
        readme = folder / "README.md"
        brain = folder / "brain.yaml"
        if not readme.is_file():
            errors.append(f"missing hub: {rel(root, folder)}/README.md")
        if not brain.is_file():
            errors.append(f"missing brain.yaml: {rel(root, folder)}/brain.yaml")
        elif brain.is_file():
            parsed = parse_brain_yaml(brain)
            for field in BRAIN_REQUIRED:
                if field not in parsed or (
                    parsed[field] is None and field != "parent"
                ):
                    errors.append(f"{rel(root, brain)}: missing field `{field}`")
            if folder == root and parsed.get("parent") not in (None, "null"):
                errors.append(f"{rel(root, brain)}: root parent must be null")
            files_map = parsed.get("files") or {}
            if isinstance(files_map, dict):
                for fname in files_map:
                    candidate = folder / fname
                    if not candidate.exists():
                        errors.append(
                            f"{rel(root, brain)}: files entry not found: {fname}"
                        )
            when = parsed.get("when_to_read") or {}
            if isinstance(when, dict) and not when:
                warnings.append(f"{rel(root, brain)}: empty when_to_read")

    # Broken relative links
    records, _ = collect_markdown_targets(root)
    broken: list[str] = []
    root_resolved = root.resolve()
    for source, href, dest in records:
        if dest is None:
            continue  # external / anchor
        try:
            dest.relative_to(root_resolved)
        except ValueError:
            continue
        if not dest.exists():
            broken.append(f"{rel(root, source)} -> {href}")
            errors.append(f"broken link: {rel(root, source)} -> {href}")

    # Orphans: every non-hidden file must be reachable from the root hub
    reachable = reachable_from_root(root)
    orphans: list[str] = []
    for path in files:
        resolved = path.resolve()
        if resolved in reachable:
            continue
        # A file is also reachable if a reachable markdown links to it
        # (already in `reachable` if it is markdown). For non-md, check inbound.
        inbound = False
        for source, href, dest in records:
            if dest is None:
                continue
            if dest.resolve() == resolved and source.resolve() in reachable:
                inbound = True
                break
        if inbound:
            continue
        orphans.append(rel(root, path))
        errors.append(f"orphan: {rel(root, path)}")

    # Nav-header check for non-hub markdown
    for path in files:
        if path.suffix.lower() != ".md" or path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if not has_nav_header(text):
            warnings.append(f"missing nav header: {rel(root, path)}")

    # Savings table: full-scan vs hub + brain.yaml + this file (+ ancestor hubs)
    rows: list[tuple[str, int, int, int, str]] = []
    for path in files:
        ancestors = []
        folder = path.parent
        while True:
            try:
                folder.resolve().relative_to(root_resolved)
            except ValueError:
                break
            ancestors.append(folder / "README.md")
            ancestors.append(folder / "brain.yaml")
            if folder.resolve() == root_resolved:
                break
            folder = folder.parent
        hub_tokens = 0
        seen_anc: set[Path] = set()
        for anc in ancestors:
            key = anc.resolve() if anc.exists() else anc
            if key in seen_anc:
                continue
            seen_anc.add(key)
            hub_tokens += token_by_file.get(anc, file_tokens(anc) if anc.exists() else 0)
        # The file itself is counted once (may already be a hub README)
        file_tok = token_by_file[path]
        if path not in {p.resolve() for p in seen_anc}:
            nav_tokens = hub_tokens + file_tok
        else:
            nav_tokens = hub_tokens
        savings = max(0, total_tokens - nav_tokens)
        pct = (savings / total_tokens * 100.0) if total_tokens else 0.0
        rows.append((rel(root, path), total_tokens, nav_tokens, savings, f"{pct:.1f}%"))

    print(f"brAIn audit: {root}")
    print(f"folders={len(folders)} files={len(files)} tokens≈{total_tokens}")
    print()
    print("## Savings (full-scan vs hub navigation)")
    print()
    print("| File | Full-scan tokens | Hub-nav tokens | Saved | Saved % |")
    print("|------|-----------------:|---------------:|------:|--------:|")
    for name, full, nav, saved, pct in rows:
        print(f"| {name} | {full} | {nav} | {saved} | {pct} |")
    print()
    if rows:
        avg_pct = sum(float(r[4][:-1]) for r in rows) / len(rows)
        print(f"Average savings: {avg_pct:.1f}%  (chars/4 token estimate)")
        print()

    print(f"Broken links: {len(broken)}")
    for item in broken:
        print(f"  - {item}")
    print(f"Orphan files: {len(orphans)}")
    for item in orphans:
        print(f"  - {item}")
    print()
    if warnings:
        print("Warnings (non-fatal):")
        for item in warnings:
            print(f"  - {item}")
        print()

    extra = [e for e in errors if not e.startswith("broken link:") and not e.startswith("orphan:")]
    if extra:
        print("Other errors:")
        for item in extra:
            print(f"  - {item}")
        print()

    if errors:
        print(f"FAIL  ({len(errors)} error(s))")
        return 1
    print("PASS  (0 broken links, 0 orphans)")
    return 0


def _self_check() -> None:
    """Smallest check that fails if core link/token logic breaks."""
    assert estimate_tokens("abcd") == 1
    assert estimate_tokens("abcdefgh") == 2
    assert is_external("https://example.com")
    assert not is_external("./README.md")
    assert extract_links("see [x](./a.md) and [y](https://z)") == ["./a.md", "https://z"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit a brAIn folder")
    parser.add_argument("target", nargs="?", default=".", help="folder to audit")
    parser.add_argument("--json", action="store_true", help="unused; table is markdown")
    args = parser.parse_args(argv)
    _self_check()
    root = Path(args.target).resolve()
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2
    return audit(root)


if __name__ == "__main__":
    sys.exit(main())
