# CHANGELOG — dados-kommo-audit

## [v1.0.0] — 2026-04-21

### Inicial
- Versão de lançamento
- Auditoria de atendimento comercial no Kommo CRM em 4 camadas: pipeline, timing, origem/canal e qualidade do atendimento
- Coleta estrutural via API v4 (Bearer token): pipelines, usuários, fontes, leads com paginação e rate limit de 7 req/s
- Interpretação de período em linguagem natural (ontem, últimos N dias, mês passado, custom, etc.) com confirmação explícita da janela
- Análise qualitativa opcional via cookies de sessão do painel Kommo (endpoint `/ajax/v3/leads/{id}/events_timeline`) — desbloqueia leitura de mensagens de WhatsApp, imagens e PDFs reais
- Detecção de padrões sistêmicos: apresentação, qualificação, gaps de resposta, transferências sem contexto, falta de follow-up, reação a mídias
- DNA comparativo ganhos × perdidos em 7 eixos (timing, volume de msgs, qualificação, follow-ups, apresentação, gaps)
- Amostra balanceada de até 15 leads (ganhos + perdidos + em andamento) cobrindo top SDRs, top origens e dias diferentes
- Output em HTML (default, com export para PDF via print) ou Markdown (Notion/Obsidian)
- Degradação graceful: se usuário não fornecer cURL do painel, roda só as 3 primeiras camadas e explicita no footer
- Transparência de método obrigatória no footer (endpoints usados, tamanho de amostra, o que ficou de fora)
