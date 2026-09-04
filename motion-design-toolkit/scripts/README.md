# scripts

Wrapper around the repo-root installer.

> Hub · [brain.yaml](./brain.yaml) · Parent: [../README.md](../README.md)

## Contents

| File | Purpose |
|------|---------|
| [README.md](./README.md) | This hub. |
| [install-local.sh](./install-local.sh) | Calls [../../scripts/install-local.sh](../../scripts/install-local.sh). |
| [brain.yaml](./brain.yaml) | Routing table. |

## Subfolders

_None._

The git root is the Cursor plugin. Prefer:

```bash
bash scripts/install-local.sh
```

from the repository root. To load **this folder only** (eight design skills, no review plugin):

```bash
mkdir -p ~/.cursor/plugins/local
ln -sfn "$PWD" ~/.cursor/plugins/local/pro-design
```
