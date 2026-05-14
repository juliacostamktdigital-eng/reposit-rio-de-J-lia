---
name: guardrails-otimizacao-midia
description: Define e aplica guardrails de decisão para otimização de mídia, evitando cortes cegos por CPL e conectando métricas de mídia, funil, tracking, qualidade comercial e changelog. Use em rotina de otimização, leitura semanal/quinzenal, revisão de campanhas, decisão de pausar/escalar/ajustar ou quando houver conflito entre CPL, CPMQL, SQL e qualidade.
---

# Guardrails Otimização Mídia

## Quando Usar

Use quando houver plano de mídia em execução e for necessário decidir o que fazer com campanhas, canais, públicos, criativos, LPs ou budget.

Situações típicas:

- CPL acima da meta;
- CPL baixo com lead ruim;
- campanha gastando sem evento;
- CTR alto e conversão baixa;
- MQL bom e SQL ruim;
- divergência entre previsto e realizado;
- mudança de budget, mix, público, criativo ou destino;
- discussão sobre pausar, escalar, manter ou investigar.

## Inputs Necessários

- plano e metas previstas;
- métricas realizadas de mídia;
- métricas de LP/funil;
- MQL, SQL, oportunidade, venda e receita;
- qualidade comercial/feedback do time de vendas;
- tracking e lead teste;
- período mínimo de leitura;
- volume mínimo de dados;
- changelog anterior.

## Workflow

1. Identifique o nível de leitura:
   - diário: risco grave, gasto, reprovação, tracking;
   - semanal: ritmo, CPL, qualidade inicial;
   - quinzenal: MQL/SQL, padrões criativos, decisão;
   - mensal: aprendizado, revisão de plano.
2. Cheque se há volume mínimo e tracking confiável.
3. Compare previsto vs realizado.
4. Leia mídia junto com funil e qualidade comercial.
5. Aplique guardrails:
   - não matar CPL alto se CPMQL/SQL está saudável;
   - não escalar CPL baixo se MQL/SQL está ruim;
   - investigar tracking antes de mexer em criativo quando há gasto e zero evento;
   - revisar LP/oferta se CTR alto e conversão baixa;
   - revisar SLA/handoff se lead bom e SQL baixo;
   - recalcular projeção quando previsto diverge do realizado.
6. Classifique severidade:
   - crítico: tracking quebrado, gasto sem evento, promessa impossível;
   - alto: qualidade comercial ruim, CAC inviável, gargalo forte;
   - médio: sinal criativo/oferta/canal precisa teste;
   - baixo: monitorar.
7. Recomende ação:
   - manter;
   - escalar;
   - ajustar;
   - pausar;
   - investigar tracking;
   - revisar LP/oferta;
   - revisar público/criativo;
   - revisar SLA/handoff;
   - recalcular plano.
8. Registre changelog com motivo, métrica observada e próxima leitura esperada.

## Output Esperado

- diagnóstico por sinal;
- decisão recomendada;
- severidade;
- evidência;
- risco de decisão;
- próxima ação;
- registro de changelog.

Use `templates/checklist-guardrails.md` para revisão manual.
Use `templates/sinais-otimizacao.csv` com o script para classificação tabular.

## Script Utilitário

```bash
python3 scripts/classify_media_signals.py templates/sinais-otimizacao.csv --md /tmp/guardrails.md --csv /tmp/guardrails.csv
```

O script classifica sinais comuns e sugere ação. A decisão final deve considerar contexto, volume mínimo e confiabilidade do tracking.

## Definition Of Done

- A decisão não depende de CPL isolado.
- Tracking foi validado antes de otimizar.
- Funil e qualidade comercial foram considerados.
- Ação recomendada tem evidência e próxima leitura.
- Mudança relevante entrou em changelog.
- Risco de falso positivo foi declarado.
