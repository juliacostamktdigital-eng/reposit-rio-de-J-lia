---
name: ekyte-briefing-refresh
description: Atualiza drives.md e backups-crm.md usados pela skill /ekyte-briefing — adiciona novos clientes, altera links de Drive ou planilhas de backup CRM.
user-invocable: true
---

# /ekyte-briefing-refresh — Atualizar drives e backups CRM

Mantém dois arquivos em `clientes/_skill-ekyte/`: `drives.md` (links de Google Drive por cliente) e `backups-crm.md` (planilhas de backup CRM).

## Quando usar

- Cliente novo entra no sistema
- Link de Drive precisa ser alterado ou adicionado
- Planilha de backup CRM é criada ou atualizada
- `/ekyte-briefing-refresh` invocado diretamente

## Fluxo

**Passo 1:** Perguntar qual tipo de atualização (Drive, Backup CRM, ou ambos)

**Passo 2 (Drive):** Exibir lista de clientes com links atuais → selecionar ou adicionar novo

**Passo 3 (Backup CRM):** Listar clientes com status atual → solicitar novo link

**Passo 4:** Mostrar diff (antes/depois) para confirmação antes de salvar

## Regras críticas

- Validar que URLs de Drive contêm `drive.google.com`
- Avisar quando cliente novo é adicionado fora dos fixos — `cache.md` também pode precisar de atualização
- Nunca modificar arquivos de template (`briefing-templates/`) — essa responsabilidade é da `/ekyte-templates-refresh`
- Não alterar `cache.md` diretamente

## Resultado esperado

Relatar as modificações salvas com confirmação dos arquivos afetados.
