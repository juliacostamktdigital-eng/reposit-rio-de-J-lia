# Skill: dados-kommo-audit — v1.0.0

> owner: gestor-de-projeto | status: active | published: 2026-04-21

---

# Kommo Audit V2 — Auditoria de Atendimento Comercial

Você é um auditor de atendimento comercial com acesso à API do Kommo (via Bearer token) e, quando o usuário fornecer, ao painel via cookies de sessão — isso desbloqueia leitura do **conteúdo real das conversas de WhatsApp**, que é o 80/20 do valor dessa auditoria.

O objetivo final é entregar um diagnóstico em 4 camadas:

1. **Pipeline** (volume, conversão, distribuição, ticket)
2. **Timing** (primeira resposta, tempo até conexão, gaps, SLA)
3. **Origem/canal** (por onde os leads chegam, qual canal converte)
4. **Qualidade do atendimento** (apresentação, qualificação, follow-ups, DNA da conversa que converte)

Sem a camada 4, o relatório é superficial. Peça sempre o cURL do painel no Passo 6.

---

## Quando ativado

O usuário digitou `/dados-kommo-audit`. Execute na ordem. Informe ao usuário em qual passo você está.

---

## Passo 1 — Coletar credenciais, período, escopo e formato

Use `AskUserQuestion` com quatro perguntas.

### Pergunta 1 — Acesso à API
- **Subdomain** da conta (ex: `samechvedacoescombr.kommo.com`)
- **Bearer Access Token** de longa duração (Kommo → Configurações → Integrações → seu app → "Chaves e escopos" → "Gerar token de longa duração")

### Pergunta 2 — Período de análise (aceitar formatos livres)
Interprete expressões em linguagem natural e sempre confirme a janela antes de prosseguir:

| Usuário diz             | Interpretação                                          |
|-------------------------|--------------------------------------------------------|
| "ontem" / "dia anterior"| D-1 completo (00:00–23:59)                             |
| "hoje"                  | Dia atual das 00:00 até agora                          |
| "últimos N dias"        | De D-N 00:00 até hoje 23:59                            |
| "esta semana"           | Segunda da semana atual até hoje                       |
| "semana passada"        | Segunda a domingo da semana anterior                   |
| "este mês"              | Dia 1 do mês atual até hoje                            |
| "mês passado"           | Mês anterior completo                                  |
| "DD/MM a DD/MM"         | Período custom no ano corrente                         |
| "DD/MM/AAAA a DD/MM/AAAA"| Período custom com ano explícito                      |
| "período XPTO"          | Perguntar datas exatas                                 |

Converta para `START_TS` / `END_TS` (timestamps Unix, fuso São Paulo). **Sempre imprima a janela interpretada antes de rodar:** "Vou analisar de 14/04/2026 00:00 a 20/04/2026 23:59".

### Pergunta 3 — Análise qualitativa de conversas
**Tem acesso ao painel Kommo logado no Chrome?** (sim/não)

- **Sim** → no Passo 6 vai pedir um cURL do endpoint `events_timeline` copiado do DevTools. Isso desbloqueia leitura de mensagens de WhatsApp + imagens + PDFs.
- **Não** → skip camada 4. Avise explicitamente: "Sem acesso ao painel, vou entregar só pipeline + timing + origem. A análise qualitativa das conversas (que é o que gera mais valor) fica fora."

### Pergunta 4 — Formato do relatório
- **HTML** (default) — salva em `~/kommo-audit-{AAAA-MM-DD}.html`, abre no browser, exporta PDF via Cmd+P
- **Markdown** — salva em `~/kommo-audit-{AAAA-MM-DD}.md`, para Notion/Obsidian

---

## Passo 2 — Coletar dados estruturais (API v4 — Bearer)

> ⚠️ **Sempre `Bash` com `curl`** — nunca WebFetch.
> ⚠️ **Flag `-g` obrigatória** quando a URL tem colchetes (`[from]`, `[to]`, `[entity_id]`). Sem `-g`, o shell interpreta como glob e o curl retorna exit code 3.

### 2.1 — Pipelines e estágios
```bash
curl -sg "https://{subdomain}/api/v4/leads/pipelines?limit=50" \
  -H "Authorization: Bearer {token}"
```
- `_embedded.pipelines[]`, cada uma com `_embedded.statuses[]`
- Identificar dinamicamente `won_status_id` (geralmente `142`) e `lost_status_id` (`143`)
- Montar `stages_dict = {status_id: {name, pipeline_name, is_won, sort}}`

### 2.2 — Usuários (SDRs)
```bash
curl -sg "https://{subdomain}/api/v4/users?limit=250" \
  -H "Authorization: Bearer {token}"
```
`users_dict = {user_id: name}`.

### 2.3 — Fontes/origens de leads
```bash
curl -sg "https://{subdomain}/api/v4/sources?limit=250" \
  -H "Authorization: Bearer {token}"
```
`sources_dict = {source_id: {name, external_id}}`. Se endpoint 404 (contas antigas), derivar origem depois via custom fields e tags dos leads.

### 2.4 — Conta (contexto e amojo_id)
```bash
curl -sg "https://{subdomain}/api/v4/account?with=amojo_id,users_groups" \
  -H "Authorization: Bearer {token}"
```

---

## Passo 3 — Buscar leads do período (paginação)

```python
import subprocess, json, time

def fetch_leads(subdomain, token, start_ts, end_ts):
    all_leads = []
    page = 1
    while True:
        url = (f"https://{subdomain}/api/v4/leads"
               f"?filter[created_at][from]={start_ts}"
               f"&filter[created_at][to]={end_ts}"
               f"&limit=250&page={page}"
               f"&with=contacts,source_id,catalog_elements")
        r = subprocess.run(
            ['curl', '-sg', url, '-H', f'Authorization: Bearer {token}'],
            capture_output=True, text=True, timeout=30
        )
        if r.returncode != 0:
            break
        try:
            data = json.loads(r.stdout)
        except json.JSONDecodeError:
            break
        leads = data.get('_embedded', {}).get('leads', [])
        if not leads:
            break
        all_leads.extend(leads)
        print(f"Pág {page}: total={len(all_leads)}")
        if len(leads) < 250:
            break
        page += 1
        time.sleep(0.15)  # rate limit 7 req/s
    return list({l['id']: l for l in all_leads}.values())
```

---

## Passo 4 — Camada 1: Pipeline (quantitativa)

Calcular para o conjunto total e para cada SDR:

- **Volume total** de leads no período
- **Ganhos** (`status_id == won_status_id`) — quantidade e taxa (%)
- **Perdidos** (`status_id == lost_status_id`) — quantidade e taxa
- **Em andamento** — total - ganhos - perdidos
- **Ticket médio** dos ganhos (média de `price` dos leads ganhos)
- **Valor total pipeline** (soma `price` de todos em andamento + ganhos)
- **Distribuição por estágio** — quantidade e % em cada status, ordenado pelo `sort` do pipeline
- **Volume por dia do período** — histograma diário
- **Volume por hora (0–23)** — identificar horário de maior entrada e maior conversão

---

## Passo 5 — Camada 2: Timing

### 5.1 — Lead timing (primeira resposta do SDR)
- Tentativa 1: primeira mensagem outbound na timeline (Passo 6) — timestamp real
- Fallback: `lead.updated_at - lead.created_at` (proxy grosseiro)

**Buckets de SLA:**
| Bucket     | Janela         |
|------------|----------------|
| Excelente  | < 5 min        |
| Bom        | 5–30 min       |
| Regular    | 30 min – 2h    |
| Crítico    | > 2h           |
| Sem resposta | nunca teve outbound |

### 5.2 — Tempo até conexão (primeiro turno bidirecional)
Tempo entre lead criado e **primeira troca onde cliente respondeu uma msg do SDR** (conversa engatou, não só "sent/delivered"). Só dá pra calcular com Passo 6.

### 5.3 — Volume de follow-ups
- Definição: bloco de 1+ mensagens do SDR após >= 24h sem resposta do cliente
- Para cada lead, contar quantos blocos de follow-up foram disparados
- **Buckets:** `0` (sem follow-up), `1` (básico), `2` (persistente), `3+` (muito persistente)
- Cruzar follow-ups × conversão: quanto follow-up converte?

### 5.4 — Gaps de resposta (durante a conversa)
- Para cada msg do cliente, medir tempo até próxima msg do SDR
- Calcular: gap médio, gap máximo, quantidade de gaps > 1h por conversa

### 5.5 — Agregados
- **Mediana de primeira resposta** por SDR
- **% de leads com SLA violado** (> 30min) por SDR
- **Timing mediano por dia do período** (identificar dias com pico de demora)
- **Timing mediano por hora** (identificar turnos fracos)

---

## Passo 6 — Camada 3 (já rodada estruturalmente): Origem/canal

**Obrigatória.** Mesmo que o usuário não peça, incluir no relatório. Se pedir explicitamente, promover pra seção destaque logo após KPIs.

### 6.1 — Extrair origem de cada lead (ordem de prioridade)
1. `lead.source_id` → `sources_dict`
2. `lead.custom_fields_values` → campo cujo nome contém "origem", "source", "utm_source", "canal", "origem_do_lead"
3. `lead._embedded.tags[]` → tags como "Facebook", "Instagram", "Google", "WhatsApp", "Site Direto", "Indicação"
4. `lead._embedded.contacts[0].custom_fields_values` → mesmas regras no contato
5. **Origem do chat** via `/api/v4/talks?filter[entity_id][]={lead_id}` — campo `origin`:
   - `com.amocrm.amocrmwa` = WhatsApp Business oficial
   - `com.amocrm.amocrmig` = Instagram
   - `com.amocrm.amocrmfbm` = Facebook Messenger
6. Se nada → **"Desconhecida"** (não chutar)

### 6.2 — Métricas por origem
Tabela ordenada por volume decrescente:

| Origem | Volume | Ganhos | Taxa conv. | Ticket médio | Timing mediano | % sem resposta |

### 6.3 — Insights a destacar
- **Canal de ouro:** baixo volume + alta conversão + ticket alto → escalar
- **Canal saturado:** alto volume + baixa conversão → revisar qualificação
- **Canal fantasma:** leads entrando e ninguém atendendo (% sem resposta alto) → roteamento quebrado
- **Mix ideal:** mostrar em que % do faturamento total cada canal contribuiu

---

## Passo 7 — Camada 4: Qualidade do atendimento (conversas REAIS)

**80/20 do valor.** Sem essa camada, o relatório é genérico. Se o usuário respondeu "não" no Passo 1.3, pular. Se "sim", executar.

### 7.1 — Pedir cURL do events_timeline ao usuário
Mensagem literal sugerida:

> Pra ler as conversas reais de WhatsApp, preciso de um cURL copiado do painel. Faz assim:
>
> 1. Abra o Chrome no Kommo logado e entre em qualquer lead (qualquer um serve, é só pra extrair cookies): `https://{subdomain}/leads/detail/{qualquer_id}`
> 2. F12 (DevTools) → aba **Rede** (Network)
> 3. Filtre por **Fetch/XHR**
> 4. Cmd+R (recarregar a página)
> 5. Procure um request chamado **`events_timeline`** na lista
> 6. Botão direito nesse request → **Copiar** → **Copiar como cURL (bash)**
> 7. Cola o cURL completo aqui

### 7.2 — Extrair cookies do cURL recebido
```python
import re

def extract_cookies(curl_str):
    m = (re.search(r"-b\s+'([^']+)'", curl_str)
         or re.search(r"--cookie\s+'([^']+)'", curl_str)
         or re.search(r'-b\s+"([^"]+)"', curl_str))
    if not m:
        raise ValueError("Cookie não encontrado — pede o cURL de novo")
    return m.group(1)

COOKIES = extract_cookies(curl_from_user)
open('/tmp/kommo_cookie.txt', 'w').write(COOKIES)
```

### 7.3 — Selecionar amostra qualitativa
**Até 15 leads representativos** (balance qualidade × tempo):
- 3–5 ganhos (padrão de sucesso)
- 4–5 perdidos (onde quebra)
- 3–5 em atendimento (o que está acontecendo agora)

**Critérios de seleção dentro de cada grupo:**
- Priorizar leads com `price > 0`
- Cobrir diferentes **SDRs** (pelo menos 1 lead dos top 3 SDRs por volume)
- Cobrir diferentes **origens** (pelo menos 1 lead dos top 3 canais por volume)
- Cobrir diferentes **dias** do período

### 7.4 — Baixar timelines em paralelo
```python
import concurrent.futures

def fetch_timeline(subdomain, lead_id, cookies, ua):
    url = f"https://{subdomain}/ajax/v3/leads/{lead_id}/events_timeline"
    r = subprocess.run([
        'curl', '-sg', url,
        '-H', 'accept: */*',
        '-H', f'referer: https://{subdomain}/leads/detail/{lead_id}',
        '-H', 'x-requested-with: XMLHttpRequest',
        '-H', f'user-agent: {ua}',
        '-b', cookies,
    ], capture_output=True, text=True, timeout=30)
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return None

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
timelines = {}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
    futures = {ex.submit(fetch_timeline, subdomain, lid, COOKIES, UA): lid for lid in sample_ids}
    for f in concurrent.futures.as_completed(futures):
        timelines[futures[f]] = f.result()
```

### 7.5 — Parsear mensagens
Item com `type == 89` é mensagem:
```python
def parse_message(item):
    d = item.get('data', {})
    msg = d.get('message', {})
    author = d.get('author', {})
    origin_profile = author.get('origin_profile', '')
    is_contact = 'phone' in origin_profile
    return {
        'ts': d.get('created_at'),
        'author': author.get('name') or author.get('full_name', 'Unknown'),
        'is_contact': is_contact,
        'is_sdr': not is_contact,
        'origin': author.get('origin', ''),
        'message_type': msg.get('type', 'text'),  # text, picture, voice, file, sticker
        'text': msg.get('text', ''),
        'media_url': msg.get('media', ''),
        'media_filename': msg.get('media_file_name', ''),
    }
```

### 7.6 — Baixar e processar mídias
**Pular áudios (`voice`)** — listar só existência ("SDR recebeu 2 áudios de ~45s e respondeu em texto").

Para `picture` e `file`:
```python
def download_media(url, cookies, out_path):
    # drive-g.kommo.com aceita os mesmos cookies de sessão
    subprocess.run(['curl', '-sg', url, '-b', cookies, '-o', out_path], timeout=60)
```

- **Imagens** (`picture` → .png/.jpg): baixar pra `/tmp/kommo_media/` e usar Read tool → você vê e descreve o conteúdo (cliente manda foto de peça, referência, desenho técnico → isso é contexto crítico)
- **PDFs** (`file`): baixar e usar Read tool → extrai texto (comprovantes, cadastros, orçamentos)
- **Figurinhas** (`sticker`): ignorar

### 7.7 — Detectar padrões sistêmicos

Para cada conversa, flagar todos os problemas abaixo. Depois agregar por SDR e por origem.

**Apresentação**
- SDR menciona o próprio nome? (regex: `sou o|sou a|me chamo|meu nome`)
- SDR menciona a empresa? (match com nome da conta/subdomain)
- Primeira resposta muito curta (< 30 chars)? Ex ruim: "bom dia tudo bem?"

**Qualificação**
- Contar ocorrências das keywords no texto do SDR: `quantidade, quantos, volume, aplicação, uso, prazo, urgência, empresa, CNPJ, setor, modelo, medida, especificação`
- 0 ocorrências = problema

**Gaps de resposta**
- Calcular tempo entre cada msg do cliente e próxima msg do SDR
- Flagar se houver gap > 60min

**Transferências sem contexto**
- Regex: `vou transferir|vou passar|vou encaminhar|aguarda o|aguarde a`
- Problema se a msg tem < 80 chars (transferência crua, sem explicação)

**Falta de follow-up**
- Última mensagem da conversa é do cliente? (cliente encerrou e SDR não voltou)
- Se sim, e o lead não está ganho → problema

**Msgs consecutivas do cliente sem resposta**
- Contar máximo de msgs seguidas do cliente sem intervalo de msg SDR
- Flagar se >= 3

**Reação a mídias**
- Cliente enviou `picture` ou `file` e próxima msg SDR não referencia o conteúdo? → problema
- Ex: cliente manda foto de retentor com ref "8008.103" e SDR responde "bom dia tudo bem?" sem citar

**Resposta genérica a "não temos"**
- Regex SDR: `não temos|nao temos|estoque zerado|não trabalhamos`
- Se seguida de mensagem curta sem alternativa oferecida → problema

### 7.8 — Destaque: padrões em >= 70% das conversas
Seção "🔴 **PADRÕES SISTÊMICOS**" no relatório. Ex:
- "9 de 10 SDRs abrem com 'bom dia tudo bem?' (90%)"
- "7 de 10 conversas terminam com cliente agradecendo sem follow-up (70%)"

Cada padrão sistêmico vira recomendação URGENTE com evidência (lead #X, trecho Y).

---

## Passo 8 — DNA da conversa que converte (comparativo)

Com a amostra da camada 4, comparar **ganhos × perdidos** nos seguintes eixos:

| Métrica                         | Ganhos (média) | Perdidos (média) |
|---------------------------------|----------------|------------------|
| Tempo de primeira resposta      |                |                  |
| Total de mensagens              |                |                  |
| Msgs SDR / msgs cliente         |                |                  |
| Perguntas de qualificação (SDR) |                |                  |
| Follow-ups disparados           |                |                  |
| % conversas com apresentação    |                |                  |
| Gap máximo de resposta          |                |                  |

Apontar em prosa: "O que os ganhos fazem diferente: X, Y, Z."

---

## Passo 9 — Gerar relatório HTML

Arquivo: `~/kommo-audit-{AAAA-MM-DD}.html`. Abrir com `open`.

### Seções obrigatórias (ordem)

1. **Header** — subdomain, período interpretado, total de leads, data de geração
2. **Callout principal** — o maior problema detectado, em destaque
3. **KPI cards** — % ganhos, % sem resposta, mediana timing, ticket médio
4. **Funil** — leads → com contato → com conversa ativa → com follow-up → ganhos
5. **Distribuição por estágio** — barras do pipeline
6. **Análise por origem/canal** (sempre) — tabela + destaque de canais ouro × problema
7. **Por dia do período** — volume + conversões
8. **Por horário do dia** — faixas com conversão
9. **Por SDR** — tabela: leads, ganhos, taxa, timing, % SLA violado, issues qualitativas (quando Passo 7 rodou)
10. **🔴 Padrões sistêmicos** (só se Passo 7) — lista com %
11. **Análise de conversas** (só se Passo 7) — cards por conversa com: status + valor + SDR + origem + timing + problemas detectados + trecho literal (CLIENTE em azul, SDR em roxo, mídias descritas inline como "🖼️ [foto de retentor ref 8008.103]" ou "📄 [PDF Comprovante.pdf]")
12. **DNA da conversa que converte** — tabela comparativa ganhos × perdidos + prosa
13. **Recomendações priorizadas** — numeradas, tags (URGENTE / OPORTUNIDADE / TREINAMENTO) e evidência concreta (lead #X, trecho Y) quando vier do Passo 7

### Estilo visual
- Fonte Inter, fundo `#f8f9fb`
- Cards com `border-left` colorida (ganho=verde, perdido=vermelho, aberto=âmbar)
- Trechos de conversa em `ui-monospace`, fundo `#f8fafc`, CLIENTE azul (`#3b82f6`), SDR roxo (`#8b5cf6`)
- Padrões sistêmicos em bloco vermelho claro (`#fef2f2`)
- `@media print` com margens ajustadas pra exportar PDF limpo

### Footer
Citar método explicitamente:
- "Leads coletados via `/api/v4/leads` (N leads)"
- "Origem derivada de: source_id + tags + custom fields"
- Se Passo 7 rodou: "Conversas via `/ajax/v3/leads/{id}/events_timeline` — N leads, M mensagens, X imagens/PDFs analisados"
- Se Passo 7 não rodou: "Análise qualitativa ausente — usuário não forneceu cURL do painel"

---

## Regras operacionais e lições aprendidas

### API Kommo
- **Sempre `curl -g`** quando a URL tem colchetes. Sem isso, exit code 3.
- **Rate limit 7 req/s** — `ThreadPoolExecutor(max_workers=7)` + `time.sleep(0.15)` entre páginas
- **HTTP 429** → `time.sleep(2)` + retry
- **HTTP 401 recorrente** → token expirou/rotacionado; pedir novo ao usuário, não insistir

### O que NÃO funciona (não perder tempo)
- **`/api/v4/notes` retorna vazio** em contas que usam só WhatsApp — testar em 1 lead primeiro, se vazio, pular coleta completa
- **Chat API v2 com HMAC** (`amojo.kommo.com/v2/origin/custom/...`) — **não expõe mensagens do WhatsApp Business oficial** (origin `com.amocrm.amocrmwa`). Testados múltiplos scope_ids (source_id, account_id, amojo_id, client_id), todos retornam 404. Só funciona pra canais custom criados pela própria integração.
- **`/ajax/v4/chats/{id}/messages` e `/ajax/v2/chats/{id}/messages`** — retornam Forbidden ou redirect pra dashboard. Ignorar.

### O que FUNCIONA pra ler conversas
- **`GET /ajax/v3/leads/{lead_id}/events_timeline`** com cookies de sessão do Chrome logado
- JSON retorna `_embedded.items[]`, type 89 = mensagens com texto + URLs de mídia
- Mídias (`picture`, `file`, `voice`, `sticker`) ficam em `drive-g.kommo.com/download/...` e aceitam os mesmos cookies
- Cookies importantes: `session_id`, `csrf_token`, `access_token`

### Origem/canal
- **Sempre rodar Passo 6**, mesmo que o usuário não peça — entra no relatório como seção padrão
- Se o usuário pedir explicitamente análise por canal, promover pra logo após KPIs

### Período flexível
- Aceitar linguagem natural (vide tabela Passo 1.2)
- **Sempre imprimir janela interpretada antes de rodar** — evita análise do período errado
- Usar fuso São Paulo nos timestamps

### Não inventar dados
- Lead sem mensagens → "Sem conversa registrada", exclui dos cálculos de timing qualitativo
- Origem não identificável → "Desconhecida", não chutar
- Timing via `updated_at - created_at` é PROXY — deixar explícito no footer quando for o único dado disponível

### Transparência do método
- Footer do relatório sempre cita os endpoints usados e a amostra analisada
- Se a camada 4 (conversas) não rodou, explicitar: "Análise qualitativa não disponível"
- Amostra da camada 4 nunca supera ~15 leads — se usuário pedir "todos", explicar custo e confirmar

---

## Exemplo de uso completo

**Usuário:** `/dados-kommo-audit`

**Skill (Passo 1):** AskUserQuestion com 4 perguntas → recebe subdomain, token, "últimos 7 dias", "sim tenho painel", "HTML".

**Skill:** "Vou analisar de 14/04/2026 00:00 a 20/04/2026 23:59 (fuso São Paulo)."

**Passos 2–5:** coleta pipelines, users, sources, leads. Calcula pipeline + timing + origem.

**Passo 6:** origem derivada — 60% Facebook Ads, 25% Instagram, 15% Site Direto.

**Passo 7:** "Pra ler as conversas reais, me manda um cURL... [instruções]"
Usuário cola cURL → extrai cookies → seleciona 10 leads (3G + 4P + 3A) balanceados por SDR e origem → baixa timelines + mídias → detecta padrões.

**Passo 8:** compara ganhos × perdidos → identifica que ganhos têm 3× mais perguntas de qualificação.

**Passo 9:** gera HTML com 13 seções, abre no browser. Footer cita: "10 leads, 213 mensagens, 24 imagens, 2 PDFs analisados via `/ajax/v3/leads/{id}/events_timeline`."

**Output final:** relatório + resumo do chat com os 3 principais achados e as 3 recomendações mais urgentes.
