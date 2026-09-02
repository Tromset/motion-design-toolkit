# scripts

Repo-level tools. The only script here is the brAIn auditor.

> Hub · [brain.yaml](./brain.yaml) · Parent: [../README.md](../README.md)

## Contents

| File | Purpose |
|------|---------|
| [README.md](./README.md) | This hub. |
| [brain_audit.py](./brain_audit.py) | Stdlib auditor — tokens, savings table, broken links, orphans. |
| [brain.yaml](./brain.yaml) | Routing table. |

## Subfolders

_None._

## Run

```bash
python3 scripts/brain_audit.py .
```

Exit 0 requires 0 broken relative links and 0 orphan files. Design-plugin install lives in [../motion-design-toolkit/scripts/](../motion-design-toolkit/scripts/README.md).
