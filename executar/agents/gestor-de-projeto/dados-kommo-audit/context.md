---
skill: dados-kommo-audit
owner: gestor-de-projeto
latest: v1.0.0
status: active
segment:
  - b2b
  - b2c
  - b2b2c
tier:
  - growth
  - scale
  - enterprise
software:
  - api
specialization:
  - inside-sales
  - local-business
created: 2026-04-21
updated: 2026-04-21
---

## Propósito

Auditoria de atendimento comercial no Kommo CRM por período flexível. Analisa pipeline (volume, conversão, ticket), timing (primeira resposta, tempo até conexão, gaps), origem/canal dos leads e qualidade do atendimento via conversas REAIS de WhatsApp (mensagens + imagens + PDFs). Gera relatório HTML com diagnóstico qualitativo, DNA comparativo de ganhos vs perdidos e recomendações priorizadas com evidências literais das conversas.

O diferencial é a **camada qualitativa**: em vez de parar nos números do funil, a skill lê o conteúdo real das conversas (via cookies de sessão do painel Kommo) e identifica padrões sistêmicos de atendimento — apresentação, qualificação, gaps, follow-ups, reação a mídias. É o 80/20 do valor da auditoria.

## Quando usar

- Check-in mensal com cliente que usa Kommo e tem operação comercial ativa
- Retrospectiva de ciclo 90D para decisão de continuidade
- Diagnóstico pontual quando cliente reporta "leads não convertem" / "time não responde"
- Validação de qualidade do atendimento após treinamento do comercial do cliente
- Antes de escalar investimento em tráfego — garantir que o funil comporta o volume

## Quando NÃO usar

- Cliente não usa Kommo (ver `dados-activecampaign-audit` ou `dados-chatwoot-audit`)
- Período com volume muito baixo (< 20 leads) — amostra insuficiente pra diagnóstico
- Quando o objetivo é só reportar KPI de funil — use dashboard simples em vez de auditoria completa

## Inputs esperados

- `subdomain` — ex: `clientexyz.kommo.com`
- `bearer_token` — token de longa duração da conta (Kommo → Configurações → Integrações → app → "Chaves e escopos")
- `periodo` — linguagem natural aceita (ex: "ontem", "últimos 7 dias", "mês passado", "14/04 a 20/04")
- `curl_painel` (opcional, mas recomendado) — cURL do endpoint `events_timeline` copiado do DevTools do Chrome logado no painel Kommo. Desbloqueia a leitura de conversas reais. Sem ele, o relatório entrega só 3 das 4 camadas.
- `formato_saida` — HTML (default) ou Markdown

## Output esperado

Relatório salvo em `~/kommo-audit-{AAAA-MM-DD}.{html|md}` com 13 seções obrigatórias:

1. Header (subdomain, período, total de leads, data)
2. Callout principal (maior problema detectado)
3. KPI cards (% ganhos, % sem resposta, mediana timing, ticket médio)
4. Funil
5. Distribuição por estágio
6. Análise por origem/canal
7. Volume por dia
8. Volume por hora
9. Por SDR
10. Padrões sistêmicos (se cookie disponível)
11. Análise de conversas com trechos literais (se cookie disponível)
12. DNA da conversa que converte (comparativo ganhos × perdidos)
13. Recomendações priorizadas com evidências

Footer sempre cita endpoints e tamanho de amostra — transparência de método obrigatória.

## Agentes que usam esta skill

- `owner`: gestor-de-projeto
- `consumers`: coordenador (para pautar check-in), gerente (para decisão estratégica)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-21 | latest | Versão inicial — 4 camadas de análise, HTML/MD, suporte a cookies do painel |
