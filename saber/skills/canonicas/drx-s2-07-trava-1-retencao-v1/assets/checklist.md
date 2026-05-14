# Checklist: Diagnóstico — Trava 1 (Retenção)

**Objetivo:** Diagnosticar se o sistema transforma vendas em geração cumulativa de Throughput ou depende estruturalmente de aquisição constante.
**Responsável:** Consultor DR-X
**Frequência:** Uma vez por cliente — etapa de Análise Diagnóstica do DR-X
**Referência:** context-trava-1-retencao.md (definições, gabarito e interpretação)

---

## Antes de Começar
- [ ] Identificar o(s) modelo(s) de venda aplicável(is): Inside Sales / Vendas Online / PDV
- [ ] Solicitar: base de clientes ativos/inativos (últimos 12 meses), receita por cliente, data de aquisição, produto, canal e CAC médio
- [ ] Verificar se histórico >= 6 meses está disponível — registrar limitação se não

---

## Execução

### Camada Analítica — Leitura Econômica

**Cohort de Retenção:**
- [ ] Construir tabela: mês de aquisição / clientes iniciais / ativos após 3m / ativos após 6m / ativos após 12m
- [ ] ⚠️ Se não for possível construir cohort: **registrar formalmente como fragilidade estrutural**

**LTV vs CAC:**
- [ ] Calcular LTV médio real (receita total por cliente no período disponível)
- [ ] Comparar LTV com CAC médio:
  - LTV <= CAC → **retenção crítica** ⚠️
  - LTV pouco superior ao CAC → risco estrutural
- [ ] Registrar interpretação

**Receita Recorrente:**
- [ ] Calcular % da receita proveniente da base existente (vs. novos clientes)
- [ ] Analisar por produto/serviço

### Camada Experiencial — por Modelo de Venda
**Inside Sales (se aplicável):**
- [ ] Solicitar proposta real e registrar processo até fechamento
- [ ] Após fechamento (simular): existe onboarding estruturado?
- [ ] Existe reunião de acompanhamento definida?
- [ ] Após 30 dias: houve contato proativo? Houve proposta adicional?
- [ ] Simular cliente inativo: existe processo formal de reativação?

**Vendas Online (se aplicável):**
- [ ] Realizar compra real e mapear: confirmação, comunicação pós-compra, oferta de recompra/expansão
- [ ] Medir tempo até primeiro contato pós-compra e existência de automação
- [ ] Verificar remarketing ativo para base

**PDV (se aplicável):**
- [ ] Realizar compra presencial e observar: solicitação de cadastro, convite para retorno, programa de fidelização
- [ ] Verificar se existe base estruturada de clientes e comunicação futura

### Entrada Visual Obrigatória
- [ ] Construir Scorecard de Retenção por produto: Receita Recorrente (%) / Recompra (%) / Permanência Média / LTV / Observações

### Score da Trava 1
- [ ] Pontuar Dimensão A — Dados Estruturados de Retenção (0–5) + evidências ⚠️ *nota > 3 exige evidência formal*
- [ ] Pontuar Dimensão B — Receita Recorrente Relevante (0–5) + evidências
- [ ] Pontuar Dimensão C — Jornada Formal de Pós-Venda (0–5) + evidências
- [ ] Pontuar Dimensão D — Política Clara de Continuidade (0–5) + evidências
- [ ] Pontuar Dimensão E — Estratégia Ativa de Expansão (0–5) + evidências
- [ ] Calcular Total (0–25) e registrar faixa ⚠️ *consultar gabarito no arquivo de contexto*

### Consolidação Causal
- [ ] Formular: *"A empresa opera sob a política implícita de ___, gerando ___, limitando o crescimento cumulativo."*
- [ ] ⚠️ Evitar causas operacionais superficiais

### Determinação Preliminar
- [ ] Score <= 15? ⚠️
- [ ] LTV limita crescimento?
- [ ] Resolver retenção aumenta Throughput mais do que aquisição?
- [ ] Registrar: **Trava 1 é / não é potencial governante** — validação final na CRT

---

## Verificação Final
- [ ] Cohort construído (ou fragilidade registrada formalmente)
- [ ] LTV calculado e comparado com CAC
- [ ] Scorecard de Retenção por produto preenchido
- [ ] Score (0–25) calculado com evidências formais onde nota > 3
- [ ] Consolidação Causal formulada como política organizacional
- [ ] Determinação preliminar registrada
