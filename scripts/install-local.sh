#!/usr/bin/env bash
# Install this git checkout as one Cursor skill (~/.cursor/skills/...).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILL="$ROOT/SKILL.md"
SKILL_LINK="${CURSOR_SKILL_LINK:-$HOME/.cursor/skills/motion-design-toolkit}"
PLUGIN_LINK="${CURSOR_PLUGIN_LINK:-$HOME/.cursor/plugins/local/motion-design-toolkit}"

if [[ ! -f "$SKILL" ]]; then
  echo "Missing unique skill: $SKILL" >&2
  exit 1
fi

python3 - "$ROOT" "$SKILL" <<'PY'
import sys
from pathlib import Path

root = Path(sys.argv[1])
skill = Path(sys.argv[2])
text = skill.read_text()
if "name: motion-design-toolkit" not in text:
    raise SystemExit("SKILL.md must declare name: motion-design-toolkit")

needed = [
    root / "motion-design-toolkit/skills/react-three-fiber/SKILL.md",
    root / "motion-design-toolkit/skills/liquid-glass-js/SKILL.md",
    root / "motion-design-toolkit/skills/liquid-logo/SKILL.md",
    root / "motion-design-toolkit/skills/ui-ux-pro-max/SKILL.md",
    root / "motion-design-toolkit/skills/lenis/SKILL.md",
    root / "motion-design-toolkit/skills/gsap/SKILL.md",
    root / "motion-design-toolkit/skills/vanta/SKILL.md",
    root / "motion-design-toolkit/skills/react-bits/SKILL.md",
    root / "plugins/ponytail-review/skills/ponytail-review/SKILL.md",
]
missing = [str(p.relative_to(root)) for p in needed if not p.is_file()]
if missing:
    raise SystemExit("specialist SKILL.md missing: " + ", ".join(missing))
print("ok: unique skill motion-design-toolkit (9 specialist files)")
PY

mkdir -p "$(dirname "$SKILL_LINK")"
ln -sfn "$ROOT" "$SKILL_LINK"
echo "✓ Skill linked:  $SKILL_LINK -> $ROOT"

# Same checkout, now a single-skill plugin (root SKILL.md, no skills/ scan).
mkdir -p "$(dirname "$PLUGIN_LINK")"
ln -sfn "$ROOT" "$PLUGIN_LINK"
echo "✓ Plugin linked: $PLUGIN_LINK -> $ROOT (one skill)"
echo "Reload Cursor: Developer → Reload Window"
