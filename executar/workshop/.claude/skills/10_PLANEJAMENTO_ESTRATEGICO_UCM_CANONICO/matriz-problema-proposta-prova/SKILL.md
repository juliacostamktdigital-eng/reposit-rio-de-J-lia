---
name: matriz-problema-proposta-prova
description: Conecta problemas priorizados, impacto, proposta de valor, mecanismo, promessa, objeção, prova e claims pendentes em matriz 3D (problema × proposta × prova-por-papel) para evitar comunicação sem evidência. Aplica vocabulário regulatório formal (FTC reasonable basis, substantiation, CONAR Brasil), Anti-claim explícito (o que NÃO podemos afirmar) e hierarquia Message House (roof claim → pillars → proof points, padrão Atlassian). Use em UCM, DEOC, DCC, LP, copy, criativos, briefing e revisão estratégica de claims.
---

# Matriz Problema Proposta Prova

## Quando Usar

Use antes de transformar dor em promessa. A skill evita claims soltos, promessa sem prova e copy sem mecanismo.

Use especialmente para:

- priorizar problemas estratégicos;
- criar proposta de valor;
- revisar claims;
- estruturar LP;
- orientar criativos;
- alinhar comercial;
- alimentar DEOC/DCC.

## Inputs

- discovery;
- UCM/DEOC;
- cases;
- números;
- provas;
- objeções;
- restrições jurídicas;
- feedback comercial.

## Workflow

1. Liste problemas reais do público.
2. Para cada problema, registre:
   - descrição objetiva;
   - impacto prático;
   - impacto emocional;
   - impacto financeiro/operacional;
   - voz do cliente;
   - estágio do funil.
3. Conecte cada problema a:
   - proposta de valor;
   - mecanismo;
   - promessa;
   - objeção;
   - prova.
4. Classifique prova:
   - forte;
   - parcial;
   - ausente;
   - proibida/restrita.
5. Cruze com papéis (matriz 3D problema × proposta × prova-por-papel) — a mesma proposta exige provas distintas:
   - Economic Buyer: ROI quantificado, payback, TCO;
   - User: demo, screenshot, fluxo real;
   - Technical Buyer: arquitetura, segurança, integração;
   - Champion: case interno aplicável, narrativa pra defender com pares.
6. Liste o Anti-claim — o que NÃO podemos afirmar:
   - regulatório (vedação ANVISA, CONAR, Lei 14.790, BACEN, CVM);
   - comparativo sem benchmark publicado;
   - factual ainda não comprovado (sem reasonable basis no momento da emissão).
7. Marque promessa sem prova como claim pendente.
8. Priorize por impacto, frequência, evidência e risco.

## Output Esperado

- matriz de problemas priorizados;
- proposta de valor por problema;
- mecanismos e promessas;
- provas associadas;
- claims pendentes;
- recomendações para copy, LP, criativo e comercial.

Use `templates/matriz-problema-prova.md`.
Use `templates/matriz-problema-prova.json` com o script para gerar Markdown/CSV.

## Script Utilitário

```bash
python3 scripts/build_problem_proof_matrix.py templates/matriz-problema-prova.json --md /tmp/matriz.md --csv /tmp/matriz.csv
```

## Definition Of Done

- Toda promessa forte tem prova ou vira claim pendente.
- Cada claim possui reasonable basis substantiation no momento da emissão (padrão FTC + CONAR Brasil) — claim sem reasonable basis = passivo regulatório.
- Anti-claim explícito está listado (regulatório, comparativo sem benchmark, factual não comprovado).
- Matriz 3D entrega prova diferenciada por papel (Economic Buyer / User / Technical Buyer / Champion).
- Estrutura segue Message House (Atlassian): roof claim → pillars → proof points hierarquicamente consistentes.
- Problema tem impacto e voz do cliente.
- Proposta de valor tem mecanismo.
- Risco jurídico/comercial está marcado.
- Saída orienta ativos executáveis.
