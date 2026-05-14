# Contexto: Preparação da Matriz de Expansão

> Referência rápida para consulta durante execução.

---

## Definição

Mapear e priorizar as oportunidades de crescimento além do escopo atual do negócio, organizando as alavancas de expansão em uma matriz estruturada que conecta capacidade operacional, potencial de mercado e coerência estratégica.

**Escopo:** Aplica-se à Semana 5 do DR-X, após a definição do cronograma de implementação e do forecast. A matriz de expansão projeta o crescimento futuro além do plano de 90 dias, identificando para onde o negócio pode ir depois que as travas atuais forem resolvidas. O consultor prepara a matriz individualmente e apresenta ao cliente como parte do planejamento estratégico.

**Aplica-se quando:**
- Master Contexto do cliente (outputs/drx/clientes/[cliente]/master-contexto.md)
- ICP definido (Ficha de ICP do POP de Definição de ICPs)
- PUV definida (output do POP de Definição de PUV)
- Diferenciais Competitivos / Matriz CVB (output do POP de Diferenciais Competitivos)
- Fluxo de Estratégia de Crescimento (output do POP de Fluxo de Estratégia)
- Sizing de Mercado (TAM/SAM/SOM)
- Estudo de Concorrentes
- Cronograma de Implementação (context-cronograma-de-implementacao)
- Forecast (context-elaboracao-de-forecast)
- Árvore de Transição (context-arvore-de-transicao)

---

## Processo de Referência

**1. Mapear todas as oportunidades de crescimento possíveis a partir dos artefatos já produzidos e organizar em quatro categorias: Mercado atual + Oferta atual (Penetração), Mercado atual + Oferta nova (Desenvolvimento de produto), Mercado novo + Oferta atual (Desenvolvimento de mercado), Mercado novo + Oferta nova (Diversificação)**
- Ferramenta: Matriz Ansoff, Fluxo de Estratégia, PUV, CVB, Estudo de Concorrentes, Sizing
**2. Avaliar cada oportunidade mapeada em três dimensões: Potencial de receita (tamanho estimado e tempo de retorno), Esforço de implementação (mudanças operacionais, novos recursos, escalabilidade), Coerência estratégica (alinhamento com ICP e PUV, impacto no posicionamento, competição com recursos do plano de 90 dias)**
- Ferramenta: Dados do Sizing, Cronograma de Implementação, Forecast
**3. Construir matriz de priorização posicionando cada oportunidade com avaliação de Potencial (Alto/Médio/Baixo), Esforço (Alto/Médio/Baixo), Coerência (Alta/Média/Baixa) e atribuindo Prioridade (1-5) conforme regra: Prioridade 1 (alto potencial + baixo esforço + alta coerência), Prioridade 2 (alto potencial + médio esforço + alta coerência), Prioridade 3 (médio potencial ou média coerência), Descartar (baixa coerência ou alto esforço sem potencial)**
- Ferramenta: Matriz de priorização
**4. Definir horizonte de expansão para oportunidades priorizadas (Prioridade 1 e 2) em três níveis: Horizonte 1 (90-180 dias) para extensões naturais do plano atual, Horizonte 2 (6-12 meses) para movimentos que exigem preparação, Horizonte 3 (12+ meses) para apostas estratégicas de longo prazo, com máximo de 2-3 oportunidades por horizonte**

**5. Verificar se as oportunidades de Horizonte 1 estão contempladas no Forecast. Se não, estimar impacto incremental de receita, identificar o que precisaria ser adicionado ao cronograma e registrar como oportunidade de upside**
- Ferramenta: Forecast, Cronograma de Implementação- Condição: Se oportunidades de Horizonte 1 não estão no Forecast
**6. Documentar e consolidar a Matriz de Expansão em documento contendo: Mapa de oportunidades por categoria (Ansoff), Matriz de priorização preenchida, Horizonte de expansão com timeline, Conexão com Forecast (upside identificado)**


---

## Saídas Esperadas

- Mapa de oportunidades de expansão por categoria
- Matriz de priorização com critérios objetivos
- Horizonte de expansão em 3 níveis (90-180d, 6-12m, 12m+)
- Estimativa de impacto incremental no Forecast
- Documento pronto para incorporação na Entrega Final

---

## Exceções

- Negócio sem potencial de expansão claro: registrar que o foco deve ser consolidação e eficiência antes de expansão. A matriz terá poucas ou nenhuma oportunidade de Prioridade 1.
- Todas as oportunidades exigem alto esforço: sinalizar que o negócio precisa resolver restrições estruturais antes de expandir, referenciar as travas diagnosticadas que bloqueiam a escala.
- Oportunidade exige mudança de ICP: registrar separadamente como 'expansão com reposicionamento' — não misturar com a estratégia atual.

---

## Riscos e Pontos de Atenção

- ⚠️ Qualidade da análise depende diretamente da completude e precisão dos artefatos de entrada (Master Contexto, ICP, PUV, CVB, Sizing, Forecast), que podem estar incompletos ou desatualizados
- ⚠️ A priorização das oportunidades na matriz envolve julgamento estratégico subjetivo que a IA pode executar com viés se os dados de entrada forem ambíguos
- ⚠️ A definição de horizontes temporais exige conhecimento contextual profundo do negócio do cliente, aumentando risco de alocação incorreta sem validação humana
- ⚠️ Ausência de ferramenta definida nos passos 4 e 6 pode gerar inconsistência no formato do documento final

---

## Dependências

- Master Contexto do cliente (outputs/drx/clientes/[cliente]/master-contexto.md)
- Ficha de ICP (output do POP de Definição de ICPs)
- PUV definida (output do POP de Definição de PUV)
- Diferenciais Competitivos / Matriz CVB (output do POP de Diferenciais Competitivos)
- Fluxo de Estratégia de Crescimento (output do POP de Fluxo de Estratégia)
- Sizing de Mercado (TAM/SAM/SOM)
- Estudo de Concorrentes
- Cronograma de Implementação (context-cronograma-de-implementacao)
- Forecast (context-elaboracao-de-forecast)
- Árvore de Transição (context-arvore-de-transicao)
