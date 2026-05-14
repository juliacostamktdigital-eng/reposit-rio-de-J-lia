# Taxonomia Canônica de UTM, IDs e Subparâmetros
**Atualizado:** 2026-04-30  
**Fonte final:** consolidação em `assets/canonicos`; base canônica original + canônico original sem skill merge dedicada.  
**Decisão de merge:** sem skill dedicada; mantido como padrão transversal obrigatório para mídia, tracking e CRM.


Status: v1 para workshop  
Escopo: campanhas de geração de demanda qualificada em Inside Sales / leadgen  
Objetivo: permitir análise ponta a ponta entre investimento, campanha, criativo, lead, MQL, SQL, oportunidade e venda.

## 1. Princípio

A UTM não serve só para saber "veio do Meta". Ela precisa ser a ponte entre:

```text
investimento -> campanha -> conjunto/ad group -> criativo -> lead -> MQL -> SQL -> oportunidade -> venda
```

Se essa ponte quebra, o time passa a otimizar por métricas superficiais, como CPL, sem saber quais padrões realmente geram demanda qualificada.

## 2. Regra de ouro

UTM e nomenclatura são parte do processo de growth, não burocracia.

O padrão deve permitir responder:

- qual canal trouxe o lead;
- qual campanha trouxe o lead;
- qual conjunto/ad group trouxe o lead;
- qual criativo trouxe o lead;
- qual formato de criativo performou;
- qual hook performou;
- qual dor/desejo performou;
- qual ICP/persona performou;
- qual ângulo performou;
- qual versão performou;
- qual etapa do funil performou;
- qual combinação gerou MQL/SQL/venda, não apenas lead.

## 3. Convenções gerais

### Princípio de simplicidade

O nome visível na plataforma deve ser curto o suficiente para o time operar sem medo de errar.

A análise pós-campanha não deve depender de nomes enormes. Ela deve depender de:

- ID único no começo do nome;
- poucos atributos essenciais no nome visível;
- subparâmetros parseáveis nas UTMs e/ou na planilha;
- campos próprios (`v4_*`) sempre que possível.

Regra prática:

```text
nome visível = ID + 3 a 5 dimensões humanas + slug descritivo
análise = IDs + subparâmetros parseados + planilha de growth
```

Se o nome virar uma frase, está complexo demais.

### Normalização

Usar sempre:

- letras minúsculas;
- sem acentos;
- sem espaços;
- `-` para separar palavras dentro de um valor;
- `__` para separar blocos/dimensões;
- prefixos curtos para facilitar leitura;
- valores estáveis, não frases longas.

Exemplo:

```text
hook-roi
dor-fraude
per-cfo
fmt-video
ang-risco-financeiro
```

### Separadores

Separador entre dimensões:

```text
__
```

Separador entre chave e valor:

```text
-
```

Exemplo:

```text
fmt-video__per-cfo__hook-roi__dor-fraude__ang-risco-financeiro
```

## 4. IDs canônicos

### ID do cliente

Formato:

```text
cli-{slug_cliente}
```

Exemplos:

```text
cli-hs-prevent
cli-prado-goncalves
cli-g4-frontier
```

### ID da campanha

Formato:

```text
cmp-{cliente}-{ano}{mes}-{sequencial}
```

Exemplo:

```text
cmp-hs-prevent-202605-001
```

### ID do conjunto/ad group

Formato:

```text
adg-{cliente}-{ano}{mes}-{sequencial}
```

Exemplo:

```text
adg-hs-prevent-202605-003
```

### ID do criativo

Formato:

```text
crv-{cliente}-{ano}{mes}-{sequencial}
```

Exemplo:

```text
crv-hs-prevent-202605-014
```

### ID do teste

Formato:

```text
tst-{cliente}-{ano}{mes}-{sequencial}
```

Exemplo:

```text
tst-hs-prevent-202605-004
```

## 5. UTM source

Define a origem/plataforma.

Valores recomendados:

```text
meta
google
linkedin
tiktok
youtube
email
whatsapp
crm
organic
referral
direct
offline
```

Exemplo:

```text
utm_source=meta
```

## 6. UTM medium

Define o tipo de mídia/canal.

Valores recomendados:

```text
paid_social
paid_search
display
video
organic_social
email
crm
referral
partner
offline
```

Exemplo:

```text
utm_medium=paid_social
```

## 7. UTM campaign

Define a campanha em nível estratégico.

A campanha deve falar mais sobre o tipo de campanha, objetivo, movimento e um slug descritivo. Cohort, segmento e período podem aparecer como subparâmetros para análise, mas não devem poluir o nome visível.

Formato:

```text
{campaign_id}__typ-{tipo_campanha}__obj-{objetivo}__mov-{movimento}__slug-{slug}__coh-{cohort}__seg-{segmento}__per-{periodo}
```

Subparâmetros:

- `campaign_id`: ID único da campanha.
- `typ`: tipo da campanha.
- `obj`: objetivo da campanha.
- `mov`: movimento estratégico/tático.
- `slug`: descrição curta da campanha.
- `coh`: cohort/modelo de negócio.
- `seg`: segmento.
- `per`: período ou safra.

Valores de tipo de campanha:

```text
aquisicao
remarketing
reativacao
validacao-oferta
captura-demanda
geracao-demanda
conteudo
prova
evento
```

Valores de objetivo:

```text
leadgen
mql
sql
venda
remarketing
branding
trafego
engajamento
conversao
cadastro
```

Valores de movimento:

```text
lancamento
always-on
teste-oferta
teste-canal
teste-criativo
escala-vencedor
retomada
prova-social
quebra-crenca
demanda-fria
demanda-quente
```

Exemplo:

```text
utm_campaign=cmp-hs-prevent-202605-001__typ-aquisicao__obj-mql__mov-teste-oferta__slug-antifraude-cfo__coh-b2b-high-ticket__seg-antifraude__per-2026q2
```

## 8. UTM content

Define o criativo e seus atributos analisáveis.

Formato:

```text
{creative_id}__fmt-{formato}__hook-{tipo_hook}__per-{persona}__slug-{slug}__dor-{dor}__ang-{angulo}__stage-{etapa}__ver-{versao}
```

Subparâmetros:

- `creative_id`: ID único do criativo.
- `fmt`: formato.
- `hook`: tipo de hook.
- `per`: persona.
- `slug`: descrição curta do criativo.
- `dor`: dor central.
- `ang`: ângulo criativo.
- `stage`: etapa do funil.
- `ver`: versão.

Valores de formato:

```text
video
static
carousel
ugc
founder
demo
proof
lp
email
whatsapp
```

Valores de persona/ICP:

```text
cfo
ceo
cto
head-growth
head-produto
gestor-comercial
founder
investidor
comprador-final
```

Valores de hook:

```text
dor
npa
noticia
beneficio
roi
medo
prova
autoridade
comparativo
diagnostico
urgencia
status
curiosidade
erro-comum
mito
antes-depois
pergunta
oferta-direta
```

Valores de dor:

```text
fraude
lead-ruim
custo-alto
baixa-conversao
atrito
risco-juridico
tempo-perdido
operacao-manual
falta-contexto
baixa-previsibilidade
```

Valores de ângulo:

```text
risco-financeiro
perda-oportunidade
comparativo-mercado
antes-depois
autoridade-tecnica
prova-social
demonstracao
educacional
quebra-crenca
oferta-direta
```

Valores de etapa:

```text
tofu
mofu
bofu
rmkt
reativacao
upsell
```

Exemplo:

```text
utm_content=crv-hs-prevent-202605-014__fmt-video__hook-roi__per-cfo__slug-fraude-invisivel__dor-fraude__ang-risco-financeiro__stage-tofu__ver-v01
```

## 9. UTM term

Define público, temperatura, posicionamento, keyword ou recorte tático.

Formato para social:

```text
{adgroup_id}__pub-{publico}__temp-{temperatura}__pos-{posicionamento}__slug-{slug}__plc-{placement}__geo-{geo}
```

Exemplo social:

```text
utm_term=adg-hs-prevent-202605-003__pub-cfo-fintech__temp-frio__pos-interesses__slug-cfo-antifraude__plc-reels__geo-br
```

Formato para search:

```text
{adgroup_id}__kw-{keyword_slug}__match-{tipo_match}__temp-{temperatura}__slug-{slug}__geo-{geo}
```

Exemplo search:

```text
utm_term=adg-hs-prevent-202605-004__kw-api-antifraude__match-phrase__temp-quente__slug-busca-api-antifraude__geo-br
```

Valores de temperatura:

```text
frio
morno
quente
remarketing
lookalike
base
```

Valores de posicionamento/segmentação:

```text
interesses
lookalike
lista
retargeting
aberto
keyword
contextual
cargo
empresa
geo
```

## 10. Parâmetros customizados recomendados

Além das UTMs padrão, usar parâmetros próprios quando possível. Eles são mais fáceis de ler em planilha/CRM e evitam sobrecarregar UTMs.

### v4_client_id

```text
v4_client_id=cli-hs-prevent
```

### v4_campaign_id

```text
v4_campaign_id=cmp-hs-prevent-202605-001
```

### v4_adgroup_id

```text
v4_adgroup_id=adg-hs-prevent-202605-003
```

### v4_creative_id

```text
v4_creative_id=crv-hs-prevent-202605-014
```

### v4_test_id

```text
v4_test_id=tst-hs-prevent-202605-004
```

## 11. URL exemplo completa

```text
https://cliente.com/lp-onboarding-digital
?utm_source=meta
&utm_medium=paid_social
&utm_campaign=cmp-hs-prevent-202605-001__typ-aquisicao__obj-mql__mov-teste-oferta__slug-antifraude-cfo__coh-b2b-high-ticket__seg-antifraude__per-2026q2
&utm_content=crv-hs-prevent-202605-014__fmt-video__hook-roi__per-cfo__slug-fraude-invisivel__dor-fraude__ang-risco-financeiro__stage-tofu__ver-v01
&utm_term=adg-hs-prevent-202605-003__pub-cfo-fintech__temp-frio__pos-interesses__slug-cfo-antifraude__plc-reels__geo-br
&v4_client_id=cli-hs-prevent
&v4_campaign_id=cmp-hs-prevent-202605-001
&v4_adgroup_id=adg-hs-prevent-202605-003
&v4_creative_id=crv-hs-prevent-202605-014
&v4_test_id=tst-hs-prevent-202605-004
```

## 12. Nome de campanha na plataforma

Formato:

```text
{campaign_id} | {tipo_campanha} | {objetivo} | {movimento} | {slug}
```

Exemplo:

```text
cmp-hs-prevent-202605-001 | aquisicao | mql | teste-oferta | antifraude-cfo
```

## 13. Nome de conjunto/ad group

Formato:

```text
{adgroup_id} | {publico} | {temperatura} | {posicionamento} | {slug}
```

Exemplo:

```text
adg-hs-prevent-202605-003 | cfo-fintech | frio | interesses | cfo-antifraude
```

## 14. Nome de criativo

Formato:

```text
{creative_id} | {formato} | {hook} | {persona} | {slug} | {versao}
```

Exemplo:

```text
crv-hs-prevent-202605-014 | video | roi | cfo | fraude-invisivel | v01
```

## 15. Campos mínimos no CRM ou planilha de leads

Campos de identificação:

- `lead_id`
- `created_at`
- `client_id`
- `campaign_id`
- `adgroup_id`
- `creative_id`
- `test_id`

Campos UTM:

- `utm_source`
- `utm_medium`
- `utm_campaign`
- `utm_content`
- `utm_term`

Campos parseados:

- `objetivo`
- `tipo_campanha`
- `movimento`
- `campaign_slug`
- `cohort`
- `segmento`
- `periodo`
- `publico`
- `temperatura`
- `posicionamento`
- `adgroup_slug`
- `formato`
- `persona`
- `hook`
- `creative_slug`
- `dor`
- `angulo`
- `etapa_funil`
- `versao`
- `placement`
- `geo`

Campos comerciais:

- `lead_status`
- `mql_status`
- `sql_status`
- `opportunity_status`
- `deal_status`
- `disqualification_reason`
- `sales_owner`
- `first_contact_at`
- `speed_to_lead_minutes`
- `feedback_quality`

## 16. First-touch e last-touch

Para não perder histórico:

- First-touch deve ser write-once.
- Last-touch deve atualizar em nova conversão relevante.

Campos first-touch:

- `first_utm_source`
- `first_utm_medium`
- `first_utm_campaign`
- `first_utm_content`
- `first_utm_term`
- `first_conversion_at`

Campos last-touch:

- `last_utm_source`
- `last_utm_medium`
- `last_utm_campaign`
- `last_utm_content`
- `last_utm_term`
- `last_conversion_at`

## 17. Teste obrigatório antes do go-live

Checklist:

- Abrir URL com UTMs.
- Submeter formulário teste.
- Verificar se os campos chegaram na planilha/CRM.
- Verificar se IDs foram preservados.
- Verificar se first-touch não foi sobrescrito.
- Verificar se last-touch atualiza quando deve.
- Verificar se lead é deduplicado.
- Verificar se export consegue cruzar lead com campanha/criativo.

## 18. Critério N2

Tracking está N2 quando:

- toda campanha tem ID;
- todo criativo tem ID;
- toda URL tem UTM conforme;
- todo lead carrega origem;
- a fonte da verdade preserva os campos;
- existe teste ponta a ponta registrado.

## 19. Critério N3

Tracking está N3 quando:

- a operação usa os campos para decidir;
- performance é agrupada por atributos de criativo;
- a qualidade comercial retroalimenta o próximo ciclo;
- existem aprendizados por cohort/segmento;
- o padrão é revisado quando gera ruído ou falso aprendizado.
