---
name: gsap
description: GreenSock Animation Platform — high-performance JavaScript animations. Use when the user wants GSAP tweens, timelines, ScrollTrigger scroll animations, SplitText, Flip layouts, Draggable, motion paths, staggered animations, useGSAP React hook, scroll-driven reveals, or mentions gsap, greensock, GreenSock, ScrollTrigger, or ScrollSmoother.
---

# GSAP (GreenSock Animation Platform)

[GSAP](https://github.com/greensock/GSAP) is a framework-agnostic JavaScript animation library. Animate CSS transforms, SVG, canvas, generic objects, colors, and strings with precise timing, sequencing, and browser compatibility. The entire toolset — including ScrollTrigger, SplitText, Flip, MorphSVG — is **free for commercial use** (as of 2024, sponsored by Webflow).

Docs: https://gsap.com/docs/v3/

## When to Apply

Trigger when the user wants:

- Timeline-based or sequenced animations
- Scroll-driven animations (ScrollTrigger, pin, scrub, snap)
- Text splitting and character/word animations (SplitText)
- Layout transitions (Flip plugin)
- Drag-and-drop with inertia (Draggable)
- SVG morphing, motion paths, or draw effects
- Staggered entrance animations
- GSAP in React via `useGSAP()` from `@gsap/react`
- Integration with Lenis smooth scroll

Skip for simple CSS `@keyframes` transitions, Framer Motion-only React animations (unless mixing with GSAP), or WebGL shader effects (use `react-three-fiber` / `vanta`).

## Installation

```bash
npm install gsap
# React helper
npm install @gsap/react
```

CDN:

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15/dist/gsap.min.js"></script>
```

### Import & Register Plugins

```js
import gsap from 'gsap'
import ScrollTrigger from 'gsap/ScrollTrigger'
import Flip from 'gsap/Flip'
import SplitText from 'gsap/SplitText'

gsap.registerPlugin(ScrollTrigger, Flip, SplitText)
```

Or import everything (excluding legacy members-only):

```js
import { gsap, ScrollTrigger, Draggable, MotionPathPlugin } from 'gsap/all'
gsap.registerPlugin(ScrollTrigger, Draggable, MotionPathPlugin)
```

## Core Concepts

1. **Tween** — Animates properties from current values to target values (`gsap.to`, `.from`, `.fromTo`, `.set`).
2. **Timeline** — Sequences tweens with precise offsets, labels, and nesting (`gsap.timeline()`).
3. **Plugins** — Extend GSAP (ScrollTrigger, SplitText, Flip, Draggable, etc.); must call `gsap.registerPlugin()`.
4. **Context** — `gsap.context()` scopes animations for batch cleanup (used automatically by `useGSAP`).
5. **Eases** — Built-in (`power2.out`, `elastic.out(1, 0.3)`) or custom; see [Ease Visualizer](https://gsap.com/docs/v3/Eases).

## Minimal Examples

### Basic Tween

```js
gsap.to('.box', { rotation: 27, x: 100, duration: 1, ease: 'power2.out' })
```

### Timeline

```js
const tl = gsap.timeline({ defaults: { ease: 'power2.inOut', duration: 0.8 } })

tl.from('.hero-title', { y: 80, opacity: 0 })
  .from('.hero-sub', { y: 40, opacity: 0 }, '-=0.4')
  .from('.hero-cta', { scale: 0.8, opacity: 0 }, '-=0.3')
```

### ScrollTrigger

```js
import gsap from 'gsap'
import ScrollTrigger from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

gsap.from('.card', {
  scrollTrigger: {
    trigger: '.card',
    start: 'top 80%',
    toggleActions: 'play none none reverse',
  },
  y: 60,
  opacity: 0,
  duration: 0.8,
  stagger: 0.15,
})
```

## Key APIs

| API | Purpose |
|-----|---------|
| `gsap.to(target, vars)` | Animate **to** values |
| `gsap.from(target, vars)` | Animate **from** values |
| `gsap.fromTo(target, fromVars, toVars)` | Explicit start and end |
| `gsap.set(target, vars)` | Instant set (duration 0) |
| `gsap.timeline(vars)` | Sequenced animation container |
| `tl.to/from/add/pause/play/reverse()` | Timeline control |
| `gsap.context(fn, scope?)` | Scoped animation batch for cleanup |
| `gsap.matchMedia()` | Responsive animation breakpoints |
| `gsap.utils.interpolate()` | Value interpolation utilities |

### Tween Vars (common)

| Var | Description |
|-----|-------------|
| `duration` | Seconds (default ~0.5) |
| `delay` | Start delay |
| `ease` | Easing function or string |
| `stagger` | Delay between multiple targets |
| `repeat` / `yoyo` | Loop control |
| `paused` | Start paused |
| `onComplete` / `onUpdate` | Callbacks |

### Transform Shorthands

GSAP uses transform shorthands that map to CSS:

- `x`, `y`, `z` — translate
- `rotation`, `rotationX`, `rotationY` — rotate (degrees)
- `scale`, `scaleX`, `scaleY`
- `opacity`, `autoAlpha` (opacity + visibility)

## ScrollTrigger Patterns

```js
ScrollTrigger.create({
  trigger: '.section',
  start: 'top top',      // when top of trigger hits top of viewport
  end: '+=500',          // end 500px later
  pin: true,             // pin element during scroll
  scrub: 1,              // link animation progress to scroll (smooth: 1s catch-up)
  snap: 1 / 4,           // snap to quarters
  markers: true,         // debug (dev only)
  onEnter: () => {},
})
```

**With Lenis smooth scroll:**

```js
lenis.on('scroll', ScrollTrigger.update)
gsap.ticker.add((time) => lenis.raf(time * 1000))
gsap.ticker.lagSmoothing(0)
```

## React — `useGSAP()`

```bash
npm install @gsap/react
```

```tsx
'use client'

import { useRef } from 'react'
import gsap from 'gsap'
import { useGSAP } from '@gsap/react'

gsap.registerPlugin(useGSAP)

export function Hero() {
  const container = useRef<HTMLDivElement>(null)

  useGSAP(
    () => {
      gsap.from('.hero-item', {
        y: 60,
        opacity: 0,
        stagger: 0.12,
        duration: 0.9,
        ease: 'power3.out',
      })
    },
    { scope: container }
  )

  return (
    <div ref={container}>
      <h1 className="hero-item">Title</h1>
      <p className="hero-item">Subtitle</p>
    </div>
  )
}
```

### useGSAP Config

| Option | Description |
|--------|-------------|
| `scope` | Ref or element — scopes selector text (`.box` searches inside scope) |
| `dependencies` | Re-run when deps change |
| `revertOnUpdate` | Revert animations on every dep change (not just unmount) |

### Event Handlers — `contextSafe()`

Functions called **after** the hook (click handlers, setTimeout) must use `contextSafe()` for automatic cleanup:

```tsx
const { contextSafe } = useGSAP({ scope: container })

const onClick = contextSafe(() => {
  gsap.to('.good', { rotation: 180 })
})
```

## Popular Plugins

| Plugin | Use case |
|--------|----------|
| **ScrollTrigger** | Scroll-driven animations, pin, scrub, snap |
| **ScrollSmoother** | Smooth scrolling wrapper (alternative to Lenis) |
| **SplitText** | Split text into chars/words/lines for animation |
| **Flip** | Animate between layout states (FLIP technique) |
| **Draggable** | Drag with bounds, inertia, snap |
| **MotionPathPlugin** | Animate along SVG paths |
| **MorphSVGPlugin** | Morph between SVG shapes |
| **Observer** | Normalized wheel/touch/pointer events |

### SplitText Example

```js
import SplitText from 'gsap/SplitText'
gsap.registerPlugin(SplitText)

const split = new SplitText('.heading', { type: 'chars,words' })
gsap.from(split.chars, { opacity: 0, y: 40, stagger: 0.03, duration: 0.6 })
// split.revert() to restore original DOM
```

### Flip Example

```js
import Flip from 'gsap/Flip'
gsap.registerPlugin(Flip)

const state = Flip.getState('.items')
// ... reorder DOM ...
Flip.from(state, { duration: 0.7, ease: 'power1.inOut', stagger: 0.05 })
```

## Responsive Animations

```js
const mm = gsap.matchMedia()

mm.add('(min-width: 768px)', () => {
  gsap.to('.sidebar', { x: 0, duration: 0.5 })
  return () => gsap.set('.sidebar', { clearProps: 'all' }) // cleanup
})

mm.add('(max-width: 767px)', () => {
  gsap.set('.sidebar', { x: '-100%' })
})
```

## Next.js

- Mark animation components `'use client'`.
- Use `useGSAP()` — it handles SSR via `useIsomorphicLayoutEffect`.
- Call `ScrollTrigger.refresh()` after route transitions, font load, or dynamic content.
- Avoid animating layout properties (`width`, `height`, `top`, `left`) — prefer transforms.

```tsx
'use client'
import { useGSAP } from '@gsap/react'
import ScrollTrigger from 'gsap/ScrollTrigger'

gsap.registerPlugin(useGSAP, ScrollTrigger)

// In layout or page transition handler:
ScrollTrigger.refresh()
```

## Best Practices

1. **Animate transforms and opacity** — GPU-friendly; avoid layout thrashing.
2. **Use timelines** for sequenced UI — cleaner than chained delays.
3. **Register plugins once** — at module top level.
4. **Use `gsap.context()` / `useGSAP`** — automatic cleanup on unmount.
5. **Respect reduced motion** — wrap in `matchMedia('(prefers-reduced-motion: reduce)')` or shorten/disable.
6. **ScrollTrigger.refresh()** — after DOM/layout changes.
7. **Kill tweens on re-run** — `useGSAP` with `revertOnUpdate: true` or manual `gsap.killTweensOf()`.

## Common Pitfalls

- **Forgot `registerPlugin`** — ScrollTrigger/SplitText silently fail.
- **Selector scope in React** — use `scope` ref or unique class names; avoid global selectors hitting wrong elements.
- **Missing cleanup** — memory leaks and duplicate ScrollTriggers without `context.revert()`.
- **ScrollTrigger + smooth scroll** — must sync Lenis/ScrollSmoother with `ScrollTrigger.update`.
- **SplitText DOM changes** — call `.revert()` before React re-renders the same text node.
- **Layout properties** — animating `width`/`height` causes reflow; use `scale` or FLIP.

## Resources

- Docs: https://gsap.com/docs/v3/
- React guide: https://gsap.com/resources/React
- ScrollTrigger: https://gsap.com/docs/v3/Plugins/ScrollTrigger
- Demos: https://gsap.com/demos
- Cheat sheet: https://gsap.com/cheatsheet
- Ease Visualizer: https://gsap.com/docs/v3/Eases
- @gsap/react: https://www.npmjs.com/package/@gsap/react

## License

GreenSock standard "no charge" license: https://gsap.com/standard-license
