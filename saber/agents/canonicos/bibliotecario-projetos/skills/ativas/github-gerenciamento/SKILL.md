---
name: github-gerenciamento
description: >-
  Orienta fluxos de repositório no GitHub: autenticação, branches, PRs, issues,
  revisões e releases via Git e CLI `gh`. Usar quando o pedido envolver GitHub,
  pull request, fork, clone, CI, proteção de branch, ou automatização de tarefas
  no remoto sem expor segredos.
---

# GitHub — gerenciamento (Colli / brain_v4_colli)

## Objetivo

Padronizar como o agente **opera no GitHub** de forma segura e auditável: trabalho local, envio ao remoto, abertura/revisão de PRs e uso da API/CLI sem vazar tokens.

## Quando usar

- Criar ou atualizar **branch**, **PR**, **draft PR**, **review**, **merge**.
- Listar **issues**, comentar, etiquetar (quando houver permissão).
- **Fork**, **remote**, sincronizar `upstream`.
- Diagnosticar **falhas de CI** ligadas a workflows (ler logs via UI ou `gh run`).
- Ligar repositório a integrações (Paperclip, etc.) — apenas orientação; credenciais ficam fora do cérebro.

## Pré-requisitos

- `git` instalado; repositório com `origin` apontando para GitHub.
- **GitHub CLI** `gh` (preferido para PRs, issues, runs): [https://cli.github.com](https://cli.github.com)
- Autenticação: `gh auth login` (HTTPS ou SSH conforme o time). Não pedir nem armazenar PAT em ficheiros do brain.

## Segurança (obrigatório)

- **Nunca** commitar: tokens, `workstation/paperclip/.env`, chaves SSH privadas, passwords.
- Seguir `empresa/contexto/07-CONTEXT-SECURITY.md` e `empresa/contexto/06-AGENT-PROTOCOLS.md` para escopo e commits neste repositório.
- Se um comando precisar de secret (Actions, deploy), usar **GitHub Secrets** ou variáveis do ambiente do utilizador — não inline no Markdown do cérebro.

## Fluxo recomendado: branch → commit → push → PR

1. Confirmar **cwd** no repositório certo e `git status` limpo ou intencional.
2. Criar branch descritiva: `git checkout -b tipo/descricao-curta` (ex.: `fix/ajuste-map`, `feat/skill-github`).
3. Commits **pequenos e focados**; mensagem clara (português ou inglês, alinhado ao repo).
4. `git push -u origin <branch>`.
5. Abrir PR:
   - `gh pr create --fill` ou `gh pr create --title "..." --body "..."`.
6. Aguardar CI; se falhar, `gh run list` / `gh run view <id> --log-failed` quando aplicável.

## Revisão e merge

- **Revisor**: comentários por linha na UI ou `gh pr review`.
- **Merge**: respeitar regras do repo (squash, rebase, required checks). Preferir **squash** quando o histórico do `main` deve ficar linear, se for política do time.
- Não fazer **force push** em branches partilhadas sem acordo explícito do utilizador.

## Issues e project boards

- Criar issue: `gh issue create` (título/corpo claros; referenciar PRs com `Closes #n` quando fechar automaticamente).
- Etiquetas e milestones: usar nomes existentes no repo; não inventar processo novo sem pedido.

## Fork e upstream

```bash
git remote add upstream https://github.com/org/repo-original.git
git fetch upstream
git checkout main
git merge upstream/main   # ou rebase, conforme convenção do projeto
```

## CI / Actions (visão geral)

- Workflows em `.github/workflows/*.yml` — alterações exigem entender impacto em todos os branches.
- Para inspeção rápida: `gh workflow list`, `gh run list --workflow=nome.yml`.

## O que não fazer

- Apagar remoto (`git push --force` para `main`/`master`) sem instrução explícita.
- Criar repositórios ou transferir ownership sem confirmação humana.
- Assumir org/team `CODEOWNERS` — ler o ficheiro no repo se existir.

## Referências no brain

- Commits e escopo: `empresa/contexto/07-CONTEXT-SECURITY.md`
- Protocolos de escrita: `empresa/contexto/06-AGENT-PROTOCOLS.md`

## Comandos `gh` úteis (cola rápida)

| Ação | Comando |
|------|---------|
| Estado auth | `gh auth status` |
| PR atual | `gh pr status` |
| Ver PR | `gh pr view --web` |
| Checks | `gh pr checks` |
| Lista runs | `gh run list --limit 10` |
| Clonar org | `gh repo clone org/repo` |

Para detalhes oficiais: `gh help` e [documentação GitHub CLI](https://cli.github.com/manual/).
