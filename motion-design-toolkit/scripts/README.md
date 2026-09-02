# scripts

Local install helper for the Pro Design plugin.

> Hub · [brain.yaml](./brain.yaml) · Parent: [../README.md](../README.md)

## Contents

| File | Purpose |
|------|---------|
| [README.md](./README.md) | This hub. |
| [install-local.sh](./install-local.sh) | Origin clone/update + `~/.cursor/plugins/local/pro-design` symlink. |
| [brain.yaml](./brain.yaml) | Routing table. |

## Subfolders

_None._

## Prefer this when you already have the repo

```bash
mkdir -p ~/.cursor/plugins/local
ln -sfn /workspace/motion-design-toolkit ~/.cursor/plugins/local/pro-design
```

`install-local.sh` still talks to Origin and a historical feature branch — see [../../Agents/reviews/senior-review.md](../../Agents/reviews/senior-review.md).
