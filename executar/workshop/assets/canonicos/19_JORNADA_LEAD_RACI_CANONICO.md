# Jornada do Lead + RACI — Canônico
**Atualizado:** 2026-04-30  
**Fonte final:** consolidação em `assets/canonicos`; base canônica original + `assets/legacy/merge/skills/06-jornada-lead-raci.md`.  
**Decisão de merge:** skill 06 já estava promovida; `assets/canonicos` mantém jornada/RACI como fonte final.


Status: v1  
Escopo: touchpoints da jornada do lead e responsabilidades por etapa  
Objetivo: governança do Funil Unificado e do Protocolo de handoff com donos e evidência mínima.

---

## Nome e propósito

- **Nome canônico:** Jornada do Lead + Responsabilidades (RACI)
- **Propósito (1 frase):** mapear a jornada do lead (touchpoints e decisões) e atribuir responsabilidades por etapa para garantir execução e governança do Funil Unificado e do Protocolo de handoff.

---

## Quando usar / quando não usar

- **Quando usar:**
  - quando o lead “some” entre áreas (ninguém sabe quem era o dono)
  - quando o cliente tem múltiplos papéis e rotas (inbound, outbound, SDR, closer)
  - antes de definir SLA e handoffs
- **Quando não usar:**
  - para “burocratizar” sem impacto; a matriz deve servir o processo e os KPIs

---

## Entradas (Inputs)

- Funil Unificado (etapas e fonte da verdade).
- Protocolo de handoff (pontos de handoff e SLA).
- Estrutura do time (Marketing, Vendas, Atendimento/CS quando aplicável).
- Ferramentas (CRM e canais de contato).

## Saídas (Outputs)

- Jornada do lead (mapa simples) com:
  - etapas do funil e touchpoints principais
  - quem faz o quê em cada etapa
  - evidência mínima gerada por cada responsável
- RACI mínimo por etapa (R/A/C/I).

---

## Passo a passo

1) Listar etapas do Funil Unificado e os touchpoints relevantes.
2) Para cada etapa, definir:
   - **R** (Responsible): quem executa
   - **A** (Accountable): quem responde pelo resultado
   - **C** (Consulted): quem precisa ser consultado
   - **I** (Informed): quem precisa ser informado
3) Definir evidência mínima por etapa (o que deve ficar registrado).
4) Validar contra capacidade real do time e SLA.
5) Publicar como artefato e linkar em Funil Unificado + Protocolo de handoff.

---

## Componentes críticos (o que iterar)

- Clareza de “dono” por etapa (Accountable) vs “todo mundo é dono”.
- Evidência mínima por etapa (rastro) vs dependência de memória.
- SLA por responsável (viável) vs expectativa impossível.
- Integração com o loop de melhoria (quem muda o quê quando piora).

---

## Template(s)

- `./assets/canonicos/templates/asset-skill.md`
- `./assets/canonicos/templates/processo-loop.md`

---

## Exemplo real

> **Lacuna:** exemplo real de Jornada + RACI ainda não está versionado neste diretório.

---

## Definição de pronto (DoD)

- RACI definido para todas as etapas do Funil Unificado.
- Evidência mínima por etapa definida (o que fica no CRM/registro).
- SLA compatível com os responsáveis.
- Links/integração com Funil Unificado e Protocolo de handoff.

---

## Como gerenciar (Gerenciado)

- **Métrica(s) / KPI(s):** % etapas com dono; % violações de SLA; % etapas sem evidência mínima.
- **Thresholds (verde/amarelo/vermelho):**
  - vermelho: etapas sem dono; handoff sem responsável; lead “sumindo”
  - amarelo: dono existe, mas sem evidência; SLA estoura sem ação
  - verde: dono + evidência + ação definida quando estoura
- **Cadência de revisão:** mensal (ou quando trocar estrutura do time).
- **Dono:** (lacuna)
- **Registro obrigatório:** change log do RACI (mudanças por papel e por quê).
