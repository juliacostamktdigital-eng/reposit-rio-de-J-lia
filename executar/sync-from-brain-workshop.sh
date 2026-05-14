#!/usr/bin/env bash
# Sincroniza workflow_marketing_os_v1 (brain) → executar/workshop e regera js/app.bundle.js.
# Uso: na raiz de skills_colli_co ou v4-os-all; ou ./sync-from-brain-workshop.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
WORKSPACE="$(cd "$SKILLS_ROOT/.." && pwd)"

SOURCE="${SOURCE_OVERRIDE:-$WORKSPACE/brain_v4_colli/areas/iniciativas/projeto_workshop_mkt_resultados/workflow_marketing_os_v1}"
DEST="${DEST_OVERRIDE:-$SKILLS_ROOT/executar/workshop}"

if [[ ! -d "$SOURCE" ]]; then
  echo "Origem não encontrada: $SOURCE" >&2
  echo "Defina SOURCE_OVERRIDE ou clone brain_v4_colli ao lado de skills_colli_co." >&2
  exit 1
fi

mkdir -p "$DEST"

echo "→ rsync: $SOURCE → $DEST"
rsync -a --delete \
  --exclude 'assets/legacy' \
  --exclude 'metodologia-criacao-skills' \
  --exclude 'build-docs.mjs' \
  --exclude '.DS_Store' \
  --exclude 'node_modules' \
  "$SOURCE/" "$DEST/"

echo "→ esbuild bundle"
cd "$DEST"
npx --yes esbuild js/main.js --bundle --outfile=js/app.bundle.js --platform=browser --format=iife

echo "→ remover fontes modulares JS (mantém só app.bundle.js)"
rm -f js/main.js js/store.js
rm -rf js/canvas js/engine

echo "→ aplicar index.html com bundle (idempotente)"
if grep -q 'type="module".*main.js' index.html 2>/dev/null; then
  # macOS e GNU sed
  if sed --version >/dev/null 2>&1; then
    sed -i 's|<script type="module" src="./js/main.js"></script>|<script defer src="./js/app.bundle.js"></script>|' index.html
  else
    sed -i '' 's|<script type="module" src="./js/main.js"></script>|<script defer src="./js/app.bundle.js"></script>|' index.html
  fi
fi

echo "Feito. Abra com: cd \"$DEST\" && python3 -m http.server 8765"
