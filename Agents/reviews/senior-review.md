> [Hub](./README.md) · [brain.yaml](./brain.yaml) · Related: [../objectives.md](../objectives.md), [../../plugins/ponytail-review/skills/ponytail-review/SKILL.md](../../plugins/ponytail-review/skills/ponytail-review/SKILL.md)

# Ponytail senior review — motion-design-toolkit

Scope: `/workspace` as of this branch (`cursor/brainify-ponytail-plugin-8fc9`). Tree is a **Cursor skill pack**, not an app. Upstream methodology: [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) (7-rung ladder, review tags, never-lazy list). Date: 2026-09-02.

## Pass A — complexity

- `motion-design-toolkit/README.md:L32-36: delete: second copy of the same \`ln -sfn "$PWD" ~/.cursor/plugins/local/pro-design\` block after install-local.sh. Keep one.`
- `motion-design-toolkit/scripts/install-local.sh:L10-29: native: Origin CLI + curl-pipe-sh + hardcoded feature branch to clone a plugin that is already this git repo. \`mkdir -p ~/.cursor/plugins/local && ln -sfn "$PWD" ~/.cursor/plugins/local/pro-design\` is the whole installer when you already have a checkout.`
- `motion-design-toolkit/skills/gsap/SKILL.md: shrink: 324-line skill (largest in the pack). Split APIs/examples into \`references/\` like cursor-sdk; keep SKILL.md as trigger + 3 recipes. Same pattern for lenis (268), vanta (266), react-bits (228).`
- `motion-design-toolkit/skills/ui-ux-pro-max/SKILL.md:L1-4: yagni: description promises "79 styles, 192 palettes, 74 font pairings" and a CLI database the README admits is **not vendored**. Either vendor the data or stop advertising it.`
- `motion-design-toolkit/README.md:L102-129: yagni: "Plugin Structure" tree documents \`.cursor-plugin/plugin.json\` which was missing on \`main\`. A tree that does not match the tree is docs-as-fiction.`

net: ~-40 lines possible in README/installer alone; skill splits are moves, not deletes (token win for agents, not LOC win on disk).

## Pass B — senior lens

### Architecture

- **P0 `motion-design-toolkit/README.md` vs tree** — The documented plugin root is `motion-design-toolkit/` with `.cursor-plugin/plugin.json` (`name: pro-design`). On `main` that manifest **did not exist**. Cursor discovers plugins via `.cursor-plugin/plugin.json` + `"skills": "./skills/"` (see the installed `cursor-sdk` plugin at `~/.cursor/plugins/cache/cursor-public/7975/...`). Without the manifest, `ln -sfn` into `~/.cursor/plugins/local/pro-design` links a folder Cursor may treat as an inert directory. This branch adds the missing manifest; keep it.
- **P1 repo root vs plugin root** — GitHub repo `Tromset/motion-design-toolkit` has a 1-line root `README.md` and nests the real plugin one directory down. Users who clone and symlink `$PWD` (repo root) do not get a plugin. Users who symlink `motion-design-toolkit/` do. The install script and the README disagree about which path is canonical (`~/motion-design-toolkit` vs this repo's nested folder).
- **P2 eight skills, no shared index skill** — Each SKILL.md repeats "When to Apply / Skip". Fine for independent triggers. There is no routing skill that says "user asked for a hero with waves + scroll + 3D" → vanta + lenis + r3f. Agents will over-apply adjacent skills (R3F **and** Vanta for a background).

### Correctness

- **P0 `motion-design-toolkit/scripts/install-local.sh`** — Clones `tromset/pro-design-toolkit` via Origin, then `git checkout cursor/pro-design-plugin-4089`. The public GitHub remote is `Tromset/motion-design-toolkit` and the default branch is `main`. A clean machine following the script will either fail the clone name or pin an old agent branch. The "already a git checkout" path still tries that branch first (L24).
- **P1 CDN / version pins in skills**
  - `skills/vanta/SKILL.md` pulls `three.js/r134` from cdnjs. R3F skill talks React 18/19 + R3F 8/9. An agent following both snippets on one page can load two Three runtimes.
  - `skills/gsap/SKILL.md` pins `gsap@3.15` on jsDelivr. Fine if kept current; there is no "last verified" date.
  - `skills/liquid-glass-js/SKILL.md` tells the agent to copy `container.js` / `button.js` / `glass.css` that **are not in this repo**. The skill is a guide, not a vendor copy — say that in the first screen, or the agent will `read` paths that 404.
- **P1 `skills/ui-ux-pro-max/SKILL.md` vs `README.md` "ui-ux-pro-max Status"** — Skill frontmatter claims the full UI UX Pro Max corpus. Toolkit README says the searchable DB was **not found locally** and only ships two reference markdowns. Agents will invent palettes from the description numbers.

### Maintainability

- **P2 skill length** — gsap 324, lenis 268, vanta 266, liquid-glass 238, react-bits 228, liquid-logo 203, r3f 199, ui-ux 169 + 256 + 117 references. Cursor-sdk keeps SKILL.md short and points at `references/`. Every extra token is paid on every GSAP-flavored prompt.
- **P2 no LICENSE at repo root** — README says "Skill content references upstream MIT/Apache". `react-bits` skill itself notes **MIT + Commons Clause**. Shipping that text inside a "MIT/Apache" umbrella is legally sloppy. Add a root LICENSE and a per-skill `Licenses` line that matches upstream (especially Commons Clause).
- **P2 no `.gitignore`** — small, but the next person who runs `npx serve` or copies a demo into the tree will commit junk.

### Security

- **P1 `install-local.sh` L12** — `curl -fsSL https://downloads.cursor.com/origin/install.sh | sh` then `origin auth login`. Supply chain + interactive auth in a "helper script". Acceptable for a personal bootstrap; dangerous as the documented default. Prefer: "if you already cloned from GitHub, only symlink."
- **P2 copied snippets** — `liquid-glass-js` depends on html2canvas (page sampling). Agents will paste that into production SPAs without noting it snapshots the DOM (privacy) and needs a same-origin page. Call that out next to the CDN script tag.
- **P3 no secrets in tree** — good. Do not add Origin tokens to the installer.

### Tests

- **P2 entire repo** — zero tests on `main`. The installer is the only executable, and it is untested. Ponytail minimum for non-trivial logic: one `assert` self-check. `scripts/brain_audit.py` on this branch carries a tiny `_self_check()`; the install script still has none. A 10-line test that `plugin.json` exists, `name` is `pro-design`, and each `skills/*/SKILL.md` has YAML `name` + `description` would have caught the missing manifest.

### DX

- **P1 root README was one sentence** — GitHub's landing page did not mention install, skills, or the nested plugin folder. This branch expands it as a brAIn hub; keep a 5-line "clone + symlink `motion-design-toolkit/`" snippet near the top of the nested README as well.
- **P1 skill triggers overlap** — `ui-ux-pro-max` description triggers on generic words: "design, build, create, implement, review, landing page". That steals traffic from gsap/lenis/react-bits and from this ponytail-review skill (`review`). Narrow the description to UI/UX nouns.
- **P2 `install-local.sh` INSTALL_DIR default `$HOME/motion-design-toolkit`** — on this Cloud Agent the checkout is `/workspace` with the plugin in a subfolder. The script cannot succeed here without arguments, and it wants Origin credentials.

### Risks

- **P1 stale upstream copies** — skills are adapted snapshots. There is no `UPSTREAM.md` with commit SHAs. GSAP "free for commercial use as of 2024" will rot. Pin `source: <url>@<sha or tag>` in each skill's hub.
- **P2 license mix (Commons Clause on react-bits)** — a company using this pack to generate production components may violate Commons Clause if they "sell" the generated UI kit. Flag in the toolkit README.
- **P3 two plugins in one git repo** — `pro-design` (nested) and `ponytail-review` (`plugins/`). Fine if documented; confusing if someone `ln -sfn` the git root.

### Prioritized actions

1. **P0** Keep `.cursor-plugin/plugin.json` in `motion-design-toolkit/` (`name: pro-design`, `skills: ./skills/`). Never document a manifest you do not commit.
2. **P0** Rewrite `install-local.sh` to: symlink the current checkout's `motion-design-toolkit/` directory; drop Origin clone-of-another-name and the stale branch as the default path.
3. **P1** Align clone URL / folder name (`motion-design-toolkit` vs `pro-design-toolkit`) in README + script.
4. **P1** Narrow `ui-ux-pro-max` description; state clearly that the CLI database is optional and not in-tree.
5. **P1** Label vendor-less skills (`liquid-glass-js`) "guide only — files are not in this repo."
6. **P2** Split the four longest skills into `references/`; add a 15-line manifest test; add LICENSE + react-bits Commons Clause note.
7. **P2** Deduplicate the double `ln -sfn` in the toolkit README.
8. **P3** Add `.gitignore`; record upstream SHAs.

## Method notes (ponytail)

Upstream `/ponytail-review` would have stopped after Pass A. Pass B is the senior increment: this pack's failures are **docs/install/manifest**, not abstractions. The code you should not write is a second installer that talks to Origin. The code you should write is fifteen lines of JSON and a three-line symlink.
