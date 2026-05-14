# Setup de Campanhas Meta Ads Canônico
**Atualizado:** 2026-04-30  
**Fonte final:** consolidação em `assets/canonicos`; base canônica original + `assets/legacy/merge/skills/10-estrutura-campanhas-meta-ads.md`, `assets/legacy/merge/skills/10-1-meta-lead-nativo.md`, `assets/legacy/merge/skills/10-2-meta-conversao.md`, `assets/legacy/merge/skills/10-3-meta-engajamento.md`.  
**Decisão de merge:** skills 10, 10-1, 10-2 e 10-3 incorporadas em uma única fonte Meta Ads, preservando subtipos por seção.


Status: v1 para Marketing OS / EXECUTAR  
Escopo: preparação de conta, pixel, públicos, estrutura de campanhas, conjuntos e anúncios antes do go-live em Meta Ads  
Objetivo: impedir que a operação pule de plano/asset direto para campanha no ar sem preparar conta, públicos, tracking, nomenclatura, estrutura de teste e critérios de leitura.

## 1. Princípio

Setup de campanha não é execução. É a preparação para que a execução gere aprendizado confiável.

Antes de subir campanha, a conta precisa responder:

- a conta de anúncio está configurada?
- pixel/CAPI/eventos estão funcionando?
- públicos básicos existem?
- campanha, conjunto e anúncio têm IDs?
- a estrutura de campanha permite teste sem fragmentar demais?
- existe hipótese clara?
- existe plano de leitura?
- existe planilha backup e contrato de dados?

## 2. Referências usadas

Este documento consolida:

- princípios de públicos e campanhas do Pedro Sobral/Subido;
- boas práticas de Meta Ads sobre estrutura campanha/conjunto/anúncio;
- boas práticas recentes de simplificação de estrutura, separação por intenção/temperatura, públicos personalizados, semelhantes, exclusões e 3-5 variações criativas por conjunto.

Links úteis:

- https://pedrosobral.com.br/blog/c/introducao-ao-trafego-pago/como-escolher-publicos-no-meta-ads
- https://pedrosobral.com.br/blog/c/introducao-ao-trafego-pago/como-anunciar-para-o-publico-certo-no-meta-ads-em-2025
- https://pedrosobral.com.br/blog/c/introducao-ao-trafego-pago/os-3-tipos-de-campanha-que-todo-gestor-de-trafego-precisa-dominar-no-meta-ads
- https://pedrosobral.com.br/blog/c/estrategias-de-trafego-pago/como-criar-campanhas-no-meta-ads-em-2026-o-guia-completo-para-anunciar-no-instagram-facebook-e-whatsapp

## 3. Inputs obrigatórios

- DEOC;
- plano de mídia;
- LP/ponto de conversão;
- contrato de dados;
- taxonomia UTM/IDs;
- criativos aprovados ou em fila final;
- planilha backup obrigatória;
- planilha de testes growth;
- CRM/SLA marketing-vendas;
- matriz de testes do ciclo: o que varia e o que fica constante;
- definição de lead correto e follow-up por tipo de campanha;
- acesso ao Business Manager, conta de anúncios, pixel, página, Instagram e domínio.

## 4. Checklist de conta

Antes de estruturar campanha:

- Business Manager correto;
- conta de anúncio correta;
- método de pagamento ativo;
- página Facebook vinculada;
- Instagram vinculado;
- domínio verificado quando aplicável;
- permissões do time conferidas;
- pixel instalado;
- CAPI configurada quando possível;
- eventos principais testados;
- eventos priorizados quando aplicável;
- UTMs preservadas na LP/formulário;
- planilha backup recebendo lead;
- CRM recebendo ou sendo conciliado depois via backup.

## 5. Eventos e pixel

### Eventos mínimos para leadgen

- `PageView`;
- `ViewContent` ou equivalente de visita qualificada;
- `Lead` no envio do formulário;
- evento customizado para `MQL` quando houver integração;
- evento customizado/offline para `SQL`, oportunidade ou venda quando houver volume e CRM.

### Regra

O evento de otimização deve ser o mais profundo possível sem matar volume.

Se ainda não há volume:

- começar com `Lead` ou evento de formulário;
- usar qualidade comercial na planilha de growth;
- evoluir para MQL/SQL/offline conversion quando houver dados suficientes.

## 6. Públicos padrão

### Públicos frios

Usar para aquisição/prospecção:

- amplo/aberto quando o criativo segmenta bem;
- interesses por segmento;
- interesses empilhados quando fizer sentido;
- lookalike 1%;
- lookalike 2-3%;
- localização pura para negócios locais;
- cargo/interesse quando o nicho exigir recorte.

### Públicos mornos

Usar para pessoas com algum contato:

- engajamento Instagram/Facebook 30D;
- visitantes do site 30D;
- visualizadores de vídeo 50% ou 75%;
- aberturas de formulário sem envio;
- visitas em páginas-chave.

### Públicos quentes

Usar para maior intenção:

- leads capturados;
- lista CRM;
- visitantes de LP/formulário 7D/14D;
- pessoas que clicaram ou iniciaram conversa;
- oportunidades abertas;
- carrinho/checkout quando ecommerce existir;
- listas de clientes para exclusão ou upsell.

## 7. Princípios de públicos

### 7.1 Segmentação não é só público

No Meta, segmentação vem de quatro lugares:

- público configurado;
- objetivo da campanha;
- criativo;
- pixel/eventos.

Se o criativo fala com a pessoa errada, a campanha tende a aprender errado mesmo com público aparentemente certo.

### 7.2 Públicos do passo anterior

Priorizar públicos que estão um passo antes do objetivo final.

Exemplos:

- quer venda? testar leads, visitantes de página de preço, conversas iniciadas;
- quer MQL? testar visitantes qualificados e pessoas que abriram formulário;
- quer audiência? testar vídeo/engajamento/conteúdo.

### 7.3 Temperatura separada

Evitar misturar público quente e frio sem intenção.

Preferir:

- campanha de aquisição/frio;
- campanha de remarketing/morno-quente;
- campanha de reativação/base quando houver volume.

### 7.4 Quantidade de conjuntos

Como referência operacional:

- campanha inicial: 3 a 6 conjuntos;
- limite comum: 4 a 8 conjuntos;
- evitar 12+ conjuntos sem motivo, porque fragmenta orçamento e aprendizado.

### 7.5 Exclusões

Evitar sobreposição desnecessária.

Exemplos:

- aquisição exclui leads/clientes;
- remarketing exclui convertidos;
- conjunto 01 pode excluir conjunto 00 quando houver hierarquia de públicos;
- listas quentes não devem competir com público frio amplo.

## 8. Estrutura inicial recomendada

### Estrutura simples para leadgen B2B/B2C consultivo

Campanha 1: aquisição / público frio

- Conjunto 00: amplo ou Advantage/broad;
- Conjunto 01: interesses principais do segmento;
- Conjunto 02: lookalike 1-3% da melhor base disponível;
- Conjunto 03: público segmentado por cargo/interesse/local quando fizer sentido.

Campanha 2: remarketing / público morno-quente

- Conjunto 00: engajamento IG/FB 30D;
- Conjunto 01: visitantes LP/site 30D;
- Conjunto 02: vídeo viewers 50/75% ou formulário aberto sem envio;
- excluir leads já capturados quando o objetivo for novo lead.

Campanha 3: reativação/base

- Conjunto 00: leads antigos sem oportunidade;
- Conjunto 01: clientes ou oportunidades perdidas;
- usar apenas quando houver base e oferta adequada.

### Estrutura mínima quando budget é baixo

Se budget é baixo, consolidar:

- 1 campanha aquisição;
- 2 a 3 conjuntos;
- 3 a 5 anúncios por conjunto;
- remarketing só se houver público suficiente.

## 9. Tipos de campanha

### Construção de público

Objetivo: criar audiência qualificada para usar depois.

Usar quando:

- marca ainda não tem público;
- pixel sem dados;
- produto precisa de contexto;
- venda direta para frio é improvável.

Exemplos:

- vídeo views;
- engajamento;
- tráfego qualificado para conteúdo/LP.

### Captação de leads

Objetivo: coletar contato qualificado. Separar explicitamente formulário nativo, LP/formulário externo e WhatsApp/mensagem, porque cada destino muda qualidade, fricção, tracking e SLA.

Usar quando:

- há oferta clara;
- LP/formulário está pronto;
- CRM/SLA existe;
- planilha backup está ativa;
- formulário nativo tem perguntas suficientes para intenção/qualificação sem matar volume;
- SLA de follow-up está aceito antes de ativar lead nativo.

Exemplos:

- formulário nativo;
- LP com formulário;
- WhatsApp/mensagem.

### Venda/conversão

Objetivo: compra, agendamento, oportunidade ou venda. Usar quando o evento do site é confiável, a LP está pronta e pixel/CAPI conseguem preservar sinal suficiente para otimização.

Usar quando:

- evento de conversão está validado;
- há volume suficiente;
- ciclo e valor justificam otimização mais profunda.

### Engajamento e aquecimento

Objetivo: criar público qualificado para remarketing ou dar contexto quando venda direta para frio é improvável. Não deve virar substituto eterno de campanha de performance: precisa de regra de passagem para remarketing, janela de público, criativos por hipótese e leitura de contribuição.

## 10. Nomenclatura

Usar o padrão da taxonomia:

### Campanha

```text
{campaign_id} | {tipo_campanha} | {objetivo} | {movimento} | {slug}
```

Exemplo:

```text
cmp-hs-prevent-202605-001 | aquisicao | mql | teste-oferta | antifraude-cfo
```

### Conjunto

```text
{adgroup_id} | {publico} | {temperatura} | {posicionamento} | {slug}
```

Exemplo:

```text
adg-hs-prevent-202605-003 | cfo-fintech | frio | interesses | cfo-antifraude
```

### Anúncio

```text
{creative_id} | {formato} | {hook} | {persona} | {slug} | {versao}
```

Exemplo:

```text
crv-hs-prevent-202605-014 | video | roi | cfo | fraude-invisivel | v01
```

## 11. Padrão de criativos por conjunto

Começar com:

- 3 a 5 anúncios por conjunto;
- variações reais de hook/formato/persona;
- não subir cinco peças quase iguais;
- cada criativo precisa de `creative_id`;
- cada criativo precisa ter hipótese de leitura.

Exemplo:

- vídeo dor;
- vídeo ROI;
- estático prova;
- carrossel educacional;
- depoimento/autoridade.

## 12. Orçamento e aprendizado

Regras práticas:

- evitar fragmentar verba em conjuntos demais;
- garantir orçamento mínimo para cada conjunto aprender;
- usar CBO quando a intenção é deixar o algoritmo distribuir;
- usar ABO apenas quando a operação precisa controlar verba por público/teste;
- não matar conjunto cedo demais sem volume;
- não forçar orçamento em conjunto que a plataforma não quer gastar sem hipótese clara.

## 13. Checklist antes do go-live

- campanha criada com ID;
- conjuntos criados com ID;
- anúncios criados com ID;
- público e temperatura corretos;
- exclusões aplicadas;
- pixel/eventos testados;
- UTMs aplicadas;
- planilha backup testada;
- CRM/handoff testado;
- criativos aprovados;
- matriz de testes registrada;
- campos e perguntas do lead nativo conferidos quando aplicável;
- regra de criação/uso de públicos de engajamento e vídeo definida quando aplicável;
- orçamento e datas conferidos;
- hipótese registrada na planilha de growth;
- change log preparado para mudanças de estrutura, público, criativo, evento ou orçamento.

## 14. Critério N2

Setup Meta está N2 quando:

- conta, pixel e eventos estão configurados;
- públicos padrão foram criados;
- estrutura de campanha respeita objetivo e temperatura;
- campanha/conjunto/anúncio têm IDs e nomes corretos;
- UTMs e campos `v4_*` estão aplicados;
- planilha backup recebe lead teste;
- hipótese e critério de leitura estão registrados;
- subtipos lead nativo, conversão e engajamento têm checklist específico quando usados;
- checklist de go-live está preenchido.

## 15. Critério N3

Setup Meta está N3 quando:

- públicos vencedores são versionados;
- exclusões são revisadas em cadência;
- aprendizados por público/hook/formato entram na planilha de growth;
- campanhas são consolidadas ou separadas com base em dados;
- novos testes nascem do debrief, não de improviso.

## 16. O que evitar

- campanha sem ID;
- criativo sem ID;
- público quente e frio misturados sem intenção;
- 12+ conjuntos com pouca verba;
- muitos interesses pequenos sem volume;
- remarketing sem exclusão de convertidos;
- criativos genéricos que não segmentam pelo próprio conteúdo;
- pixel/evento não testado;
- lead sem planilha backup;
- otimizar só por CPL sem qualidade comercial;
- lead nativo sem SLA ou sem perguntas mínimas;
- conversão no site sem evento validado;
- engajamento usado indefinidamente sem ponte para remarketing/performance.
