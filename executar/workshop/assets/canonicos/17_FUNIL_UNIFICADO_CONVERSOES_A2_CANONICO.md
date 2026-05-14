# Funil Unificado (A-2) — Canônico
**Atualizado:** 2026-04-30  
**Fonte final:** consolidação em `assets/canonicos`; base canônica original + `assets/legacy/merge/skills/04-funil-unificado-a2.md`.  
**Decisão de merge:** skill 04 já estava promovida; `assets/canonicos` mantém o formato operacional canônico sem duplicar conteúdo.


Status: v1  
Escopo: definição única do fluxo lead (Marketing + Vendas), conversões e fonte da verdade por etapa  
Objetivo: permitir tracking, CRM e otimização sem vocabulários concorrentes entre áreas.

---

## Nome e propósito

- **Nome canônico:** Funil Unificado (A-2)
- **Propósito (1 frase):** definir o fluxo end-to-end do lead (geração → venda/drop), com etapas e definições únicas (Marketing + Vendas) para que tracking, gestão e otimização tenham uma fonte da verdade.

---

## Quando usar / quando não usar

- **Quando usar:**
  - antes de finalizar o Plano de Mídia (para garantir que as conversões “que importam” existem e são rastreáveis)
  - antes de implementar tracking/CRM como fonte da verdade
  - quando há conflito de definições (“cada área mede um funil diferente”)
- **Quando não usar:**
  - para redesenhar organograma; o foco é fluxo, definições e evidência

---

## Entradas (Inputs)

- Plano de Mídia (canais/campanhas e evento de conversão pretendido).
- DEOC / DEOC (ICP + anti-ICP operacional, persona, mensageria e proposta).
- AS IS do cliente:
  - processo comercial e etapas atuais
  - estrutura do time (papéis e responsabilidades)
  - ferramentas (CRM + formulários + tracking)
- Benchmarking (padrões do segmento e referências de conversão por etapa).

## Saídas (Outputs)

- Funil unificado v1 contendo:
  - etapas (nome + definição) do primeiro clique até fechamento/drop
  - evento de conversão por etapa (o que “conta”)
  - taxa de conversão “aceitável” por etapa (faixas) baseada em benchmark + contexto do cliente
  - fonte da verdade por etapa (onde o dado vive)
  - campos mínimos obrigatórios no CRM (e/ou sistema equivalente)
  - pontos de handoff (links com o Protocolo de handoff)

---

## Passo a passo

1) Definir objetivo do funil (qual conversão final importa e qual “lead correto”).
2) Mapear AS IS (Marketing e Vendas): como o lead nasce, como é atendido, onde cai, onde some.
3) Desenhar TO BE (etapas propostas) e alinhar nomes/definições (um vocabulário único).
4) Para cada etapa:
   - definição do que é “passou”
   - evidência mínima (auditável)
   - faixa de conversão aceitável (verde/amarelo/vermelho) com fonte (benchmark/histórico)
   - fonte da verdade (CRM, planilha, plataforma — escolher 1)
   - campos mínimos obrigatórios
5) Definir quais eventos precisam existir no tracking para sustentar o funil.
6) Validar coerência com capacidade do time e ciclo de venda (evitar “funil impossível de operar”).
7) Publicar como artefato e abrir backlog de gaps (campos, integrações, treinamento, adoção).

---

## Componentes críticos (o que iterar)

- Definições operacionais de etapa (passa/não passa) vs “nome bonito”.
- Fonte da verdade por etapa (evitar “planilha paralela”).
- Campos mínimos (poucos e essenciais) vs burocracia impossível de usar.
- Coerência com Plano de Mídia (o tracking mede o que o funil exige).
- Coerência com capacidade e ciclo (funil tem que caber na operação real).

---

## Template(s)

- `./assets/canonicos/templates/asset-skill.md`
- `./assets/canonicos/templates/processo-loop.md`

---

## Exemplo real

> **Lacuna:** exemplo real de Funil Unificado (com etapas e campos) ainda não está versionado neste diretório.

---

## Definição de pronto (DoD)

- Etapas nomeadas e definidas (Marketing + Vendas concordam).
- Fonte da verdade definida por etapa (com 1 sistema preferencial).
- Campos mínimos obrigatórios por etapa (com definição de preenchimento).
- Handoffs identificados e linkados ao Protocolo de handoff.
- Backlog de implementação (tracking/campos/integrações/adoção) criado e priorizado.

---

## Como gerenciar (Gerenciado)

- **Métrica(s) / KPI(s):** % leads com status válido; % campos mínimos preenchidos; tempo de ciclo por etapa.
- **Thresholds (verde/amarelo/vermelho):**
  - vermelho: discrepância entre fontes (CRM ≠ relatório ≠ planilha) ou etapas “sem dono”
  - amarelo: muita etapa e pouco dado confiável (baixa adesão)
  - verde: funil operando com rastreio mínimo e aderência do time
- **Cadência de revisão:** quinzenal (até estabilizar) e mensal (depois), com registro de mudanças.
- **Dono:** (lacuna)
- **Registro obrigatório:** change log do funil (o que mudou, por quê, impacto esperado/observado).
