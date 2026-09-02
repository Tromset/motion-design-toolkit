---
name: react-three-fiber
description: Build declarative 3D scenes in React with @react-three/fiber (React Three Fiber / R3F). Use when the user wants Three.js in React, 3D components, Canvas scenes, WebGL meshes, useFrame animations, interactive 3D UI, @react-three/drei helpers, GLTF models, post-processing, XR, or mentions react-three-fiber, R3F, pmndrs, or three.js with React.
---

# React Three Fiber

[React Three Fiber](https://github.com/pmndrs/react-three-fiber) is a React renderer for [Three.js](https://threejs.org). Build scenes declaratively with reusable components that react to state, handle pointer events, and participate in React's ecosystem.

## When to Apply

Trigger this skill when the user wants to:

- Add 3D graphics, scenes, or WebGL to a React app
- Animate meshes, lights, or cameras in a render loop
- Load GLTF/GLB models or textures in React
- Build interactive 3D product viewers, hero sections, or data visualizations
- Use ecosystem packages: `@react-three/drei`, `@react-three/postprocessing`, `@react-three/rapier`, `@react-three/xr`

Skip for pure CSS/SVG 2D effects, Canvas 2D, or vanilla Three.js without React (unless migrating to R3F).

## Installation

Match R3F major version to React:

```bash
npm install three @types/three @react-three/fiber
# React 18 → @react-three/fiber@8
# React 19 → @react-three/fiber@9
```

Common add-ons:

```bash
npm install @react-three/drei @react-three/postprocessing
```

## Core Concepts

1. **`<Canvas>`** — Root container; creates scene, camera, renderer, and render loop.
2. **JSX = Three.js** — `<mesh>`, `<boxGeometry>`, `<meshStandardMaterial>` map to `THREE.Mesh`, `THREE.BoxGeometry`, etc.
3. **`useFrame`** — Subscribe to the render loop (like `requestAnimationFrame` scoped to the component).
4. **`useRef`** — Direct access to Three.js objects for imperative updates.
5. **Props = setters** — JSX props call Three.js setters; attach/detach on mount/unmount.

## Minimal Example

```tsx
import { Canvas, useFrame } from '@react-three/fiber'
import { useRef, useState } from 'react'
import type * as THREE from 'three'

function Box(props: JSX.IntrinsicElements['mesh']) {
  const ref = useRef<THREE.Mesh>(null!)
  const [hovered, hover] = useState(false)
  const [clicked, click] = useState(false)

  useFrame((_, delta) => {
    if (ref.current) ref.current.rotation.x += delta
  })

  return (
    <mesh
      {...props}
      ref={ref}
      scale={clicked ? 1.5 : 1}
      onClick={() => click(!clicked)}
      onPointerOver={() => hover(true)}
      onPointerOut={() => hover(false)}
    >
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color={hovered ? 'hotpink' : 'orange'} />
    </mesh>
  )
}

export default function Scene() {
  return (
    <Canvas>
      <ambientLight intensity={Math.PI / 2} />
      <spotLight position={[10, 10, 10]} angle={0.15} penumbra={1} decay={0} intensity={Math.PI} />
      <pointLight position={[-10, -10, -10]} decay={0} intensity={Math.PI} />
      <Box position={[-1.2, 0, 0]} />
      <Box position={[1.2, 0, 0]} />
    </Canvas>
  )
}
```

## Key APIs

| API | Purpose |
|-----|---------|
| `Canvas` | Scene root; props: `camera`, `gl`, `dpr`, `shadows`, `frameloop` |
| `useFrame((state, delta) => {})` | Per-frame callback; `state` has camera, scene, clock |
| `useThree()` | Access renderer, scene, camera, size, viewport |
| `useLoader(loader, url)` | Load textures, GLTF, etc. (Suspense required) |
| `ThreeElements['mesh']` | TypeScript typing for mesh props |

## Pointer Events

R3F meshes support React-style events with 3D raycasting:

- `onClick`, `onPointerOver`, `onPointerOut`, `onPointerDown`, `onPointerUp`
- `event.stopPropagation()` prevents bubbling to parent meshes
- Set `event.object` or use `pointer-events` patterns for layered UI

## Patterns & Best Practices

### Composition

Split scenes into small components (`<Lights />`, `<Model />`, `<Controls />`). Each owns its state and hooks.

### Performance

- Components render **outside** React's reconciliation for Three.js objects — no inherent overhead vs raw Three.js.
- Use `instancedMesh` for many identical objects.
- Lazy-load heavy assets with `React.Suspense` + `useLoader` or `@react-three/drei`'s `useGLTF`.
- Prefer `frameloop="demand"` when the scene is static; call `invalidate()` on changes.
- Dispose geometries/materials on unmount when creating imperatively.

### Lighting

Use physically based units where possible (`intensity={Math.PI}` for lights). Combine `ambientLight` + `directionalLight`/`spotLight` + environment maps (`<Environment />` from drei).

### Camera & Controls

```tsx
import { OrbitControls, PerspectiveCamera } from '@react-three/drei'

<Canvas>
  <PerspectiveCamera makeDefault position={[0, 0, 5]} />
  <OrbitControls enableDamping />
  {/* scene */}
</Canvas>
```

### Loading Models

```tsx
import { useGLTF } from '@react-three/drei'

function Model() {
  const { scene } = useGLTF('/model.glb')
  return <primitive object={scene} />
}

// Preload
useGLTF.preload('/model.glb')
```

Wrap in `<Suspense fallback={null}>`.

### Responsive Canvas

```tsx
<Canvas style={{ width: '100%', height: '100vh' }} dpr={[1, 2]}>
```

Use `useThree(({ size, viewport }) => ...)` for responsive layout in 3D space.

### Next.js

Use dynamic import with `ssr: false`:

```tsx
import dynamic from 'next/dynamic'
const Scene = dynamic(() => import('./Scene'), { ssr: false })
```

### React Native

Import from `@react-three/fiber/native`. Configure Metro for `.glb`/`.png` assets in `metro.config.js`.

## Ecosystem (pmndrs)

| Package | Use case |
|---------|----------|
| `@react-three/drei` | Helpers: OrbitControls, Environment, Text, Html, useGLTF |
| `@react-three/postprocessing` | Bloom, SSAO, depth of field |
| `@react-three/rapier` | Physics |
| `@react-three/xr` | VR/AR |
| `@react-three/gltfjsx` | Convert GLTF to JSX components |
| `zustand` / `jotai` | Scene state management |
| `leva` | Debug GUI controls |

## Common Pitfalls

- **Version mismatch** — R3F 8 requires React 18; R3F 9 requires React 19.
- **Missing Suspense** — `useLoader` and async drei hooks need a Suspense boundary.
- **Forgetting lights** — `meshStandardMaterial` needs lighting or an environment map.
- **SSR** — Canvas requires browser WebGL; disable SSR in Next.js.
- **Scale & units** — Three.js uses arbitrary units; keep camera distance and object scale consistent.

## Resources

- Docs: https://docs.pmnd.rs/react-three-fiber
- Three.js manual: https://threejs.org/manual/
- Examples: https://docs.pmnd.rs/react-three-fiber/getting-started/examples
