---
name: backlog-operacional-growth
description: Transforma gaps operacionais de growth em backlog acionável com dono, prazo, severidade, impacto, dependências, esforço e decisão go/no-go. Use após inventário de gaps, QA criativo/LP/tracking, auditoria CRM, preparação de go-live ou quando a operação precisa priorizar correções antes de rodar campanha.
---

# Backlog Operacional Growth

## Quando Usar

Use quando já existem gaps identificados e é preciso decidir o que resolver, aceitar, substituir ou bloquear antes de avançar.

Situações típicas:

- gaps de produção criativa;
- LP sem QA;
- formulário sem CRM;
- tracking sem teste;
- campanha sem UTM/ID;
- ausência de acesso;
- aprovação pendente;
- restrição jurídica sobre claim;
- divergência entre oferta, anúncio, destino e vendas;
- go-live com risco.

## Inputs Necessários

- inventário de gaps;
- QA criativo;
- QA LP;
- QA tracking;
- CRM/SLA;
- acessos;
- aprovações;
- restrições;
- evidências;
- datas de go-live;
- donos operacionais.

## Workflow

1. Reúna gaps em uma lista única.
2. Para cada gap, preencha:
   - descrição;
   - categoria;
   - componente afetado;
   - impacto;
   - severidade;
   - urgência;
   - esforço;
   - dono;
   - prazo;
   - dependência;
   - evidência;
   - decisão.
3. Classifique decisão:
   - resolver antes do go-live;
   - aceitar risco por ciclo;
   - substituir hipótese;
   - retirar do pacote v1;
   - bloquear go-live.
4. Priorize:
   - críticos de tracking/CRM/LP/prova primeiro;
   - bloqueadores de leitura antes de otimização;
   - claims/compliance antes de mídia;
   - dependências que destravam múltiplas frentes.
5. Gere plano de resolução:
   - sequência;
   - dono;
   - prazo;
   - status;
   - evidência de conclusão.
6. Registre decisão e changelog quando a resolução mudar escopo, campanha, hipótese, tracking ou oferta.

## Output Esperado

- backlog priorizado;
- decisões go/no-go por gap;
- dependências;
- plano de resolução;
- riscos aceitos;
- itens removidos do pacote v1;
- changelog de decisões.

Use `templates/backlog-gaps.md` para entrega manual.
Use `templates/backlog-gaps.json` com o script para gerar CSV/Markdown.

## Script Utilitário

```bash
python3 scripts/prioritize_operational_backlog.py templates/backlog-gaps.json --md /tmp/backlog-growth.md --csv /tmp/backlog-growth.csv
```

O script calcula prioridade a partir de severidade, urgência, decisão go/no-go e esforço.

## Definition Of Done

- Todo gap tem dono.
- Todo gap tem decisão.
- Bloqueadores estão separados de melhorias.
- Dependências estão explícitas.
- Prazos estão definidos.
- Riscos aceitos foram registrados.
- Itens críticos têm evidência exigida para conclusão.

## Cuidados

- Não tratar bloqueio como tarefa normal.
- Não aceitar risco de tracking sem decisão explícita.
- Não colocar "time" como dono.
- Não avançar go-live com gap crítico sem registro.
- Não misturar backlog operacional com wishlist estratégica.
