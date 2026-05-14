# Referência — Loop de ajuste A-4 ↔ playbook 18

## Âncoras no canônico

| Conceito | Onde |
|----------|------|
| Ação quando KPI piora | Passo 5 — *o que muda quando piora (ação definida)* |
| Evitar só “ler número” | Componentes críticos — *rotina decisória* |
| Marketing ajusta oferta/mensagem/segmentação com dado de handoff | Componentes críticos — *loop de ajuste* |
| KPIs de entrada | § Gerenciado — taxa MQL→SQL, SQL→venda, 1º contato, % rejeições por motivo, % leads sem status |
| Registro pós-decisão | § Gerenciado + DoD — ata/card + change log |

## Campos JSON principais

| Bloco | Uso |
|-------|-----|
| `leitura_kpis` | Valor observado × faixa V/A/V × referência ao threshold do protocolo |
| `sinais_qualitativos` | Rejeições, SLA, voz de vendas — insumo para hipóteses |
| `hipoteses_causa` | Causa → evidência → confiança |
| `plano_acao` | Mudança concreta; `leva_em`: segmentação \| mensagem \| oferta \| processo_comercial \| crm \| outro |
| `registro` | Onde ficou a decisão (ata, change log, próxima data) |

## Auditoria (`--audit`)

- Meta (projeto, período, link protocolo A-4).
- Pelo menos **3** linhas em `leitura_kpis` com `faixa` preenchida.
- Se alguma faixa for **vermelho** ou **amarelo**, exige **≥1** ação em `plano_acao` com `descricao` + `responsavel` **ou** justificativa explícita em `registro.justificativa_sem_acao`.
- Com ação no plano: `registro.ata_ou_card` ou `registro.changelog_funil_ou_protocolo` preenchido.

## `faixa` em `leitura_kpis`

Valores aceitos pelo script: `verde`, `amarelo`, `vermelho` (normalização semelhante às outras skills).
