---
name: leitura-performance-growth-n3
description: Lê performance de growth em nível N3 conectando mídia, LP, funil, CRM e qualidade comercial, sem otimizar por CPL isolado. Use para analisar planilha de testes, exports de mídia/CRM, qualidade de lead, padrões criativos, funil, decisões de escalar/ajustar/matar e diagnóstico pós-campanha.
---

# Leitura Performance Growth N3

## Quando Usar

Use quando precisar:

- ler performance após ou durante um ciclo;
- comparar mídia com qualidade comercial;
- identificar criativos/campanhas vencedores, perdedores e inconclusivos;
- detectar tracking quebrado;
- separar lead barato ruim de lead caro bom;
- decidir próximos testes sem olhar só CPL;
- preparar debrief N3 ou próximo ciclo.

Não use para montar a planilha do zero. Para isso, use `montar-planilha-testes-growth`.

## Inputs Necessários

- Aba de testes com hipóteses e metas.
- Performance de mídia por campanha/adgroup/criativo.
- Leads e funil com MQL, SQL, oportunidade, venda e feedback.
- UTMs e IDs confiáveis.
- Critérios de sucesso e janela de leitura.
- Observações de tracking e mudanças feitas no ciclo.

Se tracking ou IDs estiverem ruins, classifique a leitura como parcial e recomende correção antes de concluir.

## Workflow

1. Confirme o grão da análise: campanha, adgroup, criativo, teste ou lead.
2. Verifique integridade mínima:
   - IDs preenchidos;
   - origem preservada;
   - volume suficiente;
   - feedback comercial disponível;
   - período e janela de aprendizado respeitados.
3. Junte mídia e funil por IDs.
4. Calcule métricas:
   - mídia: spend, impressions, clicks, CTR, CPC, CPM, LP views, leads, CPL;
   - funil: MQL, SQL, oportunidade, venda, receita;
   - qualidade: cost per MQL, cost per SQL, CAC, ROAS, speed-to-lead, feedback.
5. Leia por atributos criativos:
   - formato;
   - hook;
   - dor;
   - persona;
   - ângulo;
   - etapa;
   - versão.
6. Classifique cada hipótese:
   - vencedor;
   - perdedor;
   - manter para mais volume;
   - ajustar;
   - inconclusivo por volume;
   - inconclusivo por tracking;
   - inválido por execução.
7. Gere decisão recomendada: escalar, manter, ajustar, matar, replicar, corrigir tracking, revisar oferta ou acionar vendas.
8. Liste próximos testes e dados necessários para N3.

## Output Esperado

Produza:

- diagnóstico executivo;
- tabela consolidada de mídia + funil;
- leitura por hipótese;
- leitura por atributo criativo;
- alertas de tracking/dados;
- decisões recomendadas;
- próximos testes;
- limites da conclusão.

Use `templates/relatorio-performance-n3.md` para o relatório.
Use CSVs de exemplo em `templates/` com o script.

## Script Utilitário

Para consolidar mídia e funil:

```bash
python scripts/analyze_growth_performance.py \
  --media templates/performance-midia.csv \
  --funnel templates/performance-funil.csv \
  --out /tmp/performance-growth.csv \
  --md /tmp/performance-growth.md
```

O script gera uma leitura inicial. O julgamento final deve considerar hipótese, contexto e qualidade dos dados.

## Definition Of Done

- Mídia e funil foram conectados por IDs.
- CPL não foi usado como critério isolado.
- Qualidade comercial entrou na leitura.
- Hipóteses foram classificadas com evidência.
- Inconclusivos foram separados de vencedores/perdedores.
- Tracking quebrado foi sinalizado.
- Próximos passos são acionáveis.

## Armadilhas

- Matar criativo apenas por CPL.
- Ignorar volume mínimo e tempo de aprendizado.
- Tratar lead como resultado final.
- Ignorar feedback de vendas.
- Tirar conclusão com origem desconhecida alta.
- Comparar criativos com etapas ou públicos diferentes sem avisar.
- Mudar várias variáveis e atribuir resultado a uma só.

## Referências

- Playbook canônico: `assets/canonicos/02_PLANILHA_DE_TESTES_GROWTH_CANONICA.md`
- Detalhamento: `reference.md`
- Template: `templates/relatorio-performance-n3.md`
- Exemplo mídia: `templates/performance-midia.csv`
- Exemplo funil: `templates/performance-funil.csv`
