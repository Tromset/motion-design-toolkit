---
name: vanta
description: Animated 3D WebGL backgrounds with Vanta.js. Use when the user wants animated hero backgrounds, three.js shader backgrounds, waves/birds/fog/net effects, interactive WebGL page backgrounds, VANTA.WAVES, vantajs.com effects, or mentions vanta, vanta.js, tengbao vanta, or WebGL background animations.
---

# Vanta.js

[Vanta.js](https://github.com/tengbao/vanta) adds 3D animated digital art as webpage backgrounds with a few lines of code. Effects render via [three.js](https://threejs.org) (WebGL) or [p5.js](https://p5js.org), respond to mouse/touch, and weigh ~120kb minified+gzipped (mostly three.js).

> **Note:** The canonical repo is [tengbao/vanta](https://github.com/tengbao/vanta) (npm package `vanta`). Customize effects at https://www.vantajs.com

## When to Apply

Trigger when the user wants:

- Animated WebGL hero or section backgrounds
- Interactive 3D backgrounds (waves, birds, fog, globe, topology, etc.)
- Lightweight alternatives to background video/images
- Brand-colored shader backgrounds with mouse parallax
- React/Next.js background effects without full R3F setup

Skip for full interactive 3D scenes with meshes/models (use `react-three-fiber`), CSS-only gradients, or static images.

## Available Effects

| Effect | Renderer | Import path |
|--------|----------|-------------|
| WAVES | three.js | `vanta/dist/vanta.waves.min` |
| BIRDS | three.js | `vanta/dist/vanta.birds.min` |
| FOG | three.js | `vanta/dist/vanta.fog.min` |
| CLOUDS / CLOUDS2 | three.js | `vanta/dist/vanta.clouds.min` |
| GLOBE | three.js | `vanta/dist/vanta.globe.min` |
| NET | three.js | `vanta/dist/vanta.net.min` |
| RINGS | three.js | `vanta/dist/vanta.rings.min` |
| HALO | three.js | `vanta/dist/vanta.halo.min` |
| CELLS | three.js | `vanta/dist/vanta.cells.min` |
| DOTS | three.js | `vanta/dist/vanta.dots.min` |
| RIPPLE | three.js | `vanta/dist/vanta.ripple.min` |
| TRUNK / TOPOLOGY | p5.js | `vanta/dist/vanta.trunk.min` |

Explore all parameters at https://www.vantajs.com

## Installation

### Script Tags (simplest)

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vanta/dist/vanta.waves.min.js"></script>
<script>
  VANTA.WAVES('#my-background')
</script>
```

### NPM

```bash
npm install vanta three
# p5.js effects also need:
npm install p5
```

## Core Concepts

1. **`el`** — Container element (selector string or DOM ref). Canvas is appended as child; container controls size.
2. **Effect function** — Import specific effect (`WAVES`, `BIRDS`, etc.); returns instance with `setOptions`, `resize`, `destroy`.
3. **Foreground content** — Container can have other children; they render above the canvas.
4. **THREE / p5 passthrough** — Pass npm imports to avoid global `window.THREE`.
5. **Cleanup** — Always call `effect.destroy()` on unmount.

## Minimal Example

```js
VANTA.WAVES({
  el: '#my-background',
  color: 0x000000,
  waveHeight: 20,
  shininess: 50,
  waveSpeed: 1.5,
  zoom: 0.75,
  mouseControls: true,
  touchControls: true,
  gyroControls: false,
})
```

### Common Options (all effects)

| Option | Default | Description |
|--------|---------|-------------|
| `el` | — | Element selector or DOM node (required) |
| `mouseControls` | `true` | Mouse interaction |
| `touchControls` | `true` | Touch interaction |
| `gyroControls` | `false` | Gyroscope as mouse (mobile) |

Each effect has unique parameters (color, speed, scale, etc.) — configure at vantajs.com and export settings.

### Update & Resize

```js
const effect = VANTA.WAVES({ el: '#bg', color: 0x000000 })

effect.setOptions({ color: 0xff88cc })
effect.resize() // after container size change
effect.destroy() // cleanup
```

## React / Next.js

```tsx
'use client'

import { useEffect, useRef, useState } from 'react'
import * as THREE from 'three'
import WAVES from 'vanta/dist/vanta.waves.min'

export function VantaBackground({ children }: { children?: React.ReactNode }) {
  const ref = useRef<HTMLDivElement>(null)
  const [effect, setEffect] = useState<ReturnType<typeof WAVES> | null>(null)

  useEffect(() => {
    if (!ref.current || effect) return

    const vantaEffect = WAVES({
      el: ref.current,
      THREE,
      color: 0x0a0a0a,
      waveHeight: 15,
      shininess: 45,
      waveSpeed: 1.2,
    })
    setEffect(vantaEffect)

    return () => {
      vantaEffect.destroy()
    }
  }, [effect])

  return (
    <div ref={ref} className="relative min-h-screen w-full">
      {children}
    </div>
  )
}
```

### React Hooks Pattern (official)

```tsx
'use client'

import { useEffect, useRef, useState } from 'react'
import BIRDS from 'vanta/dist/vanta.birds.min'
import * as THREE from 'three'

export function BirdsBackground() {
  const [vantaEffect, setVantaEffect] = useState<ReturnType<typeof BIRDS> | null>(null)
  const ref = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!vantaEffect && ref.current) {
      setVantaEffect(
        BIRDS({
          el: ref.current,
          THREE,
        })
      )
    }
    return () => {
      if (vantaEffect) vantaEffect.destroy()
    }
  }, [vantaEffect])

  return (
    <div ref={ref} className="min-h-screen">
      {/* foreground content */}
    </div>
  )
}
```

### Next.js App Router

- **Client-only** — Vanta requires WebGL and DOM; use `'use client'`.
- **Dynamic import** — optional wrapper with `next/dynamic(..., { ssr: false })`.
- **Container sizing** — parent must have explicit height (`min-h-screen`, `h-[600px]`); canvas fills container.
- **Resize** — call `effect.resize()` on window resize or layout change:

```tsx
useEffect(() => {
  const onResize = () => effect?.resize()
  window.addEventListener('resize', onResize)
  return () => window.removeEventListener('resize', onResize)
}, [effect])
```

### p5.js Effects (TRUNK, TOPOLOGY)

```tsx
import p5 from 'p5'
import TRUNK from 'vanta/dist/vanta.trunk.min'

TRUNK({ el: ref.current, p5 })
```

## Styling Patterns

```css
.vanta-container {
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow: hidden;
}

.vanta-container > canvas {
  position: absolute !important;
  top: 0;
  left: 0;
  z-index: 0;
}

.vanta-content {
  position: relative;
  z-index: 1;
}
```

## Best Practices

1. **Import one effect** — tree-shake by importing only the effect you need (`vanta/dist/vanta.waves.min`).
2. **Pass THREE from npm** — avoids global script tag dependency in bundlers.
3. **Destroy on unmount** — prevents WebGL context leaks and duplicate canvases.
4. **Size the container** — canvas matches container dimensions; zero-height parent = invisible effect.
5. **Use vantajs.com** — preview and export exact color/speed parameters before coding.
6. **Limit instances** — one effect per visible section; multiple WebGL contexts hurt performance.
7. **Reduced motion** — consider static fallback when `prefers-reduced-motion: reduce`.

## Common Pitfalls

- **`window.THREE` undefined** — include three.js script tag OR pass `THREE` import to effect constructor.
- **SSR crash** — never init Vanta during server render; use client component.
- **Missing destroy** — navigating away in SPA leaves orphaned canvases without cleanup.
- **Wrong effect import** — each effect is a separate file; no default export from `vanta` root.
- **Container has no height** — effect inits but canvas is 0px tall.
- **Strict Mode double-mount** — React 18 Strict Mode runs effects twice; guard with ref or destroy in cleanup.

## Vanta vs React Three Fiber

| | Vanta | R3F |
|---|-------|-----|
| Setup | Few lines, preset effects | Full scene graph |
| Customization | Effect parameters only | Full Three.js control |
| Bundle | ~120kb + one effect | three + @react-three/fiber + helpers |
| Best for | Hero backgrounds | Interactive 3D products/scenes |

## Resources

- Repo: https://github.com/tengbao/vanta
- Gallery & configurator: https://www.vantajs.com
- npm: https://www.npmjs.com/package/vanta
- three.js: https://threejs.org

## License

MIT — see upstream repo
