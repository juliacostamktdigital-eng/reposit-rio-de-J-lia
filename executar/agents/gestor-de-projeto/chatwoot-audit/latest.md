# chatwoot-audit v1.0.0

## Passo 1 — Coletar credenciais e parâmetros

Use `AskUserQuestion` para fazer **2 perguntas**:

**Pergunta 1 — Acesso:**
- URL base da instância (ex: `https://chatwoot.suaempresa.com`, sem barra no final)
- API Access Token (Chatwoot → Perfil → "Access Token")
- Account ID (visível na URL: `/app/accounts/N/` — geralmente `1`)

**Pergunta 2 — Escopo e formato:**
- Período de análise: data início e data fim (ex: "09/04 a 13/04"). Se não informado, usar os últimos 7 dias.
- Formato do relatório:
  - **HTML** — abre no browser, exporta como PDF via `Cmd+P`. Ideal para apresentar ao time.
  - **Markdown** — para usar no Notion, Obsidian ou VSCode.

---

## Passo 2 — Buscar conversas via API

> ⚠️ **SEMPRE use `Bash` com `curl`** — nunca `WebFetch`. A API do Chatwoot exige autenticação via header que o WebFetch não suporta. Se receber 401, confirme que o token está no header `api_access_token`, não na query string.

```bash
curl -s "{base_url}/api/v1/accounts/{account_id}/conversations?page=N&sort=-created_at" \
  -H "api_access_token: {token}"
```

### Estratégia de paginação por período

A API retorna 25 conversas por página. O `sort=-created_at` **não é totalmente ordenado** — não pare na primeira página com datas fora do período. Varra página por página até que 2 páginas consecutivas estejam inteiramente anteriores ao período.

```python
START_TS = unix_timestamp(data_inicio + " 00:00:00")
END_TS   = unix_timestamp(data_fim + " 23:59:59")

all_convs = []
old_pages = 0

for page in range(1, 500):
    convs = fetch_page(page)
    in_period = [c for c in convs if START_TS <= c['created_at'] <= END_TS]
    all_convs.extend(in_period)

    if all(c['created_at'] < START_TS for c in convs):
        old_pages += 1
        if old_pages >= 2: break
    else:
        old_pages = 0

# Deduplicar por ID
all_convs = list({c['id']: c for c in all_convs}.values())
```

Mostre progresso durante a coleta: `"Pág 5: coletadas=118 | última=09/04 | stop=False"`

### Filtrar apenas leads humanos

Excluir conversas onde `sender.name` contenha: `evolutionapi`, `bot`, `webhook`, `automation`. Excluir `message_type: 2` (activity messages) de todas as listas de mensagens.

---

## Passo 3 — Buscar mensagens em paralelo

Com muitas conversas (50+), use `ThreadPoolExecutor` para não demorar:

```python
import concurrent.futures, subprocess, json

def fetch_messages(conv_id):
    url = f"{base_url}/api/v1/accounts/{account_id}/conversations/{conv_id}/messages"
    r = subprocess.run(['curl', '-s', url, '-H', f'api_access_token: {token}'],
                       capture_output=True, text=True, timeout=20)
    data = json.loads(r.stdout)
    return {'conv_id': conv_id, 'messages': data.get('payload', [])}

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch_messages, conv_ids))
```

Para cada conversa, separe:
- `outgoing` = `message_type: 1` e não `private` — mensagens do agente
- `incoming` = `message_type: 0` — mensagens do lead
- Use `conversation.first_reply_created_at` para timing quando disponível (mais preciso que calcular manualmente)

---

## Passo 4 — Calcular métricas por conversa

### Lead Timing
- Preferir `first_reply_created_at` da conversa; senão, `min(outgoing.created_at)`
- Diferença em minutos entre `conversation.created_at` e primeira resposta
- `< 5 min` = Excelente | `5–30 min` = Bom | `30 min–2h` = Regular | `> 2h` = Crítico | sem outgoing = **Sem resposta**

### Distinção crítica para "Sem resposta"

> **Conceito-chave:** o SDR deve ser SEMPRE quem abre a conversa — o lead não deve precisar escrever primeiro. Portanto, toda conversa sem mensagem do agente é um GAP de atendimento, independentemente de o lead ter escrito ou não.

Ao detalhar as "sem resposta", registre a distinção para diagnóstico operacional:
- **Lead ativo ignorado**: lead enviou mensagem, agente não respondeu → problema mais grave, ação imediata
- **Lead não abordado (conversa vazia)**: sistema registrou o lead, mas o SDR ainda não iniciou contato → também é um GAP

Ambos contam como falha de atendimento no total de "sem resposta".

### Follow-ups
- Follow-up = bloco de mensagens de saída após ter havido ao menos 1 mensagem de entrada, sem resposta do lead entre os blocos
- `0` = Sem follow-up | `1` = Básico | `2+` = Persistente

### Personalização
- **Alto**: menciona nome do lead E faz perguntas de qualificação sobre objetivo/contexto/perfil
- **Médio**: usa nome OU faz perguntas, mas não ambos consistentemente
- **Baixo**: template sem referência ao lead, sem perguntas de qualificação

### Conversão (agendamento de reunião)
Use as labels da conversa:
- `conectado` = agendou reunião → **CONVERTIDO**
- `qualificado_ia` = avançou mas não agendou → **QUALIFICADO**
- `alerta` = lead problemático
- `desqualificado` / `numero_invalido` = perdido

Também verificar no texto das mensagens do agente: links `meet.google`, `calendly`, `cal.link`, `bloqueei o horário`.

---

## Passo 5 — Calcular métricas agregadas

### Por agente
Total de leads, % sem resposta, timing mediano, % follow-up, % personalização alta, **taxa de conversão** (convertidos/total).

### Por dia do período
Volume, % sem resposta, % excelente timing, % follow-up, % personalização alta. Identifica dias problemáticos.

### Por horário do dia
Leads e convertidos por hora → taxa de conversão por faixa horária. Leads de madrugada (0–6h) e noite (19–23h) costumam converter significativamente mais.

### Comparativo convertidos vs não convertidos
Para os dois grupos, calcular médias de: timing, follow-ups, msgs do agente, msgs do lead, número de perguntas (`?`), chars totais escritos, % personalização alta.

---

## Passo 6 — Gerar relatório

Salvar conforme o formato escolhido no Passo 1 e abrir com `open`.

**Se HTML:** `~/chatwoot-audit-{AAAA-MM-DD}.html`
**Se Markdown:** `~/chatwoot-audit-{AAAA-MM-DD}.md`

### Seções obrigatórias do relatório

1. **Header** — período, total de leads, instância
2. **Callout de alerta principal** — o maior problema encontrado em destaque
3. **KPI cards** — % sem resposta (vermelho), % convertidos (azul/verde), % follow-up (amarelo), mediana timing (verde)
4. **Funil de conversão** — barras: leads → respondidos → convertidos
5. **Evolução por dia** — métricas por dia do período
6. **Por agente** — tabela com: leads, sem resposta, timing mediano, follow-up, personal. alta, taxa de conversão
7. **Análise das "sem resposta"** — total de GAPs, distinção entre lead ativo ignorado vs lead não abordado
8. **Comparativo convertidos vs não convertidos** — dois boxes lado a lado com métricas
9. **DNA da conversa que converte** — exemplos reais de fluxo de mensagens boas vs ruins, extraídos dos dados
10. **Conversão por horário** — tabela por faixa horária com taxa
11. **Análise qualitativa** — padrões, insights, diagnóstico em prosa
12. **Recomendações numeradas** — com tags de urgência (URGENTE / OPORTUNIDADE / TREINAMENTO)

**Se HTML:** use o estilo visual desenvolvido nas auditorias anteriores — fonte Inter, fundo `#f8f9fb`, cards com `border-left` colorida, badges coloridos, tabelas com hover, `@media print` para PDF.

---

## Regras operacionais

- **Sempre use Bash + curl** — nunca WebFetch para a API
- **Mostre progresso durante coleta** de mensagens: ex. `"50/508 | 5s | ~42s restantes"`
- **Toda conversa sem mensagem do agente é um GAP** — não minimize como "conversa vazia"
- **Calcule taxa de conversão sempre** — é a métrica mais estratégica
- **Identifique o padrão textual** que separa convertidos de não convertidos com exemplos reais das mensagens
- **Não invente dados** — conversas sem mensagens entram como "Sem mensagens" e são excluídas dos cálculos de timing/personalização

---

## Benchmark — Omni Hypnosis (09–13/04/2026, 508 leads)

Use como referência ao interpretar auditorias da mesma instância:

- **Taxa de conversão**: 16% geral (David 20,5% · Layslla 11,3% · Alexandre 0%)
- **Convertidos**: 7,6 msgs agente | 3,3 follow-ups | 5,4 perguntas | 80% personalização alta
- **Não convertidos**: 1,6 msgs agente | 0,4 follow-ups | 2,1 perguntas | 11% personalização alta
- **Sequência vencedora**: contexto do lead → meta de renda → histórico de investimentos → preço → agendamento
- **Erro fatal**: revelar o preço antes de qualificar disposição financeira
- **Melhores horários**: madrugada 0–6h (56% conversão) · noite 19h (75%) · noite 20–23h (23%)
- **Pior horário**: tarde 13–17h (11%) apesar de concentrar 60% do volume
- **Paradoxo Layslla vs David**: Layslla escreve melhor, David converte mais — diferença está no volume de follow-up (32% vs 18%)
- **Labels úteis**: `conectado` = convertido | `qualificado_ia` | `alerta` | `desqualificado`
