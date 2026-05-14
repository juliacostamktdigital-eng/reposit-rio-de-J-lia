---
slug: brain-v4-colli-workflow-v1
name: brain-v4-colli-workflow-v1
description: "Permite que qualquer membro do time contribua com o repositório `brain_v4_colli`"
---

# Skill: brain_v4_colli — Workflow de Colaboração (GitHub)

Permite que qualquer membro do time contribua com o repositório `brain_v4_colli`
sem precisar conhecer Git. Claude executa as operações Git por baixo dos panos.
Expõe apenas 3 comandos: **começar**, **ver status**, **submeter**.

---

## Quando Usar

**Acionar esta skill quando o usuário disser:**
- "começar alteração", "criar branch", "iniciar contribuição sobre [tema]"
- "ver status", "o que mudei", "o que está diferente"
- "submeter", "abrir PR", "enviar para revisão", "mandar para aprovação"

**Não usar esta skill para:**
- Merge de Pull Requests → orientar o usuário a fazer pelo GitHub
- Rebase ou resolução de conflitos avançados → parar, explicar o problema, pedir ajuda do responsável
- Qualquer operação que não seja uma das 3 fases definidas abaixo

---

## Pré-requisitos (verificar antes de qualquer fase)

Antes de executar qualquer operação, verificar:

1. `git` está instalado → rodar `git --version`
2. `gh` está instalado e autenticado → rodar `gh auth status`
   - Se não autenticado: orientar o usuário a rodar `gh auth login` e parar
3. Está dentro de um repositório Git → rodar `git rev-parse --show-toplevel`
4. O repositório remoto é `brain_v4_colli` → verificar `git remote -v`

Se qualquer pré-requisito falhar: explicar o problema em linguagem simples e parar.

---

## Processo de Execução

### FASE 1 — COMEÇAR

**Trigger:** "começar alteração sobre [tema]", "quero criar uma branch", "iniciar contribuição"

```
Step 1.1 — Verificar pré-requisitos (conforme seção acima)

Step 1.2 — Verificar estado atual do workspace
  Executar: git status
  → Se houver alterações não commitadas:
      Parar e perguntar: "Você tem alterações não salvas. Quer revisar antes de começar uma nova contribuição?"
      Não prosseguir sem resposta do usuário.
  → Se estiver em branch diferente de main:
      Perguntar: "Você está na branch [X]. Quer criar uma branch nova a partir daqui ou voltar para a main primeiro?"

Step 1.3 — Coletar informações
  → Se o usuário não informou o assunto: perguntar "Sobre o que é essa alteração? (ex: cliente-x, revisao-wiki)"
  → Usar o nome do usuário Git configurado localmente como identificador padrão

Step 1.4 — Executar o script de início
  Executar: bash .claude/skills/brain-v4-colli-workflow-v1/scripts/start.sh <usuario> <assunto>

  Interpretar saída:
  - OK:BRANCH_CREATED:<branch>   → informar ao usuário o nome da branch criada
  - ERROR:GH_NOT_AUTH            → orientar a rodar "gh auth login"
  - ERROR:UNCOMMITTED_CHANGES    → informar que há alterações pendentes e parar

Step 1.5 — Confirmar ao usuário
  Dizer: "Tudo pronto. Você está na branch contrib/<usuario>/<assunto>-<data>. Pode trabalhar normalmente."
```

---

### FASE 2 — VER STATUS

**Trigger:** "ver status", "o que mudei", "o que está diferente", "quais arquivos alterei"

```
Step 2.1 — Executar o script de status
  Executar: bash .claude/skills/brain-v4-colli-workflow-v1/scripts/status.sh

Step 2.2 — Interpretar a saída e traduzir para linguagem simples
  - SUMMARY:CHANGED=X:NEW=Y      → "Você alterou X arquivo(s). Criou Y arquivo(s) novo(s)."
  - FILES:<lista>                → listar os arquivos em formato legível
  - WARNING:PROTECTED_AREA:<area> → "⚠️ Atenção: esta alteração toca a área [X], que exige aprovação do responsável."

Step 2.3 — Apresentar resumo claro
  Exemplo de saída para o usuário:
  ---
  📋 Status atual:
  - 2 arquivos alterados
  - 1 arquivo novo

  Arquivos:
  - wiki/clientes/cliente-x.md (alterado)
  - inputs/reunioes/reuniao-2026-05.md (alterado)
  - wiki/processos/novo-processo.md (novo)

  ✅ Nenhuma área crítica foi tocada.
  ---
```

---

### FASE 3 — SUBMETER

**Trigger:** "submeter", "enviar para revisão", "abrir PR", "mandar para aprovação"

```
Step 3.1 — Verificar pré-requisitos (conforme seção acima)

Step 3.2 — Mostrar resumo do que será submetido
  Executar: bash .claude/skills/brain-v4-colli-workflow-v1/scripts/status.sh
  Apresentar lista de arquivos que serão incluídos no commit.

Step 3.3 — Pedir confirmação explícita ANTES de qualquer commit
  Perguntar: "Confirma que quer submeter essas alterações? Responda sim ou não."
  → Se não: cancelar completamente e aguardar nova instrução
  → Se sim: continuar

Step 3.4 — Coletar título e descrição
  → Perguntar: "Qual é o título desta contribuição?" (ou sugerir com base nos arquivos alterados)
  → Perguntar: "Quer adicionar uma descrição? (opcional)"

Step 3.5 — Executar o script de submissão
  Executar: bash .claude/skills/brain-v4-colli-workflow-v1/scripts/submit.sh "<titulo>" "<descricao>"

  Interpretar saída e comunicar ao usuário conforme o tipo:

  - OK:AUTO_MERGED:<url>
    → "/inputs/ detectado. Alteração mesclada diretamente — nenhuma aprovação necessária."
    → Não mostrar o link do PR (já está merged e fechado)

  - OK:PR_CONTENT:<url>
    → "PR criado. O consultor foi notificado para revisão."
    → Mostrar link: <url>
    → "Aguarde a aprovação antes de usar este conteúdo como insumo."

  - OK:PR_CRITICAL:<url>
    → "⚠️ Esta alteração toca uma área crítica. PR criado para aprovação do coordenador."
    → Mostrar link: <url>
    → "Não prossiga com mudanças dependentes desta área até a aprovação."

  - ERROR:DIRECT_PUSH_TO_MAIN    → "Não é possível submeter direto na main. Crie uma branch primeiro."
  - ERROR:NOTHING_TO_COMMIT      → "Não há alterações para submeter."
```

---

## 🛑 Regras de Ouro — Segurança

**NUNCA executar:**
- `git push --force` ou `git push -f`
- `git reset --hard`
- `git clean -f` ou `git clean -fd`
- `gh pr merge`
- `rm -rf` sem confirmação explícita do usuário

**NUNCA:**
- Fazer push direto para `main`
- Fazer merge automático de qualquer PR
- Alterar `.github/` sem alerta explícito ao usuário
- Alterar `.claude/` sem alerta explícito ao usuário
- Deletar arquivos sem confirmação explícita
- Avançar da Fase 3 sem confirmação explícita (Step 3.3 é obrigatório)

**SE houver conflito de merge:**
Parar completamente. Explicar em linguagem simples:
"Sua branch tem um conflito com alterações que já estão no repositório. Isso precisa ser resolvido manualmente. Chame o responsável técnico."

**SE `gh` não estiver autenticado:**
"Para continuar, você precisa autenticar o GitHub CLI. Rode o comando: `gh auth login` e siga as instruções. Depois me avise para continuar."

---

## Áreas e Fluxos

| Área | Fluxo | Revisor | Sinal do script |
|---|---|---|---|
| `/inputs/` | Auto-merge direto | Ninguém | `OK:AUTO_MERGED` |
| `/wiki/`, `/projetos/`, `/mapa/` | PR criado | Consultor | `OK:PR_CONTENT` |
| `/.claude/`, `/schema/`, `/decisoes/`, `.github/` | PR criado | Coordenador | `OK:PR_CRITICAL` |

**Regra de prioridade:** se um commit tocar áreas de níveis diferentes, o nível mais alto prevalece.
Exemplo: `/inputs/` + `/.claude/` → fluxo crítico (coordenador).

---

## Formato de Saída Obrigatório

Sempre comunicar ao usuário em português claro. Nunca exibir saída bruta de terminal.
Usar emojis apenas para sinalizar status: ✅ sucesso, ⚠️ atenção, ❌ erro.

Exemplo de resposta ao final da Fase 1:
```
✅ Branch criada com sucesso!

Você está agora na branch: contrib/joao/revisao-wiki-20260504

Pode trabalhar normalmente nos arquivos. Quando terminar, diga "ver status" para revisar
o que foi alterado, ou "submeter para revisão" para abrir o Pull Request.
```

Exemplo de resposta ao final da Fase 3:
```
✅ Pull Request criado com sucesso!

Título: Revisão da wiki de clientes
Link: https://github.com/org/brain_v4_colli/pull/42

O merge será feito pelo responsável após aprovação. Você receberá uma notificação pelo GitHub.
```
