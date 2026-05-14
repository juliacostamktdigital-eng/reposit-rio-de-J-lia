---
name: debrief-aprendizados-growth
description: Gera debrief N3 e transforma testes concluídos em decisões, aprendizados, backlog, recomendações e briefing do próximo ciclo. Use após ciclos de campanha, leitura de performance, planilha de testes, análise de criativos, revisão de funil ou quando o usuário pedir debrief, aprendizados, canonização ou próximos testes.
---

# Debrief Aprendizados Growth

## Quando Usar

Use quando houver testes finalizados ou um ciclo que precisa virar decisão:

- após leitura de performance;
- antes de planejar o próximo ciclo;
- quando existe relatório, mas falta decisão;
- quando aprendizados precisam virar backlog;
- quando padrões podem ser canonizados;
- quando tracking, oferta ou vendas precisam ser corrigidos.

Não use para analisar dados crus do zero. Para isso, use `leitura-performance-growth-n3`.

## Inputs Necessários

- Testes concluídos ou pausados.
- Resultado vs meta.
- Decisões sugeridas ou tomadas.
- Evidências por teste.
- Limites da conclusão.
- Performance de mídia e funil.
- Feedback comercial.
- Gaps de tracking.
- Assets impactados: DEOC, plano de mídia, briefing criativo, LP, CRM/SLA.

Se não houver evidência ou limite da conclusão, classifique como hipótese, não como aprendizado.

## Workflow

1. Liste todos os testes do ciclo com status, hipótese, variável e meta.
2. Para cada teste, registre:
   - resultado;
   - decisão;
   - evidência;
   - limite da conclusão;
   - próximo passo.
3. Separe decisões:
   - escalar;
   - manter;
   - ajustar;
   - matar;
   - replicar;
   - criar novo teste;
   - corrigir tracking;
   - revisar oferta;
   - acionar vendas;
   - inconclusivo.
4. Transforme aprendizados em backlog priorizado.
5. Indique quais assets precisam mudar.
6. Identifique padrões e anti-padrões candidatos a canonização.
7. Gere briefing do próximo ciclo.
8. Registre changelog de decisões.

## Output Esperado

Produza:

- debrief N3;
- decisões por teste;
- aprendizados com evidência e limite;
- backlog de próximos testes;
- recomendações por asset;
- padrões/anti-padrões candidatos;
- briefing do próximo ciclo;
- changelog.

Use `templates/debrief-n3.md` para o documento final.
Use `templates/aprendizados.csv` com o script para consolidar backlog e canonização.

## Script Utilitário

Para consolidar aprendizados em Markdown e backlog CSV:

```bash
python scripts/build_debrief.py templates/aprendizados.csv --md /tmp/debrief-n3.md --backlog /tmp/backlog-aprendizados.csv
```

O script organiza decisões e aprendizados. O debrief final ainda deve receber contexto, narrativa e julgamento do especialista.

## Definition Of Done

- Todo teste tem decisão ou motivo de inconclusivo.
- Todo aprendizado tem evidência e limite.
- Backlog está priorizado.
- Próximo ciclo tem hipóteses claras.
- Assets impactados foram listados.
- Padrões canonizáveis foram separados de aprendizados locais.
- Erros de tracking viraram ação corretiva.

## Armadilhas

- Fazer resumo bonito sem decisão.
- Chamar hipótese de aprendizado.
- Não registrar limite da conclusão.
- Ignorar testes inconclusivos.
- Não alimentar o próximo ciclo.
- Canonizar padrão sem contexto.
- Repetir teste sem explicar o que muda.

## Referências

- Playbook canônico: `assets/canonicos/02_PLANILHA_DE_TESTES_GROWTH_CANONICA.md`
- Detalhamento: `reference.md`
- Template: `templates/debrief-n3.md`
- Exemplo CSV: `templates/aprendizados.csv`
