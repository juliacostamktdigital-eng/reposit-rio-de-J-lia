---
slug: drx-s2-02-sizing-mercado-v1
name: drx-s2-02-sizing-mercado-v1
description: "Executa o dimensionamento de mercado completo (TAM, SAM e SOM) para um negócio dentro do projeto DR-X. Pesquisa dados de mercado, calcula os três níveis com premissas explícitas e entrega documento estruturado pronto para validação com o..."
---

# Sizing de Mercado DR-X (TAM / SAM / SOM)

## Descrição
Executa o dimensionamento de mercado completo (TAM, SAM e SOM) para um negócio dentro do projeto DR-X. Pesquisa dados de mercado, calcula os três níveis com premissas explícitas e entrega documento estruturado pronto para validação com o cliente.

## Quando Usar
- Triggers: "sizing de mercado", "calcular TAM", "dimensionar mercado", "TAM SAM SOM", "quanto vale esse mercado"
- **NÃO usar quando:**
  1. O cliente já tem sizing recente validado — usar como revisão crítica, não recálculo completo
  2. O ICP do cliente não está definido — resolver o ICP antes de calcular SAM/SOM
  3. Não há ticket médio disponível nem estimável — coletar esse dado antes de qualquer cálculo

## Inputs Necessários
Solicitar antes de iniciar. Se faltar algum, perguntar antes de prosseguir:

0. **Nome do consultor** — para identificação no documento de saída
1. **Descrição do produto/serviço** — qual problema resolve e para quem
2. **Ticket médio + tipo do ticket** (input duplo, obrigatório):
   - Valor declarado em R$
   - **Tipo:** (a) **por transação** (uma venda fechada), (b) **por cliente-ano** (receita média anual de um cliente ativo, somando recompras), ou (c) **por projeto/contrato** (escopo fechado, pode envolver múltiplas transações).
   - ⚠️ Se o consultor não souber distinguir, **NÃO assumir** — perguntar com exemplos do negócio. Confundir esses tipos distorce o TAM em ordem de grandeza. Se o input vier ambíguo, calcular **dois TAMs** (otimista e conservador) explicitando a diferença no output.
3. **Modelo de monetização** — recorrente, transacional ou híbrido
4. **ICP preliminar** — segmento, porte, geografia, características do cliente ideal
5. **Restrições operacionais** — capacidade atual, ciclo de vendas, limitações conhecidas
6. **Horizonte estratégico** — prazo para o SOM (padrão: **24 meses** se não informado)

---

## Processo de Execução

### 0. Gate de Pesquisa (BLOQUEANTE — antes de qualquer cálculo)

**Esta fase é portão de entrada. Não prosseguir para a fase 1 sem cumpri-la.**

- **Verificar disponibilidade de WebSearch/WebFetch.** Se as ferramentas web NÃO estiverem disponíveis na sessão atual:
  - **NÃO gerar sizing.** Em vez disso, gerar `sizing-mercado-RESEARCH-BRIEF.md` com: (i) lista das bases populacionais que precisam ser buscadas, (ii) fontes-alvo sugeridas (IBGE, associações setoriais, relatórios públicos), (iii) perguntas específicas a responder, (iv) ticket médio que será usado depois.
  - Devolver ao consultor com instrução: *"Web indisponível nesta sessão. Reabrir a skill com web habilitada ou colar os dados pesquisados no brief para que o cálculo seja feito."*
  - **PARAR aqui.** Não calcular TAM/SAM/SOM com chutes.
- **Se web estiver disponível:** executar WebSearch/WebFetch para **cada base populacional crítica** que entrará no TAM (ex: nº de supermercados no Brasil, nº de farmácias, etc.). Capturar para cada uma: **número, ano-base, URL da fonte primária**.
- **Critério de aprovação para sair desta fase:** ≥80% das bases populacionais usadas no TAM têm fonte rastreável (URL + ano). Se ficar abaixo disso, voltar a buscar — não passar para o cálculo.

### 1. Definição do Mercado Relevante
- Descrever o mercado com base no **problema resolvido** (não na categoria do produto)
- Definir exclusões explícitas: quem NÃO faz parte do mercado
- Registrar premissa de definição

### 2. Cálculo do TAM
- Identificar base total de clientes potenciais que têm o problema (usar números coletados na **Fase 0**)
- **Abordagem preferencial (bottom-up):** nº de potenciais clientes × ticket médio (atenção ao **tipo** declarado no input 2 — por transação vs cliente-ano vs projeto)
- **Abordagem alternativa (top-down):** receita total do mercado × taxa de penetração estimada
- **Precisão Matemática:** Mostre o raciocínio matemático explícito no rascunho (ex: 50.000 clientes × R$ 1.200/ano = R$ 60.000.000) para garantir a exatidão antes de preencher o formato final.
- **Regra de fontes (HARD):** Cada linha da tabela de base de cálculo deve preencher a coluna `Fonte` com **URL + ano-base** OU com o marcador `[BLOQUEADO — sem fonte]`. **Proibido** usar rótulos vagos como "estimativa setorial", "aproximação", "estimativa pública". Se aparecer `[BLOQUEADO]` em qualquer linha crítica, voltar à Fase 0 e completar a pesquisa antes de finalizar o output.
- Documentar todas as premissas utilizadas (separadas das fontes)
- **Sanity Check:** Se TAM > R$10bi, questionar se a definição de mercado não está ampla demais antes de prosseguir. Registrar no output com nota.

### 3. Cálculo do SAM
- Aplicar filtros sobre o TAM usando a fórmula:
  - `SAM = TAM × %_geografia × %_segmento × %_aderência_oferta`
  - Exemplo: `R$60M × 40% (SP/MG) × 30% (porte aderente) × 70% (oferta cobre) = R$5,04M`
- Filtros a considerar:
  - Geografia (onde o cliente atua ou consegue atuar)
  - Segmento (porte, nicho, maturidade que aderem ao produto)
  - Aderência real à oferta atual
- Excluir segmentos não atendidos pela oferta atual

### 4. Cálculo do SOM
- Analisar restrições reais do sistema:
  - Capacidade operacional atual
  - Modelo comercial e ciclo de vendas
  - Concorrência e share estimado
- Definir market share plausível para o horizonte informado
- Calcular `SOM = SAM × market share estimado`
- Registrar como premissa simplificadora: o modelo assume market share constante no horizonte — ajustar se o crescimento for em rampas.

### 5. Validação TOC (Teoria das Restrições)
Responda cada pergunta abaixo com base nos dados calculados e inclua as respostas na seção TOC do documento de saída:
- "Se capturássemos 100% desse SOM, o sistema atual suportaria?"
- "O crescimento é limitado por demanda ou por capacidade operacional?"
- "Qual é a maior alavanca de throughput disponível?"

---

## Formato de Saída

```markdown
## Sizing de Mercado — [Nome do Cliente]
**Data:** [data] | **Consultor:** [nome do consultor informado] | **Horizonte:** [prazo]

### Definição do Mercado
[Descrição do mercado com base no problema resolvido]
**Exclusões:** [quem não faz parte]

### TAM — Total Addressable Market
**Valor:** R$ [X] / ano
**Metodologia:** [bottom-up / top-down]
**Tipo de ticket usado:** [por transação / por cliente-ano / por projeto] — R$ [valor]

**Bases populacionais (cada linha exige fonte rastreável):**

| Base | Volume | Fonte (URL + ano-base) |
|---|---|---|
| [ex: Supermercados Brasil] | [nº] | [https://... — 2024] |
| ... | ... | ... |

> Marcadores aceitos na coluna Fonte: URL+ano OU `[BLOQUEADO — sem fonte]`. **Proibido** "estimativa setorial" ou similar. Se houver `[BLOQUEADO]`, voltar à Fase 0.

**Cálculo explícito:** [nº potenciais clientes] × R$ [ticket] = R$ [resultado]
**Premissas (separadas das fontes):** [listar premissas de cálculo, filtros, conversões]
**Sanity check:** [ok / atenção — definição de mercado pode estar ampla demais: justificar]
**TAM duplo (se ticket veio ambíguo):** otimista R$ [X] · conservador R$ [Y] — explicar diferença

### SAM — Serviceable Available Market
**Valor:** R$ [X] / ano ([Y]% do TAM)
**Base de cálculo:** R$ [TAM] × [%geo] × [%segmento] × [%aderência] = R$ [resultado]
**Filtros aplicados:** [geografia, segmento, aderência]
**Premissas:** [listar]

### SOM — Serviceable Obtainable Market
**Valor:** R$ [X] / ano ([Y]% do SAM)
**Market share assumido:** [Z]% em [prazo]
**Restrições consideradas:** [listar]
**Premissas:** [listar]
*Nota: modelo assume market share constante no horizonte — ajustar se crescimento for em rampas.*

### Restrição Principal (TOC)
- **O sistema suporta 100% do SOM?** [Sim / Não — justificar brevemente]
- **Crescimento limitado por:** [Demanda / Capacidade / Ambos — justificar]
- **Maior alavanca de throughput:** [identificar a principal]

### Insights Estratégicos
- **Concentração de valor:** [Onde está a maior densidade de valor no SAM? Segmento ou geografia com maior ticket × volume]
- **Restrição ao crescimento:** [Qual restrição (TOC) mais limita a captura do SOM no horizonte definido?]
- **Prioridade de ação:** [Qual ação expande o SOM sem aumentar a restrição principal?]

### Validação Necessária com o Cliente
- [ ] Confirmar ticket médio utilizado
- [ ] Validar premissas de segmentação do SAM
- [ ] Alinhar restrições operacionais para o SOM
```

---

## Exceções e Fallbacks
- **Web indisponível na sessão:** **NÃO gerar sizing.** Gerar `sizing-mercado-RESEARCH-BRIEF.md` (estrutura na Fase 0) e parar. Proibido produzir TAM/SAM/SOM com números sem fonte rastreável.
- **Web disponível mas fonte não encontrada para uma base específica:** marcar a linha como `[BLOQUEADO — sem fonte]` e sinalizar no topo do output como pendência. Se >20% das bases ficarem bloqueadas, escalar para o consultor antes de finalizar.
- **Sem ticket médio fornecido:** perguntar antes de calcular — não assumir valor.
- **Ticket fornecido sem o tipo (transação / cliente-ano / projeto):** perguntar com exemplos do negócio. Se mesmo assim ficar ambíguo, calcular TAM duplo (otimista e conservador) explicitando a diferença.
- **Sem ICP definido:** registrar como fragilidade e calcular TAM amplo com ressalva de que SAM/SOM dependerão da definição do ICP.
- **Mercado muito nichado:** buscar proxy de mercado (categoria mais ampla × fator de penetração) — proxy também precisa de fonte rastreável.
- **TAM implausível (> R$10bi para negócio de nicho):** sinalizar no output e sugerir redefinição do mercado antes de apresentar ao cliente.

---

**Salvar em:** `clientes/[nome-cliente]/produtos/[produto-ativo]/sizing-mercado.md`
- Se o diretório não existir, criá-lo.
- Se não tiver permissão de escrita, exibir o conteúdo no chat para o consultor salvar manualmente.

**Registrar em `produtos/[produto-ativo]/changelog.md`:**
Adicionar entry com: data de validação, status `✅ VALIDADO`, e 3–5 insights principais do output.
