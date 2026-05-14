---
slug: drx-s2-03-estudo-de-concorrentes-v1
name: drx-s2-03-estudo-de-concorrentes-v1
description: "Executa a análise competitiva completa para um negócio dentro do projeto DR-X. Mapeia concorrentes diretos, indiretos e substitutos, compara posicionamentos, identifica padrões de mercado, oportunidades de diferenciação e ameaças externa..."
---

# Estudo de Concorrentes DR-X

## Descrição
Executa a análise competitiva completa para um negócio dentro do projeto DR-X. Mapeia concorrentes diretos, indiretos e substitutos, compara posicionamentos, identifica padrões de mercado, oportunidades de diferenciação e ameaças externas, entregando documento estruturado pronto para validação com o cliente.

## Quando Usar
- Triggers: "estudo de concorrentes", "análise competitiva", "mapeamento de concorrentes", "benchmark de mercado", "quem são os concorrentes", "como estamos posicionados", "landscape competitivo"
- **NÃO usar quando:**
  1. O ICP preliminar não está definido — resolver o ICP antes de mapear concorrentes
  2. O produto/serviço analisado não está minimamente descrito — coletar esse dado antes
  3. O SOM ainda não foi calculado — a análise de concorrentes pressupõe mercado endereçável definido para o passo 6

## Inputs Necessários
Solicitar antes de iniciar. Se faltar algum, perguntar antes de prosseguir:

0. **Nome do consultor** — para identificação no documento de saída
1. **Descrição do produto/serviço** — qual problema resolve e para quem
2. **Lista inicial de concorrentes conhecidos** *(opcional — ver nota abaixo)* — mesmo que incompleta; ponto de partida para expansão
3. **ICP preliminar** — segmento, porte, geografia, características do cliente ideal
4. **SOM definido** — mercado endereçável calculado previamente (necessário para o passo 6)
5. **Fontes disponíveis** *(opcional)* — sites, materiais comerciais, redes sociais, reviews que o cliente já levantou

> **Nota — input 2 ausente:** Se a lista de concorrentes não foi coletada com o cliente (falha de coleta no kickoff), o skill executa via pesquisa autônoma (ver Fallback: Lista inicial vazia). O output será marcado como `DRAFT — PESQUISA AUTÔNOMA` e terá qualidade reduzida: concorrentes identificados pelo consultor podem não refletir quem o cliente realmente reconhece como ameaça. **A validação da lista com o cliente (passo 1) se torna obrigatória antes de qualquer uso estratégico do documento.**

---

## Processo de Execução

### 1. Mapeamento de Concorrentes
- A partir da lista inicial fornecida pelo cliente, expandir via pesquisa pública:
  - **Diretos:** mesmo problema, mesma solução
  - **Indiretos:** mesmo problema, solução diferente
  - **Substitutos:** formas alternativas de resolver o problema (incluindo "não fazer nada")
- **Pesquisa de fontes:** Utilizar busca web (sites, LinkedIn, G2, Capterra, Trustpilot, redes sociais, reviews) para identificar players não mencionados pelo cliente. Caso sem acesso web, informar limitação e solicitar fontes ao usuário.
- **Representantes e revendedores de grandes marcas:** Se o cliente for representante ou revendedor exclusivo/autorizado de uma marca, acessar o site oficial dessa marca e mapear outros representantes listados para o mesmo estado, região ou segmento de clientes. Esses players são concorrentes diretos no território e compartilham a mesma oferta de produto — a diferenciação entre eles ocorre exclusivamente em serviço, relacionamento e execução. Registrá-los como **Diretos — mesma marca** na tabela de concorrentes.
- Registrar para cada concorrente: nome, URL, categoria (direto/indireto/substituto)
- **Validação:** apresentar lista consolidada ao cliente antes de avançar para o passo 2. Não prosseguir sem confirmação.

### 2. Levantamento por Concorrente
Para cada concorrente mapeado, levantar com base em informações públicas:
- **Proposta de valor** — o que prometem e para quem
- **Público-alvo** — segmento, porte, geografia declarados
- **Modelo de monetização** — recorrente, transacional, freemium, etc.
- **Posicionamento de preço** — premium, mid-market, low-cost (referência relativa)
- **Principais promessas de marketing** — frases-chave, headlines, CTAs
- **Diferenciais declarados** — o que afirmam ser únicos
- **Evidências de autoridade** — cases, depoimentos, certificações, prêmios, volume de clientes
- **Precisão:** registrar apenas o que é verificável em fontes públicas. Marcar lacunas explicitamente com `[não encontrado]`.

### 3. Comparação e Clustering Estratégico
- Comparar todos os concorrentes considerando:
  - Clareza da proposta de valor (genérica vs. específica)
  - Nível de especialização por nicho
  - Maturidade da oferta (versão inicial vs. consolidada)
  - Complexidade percebida (simples vs. robusto/complexo)
  - Barreiras de entrada implícitas (preço, contrato, onboarding)
- **Identificar clusters estratégicos:** agrupar players com posicionamentos similares (ex: "low-cost generalista", "premium especializado", "DIY/self-service")
- Registrar em qual cluster o cliente se posiciona atualmente (mesmo que por default)

### 4. Padrões e Lacunas de Mercado
- Mapear **padrões recorrentes** entre os concorrentes:
  - Promessas comuns repetidas por múltiplos players
  - Modelos de entrega similares
  - Argumentos de venda padronizados (commoditizados)
- Identificar **lacunas** do mercado:
  - Dores pouco exploradas por qualquer player
  - Segmentos negligenciados ou mal atendidos
  - Excessos de complexidade que abrem espaço para simplificação
  - Comoditização de promessas que permite diferenciação por especificidade

### 5. Oportunidades e Ameaças
**Oportunidades — analisar:**
- Diferenciação clara de posicionamento frente aos clusters identificados
- Simplificação da oferta onde o mercado é percebido como complexo
- Foco em throughput do cliente (resultado mensurável que nenhum concorrente entrega explicitamente)
- Exploração de restrições ignoradas pelo mercado (TOC aplicado ao cliente, não ao produto)

**Ameaças — analisar:**
- Concorrentes altamente capitalizados com capacidade de escalar rapidamente
- Ofertas substitutas de baixo custo que sufocam a percepção de valor
- Barreiras regulatórias ou tecnológicas que favorecem players incumbentes
- Dinâmica de guerra de preços no segmento

### 6. Consolidação Estratégica
- Consolidar os **3–5 aprendizados-chave** da análise (o que muda a visão estratégica do negócio)
- Relacionar achados com o SOM definido: qual fatia está mais disputada? Qual está subatendida?
- Traduzir insights em **hipóteses estratégicas** para as próximas etapas do DR-X:
  - Hipótese de posicionamento (onde competir)
  - Hipótese de diferenciação (como ganhar)
  - Hipótese de restrição (o que pode bloquear o crescimento)

---

## Formato de Saída

```markdown
## Estudo de Concorrentes — [Nome do Cliente]
**Data:** [data] | **Consultor:** [nome do consultor informado]

---

### Mapa de Concorrentes

| Concorrente | Categoria | URL | Proposta de Valor | Público-Alvo | Preço | Diferenciais Declarados | Autoridade |
|-------------|-----------|-----|-------------------|--------------|-------|-------------------------|------------|
| [nome]      | Direto    | [url] | [resumo]        | [segmento]   | [ref] | [lista]                 | [evidências] |
| [nome]      | Indireto  | [url] | [resumo]        | [segmento]   | [ref] | [lista]                 | [evidências] |
| [nome]      | Substituto| [url] | [resumo]        | [segmento]   | [ref] | [lista]                 | [evidências] |

---

### Clusters Estratégicos do Mercado

**Cluster [nome]:** [players] — [descrição do posicionamento comum]
**Cluster [nome]:** [players] — [descrição do posicionamento comum]

**Posicionamento atual do cliente:** [cluster em que se encontra] — [avaliação]

---

### Padrões de Mercado

**Promessas commoditizadas (todos falam):**
- [promessa 1]
- [promessa 2]

**Modelos de entrega predominantes:**
- [modelo 1]
- [modelo 2]

**Argumentos repetidos (ruído):**
- [argumento 1]

---

### Lacunas Identificadas

**Dores pouco exploradas:**
- [dor 1]
- [dor 2]

**Segmentos negligenciados:**
- [segmento 1]

**Oportunidades de simplificação:**
- [oportunidade 1]

---

### Oportunidades Estratégicas

1. [oportunidade com justificativa]
2. [oportunidade com justificativa]
3. [oportunidade com justificativa]

### Ameaças Externas

1. [ameaça com justificativa]
2. [ameaça com justificativa]

---

### Aprendizados-Chave

1. [aprendizado que muda a perspectiva estratégica]
2. [aprendizado que muda a perspectiva estratégica]
3. [aprendizado que muda a perspectiva estratégica]

---

### Hipóteses Estratégicas para as Próximas Etapas

- **Onde competir (posicionamento):** [hipótese]
- **Como ganhar (diferenciação):** [hipótese]
- **O que pode bloquear (restrição):** [hipótese]

---

### Relação com o SOM

**Fatia mais disputada:** [segmento/cluster]
**Fatia subatendida:** [segmento/cluster]
**Implicação para o SOM:** [o que isso significa para o mercado capturável]

---

### Validação Necessária com o Cliente

- [ ] Confirmar lista final de concorrentes (passo 1 — obrigatório antes de avançar)
- [ ] Validar posicionamento de preço relativo atribuído a cada player
- [ ] Confirmar em qual cluster o cliente se reconhece
- [ ] Priorizar quais hipóteses estratégicas serão testadas nas próximas etapas
```

---

## Exceções e Fallbacks
- **Concorrente com informações públicas insuficientes:** registrar `[não encontrado]` nos campos em branco, documentar limitação no output, não assumir dados não verificáveis
- **Lista inicial vazia (falha de coleta no kickoff):** conduzir pesquisa autônoma com base no ICP, segmento e problema resolvido. Marcar o output com `DRAFT — PESQUISA AUTÔNOMA`. Incluir aviso explícito no documento: *"Lista de concorrentes não foi coletada com o cliente — pesquisa realizada autonomamente. Valide a lista antes de usar este documento para decisões estratégicas."* A validação no passo 1 continua obrigatória antes de qualquer uso do output.
- **Cliente recusa validação no passo 1:** registrar como bloqueio explícito; não avançar para os passos seguintes sem confirmação — documentar no output com status `BLOQUEADO: aguardando validação da lista`
- **Mercado muito nichado com poucos concorrentes públicos:** expandir para substitutos e soluções adjacentes; registrar como ressalva que o mercado pode ter baixa maturidade ou ser muito fragmentado
- **SOM não disponível para o passo 6:** realizar a análise até o passo 5 e sinalizar que o passo 6 (consolidação estratégica) está incompleto — `PENDENTE: aguardando SOM`

---

**Salvar em:** `clientes/[nome-cliente]/produtos/[produto-ativo]/estudo-concorrentes.md`
- Se o diretório não existir, criá-lo.
- Se não tiver permissão de escrita, exibir o conteúdo no chat para o consultor salvar manualmente.

**Registrar em `produtos/[produto-ativo]/changelog.md`:**
Adicionar entry com: data de validação, status `✅ VALIDADO`, e 3–5 insights principais do output.
