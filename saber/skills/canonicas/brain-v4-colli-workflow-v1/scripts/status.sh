#!/bin/bash

CRITICAL_AREAS=("schema/" "decisoes/" ".github/" ".claude/")
REVIEW_AREAS=("wiki/" "projetos/" "mapa/")

# Coletar arquivos alterados
CHANGED=$(git diff --name-only)
STAGED=$(git diff --cached --name-only)
UNTRACKED=$(git ls-files --others --exclude-standard)
ALL_CHANGED=$(echo -e "$CHANGED\n$STAGED\n$UNTRACKED" | sort -u | grep -v '^$')

TOTAL_CHANGED=$(echo "$ALL_CHANGED" | grep -c . || echo 0)
TOTAL_NEW=$(echo "$UNTRACKED" | grep -c . || echo 0)

echo "SUMMARY:CHANGED=$TOTAL_CHANGED:NEW=$TOTAL_NEW"
echo "FILES:$ALL_CHANGED"

# Detectar áreas críticas (requer coordenador)
CRITICAL_HIT=""
for area in "${CRITICAL_AREAS[@]}"; do
  if echo "$ALL_CHANGED" | grep -q "$area"; then
    CRITICAL_HIT="$CRITICAL_HIT $area"
  fi
done

# Detectar áreas de conteúdo (requer consultor)
REVIEW_HIT=""
for area in "${REVIEW_AREAS[@]}"; do
  if echo "$ALL_CHANGED" | grep -q "$area"; then
    REVIEW_HIT="$REVIEW_HIT $area"
  fi
done

if [ -n "$CRITICAL_HIT" ]; then
  echo "WARNING:CRITICAL_AREA:$CRITICAL_HIT"
elif [ -n "$REVIEW_HIT" ]; then
  echo "WARNING:REVIEW_AREA:$REVIEW_HIT"
fi
