---
name: setup-meta-engajamento-remarketing
description: Estrutura campanhas Meta de engajamento/video para aquecer audiencia e alimentar remarketing com funcao clara no funil, publicos/exclusoes, janelas, criativos por hipotese, regra de entrada/saida e checklist N2. Use quando o plano de midia prever construcao de publico morno antes de oferta direta; nao use como substituto permanente de campanha de performance.
---

# Setup Meta Ads — Engajamento e remarketing

## Fonte canonica

Playbook **`15_SETUP_CAMPANHAS_META_ADS_CANONICO.md`**, subtipo de engajamento/construcao de audiencia dentro da estrutura Meta. Referencia operacional curta: `executar-ai/workshop/skills/10-3-meta-engajamento.md`.

## Principio

Engajamento so entra quando tem **funcao no funil**: aquecer publico, criar pool de remarketing, educar antes da oferta direta ou sustentar uma janela de recuperacao. Se a campanha nao aponta para o proximo passo, ela vira gasto de vaidade.

## Dependencias

- **`setup-campanhas-meta-ads`** — conta, pixel/CAPI quando aplicavel, publicos base, nomenclatura, matriz de testes e checklist geral.
- **`plano-midia-leadgen`** — papel do canal, objetivo, budget e janela de decisao.
- **`selecao-pack-criativo-ciclo`** ou **`briefing-criativo-video-first`** — criativos de educacao, prova, objecao ou aquecimento.
- **`gerador-taxonomia-utm-ids`** — IDs e nomes consistentes.
- **`funil-unificado-conversoes-a2`** e **`protocolo-handoff-mql-sql-a4`** — como o publico aquecido volta para captacao/MQL/SQL.

## Quando usar / quando nao usar

| Usar | Nao usar |
| --- | --- |
| Precisa aquecer publico frio antes de oferta direta | Como substituto eterno de lead/conversao |
| Precisa criar pool de remarketing por video, engajamento ou interacao | Quando nao ha campanha seguinte ou destino claro |
| O plano define janela, verba e criterio de leitura | Para perseguir metrica de vaidade sem impacto no funil |
| Ha criativos educativos/prova/objecao com hipotese | Sem regra de entrada/saida do publico aquecido |

## Inputs obrigatorios

- Plano de midia com objetivo Meta Engajamento, budget, janela e papel no funil.
- DEOC/DCC ou documento de comunicacao vigente com angulos, provas e restricoes.
- Pack/brief de criativos de engajamento com tema, hipotese e CTA leve.
- Publicos frios/mornos/quentes, exclusoes e anti-ICP.
- Regra de remarketing: publico criado, janela, destino e campanha seguinte.
- Taxonomia de campanha/conjunto/criativo.

## Workflow

1. Definir a **funcao no funil**: aquecer para qual etapa, campanha ou oferta seguinte.
2. Escolher objetivo Meta adequado: visualizacao de video, engajamento ou outro objetivo de construcao de audiencia previsto no plano.
3. Definir publico inicial e exclusoes: anti-ICP, convertidos, leads recentes, compradores e saturados quando aplicavel.
4. Definir **pool aquecido**: criterio de inclusao, janela, tamanho minimo esperado e destino no remarketing.
5. Montar matriz de criativos por hipotese: tema, angulo, prova, objecao, formato e `creative_id`.
6. Definir regra de entrada/saida: quando entra no remarketing, quando sai, para qual campanha vai e o que exclui.
7. Registrar budget, periodo, frequencia/pressao e metrica de leitura.
8. Preencher `templates/meta-engajamento-remarketing.md` ou o JSON e gerar consolidado.
9. No setup geral Meta, marcar `subtipos.engajamento_construcao_audiencia: true` e linkar este artefato.
10. Antes do ar, rodar `qa-go-live-meta-ads` e confirmar que o checklist geral reconhece este subtipo.

## Outputs

- Blueprint de campanha de engajamento/aquecimento.
- Publicos e exclusoes documentados.
- Regra de remarketing com janela e destino.
- Matriz de criativos por hipotese.
- Checklist N2 especifico do subtipo.

## Artefatos

- `reference.md`
- `templates/meta-engajamento-remarketing.md`
- `templates/meta-engajamento-remarketing.json`
- `scripts/build_meta_engajamento_remarketing.py`

## Scripts

```bash
python3 scripts/build_meta_engajamento_remarketing.py templates/meta-engajamento-remarketing.json --md ./engajamento-remarketing-saida.md
python3 scripts/build_meta_engajamento_remarketing.py templates/meta-engajamento-remarketing.json --audit
```

## Definition of Done

- Funcao no funil definida e linkada a uma campanha/etapa seguinte.
- Publico inicial, exclusoes e anti-ICP documentados.
- Pool aquecido definido com criterio, janela e destino.
- Criativos planejados por hipotese, nao apenas por formato.
- Matriz de testes e metricas de leitura registradas.
- Subtipo marcado no setup Meta geral.
- Go-live aprovado sem depender de metrica de vaidade como criterio unico.

## Armadilhas

- Rodar engajamento porque o CPM parece barato.
- Criar publico morno sem campanha seguinte.
- Misturar mensagens educativas e oferta direta sem criterio.
- Nao excluir convertidos/leads quando isso distorce leitura.
- Tratar view/engajamento como resultado final em leadgen.
