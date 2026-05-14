---
name: rubrica-n1-n2-n3-componentes
description: Padroniza avaliação N1/N2/N3 por componente do Marketing OS, definindo evidências, falsos positivos, donos, frequência de revisão e recomendação de próximo nível. Use em auditorias, readiness, inventário de gaps, health check operacional ou quando for preciso reduzir subjetividade na maturidade da conta.
---

# Rubrica N1 N2 N3 Componentes

## Quando Usar

Use quando a avaliação de maturidade precisa deixar de ser opinativa e virar critério verificável.

Situações típicas:

- auditoria de conta;
- readiness antes de go-live;
- revisão N2/N3;
- inventário de gaps;
- priorização de backlog;
- discussão sobre "temos isso" vs "isso roda";
- comparação entre cohorts, squads ou clientes.

## Inputs Necessários

- componentes do Marketing OS;
- assets existentes;
- evidências;
- donos;
- frequência de revisão;
- dados de execução;
- decisões/changelog;
- critérios do playbook;
- gaps conhecidos.

## Escala

### N0 - Ausente

Não há asset, dono, evidência ou processo. A informação depende de conversa solta.

### N1 - Existente Ou Rascunho

Existe arquivo, checklist, campanha, planilha ou setup inicial, mas sem rastro suficiente para auditoria.

### N2 - Implementado E Auditável

Assets obrigatórios existem, donos estão claros, dados mínimos são preservados, há evidência de execução e o processo pode ser auditado.

### N3 - Gerenciado

Dados são lidos em cadência, decisões são registradas, hipóteses entram no backlog, aprendizados alimentam o próximo ciclo e mudanças têm changelog.

## Workflow

1. Liste os componentes avaliáveis.
2. Para cada componente, registre:
   - nível declarado;
   - evidência;
   - dono;
   - frequência de revisão;
   - falso positivo observado;
   - lacuna para próximo nível.
3. Verifique se o nível declarado é sustentado por evidência.
4. Rebaixe quando houver falso positivo:
   - arquivo existe, mas não é usado;
   - setup existe, mas não preserva dados;
   - campanha roda, mas não aprende;
   - decisão existe, mas não tem registro;
   - processo depende de uma pessoa.
5. Recomende próximo nível:
   - de N0 para N1: criar asset mínimo;
   - de N1 para N2: tornar auditável;
   - de N2 para N3: criar cadência, decisão e changelog.
6. Gere gaps para `inventario-gaps-assets-marketing-os` ou backlog.

## Output Esperado

- rubrica por componente;
- nível validado;
- evidências exigidas;
- falsos positivos;
- lacunas;
- recomendação para próximo nível;
- prioridade de melhoria.

Use `templates/rubrica-n1-n2-n3.md` para revisão manual.
Use `templates/rubrica-componentes.json` com o script para gerar pontuação.

## Script Utilitário

```bash
python3 scripts/score_component_rubric.py templates/rubrica-componentes.json --md /tmp/rubrica.md --csv /tmp/rubrica.csv
```

O script valida nível declarado, rebaixa falsos positivos e gera recomendação de evolução.

## Definition Of Done

- Cada componente tem definição N1/N2/N3.
- Evidência mínima está explícita.
- Falsos positivos foram listados.
- Nível validado não depende de opinião.
- Próximo passo de evolução está claro.
- Gaps acionáveis podem virar backlog.
