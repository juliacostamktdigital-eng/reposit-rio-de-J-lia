---
slug: ee-s4-00-guia-comercial-v1
name: ee-s4-00-guia-comercial-v1
description: "POP do track comercial Saber E.E — Semana 4. Define pré-requisitos, as duas fases (Campo e Análise), sequência de skills, I/O de context files e output pack para S5. Acione quando o consultor for iniciar S4 ou tiver dúvida de por onde começar no diagnóstico comercial."
week: 4
estimated_time: "5 min (orientação)"
---

# POP — Track Comercial (Semana 4)

## Pré-requisitos para iniciar S4

S4 só começa com todos os itens abaixo validados:

- [ ] `outputs/definicao-icp-b2b.json` — ICP validado (S2)
- [ ] `context/business.md` — status `[VALIDADO]`
- [ ] `context/gtm.md` — status `[VALIDADO]`
- [ ] S3 concluído — pelo menos Meta Ads e Google Ads diagnosticados

---

## Visão geral do track

S4 tem **duas fases distintas** com naturezas operacionais diferentes:

| Fase | Onde acontece | Quem executa | Objetivo |
|---|---|---|---|
| **Fase 1 — Campo** | Junto ao cliente | Consultor (manual) | Coletar dados reais: entrevistas, CRM, scripts, conversas |
| **Fase 2 — Análise** | Back-office | IA + consultor | Processar o que foi coletado e gerar diagnóstico |

---

## FASE 1 — Campo

### Passo 1 — Cliente Oculto ← fazer ANTES de comunicar ao time

Executar o cliente oculto **antes** de iniciar as entrevistas formais. O time ainda não está "ligado" e o comportamento é o mais natural possível. Só comunicar que o diagnóstico começa depois disso.

→ `/v4-skills:e.e:ee-s4-03-cliente-oculto-v1`

> **Nota:** `ee-s4-03` pode ser executado apenas com o ICP e o contexto do kickoff — o `diagnostico-comercial-crm.json` ainda não existe neste momento e isso é esperado.

### Passo 2 — Kit de Entrevistas

Antes de entrar nas reuniões, gerar o roteiro personalizado de perguntas por papel. O kit é baseado no contexto do cliente (business.md, gtm.md, constraints.md, ICP de S2) e nas hipóteses levantadas nos diagnósticos de S3.

→ `/v4-skills:e.e:ee-s4-00-kit-entrevista-comercial-v1`

### Passo 3 — Entrevistas + Coleta (MANUAL)

O consultor executa as entrevistas com os membros da equipe comercial relevantes (gestor, vendedor, SDR, pós-venda — quem for pertinente ao processo desse cliente). Não há um número fixo de pessoas — entrevistar quem tiver papel real no ciclo de vendas.

**Materiais a obter durante as entrevistas:**
- [ ] Acesso ao CRM — ou prints das últimas 30 oportunidades (abertas + fechadas)
- [ ] Export de negócios dos últimos 12 meses (valor + segmento + canal + data)
- [ ] 5–10 conversas reais (WhatsApp ou email) — idealmente 3 ganhos + 3 perdidos
- [ ] Script ou roteiro de vendas (formal ou informal — o que geralmente usam)
- [ ] Lead Response Time médio (pode ser estimativa do gestor)
- [ ] Cadência de contato atual (quantas tentativas, em que intervalo)

---

## FASE 2 — Análise

Executar em sequência após ter todos os materiais coletados:

### Passo 4 — Diagnóstico Comercial — CRM (ee-s4-01)

Lê: `context/business.md`, `context/gtm.md`, `outputs/definicao-icp-b2b.json`
Atualiza: `context/constraints.md` (gargalos reais identificados no processo)
Produz: `diagnostico-comercial-crm.json`

→ `/v4-skills:e.e:ee-s4-01-diagnostico-comercial-crm-v1`

### Passo 5 — Análise CRM & Receita (ee-s4-02)

Lê: `context/business.md`, `outputs/diagnostico-comercial-crm.json`, `outputs/definicao-icp-b2b.json`
Atualiza: `context/business.md` (ICP real confirmado ou corrigido vs ICP declarado)
Produz: `analise-crm-receita.json`

→ `/v4-skills:e.e:ee-s4-02-analise-crm-receita-v1`

---

## Tabela de I/O — context files

| Skill | Lê de context/ | Atualiza context/ | Output |
|---|---|---|---|
| `ee-s4-03` (campo) | — | `constraints.md` (atendimento real) | `cliente-oculto.json` |
| `ee-s4-01` (análise) | `business.md`, `gtm.md` | `constraints.md` (gargalos de processo) | `diagnostico-comercial-crm.json` |
| `ee-s4-02` (análise) | `business.md` | `business.md` (ICP real vs declarado) | `analise-crm-receita.json` |

---

## Critério de encerramento de S4

S4 está concluída quando **todos** os itens estão validados:

- [ ] `cliente-oculto.json` validado pelo consultor
- [ ] `diagnostico-comercial-crm.json` validado
- [ ] `analise-crm-receita.json` validado
- [ ] `context/constraints.md` atualizado com gargalos reais (atendimento + processo)
- [ ] `context/business.md` atualizado com ICP real confirmado pelo CRM

Registrar conclusão com `coringa-sx-03` (changelog).

---

## Output pack de S4 → S5

| Output de S4 | Consome em S5 |
|---|---|
| `diagnostico-comercial-crm.json` | ee-s5-01 (drawflow — bloqueadores de conversão), ee-s5-02 (GTM — canais por Win Rate) |
| `analise-crm-receita.json` | ee-s5-02 (GTM — priorização de ICP), ee-s5-03 (forecast — ticket real) |
| `cliente-oculto.json` | ee-s5-02 (GTM — calibrar CTA e timing), ee-s5-04 (deck — evidência de atendimento) |
| `context/constraints.md` (atualizado) | ee-s5-01 (drawflow — restrições reais do processo) |
| `context/business.md` (ICP real) | ee-s5-02, ee-s5-03 |

---

## Skills de apoio (não product steps)

Estas skills existem mas **não fazem parte do pipeline de produto** — são ferramentas de apoio que o consultor pode invocar a qualquer momento:

| Skill | Quando usar |
|---|---|
| `sales-ops-consulting` | Para pensar a hipótese causal antes de iniciar S4, validar diagnóstico com raciocínio mais profundo, ou discutir um problema comercial ad-hoc fora do fluxo estruturado |
| `sales-enablement` | Após S4, se o cliente precisar de materiais de capacitação (playbooks, objection docs, scripts de venda) — não é output padrão do E.E, mas pode ser entregável adicional acordado |
