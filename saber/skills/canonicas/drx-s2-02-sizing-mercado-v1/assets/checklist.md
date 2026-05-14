# Checklist: Sizing de Mercado (TAM / SAM / SOM)

**Objetivo:** Garantir que o dimensionamento de mercado seja executado com premissas explícitas, cálculos replicáveis e validação com o cliente.
**Responsável:** Consultor DR-X (execução pode ser apoiada pela skill de sizing)
**Frequência:** Uma vez por cliente — etapa de Pesquisa de Mercado do DR-X
**Tempo total estimado:** 45–60 minutos de trabalho; 20–30 min de validação com cliente

---

## Antes de Começar
- [ ] Descrição do produto/serviço analisado obtida
- [ ] Ticket médio atual ou projetado confirmado com o cliente
- [ ] **Tipo do ticket explícito:** por transação / por cliente-ano / por projeto ⚠️ *confundir esses tipos distorce o TAM em ordem de grandeza*
- [ ] Modelo de monetização definido (recorrente / transacional / híbrido)
- [ ] ICP preliminar identificado (segmento, porte, geografia)
- [ ] Restrições operacionais conhecidas (capacidade, ciclo de vendas)
- [ ] Horizonte estratégico definido (padrão: 12–36 meses)

---

## Execução

### 0. Gate de Pesquisa (BLOQUEANTE)
- [ ] WebSearch/WebFetch disponível na sessão? Se **NÃO**: parar, gerar `sizing-mercado-RESEARCH-BRIEF.md` e devolver ao consultor — **não calcular sizing**
- [ ] Para cada base populacional do TAM, executar busca e capturar: **número, ano-base, URL da fonte primária**
- [ ] ≥80% das bases têm fonte rastreável antes de prosseguir ⚠️ *abaixo disso, voltar a pesquisar*

### 1. Definição do Mercado Relevante
- [ ] Descrever o mercado com base no **problema resolvido** — não na categoria do produto
- [ ] Definir exclusões explícitas: quem NÃO faz parte do mercado ⚠️ *sem exclusões o TAM fica inflado*
- [ ] Registrar premissa de definição

### 2. Cálculo do TAM
- [ ] Escolher abordagem: bottom-up (preferencial) ou top-down
- [ ] **Bottom-up:** identificar nº de potenciais clientes × ticket médio (atenção ao **tipo** declarado)
- [ ] **Top-down:** localizar dado macro de mercado × ticket médio
- [ ] Cada linha da tabela de bases tem `Fonte: URL+ano` OU `[BLOQUEADO — sem fonte]` ⚠️ *proibido "estimativa setorial", "aproximação" ou similar*
- [ ] Se ticket veio ambíguo, calcular **TAM duplo** (otimista + conservador) e explicar a diferença
- [ ] Registrar premissas explicitamente (separadas das fontes) ⚠️ *cálculo sem fonte documentada não é aprovado*

### 3. Cálculo do SAM
- [ ] Aplicar filtro geográfico sobre o TAM
- [ ] Aplicar filtro de segmento (porte, nicho, maturidade)
- [ ] Aplicar filtro de aderência real à oferta atual
- [ ] Calcular valor do SAM com premissas documentadas

### 4. Cálculo do SOM
- [ ] Mapear restrições operacionais atuais do sistema
- [ ] Definir market share plausível para o horizonte estratégico ⚠️ *usar referência de mercado comparável se disponível*
- [ ] Calcular SOM = SAM × market share estimado
- [ ] Confrontar SOM com capacidade operacional real — o SOM deve ser menor que o limite do sistema

### 5. Validação com o Cliente
- [ ] Apresentar TAM, SAM e SOM com premissas explícitas
- [ ] Confirmar ticket médio utilizado
- [ ] Validar premissas de segmentação do SAM com o cliente
- [ ] Alinhar restrições operacionais para o SOM
- [ ] Ajustar premissas após validação se necessário
- [ ] Registrar aprendizados-chave e insights estratégicos

---

## Verificação Final
- [ ] TAM, SAM e SOM calculados com valores e metodologia documentados
- [ ] **Toda linha da tabela de bases tem `Fonte: URL+ano` ou `[BLOQUEADO]`** — zero ocorrências de "estimativa setorial" ou rótulos vagos
- [ ] Tipo do ticket está explícito no output (transação / cliente-ano / projeto)
- [ ] Todas as premissas explícitas e validadas com o cliente
- [ ] Coerência entre TAM > SAM > SOM verificada
- [ ] SOM alinhado às restrições reais do sistema
- [ ] Insights utilizáveis nas etapas seguintes do DR-X registrados
- [ ] Documento salvo e compartilhado com o cliente
