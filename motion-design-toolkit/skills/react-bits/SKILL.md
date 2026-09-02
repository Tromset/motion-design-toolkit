---
name: react-bits
description: Animated React components library with 165+ text animations, UI elements, and backgrounds. Use when the user wants copy-paste React animation components, BlurText, SplitText, animated backgrounds, shadcn-compatible animated UI, reactbits.dev components, text reveal effects, or mentions react-bits, DavidHDev, or reactbits.
---

> [Hub](./README.md) · [brain.yaml](./brain.yaml) · Related: [gsap](../gsap/SKILL.md), [liquid-logo](../liquid-logo/SKILL.md)

# React Bits

[React Bits](https://github.com/DavidHDev/react-bits) is the largest open-source library of animated React components — 165+ free, customizable animations for text, backgrounds, and UI. Copy-paste into any modern React project or install via shadcn/jsrepo CLI.

Docs: https://reactbits.dev/

## When to Apply

Trigger when the user wants:

- Pre-built animated text effects (blur reveal, scramble, typewriter, gradient, etc.)
- Animated UI components (cards, nav, dock, sliders, bento grids)
- WebGL/shader animated backgrounds (Plasma, Iridescence, LightTunnel, etc.)
- Quick polish for landing pages without writing animations from scratch
- shadcn-compatible component installs (`@react-bits/ComponentName-TS-TW`)
- Copy-paste animated React components with JS/TS and CSS/Tailwind variants

Skip for non-React projects, vanilla GSAP/CSS-only animations built from scratch, or full 3D product viewers (use `react-three-fiber`).

## Component Categories

| Category | Examples |
|----------|----------|
| **Text Animations** | BlurText, SplitText, GradientText, GlitchText, DecryptedText, CountUp, ScrollReveal, TextType |
| **Components** | MagicBento, Dock, PillNav, GlassSurface, FluidGlass, TiltedCard, Stepper, ProfileCard, MorphSlider |
| **Backgrounds** | Plasma, Iridescence, LightTunnel, Waves, Threads, PixelBlast, Topography, GridScan, LightPillar |

Browse all at https://reactbits.dev/

## Variants (4 per component)

Every component ships in four stack combinations:

| Suffix | Language | Styling |
|--------|----------|---------|
| `JS-CSS` | JavaScript | CSS modules / plain CSS |
| `JS-TW` | JavaScript | Tailwind CSS |
| `TS-CSS` | TypeScript | CSS |
| `TS-TW` | TypeScript | Tailwind CSS |

Pick the variant matching the project's `package.json` stack — **never assume**.

## Installation

### CLI (shadcn registry)

Each component page shows a copy-ready command:

```bash
npx shadcn@latest add @react-bits/BlurText-TS-TW
npx shadcn@latest add @react-bits/Plasma-TS-TW
npx shadcn@latest add @react-bits/MagicBento-JS-TW
```

Requires shadcn/ui initialized in the project. See https://reactbits.dev/get-started/installation

### Manual Copy-Paste

1. Browse https://reactbits.dev — open a component.
2. Set language (JS/TS) and styling (CSS/TW) in the site UI.
3. Copy source from the **Code** tab into your project.
4. Install any listed peer dependencies.
5. Import and render.

```bash
# Example deps for text components using motion
npm install motion

# Example deps for GSAP-based components
npm install gsap @gsap/react
```

```tsx
import SplitText from './SplitText'

<SplitText text="Hello, you!" delay={100} duration={0.6} />
```

## Minimal Example — BlurText (Tailwind + TS)

Typical text animation pattern: IntersectionObserver trigger + motion keyframes:

```tsx
import BlurText from '@/components/BlurText'

<BlurText
  text="Ship stunning interfaces faster"
  delay={150}
  animateBy="words"
  direction="top"
  className="text-4xl font-bold"
  onAnimationComplete={() => console.log('done')}
/>
```

Key props (BlurText):

| Prop | Default | Description |
|------|---------|-------------|
| `text` | `''` | Text to animate |
| `delay` | `200` | Stagger delay (ms) between words/letters |
| `animateBy` | `words` | `words` or `letters` |
| `direction` | `top` | `top` or `bottom` entry direction |
| `threshold` | `0.1` | IntersectionObserver threshold |
| `stepDuration` | `0.35` | Per-step animation duration |
| `animationFrom` / `animationTo` | — | Custom keyframe overrides |

## Minimal Example — Background (Plasma)

```tsx
'use client'

import Plasma from '@/components/Plasma'

<div className="relative h-screen w-full">
  <Plasma
    color="#6366f1"
    speed={0.6}
    direction="forward"
    scale={1.2}
    opacity={0.8}
  />
  <div className="relative z-10">{/* foreground content */}</div>
</div>
```

Background components typically fill their parent — wrap in a sized container with foreground content at higher `z-index`.

## Workflow for AI Agents

1. **Detect stack** — read `package.json` for React version, TypeScript, Tailwind, shadcn.
2. **Pick variant** — e.g. Next.js 15 + TS + Tailwind → `TS-TW`.
3. **Find component** — search https://reactbits.dev or repo paths:
   - `src/ts-tailwind/TextAnimations/<Name>/`
   - `src/ts-tailwind/Components/<Name>/`
   - `src/ts-tailwind/Backgrounds/<Name>/`
4. **Install deps** — check component source imports (`motion`, `gsap`, `three`, `@react-three/fiber`, etc.).
5. **Copy or CLI add** — prefer shadcn add when registry is configured; otherwise copy source.
6. **Customize via props** — all components expose props; edit source for deeper changes.

## Common Dependencies by Category

| Category | Typical deps |
|----------|-------------|
| Text animations | `motion` (Framer Motion v12+) |
| GSAP text | `gsap`, `@gsap/react` |
| 3D components | `three`, `@react-three/fiber`, `@react-three/drei` |
| Backgrounds | `ogl`, `three`, or pure CSS/canvas — check each component |
| UI components | `motion`, `clsx`, sometimes `lucide-react` |

The upstream repo itself uses: `motion`, `gsap`, `@gsap/react`, `lenis`, `@react-three/fiber`, `@react-three/drei`, `matter-js`, `gl-matrix`, and more — **only install what your chosen component imports**.

## React / Next.js Integration

### App Router

```tsx
'use client' // required for animated/interactive components

import dynamic from 'next/dynamic'

const Plasma = dynamic(() => import('@/components/Plasma'), { ssr: false })
```

- Mark animated components `'use client'`.
- Backgrounds with WebGL/canvas: use `dynamic(..., { ssr: false })` or client-only import.
- Place heavy backgrounds once in layout or hero — not on every page.

### Tailwind v4

React Bits TW variants use Tailwind classes. Ensure Tailwind is configured; v4 projects use `@tailwindcss/vite` or PostCSS plugin.

### shadcn/ui

React Bits publishes to the shadcn registry as `@react-bits/<Component>-<Variant>`. Initialize shadcn first:

```bash
npx shadcn@latest init
npx shadcn@latest add @react-bits/GooeyNav-TS-TW
```

## Creative Tools (reactbits.dev/tools)

| Tool | Purpose |
|------|---------|
| [Background Studio](https://reactbits.dev/tools) | Preview backgrounds, export video/image/code |
| [Shape Magic](https://reactbits.dev/tools) | Inner rounded corners between shapes → SVG/React/clip-path |
| [Texture Lab](https://reactbits.dev/tools) | Noise, dithering, ASCII effects on images/video |

## Best Practices

1. **Match variant to stack** — don't mix TW component into CSS-only project without conversion.
2. **Install only needed deps** — components are independent; don't install the whole upstream monorepo.
3. **IntersectionObserver text** — most text animations trigger on scroll-into-view; adjust `threshold`/`rootMargin`.
4. **Respect reduced motion** — wrap or disable animations when `prefers-reduced-motion: reduce`.
5. **One background per viewport** — WebGL backgrounds are GPU-heavy; avoid stacking multiple.
6. **Keep source editable** — components are designed to be copied and customized, not opaque black boxes.

## Common Pitfalls

- **Wrong variant** — TS-TW component in JS-CSS project causes type/Tailwind errors.
- **Missing `'use client'`** — Next.js server components can't use hooks/observers/WebGL.
- **Missing peer deps** — `motion`, `gsap`, or `three` not installed → runtime import errors.
- **Zero-height background parent** — WebGL backgrounds need explicit container dimensions.
- **SSR WebGL** — canvas/WebGL components crash on server; use dynamic import with `ssr: false`.

## Official Ports

| Framework | URL |
|-----------|-----|
| Vue.js | https://vue-bits.dev |
| Svelte | https://sveltebits.xyz |

## Resources

- Site & docs: https://reactbits.dev
- Repo: https://github.com/DavidHDev/react-bits
- Installation: https://reactbits.dev/get-started/installation
- Tools: https://reactbits.dev/tools

## License

MIT + Commons Clause — free for personal and commercial use. See [LICENSE.md](https://github.com/DavidHDev/react-bits/blob/main/LICENSE.md).
