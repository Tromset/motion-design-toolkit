# plugins

Cursor plugins that live in-repo (not marketplace). Local symlink install only.

> Hub · [brain.yaml](./brain.yaml) · Parent: [../README.md](../README.md)

## Contents

| File | Purpose |
|------|---------|
| [README.md](./README.md) | This hub. |
| [brain.yaml](./brain.yaml) | Routing table. |

## Subfolders

- [ponytail-review/](./ponytail-review/README.md) — senior-engineer review skill (ponytail ladder + full review lens).

## Local install

The usual path is the **whole repo** as one plugin:

```bash
bash scripts/install-local.sh
```

Review plugin only:

```bash
mkdir -p ~/.cursor/plugins/local
ln -sfn "$PWD/plugins/ponytail-review" ~/.cursor/plugins/local/ponytail-review
```

The eight design skills live in [../motion-design-toolkit/](../motion-design-toolkit/README.md) and are included when you install the git root.
