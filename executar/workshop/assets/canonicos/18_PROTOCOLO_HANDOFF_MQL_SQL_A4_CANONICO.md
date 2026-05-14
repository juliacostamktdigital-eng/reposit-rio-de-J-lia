# Protocolo de Handoff MQL/SQL (A-4) — Canônico
**Atualizado:** 2026-04-30  
**Fonte final:** consolidação em `assets/canonicos`; base canônica original + `assets/legacy/merge/skills/05-protocolo-handoff-a4.md`.  
**Decisão de merge:** skill 05 já estava promovida; `assets/canonicos` mantém o protocolo A-4 como fonte principal e referencia CRM/SLA como complemento.


Status: v1  
Escopo: handoffs Marketing→Vendas, em especial MQL → SQL  
Objetivo: critérios, evidência e cadência para fechar o loop inter-áreas sem “guerra de lead”.

**Relação com:** `07_CRM_HANDOFF_SLA_MARKETING_VENDAS_CANONICO.md` — este documento é o recorte **skill/A-4** (definições e DoD); o 07 permanece o consolidado de CRM, SLA e operação.

---

## Nome e propósito

- **Nome canônico:** Protocolo de Handoff (A-4)
- **Propósito (1 frase):** definir e operar os handoffs (principalmente **MQL → SQL**) com critérios, evidência e cadência, para fechar loop inter-áreas sem “guerra de lead”.

---

## Quando usar / quando não usar

- **Quando usar:**
  - sempre que houver handoff Marketing→Vendas (quase sempre)
  - quando “lead ruim” e “vendas não atende” vira conflito recorrente
  - quando o funil tem etapas ambíguas (MQL/SQL sem definição)
- **Quando não usar:**
  - como cerimônia sem consequência (ritual que não muda nada não fecha Gerenciado)

---

## Entradas (Inputs)

- Funil Unificado (etapas, fonte da verdade e campos mínimos).
- DEOC / DEOC (ICP/anti-ICP; mensageria e promessa).
- Plano de Mídia (o que está sendo prometido e para quem).
- Capacidade e SLA do time comercial (quem atende, quando, por qual canal).
- Benchmarking (referências de conversão e expectativas realistas por etapa).

## Saídas (Outputs)

- Protocolo de handoff v1 com:
  - definição operacional de **MQL** e **SQL** (passa/não passa)
  - critérios de aceitação/rejeição (com motivo padronizado)
  - campos mínimos obrigatórios no CRM para registrar o handoff
  - SLA de atendimento e regra de redistribuição (quando estoura)
  - cadência do loop (revisão + ações) e evidências mínimas

---

## Passo a passo

1) Fixar o que é lead “correto” (ICP + anti-ICP operando).
2) Definir MQL e SQL como eventos/estados no Funil Unificado:
   - condição de entrada
   - evidência mínima
3) Definir critérios de aceitação/rejeição (e motivos) no CRM.
4) Definir SLA e responsabilidades (quem atende; em quanto tempo; o que fazer se não atender).
5) Definir a rotina de revisão:
   - quais KPIs (taxas por etapa + tempo)
   - thresholds (verde/amarelo/vermelho)
   - o que muda quando piora (ação definida)
6) Implementar o registro obrigatório (rastro) e auditar aderência.

---

## Componentes críticos (o que iterar)

- Definição de MQL/SQL com critério e evidência vs “nome subjetivo”.
- Motivos padronizados de rejeição (para virar insumo de melhoria).
- SLA realista + enforcement (sem SLA, o handoff vira ruído).
- Rotina decisória (o que muda quando a taxa piora) vs leitura de número.
- Loop de ajuste (Marketing muda segmentação/mensagem/oferta com base no dado de handoff).

---

## Template(s)

- `./assets/canonicos/templates/asset-skill.md`
- `./assets/canonicos/templates/processo-loop.md`

---

## Exemplo real

> **Lacuna:** exemplo real de Protocolo de handoff (MQL→SQL) ainda não está versionado neste diretório.

---

## Definição de pronto (DoD)

- MQL e SQL definidos com passa/não passa e evidência mínima.
- Campos e motivos padronizados no CRM (ou sistema equivalente).
- SLA definido e comunicado (com regra de exceção).
- KPIs e thresholds definidos + ação definida por faixa.
- Rotina de revisão com registro (ata/card) e change log de ajustes.

---

## Como gerenciar (Gerenciado)

- **Métrica(s) / KPI(s):** taxa MQL→SQL; taxa SQL→Venda; tempo de 1º contato; % rejeições por motivo; % leads sem status.
- **Thresholds (verde/amarelo/vermelho):** definidos por contexto e benchmark (documentar fonte).
- **Cadência de revisão:** semanal (operacional) + mensal (estrutural).
- **Dono:** (lacuna)
- **Registro obrigatório:** ata/card com decisões + change log de mudanças (segmentação, mensagem, processo).
