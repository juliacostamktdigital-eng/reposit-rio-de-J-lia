# Skill: status-report — v1.0.0

> owner: gestor-de-projeto | status: active | published: 2026-04-06

---

## Instrução

Você é o Gestor de Projeto emitindo o relatório de status do sprint. Seja direto — o Coordenador precisa saber rapidamente o que está bem, o que está em risco e o que precisa de decisão.

## Legenda de status

| Símbolo | Status |
|---------|--------|
| ✅ | Concluído |
| 🔄 | Em andamento — no prazo |
| ⚠️ | Em andamento — atenção necessária |
| ❌ | Atrasado ou bloqueado |
| 🔲 | Não iniciado |

## Documento de status report

```
# Status Report — Sprint [N] — [Cliente]
Data: [data]
Gestor: [nome]
Sprint: [data início] – [data fim]

---

## Resumo executivo

[2–3 frases: como está o sprint no geral? No prazo? Riscos? Destaques?]

Status geral: 🟢 No prazo | 🟡 Atenção | 🔴 Em risco

---

## Status por task

| # | Task | Agente | Prazo | Status | Observação |
|---|------|--------|-------|--------|-----------|
| 1 | [task] | [agente] | [data] | ✅ | — |
| 2 | [task] | [agente] | [data] | 🔄 | 60% concluído |
| 3 | [task] | [agente] | [data] | ⚠️ | Aguardando aprovação do cliente |
| 4 | [task] | [agente] | [data] | ❌ | Bloqueado: falta acesso ao CRM |

---

## Bloqueios e riscos

| Item | Descrição | Impacto | Ação necessária | Responsável |
|------|-----------|---------|-----------------|-------------|
| [item] | [o que está bloqueando] | [no prazo do sprint | no prazo do cliente] | [o que precisa acontecer] | [quem deve agir] |

---

## Concluído desde o último check-in

- ✅ [task concluída]
- ✅ [task concluída]

## Próximas entregas (próximos 3 dias)

- [task] — [agente] — [prazo]
- [task] — [agente] — [prazo]

---

## Itens que precisam de decisão

- [item que requer decisão do Coordenador ou Gerente]
```

## Regras

- Emita o status report **antes do report consolidado do Coordenador**
- **Não omita tarefas atrasadas** — identificar cedo é melhor que surpreender o cliente
- Se há bloqueio externo (cliente não aprovou, acesso não veio), sinalize imediatamente
- Um ❌ sem plano de recuperação não é aceitável — sempre inclua a ação necessária
