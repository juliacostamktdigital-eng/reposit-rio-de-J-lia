---
name: dashboard-refresh
description: Lê todos os GrowthPacks via Google Drive, extrai métricas do mês atual e salva no cache do dashboard. Rodar sempre que quiser atualizar os dados do dashboard.
argument-hint: "[opcional: tickers específicos, ex: FARE1 TECN1]"
---

# Skill: Dashboard Refresh

Você vai ler os GrowthPacks dos clientes via Google Drive MCP, extrair as métricas do mês atual (hoje é {{CURRENT_DATE}}) e salvar o cache do dashboard em `dashboard/cache/sprint-data.json`.

---

## CLIENTES E GROWTHPACKS

| Ticker | Nome            | fileId                                         | Tipo |
|--------|-----------------|------------------------------------------------|------|
| ACCE   | VLoca           | 1DJYnq3qXC9Td8Fip1LJvFy4qn8XBIIkcGhT8QC2m_M8  | EC   |
| NATU   | Natuclean       | 192GhJhK66MrCytkpDuWQFR7vvuIJrChMcpU-LNJI2hg  | IS   |
| FARE1  | Fares Aquino    | 1y_veFQsSb7q8Nzz_Q0ZD68D29vWM20c578JZDVZLkpU  | IS   |
| MSZB   | Massimo Zanetti | 1Trpq5YTb4e_spNIG94bE12z1u6ZWPkPEr_wDPlcz29Y  | EC   |
| SOTB   | Atlantica Maq.  | 1GDiRcey6G4kmx0ybSoIhVJSMRx-LGM5Ae7LepLNMoB0  | IS   |
| TAWV   | Tawa Veículos   | 1qGWXaxS2yLu3jX9hTIxX87jwnT1ONi59kFNSSXVIaDY  | IS   |
| TECN1  | Tecnipool       | 1e2PKWFMxEHoc-9K_0_omXVLiLIT8bASte0J_s6KCiMg  | IS   |

> **ATENÇÃO**: Os IDs do NATU e TAWV podem estar incorretos — os arquivos lidos em jun/2026 retornaram dados de outros clientes. Se o budget retornar "—" ou os dados não baterem, sinalizar para Julia verificar com a GT.

Se {{ARGS}} contiver tickers específicos, processar apenas esses. Caso contrário, processar todos.

---

## FLUXO

### Passo 1 — Ler cada GrowthPack via Google Drive MCP

Para cada cliente, use `mcp__claude_ai_Google_Drive__read_file_content` com o fileId. O resultado pode ser um arquivo temporário grande (80-240k chars).

### Passo 2 — Extrair dados via PowerShell

Use o seguinte script PowerShell para processar TODOS os arquivos salvos. Substitua `[PATH_TICKER]` pelos caminhos retornados pelas leituras acima.

```powershell
$invCulture = [cultureinfo]::InvariantCulture

function isValid($v) {
    if ($null -eq $v) { return $false }
    $s = [string]$v
    return -not ($s -eq "" -or $s -eq "-" -or $s -eq "—" -or $s -match '#REF|#DIV|#VALUE|#N/A|#NULL' -or $s -match '^\s*$')
}

function parseBRL($str) {
    if (-not (isValid $str)) { return 0.0 }
    $c = [string]$str -replace "R\$\s*","" -replace "\s","" -replace "\.","" -replace ",","."
    $d = [ref]0.0
    if ([double]::TryParse($c, [System.Globalization.NumberStyles]::Any, $invCulture, $d)) { return [Math]::Round($d.Value, 2) }
    return 0.0
}

function parseNum($str) {
    if (-not (isValid $str)) { return 0 }
    $c = [string]$str -replace "[^\d]",""; if ($c -eq "") { return 0 }
    $n = 0; if ([int]::TryParse($c, [ref]$n)) { return $n }; return 0
}

function fmtBRL($val) {
    if ($val -le 0) { return "—" }
    $s = ("{0:N0}" -f $val)
    return "R$ " + $s
}

function getCell($lines, $pat, $idx, $maxCols=0) {
    if ($idx -lt 0) { return $null }
    foreach ($l in $lines) {
        if ($l -match $pat) {
            $cells = $l -split '\|' | ForEach-Object { $_.Trim() }
            if ($maxCols -gt 0 -and $cells.Count -gt $maxCols) { continue }
            if ($cells.Count -gt $idx) { $v = $cells[$idx]; if (isValid $v) { return $v } }
        }
    }
    return $null
}

function extractBudget($lines) {
    # 1) Linha TOTAL com BRL > 0
    foreach ($l in $lines) {
        if ($l -match '^\|\s*TOTAL\s*\|') {
            $bm = [regex]::Match($l, 'R\$[\d.]+,\d{2}')
            if ($bm.Success -and (parseBRL $bm.Value) -gt 0) { return $bm.Value }
        }
    }
    # 2) Verba de midia
    foreach ($l in $lines) {
        if ($l -match '(?i)^\|\s*Verbademidia\s*\|') {
            $bm = [regex]::Match($l, 'R\$[\d.]+,\d{2}')
            if ($bm.Success -and (parseBRL $bm.Value) -gt 0) { return $bm.Value }
        }
    }
    # 3) Soma subtotais Google + Meta (min 2)
    $sub = 0.0; $cnt = 0
    foreach ($l in $lines) {
        if ($l -match '(?i)\|\s*Subtotal\s*\|' -and $l -match 'R\$[\d.]+,\d{2}') {
            $bm = [regex]::Match($l, 'R\$([\d.]+,\d{2})')
            if ($bm.Success) { $v = parseBRL $bm.Value; if ($v -gt 0) { $sub += $v; $cnt++ } }
        }
    }
    if ($sub -gt 0 -and $cnt -ge 2) {
        $f = ("{0:N2}" -f $sub) -replace "^(\d+)\.(\d{3}),(\d{2})$", '$1.$2,$3'
        return "R$" + $f
    }
    return "—"
}

function extractGP($filePath, $ticker) {
    if (-not (Test-Path $filePath)) { return $null }
    $raw = (Get-Content $filePath -Encoding UTF8 -Raw | ConvertFrom-Json).fileContent
    if (-not $raw) { return $null }

    # Dividir em linhas ANTES de normalizar
    $lines = $raw -split "(?:\\n|\r?\n)"
    # Normalizar caracteres espaçados (ex: "F a c e b o o k" -> "Facebook")
    for ($p = 0; $p -lt 15; $p++) {
        $lines = $lines -replace '([A-Za-zÀ-ÿ0-9$.,\#]) ([A-Za-zÀ-ÿ0-9$.,\#])', '$1$2'
    }

    # Encontrar coluna do mês atual — dois formatos
    $junhoIdx = -1; $maiIdx = -1; $headerCols = 0
    foreach ($l in $lines) {
        if ($l -match '^\|\s*M[eê]s\s*\|' -and $l -match '\|\s*junho\s*\|' -and $l -notmatch '\d{2}/\d{2}/\d{4}/junho') {
            $cols = $l -split '\|' | ForEach-Object { $_.Trim().ToLower() }
            for ($i = 0; $i -lt $cols.Count; $i++) {
                if ($cols[$i] -eq "junho") { $junhoIdx = $i; if ($i -ge 1) { $maiIdx = $i-1 }; break }
            }
            $headerCols = $cols.Count; break
        }
        if ($l -match '^\|\s*M[eê]s\s*\|' -and $l -match '\d{2}/06/2026/junho') {
            $cols = $l -split '\|' | ForEach-Object { $_.Trim() }
            for ($i = 0; $i -lt $cols.Count; $i++) {
                if ($cols[$i] -match '06/2026/junho') { $junhoIdx = $i; if ($i -ge 1) { $maiIdx = $i-1 }; break }
            }
            $headerCols = $cols.Count; break
        }
    }
    $maxC = if ($headerCols -gt 0) { $headerCols + 2 } else { 0 }

    $rawBudget = extractBudget $lines

    $rawInvest = "—"
    if ($junhoIdx -ge 0) {
        $v = getCell $lines '(?i)^\|\s*InvestimentoReal\s*\|' $junhoIdx $maxC
        if (-not (isValid $v)) { $v = getCell $lines '(?i)^\|\s*Investimento\s*\|' $junhoIdx $maxC }
        if (isValid $v) { $rawInvest = $v }
    }
    if ($rawInvest -eq "—" -and $maiIdx -ge 0) {
        $v = getCell $lines '(?i)^\|\s*InvestimentoReal\s*\|' $maiIdx $maxC
        if (-not (isValid $v)) { $v = getCell $lines '(?i)^\|\s*Investimento\s*\|' $maiIdx $maxC }
        if (isValid $v) { $rawInvest = $v }
    }

    # Meta Ads e Google Ads separados
    $rawMetaInvest   = "—"
    $rawGoogleInvest = "—"
    if ($junhoIdx -ge 0) {
        $vm = getCell $lines '(?i)^\|\s*(InvestimentoMeta|InvestimentoFacebook|Meta)\s*\|' $junhoIdx $maxC
        if (isValid $vm) { $rawMetaInvest = $vm }
        $vg = getCell $lines '(?i)^\|\s*(InvestimentoGoogle|Google)\s*\|' $junhoIdx $maxC
        if (isValid $vg) { $rawGoogleInvest = $vg }
    }

    $rawLeads     = getCell $lines '(?i)^\|\s*Leads\s*\|' $junhoIdx $maxC
    $rawMQL       = getCell $lines '(?i)^\|\s*MQL\s*\|' $junhoIdx $maxC
    $rawSQL       = getCell $lines '(?i)^\|\s*SQL\s*\|' $junhoIdx $maxC
    $rawMetaLeads = getCell $lines '(?i)^\|\s*MetadeLeads\s*\|' $junhoIdx $maxC

    $rawVendas = $null
    if ($junhoIdx -ge 0) {
        $v = getCell $lines '(?i)^\|\s*Vendas\s*\|' $junhoIdx $maxC
        if (-not (isValid $v)) { $v = getCell $lines '(?i)^\|\s*Compras\s*\|' $junhoIdx $maxC }
        if (isValid $v) { $rawVendas = $v }
    }

    $rawCPL = "—"
    $v = getCell $lines '(?i)^\|\s*CustoportLead\s*\|' $junhoIdx $maxC
    if (-not (isValid $v)) { $v = getCell $lines '(?i)^\|\s*CPL\s*\|' $junhoIdx $maxC }
    if (isValid $v) { $rawCPL = $v }

    $rawFat = "—"
    $v = getCell $lines '(?i)^\|\s*(ReceitaFaturada|FaturamentoDireto|Faturamento)\s*\|' $junhoIdx $maxC
    if (isValid $v) { $rawFat = $v }

    # Mensagem da semana atual
    $semanaAtual = (Get-Date | Get-Date -UFormat "%V")
    $mensagem = ""
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -match "Semana\s+0*$semanaAtual\b|S0*$semanaAtual\b") {
            for ($j = $i+1; $j -lt [Math]::Min($i+20, $lines.Count); $j++) {
                $l = $lines[$j].Trim()
                if ($l -and $l.Length -gt 8 -and $l -notmatch '^[\|\-: ]+$' -and
                    $l -notmatch '(?i)^\|\s*(Mês|Janeiro|Fevereiro|Março|Abril|Maio|Junho|---)\s*\|') {
                    $clean = ($l -replace '^\||\|$','').Trim() -replace '\*+','*' -replace '\s+',' '
                    if ($clean -and $clean.Length -gt 8 -and $clean -notmatch '^[-:| ]+$') {
                        $mensagem = $clean; break
                    }
                }
            }
            if ($mensagem) { break }
        }
    }

    $budgetVal  = parseBRL $rawBudget
    $investVal  = parseBRL $rawInvest
    $metaVal    = parseBRL $rawMetaInvest
    $googleVal  = parseBRL $rawGoogleInvest
    $cplVal     = parseBRL $rawCPL
    $fatVal     = parseBRL $rawFat

    return @{
        rawBudget   = if ($budgetVal -gt 0) { fmtBRL $budgetVal } else { "—" }
        rawInvest   = if ($investVal -gt 0) { fmtBRL $investVal } else { "—" }
        rawCPL      = $rawCPL
        rawFat      = if ($fatVal -gt 0) { fmtBRL $fatVal } else { "—" }
        rawMeta     = if ($metaVal -gt 0) { fmtBRL $metaVal } else { "—" }
        rawGoogle   = if ($googleVal -gt 0) { fmtBRL $googleVal } else { "—" }
        budget      = $budgetVal
        investido   = $investVal
        meta        = $metaVal
        google      = $googleVal
        cpl         = $cplVal
        faturamento = $fatVal
        leads       = parseNum $rawLeads
        mql         = parseNum $rawMQL
        sql         = parseNum $rawSQL
        vendas      = parseNum $rawVendas
        metaLeads   = parseNum $rawMetaLeads
        mensagem    = $mensagem
    }
}

$clientMap = @(
    @{ t="ACCE";  n="VLoca";             tipo="EC"; f="[PATH_ACCE]"  }
    @{ t="NATU";  n="Natuclean";         tipo="IS"; f="[PATH_NATU]"  }
    @{ t="FARE1"; n="Fares Aquino";       tipo="IS"; f="[PATH_FARE1]" }
    @{ t="MSZB";  n="Massimo Zanetti";    tipo="EC"; f="[PATH_MSZB]"  }
    @{ t="SOTB";  n="Atlantica Maquinas"; tipo="IS"; f="[PATH_SOTB]"  }
    @{ t="TAWV";  n="Tawa Veículos";      tipo="IS"; f="[PATH_TAWV]"  }
    @{ t="TECN1"; n="Tecnipool";          tipo="IS"; f="[PATH_TECN1]" }
)

$clientes = @()
foreach ($c in $clientMap) {
    $gp = extractGP $c.f $c.t
    if (-not $gp) {
        $gp = @{ rawBudget="—"; rawInvest="—"; rawCPL="—"; rawFat="—"; rawMeta="—"; rawGoogle="—";
                 budget=0; investido=0; meta=0; google=0; cpl=0; faturamento=0;
                 leads=0; mql=0; sql=0; vendas=0; metaLeads=0; mensagem="" }
    }
    $clientes += @{ ticker=$c.t; nome=$c.n; tipo=$c.tipo; gp=$gp; hs=@{ flag="N/D"; score=0; lt=0 }; com=$null }
}

$cache = @{ savedAt=(Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ"); clientes=$clientes }
$cacheFile = "c:\Users\Windows User\OneDrive\Desktop\skills_colli_co-main\dashboard\cache\sprint-data.json"
$enc = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText($cacheFile, ($cache | ConvertTo-Json -Depth 10), $enc)
Write-Host "Cache salvo: $cacheFile"

try { Invoke-RestMethod "http://localhost:3001/api/refresh" -TimeoutSec 5 | Out-Null } catch {}
```

### Passo 3 — Confirmar resultado

```powershell
$r = Invoke-RestMethod "http://localhost:3001/api/sprint-data?force=1" -TimeoutSec 10
Write-Host "Semana $($r.semana) | $($r.periodo) | Pace esp: $($r.paceEsperado)%"
foreach ($c in $r.clientes) {
    Write-Host "  $($c.ticker) | Budget: $($c.gp.rawBudget) | Invest: $($c.gp.rawInvest) | Pace: $($c.paceReal)% | Leads: $($c.gp.leads)"
}
```

Reportar para Julia:

| Ticker | Budget | Investido | Pace% | Leads | MQL | SQL | Vendas |
|--------|--------|-----------|-------|-------|-----|-----|--------|

Dashboard disponível em **http://localhost:3001**

Se NATU ou TAWV retornar dados vazios ou inconsistentes (budget errado, métricas de ecommerce para IS), avisar Julia para verificar os IDs das planilhas com a GT.

---

## NOTAS TÉCNICAS

1. **Normalizar ANTES de dividir em linhas** — usar `$lines = $content -split "..."` primeiro, depois `$lines = $lines -replace '...'`
2. **Sem BOM** — sempre usar `[System.IO.File]::WriteAllText($path, $json, (New-Object System.Text.UTF8Encoding $false))`
3. **parseBRL com InvariantCulture** — sem `$invCulture`, `.` é interpretado como separador de milhar
4. **"R$" + $f, não "R$$f"** — `$$` em PowerShell é variável automática (PID)
5. **maxCols** — filtra tabelas de tracking diário que têm mais colunas que a tabela mensal
6. **Formatos por cliente**:
   - ACCE, TECN1: padrão `| Mês | Janeiro | ... | junho | Total |`, budget via linha TOTAL
   - MSZB: ecommerce, budget via Subtotais Google+Facebook
   - SOTB: header com datas `| Mês | 31/01/2024/Janeiro | ... | 11/06/2026/junho |`
   - FARE1: formato padrão, budget pode não ter linha TOTAL preenchida
   - NATU, TAWV: IDs precisam de verificação — podem estar trocados
