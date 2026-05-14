---
slug: drx-s4-01-analise-swot-v1
name: drx-s4-01-analise-swot-v1
description: "Organizar de forma estruturada as Forças, Fraquezas, Oportunidades e Ameaças do negócio, com o objetivo de suportar decisões estratégicas, priorização de iniciativas e definição de foco, evitando análises genéricas ou desconectadas da re..."
---

# Análise SWOT

## Descrição
Organizar de forma estruturada as Forças, Fraquezas, Oportunidades e Ameaças do negócio, com o objetivo de suportar decisões estratégicas, priorização de iniciativas e definição de foco, evitando análises genéricas ou desconectadas da realidade operacional.
Ativar quando estratégia, posicionamento, análise, swot, diagnóstico, decisão estratégica for necessário.

## Quando Usar
- Trigger: "estratégia", "posicionamento", "análise", "SWOT", "diagnóstico", "decisão estratégica"
- NÃO usar quando: Análise SWOT pode ser superficial ou genérica se os artefatos de entrada estiverem incompletos ou desatualizados; Ausência de ferramenta definida para qualquer passo aumenta o risco de inconsistência na execução entre consultores diferentes; A consolidação estratégica (passo 7) depende fortemente de julgamento interpretativo, o que limita a automação e eleva o risco de viés analítico; A apresentação no comitê (passo 8) não possui critérios de aprovação ou próximos passos definidos, criando ambiguidade sobre o encerramento do processo
## Inputs Necessários
Solicitar antes de iniciar. Se faltar algum, perguntar antes de prosseguir:

1. **Master Contexto do cliente (context/business.md, context/gtm.md e context/constraints.md)**
2. **Diagnósticos de travas do sistema (outputs das travas 1-7)**
3. **LTP (Logical Thinking Process) realizada — CRT concluída**
4. **Análise de mercado — Sizing de mercado (TAM/SAM/SOM)**
5. **Estudo de Concorrentes concluído (output da skill de Estudo de Concorrentes)**

## Processo de Execução

### 1. Reunir insumos - Consolidar os artefatos de entrada (diagnósticos, LTP, análise de mercado, benchmarking) em um local acessível para consulta durante o preenchimento.

### 2. Mapear Forças (Ambiente Interno) - Listar fatores internos favoráveis ao negócio, respondendo: O que o negócio faz melhor que a média? Onde há vantagem clara e comprovada? Quais forças sustentam resultados atuais? Foco: diferenciais competitivos claros, eficiência operacional, know-how do time, ativos estratégicos (marca, base, tecnologia).

### 3. Mapear Fraquezas (Ambiente Interno) - Listar limitações estruturais, gargalos e vulnerabilidades internas, respondendo: O que limita o crescimento hoje? Onde o sistema falha de forma recorrente? Quais fragilidades expõem riscos? Foco: dependência de pessoas-chave, processos frágeis, baixa maturidade digital, falta de previsibilidade.

### 4. Mapear Oportunidades (Ambiente Externo) - Listar fatores externos exploráveis para crescimento, respondendo: Onde o mercado está se abrindo? Quais movimentos externos favorecem o negócio? As oportunidades são reais ou hipotéticas? Foco: tendências de mercado, mudanças regulatórias favoráveis, lacunas de concorrentes, evolução de comportamento do cliente.

### 5. Mapear Ameaças (Ambiente Externo) - Listar fatores externos de risco, respondendo: O que pode reduzir margem ou demanda? Onde o negócio está vulnerável externamente? As ameaças são iminentes ou potenciais? Foco: concorrência mais estruturada, mudanças regulatórias restritivas, dependência de canais terceiros, commoditização.

### 6. Aplicar Regras de Qualidade - Revisar todos os quadrantes verificando: Nenhuma fraqueza interna foi confundida com ameaça externa; Nenhum desejo foi listado como força; Nenhuma oportunidade foi listada sem capacidade interna mínima; Todos os itens são específicos, baseados em evidência e relevantes para decisão; Prioridade é impacto estratégico, não quantidade de itens.

### 7. Consolidação Estratégica - Responder obrigatoriamente: Quais forças devem ser protegidas e exploradas? Quais fraquezas exigem ação imediata? Quais oportunidades são coerentes com a maturidade atual? Quais ameaças exigem mitigação ou mudança de rota? Esta consolidação é a ponte para a definição de foco estratégico e priorização de injeções.

### 8. Apresentar no Comitê - Levar a matriz SWOT finalizada e a consolidação estratégica para o próximo comitê com o cliente.

## Formato de Saída
- Matriz SWOT estruturada e justificada
- Consolidação estratégica com decisões claras por quadrante
- Base sólida para decisões de posicionamento
- Insumo para priorização de injeções

## Exceções e Fallbacks
- Se o cliente não possui histórico suficiente para algum quadrante (ex: empresa nova sem ameaças concretas): registrar como "insuficiente para análise" e basear-se nas evidências disponíveis da análise de mercado e benchmarking.
- Se houver divergência entre os dados do diagnóstico e a percepção do cliente: prevalecem os dados do diagnóstico; a divergência deve ser registrada e discutida no comitê.
