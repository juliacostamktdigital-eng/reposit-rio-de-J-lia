---
name: monitor-sla-leads
description: Monitora SLA de atendimento de leads, detectando leads sem dono, sem primeiro contato, SLA estourado, baixa cadência, falhas de roteamento e risco de perda comercial. Use em rotina diária de CRM, pós-go-live, auditoria de vendas, análise de speed-to-lead ou quando leads bons não viram SQL.
---

# Monitor SLA Leads

## Quando Usar

Use para verificar se leads estão sendo atendidos dentro do SLA e se o processo comercial está preservando a demanda gerada por marketing.

Situações típicas:

- rotina diária de CRM;
- campanha recém-lançada;
- lead quente sem contato;
- MQL bom não vira SQL;
- vendedor sem dono atribuído;
- speed-to-lead alto;
- falha de roteamento;
- queda de resposta por atendimento tardio.

## Inputs Necessários

- export CRM;
- `lead_id`;
- `created_at`;
- `lead_temperature`;
- `sales_owner`;
- `assigned_at`;
- `first_contact_at`;
- `contact_attempts`;
- `last_contact_at`;
- `lead_status`;
- `next_step`;
- regras de SLA.

## Regras Canônicas

### Lead Quente

- primeiro contato em até 5 minutos;
- mínimo de 3 tentativas no primeiro dia;
- mínimo de 6 tentativas em 7 dias;
- canais: telefone, WhatsApp, email;
- se não responder, nurture.

### Lead Morno

- primeiro contato em até 2 horas úteis;
- mínimo de 3 tentativas em 7 dias;
- se não responder, nurture.

### Lead Frio

- qualificação assíncrona;
- fluxo de conteúdo;
- retentativa após novo sinal de intenção.

## Workflow

1. Carregue leads do CRM.
2. Verifique dono:
   - sem `sales_owner`;
   - atribuição atrasada;
   - roteamento ausente.
3. Verifique primeiro contato:
   - ausente;
   - fora do SLA por temperatura;
   - `speed_to_lead_minutes` alto.
4. Verifique cadência:
   - tentativas insuficientes no primeiro dia;
   - tentativas insuficientes em 7 dias;
   - `next_step` vazio;
   - `last_contact_at` muito antigo.
5. Classifique risco:
   - crítico: lead quente sem contato/dono;
   - alto: SLA estourado;
   - médio: cadência insuficiente;
   - baixo: monitorar.
6. Gere lista de ação por responsável.

## Output Esperado

- alertas de SLA;
- lista de leads em risco;
- responsável por correção;
- motivo do alerta;
- ação recomendada;
- resumo por vendedor;
- evidência para rotina diária.

Use `templates/checklist-sla.md` para rotina manual.
Use `templates/leads-sla.csv` com o script para gerar alertas.

## Script Utilitário

```bash
python3 scripts/monitor_sla_leads.py templates/leads-sla.csv --now "2026-05-03T12:00:00" --md /tmp/sla.md --csv /tmp/sla-alertas.csv
```

O script calcula alertas com base nos timestamps e regras de SLA.

## Definition Of Done

- Leads sem dono foram detectados.
- Leads sem primeiro contato foram detectados.
- SLA estourado foi marcado por temperatura.
- Tentativas mínimas foram verificadas.
- Próxima ação e responsável foram definidos.
- Alertas podem alimentar rotina diária de CRM.
