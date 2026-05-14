#!/bin/bash
set -e

# Handles dos revisores — preencher com os usernames GitHub reais
REVISOR_COORDENADOR="${COORDENADOR:-}"
REVISOR_CONSULTOR="${CONSULTOR:-}"

TITULO="${1:-Contribuição sem título}"
DESCRICAO="${2:-}"
BRANCH=$(git branch --show-current)

# Bloquear push direto para main
if [ "$BRANCH" = "main" ]; then
  echo "ERROR:DIRECT_PUSH_TO_MAIN"
  exit 1
fi

# Verificar se há algo para commitar
if git diff --quiet && git diff --cached --quiet && \
   [ -z "$(git ls-files --others --exclude-standard)" ]; then
  echo "ERROR:NOTHING_TO_COMMIT"
  exit 1
fi

# Coletar todos os arquivos alterados
ALL_CHANGED=$(
  git diff --name-only
  git diff --cached --name-only
  git ls-files --others --exclude-standard
)

# Área crítica: requer aprovação do coordenador
has_critical() {
  echo "$ALL_CHANGED" | grep -qE "^\.(github|claude)/|^schema/|^decisoes/"
}

# Inputs apenas: fluxo livre, auto-merge
is_inputs_only() {
  [ -z "$(echo "$ALL_CHANGED" | grep -v '^$' | grep -v '^inputs/')" ]
}

# Commit e push
git add --all
git commit -m "$TITULO"
git push -u origin "$BRANCH"

PR_BODY="$DESCRICAO

---
*Criado via brain_v4_colli-workflow skill — Claude Code*"

# Roteamento por área tocada
if is_inputs_only; then
  # /inputs/ apenas — sem revisão, auto-merge
  PR_URL=$(gh pr create \
    --title "$TITULO" \
    --body "$PR_BODY" \
    --base main \
    --head "$BRANCH")
  gh pr merge --merge --delete-branch 2>/dev/null || true
  echo "OK:AUTO_MERGED:$PR_URL"

elif has_critical; then
  # Área crítica — PR para coordenador
  if [ -n "$REVISOR_COORDENADOR" ]; then
    PR_URL=$(gh pr create \
      --title "$TITULO" \
      --body "$PR_BODY" \
      --base main \
      --head "$BRANCH" \
      --reviewer "$REVISOR_COORDENADOR")
  else
    PR_URL=$(gh pr create \
      --title "$TITULO" \
      --body "$PR_BODY" \
      --base main \
      --head "$BRANCH")
  fi
  echo "OK:PR_CRITICAL:$PR_URL"

else
  # Área de conteúdo (wiki, projetos, mapa) — PR para consultor
  if [ -n "$REVISOR_CONSULTOR" ]; then
    PR_URL=$(gh pr create \
      --title "$TITULO" \
      --body "$PR_BODY" \
      --base main \
      --head "$BRANCH" \
      --reviewer "$REVISOR_CONSULTOR")
  else
    PR_URL=$(gh pr create \
      --title "$TITULO" \
      --body "$PR_BODY" \
      --base main \
      --head "$BRANCH")
  fi
  echo "OK:PR_CONTENT:$PR_URL"
fi
