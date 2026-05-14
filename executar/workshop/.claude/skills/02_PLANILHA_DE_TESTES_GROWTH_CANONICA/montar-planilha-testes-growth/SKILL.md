---
name: montar-planilha-testes-growth
description: Cria ou audita a estrutura da planilha canônica de testes de growth com abas, colunas, dicionário de campos, IDs, hipóteses, mídia, leads, funil e aprendizados. Use quando montar base de testes, organizar planilha de growth, preparar N2/N3, registrar hipóteses ou estruturar dados para debrief.
---

# Montar Planilha Testes Growth

## Quando Usar

Use quando precisar:

- criar a planilha/base canônica de testes;
- auditar se uma planilha existente está N2;
- definir abas e colunas mínimas;
- ligar hipóteses, campanhas, criativos, leads e funil;
- preparar dados para leitura de performance, debrief e próximo ciclo;
- padronizar uma operação que está olhando só métricas de plataforma.

Não use para ler performance em profundidade. Para isso, use a futura skill `leitura-performance-growth-n3`.

## Inputs Necessários

- Cliente, cohort, segmento e período.
- Plano de mídia.
- Taxonomia UTM/IDs.
- DEOC/DCC ou fonte de copy/oferta.
- CRM, funil e critérios MQL/SQL.
- Campanhas, ad groups e criativos planejados.
- LP/ponto de conversão e fonte de leads.
- Métricas e metas do ciclo.

Se algum input não existir, a planilha deve marcar lacuna em vez de fingir completude.

## Workflow

1. Defina o objetivo da planilha: setup inicial, auditoria, ciclo ativo ou pós-ciclo.
2. Crie ou valide as abas obrigatórias:
   - `00_README`;
   - `01_TESTES`;
   - `02_CRIATIVOS`;
   - `03_CAMPANHAS`;
   - `04_ADGROUPS`;
   - `05_LEADS_FUNIL`;
   - `06_PERFORMANCE_MIDIA`;
   - `07_PERFORMANCE_FUNIL`;
   - `08_APRENDIZADOS`.
3. Garanta que IDs conectam as abas:
   - `test_id`;
   - `campaign_id`;
   - `adgroup_id`;
   - `creative_id`;
   - `lead_id`.
4. Para cada teste, registre hipótese, variável testada, variáveis controladas, métrica primária e critério de decisão.
5. Para cada criativo, registre atributos analisáveis: formato, hook, persona, dor, desejo, ângulo, etapa e versão.
6. Para leads, preserve UTMs, IDs, status, qualidade comercial e timestamps.
7. Para performance, separe mídia de funil e qualidade comercial.
8. Crie aba de aprendizados com evidência, limite da conclusão e recomendação.
9. Valide critérios N2 e marque lacunas.

## Output Esperado

Produza:

- estrutura da planilha;
- dicionário de abas e campos;
- checklist N2;
- campos faltantes;
- regras de preenchimento;
- CSVs ou XLSX quando solicitado;
- recomendações de manutenção.

Use `templates/estrutura-planilha-growth.md` para especificação.
Use `templates/planilha-growth-schema.json` com o script para gerar CSVs e opcionalmente XLSX.

## Script Utilitário

Para gerar arquivos CSV por aba e documentação Markdown:

```bash
python scripts/build_growth_workbook.py templates/planilha-growth-schema.json --out /tmp/planilha-growth --md /tmp/planilha-growth.md
```

Para tentar gerar XLSX também, se `openpyxl` estiver instalado:

```bash
python scripts/build_growth_workbook.py templates/planilha-growth-schema.json --out /tmp/planilha-growth --xlsx /tmp/planilha-growth.xlsx
```

## Definition Of Done

- Todas as abas obrigatórias existem.
- Toda campanha, criativo e teste tem ID.
- Todo lead pode ser ligado a campanha/criativo quando houver dados.
- Cada teste tem hipótese e variável.
- A leitura inclui qualidade comercial, não só CPL.
- Existe espaço para decisão e aprendizado.
- Campos faltantes foram documentados.

## Armadilhas

- Criar relatório de mídia e chamar de planilha de testes.
- Teste sem hipótese.
- Criativo sem atributo.
- Campanha sem objetivo claro.
- Lead sem UTM ou ID.
- Decisão sem aprendizado.
- Mudar várias variáveis sem registrar.
- Não separar performance de mídia e performance de funil.

## Referências

- Playbook canônico: `assets/canonicos/02_PLANILHA_DE_TESTES_GROWTH_CANONICA.md`
- Detalhamento: `reference.md`
- Template: `templates/estrutura-planilha-growth.md`
- Schema: `templates/planilha-growth-schema.json`
