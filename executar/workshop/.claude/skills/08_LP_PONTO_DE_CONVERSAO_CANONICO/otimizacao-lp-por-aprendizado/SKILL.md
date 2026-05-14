---
name: otimizacao-lp-por-aprendizado
description: Propõe otimizações de LP e ponto de conversão com base em conversão, qualidade de lead, MQL/SQL, feedback comercial, objeções e testes anteriores. Use em N3, debrief, revisão de LP, priorização de testes de headline, CTA, formulário, prova, FAQ ou seções.
---

# Otimização LP Por Aprendizado

## Quando Usar

Use quando a LP já rodou ou recebeu feedback suficiente para gerar uma versão melhor.

Situações típicas:

- taxa de conversão baixa;
- conversão alta com lead ruim;
- MQL/SQL baixo por LP;
- objeção comercial recorrente;
- headline desalinhada com criativo;
- CTA cria expectativa errada;
- formulário gera fricção;
- falta de prova afeta avanço comercial.

## Inputs Necessários

- performance da LP;
- leads;
- MQL/SQL/oportunidades/vendas;
- feedback comercial;
- testes anteriores;
- objeções;
- QA da LP;
- mapa de seções;
- campanha/criativos de origem.

## Workflow

1. Leia performance da LP junto com qualidade comercial.
2. Identifique o gargalo:
   - atração;
   - promessa;
   - prova;
   - CTA;
   - formulário;
   - objeção;
   - tracking;
   - SLA/comercial.
3. Formule hipótese de otimização.
4. Defina variação proposta:
   - headline;
   - subheadline;
   - CTA;
   - seção;
   - prova;
   - FAQ;
   - formulário;
   - thank-you.
5. Defina métrica de leitura:
   - conversão LP;
   - form_start -> submit;
   - MQL rate;
   - SQL rate;
   - lead quality;
   - objeção reduzida.
6. Priorize por impacto, confiança, esforço e risco.
7. Registre versão, critério de sucesso e limite da conclusão.

## Output Esperado

- backlog de testes de LP;
- hipóteses;
- variações propostas;
- prioridade;
- métrica de leitura;
- critérios de sucesso;
- riscos;
- próxima versão documentada.

Use `templates/backlog-testes-lp.md` para planejamento manual.
Use `templates/testes-lp.json` com o script para priorizar.

## Script Utilitário

```bash
python3 scripts/prioritize_lp_tests.py templates/testes-lp.json --md /tmp/testes-lp.md --csv /tmp/testes-lp.csv
```

## Definition Of Done

- Cada otimização nasce de evidência.
- Cada teste tem hipótese clara.
- Métrica de leitura inclui qualidade, não só conversão.
- Variação muda uma alavanca principal.
- Próxima versão da LP fica documentada.
