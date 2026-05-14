# Referência — Benchmark Para Backlog Growth

**Fonte normativa:** `assets/canonicos/12_BENCHMARK_MERCADO_TAM_SAM_SOM_CANONICO.md`.

Este arquivo expande trechos do playbook que governam **hipóteses testáveis** e **encerramento** do trabalho de benchmark. Leia o playbook completo quando houver dúvida de N2/N3 do pacote institucional inteiro.

## Princípio (Seção 1)

Benchmark sem evidência ou sem ligação com decisão vira teatro: tudo que entra no dossiê deve ter **lastro** (print, link, nota de fonte, premissa explícita). O backlog desta skill exige **evidência** por hipótese, mesmo que seja “premissa documentada + risco registrado”.

## Anti-padrão Direto (Seção 3.3)

O benchmark **não** pode ser “pesquisa infinita sem decisão nem backlog”. O trabalho precisa encerrar em **entregáveis e hipóteses testáveis**. Esta skill é o encerramento operacional dessa obrigação.

## Passo 7 Do Fluxo (Seção 5)

> Gerar backlog de hipóteses testáveis com **prioridade** e **métrica de sucesso** (CPL, CAC, CTR, taxa de conversão, conforme objetivo).

Interpretação operacional:

- **Prioridade** = função de impacto esperado, confiança na evidência, esforço de implementação e risco de erro.
- **Métrica** deve ser **uma primária** por hipótese (evitar otimizar três métricas ao mesmo tempo sem hierarquia).

## Consumidores Da Saída (Seção 7)

O pacote de benchmark alimenta:

- DEOC e assets de narrativa;
- **plano de mídia** (canais, campanhas, cadência);
- **planilha ou backlog de testes** (hipóteses priorizadas e métrica de sucesso).

Por isso cada hipótese deve indicar **asset impactado** e, quando possível, compatibilidade com `test_id` / taxonomia de testes (`montar-planilha-testes-growth`).

## Como Alimenta Os Assets (Seção 8)

Use o benchmark para decidir explicitamente:

- canal prioritário;
- segmento inicial;
- ICP/persona foco;
- promessa mais defensável;
- tipo de campanha;
- tipo de LP;
- provas necessárias;
- risco de mercado;
- esforço de diferenciação;
- **hipótese de mídia**.

Traduza cada decisão “grande” em **uma ou mais hipóteses** com métrica.

## Componentes Críticos (Seção 9)

Iterar com rigor:

- **Backlog de hipóteses:** testável, com métrica, **priorizado** e **rastreável** até teste e aprendizado.

Checklist interno por item:

- [ ] Se eu mudar o texto da hipótese, ainda sei **como medir**?
- [ ] Se o teste rodar, sei **qual asset** muda?
- [ ] Há **linha no changelog** para fechar o loop?

## DoD Mínimo Do Entregável Global (Seção 10.1 — item backlog)

O checklist operacional do benchmark exige:

- Backlog de hipóteses com **prioridade** e **métrica** (CPL, CAC, CTR, conversão, conforme objetivo).

Esta skill ajuda a auditar esse item: o script pode sinalizar quando **não há hipóteses** ou quando falta métrica/evidência.

## Gestão Contínua E Changelog (Seção 12)

- **KPIs sugeridos:** % de hipóteses testadas; impacto médio; tempo de ciclo hipótese → teste → aprendizado.
- **Semáforo:**
  - **Verde:** backlog atualizado e hipóteses testadas na cadência combinada;
  - **Amarelo:** muito dado, pouca decisão ou pouco teste;
  - **Vermelho:** benchmark não gera mudança em plano de mídia ou dossiê por **dois ciclos** seguidos.
- **Registro obrigatório:** changelog do que mudou no ciclo **benchmark → decisão → teste → resultado**.

Modelo de linha de changelog (preencher ao longo do tempo):

| Data | Benchmark observado | Decisão | Teste executado | Resultado | Próximo passo |
| --- | --- | --- | --- | --- | --- |

## Relação Com Outras Skills

| Skill | Papel |
| --- | --- |
| `benchmark-campo-batalha-gtm` | Insurge padrões, gaps e evidências brutas |
| `sizing-mercado-tam-sam-som` | Limita expectativa numérica e viabilidade |
| `posicionamento-competitivo-beachhead` | Recorta segmento e eixos competitivos |
| `montar-planilha-testes-growth` | Destino estrutural dos IDs e abas |
| `plano-midia-leadgen` | Converte hipóteses em estrutura de investimento |
| `debrief-aprendizados-growth` | Fecha o loop pós-teste e atualiza changelog |

## O Que Evitar (alinhado Seção 13)

- hipótese sem métrica;
- priorização só por “achismo” sem vínculo com evidência;
- backlog maior que a capacidade de teste do time;
- copiar concorrente sem hipótese explícita de **por que** aquilo deveria funcionar na sua conta.
