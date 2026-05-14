---
name: plano-midia-leadgen
description: Cria plano de mídia para leadgen conectando objetivo, budget, canais, funil, cenários, hipóteses, tracking, cronograma e guardrails. Use quando o usuário pedir plano de mídia, estratégia de canais, distribuição de verba, estrutura de campanhas, metas de funil, planejamento de investimento ou critérios de leitura.
---

# Plano Mídia Leadgen

## Quando Usar

Use quando precisar construir ou revisar um plano de mídia para demanda qualificada:

- antes de setup Meta Ads ou Google Ads;
- após DEOC, benchmark e funil unificado;
- quando houver budget e meta, mas faltar tese de distribuição;
- quando o cliente pedir canais, verba, campanhas e metas;
- quando for necessário conectar investimento a MQL, SQL, oportunidades, vendas e qualidade comercial.

Não use para:

- simular cenários isoladamente em profundidade, use `simulador-cenarios-midia-funil`;
- decidir otimização pós-campanha, use `guardrails-otimizacao-midia` ou `leitura-performance-growth-n3`;
- criar UTMs finais, use `gerador-taxonomia-utm-ids`.
- recriar ICP, persona ou promessa; se isso estiver instável, volte ao DEOC antes de decidir canal e budget.

## Inputs Necessários

- contrato/escopo;
- objetivo do cliente;
- ticket médio ou valor por venda;
- meta de vendas, oportunidades ou MQLs;
- budget disponível;
- período do plano;
- cohort e segmento;
- funil e taxas de conversão;
- histórico de mídia e comercial;
- benchmark de segmento;
- capacidade comercial e SLA;
- DEOC;
- restrições legais/comerciais;
- lead correto e qualidade mínima esperada.

Se faltar premissa crítica, declare a lacuna e use intervalo/conservadorismo. Não esconda premissa fraca.

## Fronteira Com DEOC

O DEOC define **o que dizer**, **para quem dizer** e quais claims/provas podem ser usados. O plano de mídia define **onde operar**, **como estruturar campanha**, **qual budget testar**, **qual baseline esperar** e **o que muda quando o número sai da faixa**. Se durante o plano aparecer incoerência de ICP, oferta ou mensagem, registre backlog de ajuste no DEOC em vez de remendar a narrativa dentro da mídia.

## Workflow

1. Defina objetivo comercial, período, budget, meta principal, maior risco e critério de sucesso.
2. Estruture premissas comerciais: ticket, conversões, capacidade, ciclo, SLA, valor esperado e restrições.
3. Modele a lógica de funil: investimento -> leads -> MQL -> SQL -> oportunidade -> venda -> receita.
4. Distribua investimento por canal com papel claro:
   - aquisição/captação;
   - remarketing;
   - CRM/reativação;
   - busca/demanda ativa;
   - awareness/contexto quando fizer sentido;
   - offline/parceiros quando relevante.
5. Para cada canal, defina objetivo, etapa, investimento, metas, papel, risco e critério de corte/revisão.
6. Defina estrutura planejada de campanhas com IDs previstos, público, oferta, LP, criativos, hipótese, métrica e janela de decisão.
7. Planeje criativos necessários por formato/persona/hook/dor/ângulo e conecte com briefing criativo.
8. Inclua plano de tracking: taxonomia UTM, IDs, fonte da verdade, CRM, first/last-touch e lead teste.
9. Defina ritmo de leitura diário, semanal, quinzenal e mensal.
10. Crie cronograma de investimento e previsto vs realizado quando o período tiver semanas/lotes.
11. Adicione guardrails de decisão para evitar otimização cega por CPL.

## Output Esperado

Produza:

- resumo executivo;
- premissas comerciais;
- distribuição por canal;
- estrutura planejada de campanhas;
- estrutura de criativos;
- plano de tracking;
- ritmo de leitura;
- cronograma de investimento;
- guardrails;
- critérios N2/N3 e gaps.

Use `templates/plano-midia.md` para o documento.
Use `templates/plano-midia.json` com o script para gerar tabelas CSV/Markdown.

## Script Utilitário

Para gerar tabelas de canais e campanhas:

```bash
python3 scripts/build_media_plan.py templates/plano-midia.json --out /tmp/plano-midia --md /tmp/plano-midia.md
```

O script calcula leads, MQLs, SQLs, vendas, CAC e ROAS por canal/campanha com base nas premissas. Revise antes de apresentar ao cliente.

## Definition Of Done

- Premissas explícitas.
- Budget conectado a meta de funil.
- Distribuição de verba por canal com papel e risco.
- Metas por etapa do funil.
- Hipóteses por campanha.
- Plano de tracking antes do go-live.
- Cenários ou premissas suficientes para avaliar viabilidade.
- Critérios de leitura e guardrails definidos.
- Plano linkado a DEOC, tracking e planilha de testes.
- Incoerências de DEOC foram resolvidas ou registradas como backlog antes do go-live.

## Armadilhas

- Dividir verba por canal sem tese.
- Prometer resultado sem funil, ticket e capacidade.
- Otimizar por CPL sem qualidade.
- Plano sem tracking.
- Campanhas sem hipótese.
- Budget fragmentado demais para aprender.
- Ignorar SLA e capacidade comercial.
- Não registrar o que muda quando métrica sai da faixa.

## Referências

- Playbook canônico: `assets/canonicos/03_PLANO_DE_MIDIA_CANONICO.md`
- Detalhamento: `reference.md`
- Template: `templates/plano-midia.md`
- Schema: `templates/plano-midia.json`
