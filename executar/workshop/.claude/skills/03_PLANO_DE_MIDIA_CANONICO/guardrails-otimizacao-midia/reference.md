# Referência De Guardrails De Otimização De Mídia

Fonte normativa: `assets/canonicos/03_PLANO_DE_MIDIA_CANONICO.md`.

## Princípio

Guardrails não são regras cegas. Eles impedem decisões superficiais e forçam leitura integrada entre mídia, LP, funil, CRM, qualidade comercial e tracking.

## Regras Canônicas

### CPL Alto + CPMQL Saudável

Não matar automaticamente. Investigue:

- qualidade do MQL;
- avanço para SQL;
- ticket/valor esperado;
- margem;
- saturação de público;
- hipótese criativa.

Ação provável: manter ou ajustar criativo/público com nova leitura.

### CPL Baixo + MQL Baixo

Lead barato sem qualidade não é vitória.

Investigue:

- público amplo demais;
- promessa desalinhada;
- formulário frouxo;
- oferta gerando curiosidade sem intenção;
- canal com baixa aderência ao ICP.

Ação provável: revisar público, promessa ou formulário.

### Lead Bom + SQL Baixo

O problema pode estar no processo comercial.

Investigue:

- SLA;
- abordagem;
- handoff;
- enriquecimento;
- definição de SQL;
- priorização de leads.

Ação provável: revisar SLA/handoff antes de cortar mídia.

### Gasto + Zero Evento

Não otimizar criativo antes de validar tracking.

Investigue:

- pixel/evento;
- UTMs;
- LP;
- formulário;
- redirecionamento;
- consentimento/cookies;
- CRM/planilha backup.

Ação provável: bloquear decisão de mídia e fazer QA.

### CTR Alto + Conversão Baixa

Criativo atrai, mas a promessa quebra depois do clique.

Investigue:

- LP;
- oferta;
- carregamento mobile;
- coerência anúncio -> página;
- fricção de formulário;
- expectativa criada.

Ação provável: revisar LP/oferta.

### CTR Baixo + MQL Bom

Criativo não escala bem, mas o tráfego que entra é qualificado.

Ação provável: testar variação de hook/formato antes de matar.

### LP Views Muito Abaixo Dos Cliques

Investigue:

- velocidade de página;
- tracking;
- pixel;
- experiência mobile;
- redirecionamentos;
- queda por origem/canal.

### Checkout/Form Start Existe, Mas Lead/Compra Cai

Investigue:

- formulário;
- oferta;
- fricção;
- preço;
- expectativa criada;
- etapa de confirmação.

### Canal De Branding Sem Lead Direto

Avalie contribuição indireta antes de cortar:

- remarketing;
- busca de marca;
- tráfego direto;
- influência em conversões assistidas;
- aquecimento de audiência.

### Divergência Previsto Vs Realizado

Se o realizado diverge do previsto por lote/semana, recalcular projeção antes de prometer resultado acumulado.

## Changelog Obrigatório

Toda mudança relevante deve registrar:

- data;
- dono;
- item alterado;
- estado anterior;
- novo estado;
- motivo;
- métrica observada;
- hipótese;
- próxima leitura esperada;
- data da próxima leitura.

Mudanças relevantes:

- mix de canais;
- budget;
- hipótese;
- público;
- criativo;
- LP/destino;
- oferta;
- evento de otimização;
- regra de qualificação;
- SLA/handoff.

## Severidade

### Crítica

Pode invalidar a leitura ou queimar budget:

- tracking quebrado;
- gasto sem evento;
- origem perdida no CRM;
- promessa comercial impossível;
- meta baseada só no cenário otimista.

### Alta

Afeta decisão de investimento:

- CAC inviável;
- qualidade comercial ruim;
- SQL muito abaixo do esperado;
- LP com queda forte;
- canal sem aderência ao ICP.

### Média

Exige teste ou ajuste:

- CTR baixo com boa qualidade;
- criativo cansando;
- CPL moderadamente acima;
- hipótese inconclusiva.

### Baixa

Monitoramento:

- variação dentro da faixa;
- volume ainda baixo;
- primeira leitura sem maturidade.

## Decisões Permitidas

- manter;
- escalar;
- ajustar;
- pausar;
- investigar tracking;
- revisar LP/oferta;
- revisar público;
- revisar criativo;
- revisar SLA/handoff;
- recalcular plano.

Evite "otimizar" sem dizer exatamente qual alavanca muda.
