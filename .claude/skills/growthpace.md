---
name: growthpace
description: Lê os GrowthPaces de todos os clientes via Google Drive e retorna resumo diário com % pace, R$ investido vs planejado, Leads, CPL e alertas de desvio. Invocar quando a usuária pedir atualização de pace ou verificação de campanhas.
argument-hint: [nome do cliente para filtrar, ex: FCE ou FiveCred — deixe em branco para todos]
---

# Skill: GrowthPace — Verificação Diária de Campanhas

Você é um analista de performance sênior. Sua função é ler as planilhas GrowthPace dos clientes, extrair os dados do mês corrente e entregar um resumo claro com alertas de desvio.

---

## PLANILHAS DOS CLIENTES

| ID do Google Sheets | Cliente |
|---|---|
| 1e2PKWFMxEHoc-9K_0_omXVLiLIT8bASte0J_s6KCiMg | Cliente 1 |
| 1DJYnq3qXC9Td8Fip1LJvFy4qn8XBIIkcGhT8QC2m_M8 | Cliente 2 |
| 1naAmFNzrycM5cddVQDhGduDQx0nZFe0GlgtajOA2fUI | Cliente 3 |
| 1GDiRcey6G4kmx0ybSoIhVJSMRx-LGM5Ae7LepLNMoB0 | Cliente 4 |
| 1y_veFQsSb7q8Nzz_Q0ZD68D29vWM20c578JZDVZLkpU | Cliente 5 |
| 1qGWXaxS2yLu3jX9hTIxX87jwnT1ONi59kFNSSXVIaDY | Cliente 6 |
| 1Trpq5YTb4e_spNIG94bE12z1u6ZWPkPEr_wDPlcz29Y | Cliente 7 |

Se `{{ARGS}}` tiver nome de cliente, processe apenas aquele com mais detalhes.

---

## ESTRUTURA DAS PLANILHAS (padrão V4 Company)

Todas as planilhas têm o mesmo formato markdown com tabelas pipe-separated. O formato de cada linha é:

```
| Campo | valor_periodo1 | valor_periodo2 | valor_periodo3 | ...
```

As abas são concatenadas em sequência no export. As principais seções:

1. **Plano de Mídia** — primeira tabela: `| Canal | % Budget | R$ Budget | R$/dia |`
2. **Acompanhamento Mensal** — colunas = meses (Janeiro, Fevereiro, Março...); linhas = métricas
3. **Acompanhamento por Período** — colunas = períodos mensais com datas (01/04/2026, 01/05/2026, 01/06/2026...); linhas com labels como `Investimento`, `Investimento Meta`, `Investimento Google`, `Leads`, `CPL`
4. **Acompanhamento Diário** — colunas = datas diárias (01/04/2026, 02/04/2026...); linhas com labels

---

## FLUXO OBRIGATÓRIO

Execute sempre nesta ordem:

---

### PASSO 1 — Ler todas as planilhas em paralelo

Chame `mcp__claude_ai_Google_Drive__read_file_content` para todos os 7 IDs **simultaneamente**.

Quando o resultado for salvo em arquivo (tamanho excede limite), anote o caminho. Todos os dados estarão no campo `fileContent` do JSON salvo.

---

### PASSO 2 — Extrair dados via PowerShell

Para cada arquivo salvo em disco, execute este script PowerShell para extrair os dados relevantes:

```powershell
$filePath = "CAMINHO_DO_ARQUIVO.txt"
$data = Get-Content $filePath -Raw | ConvertFrom-Json
$content = $data.fileContent
$lines = $content -split "`n"

# 1. Budget total do Plano de Mídia (primeira tabela - linha TOTAL)
$budgetLine = $lines | Where-Object { $_ -match '^\|\s*TOTAL\s*\|' } | Select-Object -First 1
$budgetMatch = [regex]::Match($budgetLine, 'R\$\s*([\d\.]+,\d{2})')
$budget = if ($budgetMatch.Success) { $budgetMatch.Groups[1].Value } else { "N/A" }

# 2. Budget Disponível (do acompanhamento mensal - última coluna não vazia)
$budgetDispLine = $lines | Where-Object { $_ -match '^\|\s*Budget\s*Dispon' } | Select-Object -First 1
$budgetDispValues = $budgetDispLine -split '\|' | Where-Object { $_ -match 'R\$\s*[\d\.]+,\d{2}' } | Select-Object -Last 1

# 3. Identificar o mês atual nas colunas de período
$hoje = Get-Date
$mesAtual = $hoje.ToString("01/MM/yyyy")  # ex: 01/06/2026
$mesAnterior = $hoje.AddMonths(-1).ToString("01/MM/yyyy")

# 4. Encontrar linha de Investimento total no período atual
# Buscar linha com "| Investimento |" que tenha o maior número de colunas (linha do acompanhamento)
$investLines = $lines | Where-Object { $_ -match '^\|\s*Investimento\s*\|' -and $_ -match 'R\$' }
$mainInvestLine = $investLines | Sort-Object { ($_ -split '\|').Count } | Select-Object -Last 1

# 5. Pegar coluna da linha de Investimento correspondente ao mês atual
# Para isso, pegar a linha de cabeçalho mais próxima antes de $mainInvestLine
# Abordagem simplificada: pegar último valor não-zero/não-REF da linha de Investimento
$investValues = $mainInvestLine -split '\|' | Where-Object { $_ -match 'R\$\s*[\d\.]+,\d{2}' -and $_ -notmatch 'R\$\s*0,00' }
$investAtual = if ($investValues) { ($investValues | Select-Object -Last 1).Trim() } else { "R$ 0,00" }

# 6. Investimento Meta e Google separados
$metaLine = $lines | Where-Object { $_ -match '^\|\s*Investimento\s*Meta\s*\|' -and $_ -match 'R\$' } | Select-Object -Last 1
$googleLine = $lines | Where-Object { $_ -match '^\|\s*Investimento\s*Google\s*\|' -and $_ -match 'R\$' } | Select-Object -Last 1
$metaValues = $metaLine -split '\|' | Where-Object { $_ -match 'R\$\s*[\d\.]+,\d{2}' }
$googleValues = $googleLine -split '\|' | Where-Object { $_ -match 'R\$\s*[\d\.]+,\d{2}' }
$metaAtual = if ($metaValues) { ($metaValues | Select-Object -Last 1).Trim() } else { "—" }
$googleAtual = if ($googleValues) { ($googleValues | Select-Object -Last 1).Trim() } else { "—" }

# 7. Leads
$leadsLine = $lines | Where-Object { $_ -match '^\|\s*Leads\s*\|' -and $_ -match '\|\s*\d+\s*\|' } | Select-Object -Last 1
$leadsValues = $leadsLine -split '\|' | Where-Object { $_ -match '^\s*\d+\s*$' -and [int]($_.Trim()) -gt 0 }
$leadsAtual = if ($leadsValues) { ($leadsValues | Select-Object -Last 1).Trim() } else { "0" }

# 8. CPL
$cplLine = $lines | Where-Object { $_ -match '^\|\s*Custo\s*por\s*Lead\s*\|' -and $_ -match 'R\$' } | Select-Object -Last 1
$cplValues = $cplLine -split '\|' | Where-Object { $_ -match 'R\$\s*[\d\.]+,\d{2}' -and $_ -notmatch 'R\$\s*0,00' }
$cplAtual = if ($cplValues) { ($cplValues | Select-Object -Last 1).Trim() } else { "—" }

# 9. Identificar cliente pelo conteúdo
$clientePatterns = @(
    @{ Pattern = 'FiveCred'; Nome = 'FCE - FiveCred' },
    @{ Pattern = 'Atl[aâ]ntica\s*M[aá]quinas'; Nome = 'ACCE - Atlântica Máquinas' },
    @{ Pattern = 'Taw[aá]\s*Ve[ií]culos|TAWV'; Nome = 'TAWV - Tawá Veículos' },
    @{ Pattern = 'Massimo\s*Zanetti|Segafredo'; Nome = 'MSZB - Massimo Zanetti' },
    @{ Pattern = 'Tecnipool'; Nome = 'TECN1 - Tecnipool' },
    @{ Pattern = 'Fares'; Nome = 'FARS - Fares' },
    @{ Pattern = 'VLoca|V\.?Loca'; Nome = 'SOTB - VLoca' },
    @{ Pattern = 'Oxxy'; Nome = 'Oxxy' },
    @{ Pattern = 'Menegat'; Nome = 'Menegat' },
    @{ Pattern = 'KidysPark'; Nome = 'KidysPark' }
)
$cliente = "Cliente não identificado"
$primeirasParte = $content.Substring(0, [Math]::Min(3000, $content.Length))
foreach ($p in $clientePatterns) {
    if ($primeirasParte -match $p.Pattern) { $cliente = $p.Nome; break }
}

Write-Host "CLIENTE: $cliente"
Write-Host "BUDGET_TOTAL: $budget"
Write-Host "BUDGET_DISP: $($budgetDispValues.Trim())"
Write-Host "INVESTIDO: $investAtual"
Write-Host "META: $metaAtual"
Write-Host "GOOGLE: $googleAtual"
Write-Host "LEADS: $leadsAtual"
Write-Host "CPL: $cplAtual"
```

Execute para cada arquivo. Anote os resultados.

---

### PASSO 3 — Calcular pace para hoje

Com os valores extraídos, calcule:

```
hoje = 02/06/2026
dias_no_mes = 30
dias_decorridos = 2
pace_esperado_% = (2/30) × 100 = 6,7%

Para cada cliente:
  pace_real_% = (valor_investido / budget_disponivel) × 100
  desvio = pace_real_% - pace_esperado_%
```

**Critérios de alerta:**
- Desvio > +20pp → ACELERADO (risco de estourar budget)
- Desvio entre +10 e +20pp → Ligeiramente acelerado
- Desvio entre -10 e +10pp → No pace
- Desvio entre -20 e -10pp → Ligeiro atraso
- Desvio < -20pp → ATRASADO (entrega comprometida)

Se investimento = R$0 e ainda é o início do mês (dia ≤ 3) → marcar como "Aguardando dados GT"

---

### PASSO 4 — Exibir resumo formatado

Organize os dados desta forma:

```
# GrowthPace — 02/06/2026
Pace esperado hoje: 6,7% (dia 2 de 30)

| Cliente | Budget/Mês | Investido (jun) | Pace % | Status | Meta | Google | Leads | CPL |
|---|---|---|---|---|---|---|---|---|
| FCE - FiveCred | R$65.500 | R$278 | 0,4% | 🔴 ATRASADO | R$78 | R$200 | — | — |
...

---
## Alertas críticos
- 🔴 [Cliente] — ATRASADO: pace 0,4% vs esperado 6,7% (desvio -6,3pp)

## Sem dados / Aguardando GT
- [Cliente] — investimento zero no mês (GT ainda não atualizou ou campanha pausada)

---
*Dados do dia 02/06/2026 — atualizados pela GT diariamente*
```

Ordene: ATRASADO → ACELERADO → No pace → Aguardando dados.

---

## REGRAS GERAIS

- Nunca inventar valores. Se o campo retornar `#REF!`, `-`, `#DIV/0!` ou vazio, exibir como `—`.
- Se investimento = R$0 nos primeiros 3 dias do mês, não classificar como ATRASADO — colocar como "Aguardando dados GT".
- Mostrar Meta e Google separados quando disponível.
- Se `{{ARGS}}` tiver nome de cliente, mostrar apenas aquele com dados diários detalhados dos últimos 7 dias.
- Sempre mostrar o pace esperado para o dia de hoje no topo.
