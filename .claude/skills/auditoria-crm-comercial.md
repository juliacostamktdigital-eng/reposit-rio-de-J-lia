---
skill: auditoria-crm-comercial
version: v1.0.0
description: Auditoria integrada de CRM + planilha comercial — identifica leads sem MQL/SQL/Obs, analisa conversas Chatwoot/Kommo e mostra etapas do kanban e valores de venda
---

# Auditoria CRM Comercial

Auditoria em duas camadas para clientes V4:
- **Camada 1 — Planilha Comercial**: lê o CSV em `data/com/{TICKER}.csv` e mostra leads sem preenchimento de MQL, SQL ou observação pelo comercial
- **Camada 2 — CRM de conversas**: audita Chatwoot ou Kommo e entrega diagnóstico de timing, follow-up, taxa de conversão e etapas do kanban

---

## Passo 1 — Identificar cliente e camadas disponíveis

Pergunte ao usuário (ou derive do contexto):

1. **Ticker do cliente** — FCE, FARS, TECN1, SOTB, ACCE, TAWV, MSZB
2. **CRM de conversas** — Chatwoot, Kommo ou nenhum
3. **Escopo** — só planilha, só CRM, ou ambos

Clientes com valor de venda confirmado (usar no relatório):
- SOTB (Atlantica Maquinas) — tickets de máquinas industriais
- TAWV (Tawá Veículos) — tickets de veículos especiais
- ACCE — a confirmar

---

## Camada 1 — Planilha Comercial

### 1.1 Localizar o arquivo

O CSV fica em `C:\Users\Windows User\OneDrive\Desktop\Lps\painel\data\com\{TICKER}.csv`

Se não existir, informe que o CSV ainda não foi configurado para este cliente e oriente a exportar a planilha do Google Sheets com o comando:
> **Arquivo → Fazer download → CSV da aba ativa**

### 1.2 Estruturas conhecidas

| Ticker | Estilo | Colunas-chave |
|--------|--------|---------------|
| FCE | status | `status`, `observações`, `receita` |
| FARS | MQL/SQL | `mql`, `sql`, `observações comerciais`, `venda concluída`, `receita de vendas` |
| TECN1 | MQL/SQL | `mql (tem interesse no serviço)`, `sql (intenção de fechar)`, `observações comerciais`, `venda concluída`, `receita de vendas` |

**FCE tem múltiplas abas por produto** — ao auditar, exportar cada aba separadamente e nomear como `FCE_veículos.csv`, `FCE_consórcio.csv`, etc. Analisar cada aba individualmente.

### 1.3 Métricas a calcular

```
total_leads     = total de linhas com dados
sem_mql         = linhas onde MQL está vazio
sem_sql         = linhas onde SQL está vazio
sem_obs         = linhas onde Observações está vazio
receita_total   = soma da coluna receita (converter "R$ 1.234,56" → float)
taxa_sem_obs    = sem_obs / total_leads (%)
```

Para FCE (estilo status):
```
sem_status      = linhas onde Status está vazio
por_status      = contagem agrupada por valor de Status
fechados        = status contém "fecha" ou "comprou"
```

### 1.4 Card de alerta — leads sem atualização

Gerar um card em destaque quando `sem_obs > 0` OU `sem_mql > 0` OU `sem_sql > 0`:

```
⚠️  {sem_obs} leads sem observação · {sem_mql} sem MQL · {sem_sql} sem SQL
    precisam de atualização pelo comercial
```

Listar os primeiros 20 leads afetados com: nome, data de entrada, o que está faltando.

### 1.5 Saída da Camada 1

Relatório HTML ou Markdown com:
- KPI cards: total, sem obs, MQL, SQL, vendas, receita
- Alerta de gaps em vermelho
- Distribuição por status (FCE) ou funil MQL→SQL→Venda (FARS/TECN1)
- Lista de leads sem atualização (até 20, ordenados por data mais antiga primeiro)

---

## Camada 2 — CRM de Conversas

### Para Chatwoot

> Usar a skill completa em `executar/executar/agents/gestor-de-projeto/chatwoot-audit/latest.md`

Inputs necessários:
- URL base da instância (ex: `https://chatwoot.empresa.com`)
- API Access Token (Chatwoot → Perfil → Access Token)
- Account ID (na URL: `/app/accounts/N/`)
- Período de análise

Métricas principais: % sem resposta, % convertidos, timing mediano, follow-ups por agente, padrão da conversa que converte.

### Para Kommo

> Usar a skill completa em `executar/executar/agents/gestor-de-projeto/dados-kommo-audit/`

Inputs necessários:
- Subdomínio (ex: `clientexyz.kommo.com`)
- Bearer token (Kommo → Configurações → Integrações)
- Período de análise
- cURL do painel (opcional, mas desbloqueia leitura de conversas reais)

Métricas adicionais para clientes com valor de venda (SOTB, TAWV): ticket médio, receita por etapa do kanban, previsão de receita por pipeline.

### Etapas do Kanban a mapear

Para cada lead no CRM, registrar em qual etapa está:
```
Lead → Contato feito → Qualificado → Proposta enviada → Em negociação → Ganho / Perdido
```

Calcular: volume por etapa, tempo médio em cada etapa, taxa de avanço entre etapas.

---

## Camada 3 — Cruzamento Planilha × CRM (quando ambos disponíveis)

Quando o usuário tiver tanto a planilha comercial quanto o CRM auditado:

1. Cruzar leads pelo telefone ou nome (fuzzy match)
2. Identificar leads que estão na planilha mas NÃO estão no CRM — possível perda de contato
3. Identificar leads que estão no CRM como "Ganho" mas sem receita na planilha — subnotificação
4. Verificar se os MQLs da planilha batem com "Qualificado" no CRM

---

## Output Final

Relatório HTML salvo em `~/auditoria-crm-{TICKER}-{AAAA-MM-DD}.html` com:

1. Header — cliente, período, data de geração
2. Callout principal — maior problema identificado
3. KPI cards — total leads, gaps planilha, conversão CRM, receita
4. Planilha Comercial — distribuição, gaps, lista pendentes
5. CRM de Conversas — timing, follow-up, conversão por agente
6. Kanban — volume e taxa de conversão por etapa
7. Cruzamento — divergências entre planilha e CRM
8. Recomendações — priorizadas com urgência (URGENTE / OPORTUNIDADE / TREINAMENTO)

**Estilo visual**: fonte Inter, fundo `#f8f9fb`, cards com `border-left` colorida (vermelho = crítico, azul = info, verde = positivo), tabelas com hover, `@media print` para exportar PDF.

---

## Regras operacionais

- Nunca inventar dados — se coluna não existe, reportar como "não disponível"
- Sempre usar `Bash + curl` para APIs (nunca WebFetch)
- Para arquivos grandes (>500 linhas), processar em blocos e mostrar progresso
- FCE: sempre lembrar de verificar se há múltiplas abas exportadas
- Clientes SOTB e TAWV: sempre incluir análise de ticket médio e receita esperada
