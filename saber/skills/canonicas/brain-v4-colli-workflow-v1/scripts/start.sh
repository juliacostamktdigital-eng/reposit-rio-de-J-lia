#!/bin/bash
set -e

USUARIO="${1:-$(git config user.name | tr ' ' '-' | tr '[:upper:]' '[:lower:]')}"
ASSUNTO="${2:-contribuicao}"
DATA=$(date +%Y%m%d)
BRANCH="contrib/${USUARIO}/${ASSUNTO}-${DATA}"

# Verificar se gh está autenticado
if ! gh auth status &>/dev/null; then
  echo "ERROR:GH_NOT_AUTH"
  exit 1
fi

# Verificar se há alterações não commitadas
if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "ERROR:UNCOMMITTED_CHANGES"
  exit 1
fi

# Atualizar main e criar nova branch
git checkout main
git pull origin main
git checkout -b "$BRANCH"

echo "OK:BRANCH_CREATED:$BRANCH"
