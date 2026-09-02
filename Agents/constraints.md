> [Hub](./README.md) · [brain.yaml](./brain.yaml) · Related: [objectives.md](./objectives.md), [reviews/senior-review.md](./reviews/senior-review.md)

# Constraints

- **Do not convert** `.py` / `.sh` / real source into Markdown. This repo's "source" is SKILL.md guidance plus small install scripts.
- **Do not wipe** [motion-design-toolkit/README.md](../motion-design-toolkit/README.md). Enhance hubs; keep install docs.
- **Keep machine config as JSON** — especially `.cursor-plugin/plugin.json`.
- **Skip hidden vendor trees** (`.git/`, `node_modules/`). `.cursor/skills/` may be added but is not part of the brAIn walk.
- **No secrets** in commits. `install-local.sh` already talks to Origin CLI; do not embed tokens.
- **Ponytail**: no new dependency if stdlib / an existing file covers it. Shortest working diff after you understand the flow.
- **Accessibility and security are not optional** even in a skill pack (CDN pins, reduced-motion notes, license honesty).
