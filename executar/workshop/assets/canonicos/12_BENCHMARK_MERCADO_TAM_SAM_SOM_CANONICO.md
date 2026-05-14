# Benchmark de Mercado, Concorrentes e TAM/SAM/SOM Canônico
**Atualizado:** 2026-04-30  
**Fonte final:** consolidação em `assets/canonicos`; base canônica original + `assets/legacy/merge/skills/01-benchmarking-estudo-mercado.md`.  
**Decisão de merge:** skill 01 já estava incorporada; `assets/canonicos` consolida essa versão como fonte final.


Status: v1 — benchmark + fluxo operacional unificados neste documento  
Escopo: etapa de inteligência de mercado antes da construção dos assets do EXECUTAR  
Objetivo: criar uma leitura externa do mercado, concorrência, tamanho de oportunidade e segmento prioritário antes de decidir quais assets e canais entram no ciclo v1.

**Nome operacional:** Benchmarking / Estudo de Mercado (GTM).  
**Propósito em uma frase:** entender como o mercado joga (estratégias, concorrentes e padrões de comunicação e performance) para orientar execução com evidência e diferenciação antes de produzir assets.

## 1. Princípio

Benchmark não é "ver alguns concorrentes". É a etapa que impede o time de montar estratégia olhando só para dentro do cliente.

Antes de construir plano de mídia, dossiê estratégico, LP ou criativos, o time precisa responder:

- qual mercado estamos tentando capturar;
- qual parte desse mercado o cliente realmente consegue atender;
- qual parte consegue capturar com capacidade e budget atuais;
- quem disputa a mesma atenção;
- quais mensagens já estão saturadas;
- onde existe uma brecha de diferenciação;
- qual segmento deve ser atacado primeiro.

Benchmark sem evidência ou sem ligação com decisão vira teatro: tudo que entra no dossiê deve ter lastro (print, link, nota de fonte, premissa explícita).

## 2. Fontes internas de referência

Este documento adapta padrões das skills canônicas do SABER:

- `sizing-mercado-tam-sam-som`;
- `estudo-concorrentes`;
- `swot-beachhead-market`;
- `definicao-icp-b2b` ou `definicao-persona-b2c`, quando aplicável.

Caminho local das skills:

```text
brain_v4_colli/areas/iniciativas/agentizacao_saber/agents/canonicos/analista-mercado-benchmark/skills/ativas/
```

## 3. Quando produzir, quando reforçar e quando não usar

### 3.1 Momento na jornada (obrigatório)

Produzir depois de:

- handoff operacional;
- diagnóstico de maturidade GTM;
- discovery mínimo.

Produzir antes de:

- dossiê estratégico de oferta e comunicação;
- plano de mídia;
- briefing criativo;
- LP/ponto de conversão.

### 3.2 Quando reabrir ou reforçar o benchmark

- onboarding ou setup de conta, sempre que ainda não existir leitura N2 do mercado;
- queda de performance com suspeita de descolamento do padrão do setor;
- mudança relevante de canal, segmento, oferta ou geografia — recalibrar referências e hipóteses.

### 3.3 Quando não usar (anti-padrões)

- como pesquisa infinita sem decisão nem backlog: o trabalho precisa encerrar em entregáveis e hipóteses testáveis;
- para vestir opinião com o rótulo de "benchmark" sem evidência ou sem fonte;
- como substituto de TAM/SAM/SOM, SWOT específica, beachhead ou mapa 2x2 quando o nível N2 exige esses blocos (use o fluxo da seção 5 e a estrutura da seção 6).

## 4. Inputs obrigatórios e mínimos operacionais

### 4.1 Pacote mínimo institucional (N2)

- pacote de handoff EXECUTAR;
- plano de ROI;
- diagnóstico GTM;
- produto/serviço foco;
- ticket médio;
- região/mercado-alvo;
- ICP ou persona preliminar;
- histórico de clientes;
- budget mensal disponível;
- capacidade operacional atual;
- lista inicial de concorrentes, se existir.

### 4.2 Mínimos para execução do estudo de campo (operacional)

- contexto do cliente: segmento, produto, ticket médio, geografia, restrições;
- lista inicial de concorrentes (tipicamente 3 a 10) e/ou palavras-chave de busca para descoberta;
- canais de interesse (ex.: Meta, Google, LinkedIn, YouTube, orgânico) e objetivo da aquisição (lead, demo, compra, outro).

### 4.3 Fontes e ferramentas (orientação, não lacuna)

Priorizar evidência de mídia e de jornada, alinhado à ordem da seção 6.3: bibliotecas de anúncios (ex.: Meta Ads Library), busca e SERP, LPs e páginas de destino, redes sociais, reviews, depois oferta e prova social. Analytics internos do cliente entram quando disponíveis. A padronização fina de stack por franquia pode evoluir em documento separado; aqui o critério é: **fonte nomeada, data quando couber, e evidência anexável.**

## 5. Fluxo de execução sugerido

Ordem prática para transformar inputs na estrutura canônica (seção 6):

1. Definir escopo e pergunta de negócio (qual conversão, qual público, qual faixa de ticket, qual decisão o benchmark precisa destravar).
2. Selecionar amostra de concorrentes: diretos, substitutos e referências fortes do setor (evitar comparar com irrelevante).
3. Coletar evidências por concorrente:
   - comunicação: headline, promessa, prova, CTA, oferta;
   - criativos: estrutura, hooks, provas, formatos, padrões;
   - páginas e LPs: estrutura, primeira dobra, fricções, formulários, provas;
   - campanhas: quando visível, ângulos, segmentação aparente, consistência temporal.
4. Consolidar padrões e receitas observadas (o que se repete com força no setor).
5. Construir matriz força versus fraco por player e implicações para diferenciação do cliente.
6. Converter em decisões explícitas:
   - o que adotar como baseline (estruturas já validadas no mercado);
   - onde diferenciar (oportunidades) e o que mitigar (riscos e armadilhas).
7. Gerar backlog de hipóteses testáveis com prioridade e métrica de sucesso (CPL, CAC, CTR, taxa de conversão, conforme objetivo).

## 6. Estrutura canônica do benchmark

### 6.1 Contexto do mercado

Deve conter:

- segmento;
- geografia;
- tipo de venda;
- ticket;
- maturidade do mercado;
- sazonalidade;
- tendências relevantes;
- mudanças regulatórias, tecnológicas ou comportamentais.

### 6.2 TAM/SAM/SOM

#### TAM - Total Addressable Market

Mercado total possível para aquela categoria.

Deve conter:

- valor em BRL ou USD;
- escopo geográfico;
- fonte;
- ano da fonte;
- método usado;
- intervalo de incerteza, se estimado.

#### SAM - Serviceable Addressable Market

Parte do TAM que o cliente consegue atender por geografia, nicho, ICP, produto e canal.

Deve conter:

- filtros aplicados;
- justificativa dos filtros;
- fontes ou premissas;
- valor final;
- exclusões explícitas.

#### SOM - Serviceable Obtainable Market

Parte do SAM que o cliente consegue capturar com capacidade e budget atuais.

Regra central:

```text
SOM = menor valor entre potencial de mercado, capacidade operacional e aquisição viável com budget atual.
```

Tabela obrigatória:

| Variável | Valor | Fonte |
| --- | --- | --- |
| Capacidade operacional | clientes/projetos/mês | cliente/operação |
| Budget mensal de aquisição | R$/mês | cliente/operação |
| CPL ou custo de oportunidade estimado | R$ | histórico/benchmark |
| Leads/mês possíveis | budget / CPL | cálculo |
| Taxa de conversão estimada | % | histórico/benchmark |
| Clientes/mês capturáveis | min(capacidade, leads x conversão) | cálculo |
| Faturamento potencial/mês | clientes x ticket | cálculo |
| SOM anual | faturamento/mês x 12 | cálculo |

### 6.3 Análise de concorrentes

Começar por concorrentes que disputam atenção e mídia, não apenas por sites bonitos.

Ordem recomendada:

1. Meta Ads Library;
2. Google/Search e LPs;
3. redes sociais;
4. reviews/reputação;
5. oferta, preço, promessa e prova.

Para cada player:

- tipo: direto, indireto ou substituto;
- está anunciando?;
- formato predominante;
- mensagem principal;
- oferta;
- prova;
- pontos fortes;
- pontos fracos;
- gap explorável.

Use os recortes da etapa 3 do fluxo (seção 5) para preencher com consistência comunicação, criativos, páginas e sinais de campanha.

### 6.4 Ruído de mercado

Listar frases e promessas saturadas.

Exemplos:

- atendimento personalizado;
- equipe especializada;
- solução completa;
- inovação;
- qualidade superior;
- preço justo.

Essas frases só podem ser usadas se forem comprovadas e especificadas.

### 6.5 Mapa competitivo 2x2

Definir dois eixos relevantes para o mercado e posicionar:

- concorrentes;
- alternativas indiretas;
- posição atual do cliente;
- posição recomendada.

O eixo deve revelar uma decisão estratégica real, por exemplo:

- generalista vs especialista;
- baixo preço vs alto valor;
- conveniência vs profundidade;
- performance vs marca;
- local vs nacional;
- humano/consultivo vs autosserviço.

### 6.6 SWOT específica

A SWOT deve ser específica para o cliente.

Regra:

```text
Se trocar o nome da empresa e o item ainda servir para qualquer negócio do setor, está genérico demais.
```

Para cada item:

- título;
- evidência;
- impacto;
- implicação estratégica.

### 6.7 Beachhead Market

Beachhead é o segmento onde o cliente deve concentrar a primeira força.

Não é "todo o mercado". É o recorte onde há melhor combinação entre:

- urgência da dor;
- capacidade de pagar;
- facilidade de acesso;
- tamanho suficiente;
- baixa densidade competitiva;
- alinhamento com forças do cliente;
- viabilidade operacional.

Scorecard:

| Critério | Peso | Segmento A | Segmento B | Segmento C |
| --- | --- | --- | --- | --- |
| Urgência da dor | Alta | /5 | /5 | /5 |
| Capacidade de pagar | Alta | /5 | /5 | /5 |
| Facilidade de acesso | Média | /5 | /5 | /5 |
| Tamanho do segmento | Média | /5 | /5 | /5 |
| Densidade competitiva | Alta | /5 | /5 | /5 |
| Alinhamento com forças | Alta | /5 | /5 | /5 |

## 7. Saída esperada

O benchmark deve gerar o pacote institucional:

- contexto de mercado;
- TAM/SAM/SOM;
- concorrentes e alternativas;
- ruído de mercado;
- mapa competitivo;
- gaps e oportunidades;
- SWOT específica;
- beachhead recomendado;
- implicações para o pacote de assets v1;
- implicações para oferta/comunicação;
- implicações para mídia e criativos.

**Mapa do campo de batalha (síntese operacional):** além do acima, produzir visão consolidada com: lista de concorrentes auditados com evidências; padrões dominantes em criativos, páginas e comunicação; hipóteses de por que esses padrões funcionam (com lastro); oportunidades (lacunas) e riscos (armadilhas) do segmento.

**Consumidores diretos desta saída:**

- Dossiê estratégico de oferta e comunicação (DEOC) e demais assets de narrativa;
- plano de mídia (canais, campanhas, cadência);
- planilha ou backlog de testes (hipóteses priorizadas e métrica de sucesso).

## 8. Como alimenta os assets

O pacote de assets do ciclo deve usar o benchmark para decidir:

- canal prioritário;
- segmento inicial;
- ICP/persona foco;
- promessa mais defensável;
- tipo de campanha;
- tipo de LP;
- provas necessárias;
- risco de mercado;
- esforço de diferenciação;
- hipótese de mídia.

## 9. Componentes críticos (o que iterar com rigor)

- Qualidade da amostra: concorrentes certos; comparar com irrelevante destrói a utilidade.
- Evidência (prints, links, notas) versus opinião: sem evidência, não entra como fato.
- Extração de padrões (o que se repete) versus coleção de exemplos soltos.
- Tradução em decisão (baseline copiável mais diferenciação) versus relatório sem consequência.
- Backlog de hipóteses: testável, com métrica, priorizado e rastreável até teste e aprendizado.

## 10. Definition of pronto operacional e critério N2

### 10.1 Checklist operacional (DoD mínimo do entregável)

- Amostra mínima definida (número de concorrentes e critérios de escolha documentados).
- Evidências anexadas ou registradas (não só narrativa).
- Padrões sintetizados em cerca de 5 a 15 bullets acionáveis (evitar lista infinita).
- Decisões explícitas:
  - baseline do que será adotado do mercado;
  - cerca de 3 a 7 oportunidades de diferenciação;
  - cerca de 3 a 7 riscos a mitigar.
- Backlog de hipóteses com prioridade e métrica (CPL, CAC, CTR, conversão, conforme objetivo).

### 10.2 N2 (auditoria)

Benchmark está N2 quando:

- TAM/SAM/SOM têm fontes ou premissas explícitas;
- SOM considera capacidade e budget, não só tamanho de mercado;
- concorrentes reais foram analisados;
- ruídos de mercado foram listados;
- beachhead foi escolhido por critério;
- implicações para o pacote de assets v1 estão claras;
- fontes e incertezas estão documentadas;
- o checklist da seção 10.1 está atendido ou justificado item a item quando algum bloco for N/A (ex.: mercado muito novo — explicar e registrar risco).

## 11. Critério N3

Benchmark está N3 quando:

- estimativas são atualizadas com dados reais de campanha e CRM;
- beachhead é revisado por performance;
- concorrentes são monitorados em cadência;
- mudanças de mercado viram backlog;
- aprendizados alimentam novos benchmarks por cohort/segmento.

## 12. Gestão contínua

- **Métricas / KPIs sugeridos:** percentual de hipóteses do backlog testadas; impacto médio por hipótese; tempo de ciclo hipótese → teste → aprendizado.
- **Thresholds (verde / amarelo / vermelho):**
  - verde: backlog atualizado e hipóteses testadas em cadência combinada com o time;
  - amarelo: muito dado coletado e pouca decisão ou pouco teste;
  - vermelho: o benchmark não gera mudança observável em plano de mídia ou em dossiê/comunicação por dois ciclos consecutivos.
- **Cadência de revisão:** quinzenal ou mensal por segmento/canal, e sempre após mudança relevante de canal, segmento ou oferta.
- **Dono:** definir no kickoff ou no RACI da conta (não deixar órfão).
- **Registro obrigatório:** changelog do que mudou no ciclo benchmark → decisão → teste → resultado.

## 13. O que evitar

- usar SAM como SOM;
- inventar market share arbitrário;
- começar por site institucional e ignorar anúncios ativos;
- aceitar "qualidade" e "atendimento" como diferenciais sem prova;
- analisar concorrentes sem apontar fraquezas;
- escolher beachhead por preferência do cliente, não por evidência;
- montar plano de mídia antes de entender mercado e concorrência;
- confundir volume de screenshots com síntese ou com decisão.

## 14. Template e exemplos

- Template de estrutura genérica de skill/asset: `templates/asset-skill.md` (nesta pasta `assets/canonicos/templates/`).
- **Exemplos reais versionados:** evoluir em repositório ou anexo quando houver caso autorizado para publicação; até lá, usar este documento e o checklist 10.1 como padrão mínimo.
