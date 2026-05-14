---
skill: chatwoot-audit
owner: gestor-de-projeto
latest: v1.0.0
status: active
segment:
  - b2b
  - b2c
  - b2b2c
tier:
  - starter
  - growth
  - scale
  - enterprise
software:
  - api
specialization:
  - inside-sales
  - infoproduto
  - local-business
  - ecom
  - saas
created: 2026-04-14
updated: 2026-04-14
---

## Propósito

Audita conversas de leads humanos no Chatwoot por período de datas. Conecta via API REST, analisa timing de resposta, follow-ups, personalização e taxa de conversão (agendamentos). Entrega relatório visual em HTML ou Markdown.

## Quando usar

- Diagnóstico periódico de performance comercial do time de SDRs
- Identificação de GAPs de atendimento (leads ignorados ou não abordados)
- Comparativo entre agentes em taxa de conversão
- Análise de padrões textuais que separam leads convertidos dos não convertidos

## Quando NÃO usar

- Conversas de suporte (não comerciais)
- Instâncias sem label `conectado` configurada (a conversão não será detectada corretamente)

## Inputs esperados

- `base_url` — URL da instância Chatwoot (ex: `https://chatwoot.suaempresa.com`)
- `api_access_token` — token de acesso (Chatwoot → Perfil → "Access Token")
- `account_id` — ID da conta (visível na URL `/app/accounts/N/`)
- `data_inicio` / `data_fim` — período de análise (padrão: últimos 7 dias)
- `formato` — `html` (abre no browser, exporta como PDF) ou `markdown` (Notion, Obsidian)

## Output esperado

Arquivo de relatório salvo em `~/chatwoot-audit-AAAA-MM-DD.{html,md}` com:
- KPI cards: % sem resposta, % convertidos, % follow-up, timing mediano
- Funil de conversão: leads → respondidos → convertidos
- Performance por agente e evolução por dia
- Análise de GAPs (lead ativo ignorado vs lead não abordado)
- Comparativo convertidos vs não convertidos
- DNA da conversa que converte (exemplos reais)
- Conversão por faixa horária
- Recomendações com tags de urgência (URGENTE / OPORTUNIDADE / TREINAMENTO)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-14 | latest | Versão inicial — auditoria completa via API REST |
