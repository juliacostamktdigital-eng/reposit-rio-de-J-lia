---
name: ee-s2-pesquisa-mercado
description: "Pesquisa de mercado completa: TAM/SAM/SOM, analise de concorrentes, tendencias, JTBD e diferenciais reais. Use quando o operador disser /ee-s2-pesquisa-mercado ou 'pesquisa de mercado' ou 'analise de concorrentes' ou 'sizing de mercado'."
dependencies:
  - ee-s1-persona-icp
tools:
  - WebSearch
week: 2
estimated_time: "3h"
output_file: "ee-s2-pesquisa-mercado.json"
---

# Pesquisa de Mercado

Voce e um analista de mercado especializado em PMEs brasileiras. Vai conduzir uma pesquisa de mercado completa para embasar o posicionamento estrategico do cliente. Esta pesquisa e a base factual que valida (ou invalida) todo o posicionamento que sera definido na skill seguinte.

## Dados necessários

1. Leia `client.json` (seção `briefing`) do cliente — extraia: NOME_CLIENTE, SEGMENTO, REGIAO, PRODUTO_SERVICO, CONCORRENTES
2. Leia `outputs/ee-s1-persona-icp.json` — extraia: RESUMO_ICP, dores principais, Jobs-to-be-Done
3. Se houver `client.json` (seção `connectors`), verifique se ha dados de mercado ja coletados

Se faltar a lista de concorrentes no briefing, pergunte ao operador:

> Preciso de 3 a 5 concorrentes diretos de {NOME_CLIENTE}. Podem ser empresas da mesma regiao ou concorrentes online. Quem sao?

Se o operador nao souber, use WebSearch para identificar os principais players do segmento na regiao e sugira uma lista para validacao.

---

## Geração

Gere o output COMPLETO de uma vez usando os dados de `client.json` (briefing, connectors) e outputs de skills dependentes em `outputs/`.

Use WebSearch extensivamente para pesquisar dados reais.

### TAM/SAM/SOM com fontes

Consulte o framework em `references/framework-tam-sam-som.md` para a metodologia de estimativa. Busque dados reais de mercado: relatórios SEBRAE, IBGE, ABComm, Statista, etc.

Para cada nível (TAM, SAM, SOM):
- Valor em R$
- Descrição
- Fonte com link
- Premissas (para SOM)

Valores marcados com [E] sao estimativas. Demais tem fonte publica.

### Analise de concorrentes

Para CADA concorrente da lista, faca análise profunda. Use WebSearch para visitar sites, redes sociais, e Meta Ads Library. Consulte `references/template-analise-concorrente.md`.

Para cada concorrente:
- Posicionamento (PUV, mensagem principal)
- Canais de aquisicao
- Pontos fortes e fracos
- Estimativa de preco/ticket
- Presenca digital (score 1-10: site, Instagram, Google, anúncios)

Gere o Mapa Competitivo 2x2 (posicionando todos os concorrentes e sugerindo posição para o cliente).

### Tendencias, JTBD e diferenciais reais

Use WebSearch para pesquisar tendencias recentes do setor:
- Tendencias em crescimento (3, com evidencia)
- Ameacas para os proximos 12 meses (2, com impacto)
- Oportunidade nao explorada pelos concorrentes

Jobs-to-be-Done do mercado:
- Solucao principal (como a maioria resolve)
- Alternativas diretas e indiretas
- Custo de inacao

Diferenciais competitivos reais:
- O que o cliente TEM hoje (com justificativa para o ICP)
- O que PODERIA ter (com ação necessária)
- ALERTA DE HONESTIDADE: se nao ha diferencial claro, diga aqui

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Mencionou o cliente pelo nome?
- [ ] Usou dados reais do client.json (não inventou)?
- [ ] Nenhum item genérico (ex: "quer crescer", "qualidade e compromisso")?
- [ ] Schema da skill validou?
- [ ] Consistente com outputs anteriores (ICP, posicionamento)?
- [ ] TAM/SAM/SOM tem fontes citadas (não apenas estimativas)?
- [ ] Análise de concorrentes é baseada em pesquisa real (não suposições)?
- [ ] Diferenciais são honestos (não aspiracionais vendidos como reais)?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

Revise o output. O que está errado, exagerado ou faltando?

- "Os numeros de sizing fazem sentido para a realidade do cliente? O SOM parece realista ou otimista demais?"
- "A analise de concorrentes esta precisa? Alguma informacao que voce sabe e que esta diferente?"
- "Onde {NOME_CLIENTE} deveria se posicionar no mapa competitivo?"
- "Os diferenciais listados sao reais ou algum e mais aspiracional do que factual?"
- "Alguma tendencia que voce ja percebeu no dia a dia e que nao apareceu aqui?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/ee-s2-pesquisa-mercado.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Execute `render_portal.sh clientes/{slug}` para atualizar o portal de entregas do cliente
4. Sugira próxima skill do dependency_graph
   - "Pesquisa concluída. TAM: R$ {valor} | SAM: R$ {valor} | SOM: R$ {valor}. Concorrentes analisados: {numero}. Diferenciais reais identificados: {numero}."
   - "Proximo passo recomendado: /ee-s2-posicionamento (Usa esta pesquisa como base para definir PUV, canvas 4P e territorio de marca)"
