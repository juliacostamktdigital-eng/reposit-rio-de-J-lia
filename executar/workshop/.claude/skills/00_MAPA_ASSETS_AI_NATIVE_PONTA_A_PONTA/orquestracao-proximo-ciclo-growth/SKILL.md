---
name: orquestracao-proximo-ciclo-growth
description: Orquestra o próximo ciclo de growth a partir de resultados, debriefs, backlog, decisões, padrões vencedores e anti-padrões. Use quando o usuário pedir rebrief, próximo ciclo, plano de ação pós-campanha, priorização de hipóteses, canonização de aprendizados ou atualização do pack sem recomeçar do zero.
---

# Orquestração Próximo Ciclo Growth

## Quando Usar

Use depois de um ciclo de execução quando existir pelo menos parte de:

- dados de mídia, LP, CRM, funil ou vendas;
- planilha de testes;
- debrief ou relatório de performance;
- decisões registradas;
- backlog de hipóteses;
- aprendizados, padrões vencedores ou anti-padrões;
- assets que precisam ser atualizados para o próximo ciclo.

Nao use para:

- planejar o primeiro ciclo sem insumos;
- substituir leitura especialista de mídia, CRM ou oferta;
- criar um novo plano ignorando o que foi aprendido;
- chamar opinião de aprendizado sem evidência e limite da conclusão.

## Inputs Necessários

- Resultado vs meta do ciclo.
- Testes rodados, hipóteses e variáveis.
- Métricas de mídia, conversão e qualidade comercial.
- Decisões tomadas: escalar, ajustar, matar, corrigir tracking, revisar oferta ou acionar vendas.
- Backlog atual.
- Mudanças feitas no ciclo e changelog.
- Padrões vencedores, perdedores e inconclusivos.
- Assets atuais: DEOC, plano de mídia, briefing criativo, LP, tracking, CRM/SLA.

Se faltar dado crítico, registre como lacuna e diferencie "hipótese provável" de "aprendizado comprovado".

## Workflow

1. Reconstrua o ciclo anterior: objetivo, hipóteses, assets usados, datas e mudanças relevantes.
2. Compare resultado vs meta em três camadas:
   - mídia e distribuição;
   - conversão/LP/tracking;
   - qualidade comercial/funil.
3. Classifique cada teste:
   - vencedor;
   - perdedor;
   - inconclusivo por volume;
   - inconclusivo por tracking;
   - inválido por execução.
4. Extraia aprendizados com evidência e limite da conclusão.
5. Atualize o backlog:
   - manter/escala;
   - ajustar e retestar;
   - matar;
   - criar novo teste;
   - corrigir tracking/dados;
   - revisar oferta/mensagem;
   - acionar vendas/SLA.
6. Defina o próximo ciclo com foco:
   - objetivo principal;
   - hipótese central;
   - assets que mudam;
   - assets que permanecem;
   - riscos e dependências;
   - métricas e janela de leitura.
7. Marque o que deve ser canonizado:
   - padrão vencedor;
   - anti-padrão;
   - ajuste de playbook;
   - skill candidata;
   - template reutilizável.
8. Gere brief do próximo ciclo e changelog.

## Output Esperado

Produza:

- resumo executivo do ciclo anterior;
- leitura por camada: mídia, conversão, tracking e vendas;
- decisões por hipótese;
- backlog priorizado do próximo ciclo;
- brief do próximo ciclo;
- changelog de assets;
- itens para biblioteca de padrões e anti-padrões;
- lacunas que impedem N3.

Use `templates/brief-proximo-ciclo.md` para o documento final.
Use `templates/backlog-proximo-ciclo.json` para consolidar backlog via script.

## Script Utilitário

Para ordenar backlog por prioridade e gerar Markdown/CSV:

```bash
python scripts/prioritize_backlog.py templates/backlog-proximo-ciclo.json --md /tmp/backlog-proximo-ciclo.md --csv /tmp/backlog-proximo-ciclo.csv
```

O script organiza por severidade, impacto, confianca e esforco. A decisão final continua humana.

## Definition Of Done

- O ciclo anterior foi reconstruído com evidências.
- Cada aprendizado tem evidência e limite.
- O backlog diferencia escala, ajuste, morte, correção e novo teste.
- O próximo ciclo tem objetivo, hipótese, métricas e janela de leitura.
- Mudanças em assets estão listadas em changelog.
- Padrões e anti-padrões candidatos foram separados.
- O time não precisa recomeçar discovery para executar o próximo ciclo.

## Armadilhas

- Gerar "próximos passos" genéricos sem decisão por hipótese.
- Escalar criativo vencedor por CPL sem qualidade comercial.
- Matar teste inconclusivo por volume baixo.
- Ignorar tracking quebrado e tirar conclusão de dado ruim.
- Atualizar assets sem changelog.
- Canonizar aprendizado que só vale para um caso sem registrar limite.

## Referências

- Playbook canônico: `assets/canonicos/00_MAPA_ASSETS_AI_NATIVE_PONTA_A_PONTA.md`
- Detalhamento: `reference.md`
- Template: `templates/brief-proximo-ciclo.md`
- Schema: `templates/backlog-proximo-ciclo.json`
