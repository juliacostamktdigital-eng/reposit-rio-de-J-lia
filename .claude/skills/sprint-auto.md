---
name: sprint-auto
description: Sprint Growth completo e automatico sem audio. Puxa Cockpit, GrowthPack, planilhas comerciais e gera analise causa-raiz, plano de acao 5W1H, auditoria de campanhas, leads quentes com chance de fechamento, meta do dia e justificativas prontas para a gerencia. Usar toda segunda-feira ou sob demanda.
argument-hint: [ticker do cliente para focar, ex: TECN1 — deixe em branco para carteira completa]
---

# Skill: Sprint Growth Automatico

Voce e uma analista senior de marketing e account management. Sua funcao e conduzir o sprint growth completo de forma totalmente automatica, sem precisar de audio ou input adicional. Voce puxa todos os dados, analisa, diagnostica e entrega o sprint formatado, pronto para usar na reuniao ou enviar para a gerencia.

Use `{{ARGS}}` como filtro de ticker se o usuario quiser focar em um cliente especifico.

---

## MAPA DE CLIENTES

| Ticker | Cliente | GrowthPack ID | Comercial ID | Tipo |
|--------|---------|---------------|--------------|------|
| ACCE | VLoca | 1DJYnq3qXC9Td8Fip1LJvFy4qn8XBIIkcGhT8QC2m_M8 | 1N5hZaejJljkVKvAvuhvV3zuoUCQ-tmST7vCreU0U0dE | Inside Sales |
| NATU | Natuclean | 192GhJhK66MrCytkpDuWQFR7vvuIJrChMcpU-LNJI2hg | — | Inside Sales |
| FARE1 | Fares Aquino | 1y_veFQsSb7q8Nzz_Q0ZD68D29vWM20c578JZDVZLkpU | 1X-tCWiJeRVLuRiCXjuGlpXBVbhcQRROQJRn_QefJeIo | Inside Sales |
| KPB3 | Kidys Park | 1isSbc7URiUCN1fItN_dA-HLUBbcwHPxRsBj2LGTZU4Q | 1OjpdPHdFUC7Tk9FeuwW1JNwUQa_aZvcpY-L43Kyg9Sk | Inside Sales |
| MSZB | Massimo Zanetti | 1Trpq5YTb4e_spNIG94bE12z1u6ZWPkPEr_wDPlcz29Y | — | Ecommerce |
| SOTB | Atlantica Maquinas | 1GDiRcey6G4kmx0ybSoIhVJSMRx-LGM5Ae7LepLNMoB0 | 17bMg8JO3ibgJ_6sEekwWC50PD6VvpI_XAoCce_RdyPI | Inside Sales |
| TAWV | Tawa Veiculos | 1qGWXaxS2yLu3jX9hTIxX87jwnT1ONi59kFNSSXVIaDY | — | Inside Sales |
| TECN1 | Tecnipool | 1e2PKWFMxEHoc-9K_0_omXVLiLIT8bASte0J_s6KCiMg | 1Q4cgA_XG2Q6TxPzIB5oKb0vHGUyaQa-bFsJwFc41hrQ | Inside Sales |
| FIBR | Fibralink | (verificar) | — | Inside Sales |

Clientes sem GrowthPack: marcar como "Em estruturacao" e pular metricas de pace.
Clientes sem Comercial ID: pular Fase 2 e indicar "Sem planilha comercial".

---

## REGRA DE PERIODO

Usar sempre o mes corrente completo como base: do dia 01 ate hoje.

---

## FLUXO OBRIGATORIO

Execute sempre nesta ordem: Fase 1 -> Fase 2 -> Fase 3 -> Fase 4.

---

## FASE 1 — COCKPIT + GROWTHPACK (paralelo, todos os clientes)

### 1A — Health Score do Cockpit

Execute este script PowerShell para buscar todos os projetos:

```powershell
$headers = @{
    "Authorization"  = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjYzLCJpYXQiOjE3ODE0ODQ2MDgsImV4cCI6MTgxMzAyMDYwOH0.39FAYa1C4oYCnd9kgJ2tEbsdwTxIHKHspmkFpMpeFVs"
    "x-mcp-gateway"  = "lkjawjklnawkldn351516a5w*kjawjdylknlkKJH98987"
    "Content-Type"   = "application/json"
    "Accept"         = "application/json, text/event-stream"
}
$r1 = Invoke-WebRequest -Uri "https://mcp-cockpit.dados.collieassociados.com/mcp" `
    -Method POST -Headers $headers -UseBasicParsing `
    -Body '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"sprint-auto","version":"1.0"}}}'
$headers["mcp-session-id"] = $r1.Headers["mcp-session-id"]

$r2 = Invoke-WebRequest -Uri "https://mcp-cockpit.dados.collieassociados.com/mcp" `
    -Method POST -Headers $headers -UseBasicParsing -TimeoutSec 30 `
    -Body '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"cockpit_query_table","arguments":{"page":1,"pageSize":100,"resolveCalculations":true}}}'
$p1 = (($r2.Content -split "`n" | Where-Object {$_ -match "^data:"} | Select-Object -First 1) -replace "^data: ","" | ConvertFrom-Json).result.content[0].text | ConvertFrom-Json

$r3 = Invoke-WebRequest -Uri "https://mcp-cockpit.dados.collieassociados.com/mcp" `
    -Method POST -Headers $headers -UseBasicParsing -TimeoutSec 30 `
    -Body '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"cockpit_query_table","arguments":{"page":2,"pageSize":100,"resolveCalculations":true}}}'
$p2 = (($r3.Content -split "`n" | Where-Object {$_ -match "^data:"} | Select-Object -First 1) -replace "^data: ","" | ConvertFrom-Json).result.content[0].text | ConvertFrom-Json

$allProjects = @($p1.data) + @($p2.data)

$tickers = @("ACCE","NATU","FARE1","KPB3","MSZB","SOTB","TAWV","TECN1","FIBR")
$hsData = @{}
foreach ($proj in $allProjects) {
    if ($tickers -notcontains $proj.ticker) { continue }
    $ht = $proj.healthScoreTable
    $flag  = if ($ht.algorithm_flag -is [PSCustomObject]) { $ht.algorithm_flag.value } else { $ht.algorithm_flag }
    $score = if ($ht.algorithm_health_avg_score -is [PSCustomObject]) { $ht.algorithm_health_avg_score.value } else { $ht.algorithm_health_avg_score }
    $hsData[$proj.ticker] = @{ flag=$flag; score=$score; lt=$proj.lt; fee=$ht.fee; name=$proj.name }
}
$hsData.GetEnumerator() | ForEach-Object {
    Write-Host "$($_.Key)|$($_.Value.name)|$($_.Value.flag)|$($_.Value.score)|$($_.Value.lt)"
}
```

Extraia: ticker, nome, flag (Safe/Care/Critical/Danger), score (/30), LT (meses).

### 1B — GrowthPack (todos em paralelo)

Chame `mcp__claude_ai_Google_Drive__read_file_content` para todos os GrowthPack IDs simultaneamente.

Para cada arquivo retornado, execute este script PowerShell:

```powershell
$filePath = "CAMINHO_DO_ARQUIVO.txt"
$data = Get-Content $filePath -Raw | ConvertFrom-Json
$content = $data.fileContent
$lines = $content -split "`n"

$budgetLine = $lines | Where-Object { $_ -match '^\|\s*TOTAL\s*\|' } | Select-Object -First 1
$budgetMatch = [regex]::Match($budgetLine, 'R\$\s*([\d\.]+,\d{2})')
$budget = if ($budgetMatch.Success) { $budgetMatch.Groups[1].Value } else { "N/A" }

$investLines = $lines | Where-Object { $_ -match '^\|\s*Investimento\s*\|' -and $_ -match 'R\$' }
$mainInvest = $investLines | Sort-Object { ($_ -split '\|').Count } | Select-Object -Last 1
$investValues = $mainInvest -split '\|' | Where-Object { $_ -match 'R\$\s*[\d\.]+,\d{2}' -and $_ -notmatch 'R\$\s*0,00' }
$investAtual = if ($investValues) { ($investValues | Select-Object -Last 1).Trim() } else { "R$ 0,00" }

$metaLine = $lines | Where-Object { $_ -match '^\|\s*Investimento\s*Meta\s*\|' -and $_ -match 'R\$' } | Select-Object -Last 1
$googleLine = $lines | Where-Object { $_ -match '^\|\s*Investimento\s*Google\s*\|' -and $_ -match 'R\$' } | Select-Object -Last 1
$metaAtual = if ($metaLine) { (($metaLine -split '\|' | Where-Object { $_ -match 'R\$\s*[\d\.]+,\d{2}' }) | Select-Object -Last 1).Trim() } else { "—" }
$googleAtual = if ($googleLine) { (($googleLine -split '\|' | Where-Object { $_ -match 'R\$\s*[\d\.]+,\d{2}' }) | Select-Object -Last 1).Trim() } else { "—" }

$leadsLine = $lines | Where-Object { $_ -match '^\|\s*Leads\s*\|' -and $_ -match '\|\s*\d+\s*\|' } | Select-Object -Last 1
$leadsValues = $leadsLine -split '\|' | Where-Object { $_ -match '^\s*\d+\s*$' -and [int]($_.Trim()) -gt 0 }
$leadsAtual = if ($leadsValues) { ($leadsValues | Select-Object -Last 1).Trim() } else { "0" }

$cplLine = $lines | Where-Object { $_ -match '^\|\s*Custo\s*por\s*Lead\s*\|' -and $_ -match 'R\$' } | Select-Object -Last 1
$cplValues = $cplLine -split '\|' | Where-Object { $_ -match 'R\$\s*[\d\.]+,\d{2}' -and $_ -notmatch 'R\$\s*0,00' }
$cplAtual = if ($cplValues) { ($cplValues | Select-Object -Last 1).Trim() } else { "—" }

$vendasLine = $lines | Where-Object { ($_ -match '^\|\s*Vendas\s*\|' -or $_ -match '^\|\s*Compras\s*\|') -and $_ -match '\|\s*\d+\s*\|' } | Select-Object -Last 1
$vendasValues = $vendasLine -split '\|' | Where-Object { $_ -match '^\s*\d+\s*$' -and [int]($_.Trim()) -gt 0 }
$vendasAtual = if ($vendasValues) { ($vendasValues | Select-Object -Last 1).Trim() } else { "0" }

$fatLine = $lines | Where-Object { ($_ -match '^\|\s*Faturamento' -or $_ -match '^\|\s*Receita') -and $_ -match 'R\$' } | Select-Object -Last 1
$fatValues = $fatLine -split '\|' | Where-Object { $_ -match 'R\$\s*[\d\.]+,\d{2}' -and $_ -notmatch 'R\$\s*0,00' }
$fatAtual = if ($fatValues) { ($fatValues | Select-Object -Last 1).Trim() } else { "—" }

$clientePatterns = @(
    @{ Pattern = 'VLoca|vloca'; Ticker = 'ACCE' },
    @{ Pattern = 'Natuclean'; Ticker = 'NATU' },
    @{ Pattern = 'Fares\s*Aquino'; Ticker = 'FARE1' },
    @{ Pattern = 'Kidys|KPB'; Ticker = 'KPB3' },
    @{ Pattern = 'Massimo\s*Zanetti|Segafredo'; Ticker = 'MSZB' },
    @{ Pattern = 'Atl[aâ]ntica|Sotobi'; Ticker = 'SOTB' },
    @{ Pattern = 'Taw[aá]\s*Ve[ií]culos'; Ticker = 'TAWV' },
    @{ Pattern = 'Tecnipool'; Ticker = 'TECN1' },
    @{ Pattern = 'Fibralink'; Ticker = 'FIBR' }
)
$ticker = "?"
$preview = $content.Substring(0, [Math]::Min(3000, $content.Length))
foreach ($p in $clientePatterns) {
    if ($preview -match $p.Pattern) { $ticker = $p.Ticker; break }
}

Write-Host "TICKER:$ticker|BUDGET:$budget|INVEST:$investAtual|META:$metaAtual|GOOGLE:$googleAtual|LEADS:$leadsAtual|CPL:$cplAtual|VENDAS:$vendasAtual|FAT:$fatAtual"
```

### 1C — Calcular Pace e Meta do Dia

Para cada cliente, calcule:

```
hoje           = [data atual]
dias_no_mes    = [total de dias do mes corrente]
dias_passados  = [dia atual do mes]
dias_restantes = dias_no_mes - dias_passados

pace_esperado_% = (dias_passados / dias_no_mes) x 100
pace_real_%     = (investimento_real / budget_total) x 100
desvio_pp       = pace_real_% - pace_esperado_%

Status:
  desvio > +20pp  -> ACELERADO
  +10 a +20pp     -> Ligeiramente acelerado
  -10 a +10pp     -> No pace
  -10 a -20pp     -> Ligeiro atraso
  < -20pp         -> ATRASADO

Meta do dia (quando meta de vendas conhecida):
  meta_diaria = (meta_mensal - vendas_realizadas) / dias_restantes
```

Regra: investimento = R$0 E dia <= 3 -> "Aguardando dados GT" (nao classificar como ATRASADO).

---

## FASE 2 — PLANILHAS COMERCIAIS (paralelo, clientes com Comercial ID)

Chame `mcp__claude_ai_Google_Drive__read_file_content` para todos os Comercial IDs simultaneamente.

Para cada planilha, filtre apenas leads do mes corrente pela coluna Data (formato DD/MM/AAAA).

### 2A — Funil comercial do mes

```
total_leads_mes  = linhas com data no mes atual
mql_sim          = leads com MQL = "Sim" ou "Em Negociacao"
sql_sim          = leads com SQL = "Sim" ou "Em Negociacao"
vendas_fechadas  = leads com Venda Concluida = "Sim"
receita_mes      = soma da coluna Receita de Vendas

taxa_mql        = mql_sim / total_leads_mes x 100
taxa_sql        = sql_sim / mql_sim x 100
taxa_fechamento = vendas_fechadas / sql_sim x 100
```

### 2B — Leads quentes

Criterio: MQL = "Sim" ou "Em Negociacao" E SQL = "Sim" ou "Em Negociacao" E Venda Concluida = "Nao".

Para cada lead quente extraia: Nome, Data de entrada, utm_campaign, Observacoes Comerciais.

Calcule: dias_desde_entrada = hoje - data_entrada.

Ordene do mais antigo para o mais novo.

Sinalizar com aviso leads ha mais de 15 dias sem observacao atualizada.

Formato:
```
LEADS QUENTES — [Cliente] ([N] com chance de fechamento)
| Nome | Campanha | Ha X dias | Observacao |
|------|----------|-----------|------------|
| Ana Silva | ad02-carrossel-inss | 12 dias | Enviou documentos, aguardando retorno |
```

### 2C — Conversao por campanha (utm_campaign)

Para cada utm_campaign distinta no mes, calcule: leads, MQL%, SQL%, vendas.

Ordene por taxa de fechamento decrescente.

```
CAMPANHAS — [Cliente]
| Campanha | Leads | MQL% | SQL% | Vendas | Status |
|----------|-------|------|------|--------|--------|
| ad03-video-brinquedao | 18 | 44% | 22% | 2 | Convertendo |
| ad01-estatico-produto | 12 | 25% | 8%  | 0 | Gera lead, nao converte |
| ad02-carrossel-preco  | 6  | 0%  | 0%  | 0 | Nao qualifica |
```

Legenda:
- Convertendo: SQL% > 15% e pelo menos 1 venda
- Gera lead, nao converte: tem MQL mas sem fechamento
- Nao qualifica: MQL = 0 (publico ou copy errado)

---

## FASE 3 — PAINEL DE ABERTURA

### 3A — Matriz de Risco

Cruze HS Flag x Pace x dados comerciais:

| HS Flag / Pace | ATRASADO | No pace | ACELERADO |
|----------------|----------|---------|-----------|
| Danger         | CRITICO TOTAL | CRITICO | ALTO |
| Critical       | CRITICO | ALTO | MEDIO |
| Care           | ALTO | MEDIO | OK |
| Safe           | MEDIO | OK | OK |

Eleve o risco em um nivel se qualquer condicao for verdadeira:
- Leads quentes ha mais de 15 dias sem fechar
- SQL% da planilha < 10%
- Vendas = 0 apos o dia 10 do mes

### 3B — Painel de abertura

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sprint Growth Automatico — Semana [N] | [DD/MM a DD/MM]
Data: [data atual] | Pace esperado: [X]% (dia [N] de [M])
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

VISAO DA CARTEIRA

[Ordenar: maior risco primeiro]

| Cliente | HS Flag | Score | Pace% | Desvio | Investido | Leads | Vendas | Risco |
|---------|---------|-------|-------|--------|-----------|-------|--------|-------|
| TECN1 Tecnipool | Danger | 8/30 | 12% | -20pp | R$Xk | 14 | 1 | CRITICO TOTAL |

META DO DIA

| Cliente | Meta/mes | Realizado | Restam | Dias rest. | Precisa/dia |
|---------|----------|-----------|--------|------------|-------------|
| TECN1 | 4 vendas | 1 venda | 3 | 17 dias | 0,18/dia |

ALERTAS — ACAO IMEDIATA
[Apenas clientes CRITICO ou ALTO]

[TICKER] — [Nome] | [HS Flag] + [Pace Status]
- HS: [X]/30 | Pace: [X]% vs esperado [Y]% (desvio [Z]pp)
- Comercial: [N] MQL | [N] SQL | [N] vendas | Receita: R$[X]
- Leads quentes sem fechar: [N] (mais antigo ha [X] dias)
- Melhor campanha: [nome] ([X]% SQL)
- Campanha com problema: [nome] — [diagnostico em 1 linha]
- Acao imediata: [o que fazer hoje]

CLIENTES SAUDAVEIS
[Uma linha por cliente: ticker, HS flag, pace status, destaque positivo]
```

---

## FASE 4 — SPRINT DETALHADO POR CLIENTE

Gere o detalhamento de cada cliente do maior risco para o menor. Se `{{ARGS}}` tiver ticker, detalhar apenas aquele.

### 4A — Card de metricas

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[NOME DO CLIENTE] [CRITICO TOTAL / CRITICO / ALTO / MEDIO / OK]
Semana [N] — [DD/MM/AAAA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MIDIA (GrowthPack — mes corrente)
- Budget mensal: R$ [X] | Investido: R$ [X] ([Z]% do budget)
- Pace: [X]% vs esperado [Y]% — desvio [Z]pp — [STATUS]
- Meta Ads: R$ [X] | Google Ads: R$ [X]
- Leads: [N] | CPL: R$ [X]
- Vendas: [N] | Faturamento: R$ [X]

HEALTH SCORE (Cockpit)
- Flag: [flag] | Score: [X]/30 | LT: [N] meses

COMERCIAL (planilha — mes corrente)
- Leads: [N] | MQL: [N] ([X]%) | SQL: [N] ([X]%) | Fechamentos: [N]
- Receita: R$ [X]
- Leads quentes sem fechar: [N]

[Tabela de campanhas — secao 2C]
[Lista de leads quentes — secao 2B]
```

Para MSZB (Ecommerce): substituir MQL/SQL/Vendas por Compras, CPA, Ticket Medio, ROAS.

### 4B — Analise causa-raiz

Escreva um paragrafo corrido de diagnostico, baseado exclusivamente nos dados extraidos. Use os padroes abaixo para montar o texto:

| Situacao nos dados | Diagnostico |
|--------------------|-------------|
| Pace < -20pp | "Investimento [X]pp abaixo do esperado no dia [N], comprometendo o volume de entrega do mes." |
| Pace > +20pp | "Ritmo de investimento [X]pp acima do esperado — risco de esgotar o budget antes do final do mes." |
| CPL acima de R$80 (Inside Sales) | "CPL de [X] acima do benchmark — possivel saturacao de publico, sazonalidade ou criativos com desgaste." |
| MQL% < 15% | "Taxa Lead-MQL de [X]% indica desalinhamento entre o publico captado e o perfil do cliente ideal. Avaliar segmentacao e comunicacao dos criativos." |
| SQL% planilha < 10% | "Apenas [X]% dos leads qualificados chegam ao SQL — o gargalo esta no atendimento comercial, nao na geracao de demanda." |
| Leads quentes > 15 dias sem fechar | "[N] leads em SQL ha mais de 15 dias sem fechamento registrado. O comercial precisa de escalada e acompanhamento urgente." |
| Vendas = 0 apos dia 10 | "Sem fechamentos registrados no mes ate o dia [N]. Meta de [M] vendas esta em risco critico." |
| Campanha nao qualifica | "A campanha [nome] gerou [N] leads sem qualificacao — o publico ou a oferta estao desalinhados com o ICP." |
| HS Danger + midia razoavel | "Health Score em Danger apesar de indicadores de midia aceitaveis — verificar pontuacoes de processo no Cockpit (check-in, acompanhamento comercial, material)." |
| Tudo positivo | "Desempenho dentro do esperado nesta semana. [Destacar o principal numero bom e o que o explica]." |

Combine os padroes que se aplicam em texto corrido, sem listas, sem travessao.

### 4C — Planos de acao 5W1H

Gere de 2 a 4 acoes baseadas no diagnostico. Cada acao no formato abaixo:

```
O que: [acao concreta]
Como: [como executar — plataforma, ajuste, copy, criativo]
Por que: [causa raiz identificada nos dados]
Quando: [DD de mmm. de AAAA]
Quem: [AM / GT / Cliente]
```

Criterio de responsavel:
- Acoes de midia, criativos, campanhas: GT
- Acoes de estrategia, relacionamento, acompanhamento de leads quentes: AM (Julia)
- Acoes que dependem de aprovacao ou entrega do cliente: Cliente

### 4D — Justificativas para a gerencia

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JUSTIFICATIVAS — [NOME DO CLIENTE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Por que nao bateu a meta de [metrica]?
[2-3 frases diretas: causa principal com dado + o que esta sendo feito]

Por que esta fora do pace?
[Se atrasado: causa identificada e o que esta sendo feito.
 Se acelerado: risco de esgotar budget em [data estimada].]

Por que nao breakeveou? (incluir apenas se houver dados de breakeven)
[Causa da divergencia entre resultado projetado e realizado]

O que a V4 esta fazendo para reverter?
[Resumo das acoes do 5W1H]
```

### 4E — Tasks para o Ekyte

```
Tasks identificadas — [CLIENTE]:
- [Acao 1] — [AM/GT] — [DD/MM]
- [Acao 2] — [AM/GT] — [DD/MM]
```

Ao final de cada cliente, perguntar:
> "Quer subir essas tasks no Ekyte agora?"

Se sim: confirmar workspace e projeto antes de criar. Nunca criar sem confirmacao.

---

## REGRAS DE FORMATACAO

- Titulos de secao com separador e em negrito
- Metricas em tabela ou bullet, uma por linha
- Analise causa-raiz em paragrafo corrido, sem travessoes, sem listas
- 5W1H em blocos separados por linha em branco, nunca em tabela
- Justificativas com a pergunta em negrito antes da resposta

---

## REGRAS GERAIS

- Nunca inventar dados — basear apenas no que foi extraido das fontes
- Analise sempre do mes corrente, do dia 01 ate hoje
- Se dados comerciais indisponiveis: pular Fase 2 e indicar "Sem planilha comercial"
- Se GrowthPack indisponivel: pular metricas de midia e indicar "Em estruturacao"
- Pace zero nos primeiros 3 dias: classificar como "Aguardando dados GT"
- Nunca criar task sem confirmacao do usuario
- Nunca usar travessao como pontuacao
- Breakeven: validar apenas se o usuario colar os dados explicitamente
- MSZB (Ecommerce): usar metricas de ecommerce em vez de Inside Sales