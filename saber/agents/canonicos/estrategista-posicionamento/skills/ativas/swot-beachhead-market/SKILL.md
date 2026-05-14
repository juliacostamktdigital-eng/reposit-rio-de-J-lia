---
name: swot-beachhead-market
description: "Gera Matriz SWOT específica do cliente e define o Beachhead Market com scorecard 0-5 comparando 2-3 segmentos candidatos. Ligação direta com TAM/SAM/SOM: Beachhead é o SOM vencedor. Use quando o operador disser 'SWOT', 'beachhead', 'segmento prioritário', 'forças e fraquezas', ou ao iniciar o POP 3.2."
dependencies:
  - sizing-mercado-tam-sam-som
  - definicao-icp-b2b
  - estudo-concorrentes
outputs: ["swot-beachhead-market.json"]
week: 2
estimated_time: "2h"
ucm: "1 e 2"
---

# Matriz SWOT + Beachhead Market — Posicionamento Estratégico

Você é um estrategista de negócios sênior. Vai criar uma Matriz SWOT que NÃO é genérica — e definir o Beachhead Market: o segmento específico onde o cliente deve concentrar toda a força para ganhar antes de expandir.

> **REGRA DE OURO DA SWOT:** Cada item deve ser específico para ESTE cliente. Se você trocar o nome da empresa e o item ainda fizer sentido para qualquer negócio do setor, está genérico demais. "Atendimento diferenciado" e "equipe qualificada" são genéricos. Refaça.
>
> **BEACHHEAD = DIA D:** A estratégia do Beachhead é "ganhar uma praia, depois avançar". Não é tentar dominar o mercado inteiro — é escolher o segmento onde a chance de vitória é maior e concentrar TUDO ali primeiro. É a operação Dia D (Geoffrey Moore, Crossing the Chasm).

## Dados necessários

1. `client.json` (briefing) — NOME_CLIENTE, SEGMENTO, PRODUTO_SERVICO, DIFERENCIAIS
2. `outputs/sizing-mercado-tam-sam-som.json` — TAM/SAM/SOM por segmento
3. `outputs/definicao-icp-b2b.json` ou `outputs/definicao-persona-b2c.json` — perfil do cliente ideal
4. `outputs/estudo-concorrentes.json` — forças e fraquezas competitivas
5. `outputs/diagnostico-maturidade.json` (se existir) — scores por pilar

Se informações sobre concorrência não estiverem claras, pergunte:
> "Dos concorrentes mapeados, qual é o mais perigoso e por quê? Tem alguma vantagem que o {NOME_CLIENTE} tem e eles não conseguem copiar facilmente?"

---

## PARTE 1: Matriz SWOT

Gere o output da SWOT completo. Consulte os dados dos outputs anteriores — não invente.

### Forças (Strengths) — 4-6 itens INTERNOS POSITIVOS

Para cada força:
- **Título:** frase curta e específica (inclua dado ou evidência)
- **Evidência:** "origem do dado" — de onde vem essa força? (diagnóstico de maturidade, briefing, CRM, anos no mercado)
- **Alavancagem estratégica:** como usar essa força para capturar uma oportunidade?

Anti-padrão: "Qualidade no atendimento" ← genérico
Padrão correto: "Tempo de resposta < 15min no WhatsApp confirmado por 94% de avaliações 5★ no Google" ← específico com evidência

### Fraquezas (Weaknesses) — 4-6 itens INTERNOS NEGATIVOS

Para cada fraqueza:
- **Título:** frase curta e específica
- **Evidência:** dado concreto (score de diagnóstico, taxa de conversão, benchmark)
- **Risco e mitigação:** o que acontece se não for tratada? Como minimizar?

### Oportunidades (Opportunities) — 4-6 itens EXTERNOS POSITIVOS

Para cada oportunidade:
- **Título:** frase específica
- **Por que existe agora:** tendência, gap do concorrente, mudança de comportamento, sazonalidade
- **Como capturar:** ação específica para aproveitar

### Ameaças (Threats) — 4-6 itens EXTERNOS NEGATIVOS

Para cada ameaça:
- **Título:** frase específica
- **Evidência de que é real:** dado de mercado, comportamento de concorrente
- **Mitigação:** como se proteger

### Síntese Estratégica (3 parágrafos)

**Parágrafo 1 — Alavancagem (Forças + Oportunidades):** Como as forças capturam as oportunidades? Esta é a aposta principal.

**Parágrafo 2 — Risco (Fraquezas + Ameaças):** Quais fraquezas, se não tratadas, amplificam as ameaças?

**Parágrafo 3 — Estratégia recomendada:** Em 90 dias, o que este negócio deve priorizar? (ligação direta com o Beachhead)

---

## PARTE 2: Beachhead Market — Scorecard de Segmentos

**O que é o Beachhead:** O segmento específico e pequeno onde o cliente vai concentrar TODA a comunicação e investimento inicial. Não é "para todo mundo" — é "para este segmento específico primeiro, depois expande."

**Ligação com TAM/SAM/SOM:** O Beachhead é o SOM operacional. O segmento vencedor do scorecard é exatamente o mercado capturável no SOM que foi calculado.

### Identificar 2-3 Segmentos Candidatos

Com base no ICP, nos dados de CRM (clientes que mais compraram) e no estudo de concorrentes, identifique 2-3 segmentos candidatos. Ex:
- Segmento A: Indústrias de automação B2B no Sudeste com 50-200 funcionários
- Segmento B: Distribuidoras de equipamentos B2B com gestão de representantes
- Segmento C: Serviços técnicos de manutenção industrial contratados por licitação

### Scorecard de Decisão (0-5 por critério)

| Critério | Peso | Segmento A | Segmento B | Segmento C |
|----------|------|-----------|-----------|-----------|
| **Urgência da dor** | Alta | /5 | /5 | /5 |
| **Capacidade de pagar** | Alta | /5 | /5 | /5 |
| **Facilidade de acesso** | Média | /5 | /5 | /5 |
| **Tamanho do segmento** | Média | /5 | /5 | /5 |
| **Densidade competitiva** (menor = melhor) | Alta | /5 | /5 | /5 |
| **Alinhamento com forças** | Alta | /5 | /5 | /5 |
| **TOTAL PONDERADO** | | **/30** | **/30** | **/30** |

**Escala por critério:**
- 5 = Excepcional (ex: Urgência muito alta, pain crítica agora)
- 3 = Adequado (ex: Capacidade de pagar compatível com ticket)
- 1 = Limitado (ex: Muitos concorrentes fortes no segmento)

### Segmento Vencedor — O Beachhead

**Segmento escolhido:** {nome}

**Justificativa executiva (3-4 linhas):** por que este segmento em vez dos outros? Conecte com: urgência da dor + capacidade de pagar + alinhamento com forças do cliente.

**Ligação com SOM:** Cruzar com o TAM/SAM/SOM: o Beachhead representa qual % do SAM? O tamanho do segmento é suficiente para sustentar a meta financeira do cliente?

**Risco do Beachhead pequeno demais:** se o segmento for muito pequeno para atingir a meta → apontar explicitamente e recomendar ajuste ou expansão planejada para segmento secundário.

**Implicação para comunicação:** toda a comunicação (anúncios, copy, LP) a partir de agora deve ser escrita para ESTE segmento específico. Não para "todo mundo".

### Ações Prioritárias derivadas da SWOT + Beachhead (5-7 ações)

Para cada ação:
1. **Ação** — o que fazer (específico, mensurável)
2. **Base SWOT** — ex: "Alavanca F2, captura O1, mitiga A3"
3. **Relação com Beachhead** — relevante para o segmento escolhido? Como?
4. **Impacto** — Alto / Médio / Baixo
5. **Prazo** — semana 2 / 3 / 4

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Cada item da SWOT é específico — se trocar o nome da empresa, NÃO serve para outro negócio?
- [ ] Todos os itens têm "evidência" documentada (dado, fonte, ou referência)?
- [ ] O Scorecard do Beachhead foi preenchido com notas justificadas (não notas aleatórias)?
- [ ] O segmento vencedor foi cruzado com o SOM (tamanho compatível com a meta)?
- [ ] As ações derivam explicitamente dos quadrantes SWOT (referência F/W/O/T)?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

**Para a SWOT:**
- "Algum item que está genérico demais?"
- "Falta alguma força ou fraqueza que você enxerga no dia a dia?"
- "A síntese estratégica captura a essência do que o cliente precisa fazer?"

**Para o Beachhead:**
- "O segmento vencedor faz sentido intuitivamente para você?"
- "Esse segmento tem demanda suficiente para atingir a meta de {X} em {prazo}?"
- "Tem algum segmento que você já tem tração hoje mas que não apareceu na lista?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/swot-beachhead-market.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Sugira próxima skill:
   - `/proposta-unica-de-valor` (POP 3.3 — agora com Beachhead definido para JTBD tático)
   - "SWOT concluída. Beachhead: {segmento}. Score: {X}/30. Próximo: PUV para esse segmento."
