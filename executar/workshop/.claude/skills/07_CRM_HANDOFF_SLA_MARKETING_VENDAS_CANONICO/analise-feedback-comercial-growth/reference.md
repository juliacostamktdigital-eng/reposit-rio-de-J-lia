# Referência Da Análise De Feedback Comercial

Fonte normativa: `assets/canonicos/07_CRM_HANDOFF_SLA_MARKETING_VENDAS_CANONICO.md`.

## Princípio

Marketing não termina no lead. Feedback comercial é o mecanismo que separa:

- lead ruim;
- lead bom não atendido;
- lead bom para oferta errada;
- lead certo com promessa desalinhada;
- problema de SLA;
- problema de CRM/tracking;
- problema de processo comercial.

## Campos Obrigatórios De Feedback

Vendas deve devolver:

- lead era válido?
- era ICP?
- tinha dor real?
- tinha timing?
- tinha orçamento?
- entendeu a oferta?
- objeção principal;
- motivo de perda/desqualificação;
- qualidade percebida;
- comentário livre.

## Rotina De Feedback

- diária: SLA e leads sem atendimento;
- semanal: qualidade de leads e motivos de desqualificação;
- quinzenal: MQL/SQL por campanha/criativo;
- mensal: aprendizado para DEOC/DCC, plano de mídia e criativos.

## Campos Que Voltam Para A Planilha De Testes

- `lead_id`;
- `campaign_id`;
- `creative_id`;
- `test_id`;
- `is_mql`;
- `is_sql`;
- `is_opportunity`;
- `is_won`;
- `disqualification_reason`;
- `lead_quality`;
- `speed_to_lead_minutes`;
- `feedback_notes`.

## Diagnósticos Possíveis

### Lead Ruim

Sinais:

- baixa taxa MQL;
- baixa qualidade percebida;
- motivos como `sem-fit`, `cargo-inadequado`, `empresa-inadequada`, `curioso`;
- feedback indica desalinhamento de ICP.

Ação: revisar público, criativo, promessa, formulário e critérios de qualificação.

### Promessa Desalinhada

Sinais:

- lead entende algo diferente da oferta;
- objeção recorrente sobre expectativa;
- alta conversão inicial com rejeição comercial.

Ação: revisar copy, LP, CTA e handoff para vendas.

### Oferta Errada

Sinais:

- lead tem dor, mas oferta não resolve;
- recorrência de "busca outra solução";
- alto interesse sem avanço para SQL.

Ação: rebrief de oferta ou segmentação.

### SLA/Comercial

Sinais:

- speed-to-lead alto;
- MQL bom não vira SQL;
- muitos `nao-responde` após atendimento tardio;
- feedback ausente.

Ação: revisar SLA, roteamento, cadência e script.

### Tracking/Dados

Sinais:

- origem ausente;
- campanha/criativo sem ID;
- feedback sem `lead_id`;
- first/last-touch inconsistente.

Ação: QA tracking/CRM antes de decisão de mídia.

### Hipótese Inconclusiva

Sinais:

- volume baixo;
- feedback insuficiente;
- dados contraditórios;
- SLA não confiável.

Ação: aguardar volume, melhorar captura de feedback ou repetir teste controlado.

## Critério N3

CRM/handoff está N3 quando:

- qualidade comercial entra no debrief;
- campanhas são avaliadas por MQL/SQL/venda;
- SLA é monitorado;
- motivos de perda alimentam copy e oferta;
- aprendizados comerciais viram novos testes;
- marketing e vendas revisam juntos o funil.
