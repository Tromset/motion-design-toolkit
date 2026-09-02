---
name: ui-ux-pro-max
description: UI/UX design intelligence for web, mobile, and desktop. Use when designing, building, reviewing, or fixing interfaces — pages, components, design systems, accessibility, interaction, responsive layout, typography, color, charts, and stack-specific UI implementation. Includes 79 styles, 192 palettes, 74 font pairings, 119 UX guidelines, and 22 tech stacks. Triggers on keywords like design, build, create, implement, review, landing page, dashboard, accessibility, or color palette.
---

# UI/UX Pro Max — Design Intelligence

Adapted from [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill). Searchable design guidance for AI coding assistants: styles, palettes, typography, UX rules, icons, GSAP presets, charts, and stack-specific implementation patterns.

## When to Apply

Use this skill when the task involves **UI structure, visual design, interaction patterns, or UX quality**:

- Designing new pages, dashboards, landing pages, or apps
- Choosing colors, typography, spacing, or layout systems
- Reviewing UI for accessibility, consistency, or polish
- Implementing navigation, animation, or responsive behavior
- Fixing interfaces that "don't look professional"

**Skip** for pure backend logic, API/database design, infrastructure, or non-visual scripts — unless the task changes how something **looks, feels, moves, or is interacted with**.

## Rule Categories by Priority

Follow priority 1→10. Full rule text is in `references/quick-reference.md`; app polish rules in `references/pro-rules.md`.

| Priority | Category | Impact | Key Checks | Anti-Patterns |
|----------|----------|--------|------------|---------------|
| 1 | Accessibility | CRITICAL | Contrast 4.5:1, alt text, keyboard nav, aria-labels | Removing focus rings, icon-only buttons without labels |
| 2 | Touch & Interaction | CRITICAL | Min 44×44px targets, 8px+ spacing, loading feedback | Hover-only interactions, instant 0ms state changes |
| 3 | Performance | HIGH | WebP/AVIF, lazy loading, CLS < 0.1 | Layout thrashing, cumulative layout shift |
| 4 | Style Selection | HIGH | Match product type, SVG icons (no emoji) | Mixing flat & skeuomorphic randomly |
| 5 | Layout & Responsive | HIGH | Mobile-first, viewport meta, no horizontal scroll | Fixed px containers, horizontal scroll |
| 6 | Typography & Color | MEDIUM | Base 16px, line-height 1.5, semantic tokens | Text < 12px body, raw hex in components |
| 7 | Animation | MEDIUM | Context-aware timing, reduced-motion support | One duration for everything, animating width/height |
| 8 | Forms & Feedback | MEDIUM | Visible labels, inline errors, progressive disclosure | Placeholder-only labels, errors only at top |
| 9 | Navigation Patterns | HIGH | Predictable back, bottom nav ≤5, deep linking | Overloaded nav, broken back behavior |
| 10 | Charts & Data | LOW | Legends, tooltips, accessible colors | Color as sole data indicator |

## Workflow

### Step 1: Analyze Requirements

Extract from the user request:

- **Product type**: SaaS, e-commerce, portfolio, dashboard, tool, etc.
- **Audience & context**: age group, usage context
- **Style keywords**: minimal, dark mode, playful, glassmorphism, etc.
- **Stack**: detect from `package.json` (React/Next/Vue/Svelte), `pubspec.yaml` (Flutter), etc. **Never assume a stack.**

### Step 2: Design System (new pages/projects)

For coherent visual direction, apply reasoning from the priority table and reference files:

1. Read `references/quick-reference.md` for the relevant categories (§4 Style, §6 Typography & Color).
2. Match product type to style (e.g., SaaS → minimal/swiss; entertainment → vibrant/bold).
3. Define: pattern, style, color palette, typography pairing, effects, anti-patterns.

**Optional — full BM25 search database:**

Install the official CLI for searchable palettes, fonts, and reasoning rules:

```bash
npm install -g ui-ux-pro-max-cli
uipro init --ai cursor
```

This adds `scripts/search.py` and CSV data for queries like:

```bash
python scripts/search.py "beauty spa wellness" --design-system -p "Serenity Spa"
python scripts/search.py "glassmorphism dark" --domain style
python scripts/search.py "suspense streaming" --stack nextjs
```

### Step 2b: Persist Design System

When using the full CLI, persist with `--persist --output-dir "<project-root>"`:

```
design-system/<ProjectName>/MASTER.md       # Global source of truth
design-system/<ProjectName>/pages/<page>.md # Page-specific overrides
```

Read existing `MASTER.md` before regenerating. Never `--force` without user authorization.

### Step 3: Supplement with Domain Searches (full CLI)

| Need | Domain | Example |
|------|--------|---------|
| Product patterns | `product` | `"entertainment social" --domain product` |
| Style options | `style` | `"glassmorphism dark" --domain style` |
| Color palettes | `color` | `"saas professional" --domain color` |
| Font pairings | `typography` | `"playful modern" --domain typography` |
| UX best practices | `ux` | `"keyboard focus modal" --domain ux` |
| Landing structure | `landing` | `"hero social-proof" --domain landing` |
| Icons | `icons` | `"icon button accessible label" --domain icons` |
| GSAP animation | `gsap` | `"scroll reveal stagger" --domain gsap` |
| Charts | `chart` | `"real-time dashboard" --domain chart` |

### Step 4: Stack Guidelines (full CLI)

```bash
python scripts/search.py "<keyword>" --stack <stack>
```

**Stacks:** `react`, `nextjs`, `vue`, `svelte`, `astro`, `nuxtjs`, `angular`, `swiftui`, `react-native`, `flutter`, `html-tailwind`, `shadcn`, `threejs`, and more.

## Without the CLI (built-in guidance)

When the search database is not installed, use:

1. **Priority table above** — Apply CRITICAL rules first (accessibility, touch targets).
2. **`references/quick-reference.md`** — Full 119 UX guidelines by category.
3. **`references/pro-rules.md`** — Pre-delivery checklist for app/native UI.

Do **not fabricate** palette or font data. State explicitly when using general defaults vs. database matches.

## Design Dials (full CLI)

Tune `--design-system` output with optional sliders:

| Dial | Low (1–3) | Mid (4–7) | High (8–10) |
|------|-----------|-----------|-------------|
| `--variance` | Minimal/centered | Balanced modern | Bold/asymmetric |
| `--motion` | Subtle micro-interactions | Standard scroll/stagger | Complex choreography |
| `--density` | Spacious (24–96px) | Standard (16–64px) | Dense/dashboard (8–32px) |

## Example Workflow

**User:** "Create a modern SaaS pricing page with React and Tailwind."

1. Detect stack: React + Tailwind → `html-tailwind` or `react`
2. Apply priority rules: accessibility contrast, touch targets, mobile-first layout
3. Style direction: Minimalism/Swiss for SaaS; professional blue palette; Plus Jakarta Sans or Inter
4. Read `references/quick-reference.md` §4 (Style), §5 (Layout), §8 (Forms)
5. If CLI installed: `python scripts/search.py "saas pricing page" --design-system -p "Pricing"`
6. Implement with semantic tokens, not raw hex scattered in components

## Tips for Better Results

- One dominant intent per query: `"keyboard focus modal"`, not a full audit checklist
- Retry once with narrower terms if results are off-topic
- For accessibility: query observable outcomes (`"focus not obscured" --domain ux`)
- For layout bugs: semantic UX outcome first, then stack-specific implementation

## Before Delivering UI

Read `references/pro-rules.md` and run the **Pre-Delivery Checklist**:

- [ ] Contrast ≥4.5:1 in light and dark mode
- [ ] Touch targets ≥44×44pt / 48×48dp
- [ ] No emojis as structural icons (use SVG)
- [ ] Visible focus rings and keyboard navigation
- [ ] Reduced-motion and dynamic text size supported
- [ ] Safe areas respected on mobile
- [ ] Tested at 375px width and landscape

## Reference Files

| File | Use when |
|------|----------|
| `references/quick-reference.md` | Full rule set for all 10 categories; UI audit pass |
| `references/pro-rules.md` | App/native polish; "doesn't look professional" issues |

## Source & Updates

- Official repo: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- CLI: `npm install -g ui-ux-pro-max-cli` then `uipro init --ai cursor`
- Marketplace: `/plugin install ui-ux-pro-max@ui-ux-pro-max-skill`
