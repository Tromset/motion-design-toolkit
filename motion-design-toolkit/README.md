# Pro Design — Cursor Plugin

A Cursor agent plugin bundling eight design-focused skills for building premium web interfaces: 3D scenes, liquid glass effects, liquid metal logos, professional UI/UX intelligence, smooth scroll, GSAP animations, WebGL backgrounds, and animated React components.

**GitHub:** https://github.com/Tromset/motion-design-toolkit  
**Origin:** https://cursor.com/codebase/tromset/pro-design-toolkit

## Install on your computer

Paste this in your terminal:

```bash
# Origin CLI (if needed)
curl -fsSL https://downloads.cursor.com/origin/install.sh | sh
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc

# Sign in + clone
origin auth login
origin repo clone tromset/pro-design-toolkit ~/motion-design-toolkit

# Link plugin for Cursor
mkdir -p ~/.cursor/plugins/local
ln -sfn ~/motion-design-toolkit ~/.cursor/plugins/local/pro-design
```

Reload Cursor (`Developer: Reload Window`).

Or run the helper script after cloning:

```bash
bash ~/motion-design-toolkit/scripts/install-local.sh
```

```bash
ln -sfn "$PWD" ~/.cursor/plugins/local/pro-design
```

Then reload Cursor (`Developer: Reload Window`).

## Skills

| Skill | Source | Triggers on |
|-------|--------|-------------|
| **react-three-fiber** | [pmndrs/react-three-fiber](https://github.com/pmndrs/react-three-fiber) | 3D scenes, Three.js in React, Canvas, useFrame, GLTF, @react-three/drei |
| **liquid-glass-js** | [dashersw/liquid-glass-js](https://github.com/dashersw/liquid-glass-js) | Apple-style glass UI, WebGL refraction, frosted buttons/containers |
| **liquid-logo** | [paper-design/liquid-logo](https://github.com/paper-design/liquid-logo) | Liquid metal logos, shader animations, liquid.paper.design effects |
| **ui-ux-pro-max** | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX design, accessibility, palettes, typography, design systems |
| **lenis** | [darkroomengineering/lenis](https://github.com/darkroomengineering/lenis) | Smooth scroll, ReactLenis, useLenis, GSAP ScrollTrigger sync, parallax |
| **gsap** | [greensock/GSAP](https://github.com/greensock/GSAP) | Tweens, timelines, ScrollTrigger, SplitText, Flip, useGSAP, scroll animations |
| **vanta** | [tengbao/vanta](https://github.com/tengbao/vanta) | WebGL animated backgrounds, waves/birds/fog effects, vantajs.com |
| **react-bits** | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | Animated text, UI components, backgrounds, shadcn CLI, reactbits.dev |

## What Each Skill Covers

### react-three-fiber

Declarative Three.js in React. Installation (R3F 8/9 ↔ React 18/19), `<Canvas>`, `useFrame`, pointer events, `@react-three/drei` helpers, performance patterns, Next.js SSR, and the pmndrs ecosystem.

### liquid-glass-js

Vanilla JS WebGL 2.0 glass components. `Container` and `Button` APIs, shape types (rounded/circle/pill), nested glass, global shader parameters, CSS classes, and React wrapper patterns.

### liquid-logo

WebGL liquid metal logo effects. Shader uniforms (dispersion, edge, liquify, speed), `ImageData` pipeline, `Canvas` render loop, upload constraints, and integration from the [liquid-logo](https://github.com/paper-design/liquid-logo) Next.js app.

### ui-ux-pro-max

Design intelligence adapted from the official UI UX Pro Max skill. Priority-ordered UX rules (accessibility → charts), full reference docs for 119 guidelines, pre-delivery checklist, and optional BM25 search via `ui-ux-pro-max-cli`.

### lenis

Lightweight smooth scroll by darkroom.engineering. Native scroll wrapping, `ReactLenis`/`useLenis`, GSAP ScrollTrigger ticker integration, anchor links, nested scroll (`data-lenis-prevent`), reduced motion, and lenis/snap plugin.

### gsap

GreenSock Animation Platform — tweens, timelines, ScrollTrigger, SplitText, Flip, Draggable, motion paths. `@gsap/react` `useGSAP()` hook, `gsap.context()` cleanup, React/Next.js patterns, and Lenis sync.

### vanta

Animated 3D WebGL backgrounds (~120kb). 14 preset effects (WAVES, BIRDS, FOG, GLOBE, etc.), three.js/p5.js rendering, React hooks integration, vantajs.com configurator, and Next.js client-only setup.

### react-bits

165+ animated React components (text, UI, backgrounds). Four variants per component (JS/TS × CSS/Tailwind), shadcn CLI install (`@react-bits/Component-TS-TW`), copy-paste workflow, and reactbits.dev creative tools.

## ui-ux-pro-max Status

**Not found locally** in `~/.cursor/plugins` or `~/.cursor/skills-cursor` at setup time. This plugin includes an **adapted copy** of the official skill with:

- `skills/ui-ux-pro-max/SKILL.md` — workflow and priority rules
- `skills/ui-ux-pro-max/references/quick-reference.md` — full UX guideline index (from upstream)
- `skills/ui-ux-pro-max/references/pro-rules.md` — app polish + pre-delivery checklist (from upstream)

For the full searchable database ( palettes, fonts, reasoning rules ), install the CLI:

```bash
npm install -g ui-ux-pro-max-cli
uipro init --ai cursor
```

## Plugin Structure

```
.
├── .cursor-plugin/
│   └── plugin.json          # Plugin manifest (name: pro-design)
├── skills/
│   ├── react-three-fiber/
│   │   └── SKILL.md
│   ├── liquid-glass-js/
│   │   └── SKILL.md
│   ├── liquid-logo/
│   │   └── SKILL.md
│   ├── ui-ux-pro-max/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── quick-reference.md
│   │       └── pro-rules.md
│   ├── lenis/
│   │   └── SKILL.md
│   ├── gsap/
│   │   └── SKILL.md
│   ├── vanta/
│   │   └── SKILL.md
│   └── react-bits/
│       └── SKILL.md
└── README.md
```

## Usage

Skills auto-trigger when your request matches their descriptions. Examples:

```text
Build a 3D product viewer with React Three Fiber and orbit controls.
```

```text
Add Apple liquid glass navigation buttons to this page.
```

```text
Create a liquid metal animated logo like liquid.paper.design.
```

```text
Design a modern SaaS dashboard — pick colors, typography, and ensure accessibility.
```

```text
Add Lenis smooth scroll and sync it with GSAP ScrollTrigger.
```

```text
Animate the hero text with GSAP SplitText on scroll.
```

```text
Add a Vanta.js waves background to the landing page hero.
```

```text
Install React Bits BlurText and Plasma background for the homepage.
```

## License

Skill content references upstream MIT/Apache projects. See individual repositories for license details.
