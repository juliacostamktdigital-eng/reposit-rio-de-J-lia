# Briefing Criativo Video-First Canônico
**Atualizado:** 2026-04-30  
**Fonte final:** consolidação em `assets/canonicos`; base canônica original + `assets/legacy/merge/skills/09-briefing-pack-producao-criativos-e-conversao.md`.  
**Decisão de merge:** skill 09 dividida: frente criativa incorporada aqui; ambiente de conversão incorporado no canônico 08; gaps operacionais referenciados no 06.


Status: v1 para workshop  
Escopo: produção de criativos para campanhas de demanda qualificada  
Objetivo: padronizar como briefar criativos, especialmente vídeos, para que cada peça carregue hipótese, contexto e atributos analisáveis.

## 1. Princípio

Criativo não é só entrega visual. Criativo é uma hipótese de aquisição empacotada em mídia.

Cada criativo deve responder:

- para quem estamos falando;
- qual dor/desejo estamos ativando;
- qual crença queremos mudar;
- qual promessa estamos fazendo;
- qual prova sustenta;
- qual ação esperamos;
- qual atributo será analisado depois.

## 2. Inputs obrigatórios

Antes de briefar:

- planejamento estratégico/UCM;
- DEOC;
- plano de mídia;
- benchmark de segmento;
- hipótese de teste;
- persona/ICP;
- etapa do funil;
- formato desejado;
- restrições de marca;
- claims permitidos/proibidos;
- aprendizados anteriores;
- taxonomia de UTM/creative ID.

O briefing deve conseguir apontar de qual problema, persona, alternativa percebida e prova do UCM aquele criativo nasceu.

## 3. Estrutura do briefing

### 3.1 Identificação

Campos:

- `brief_id`
- `test_id`
- `creative_id_previsto`
- cliente;
- campanha;
- conjunto/ad group;
- responsável;
- data;
- status.

### 3.2 Objetivo do criativo

Definir:

- objetivo do criativo;
- etapa do funil;
- métrica primária;
- métrica secundária;
- evento esperado;
- hipótese.

Exemplo:

```text
Objetivo: gerar MQLs CFO para diagnóstico de risco no onboarding digital.
Etapa: TOFU.
Métrica primária: custo por MQL.
Hipótese: CFOs respondem melhor a hooks de risco financeiro do que a hooks técnicos.
```

### 3.3 Público/persona

Definir:

- persona;
- cargo;
- nível de consciência;
- principal dor;
- principal desejo;
- objeção provável;
- linguagem que usa;
- prova que convence.

### 3.4 Mensagem

Definir:

- hook;
- dor/desejo;
- ângulo;
- promessa;
- mecanismo;
- prova;
- CTA;
- função no funil;
- hipótese de aprendizado;
- destino/ponto de conversão;
- objeção atacada.

### 3.5 Formato

Definir:

- formato;
- duração;
- proporção;
- canal;
- placement;
- estilo visual;
- necessidade de captação;
- necessidade de motion;
- necessidade de narração;
- necessidade de legenda.

Formatos possíveis:

```text
video-roteirizado
ugc
founder
demo
motion
screen-record
depoimento
prova-social
static
carousel
```

### 3.6 Roteiro

Estrutura recomendada:

```text
Hook inicial:
Contexto:
Tensão:
Mecanismo:
Prova:
CTA:
```

Para vídeos curtos:

```text
0-3s: hook
3-10s: dor/tensão
10-20s: mecanismo/prova
20-30s: CTA
```

### 3.6.1 Criativos slide a slide / carrossel

Quando o criativo for carrossel, social post sequencial ou peça educacional, documentar slide a slide:

```text
Slide:
Função narrativa:
Texto principal:
Prova ou exemplo:
Visual sugerido:
CTA ou transição:
Atributo de análise:
```

Funções narrativas possíveis:

- interrupção;
- identificação da dor;
- amplificação do impacto;
- exemplo concreto;
- quebra de crença;
- mecanismo;
- prova;
- convite/CTA.

Exemplo de progressão observada nos materiais estratégicos:

```text
Slide 1: nomear a ameaça ou oportunidade.
Slide 2: mostrar que o público tem recursos, mas falta visão/processo.
Slide 3: trazer caso ou analogia.
Slide 4: aprofundar consequência.
Slide 5: formular a nova crença.
Slide 6: apresentar mecanismo/solução.
Slide 7: CTA.
```

### 3.7 Direção visual

Definir:

- referência visual;
- elementos obrigatórios;
- elementos proibidos;
- cenário;
- pessoa/ator;
- objetos;
- textos em tela;
- ritmo;
- trilha;
- tom emocional;
- assets de marca.

Quando o insumo vier de apresentação estratégica, registrar também:

- slide de origem;
- imagem/render/prova que deve ser reaproveitada;
- elementos de KV/brandbook;
- restrições de uso;
- necessidade de redesenhar imagem para mídia;
- relação com a promessa da seção ou criativo.

### 3.8 Nomenclatura e tracking

Cada criativo precisa nascer com:

- `creative_id`;
- formato;
- persona;
- hook;
- dor/desejo;
- ângulo;
- etapa;
- versão;
- `utm_content` previsto.

Exemplo:

```text
creative_id: crv-hs-prevent-202605-014
formato: video
persona: cfo
hook: roi
dor: fraude
angulo: risco-financeiro
stage: tofu
versao: v01
utm_content: crv-hs-prevent-202605-014__fmt-video__icp-cfo__hook-roi__mot-seguranca__dor-fraude__ang-risco-financeiro__stage-tofu__ver-v01
```

### 3.10 Pack de Produção e critérios de hipótese

Cada criativo do pack precisa nascer de uma hipótese do Plano de Mídia e de um tipo do Banco de Criativos. O briefing deve declarar função no funil, público/persona, hook, dor/desejo, prova, CTA, destino, métrica de leitura e variação real.

Pendências de prova, asset, edição, aprovação, LP ou tracking não ficam escondidas no briefing: entram no backlog transversal `06_ASSETS_ESQUECIDOS_E_BACKLOG_CANONICO.md` com dono e decisão de go/no-go.

## 4. Template de briefing

```text
# Brief Criativo

Cliente:
Campanha:
Test ID:
Creative ID:
Responsável:
Data:

## Hipótese

## Persona

## Dor/desejo

## Hook

## Promessa

## Prova

## Objeção atacada

## CTA

## Formato

## Roteiro

## Direção visual

## Textos em tela

## Legenda/copy do anúncio

## UTM content previsto

## Critério de aprovação

## Métrica de leitura
```

## 5. Critério de aprovação interna

Um criativo só deve ser aprovado se:

- tem objetivo claro;
- tem hipótese;
- tem persona definida;
- tem hook claro;
- tem conexão com DCC;
- tem CTA;
- respeita claims permitidos;
- tem ID;
- tem atributos para análise;
- está coerente com LP/oferta;
- tem critério de leitura.

Para carrossel ou social sequencial, também validar:

- cada slide tem uma função narrativa clara;
- a sequência progride sem repetir a mesma ideia;
- o último slide tem CTA explícito;
- a peça pode ser analisada por hook, problema, prova e persona;
- o conteúdo não depende de informação que só existe na apresentação original.

## 6. Como a IA deve usar o briefing

A IA pode:

- gerar variações de roteiro;
- sugerir hooks alternativos;
- adaptar roteiro por persona;
- transformar DCC em criativos;
- revisar se o criativo respeita claims;
- gerar legendas;
- gerar direção visual;
- transformar aprendizados em novos briefs.

Mas a IA não deve:

- criar promessa fora do DCC;
- inventar prova;
- remover tracking;
- alterar persona sem registrar;
- criar variações sem ID.

## 7. Critério N2

Briefing criativo está N2 quando:

- cada criativo tem briefing;
- briefing tem hipótese;
- briefing está conectado ao DCC;
- briefing tem ID e parâmetros;
- aprovação está registrada;
- peça final está linkada ao briefing.

## 8. Critério N3

Briefing criativo está N3 quando:

- performance retroalimenta novos briefs;
- atributos vencedores são reaproveitados;
- atributos ruins viram anti-padrões;
- o time consegue comparar levas criativas.
