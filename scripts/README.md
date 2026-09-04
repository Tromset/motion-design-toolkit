# scripts

Repo-level tools: the brAIn auditor and the local unique-skill installer.

> Hub · [brain.yaml](./brain.yaml) · Parent: [../README.md](../README.md)

## Contents

| File | Purpose |
|------|---------|
| [README.md](./README.md) | This hub. |
| [brain_audit.py](./brain_audit.py) | Stdlib auditor — tokens, savings table, broken links, orphans. |
| [install-local.sh](./install-local.sh) | Symlink this checkout to `~/.cursor/skills/motion-design-toolkit` (one skill). |
| [brain.yaml](./brain.yaml) | Routing table. |

## Subfolders

_None._

## Run

```bash
python3 scripts/brain_audit.py .
bash scripts/install-local.sh
```

Exit 0 on the auditor requires 0 broken relative links and 0 orphan files. The nested [../motion-design-toolkit/scripts/install-local.sh](../motion-design-toolkit/scripts/install-local.sh) is a wrapper around this installer.
