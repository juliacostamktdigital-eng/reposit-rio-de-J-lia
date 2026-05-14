---
slug: drx-s4-05-fluxo-de-estrategia-v1
name: drx-s4-05-fluxo-de-estrategia-v1
description: "Define a lógica sistêmica de crescimento do negócio ao longo da jornada do cliente dentro do projeto DR-X. Organiza as estratégias de aquisição, engajamento, monetização e retenção de forma integrada, cruzando cada macroetapa com as trav..."
---

# Fluxo de Estratégia de Crescimento (Aquisição, Engajamento, Monetização, Retenção)

## Descrição
Define a lógica sistêmica de crescimento do negócio ao longo da jornada do cliente dentro do projeto DR-X. Organiza as estratégias de aquisição, engajamento, monetização e retenção de forma integrada, cruzando cada macroetapa com as travas diagnosticadas para garantir coerência entre posicionamento e capacidade operacional.
Ativar quando estratégia de crescimento, fluxo de receita, jornada do cliente, aquisição, engajamento, monetização, retenção for necessário.

## Quando Usar
- Triggers: "fluxo de estratégia", "estratégia de crescimento", "como vamos crescer", "aquisição e retenção", "jornada do cliente estratégica", "playbook de crescimento"
- **NÃO usar quando:**
  1. O ICP não está definido — sem ICP, aquisição e engajamento ficam genéricos
  2. A PUV não está definida — sem PUV, o engajamento não tem mensagem central
  3. O diagnóstico de travas não foi concluído — o fluxo precisa ser cruzado com as travas

## Inputs Necessários
Solicitar antes de iniciar. Se faltar algum, perguntar antes de prosseguir:

1. **context/business.md** + **context/gtm.md** + **context/constraints.md** `[VALIDADO]` — visão geral do negócio, modelo de monetização, canais atuais
2. **Diagnóstico de travas 1-7** — contextos e checklists das travas (para cruzar com cada macroetapa)
3. **Ficha de ICP** — output da skill-definicao-de-icps (quem adquirir e como qualificar)
4. **PUV definida** — output da skill-definicao-de-puv (mensagem central para engajamento)
5. **Matriz CVB** — output da skill-diferenciais-competitivos-matriz-cvb (diferenciais para comunicação)
6. **Estudo de Concorrentes** — output da skill-estudo-de-concorrentes (landscape, clusters, lacunas)

---

## Processo de Execução

### 1. Definir Estratégia de Aquisição
Definir como atrair clientes alinhados ao ICP, em volume e qualidade compatíveis com a capacidade do sistema.

**Documentar:**
- Canais prioritários de aquisição e papel de cada canal
- Critérios mínimos de entrada (o que qualifica um lead como potencial)
- Estimativa de volume que o sistema absorve

**Perguntas-chave:**
- Onde o ICP pode ser encontrado? (usar Estudo de Concorrentes — segmentos negligenciados)
- A aquisição é previsível ou oportunista?
- O volume gerado é absorvível pelo sistema?

**Cruzar com travas:** Verificar diagnóstico da **Trava 7 (Exposição)** e **Trava 6 (Atenção)**.
- Se Trava 7 é crítica: aquisição tem problema de alcance — priorizar visibilidade
- Se Trava 6 é crítica: aquisição atinge mas não captura — priorizar mensagem

> Aquisição sem critério gera gargalos nas travas seguintes.

### 2. Definir Estratégia de Engajamento
Definir como converter atenção inicial em envolvimento ativo com a proposta de valor.

**Documentar:**
- Conteúdos e interações-chave por estágio do funil
- Pontos de aprofundamento e gatilhos de progressão
- Onde o engajamento se perde (pontos de fuga)

**Perguntas-chave:**
- O cliente entende rapidamente a PUV? (usar output da skill-definicao-de-puv)
- Existe progressão clara de interesse?
- Onde o engajamento se perde?

**Cruzar com travas:** Verificar diagnóstico da **Trava 5 (Interesse)** e **Trava 4 (Qualificação)**.

> Engajamento fraco indica falha de mensagem ou valor percebido.

### 3. Definir Estratégia de Monetização
Definir como transformar engajamento em receita, de forma clara e previsível.

**Documentar:**
- Arquitetura de oferta (produtos, pacotes, tiers)
- Modelo de precificação e lógica de valor (usar Matriz CVB — benefício percebido)
- Momentos de pedido de decisão (quando e como pedir a compra)

**Perguntas-chave:**
- O valor é percebido antes do preço?
- O pedido de compra é claro?
- O sistema sustenta o modelo de monetização?

**Cruzar com travas:** Verificar diagnóstico da **Trava 3 (Compromisso)** e **Trava 2 (Decisão)**.

> Monetização sem clareza gera fricção e perda de decisão.

### 4. Definir Estratégia de Retenção
Definir como sustentar geração de valor após a compra.

**Documentar:**
- Critério de sucesso do cliente (o que significa "dar certo")
- Estratégia de ativação e acompanhamento pós-venda
- Sinais de risco de churn e plano de reação

**Perguntas-chave:**
- O cliente gera valor de forma recorrente?
- O sistema detecta churn antecipadamente?
- Existe evolução do relacionamento?

**Cruzar com travas:** Verificar diagnóstico da **Trava 1 (Retenção)**.

> Retenção fraca transforma crescimento em ilusão.

### 5. Integrar Fluxo com Mapa de Travas
Montar tabela de integração:

| Macroetapa | Travas | Estratégia endereça a restrição? | Ajuste necessário |
|---|---|---|---|
| Aquisição | Trava 7 + Trava 6 | [sim/não] | [se não, o que falta] |
| Engajamento | Trava 5 + Trava 4 | [sim/não] | [se não, o que falta] |
| Monetização | Trava 3 + Trava 2 | [sim/não] | [se não, o que falta] |
| Retenção | Trava 1 | [sim/não] | [se não, o que falta] |

Se alguma linha tiver "não", ajustar a estratégia antes de consolidar.

### 6. Consolidar e Validar — Checklist de Conclusão
O fluxo está pronto quando:

- [ ] Cada macroetapa tem canais, ações e critérios definidos (não apenas descrição conceitual)
- [ ] Toda macroetapa está conectada às travas correspondentes e as estratégias endereçam as restrições
- [ ] Não há etapa "oca" — todas possuem ao menos uma ação concreta documentada
- [ ] A transição entre etapas é coerente (output de aquisição alimenta engajamento, e assim por diante)
- [ ] O volume projetado de aquisição é absorvível pelo sistema nas etapas seguintes
- [ ] O fluxo é sustentável com a estrutura atual ou identifica claramente o que precisa mudar

Responder obrigatoriamente:
- O fluxo está equilibrado ou há sobrecarga em alguma etapa?
- Onde o crescimento trava quando escala?
- O sistema cresce de forma sustentável ou frágil?

### 7. Apresentar no Comitê
Levar o fluxo consolidado para apresentação ao cliente. O documento final serve como base para desenho de playbooks táticos e alimenta diretamente o Cronograma de Implementação e o Forecast.

---

## Formato de Saída

```markdown
## Fluxo de Estratégia de Crescimento — [Nome do Cliente]
**Data:** [data] | **Consultor:** [nome]

### 1. Aquisição
**Canais:** [lista] | **Critérios de entrada:** [lista] | **Volume estimado:** [X/mês]
**Travas relacionadas:** Trava 7 ([score]) + Trava 6 ([score])
**Ações definidas:**
- [ação 1]
- [ação 2]

### 2. Engajamento
[mesmo formato]

### 3. Monetização
[mesmo formato]

### 4. Retenção
[mesmo formato]

### Integração Fluxo × Travas
[tabela do passo 5]

### Checklist de Conclusão
[checklist do passo 6]

### Consolidação
- Equilíbrio: [avaliação]
- Ponto de quebra na escala: [onde trava]
- Sustentabilidade: [avaliação]
```

---

## Exceções e Fallbacks
- **Negócio com modelo de receita única (sem retenção recorrente):** a etapa de Retenção foca em recompra e indicação, não em recorrência. Ajustar o critério de sucesso para ciclo de recompra.
- **Trava não diagnosticada (ex: negócio novo sem dados de Trava 1):** registrar como "sem diagnóstico" na integração e basear a estratégia em hipótese validável. Marcar no documento.
- **Fluxo desequilibrado sem solução operacional viável:** registrar como achado estratégico crítico — recomendar escopo reduzido ou priorização de uma macroetapa antes de expandir.
- **ICP ou PUV ainda em draft:** prosseguir com ressalva. Marcar fluxo como `DRAFT — DEPENDÊNCIAS PENDENTES`. Revisar após validação.
