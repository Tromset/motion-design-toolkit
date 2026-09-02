> [Hub](./README.md) · [brain.yaml](./brain.yaml) · Related: [constraints.md](./constraints.md), [reviews/senior-review.md](./reviews/senior-review.md)

# Objectives

This repository ships **Cursor skills** that help an agent build premium motion/UI (3D, glass, GSAP, Lenis, Vanta, React Bits, UI/UX rules) and, on this branch, a **ponytail senior-review** skill/plugin plus a **brAIn** navigation layer.

## Success

1. An agent can install the Pro Design plugin and trigger the right skill from a short user request.
2. An agent can open the root [brain.yaml](../brain.yaml) and jump to one file instead of reading every SKILL.md.
3. A senior review of the toolkit exists and is concrete (files, why, fixes).
4. The ponytail-review skill + plugin is installed locally on the Cloud Agent VM without a marketplace publish.

## Non-goals

- Not a web application. There is no runtime to start.
- Not a rewrite of upstream libraries (GSAP, R3F, Lenis, …). Skills point at those APIs.
- Not converting skill source into Markdown code fences (rule 4 is for notes/snippets, not this plugin's guidance files — they are already Markdown).
