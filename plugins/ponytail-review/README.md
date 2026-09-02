# ponytail-review

Cursor plugin that makes an agent review like a lazy senior: climb the ponytail ladder, then finish a full senior pass (architecture, correctness, security, tests, DX).

> Hub · [brain.yaml](./brain.yaml) · Parent: [../README.md](../README.md)

## Contents

| File | Purpose |
|------|---------|
| [README.md](./README.md) | This hub — install and usage. |
| [brain.yaml](./brain.yaml) | Routing table. |

Machine config (not converted — brAIn rule 5): [.cursor-plugin/plugin.json](./.cursor-plugin/plugin.json).

## Subfolders

- [skills/](./skills/README.md) — `ponytail-review` skill + references.
- [rules/](./rules/README.md) — Cursor rule (`ponytail-review.mdc`).

## Install (this VM / any machine)

No marketplace publish. Symlink the plugin root:

```bash
mkdir -p ~/.cursor/plugins/local ~/.cursor/skills
ln -sfn /workspace/plugins/ponytail-review ~/.cursor/plugins/local/ponytail-review
ln -sfn /workspace/plugins/ponytail-review/skills/ponytail-review ~/.cursor/skills/ponytail-review
```

From a clone of this repo, replace `/workspace` with `$PWD` if the plugin lives at `plugins/ponytail-review`.

Reload Cursor (`Developer: Reload Window`).

## When to trigger

User says: review, senior review, ponytail-review, over-engineered, what can we delete, audit this repo, is this safe to ship.

## Companion plugin

Design/motion skills: [../../motion-design-toolkit/README.md](../../motion-design-toolkit/README.md).
