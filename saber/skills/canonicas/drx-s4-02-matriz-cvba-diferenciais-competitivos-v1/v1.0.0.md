---
slug: drx-s4-02-matriz-cvba-diferenciais-competitivos-v1
name: drx-s4-02-matriz-cvba-diferenciais-competitivos-v1
description: "Clarificar de forma objetiva por que o cliente deve escolher a empresa frente às alternativas disponíveis, identificando e organizando os diferenciais competitivos reais com base na Matriz CVB (Característica, Vantagem e Benefício perceb..."
---

# Diferenciais Competitivos / Matriz CVB

## Descrição
Clarificar de forma objetiva por que o cliente deve escolher a empresa frente às alternativas disponíveis, identificando e organizando os diferenciais competitivos reais com base na Matriz CVB (Característica, Vantagem e Benefício percebido).
Ativar quando posicionamento estratégico, matriz cvb, diferenciais competitivos, estudo de concorrentes, dr-x, pe&g for necessário.

## Quando Usar
- Trigger: "Posicionamento Estratégico", "Matriz CVB", "Diferenciais Competitivos", "Estudo de Concorrentes", "DR-X", "PE&G"
- NÃO usar quando: Qualidade da análise depende diretamente da profundidade do Estudo de Concorrentes e da Ficha de ICP — entradas incompletas comprometem todo o output; O passo de Reality Check exige julgamento estratégico contextualizado que a IA pode executar parcialmente, mas com risco de falsos positivos/negativos sem validação humana; A entrevista com o cliente (entrada crítica) é um dado qualitativo não estruturado, sujeito a interpretações divergentes; Diferenciais latentes ou não articulados pelo cliente podem ser subidentificados por agentes autônomos; A apresentação no comitê (passo 6) é uma interação humana insubstituível e de alto impacto estratégico
## Inputs Necessários
Solicitar antes de iniciar. Se faltar algum, perguntar antes de prosseguir:

1. **Master Contexto do cliente (context/business.md, context/gtm.md e context/constraints.md)**
2. **Estudo de Concorrentes concluído (output da skill de Estudo de Concorrentes — mapa de concorrentes, clusters, lacunas e oportunidades)**
3. **ICP definido (Ficha de ICP gerada no POP de Definição de ICPs)**
4. **Entrevista com o cliente (percepção de valor, dores, razões de escolha)**

## Processo de Execução

### 1. Identificar Alternativas de Escolha a partir do Estudo de Concorrentes, selecionando as alternativas que o cliente do negócio realmente considera ao tomar a decisão de compra. Registrar nome do concorrente/alternativa e categoria (direto, indireto, substituto).
- Ferramenta: *Mapa de concorrentes do Estudo de Concorrentes, Entrevista com o cliente, Deep research com IA*- Condicional: Se não houver concorrentes diretos identificáveis, usar o produto/serviço mais próximo que o público-alvo usaria como alternativa, incluindo 'não fazer nada' ou soluções internas improvisadas.
### 2. Levantar Atributos Comparáveis identificando os atributos que o cliente do negócio usa para comparar as opções. A lista é livre por segmento.

### 3. Construir a Matriz CVB preenchendo, para cada atributo relevante, a comparação do negócio do cliente com as alternativas identificadas, seguindo as colunas: Atributo, Característica (o que é), Vantagem (por que é melhor), Benefício (o que o cliente ganha).
- Ferramenta: *Matriz CVB*- Condicional: Característica é fato, não opinião; Vantagem é comparativa com referência a uma alternativa; Benefício é do ponto de vista do cliente, não do negócio; manter simples e direto sem escalas numéricas.
### 4. Reality Check dos Diferenciais revisando cada diferencial contra: sustentabilidade no médio prazo, capacidade de cópia, relevância para o ICP e entregabilidade. Descartar diferenciais que falham em 2 ou mais critérios registrando o motivo da exclusão.

### 5. Consolidar Diferenciais Reais selecionando os 3-5 diferenciais que passaram no reality check e classificando-os em: Diferencial de posicionamento, Diferencial de entrega ou Diferencial de percepção.

### 6. Apresentar no Comitê levando a Matriz CVB e os diferenciais consolidados para apresentação ao cliente. Os diferenciais validados alimentam a PUV e o discurso comercial.

## Formato de Saída
- Mapa das alternativas de escolha do cliente
- Matriz CVB preenchida com atributos comparados
- Lista de 3-5 diferenciais reais validados pelo reality check
- Base para posicionamento, PUV e discurso comercial

## Exceções e Fallbacks
- {'condicao': 'Mercado sem concorrentes públicos identificáveis', 'acao': "Expandir para substitutos e soluções adjacentes. Usar dados do Estudo de Concorrentes (seção 'Lacunas Identificadas') como referência."}
- {'condicao': 'Todos os diferenciais falham no reality check', 'acao': 'Registrar como achado estratégico crítico — o foco do DR-X deve migrar para construção de diferencial, não apenas comunicação.'}
- {'condicao': 'Diferencial existe mas o cliente não consegue articular', 'acao': "Registrar como 'diferencial latente' e incluir na PUV como oportunidade de comunicação."}
