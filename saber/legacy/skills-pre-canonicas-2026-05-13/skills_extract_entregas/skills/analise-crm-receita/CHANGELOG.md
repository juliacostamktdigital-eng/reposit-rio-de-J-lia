# CHANGELOG — analise-crm-receita

---

## [1.1.0] — 2026-05-07 — MINOR

**Contexto:** Piloto com Alisson Joias evidenciou que o output JSON não era adequado como entregável consultivo — o formato era legível por máquina mas não documentava lacunas analíticas de forma transparente ao operador. Adicionalmente, a ausência de checks de qualidade de dados causava análises silenciosas onde dados insuficientes simplesmente não apareciam no output.

**O que mudou:**

### Adicionado
- **CHECK 0 — Qualidade dos Dados:** tabela de auditoria prévia (valor preenchido, canal de origem, segmento, bate com faturamento declarado ± 10%) com status ✅/⚠️/❌ e classificação de confiabilidade
- **CHECK 0.5 — Distorção Oculta nos Dados de CRM:** 5 distorções documentadas com como identificar e como corrigir (limite de colunas, ticket inflando métricas, origem confundida, inativos contaminando, segmento heterogêneo)
- Nota específica para plataforma Omie: export padrão não inclui campos de funil — cruzar NF + planilha manual
- Instrução explícita de cobertura obrigatória: análises não executáveis devem aparecer no .md com (a) motivo e (b) o que seria necessário — nunca omitir silenciosamente
- Regra explícita: se concentração ou Win Rate mudar > 20% após check, documentar o ajuste

### Modificado
- Output: de `analise-crm-receita.json` para `analise-crm-receita.md`
- Instrução de geração: output salvo diretamente em arquivo — não apresentado como texto de resposta antes de salvar
- Cada análise (1–5): adicionado bloco `[não executável]` com estrutura padronizada (motivo + o que seria necessário)
- Seção "Para completar esta análise" adicionada ao Resumo Estratégico

### Não modificado
- 5 análises principais (Concentração 80/20, Receita por Segmento, Receita por Canal, Ticket/LTV, Sazonalidade)
- Cruzamento ICP Definido vs Cliente Real
- Perguntas de apresentação ao operador
- Skills sugeridas pós-output (`/gtm-priorizacao-canais`, `/forecast-midia-3-meses`)

---

## [1.0.0] — 2026-01-01

Versão inicial. Output em `.json`. Cinco análises de receita sem checks de qualidade de dados prévios. Análises ausentes por falta de dados eram omitidas silenciosamente.
