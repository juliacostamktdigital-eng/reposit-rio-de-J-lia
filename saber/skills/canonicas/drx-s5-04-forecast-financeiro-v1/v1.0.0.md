---
slug: drx-s5-04-forecast-financeiro-v1
name: drx-s5-04-forecast-financeiro-v1
description: "Constroi a projecao financeira (Forecast) do negocio dentro do projeto DR-X, validando a matematica do funil atual, simulando o impacto da injecao na trava dominante e projetando faturamento mensal e acumulado em 12 meses. Conecta diagno..."
---

# Elaboracao de Forecast

## Descricao
Constroi a projecao financeira (Forecast) do negocio dentro do projeto DR-X, validando a matematica do funil atual, simulando o impacto da injecao na trava dominante e projetando faturamento mensal e acumulado em 12 meses. Conecta diagnostico, funil e projecao financeira em um documento tecnico que serve de base para o Plano de Acao e Cronograma.
Ativar quando forecast, projecao financeira, simulacao de injecao, meta, faturamento projetado for necessario.

## Quando Usar
- Triggers: "forecast", "projecao de faturamento", "simulacao de injecao", "meta financeira", "quanto vai faturar", "projecao 12 meses"
- **NAO usar quando:**
  1. O diagnostico de travas nao foi concluido — sem trava identificada, nao ha injecao para simular
  2. O Cronograma de Implementacao nao foi definido — o forecast precisa de timeline de execucao
  3. Dados financeiros basicos do cliente nao estao disponiveis (faturamento, ticket medio)

## Inputs Necessarios
Solicitar antes de iniciar. Se faltar algum, perguntar antes de prosseguir:

1. **context/business.md** + **context/gtm.md** + **context/constraints.md** `[VALIDADO]` — faturamento, meta, ticket medio, crescimento organico, modelo de venda
2. **Diagnostico de travas 1-7** — trava dominante identificada
3. **CRT** `[VALIDADO]` — causa-raiz e mecanismo do problema
4. **FRT** — injecao validada e sistema futuro projetado
5. **Cronograma de Implementacao** — output da skill-cronograma-implementacao (timeline de acoes)
6. **Fluxo de Estrategia** — output da skill-fluxo-de-estrategia (macroetapas e canais)
7. **Analise de Funil CRM** — metricas reais do funil (win rate, ciclo, volume)
8. **Sizing de Mercado** — TAM/SAM/SOM para validar teto de projecao

---

## Processo de Execucao

### 1. Consolidar Dados Base
Reunir os dados financeiros e operacionais do cliente:

| Campo | Valor | Fonte |
|---|---|---|
| Razao Social | [nome] | arquivos de context/ |
| Segmento | [segmento] | arquivos de context/ |
| Modelo de Venda | [B2B/B2C/Hibrido] | arquivos de context/ |
| Faturamento ultimos 12 meses | [R$] | arquivos de context/ |
| Meta proximos 12 meses | [R$] | arquivos de context/ |
| Faturamento mes atual | [R$] | arquivos de context/ |
| Ticket Medio | [R$] | analise-funil-crm |
| Crescimento organico mensal | [%] | arquivos de context/ |
| CAC | [R$] | arquivos de context/ ou benchmark |
| LTV (meses) | [X] | analise-funil-crm |
| Taxa de recompra | [%] | analise-funil-crm |
| Win rate por segmento | [%] | analise-funil-crm |

### 2. Validar Faturamento Atual via Funil
Reconstruir a matematica do funil para confirmar coerencia:

**Formula base:**
`Faturamento Mensal = Leads/mes x Taxa de Conversao x Ticket Medio`

Para cada fluxo de receita, calcular separadamente e somar.

**Regra:** O faturamento recalculado via funil deve ser coerente com o faturamento declarado (tolerancia de +/-15%). Se divergir, ajustar metricas com justificativa.

### 3. Identificar a Trava Sistemica
A partir do diagnostico, confirmar:
- Qual trava e dominante (da CRT)
- Onde a injecao atua (da FRT)
- Qual metrica do funil sera impactada pela injecao

### 4. Simular Injecao
Definir os parametros da simulacao:

| Parametro | Valor | Justificativa |
|---|---|---|
| Metrica melhorada | [ex: taxa de qualificacao] | [da FRT] |
| Percentual de melhoria | [ex: +20%] | [baseado em benchmark ou capacidade] |
| Tempo de efeito maximo | [ex: 6 meses] | [do cronograma] |
| Curva de ramp-up | [linear/exponencial/step] | [baseado na complexidade] |

**Regra:** O percentual de melhoria deve ser justificado por evidencia (benchmark, capacidade do time, analogos do mercado). Nao usar numeros arbitrarios.

### 5. Projetar Faturamento Mensal (12 meses)
Construir tabela mes a mes com:

| Mes | Receita Atual | Incremento Injecao | Receita Projetada | Acumulado | Delta vs Meta |
|---|---|---|---|---|---|
| M1 | [R$] | [R$] | [R$] | [R$] | [%] |
| M2 | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |
| M12 | ... | ... | ... | ... | ... |

**Logica de ramp-up:** A injecao nao gera efeito total no mes 1. Aplicar curva:
- Meses 1-2: 10-20% do efeito total (estruturacao)
- Meses 3-4: 40-60% (implementacao)
- Meses 5-6: 80-100% (maturacao)
- Meses 7-12: 100% (operacao plena)

### 6. Comparar Cenarios
Construir 3 linhas:
- **Cenario Atual (sem injecao):** crescimento organico apenas
- **Cenario com Injecao:** efeito da intervencao aplicado
- **Meta:** linha de referencia

Calcular:
- Em qual mes a meta e atingida (se atingida)
- Delta total em 12 meses (injecao vs atual)
- ROI estimado da intervencao

### 7. Validar Teto com Sizing
Verificar se a projecao nao excede o SOM:
- Faturamento projetado M12 < SOM? Se sim, projecao e plausivel.
- Se nao: ajustar premissas ou registrar que a meta exige expansao de mercado (conectar com Matriz de Expansao).

### 8. Consolidar Forecast
Documentar tudo em formato final, incluindo premissas explicitas, calculos transparentes e conexoes com artefatos DR-X.

---

## Formato de Saida

```markdown
## Forecast — [Nome do Cliente]
**Data:** [data] | **Consultor:** [nome]
**Horizonte:** 12 meses | **Trava dominante:** [trava]

### Dados Base
[tabela do passo 1]

### Validacao do Funil Atual
[calculo do passo 2 + coerencia]

### Simulacao de Injecao
**Metrica:** [metrica] | **Melhoria:** [%] | **Tempo de efeito:** [X meses]
**Justificativa:** [evidencia]

### Projecao Mensal
[tabela do passo 5]

### Comparativo de Cenarios
| Cenario | Faturamento M12 | Acumulado 12m | Atinge meta? | Mes de atingimento |
|---|---|---|---|---|
| Atual | [R$] | [R$] | [sim/nao] | [mes ou N/A] |
| Com Injecao | [R$] | [R$] | [sim/nao] | [mes] |
| Meta | [R$] | [R$] | — | — |

**Delta total:** [R$] | **ROI estimado:** [X:1]

### Validacao com Sizing
- SOM: [R$] | Projecao M12: [R$] | Plausivel: [sim/nao]

### Premissas
- [lista de premissas explicitas]

### Conexoes com Artefatos DR-X
- CRT: [causa-raiz]
- FRT: [injecao]
- Cronograma: [timeline de efeito]
- Sizing: [teto de mercado]
```

---

## Excecoes e Fallbacks
- **Dados financeiros incompletos:** usar benchmarks do segmento para campos faltantes. Marcar como `ESTIMADO — BENCHMARK` e registrar fonte.
- **Trava dominante nao clara:** simular 2 cenarios (uma injecao para cada candidata) e comparar impacto. Apresentar ambos ao cliente.
- **Meta declarada excede SOM:** registrar como achado estrategico. Recomendar revisao da meta ou expansao de mercado (Matriz de Expansao).
- **Crescimento organico desconhecido:** usar 0% como baseline conservador. O forecast mostra apenas o efeito da injecao.
