#!/usr/bin/env bash
# Install the pro-design Cursor plugin on your machine.
set -euo pipefail

INSTALL_DIR="${1:-$HOME/motion-design-toolkit}"
PLUGIN_LINK="$HOME/.cursor/plugins/local/pro-design"

echo "→ Installing to $INSTALL_DIR"

if ! command -v origin >/dev/null 2>&1; then
  echo "Installing Origin CLI..."
  curl -fsSL https://downloads.cursor.com/origin/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
fi

if ! origin auth status >/dev/null 2>&1; then
  echo "Sign in to Origin (sets up git credentials):"
  origin auth login
fi

if [[ -d "$INSTALL_DIR/.git" ]]; then
  echo "→ Updating existing clone..."
  git -C "$INSTALL_DIR" fetch origin
  git -C "$INSTALL_DIR" checkout cursor/pro-design-plugin-4089 2>/dev/null || git -C "$INSTALL_DIR" checkout main
  git -C "$INSTALL_DIR" pull origin cursor/pro-design-plugin-4089 2>/dev/null || git -C "$INSTALL_DIR" pull origin main
else
  echo "→ Cloning repository..."
  origin repo clone tromset/pro-design-toolkit "$INSTALL_DIR"
  git -C "$INSTALL_DIR" checkout cursor/pro-design-plugin-4089 2>/dev/null || true
fi

mkdir -p "$HOME/.cursor/plugins/local"
ln -sfn "$INSTALL_DIR" "$PLUGIN_LINK"

echo ""
echo "✓ Plugin installed at: $INSTALL_DIR"
echo "✓ Linked to:           $PLUGIN_LINK"
echo ""
echo "Reload Cursor: Developer → Reload Window"
echo "Skills: react-three-fiber, liquid-glass-js, liquid-logo, ui-ux-pro-max,"
echo "        lenis, gsap, vanta, react-bits"
