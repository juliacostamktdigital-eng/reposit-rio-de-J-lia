---
name: tese-estrategica-ucm
description: Organiza tese estratégica UCM com contexto, problema, Champion-tipo (não cliente genérico), JTBD core do Champion (solution-free, Ulwick ODI), Forces of Progress (push/pull/anxiety/habit, Bob Moesta), alternativa percebida, proposta de valor, mecanismo, inimigo, provas, narrativa central e tradução para ativos. Use quando o usuário mencionar UCM, planejamento estratégico de comunicação, tese de campanha ou quando for preciso alimentar DEOC, LP, mídia, criativos e vendas.
---

# Tese Estratégica UCM

## Quando Usar

Use depois de discovery e antes de DEOC, plano de mídia, briefing criativo, LP, script comercial ou taxonomia de testes.

Também use retroativamente quando DCC, LP ou campanhas nasceram de frases soltas e precisam de uma tese estratégica auditável.

## Inputs

- handoff sales-to-ops;
- discovery;
- site e materiais comerciais;
- histórico de campanhas;
- feedback de vendas;
- objeções reais;
- provas, cases e números;
- concorrentes e alternativas percebidas;
- restrições jurídicas, técnicas e comerciais.

## Estrutura Mínima

1. Contexto do negócio.
2. Problemas priorizados.
3. Personas e papéis de decisão.
4. Champion-tipo (perfil que vende internamente; tese gira em torno de armar ele — não cliente genérico).
5. JTBD core sintético (1 linha solution-free, padrão Ulwick ODI).
6. Alternativas percebidas.
7. Forces of Progress (push do status quo / pull da nova solução / anxiety da mudança / habit da inércia).
8. Frequência natural do problema.
9. Proposta de valor e mecanismo.
10. Inimigo/status quo.
11. Provas e autoridade.
12. Narrativa central.
13. Vocabulário estratégico.
14. Tradução para ativos.

## Workflow

1. Declare a batalha estratégica antes da copy.
2. Priorize problemas com impacto e voz do cliente.
3. Separe personas e papéis de decisão.
4. Defina o Champion-tipo (quem vende internamente) e escreva o JTBD core dele em 1 linha solution-free.
5. Mapeie alternativas percebidas e por que falham.
6. Aplique Forces of Progress (Bob Moesta) — identifique o struggling moment (instante exato em que o cliente percebe que precisa mudar) e as 4 forças:
   - push do status quo (dor que empurra);
   - pull da nova solução (atração);
   - anxiety da mudança (medo do novo);
   - habit da inércia (apego ao atual).
   A tese só vence quando push+pull > anxiety+habit.
7. Formule proposta de valor:

```text
Para [persona], que sofre com [problema], [produto/oferta] entrega [resultado] por meio de [mecanismo], sem [objeção], comprovado por [prova].
```

8. Defina inimigo/status quo.
9. Separe provas de claims pendentes.
10. Escreva narrativa central.
11. Traduza para DCC/DEOC, LP, criativos, mídia, comercial e tracking.

## Output Esperado

- tese estratégica resumida;
- problemas priorizados;
- narrativa central;
- proposta de valor;
- matriz de tradução para ativos;
- claims pendentes;
- próximos insumos para DEOC.

Use `templates/tese-ucm.md`.
Use `templates/tese-ucm.json` com o script para montar uma versão inicial.

## Script Utilitário

```bash
python3 scripts/build_ucm_thesis.py templates/tese-ucm.json --md /tmp/tese-ucm.md
```

## Definition Of Done

- A tese responde qual batalha está sendo travada.
- Problemas têm impacto e voz do cliente.
- Persona tem papel decisório e Champion-tipo está nomeado.
- JTBD core do Champion é solution-free (1 linha, padrão Ulwick).
- Forces of Progress mapeadas com struggling moment identificado.
- Proposta de valor tem mecanismo.
- Promessa forte aponta para prova ou claim pendente.
- Saída orienta ativos executáveis.
