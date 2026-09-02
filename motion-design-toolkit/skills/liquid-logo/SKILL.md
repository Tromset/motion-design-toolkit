---
name: liquid-logo
description: Turn logos into animated liquid metal effects using WebGL shaders and Paper Shaders. Use when the user wants liquid metal logos, animated logo shaders, logo upload with refraction/dispersion effects, liquid.paper.design style effects, @paper-design/shaders-react, or mentions paper-design/liquid-logo.
---

# Liquid Logo

[Liquid Logo](https://github.com/paper-design/liquid-logo) turns uploaded logos into animated liquid metal effects using custom WebGL 2.0 fragment shaders. Live tool: https://liquid.paper.design

Built with Next.js 15, React 19, and `@paper-design/shaders-react`. The core effect is a GLSL fragment shader that refracts, stripes, and animates a logo texture.

## When to Apply

Trigger when the user wants:

- Liquid metal / chrome logo animations
- WebGL shader effects on uploaded logo images or SVGs
- Adjustable dispersion, edge, blur, liquify, and speed controls for logo effects
- Shareable logo effect URLs with query-param state
- Similar aesthetics to liquid.paper.design

Skip for static SVG logos, CSS-only effects, or full 3D scenes (use `react-three-fiber` instead).

## Tech Stack

| Dependency | Purpose |
|------------|---------|
| `@paper-design/shaders-react` | Paper shader components (ecosystem) |
| Next.js 15 + React 19 | App framework |
| WebGL 2.0 | Fragment shader rendering |
| Tailwind CSS 4 | UI styling |
| Vercel Blob | Uploaded logo storage |

## Installation (from source)

```bash
git clone https://github.com/paper-design/liquid-logo.git
cd liquid-logo
bun install   # or npm install
bun dev       # next dev --turbopack
```

Key dependency:

```bash
npm install @paper-design/shaders-react
```

Requires a browser with **WebGL 2.0** support.

## Architecture

```
src/
├── app/hero/liquid-frag.ts   # GLSL fragment shader source
├── hero/
│   ├── canvas.tsx            # WebGL2 canvas + render loop
│   ├── hero.tsx              # UI controls + upload
│   ├── params.ts             # Shader parameter ranges/defaults
│   └── parse-logo-image.ts   # Logo → ImageData conversion
```

### Shader Parameters (`ShaderParams`)

| Param | Range | Default | UI Label | Description |
|-------|-------|---------|----------|-------------|
| `refraction` | 0–0.06 | 0.015 | Dispersion | Chromatic refraction strength |
| `edge` | 0–1 | 0.4 | Edge | Edge falloff / opacity |
| `patternBlur` | 0–0.05 | 0.005 | Pattern Blur | Stripe blur amount |
| `liquid` | 0–1 | 0.07 | Liquify | Noise-based liquid distortion |
| `speed` | 0–1 | 0.3 | Speed | Animation speed multiplier |
| `patternScale` | 1–10 | 2 | Pattern Scale | Stripe pattern scale |

Defaults from `params.ts`:

```typescript
export type ShaderParams = {
  patternScale: number
  refraction: number
  edge: number
  patternBlur: number
  liquid: number
  speed: number
}

export const defaultParams: ShaderParams = {
  patternScale: 2,
  refraction: 0.015,
  edge: 0.4,
  patternBlur: 0.005,
  liquid: 0.07,
  speed: 0.3,
}
```

## Core Implementation Pattern

### 1. Parse logo to ImageData

Upload PNG, JPG, or SVG (max 4.5MB). Transparent or white backgrounds work best; shapes beat wordmarks.

```typescript
// parse-logo-image.ts converts File | URL → ImageData + PNG blob
const { imageData, pngBlob } = await parseLogoImage(file)
```

### 2. WebGL Canvas Component

`Canvas` creates a WebGL2 program with vertex + fragment shaders, uploads logo as `u_image_texture`, and animates via `requestAnimationFrame`:

```tsx
<Canvas imageData={imageData} params={shaderParams} processing={false} />
```

Key uniforms:

- `u_image_texture` — Logo sampler2D
- `u_time` — Animation time (accumulated with `speed`)
- `u_ratio`, `u_img_ratio` — Aspect ratios
- `u_patternScale`, `u_refraction`, `u_edge`, `u_patternBlur`, `u_liquid`

### 3. Fragment Shader Logic

The shader (`liquid-frag.ts`):

- Samples logo alpha as edge mask
- Applies simplex noise for liquid distortion
- Renders diagonal stripe pattern with RGB channel offset (chromatic dispersion)
- Uses bulge + refraction for metallic depth
- Outputs premultiplied RGBA

### 4. Render Loop

```typescript
totalAnimationTime.current += deltaTime * params.speed
gl.uniform1f(uniforms.u_time, totalAnimationTime.current)
gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4)
requestAnimationFrame(render)
```

## Integrating into Your App

### Minimal WebGL Logo Effect

1. Copy `liquid-frag.ts` (fragment shader) and `canvas.tsx` (WebGL setup).
2. Convert your logo to `ImageData` via canvas 2D context.
3. Pass `ShaderParams` and drive sliders or presets.

```tsx
'use client'

import { Canvas } from './canvas'
import { defaultParams } from './params'

function LiquidLogo({ imageData }: { imageData: ImageData }) {
  return (
    <div className="aspect-square w-96" style={{ background: 'linear-gradient(to bottom, #eee, #b8b8b8)' }}>
      <Canvas imageData={imageData} params={defaultParams} processing={false} />
    </div>
  )
}
```

### Background Options

The demo supports preset backgrounds:

- `metal` — `linear-gradient(to bottom, #eee, #b8b8b8)`
- `white`, `black`, or custom hex from color picker

### URL State / Sharing

Hero syncs params to query string for shareable links; uploads go to `/share/{imageId}` via Vercel Blob API.

## Best Practices

1. **Logo input** — Use SVG or high-res PNG with transparent background. Simple shapes render better than detailed wordmarks.
2. **WebGL2 check** — Gracefully degrade if `getContext('webgl2')` fails.
3. **Texture cleanup** — Delete WebGL textures on unmount / image change to avoid leaks.
4. **DPR sizing** — Canvas uses `devicePixelRatio` for crisp output (demo uses 1000px side).
5. **Debounce URL updates** — Safari is sensitive to frequent `history.replaceState` calls (250ms debounce in demo).
6. **Client-only** — Mark components `'use client'` in Next.js; shader init requires browser APIs.

## Paper Shaders Ecosystem

`@paper-design/shaders-react` provides React shader components from [Paper Design](https://paper.design). Explore their docs for additional effects beyond liquid metal.

## Common Pitfalls

- **CORS / blob URLs** — Ensure image sources are same-origin or CORS-enabled before drawing to canvas.
- **Non-power-of-two textures** — Demo uses `CLAMP_TO_EDGE`; very large images may need downscaling.
- **SSR** — WebGL must run client-side only.
- **File size** — Enforce upload limits (demo: 4.5MB max).

## Resources

- Repo: https://github.com/paper-design/liquid-logo
- Live demo: https://liquid.paper.design
- Paper Shaders: `@paper-design/shaders-react`

## License

See upstream LICENSE (Apache-style, check repo).
