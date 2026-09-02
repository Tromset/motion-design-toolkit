# motion-design-toolkit

Combination of motion design tools in a skill for AI agents — plus a brAIn navigation layer and a ponytail senior-review plugin.

> Hub · [brain.yaml](./brain.yaml) · root

## Contents

| File | Purpose |
|------|---------|
| [README.md](./README.md) | This hub — folder map and routing. |
| [AGENTS.md](./AGENTS.md) | Always-on agent rules: ponytail ladder + brAIn routing. |
| [brain.yaml](./brain.yaml) | Root variables card and `when_to_read` table. |

## Subfolders

- [Agents/](./Agents/README.md) — objectives, constraints, and the senior review.
- [motion-design-toolkit/](./motion-design-toolkit/README.md) — Pro Design Cursor plugin (eight motion/UI skills).
- [plugins/](./plugins/README.md) — locally installable ponytail-review Cursor plugin.
- [scripts/](./scripts/README.md) — brAIn auditor (`brain_audit.py`).

## How to navigate (brAIn)

Open [brain.yaml](./brain.yaml) and pick the one file that answers the question. Do not full-scan the tree.

```text
python3 scripts/brain_audit.py .
```

## Install the review plugin locally

```bash
mkdir -p ~/.cursor/plugins/local ~/.cursor/skills
ln -sfn "$PWD/plugins/ponytail-review" ~/.cursor/plugins/local/ponytail-review
ln -sfn "$PWD/plugins/ponytail-review/skills/ponytail-review" ~/.cursor/skills/ponytail-review
```

Reload Cursor (`Developer: Reload Window`). Design skills install separately from [motion-design-toolkit/](./motion-design-toolkit/README.md).
