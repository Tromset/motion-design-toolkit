# motion-design-toolkit

Combination of motion design tools in a skill for AI agents — plus a brAIn navigation layer and a ponytail senior-review plugin.

> Hub · [brain.yaml](./brain.yaml) · root

## Contents

| File | Purpose |
|------|---------|
| [README.md](./README.md) | This hub — folder map and routing. |
| [AGENTS.md](./AGENTS.md) | Always-on agent rules: ponytail ladder + brAIn routing. |
| [brain.yaml](./brain.yaml) | Root variables card and `when_to_read` table. |
| [SKILL.md](./SKILL.md) | Unique Cursor skill — pick one specialist, do not load all eight. |

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

## Install as one skill

The git root is a **single** Cursor skill ([SKILL.md](./SKILL.md)). It routes to one specialist file; it does not load the eight design skills as separate plugins.

```bash
bash scripts/install-local.sh
```

That is `ln -sfn "$PWD" ~/.cursor/skills/motion-design-toolkit` (and the same path under `~/.cursor/plugins/local` so Cursor still sees a plugin with one skill). Reload Cursor (`Developer: Reload Window`).

To load a specialist pack by itself, symlink [motion-design-toolkit/](./motion-design-toolkit/README.md) or [plugins/ponytail-review/](./plugins/README.md).
