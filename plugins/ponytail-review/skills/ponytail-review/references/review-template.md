> [Hub](./README.md) · [brain.yaml](./brain.yaml) · Related: [ladder.md](./ladder.md), [../SKILL.md](../SKILL.md)

# Review template

Copy this skeleton. Delete unused bullets. Every finding needs a path.

```markdown
# Ponytail senior review — <repo>

Scope: <diff | tree | path>. Date: <ISO date>.

## Pass A — complexity

- `<file>:L<line>: <tag> <what>. <replacement>.`

net: -<N> lines possible.

## Pass B — senior lens

### Architecture
- **P? `<file>`** — finding. Why. Smallest fix.

### Correctness
- **P? `<file>`** — …

### Maintainability
- **P? `<file>`** — …

### Security
- **P? `<file>`** — …

### Tests
- **P? `<file>`** — …

### DX
- **P? `<file>`** — …

### Risks
- **P? `<file>`** — …

### Prioritized actions

1. P0 — …
2. P1 — …
3. P2 — …
```

Pass A tags: `delete:` `stdlib:` `native:` `yagni:` `shrink:`.

If Pass A is empty: `Lean already. Ship.`
