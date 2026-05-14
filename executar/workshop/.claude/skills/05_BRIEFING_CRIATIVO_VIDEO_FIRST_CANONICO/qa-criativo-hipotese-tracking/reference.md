# Referência Do QA Criativo Hipótese Tracking

Fonte normativa: `assets/canonicos/05_BRIEFING_CRIATIVO_VIDEO_FIRST_CANONICO.md`.

## Princípio

QA criativo garante que a peça final não perdeu a hipótese de aquisição. Criativo aprovado precisa continuar conectado a persona, mensagem, LP, tracking e leitura de performance.

## Critério De Aprovação Interna

Um criativo só deve ser aprovado se:

- tem objetivo claro;
- tem hipótese;
- tem persona definida;
- tem hook claro;
- tem conexão com DCC/DEOC;
- tem CTA;
- respeita claims permitidos;
- tem ID;
- tem atributos para análise;
- está coerente com LP/oferta;
- tem critério de leitura.

## Tracking Obrigatório

Cada criativo precisa nascer e sair aprovado com:

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
utm_content: crv-hs-prevent-202605-014__fmt-video__icp-cfo__hook-roi__mot-seguranca__dor-fraude__ang-risco-financeiro__stage-tofu__ver-v01
```

## QA Para Vídeo

Validar:

- hook nos primeiros 3 segundos;
- dor/tensão até 10 segundos;
- mecanismo/prova antes do CTA;
- CTA explícito;
- texto em tela legível;
- narração/legenda coerente;
- ritmo compatível com canal;
- claim sustentado por prova.

## QA Para Carrossel

Validar:

- cada slide tem função narrativa clara;
- sequência progride sem repetir a mesma ideia;
- último slide tem CTA explícito;
- peça pode ser analisada por hook, problema, prova e persona;
- conteúdo não depende de informação que só existe na apresentação original.

Funções esperadas:

- interrupção;
- identificação da dor;
- amplificação do impacto;
- exemplo concreto;
- quebra de crença;
- mecanismo;
- prova;
- convite/CTA.

## Bloqueios

Bloqueie go-live quando:

- não há `creative_id`;
- não há `utm_content`;
- hipótese está ausente;
- claim proibido aparece;
- promessa não tem prova;
- LP não sustenta a promessa;
- CTA leva para destino errado;
- peça não identifica persona/etapa;
- tracking não permite análise posterior.

## Pendências Para Backlog 06

Pendências de prova, asset, edição, aprovação, LP ou tracking não ficam escondidas. Cada item deve ter:

- pendência;
- categoria;
- severidade;
- dono;
- decisão;
- prazo;
- impacto se não resolver.

Categorias:

- prova;
- asset;
- edição;
- aprovação;
- LP;
- tracking;
- claim;
- roteiro;
- mídia.

## Decisões Permitidas

- `go`: sem bloqueios e pendências leves controladas;
- `go_com_pendencia`: pode subir, mas precisa registrar correção;
- `no_go`: precisa corrigir antes;
- `bloquear_tracking`: tracking impede leitura;
- `bloquear_claim`: risco jurídico/compliance;
- `bloquear_prova`: promessa sem sustentação.
