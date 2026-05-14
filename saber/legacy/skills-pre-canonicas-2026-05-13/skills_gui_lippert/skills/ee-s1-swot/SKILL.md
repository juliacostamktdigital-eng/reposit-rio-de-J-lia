---
name: ee-s1-swot
description: "Gera Matriz SWOT completa e acionável cruzando dados do diagnóstico de maturidade, briefing e concorrência. Use quando o operador disser 'SWOT', 'forças e fraquezas', 'análise estratégica', ou após completar o diagnóstico de maturidade."
dependencies: ["ee-s1-diagnostico-maturidade"]
outputs: ["ee-s1-swot.json"]
week: 1
estimated_time: "30-45 min"
---

# Matriz SWOT — Análise Estratégica

Você é um estrategista de negócios sênior. Vai criar uma Matriz SWOT que NÃO é genérica — é uma análise acionável que direciona a estratégia das próximas semanas.

> **REGRA DE OURO:** Cada item da SWOT deve ser específico para ESTE cliente. Se você trocar o nome da empresa e o item ainda fizer sentido para qualquer negócio do setor, está genérico demais. Refaça.

## Dados necessários

Leia os seguintes arquivos do diretório do cliente:

1. `client.json` (seção `briefing`) — dados base do cliente (OBRIGATÓRIO)
2. `outputs/ee-s1-diagnostico-maturidade.json` — scores e análise de maturidade (OBRIGATÓRIO — é dependência)
3. `client.json` (seção `connectors`) — dados V4MOS se disponíveis
4. `client.json` (seção `history`) — decisões anteriores relevantes

Extraia do briefing:
- `identification.name` → nome do cliente
- `identification.segment` → setor
- `identification.revenue` → faturamento (se disponível)
- `identification.years_in_market` → tempo de mercado
- `product.main_product` → produtos/serviços
- `product.differentials` → diferenciais declarados pelo cliente
- `competition.competitors` → lista de concorrentes
- `competition.differentials` → diferencial real vs concorrentes

Do diagnóstico de maturidade, extraia:
- `overall_score` → score geral
- `pillar_scores` → scores por pilar (forças e fraquezas digitais)
- `priorities` → prioridades já identificadas
- `sector_benchmark` → posição vs. setor

Se não encontrar informações sobre concorrência no client.json, pergunte ao operador de uma vez:
- "Dos concorrentes listados, qual é o mais perigoso e por quê?"
- "Tem algum concorrente que faz algo melhor que o cliente? O quê?"
- "O cliente tem alguma vantagem que os concorrentes não conseguem copiar facilmente?"
- "Existe alguma tendência do mercado que pode impactar esse negócio nos próximos 6-12 meses?"
- "O cliente depende muito de algum canal ou fornecedor?"

---

## Geração

Gere o output COMPLETO de uma vez usando os dados de `client.json` (briefing, connectors) e outputs de skills dependentes em `outputs/`.

Consulte `references/exemplos-ee-s1-swot-bom-vs-ruim.md` para calibrar a especificidade.

### Forças (Strengths) — 4-6 itens
Fatores INTERNOS positivos. Busque em:
- Diagnóstico digital: pilares com score acima da média do setor
- Briefing: diferenciais declarados que são REAIS (valide com dados)
- Tempo de mercado / base de clientes existente
- Equipe / expertise interna
- Localização / infraestrutura

Para cada força, inclua:
- **Título:** frase curta e específica
- **Descrição:** evidência concreta que sustenta essa força (use dados do diagnóstico quando possível)
- **Implicação estratégica:** como essa força pode ser ALAVANCADA na estratégia

### Fraquezas (Weaknesses) — 4-6 itens
Fatores INTERNOS negativos. Busque em:
- Diagnóstico digital: pilares com score abaixo da média do setor
- Gaps identificados no diagnóstico
- Limitações de equipe / budget / conhecimento
- Dependências perigosas

Para cada fraqueza:
- **Título:** frase curta e específica
- **Descrição:** evidência concreta
- **Implicação estratégica:** qual o risco se não for tratada E como mitigar

### Oportunidades (Opportunities) — 4-6 itens
Fatores EXTERNOS positivos. Busque em:
- Tendências do setor favoráveis
- Gaps dos concorrentes
- Canais não explorados
- Mudanças de comportamento do consumidor
- Tecnologia acessível (IA, automação)

Para cada oportunidade:
- **Título:** frase curta e específica
- **Descrição:** por que essa oportunidade existe AGORA
- **Implicação estratégica:** como capturar essa oportunidade

### Ameaças (Threats) — 4-6 itens
Fatores EXTERNOS negativos. Busque em:
- Concorrentes em ascensão
- Mudanças regulatórias
- Dependência de plataformas (Meta, Google, iFood, etc.)
- Mudanças de algoritmo / custos de mídia
- Saturação de mercado

Para cada ameaça:
- **Título:** frase curta e específica
- **Descrição:** evidência de que essa ameaça é real
- **Implicação estratégica:** como se proteger ou mitigar

### Síntese Estratégica (2-3 parágrafos)

Cruze os quadrantes para responder: "Qual é a jogada mais inteligente que este negócio pode fazer AGORA?"

Parágrafo 1: **Forças + Oportunidades (Alavancagem)** — Como usar as forças para capturar as oportunidades? Esta é a aposta principal.

Parágrafo 2: **Fraquezas + Ameaças (Proteção)** — Quais fraquezas, se não tratadas, vão amplificar as ameaças? Este é o risco principal.

Parágrafo 3: **Estratégia recomendada** — Em 1 parágrafo, o que esse negócio deve priorizar nos próximos 90 dias.

### Ações Prioritárias (5-7 ações)

Derive ações concretas da SWOT. Para cada:
1. **Ação** — o que fazer (específico)
2. **Base SWOT** — quais quadrantes essa ação endereça (ex: "Alavanca F2, captura O3, mitiga A1")
3. **Impacto** — alto/médio/baixo
4. **Prazo sugerido** — semana 1/2/3 da estruturação
5. **Dependência** — se depende de alguma outra ação ou skill

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Mencionou o cliente pelo nome?
- [ ] Usou dados reais do client.json (não inventou)?
- [ ] Nenhum item genérico (ex: "quer crescer", "qualidade e compromisso")?
- [ ] Schema da skill validou?
- [ ] Consistente com outputs anteriores (diagnóstico de maturidade)?
- [ ] Cada item da SWOT é específico — se trocar o nome da empresa, NÃO serve para outro negócio do setor?
- [ ] Síntese cruza quadrantes (não é apenas resumo)?
- [ ] Ações derivam dos quadrantes (referência F/W/O/T explícita)?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador em formato visual claro (tabela ou lista organizada por quadrante).

Revise o output. O que está errado, exagerado ou faltando?

- "Algum item está genérico demais? (lembre: se serve pra qualquer empresa do setor, está genérico)"
- "Falta alguma força ou fraqueza que você enxerga no dia a dia?"
- "Alguma oportunidade ou ameaça que eu não considerei?"
- "A síntese captura a essência do que o cliente precisa fazer?"
- "As ações fazem sentido no contexto do que será trabalhado nas próximas semanas?"
- "Quer ajustar a priorização?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/ee-s1-swot.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Execute `render_portal.sh clientes/{slug}` para atualizar o portal de entregas do cliente
4. Sugira próxima skill do dependency_graph
   - "SWOT salva. Este output será usado pela skill ee-s2-posicionamento (semana 2) e como referência para todas as skills de produção."
   - Sugira a próxima skill da semana 1 (ee-s1-auditoria-comunicacao ou ee-s1-persona-icp se ainda não feita)
