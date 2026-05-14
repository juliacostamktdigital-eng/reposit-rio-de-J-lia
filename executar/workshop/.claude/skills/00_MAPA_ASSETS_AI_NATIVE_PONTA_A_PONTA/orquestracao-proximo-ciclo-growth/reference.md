# Referência Da Orquestração Do Próximo Ciclo

Fonte normativa: `assets/canonicos/00_MAPA_ASSETS_AI_NATIVE_PONTA_A_PONTA.md`.

## Papel Da Skill

Esta skill opera a transição entre:

```text
execução -> leitura -> decisão -> backlog -> rebrief -> novo ciclo
```

Ela é uma camada de coordenação. Não substitui as skills especialistas de mídia, tracking, CRM, LP, copy ou criativo.

## O Que Conta Como Aprendizado

Um aprendizado precisa ter:

- hipótese original;
- evidência observada;
- métrica ou fato que sustenta;
- limite da conclusão;
- decisão associada;
- impacto no próximo ciclo.

Exemplo bom:

```text
Hooks de risco financeiro para CFO geraram CPMQL 32% menor que hooks técnicos em Meta, com volume mínimo de 42 MQLs e feedback comercial "bom/ótimo" em 67% dos casos. Limite: válido para campanha TOFU em fintech B2B high-ticket, ainda não testado em Search.
```

Exemplo ruim:

```text
Criativo de ROI funcionou.
```

## Taxonomia De Decisões

Use uma das decisões abaixo para cada hipótese/teste:

- `escalar`: resultado bom, tracking confiável e qualidade compatível;
- `manter`: resultado aceitável, precisa de mais volume;
- `ajustar`: há sinal, mas precisa mudar variável controlada;
- `matar`: hipótese perdeu com evidência suficiente;
- `replicar`: padrão pode ser testado em outro canal/persona;
- `criar-novo-teste`: aprendizado abriu nova pergunta;
- `corrigir-tracking`: leitura não é confiável;
- `revisar-oferta`: problema parece ser promessa, prova, preço, escopo ou fit;
- `acionar-vendas`: gargalo está em SLA, abordagem, qualificação ou feedback;
- `inconclusivo`: sem volume, sem tempo, sem dado ou execução inválida.

## Camadas De Leitura

### 1. Mídia

Verifique:

- spend vs previsto;
- distribuição por canal/campanha/conjunto/criativo;
- CPM, CTR, CPC, LP views, CPL;
- frequência e fadiga;
- consistência com plano de mídia;
- mudanças feitas durante o ciclo.

Não conclua por mídia isolada quando o objetivo é demanda qualificada.

### 2. Conversão E LP

Verifique:

- connect rate;
- taxa LP -> formulário/lead;
- CTA e promessa;
- qualidade mobile;
- eventos configurados;
- origem preservada;
- fricção de formulário.

Se há clique e pouca conversão, a hipótese pode estar na LP/oferta, não no criativo.

### 3. Tracking E Dados

Verifique:

- UTMs e IDs preservados;
- first-touch/last-touch;
- planilha backup;
- match CRM;
- taxa de origem desconhecida;
- creative_id fill rate;
- lead teste e evidências.

Se tracking está ruim, classifique conclusões como provisórias ou inválidas.

### 4. Comercial E Funil

Verifique:

- MQL, SQL, oportunidades e vendas;
- motivos de desqualificação;
- feedback_quality;
- speed-to-lead;
- taxa MQL -> SQL;
- objeções reais;
- divergência entre promessa e abordagem comercial.

Lead barato com baixa qualidade pode ser pior que lead caro com bom avanço.

## Priorização Do Próximo Ciclo

Priorize hipóteses que combinam:

- impacto esperado alto;
- evidência do ciclo anterior;
- esforço viável;
- risco controlado;
- dependência baixa;
- aprendizado reutilizável por cohort/segmento.

Evite backlog inflado. Um próximo ciclo bom deve ter poucas apostas claras.

## Canonização

Canonize quando:

- o padrão apareceu com evidência suficiente;
- o contexto está claro;
- o limite da conclusão foi documentado;
- o padrão pode orientar outro cliente, cohort ou segmento;
- há exemplo prático;
- há anti-padrão correspondente quando útil.

Não canonize quando:

- o dado é pequeno demais;
- tracking estava quebrado;
- a execução mudou muitas variáveis ao mesmo tempo;
- o padrão depende de uma particularidade não replicável.

## Changelog Obrigatório

Registre mudanças em:

- DEOC/narrativa/oferta;
- plano de mídia;
- orçamento e mix de canais;
- briefing criativo;
- LP/formulário;
- tracking/UTMs;
- CRM/SLA;
- taxonomia;
- backlog e prioridades.

Cada mudança deve conter:

- data;
- componente;
- mudança;
- motivo;
- evidência;
- impacto esperado;
- próxima leitura.

## Critério N3

O próximo ciclo só sustenta N3 quando:

- resultado foi lido em cadência;
- decisão está registrada;
- hipótese virou backlog;
- aprendizado alterou asset ou decisão;
- mudança entrou em changelog;
- padrão relevante foi canonizado ou descartado com motivo.
