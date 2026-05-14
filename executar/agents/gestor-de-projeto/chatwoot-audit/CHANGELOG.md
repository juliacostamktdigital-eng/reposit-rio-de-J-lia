# CHANGELOG — chatwoot-audit

## [v1.0.0] — 2026-04-14

### Inicial
- Versão de lançamento
- Auditoria completa via API REST do Chatwoot com autenticação por header
- Paginação inteligente por período (para em 2 páginas consecutivas fora do intervalo)
- Coleta paralela de mensagens com ThreadPoolExecutor (10 workers)
- Métricas: timing, follow-ups, personalização, conversão por label e texto
- Análise por agente, por dia, por faixa horária
- Comparativo convertidos vs não convertidos
- Relatório em HTML (com estilo visual, exportável como PDF) ou Markdown
- Benchmark referência: Omni Hypnosis 09–13/04/2026 (508 leads, 16% conversão)
