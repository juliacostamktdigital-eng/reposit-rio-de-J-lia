# Setup de Campanhas Google Ads Canônico
**Atualizado:** 2026-04-30  
**Fonte final:** consolidação em `assets/canonicos`; base canônica original + `assets/legacy/merge/skills/11-estrutura-campanhas-google-ads-search.md`, `assets/legacy/merge/skills/12-estrutura-campanhas-google-ads-pmax.md`, `assets/legacy/merge/skills/13-estrutura-campanhas-google-ads-display.md`.  
**Decisão de merge:** skills 11, 12 e 13 incorporadas em uma única fonte Google Ads, preservando Search, PMax e Display por seção.


Status: v1 para Marketing OS / EXECUTAR  
Escopo: preparação de conta, conversões, públicos, Search, Performance Max, asset groups, UTMs e critérios de go-live em Google Ads  
Objetivo: padronizar o setup Google Ads antes da execução, evitando campanha sem conversão confiável, sem estrutura de aprendizado e sem integração com CRM/planilha backup.

## 1. Princípio

Google Ads depende de intenção, conversão e qualidade de sinal.

Antes de rodar mídia, a operação precisa garantir:

- conta e faturamento funcionando;
- tag/GA4/GTM instalados;
- conversões configuradas corretamente;
- públicos e listas disponíveis;
- campanha estruturada sem fragmentar dados;
- termos, URLs e assets alinhados à oferta;
- UTMs e IDs aplicados;
- planilha backup e CRM prontos para reconciliar lead e qualidade.

## 2. Referências usadas

Este documento consolida:

- recomendações oficiais do Google sobre Performance Max, conversões, listas de remarketing, asset quality e learning;
- boas práticas de Search/Performance Max para leadgen;
- boas práticas recentes de consolidação, audience signals, Customer Match, enhanced conversions e importação de conversões offline.

Links úteis:

- https://support.google.com/google-ads/answer/10724896
- https://support.google.com/sa360/answer/12368425

## 3. Inputs obrigatórios

- DEOC;
- plano de mídia;
- LP/ponto de conversão;
- contrato de dados;
- taxonomia UTM/IDs;
- planilha backup obrigatória;
- CRM/SLA marketing-vendas;
- lista de palavras-chave ou temas de busca;
- lista de negativas iniciais;
- assets de texto, imagem e vídeo quando PMax/YouTube/Display;
- acesso Google Ads, GA4, GTM, Search Console quando aplicável.

## 4. Checklist de conta

Antes de criar campanha:

- conta Google Ads correta;
- faturamento ativo;
- permissões do time conferidas;
- auto-tagging avaliado;
- GA4 vinculado quando aplicável;
- Google Tag Manager publicado;
- tag Google instalada;
- conversões principais configuradas;
- enhanced conversions ativadas quando possível;
- importação offline planejada para MQL/SQL/venda quando houver CRM;
- listas de remarketing elegíveis;
- Customer Match preparado quando houver base;
- UTMs preservadas até CRM e planilha backup.

## 5. Conversões

### Conversões mínimas

- envio de formulário;
- clique ou envio WhatsApp quando for ponto de conversão real;
- ligação qualificada quando aplicável;
- MQL importado do CRM;
- SQL/oportunidade importado do CRM;
- venda/receita quando houver ciclo e dado.

### Regra de otimização

Otimizar para a conversão mais profunda que ainda tenha volume suficiente.

Se não há volume:

- começar com lead/formulário;
- medir qualidade via planilha de growth;
- importar MQL/SQL assim que houver consistência;
- diferenciar conversões principais de secundárias/observação.

## 6. GTM e parâmetros

Obrigatório validar:

- `gclid`;
- `gbraid` / `wbraid` quando aplicável;
- UTMs;
- `v4_client_id`;
- `v4_campaign_id`;
- `v4_adgroup_id`;
- `v4_creative_id`;
- `v4_test_id`;
- campos hidden no formulário;
- envio para planilha backup;
- envio para CRM.

Não publicar campanha Google sem testar submissão real de lead.

## 7. Estrutura Search

### Quando usar

Search é indicado quando há demanda ativa:

- busca por problema;
- busca por solução;
- busca por categoria;
- busca por concorrente quando permitido;
- busca de marca quando houver estratégia de defesa/captura.

### Estrutura inicial

Campanha Search 1: não-marca / intenção principal

- Grupo 00: problema direto;
- Grupo 01: solução/categoria;
- Grupo 02: comparativos/alternativas;
- Grupo 03: segmento/persona quando houver volume.

Campanha Search 2: marca

- separada para medir captura de demanda existente;
- pode ser desligada se não fizer sentido estratégico;
- não misturar com não-marca na leitura de aquisição.

Campanha Search 3: concorrentes

- usar apenas quando for permitido e estratégico;
- copy precisa respeitar regras legais e políticas de marca.

### Palavras-chave

Começar com:

- termos de alta intenção;
- correspondência de frase/exata para controle inicial;
- ampla apenas quando conversão e negativas estiverem maduras;
- negativas desde o dia 1.

## 8. Estrutura Performance Max

### Quando usar

PMax é indicado quando:

- conversão está bem configurada;
- há assets suficientes;
- há lista/audience signal relevante;
- há budget para aprendizado;
- o objetivo é expandir além de Search.

### Quando evitar no início

Evitar PMax se:

- conversão não está validada;
- LP/formulário não preserva dados;
- não há nenhum asset minimamente decente;
- budget é baixo demais;
- o cliente precisa de controle granular imediato;
- a conta ainda não tem sinais mínimos.

### Estrutura inicial

Campanha PMax 1: aquisição principal

- Asset group 00: oferta principal;
- Asset group 01: segmento/persona prioritária;
- Asset group 02: dor ou caso de uso prioritário.

Evitar asset groups demais no início. Para a maioria dos casos, 2 a 5 grupos são suficientes.

### Audience signals

Usar sinais, não como segmentação rígida:

- Customer Match;
- visitantes do site;
- leads/MQLs;
- termos de busca de alta intenção;
- URLs de concorrentes/referências;
- segmentos in-market relevantes;
- públicos do GA4.

Não sobrecarregar sinais. Começar com os sinais mais fortes e claros.

## 9. Assets para PMax

Por asset group, preparar:

- headlines curtas;
- headlines longas;
- descrições;
- imagens quadradas;
- imagens horizontais;
- imagens verticais quando possível;
- logo;
- vídeos próprios sempre que possível;
- URLs finais coerentes;
- extensões/assets de chamada, sitelink e snippet quando fizer sentido.

Regra: se não há vídeo próprio, a plataforma pode gerar vídeo automaticamente. Isso raramente representa o melhor padrão criativo. Preferir vídeos aprovados pelo DEOC/briefing criativo.

### Estrutura Display

Usar Display quando o Plano de Mídia definir função clara: alcance qualificado, remarketing, contextual, sustentação de awareness ou recuperação de intenção. A estrutura deve declarar targeting, exclusões anti-ICP, placements/apps bloqueados, brand safety, frequência, janela de remarketing, criativos por formato e métrica de leitura.

Display não deve entrar como sobra de verba nem como “barato para aparecer”. Sem exclusões, frequência e brand safety, ele gera falso aprendizado e tráfego de baixa qualidade.

## 10. Nomenclatura

### Campanha

```text
{campaign_id} | {tipo_campanha} | {objetivo} | {movimento} | {slug}
```

Exemplo Search:

```text
cmp-hs-prevent-202605-010 | search | mql | demanda-ativa | onboarding-digital
```

Exemplo PMax:

```text
cmp-hs-prevent-202605-011 | pmax | mql | expansao | antifraude-cfo
```

### Grupo / asset group

```text
{adgroup_id} | {intencao} | {temperatura} | {tipo} | {slug}
```

Exemplo:

```text
adg-hs-prevent-202605-020 | problema | quente | search | fraude-onboarding
```

### Asset/anúncio

```text
{creative_id} | {formato} | {hook} | {persona} | {slug} | {versao}
```

Exemplo:

```text
crv-hs-prevent-202605-030 | texto | risco | cfo | onboarding-fraude | v01
```

## 11. Negativas e exclusões

Criar lista inicial:

- vagas/emprego;
- grátis/free quando não for estratégia;
- curso/aula quando não for oferta;
- PDF/modelo/template quando não for desejado;
- termos irrelevantes do segmento;
- regiões fora do escopo;
- marca do cliente em campanha não-marca quando a leitura exigir aquisição pura.

Revisar termos de busca na primeira semana e em cadência semanal no início.

## 12. Orçamento e aprendizado

Princípios:

- não fragmentar campanha demais;
- permitir período mínimo de aprendizado;
- evitar mudanças grandes antes da janela de leitura;
- ajustar orçamento gradualmente;
- usar tCPA/tROAS apenas quando houver histórico suficiente;
- começar com maximizar conversões quando o objetivo é gerar volume inicial;
- importar conversões offline para ensinar qualidade.

PMax pode oscilar no aprendizado. Não alterar diariamente sem evidência.

## 13. Estrutura inicial recomendada

### Setup Google mínimo para leadgen

- 1 campanha Search não-marca;
- 1 campanha Search marca quando necessário;
- 1 campanha remarketing/Display/YouTube apenas se houver público e objetivo;
- PMax somente se conversões/assets/sinais estiverem adequados.

### Setup Google com mais maturidade

- Search não-marca por intenção;
- Search marca separada;
- PMax aquisição com asset groups por oferta/segmento;
- remarketing com audiência e mensagem própria;
- importação offline de MQL/SQL/venda.

## 14. Checklist antes do go-live

- conversões testadas;
- enhanced conversions avaliadas;
- UTMs e IDs aplicados;
- lead teste chegou na planilha backup;
- CRM recebeu ou será conciliado;
- Search com negativas iniciais;
- PMax com assets suficientes;
- audience signals configurados;
- Search com clusters, negativas e RSAs conferidos quando aplicável;
- PMax com asset groups, URL expansion, brand controls e metas de conversão conferidos quando aplicável;
- Display com placements/apps, frequência, exclusões e brand safety conferidos quando aplicável;
- URLs finais conferidas;
- orçamento, lances e datas conferidos;
- hipótese registrada na planilha de growth;
- change log preparado para mudanças de estrutura, termos, assets, audience signals, placements ou orçamento.

## 15. Critério N2

Setup Google está N2 quando:

- conta e faturamento estão prontos;
- GTM/tag/conversões estão funcionando;
- UTMs e IDs estão aplicados;
- estrutura Search/PMax está documentada;
- públicos/listas/sinais foram configurados;
- planilha backup captura lead teste;
- hipótese e critério de leitura estão registrados.

## 16. Critério N3

Setup Google está N3 quando:

- MQL/SQL/venda voltam para Google via importação offline;
- termos de busca e negativas são revisados em cadência;
- asset performance alimenta novos criativos;
- PMax/Search são separados ou consolidados por dados;
- decisões de orçamento usam qualidade comercial, não só CPL.

## 17. O que evitar

- campanha sem conversão testada;
- PMax sem asset decente;
- PMax sem audience signal;
- misturar marca e não-marca sem leitura separada;
- otimizar para clique quando o objetivo é lead qualificado;
- não importar qualidade offline;
- rodar Search sem negativas;
- alterar budget/lance todo dia;
- lead sem planilha backup;
- avaliar Google só por CPL sem MQL/SQL.
