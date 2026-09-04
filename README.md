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

## Install this repo as a Cursor plugin

The git root is the plugin (`.cursor-plugin/plugin.json`). It loads the eight design skills plus ponytail-review.

```bash
bash scripts/install-local.sh
```

That is `mkdir -p ~/.cursor/plugins/local` plus `ln -sfn "$PWD" ~/.cursor/plugins/local/motion-design-toolkit`. Reload Cursor (`Developer: Reload Window`).

Optional: symlink only [motion-design-toolkit/](./motion-design-toolkit/README.md) or [plugins/ponytail-review/](./plugins/README.md) if you want one pack.
