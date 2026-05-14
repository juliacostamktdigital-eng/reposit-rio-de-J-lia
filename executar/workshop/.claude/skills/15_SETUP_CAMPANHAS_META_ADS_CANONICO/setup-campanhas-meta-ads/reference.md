# Referência — Setup Meta Ads (playbook 15)

Fonte: **`15_SETUP_CAMPANHAS_META_ADS_CANONICO.md`**. Uso operacional: preparação antes do go-live; não substitui políticas atuais da Meta nem revisão legal.

## 1. Princípio

Setup de campanha **não é execução**. É preparação para que a execução gere **aprendizado confiável**.

Antes de subir campanha, a conta precisa responder:

- a conta de anúncio está configurada?
- pixel/CAPI/eventos estão funcionando?
- públicos básicos existem?
- campanha, conjunto e anúncio têm IDs?
- a estrutura permite teste sem fragmentar demais?
- existe hipótese clara?
- existe plano de leitura?
- existe planilha backup e contrato de dados?

## 2. Referências externas citadas no canônico

- [Como escolher públicos no Meta Ads](https://pedrosobral.com.br/blog/c/introducao-ao-trafego-pago/como-escolher-publicos-no-meta-ads)
- [Como anunciar para o público certo no Meta Ads em 2025](https://pedrosobral.com.br/blog/c/introducao-ao-trafego-pago/como-anunciar-para-o-publico-certo-no-meta-ads-em-2025)
- [Os 3 tipos de campanha que todo gestor precisa dominar](https://pedrosobral.com.br/blog/c/introducao-ao-trafego-pago/os-3-tipos-de-campanha-que-todo-gestor-de-trafego-precisa-dominar-no-meta-ads)
- [Como criar campanhas no Meta Ads em 2026 — guia completo](https://pedrosobral.com.br/blog/c/estrategias-de-trafego-pago/como-criar-campanhas-no-meta-ads-em-2026-o-guia-completo-para-anunciar-no-instagram-facebook-e-whatsapp)

## 3. Inputs obrigatórios

- DEOC; plano de mídia; LP/ponto de conversão; contrato de dados; taxonomia UTM/IDs; criativos aprovados ou em fila final; planilha backup obrigatória; planilha de testes growth; CRM/SLA marketing-vendas; matriz de testes do ciclo; definição de lead correto e follow-up por tipo de campanha; acesso ao Business Manager, conta de anúncios, pixel, página, Instagram e domínio.

## 4. Checklist de conta

Antes de estruturar campanha:

- Business Manager correto; conta de anúncio correta; pagamento ativo;
- página Facebook vinculada; Instagram vinculado; domínio verificado quando aplicável;
- permissões do time conferidas; pixel instalado; CAPI configurada quando possível;
- eventos principais testados; eventos priorizados quando aplicável;
- UTMs preservadas na LP/formulário; planilha backup recebendo lead; CRM recebendo ou conciliável via backup.

## 5. Eventos e pixel

### Mínimos para leadgen

- `PageView`; `ViewContent` ou equivalente de visita qualificada; `Lead` no envio do formulário;
- evento customizado para `MQL` quando houver integração;
- evento customizado/offline para `SQL`, oportunidade ou venda quando houver volume e CRM.

### Regra

O evento de otimização deve ser o **mais profundo possível sem matar volume**. Sem volume: começar com `Lead`/formulário; qualidade comercial na planilha de growth; evoluir para MQL/SQL/offline quando houver dados.

## 6. Públicos padrão (resumo)

**Frios:** amplo/aberto; interesses; lookalikes 1% e 2–3%; localização pura (local); cargo/interesse quando precisar recorte.

**Mornos:** engajamento IG/FB 30D; visitantes site 30D; vídeo 50/75%; abertura de formulário sem envio; páginas-chave.

**Quentes:** leads capturados; CRM; visitantes LP 7D/14D; cliques/conversa iniciada; oportunidades; carrinho/checkout (ecommerce); exclusão de clientes em aquisição quando aplicável.

## 7. Princípios de públicos

- **Segmentação** vem de: público + objetivo + criativo + pixel/eventos.
- **Um passo antes** do objetivo final (ex.: venda → testar leads/visitantes de preço; MQL → visitantes qualificados e abriram formulário).
- **Temperatura separada:** aquisição / remarketing morno-quente / reativação-base (quando há volume).
- **Quantidade de conjuntos:** referência 3–6 inicial; limite comum 4–8; evitar 12+ sem motivo.
- **Exclusões:** aquisição exclui leads/clientes; remarketing exclui convertidos; evitar competição desnecessária entre quente e frio amplo.

## 8. Estrutura inicial recomendada

### Leadgen consultivo (exemplo canônico)

**Campanha 1 — aquisição / frio:** conjunto amplo/Advantage; interesses principais; lookalike 1–3% da melhor base; recorte cargo/interesse/local quando fizer sentido.

**Campanha 2 — remarketing morno-quente:** engajamento 30D; visitantes LP/site 30D; viewers vídeo ou form aberto sem envio; excluir leads já capturados se objetivo for novo lead.

**Campanha 3 — reativação/base:** leads antigos; oportunidades perdidas; só com base e oferta adequada.

### Orçamento baixo

- 1 campanha aquisição; 2–3 conjuntos; 3–5 anúncios por conjunto; remarketing só com público suficiente.

## 9. Tipos de campanha (objetivo)

| Tipo | Quando |
| --- | --- |
| Construção de público | marca sem audiência; pixel fraco; produto precisa contexto; venda direta fria improvável (vídeo, engajamento, tráfego qualificado). |
| Captação de leads | oferta clara; LP/form pronto; CRM/SLA; backup ativo; nativo com perguntas + SLA aceito **antes** de ativar. Destinos: nativo, LP, WhatsApp/mensagem (cada um muda tracking e SLA). |
| Venda/conversão | evento confiável; LP pronta; pixel/CAPI com sinal suficiente; volume justifica otimização profunda. |
| Engajamento/aquecimento | público para remarketing ou contexto; **não** substituto eterno de performance — regra de passagem para remarketing e leitura. |

## 10. Nomenclatura (taxonomia)

**Campanha:** `{campaign_id} | {tipo_campanha} | {objetivo} | {movimento} | {slug}`

**Conjunto:** `{adgroup_id} | {publico} | {temperatura} | {posicionamento} | {slug}`

**Anúncio:** `{creative_id} | {formato} | {hook} | {persona} | {slug} | {versao}`

Exemplos no canônico: `cmp-hs-prevent-202605-001 | aquisicao | mql | teste-oferta | antifraude-cfo` (campanha); `adg-hs-prevent-202605-003 | cfo-fintech | frio | interesses | cfo-antifraude` (conjunto); `crv-hs-prevent-202605-014 | video | roi | cfo | fraude-invisivel | v01` (criativo).

## 11. Criativos por conjunto

- 3–5 anúncios por conjunto; variações **reais** de hook/formato/persona; evitar peças quase iguais;
- cada criativo com `creative_id` e **hipótese de leitura**;
- exemplo de mix: vídeo dor; vídeo ROI; estático prova; carrossel educacional; depoimento.

## 12. Orçamento e aprendizado

- Evitar fragmentar verba em excesso de conjuntos; orçamento mínimo por conjunto para aprender;
- **CBO** quando a intenção é algoritmo distribuir; **ABO** quando precisa controlar verba por teste;
- não matar conjunto cedo sem volume; investigar conjunto que não gasta com hipótese clara.

## 13. Checklist antes do go-live

Campanha/conjunto/anúncio com ID; público e temperatura; exclusões; pixel/eventos testados; UTMs; backup testada; CRM/handoff testado; criativos aprovados; matriz de testes; lead nativo (campos/perguntas); regra de públicos de engajamento/vídeo; orçamento e datas; hipótese na planilha growth; change log preparado.

## 14. Critério N2

Setup Meta está N2 quando:

- conta, pixel e eventos configurados; públicos padrão criados;
- estrutura respeita objetivo e temperatura; IDs e nomes corretos;
- UTMs e campos `v4_*` aplicados; backup recebe lead teste;
- hipótese e critério de leitura registrados;
- subtipos lead nativo, conversão e engajamento com checklist específico quando usados;
- checklist de go-live preenchido.

## 15. Critério N3

Públicos vencedores versionados; exclusões em cadência; aprendizados na planilha growth; consolidação/separação baseada em dados; novos testes do debrief.

## 16. O que evitar

Campanha ou criativo sem ID; quente+frio misturados sem intenção; 12+ conjuntos com pouca verba; interesses minúsculos sem volume; remarketing sem excluir convertidos; criativo genérico sem segmentar pelo conteúdo; pixel não testado; lead sem backup; CPL sem qualidade comercial; lead nativo sem SLA/perguntas mínimas; conversão sem evento validado; engajamento eterno sem ponte para performance.
