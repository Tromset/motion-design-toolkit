---
name: liquid-glass-js
description: Apple Liquid Glass-inspired WebGL glass effects with real-time refraction, blur, and masking. Use when the user wants liquid glass UI, glassmorphism buttons, frosted glass containers, WebGL glass shaders, Apple-style glass panels, nested glass components, or mentions liquid-glass-js, dashersw glass, or html2canvas page sampling for glass effects.
---

# Liquid Glass JS

[Liquid Glass JS](https://github.com/dashersw/liquid-glass-js) brings Apple Liquid Glass-style effects to the web using WebGL 2.0 shaders. It provides `Container` and `Button` classes with real-time refraction, multi-layer edge/rim/base distortion, background blur, and nested glass (child elements sample parent output).

Live demo: https://dashersw.github.io/liquid-glass-js/

## When to Apply

Trigger when the user wants:

- Apple-style liquid/frosted glass UI components
- WebGL-powered glass buttons, nav bars, or control panels
- Nested glass containers where inner elements refract outer glass
- Real-time adjustable glass parameters (blur, refraction, tint)
- Vanilla JS glass effects (no framework build step required)

Skip for pure CSS `backdrop-filter` glass (no refraction), React-only CSS glassmorphism without WebGL, or mobile-native glass APIs.

## Requirements

- WebGL 2.0 (Chrome 80+, Firefox 75+, Safari 14+, Edge 80+)
- ES6+ JavaScript
- [html2canvas](https://html2canvas.hertzen.com/) for page background sampling (CDN or npm)

## Installation

No build step — copy or serve the library files directly:

```
liquid-glass-js/
├── container.js   # Core Container class
├── button.js      # Button class (extends Container)
├── glass.css      # Glass component styles
└── styles.css     # Base styling
```

```html
<link rel="stylesheet" href="styles.css" />
<link rel="stylesheet" href="glass.css" />
<script src="https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js"></script>
<script src="container.js"></script>
<script src="button.js"></script>
```

Local dev: `npx serve .` (WebGL requires a local server, not `file://`).

## Quick Start

### Glass Button

```javascript
const button = new Button({
  text: 'Click Me!',
  size: 32,
  type: 'rounded',
  onClick: () => alert('Hello Glass!')
})

document.body.appendChild(button.element)
```

### Container with Nested Glass

```javascript
const container = new Container({
  borderRadius: 24,
  type: 'pill',
  tintOpacity: 0.3
})

const button1 = new Button({ text: 'Action', size: 24, type: 'pill' })
const button2 = new Button({ text: '✓', size: 24, type: 'circle' })

container.addChild(button1)
container.addChild(button2)
document.body.appendChild(container.element)
```

## API Reference

### Container

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `borderRadius` | `number` | `48` | Corner radius (px) |
| `type` | `'rounded' \| 'circle' \| 'pill'` | `'rounded'` | Shape type |
| `tintOpacity` | `number` | `0.2` | Tint overlay opacity (0–1) |

**Methods:**

- `addChild(child)` — Nest glass element; child samples parent output
- `removeChild(child)` — Remove nested child
- `updateSizeFromDOM()` — Force size recalculation from DOM

### Button (extends Container)

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `text` | `string` | `'Button'` | Label text |
| `size` | `number` | `48` | Font size (px); for `circle`, determines diameter |
| `type` | `'rounded' \| 'circle' \| 'pill'` | `'rounded'` | Shape |
| `onClick` | `function` | `null` | Click handler |
| `warp` | `boolean` | `false` | Center distortion effect |
| `tintOpacity` | `number` | `0.2` | Tint opacity (0–1) |

## Glass Effect Parameters

Fine-grained shader uniforms (adjustable globally via `window.glassControls`):

| Parameter | Range | Description |
|-----------|-------|-------------|
| `edgeIntensity` | 0–0.1 | Refraction at shape edges |
| `rimIntensity` | 0–0.2 | Rim lighting strength |
| `baseIntensity` | 0–0.05 | Center distortion |
| `edgeDistance` | 0.05–0.5 | Edge effect falloff |
| `rimDistance` | 0.1–2.0 | Rim falloff |
| `baseDistance` | 0.05–0.3 | Base falloff |
| `cornerBoost` | 0–0.1 | Corner enhancement |
| `rippleEffect` | 0–0.5 | Surface texture |
| `blurRadius` | 1–15 | Background blur |
| `tintOpacity` | 0–1 | Gradient overlay |

### Global Controls

```javascript
window.glassControls = {
  edgeIntensity: 0.02,
  rimIntensity: 0.08,
  blurRadius: 7.0,
  tintOpacity: 0.3
}

function updateAllGlassInstances() {
  Container.instances.forEach(instance => {
    if (instance.gl_refs?.gl) {
      const gl = instance.gl_refs.gl
      gl.uniform1f(instance.gl_refs.edgeIntensityLoc, window.glassControls.edgeIntensity)
      // ... update other uniforms
      instance.render?.()
    }
  })
}
```

## Shape Types

```javascript
// Rounded rectangle
new Button({ type: 'rounded', borderRadius: 16 })

// Perfect circle (size = diameter)
new Button({ type: 'circle', size: 32, text: '✓' })

// Pill / capsule (auto-width from text)
new Button({ type: 'pill', text: 'Elongated Button' })
```

## CSS Classes

```css
.glass-container          /* Base container */
.glass-container-circle   /* Circle variant */
.glass-container-pill     /* Pill variant */
.glass-button             /* Button base */
.glass-button-circle      /* Circle button */
.glass-button-text        /* Text overlay */
```

Custom themes via CSS (shadows, text color, text-shadow).

## Architecture

- **Multi-layer refraction** — Separate edge, rim, and base calculations
- **Shape-aware normals** — Different algorithms per shape type
- **Gaussian blur** — 13×13 adaptive kernel
- **Page capture** — html2canvas samples background for refraction source
- **Nested glass** — Children sample parent container WebGL output
- **Dynamic uniforms** — Live parameter updates without re-init

## Example Patterns

### Navigation Bar

```javascript
const nav = new Container({ type: 'rounded', borderRadius: 20, tintOpacity: 0.1 })
;['Home', 'About', 'Contact'].forEach(text => {
  nav.addChild(new Button({ text, size: 16, type: 'pill', onClick: t => navigate(t) }))
})
document.body.appendChild(nav.element)
```

### Control Panel

```javascript
const panel = new Container({ type: 'rounded', borderRadius: 12, tintOpacity: 0.6 })
panel.addChild(new Button({ text: '▶', size: 24, type: 'circle', onClick: () => player.play() }))
document.body.appendChild(panel.element)
```

## Best Practices

1. **Serve over HTTP** — WebGL and html2canvas fail on `file://` URLs.
2. **Limit instances** — Each glass element runs WebGL + page capture; batch related UI into containers with nested children.
3. **Use nested glass** — Prefer `container.addChild()` over many top-level instances for cohesive refraction.
4. **Test cross-browser** — Safari WebGL 2.0 behavior can differ; verify blur and tint on target browsers.
5. **Accessibility** — Glass buttons are visual-only; ensure text labels, focus states, and keyboard handlers if wrapping in accessible markup.
6. **Performance** — Page capture via html2canvas is expensive; avoid re-capturing on every frame; update on resize/scroll debounce.

## React / Framework Integration

The library is vanilla JS (no npm package yet). Wrap in React:

```tsx
function GlassButton({ text, onClick }: { text: string; onClick: () => void }) {
  const ref = useRef<HTMLDivElement>(null)
  useEffect(() => {
    const btn = new Button({ text, size: 24, type: 'pill', onClick })
    ref.current?.appendChild(btn.element)
    return () => btn.element.remove()
  }, [text, onClick])
  return <div ref={ref} />
}
```

Load `container.js`, `button.js`, and CSS in your HTML shell or via dynamic script injection.

## Roadmap (upstream)

- NPM bundle, TypeScript rewrite, React/Vue wrappers, animation system, a11y improvements

## License

MIT — https://github.com/dashersw/liquid-glass-js
