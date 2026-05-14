---
slug: drx-s4-04-icp-ideal-customer-profile-v1
name: drx-s4-04-icp-ideal-customer-profile-v1
description: "Identifica e define o perfil de cliente ideal do negócio dentro do projeto DR-X. Analisa dados de clientes existentes, identifica padrões, avalia aderência à oferta e esforço operacional, e entrega uma Ficha de ICP estruturada pronta par..."
---

# Definição de ICPs (Ideal Customer Profile)

## Descrição
Identifica e define o perfil de cliente ideal do negócio dentro do projeto DR-X. Analisa dados de clientes existentes, identifica padrões, avalia aderência à oferta e esforço operacional, e entrega uma Ficha de ICP estruturada pronta para validação com o cliente.
Ativar quando posicionamento, segmentação, ICP, perfil de cliente, qualificação for necessário.

## Quando Usar
- Triggers: "definir ICP", "perfil de cliente ideal", "ideal customer profile", "para quem vender", "segmentar clientes", "qualificação de leads"
- **NÃO usar quando:**
  1. Os arquivos context/ não existem ou não estão `[VALIDADO]` — sem contexto base não há como analisar clientes
  2. Não há acesso a nenhum dado do cliente (CRM, planilhas, entrevistas) — sem dados, o ICP é pura especulação

## Inputs Necessários
Solicitar antes de iniciar. Se faltar algum, perguntar antes de prosseguir:

1. **context/business.md** + **context/gtm.md** + **context/constraints.md** `[VALIDADO]` — visão geral do negócio, produto, modelo de monetização, ICP preliminar (se houver)
2. **Acesso ao CRM do cliente** — dados de clientes existentes (se disponível)
3. **Planilhas e dados financeiros** — faturamento, margem, LTV por cliente (se disponível)
4. **Sizing de mercado** — output da skill-sizing-mercado (TAM/SAM/SOM) para dimensionar o ICP no mercado
5. **Estudo de Concorrentes** — output da skill-estudo-de-concorrentes (segmentos negligenciados, clusters de mercado)

> **Se negócio novo sem clientes:** substituir inputs 2-3 por pesquisa de mercado, benchmarking e entrevistas com potenciais clientes. Marcar o ICP como `HIPOTÉTICO — REVISAR APÓS 3-6 MESES`.

---

## Processo de Execução

### 1. Análise de Clientes Existentes
Levantar dados dos clientes atuais a partir de CRM, planilhas, entrevistas e pesquisa.

**Critérios para identificar os melhores clientes:**
- Maior LTV ou margem de contribuição
- Maior tempo de permanência
- Menor volume de suporte ou esforço operacional
- Maior ticket médio
- Maior recorrência de compra

**Perguntas-chave:**
- Quais clientes permanecem mais tempo?
- Onde o esforço operacional é menor?
- Quais clientes têm maior margem ou LTV?

**Fonte:** CRM, planilhas financeiras, entrevistas com time comercial e dono do negócio.

> **Fallback — negócio novo:** Usar dados do Sizing (SAM/SOM) para identificar segmentos com maior potencial. Complementar com benchmarking do Estudo de Concorrentes (quem os concorrentes atendem e onde há lacunas). Conduzir entrevistas com potenciais clientes para validar hipóteses.

### 2. Identificação de Padrões Comuns
Analisar qualitativamente os melhores clientes e identificar o que eles têm em comum:

**O que buscar:**
- Segmento ou porte (B2B) / faixa de ticket ou comportamento (B2C)
- Maturidade do problema que o negócio resolve
- Capacidade de execução e decisão
- Recorrência e sensibilidade a preço

Agrupar os padrões por frequência de aparição. O foco é encontrar similaridades relevantes, não coincidências superficiais.

### 3. Avaliação de Aderência à Oferta
Cruzar os padrões com a proposta de valor do negócio:
- O cliente entende rapidamente a PUV?
- O valor é percebido cedo no relacionamento?
- O cliente precisa de muita adaptação ou customização?

**Regra:** Perfis que exigem customização excessiva raramente são bons ICPs.

### 4. Análise de Esforço Operacional
Avaliar o custo operacional de atender cada perfil:
- O cliente exige suporte intenso?
- Há dependência de pessoas específicas para atendê-lo?
- O atendimento escala ou colapsa com volume?

**ICP não é só valor gerado — é valor gerado por unidade de esforço.**

### 5. Consolidação do ICP Prioritário
Preencher a Ficha de ICP:

| Campo | Descrição |
|---|---|
| **Nome do ICP** | Rótulo descritivo (ex: "PME de serviços B2B com 10-50 funcionários") |
| **Características estruturais** | Porte, segmento, maturidade, localização |
| **Problema central** | Qual dor esse perfil tem que o negócio resolve |
| **Comportamento de compra** | Como compra, ciclo de decisão, sensibilidade a preço |
| **Valor gerado** | LTV estimado, margem, recorrência |
| **Esforço operacional** | Nível de suporte, complexidade de atendimento |
| **Critérios de inclusão** | O que define que um lead é ICP |
| **Critérios de exclusão** | O que desqualifica um lead |

**O resultado deve ser UM ICP prioritário**, não uma lista extensa.

### 6. Diferenciação B2B vs B2C
Ajustar a ficha conforme o modelo de negócio:

**Se B2B:**
- Detalhar porte, segmento, maturidade e estrutura decisória
- Diferenciar usuário, decisor e comprador
- Avaliar capacidade de execução e autonomia de decisão

**Se B2C:**
- Focar em comportamento, momento de vida e contexto de uso
- Avaliar recorrência e sensibilidade a preço
- Não basear ICP apenas em demografia

**Se modelo misto:** criar ficha separada para cada modelo, priorizando o que representa maior volume ou valor.

### 7. Apresentação e Validação
Apresentar o ICP ao cliente em reunião. Coletar feedback, registrar ajustes e revisar a ficha.

**Após validação, o ICP alimenta diretamente:**
- skill-definicao-de-puv (público-alvo da PUV)
- skill-diferenciais-competitivos-matriz-cvb (relevância dos diferenciais para o ICP)
- skill-fluxo-de-estrategia (critérios de aquisição alinhados ao ICP)

---

## Formato de Saída

```markdown
## Ficha de ICP — [Nome do Cliente]
**Data:** [data] | **Consultor:** [nome]
**Status:** [VALIDADO] / [DRAFT — HIPOTÉTICO] / [PENDENTE VALIDAÇÃO CLIENTE]

### ICP Prioritário
**Nome:** [rótulo descritivo]

| Campo | Descrição |
|---|---|
| Características estruturais | [porte, segmento, maturidade, localização] |
| Problema central | [dor que o negócio resolve] |
| Comportamento de compra | [ciclo, decisores, sensibilidade a preço] |
| Valor gerado | [LTV, margem, recorrência] |
| Esforço operacional | [suporte, complexidade, escalabilidade] |
| Critérios de inclusão | [o que qualifica como ICP] |
| Critérios de exclusão | [o que desqualifica] |

### Modelo de Negócio
**Tipo:** [B2B / B2C / Misto]
[Detalhamento conforme passo 6]

### Fontes de Dados Utilizadas
- [CRM / Planilha / Entrevista / Pesquisa / Benchmarking]

### Conexões com Artefatos DR-X
- Sizing: [relação com SAM/SOM]
- Concorrentes: [segmentos identificados]
- Master-contexto: [ICP preliminar vs. ICP definido — o que mudou]
```

---

## Exceções e Fallbacks
- **Negócio novo sem clientes:** construir ICP hipotético baseado em pesquisa de mercado e benchmarking. Marcar como `DRAFT — HIPOTÉTICO`. Agendar revisão após 3-6 meses com dados reais.
- **Dados insuficientes no CRM:** complementar com entrevistas diretas ao time comercial e ao dono do negócio. Registrar quais dados estão faltando.
- **Empate entre perfis:** priorizar o perfil com menor esforço operacional. Se persistir empate, escolher o que tem maior potencial de escala.
- **Cliente recusa validação do ICP:** registrar objeções específicas. Não avançar para PUV sem ICP minimamente validado — registrar como bloqueio.
