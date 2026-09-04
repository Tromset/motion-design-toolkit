#!/usr/bin/env bash
# Install this git checkout as a Cursor plugin (local symlink).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MANIFEST="$ROOT/.cursor-plugin/plugin.json"
LINK="${CURSOR_PLUGIN_LINK:-$HOME/.cursor/plugins/local/motion-design-toolkit}"

if [[ ! -f "$MANIFEST" ]]; then
  echo "Missing plugin manifest: $MANIFEST" >&2
  exit 1
fi

python3 - "$ROOT" "$MANIFEST" <<'PY'
import json
import sys
from pathlib import Path

root = Path(sys.argv[1])
manifest_path = Path(sys.argv[2])
manifest = json.loads(manifest_path.read_text())
name = manifest.get("name")
if not name:
    raise SystemExit("plugin.json is missing name")

skill_dirs = manifest.get("skills", [])
if isinstance(skill_dirs, str):
    skill_dirs = [skill_dirs]
if not skill_dirs:
    raise SystemExit("plugin.json has no skills paths")

found = []
for rel in skill_dirs:
    folder = (root / rel).resolve()
    if not folder.is_dir():
        raise SystemExit(f"skills path is not a directory: {rel}")
    skills = sorted(p.parent.name for p in folder.glob("*/SKILL.md"))
    if not skills:
        raise SystemExit(f"no SKILL.md under {rel}")
    found.extend(skills)

rules = manifest.get("rules")
if rules:
    rule_paths = [rules] if isinstance(rules, str) else list(rules)
    for rel in rule_paths:
        folder = (root / rel).resolve()
        if not folder.is_dir():
            raise SystemExit(f"rules path is not a directory: {rel}")
        if not any(folder.glob("*.mdc")):
            raise SystemExit(f"no .mdc rules under {rel}")

print(f"ok: {name} ({len(found)} skills: {', '.join(found)})")
PY

mkdir -p "$(dirname "$LINK")"
ln -sfn "$ROOT" "$LINK"

echo "✓ Plugin linked: $LINK -> $ROOT"
echo "Reload Cursor: Developer → Reload Window"
