# Referência Do Monitor De SLA De Leads

Fonte normativa: `assets/canonicos/07_CRM_HANDOFF_SLA_MARKETING_VENDAS_CANONICO.md`.

## Princípio

Lead bom pode virar resultado ruim se vendas demora, não entende contexto ou não executa cadência mínima. Monitorar SLA evita culpar marketing por quebra comercial.

## SLA Canônico

### Lead Quente

- primeiro contato em até 5 minutos;
- mínimo de 3 tentativas no primeiro dia;
- mínimo de 6 tentativas em 7 dias;
- canais: telefone, WhatsApp, email;
- se não responder, entra em cadência de nurture.

### Lead Morno

- primeiro contato em até 2 horas úteis;
- mínimo de 3 tentativas em 7 dias;
- se não responder, nurture.

### Lead Frio

- qualificação assíncrona;
- fluxo de conteúdo;
- retentativa após novo sinal de intenção.

## Roteamento

Definir e monitorar:

- quem recebe cada tipo de lead;
- regra por segmento;
- regra por região;
- regra por ticket;
- regra por disponibilidade do vendedor;
- regra para redistribuição;
- alerta para gestor se SLA estourar.

## Rotina De Feedback

Cadência sugerida:

- diária: SLA e leads sem atendimento;
- semanal: qualidade de leads e motivos de desqualificação;
- quinzenal: MQL/SQL por campanha/criativo;
- mensal: aprendizado para DEOC/DCC, plano de mídia e criativos.

## Alertas

### Crítico

- lead quente sem dono;
- lead quente sem primeiro contato;
- lead quente com SLA estourado;
- lead MQL sem responsável comercial.

### Alto

- lead morno sem contato após 2 horas úteis;
- tentativas insuficientes em lead quente;
- roteamento ausente;
- `next_step` vazio em lead conectado.

### Médio

- cadência insuficiente em 7 dias;
- `last_contact_at` antigo;
- `feedback_notes` ausente;
- lead sem próximo passo.

### Baixo

- dentro do SLA, monitorar.

## Ações Recomendadas

- atribuir dono;
- fazer primeiro contato;
- executar cadência mínima;
- preencher próximo passo;
- redistribuir lead;
- alertar gestor;
- devolver para nurture;
- corrigir regra de roteamento.

## O Que Evitar

- SLA verbal;
- lead sem dono;
- vendas rejeitar lead sem motivo;
- não deduplicar;
- marketing otimizar sem saber se o lead foi atendido.
