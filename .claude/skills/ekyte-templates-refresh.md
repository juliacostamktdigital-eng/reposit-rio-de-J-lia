---
name: ekyte-templates-refresh
description: Gerencia o diretório clientes/_skill-ekyte/briefing-templates/ — adicionar templates novos por sigla, ajustar existentes, atualizar arquivos compartilhados. Sempre exige diff antes de salvar.
user-invocable: true
---

# /ekyte-templates-refresh — Manutenção dos templates de briefing

Gerencia `clientes/_skill-ekyte/briefing-templates/` com templates por sigla usados pela `/ekyte-briefing`.

## Quando invocar

- `/ekyte-templates-refresh` diretamente
- Criar template para sigla nova (ex: KV, MT, EM, EV)
- "ajusta o template de CA" — adicionar/remover seções
- Após 5+ tasks reais, refinar perguntas/campos

## Estrutura do diretório

```
briefing-templates/
├── _header-universal.md    ← cabeçalho padrão (afeta todos)
├── _base-criativo.md       ← base para criativos (afeta CA, KV, RV…)
├── _5w1h.md                ← estrutura 5W1H (afeta planos de ação)
├── CA.md                   ← Criativo Ads
├── LP.md                   ← Landing Page
├── KV.md                   ← Key Visual
├── RV.md                   ← Roteiro de Vídeo
├── PC.md                   ← Plano de Conteúdo
├── AN.md                   ← Anúncio
└── CRM.md                  ← CRM / Automação
```

## Fluxo

**Passo 1:** Identificar operação (adicionar novo, ajustar existente, atualizar compartilhado, listar)

**Passo 2 (Novo):** Coletar sigla, tipo de tarefa, task_type_id e família (Criativo, Operacional, Analítica, CRM)

**Passo 3 (Ajuste):** Determinar tipo de mudança (adicionar seção, remover, modificar, reordenar)

**Passo 4 (Compartilhado):** Avisar sobre impacto em múltiplos templates antes de aplicar

**Passo 5:** Sempre mostrar diff antes de salvar, com confirmação

## Padrão de conversão Markdown → texto Ekyte

Templates são em Markdown, mas a saída para Ekyte deve ser texto plano:
- `## Seção` → `SEÇÃO` em caixa alta
- `- item` → `• item`
- Sem tags HTML, sem `<div>`, sem `<p>`

## O que NÃO fazer

- Não modificar `drives.md`, `backups-crm.md` ou `cache.md`
- Não criar templates sem validar família primeiro
- Não criar duplicatas sem confirmação
- Não incluir KV em templates analíticos/operacionais
- Diff obrigatório antes de qualquer escrita
