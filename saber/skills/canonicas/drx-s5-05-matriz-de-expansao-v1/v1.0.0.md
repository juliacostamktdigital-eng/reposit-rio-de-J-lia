---
slug: drx-s5-05-matriz-de-expansao-v1
description: "name: Matriz de Expansão"
name: Matriz de Expansão
status: draft-v1

---

# Matriz de Expansão

## Descrição
Mapeia e prioriza oportunidades de crescimento **além do plano de 90 dias**, organizando alavancas de expansão em uma matriz que conecta capacidade operacional, potencial de mercado e coerência estratégica. Projeta para onde o negócio pode ir depois das travas atuais serem resolvidas.

Ativar quando for necessário planejar horizontes de expansão pós-diagnóstico, especialmente após cronograma e forecast já definidos.

## Quando Usar
- Triggers: "matriz de expansão", "oportunidades de crescimento", "horizontes de expansão", "para onde crescer", "expansão pós-90 dias"
- **NÃO usar quando:**
  1. O Cronograma de 90 dias ainda não foi finalizado — sem ele, não há âncora para horizontes
  2. O Forecast ainda não foi elaborado — a matriz precisa conectar com projeções financeiras
  3. O ICP/PUV/CVBA não estão definidos — coerência estratégica depende deles

## Inputs Necessários
1. **Master Contexto do cliente** `[VALIDADO]`
2. **ICP definido** (output de `drx-s4-04-icp-ideal-customer-profile-v1`)
3. **PUV definida** (output de `drx-s4-03-puv-proposta-unica-de-valor-v1`)
4. **Matriz CVBA** (output de `drx-s4-02-matriz-cvba-diferenciais-competitivos-v1`)
5. **Fluxo de Estratégia** (output de `drx-s4-05-fluxo-de-estrategia-v1`)
6. **Sizing de Mercado** (TAM/SAM/SOM)
7. **Estudo de Concorrentes**
8. **Cronograma de Implementação** (output de `drx-s5-03-cronograma-90-dias-v1`)
9. **Forecast** (output de `drx-s5-04-forecast-financeiro-v1`)
10. **Árvore de Transição** (output de `drx-s5-02-arvore-de-transicao-v1`)

## Processo de Execução

### 1. Mapear oportunidades pela Matriz Ansoff
Organizar oportunidades em 4 quadrantes:
- **Penetração** (mercado atual + oferta atual)
- **Desenvolvimento de produto** (mercado atual + oferta nova)
- **Desenvolvimento de mercado** (mercado novo + oferta atual)
- **Diversificação** (mercado novo + oferta nova)

### 2. Avaliar cada oportunidade em 3 dimensões
| Dimensão | Escala | Critério |
|---|---|---|
| Potencial de receita | Alto/Médio/Baixo | Tamanho estimado + tempo de retorno |
| Esforço de implementação | Alto/Médio/Baixo | Mudanças operacionais, novos recursos, escalabilidade |
| Coerência estratégica | Alta/Média/Baixa | Alinhamento com ICP e PUV, impacto no posicionamento, competição com recursos do plano de 90 dias |

### 3. Priorizar (1-5)
- **Prioridade 1:** alto potencial + baixo esforço + alta coerência
- **Prioridade 2:** alto potencial + médio esforço + alta coerência
- **Prioridade 3:** médio potencial ou média coerência
- **Descartar:** baixa coerência ou alto esforço sem potencial

### 4. Definir horizonte temporal
Para Prioridade 1 e 2:
- **Horizonte 1 (90-180 dias):** extensões naturais do plano atual
- **Horizonte 2 (6-12 meses):** movimentos que exigem preparação
- **Horizonte 3 (12+ meses):** apostas estratégicas de longo prazo

Máximo 2-3 oportunidades por horizonte.

### 5. Conectar com Forecast (upside)
Para oportunidades de Horizonte 1 que não estão no Forecast:
- Estimar impacto incremental de receita
- Identificar o que precisaria ser adicionado ao cronograma
- Registrar como upside do Forecast

### 6. Consolidar documento
Montar documento com:
- Mapa de oportunidades por categoria Ansoff
- Matriz de priorização preenchida
- Horizonte de expansão com timeline
- Conexão com Forecast (upside identificado)

## Outputs Esperados
- Mapa de oportunidades de expansão por categoria
- Matriz de priorização com critérios objetivos
- Horizonte de expansão em 3 níveis (90-180d, 6-12m, 12m+)
- Estimativa de impacto incremental no Forecast
- Documento pronto para incorporação na Entrega Final

## Exceções
- **Negócio sem potencial de expansão claro:** registrar que o foco deve ser consolidação antes de expansão. Matriz terá poucas ou zero Prioridade 1
- **Todas as oportunidades exigem alto esforço:** sinalizar que há restrições estruturais a resolver antes
- **Oportunidade exige mudança de ICP:** registrar como "expansão com reposicionamento", separado da estratégia atual

## Riscos
- ⚠️ Qualidade depende da completude dos artefatos de entrada — lacunas geram matriz enviesada
- ⚠️ Priorização envolve julgamento estratégico subjetivo — IA pode viesar se dados forem ambíguos
- ⚠️ Horizontes temporais exigem conhecimento contextual profundo — sempre validar com consultor
