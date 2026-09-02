---
name: lenis
description: Smooth scroll with Lenis by darkroom.engineering. Use when the user wants smooth scrolling, scroll-synced WebGL/Three.js scenes, parallax, anchor link scrolling, GSAP ScrollTrigger integration, horizontal scroll, nested scroll containers, ReactLenis, useLenis, or mentions lenis, darkroomengineering, or scroll smoothing.
---

# Lenis

[Lenis](https://github.com/darkroomengineering/lenis) ("smooth" in Latin) is a lightweight, dependency-free smooth scroll library. It wraps native browser scroll so `position: sticky`, anchor links, and accessibility keep working — while giving you a single scroll loop to sync WebGL scenes, GSAP ScrollTrigger, and parallax.

Live demo: https://lenis.darkroom.engineering/

## When to Apply

Trigger when the user wants:

- Smooth scrolling on a website or SPA
- Scroll-synced WebGL / Three.js / R3F scenes
- GSAP ScrollTrigger with smooth scroll (Lenis + GSAP ticker)
- Parallax or scroll-driven animations tied to one scroll source
- Horizontal or nested smooth scrolling
- React/Next.js smooth scroll via `ReactLenis` and `useLenis`
- Anchor link smooth scrolling or programmatic `scrollTo`

Skip for CSS-only `scroll-behavior: smooth` (no sync loop), native scroll without animation, or scroll libraries that replace native scroll entirely (Locomotive Scroll) unless migrating to Lenis.

## Installation

```bash
npm install lenis
```

```js
import Lenis from 'lenis'
import 'lenis/dist/lenis.css'  // recommended — required for autoToggle
```

CDN (no build step):

```html
<link rel="stylesheet" href="https://unpkg.com/lenis@1.3.26/dist/lenis.css">
<script src="https://unpkg.com/lenis@1.3.26/dist/lenis.min.js"></script>
```

## Core Concepts

1. **Native scroll wrapper** — Lenis smooths wheel/touch input; the browser scroll position is the source of truth.
2. **`raf(time)`** — Must run every frame (or use `autoRaf: true`) to advance the smooth scroll animation.
3. **`scroll` event** — Subscribe via `lenis.on('scroll', callback)` for scroll-synced effects.
4. **`scrollTo()`** — Programmatic scroll to pixel value, selector, keyword (`top`, `bottom`), or element.
5. **React adapter** — `ReactLenis` + `useLenis` from `lenis/react`.

## Minimal Example (Vanilla)

```js
import Lenis from 'lenis'
import 'lenis/dist/lenis.css'

const lenis = new Lenis({ autoRaf: true })

lenis.on('scroll', (e) => {
  // e.scroll, e.velocity, e.direction, e.progress
})
```

Custom RAF loop (when integrating with other animation engines):

```js
const lenis = new Lenis()

function raf(time) {
  lenis.raf(time)
  requestAnimationFrame(raf)
}
requestAnimationFrame(raf)
```

## Key Options

| Option | Default | Description |
|--------|---------|-------------|
| `autoRaf` | `false` | Auto-run requestAnimationFrame loop |
| `lerp` | `0.1` | Linear interpolation intensity (0–1); overrides `duration`/`easing` |
| `duration` | `1.2` | Scroll animation duration (seconds); ignored if `lerp` set |
| `smoothWheel` | `true` | Smooth wheel-initiated scroll |
| `orientation` | `vertical` | `vertical` or `horizontal` |
| `gestureOrientation` | `vertical` | `vertical`, `horizontal`, or `both` |
| `anchors` | `false` | Enable smooth anchor link scrolling |
| `allowNestedScroll` | `false` | Auto-detect nested scrollable elements |
| `prevent` | — | `(node) => boolean` — skip smoothing for matched nodes |
| `respectReducedMotion` | `true` | Disable smoothing when user prefers reduced motion |
| `wrapper` | `window` | Scroll container element |
| `content` | `document.documentElement` | Scrolled content element |

## Key Properties & Methods

| API | Purpose |
|-----|---------|
| `lenis.scroll` | Current scroll value |
| `lenis.progress` | Scroll progress 0–1 |
| `lenis.velocity` / `lastVelocity` | Scroll speed |
| `lenis.direction` | `1` up, `-1` down |
| `lenis.isStopped` | Whether scroll is paused |
| `lenis.scrollTo(target, options)` | Scroll to number, selector, keyword, or element |
| `lenis.start()` / `lenis.stop()` | Resume / pause scroll |
| `lenis.resize()` | Recalculate dimensions (when `autoResize: false`) |
| `lenis.destroy()` | Tear down instance and listeners |

`scrollTo` options: `offset`, `lerp`, `duration`, `easing`, `immediate`, `lock`, `force`, `onComplete`.

## GSAP ScrollTrigger Integration

```js
import Lenis from 'lenis'
import gsap from 'gsap'
import ScrollTrigger from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

const lenis = new Lenis()

lenis.on('scroll', ScrollTrigger.update)

gsap.ticker.add((time) => {
  lenis.raf(time * 1000) // GSAP ticker uses seconds; Lenis expects ms
})

gsap.ticker.lagSmoothing(0)
```

## React / Next.js

```tsx
'use client'

import { ReactLenis, useLenis } from 'lenis/react'
import 'lenis/dist/lenis.css'

function ScrollLogger() {
  useLenis((lenis) => {
    // called every scroll
    console.log(lenis.scroll)
  })
  return null
}

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <ReactLenis root options={{ autoRaf: true }}>
      <ScrollLogger />
      {children}
    </ReactLenis>
  )
}
```

### ReactLenis Props

| Prop | Description |
|------|-------------|
| `root` | `true` — global instance via `useLenis` anywhere; uses default `<html>` scroll |
| `options` | Lenis constructor options |
| `ref` | Access `ref.current.lenis` for manual `raf()` when `autoRaf: false` |

### GSAP + ReactLenis

```tsx
import gsap from 'gsap'
import { ReactLenis } from 'lenis/react'
import { useEffect, useRef } from 'react'
import type { LenisRef } from 'lenis/react'

function App() {
  const lenisRef = useRef<LenisRef>(null)

  useEffect(() => {
    function update(time: number) {
      lenisRef.current?.lenis?.raf(time * 1000)
    }
    gsap.ticker.add(update)
    return () => gsap.ticker.remove(update)
  }, [])

  return <ReactLenis root options={{ autoRaf: false }} ref={lenisRef} />
}
```

### Framer Motion

Drive Lenis from Framer's `frame.update()` instead of GSAP ticker — see [lenis/react README](https://github.com/darkroomengineering/lenis/tree/main/packages/react).

### Next.js App Router

- Wrap layout or page content in `ReactLenis` inside a `'use client'` component.
- Import `lenis/dist/lenis.css` in the client component or global CSS.
- For GSAP ScrollTrigger, call `ScrollTrigger.refresh()` after route changes / dynamic content loads.

## Nested Scroll & Modals

**Simplest:** `allowNestedScroll: true` (checks DOM on every scroll — can impact performance).

**Recommended for modals/drawers:**

```html
<div data-lenis-prevent>scrollable modal content</div>
```

| Attribute | Effect |
|-----------|--------|
| `data-lenis-prevent` | Prevent all smooth scroll |
| `data-lenis-prevent-wheel` | Wheel only |
| `data-lenis-prevent-touch` | Touch only |
| `data-lenis-prevent-vertical` | Vertical only |
| `data-lenis-prevent-horizontal` | Horizontal only |

Or via JS: `prevent: (node) => node.id === 'modal'`.

## Snap Plugin

CSS `scroll-snap` is **not supported**. Use [lenis/snap](https://github.com/darkroomengineering/lenis/tree/main/packages/snap) for section snapping.

## No-Code Setup

```html
<link rel="stylesheet" href="https://unpkg.com/lenis@1.3.26/dist/lenis.css">
<script src="https://unpkg.com/lenis@1.3.26/dist/lenis.min.js"></script>
<script>new Lenis({ autoRaf: true, autoToggle: true, anchors: true, allowNestedScroll: true })</script>
```

## Best Practices

1. **Always include `lenis.css`** — required for `autoToggle` and proper overflow behavior.
2. **One Lenis instance** — use `root` in React; avoid multiple competing instances.
3. **Sync external loops** — WebGL/R3F `useFrame`, GSAP ticker, or Framer `frame` should call `lenis.raf(time)`.
4. **Respect reduced motion** — default honors `prefers-reduced-motion`; check `lenis.prefersReducedMotion` for custom animations.
5. **Refresh on resize** — `autoResize: true` (default) handles this; call `resize()` manually if disabled.
6. **Destroy on unmount** — `lenis.destroy()` or let `ReactLenis` handle cleanup.

## Common Pitfalls

- **Missing CSS** — scroll breaks or feels wrong without `lenis.css`.
- **Missing `raf()`** — scroll won't animate unless `autoRaf: true` or manual RAF/GSAP ticker.
- **GSAP time units** — multiply GSAP ticker time by 1000 for `lenis.raf()`.
- **Safari 60fps cap** — smooth scroll capped at 60fps on Safari; 30fps in low power mode.
- **Iframes** — smooth scroll stops over iframes (no wheel forwarding).
- **CSS scroll-snap** — use lenis/snap plugin instead.
- **Anchor links blocked** — set `anchors: true` (default prevents anchors while scrolling).

## Ecosystem

| Package | Use case |
|---------|----------|
| `lenis/react` | ReactLenis, useLenis |
| `lenis/vue` | Vue adapter |
| `lenis/snap` | Section scroll snapping |
| `lenis/framer` | Framer component |

Related: [r3f-scroll-rig](https://github.com/14islands/r3f-scroll-rig) for R3F scroll scenes.

## Resources

- Repo: https://github.com/darkroomengineering/lenis
- Demo: https://lenis.darkroom.engineering/
- Showcase: https://www.lenis.dev/showcase
- Manifesto: https://github.com/darkroomengineering/lenis/blob/main/MANIFESTO.md

## License

MIT © [darkroom.engineering](https://github.com/darkroomengineering)
