---
name: setup-crm-handoff-marketing-vendas
description: Define setup operacional de CRM, handoff e SLA entre marketing e vendas, incluindo campos mínimos, status, motivos de desqualificação, roteamento, SLA, contexto do lead e feedback comercial. Use em leadgen, onboarding CRM, preparação go-live, auditoria N2 ou quando leads precisam carregar origem, promessa e contexto até vendas.
---

# Setup CRM Handoff Marketing Vendas

## Quando Usar

Use para garantir que a demanda gerada por marketing seja recebida, qualificada, trabalhada e devolvida com feedback.

Situações típicas:

- CRM ainda não preserva UTMs/IDs;
- lead chega sem dono;
- SLA é verbal;
- vendas rejeita lead sem motivo;
- marketing otimiza sem feedback comercial;
- campanha vai ao ar sem campos first/last-touch;
- é necessário preparar N2 de CRM/handoff.

## Inputs Necessários

- CRM atual;
- funil comercial;
- critérios de Lead, MQL, SQL, oportunidade e venda;
- taxonomia UTM e IDs;
- SLA desejado;
- time comercial;
- regras de roteamento;
- motivos de desqualificação;
- campos de feedback;
- ponto de conversão/LP/formulário.

## Workflow

1. Defina estágios e critérios:
   - Lead;
   - MQL;
   - SQL;
   - oportunidade;
   - venda/perda.
2. Configure campos mínimos:
   - identificação;
   - origem first-touch;
   - origem last-touch;
   - IDs de campanha/adgroup/criativo/teste;
   - funil;
   - atendimento;
   - qualidade;
   - comercial.
3. Padronize status:
   - `lead_status`;
   - `mql_status`;
   - `sql_status`;
   - `opportunity_status`;
   - `deal_status`.
4. Defina motivos fechados de desqualificação.
5. Defina SLA por tipo de lead:
   - quente;
   - morno;
   - frio.
6. Defina roteamento:
   - por segmento;
   - região;
   - ticket;
   - disponibilidade;
   - redistribuição;
   - alerta de SLA.
7. Defina contexto que marketing envia para vendas:
   - campanha;
   - criativo;
   - promessa;
   - CTA;
   - persona presumida;
   - dor/ângulo;
   - etapa do funil;
   - página de conversão;
   - sugestão de abordagem.
8. Defina feedback obrigatório de vendas para marketing.
9. Crie checklist N2 e teste ponta a ponta.

## Output Esperado

- mapa de campos CRM;
- status padronizados;
- motivos de desqualificação;
- regras de SLA;
- regras de roteamento;
- contexto para vendas;
- campos de feedback;
- checklist N2;
- gaps de setup.

Use `templates/mapa-crm.md` para documentação manual.
Use `templates/mapa-crm.json` com o script para auditar campos e status.

## Script Utilitário

```bash
python3 scripts/audit_crm_handoff.py templates/mapa-crm.json --md /tmp/crm-handoff.md --csv /tmp/crm-handoff.csv
```

O script compara campos/status existentes com o mínimo canônico e gera gaps.

## Definition Of Done

- Campos mínimos existem.
- Lead preserva origem first-touch e last-touch.
- MQL/SQL estão definidos.
- SLA está definido por tipo de lead.
- Responsável comercial está definido.
- Motivo de desqualificação é obrigatório e fechado.
- Feedback volta para marketing.
- Existe evidência de teste ponta a ponta.

## Cuidados

- Não sobrescrever first-touch com last-touch.
- Não aceitar motivo de perda aberto demais.
- Não considerar lead como resultado final.
- Não deixar lead sem dono.
- Não usar SLA verbal como critério N2.
