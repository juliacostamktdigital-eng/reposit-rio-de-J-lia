# De-Para de Skills — Estruturação Estratégica

**Documento:** Backlog de skills para o produto Diagnóstico e Planejamento de Marketing e Vendas  
**Base de comparação:** `inteligencia-skills-estruturacao-estrategica.md` (26 skills mapeadas) × `skills/v4-estruturacao-marketplace-main/.agents/skills/` (26 arquivos existentes)  
**Data:** 2026-04-14

---

## Como Ler

| Status | Significado |
|--------|-------------|
| **USAR** | Skill existente já entrega o que o produto exige — usar sem alteração |
| **ITERAR** | Skill existente existe e tem o núcleo certo, mas faltam elementos críticos documentados na inteligência |
| **CRIAR** | Skill não existe na pasta, ou a existente é tão diferente que é melhor criar do zero |

> **Contexto importante:** O produto "Diagnóstico e Planejamento" é da categoria **Saber** — não executa, não produz criativos, não sobe campanha, não configura CRM. Várias skills existentes são de **execução/produção** (landing page, brandbook, SDR IA) e estão **fora do escopo deste produto**. Elas são analisadas em seção separada.

---

## 1. Tabela Principal — Skills do Produto (da Inteligência → Pasta)

### Semana 2 — Pesquisa de Mercado e Posicionamento

| # | Skill na Inteligência | Skill Existente | Status | O que a existente já faz | O que falta / Gap crítico |
|---|----------------------|-----------------|--------|--------------------------|---------------------------|
| 1 | `sizing-mercado-tam-sam-som` | `ee-s2-pesquisa-mercado` | **ITERAR** | TAM/SAM/SOM com fontes, WebSearch real, premissas explícitas | (a) Não tem parâmetro `moeda` (BRL vs USD — descoberto no PSM Company); (b) SOM não é calculado com as 2 variáveis críticas do cliente: capacidade operacional + budget; (c) não tem gráfico de funil/círculos concêntricos como formato de output prescrito; (d) não separa do restante da pesquisa (concorrentes, JTBD) — o POP 2.1 é uma skill isolada de 2h |
| 2 | `estudo-concorrentes` | `ee-s2-pesquisa-mercado` | **ITERAR** | Análise de 3-5 concorrentes com WebSearch, mapa competitivo 2x2 | (a) Não tem Meta Ads Library como **primeiro passo obrigatório** (quem investe é concorrente real, não quem tem site bonito); (b) não tem parâmetro `tipo_concorrente` (direto/indireto/substituto — crítico para B2B de serviços como PSM); (c) não está separado do TAM/SAM/SOM — a inteligência pede 2 skills distintas com 2h cada; (d) falta "coluna de Fraquezas é o coração da análise" como regra |
| 3 | `definicao-icp-b2b` | `ee-s1-persona-icp` | **ITERAR** | ICP com firmográficos, JTBD funcional/emocional/social, dores, ganhos | (a) Não tem Comitê de Compra (Iniciador/Influenciador/Decisor) — POP 2.3 exige explicitamente; (b) não tem Tabela "Motivos Racionais vs Políticos" (o político é o diferencial V4 vs consultorias genéricas); (c) não tem JTBD em 4 camadas (Principal + Funcionais + Emocionais + Sociais) — PSM Company revelou Social Jobs como camada crítica; (d) não tem parâmetro `ucm` para adaptar profundidade conforme maturidade |
| 4 | `definicao-persona-b2c` | `ee-s1-persona-icp` | **ITERAR** | Persona B2C com dados demográficos, foto, citação, canais | (a) B2B e B2C estão mesclados em uma skill só — sem parâmetro de separação; (b) não tem guia explícito de **data mining de reviews** (Instagram/Amazon de concorrentes) como passo obrigatório antes de construir a persona; (c) não tem "Persona Primária = a que paga as contas" como regra de foco |
| 5 | `jobs-to-be-done` | `ee-s1-persona-icp` | **ITERAR** | JTBD no formato "Quando/Quero/Para que", funcional + emocional + social | (a) JTBD está embutido no ICP — não é skill isolada do POP 2.5; (b) não tem 4 camadas completas: **Job Principal** (agnóstico ao produto) + Funcionais + Emocionais + Sociais; (c) Jobs Sociais B2B não têm formato estruturado ("O Gestor que Entrega" / "O Guardião" são arquétipos de reputação interna); (d) não distingue JTBD do produto vs JTBD dos clientes do cliente (dois níveis diferentes) |
| 6 | `swot-beachhead-market` | `ee-s1-swot` | **ITERAR** | SWOT específico (não genérico), síntese estratégica, ações prioritárias | (a) Não tem Beachhead Market — POP 3.2 exige scorecard 0-5 comparando 2-3 segmentos candidatos com critérios; (b) falta ligar explicitamente ao TAM/SAM: o Beachhead é o SOM vencedor; (c) a SWOT existente é ótima como núcleo — só falta acrescentar o módulo Beachhead como segunda seção da skill |
| 7 | `proposta-unica-de-valor` | `ee-s2-posicionamento` | **ITERAR** | PUV validada em 5 critérios, Canvas 4Ps, território de marca, taglines, 3 declarações | (a) Não tem 3 variações de PUV por angulação: **Ganho / Medo / Lógica** (padrão dos entregáveis Becton/Ashele); (b) não tem JTBD tático específico para o Beachhead Market como input da PUV; (c) não tem slot `falha_estrutural` para posicionamento B2B de serviços (PSM padrão); (d) skill é muito abrangente (Canvas 4Ps + território + taglines + declarações em uma só) — em projetos reais pode ser densa demais; rever se vale separar PUV de Canvas |

---

### Semana 3 — Diagnóstico de Marketing

| # | Skill na Inteligência | Skill Existente | Status | O que a existente já faz | O que falta / Gap crítico |
|---|----------------------|-----------------|--------|--------------------------|---------------------------|
| 8 | `diagnostico-meta-ads` | `ee-s2-diagnostico-midia` | **ITERAR** | Diagnóstico de mídia com benchmarks, Top 3 problemas, plano 30 dias | (a) Meta Ads e Google Ads estão misturados em uma skill — não tem auditoria **Top Down específica** (Campanha > Conjunto > Anúncio); (b) não tem validação de Pixel/API de Conversão como seção própria; (c) não analisa Fase de Aprendizado como variável; (d) não tem análise de Frequência vs Saturação de público |
| 9 | `diagnostico-google-ads` | `ee-s2-diagnostico-midia` | **ITERAR** | Idem ao #8 — coberto dentro da skill de mídia geral | (a) Não tem Escada de Maturidade de Lances (CPC Manual → tCPA → tROAS); (b) não tem análise de Termos Sanguessugas (keywords de alto custo zero conversão); (c) não tem Índice de Qualidade médio; (d) não tem avaliação SKAG vs Hagakure por estrutura de conta |
| 10 | `analise-eficiencia-investimentos` | `ee-s2-diagnostico-midia` | **ITERAR** | Análise por canal e plano de ação | (a) Não tem análise transversal **Meta vs Google vs Outros** com CPA/ROAS por canal comparados; (b) não tem mapa de funil completo (Impressão → Clique → Lead → Oportunidade → Venda) com taxas por etapa; (c) não tem recomendação explícita de **realocação de verba** com impacto projetado |
| 11 | `plano-de-acao-5w2h` | **NENHUMA** | **CRIAR** | — | Skill genérica de síntese de diagnóstico em 5W2H (O que / Por que / Quem / Onde / Quando / Como / Quanto Custa). Reutilizável em 4 POPs diferentes (4.4, 5.4, 6.4, 8.3). Deve ter priorização Low Hanging Fruits vs Impacto Estrutural. Alta prioridade — economiza tempo do Account e do GT em múltiplos módulos |
| 12 | `analise-criativos` | `ee-s2-diagnostico-criativos` | **ITERAR** | Matriz de avaliação (5 dimensões × score), padrões, briefing de produção | (a) Não tem análise **Forma** (técnica: cortes, contraste, zonas) vs **Fundo** (conteúdo: hook, Big Idea, CTA) como framework do POP 5.1; (b) não tem cruzamento explícito dos dados de performance (CTR/CPA) com avaliação visual; (c) skill é da Semana 2 no sistema existente, inteligência coloca na Semana 3 — verificar posição no fluxo |
| 13 | `benchmarking-anuncios` | Embutido em `ee-s2-diagnostico-criativos` | **CRIAR** | Diagnóstico de criativos menciona análise de concorrentes, mas não como skill dedicada | Skill dedicada para: pesquisa em Meta Ads Library + TikTok Creative Center, filtro de anúncios ativos > 30 dias (sinal de ROI), moodboard categorizado por objetivo (Awareness/Conversão/Remarketing), análise de estrutura (gancho/formato/promessa/CTA), "ideias para testar". Hoje é etapa dentro de `ee-s2-diagnostico-criativos` mas com pouca profundidade |
| 14 | `diagnostico-social-media` | Parcialmente em `ee-s1-auditoria-comunicacao` | **ITERAR** | Auditoria de Instagram dentro da auditoria geral de comunicação | (a) Auditoria geral cobre 5 canais mas não tem o formato específico do POP 5.3: Bio, Destaques, Posts Fixados, benchmark vs 3 concorrentes; (b) não tem "nova bio sugerida" como output padrão; (c) não tem avaliação de destaques como menu de navegação do ICP; (d) auditoria geral mistura social media com site, anúncios, GMB — para o produto Diagnóstico, social media merece seção própria |
| 15 | `diagnostico-copy-lp` | `ee-s2-diagnostico-cro` | **ITERAR** | CRO unificado: copy, UX, PageSpeed, hipóteses de teste, wireframe | (a) Copy, UX e PageSpeed estão bundled — a inteligência os separa em 3 skills distintas (POPs 6.1, 6.2, 6.3); (b) não tem checklist de "Message Match" (anúncio → LP); (c) não tem análise de "pontos de fuga" da página por seção; (d) a skill existente é para "reformular a LP" — o produto Saber só diagnóstica, não reescreve |
| 16 | `diagnostico-ux-ui-lp` | `ee-s2-diagnostico-cro` | **ITERAR** | Idem ao #15 | (a) UX não tem análise mobile-first específica por tipo de dispositivo Android/iOS; (b) não tem análise de contraste de CTAs vs WCAG; (c) não tem avaliação de elementos de confiança (selos, CNPJ, rodapé) como checklist |
| 17 | `diagnostico-pagespeed-tracking` | `ee-s2-diagnostico-cro` | **ITERAR** | PageSpeed está dentro do diagnóstico CRO | (a) Validação de eventos de Pixel Meta e Conversão Google (PageView/Lead/Purchase) não está explicitada como checklist separado; (b) não tem check de SEO On-page (Title Tag, H1, meta description) como seção do diagnóstico |

---

### Semana 4.1 — Diagnóstico Comercial

| # | Skill na Inteligência | Skill Existente | Status | O que a existente já faz | O que falta / Gap crítico |
|---|----------------------|-----------------|--------|--------------------------|---------------------------|
| 18 | `diagnostico-comercial-crm` | `ee-s4-diagnostico-comercial` | **ITERAR** | Funil de vendas vs benchmarks, mapa de objeções, critérios 1-5★, SLA, plano de ação | (a) Não tem auditoria de **higiene do CRM** (leads sem tarefa, motivos de perda preenchidos) — POP 8.1 exige; (b) não tem análise qualitativa de calls (técnica, processo, comportamento) — é input para identificar vícios como "fala preço antes de valor"; (c) não tem **Lead Response Time** como KPI central; (d) não tem perfil Hunter/Farmer do time de vendas; (e) foca em critérios de qualificação para SDR IA — para o produto Diagnóstico, o output é o diagnóstico do funil, não a preparação para o SDR |
| 19 | `cliente-oculto` | `ee-s4-cliente-oculto` | **USAR** | Perfil de comprador fictício, script de simulação, análise em 7 critérios, nota 0-10, prints, impacto estimado do SDR IA | Skill bem estruturada e alinhada ao POP 8.2. Único ajuste menor: o "impacto estimado do SDR IA" é irrelevante para o produto Diagnóstico (não inclui SDR) — mas não compromete o núcleo da skill |
| 26 | `analise-crm-receita` | Parcialmente em `ee-s4-diagnostico-comercial` | **CRIAR** | Diagnóstico comercial tem funil de vendas mas não mapeamento CRM → funil estratégico | Skill dedicada para: mapear CRM do cliente (Omie, Pipedrive, RD Station, HubSpot) para funil estratégico (Lead/MQL/SQL/Venda), segmentar por fluxo de receita multi-produto, calcular taxas por etapa, definir critérios de SQL, identificar gargalo principal. Diferentes plataformas de CRM exigem abordagem diferente |

---

### Semana 4.2 — Plano de Marketing e Vendas (GTM + Forecast)

| # | Skill na Inteligência | Skill Existente | Status | O que a existente já faz | O que falta / Gap crítico |
|---|----------------------|-----------------|--------|--------------------------|---------------------------|
| 20 | `gtm-priorizacao-canais` | **NENHUMA** | **CRIAR** | — | Skill de Go-To-Market com ICE Score (Impacto × Confiança × Facilidade) por canal, mix 70/30 (canal principal + canais de teste), justificativa de exclusões, slide visual "onde o cliente aparecerá nos próximos 3 meses". Alta prioridade — presente em 100% dos projetos, decisão estratégica central do produto |
| 21 | `drawflow-estrategia-aquisicao` | **NENHUMA** | **CRIAR** | — | Skill para selecionar estratégia base (Público/Lista/Lista+Monetização/Sem Monetização) e desenhar fluxo visual completo: Tráfego → Engajamento → Conversão → Remarketing. Output: fluxograma com ativos necessários por etapa e qual estratégia se aplica |
| 22 | `forecast-midia-3-meses` | `ee-s3-forecast-midia` | **ITERAR** | Modelagem financeira 3 meses, 3 cenários, distribuição plataforma/funil, cronograma, alertas, Google Sheets | (a) Não tem modo UCM 1 — cliente sem mídia precisa de **plano de lançamento**, não diagnóstico de benchmark (a skill atual pressupõe que o cliente já investe); (b) não tem projeção macro de **12 meses** além dos 3 meses detalhados; (c) não começa pela **engenharia reversa da meta** (quanto quero faturar → quantas vendas → quantos leads → qual budget); (d) está na Semana 3 do sistema existente mas a inteligência coloca na Semana 4.2 — verificar posição |

---

### Transversal — Entregáveis, Decks e Modelos de Diagnóstico

| # | Skill na Inteligência | Skill Existente | Status | O que a existente já faz | O que falta / Gap crítico |
|---|----------------------|-----------------|--------|--------------------------|---------------------------|
| 23 | `deck-semana-estruturacao` | **NENHUMA** | **CRIAR** | — | Skill geradora de deck de apresentação semanal no padrão V4: cover "WELCOME TO YOUR OWN [TEMA]", índice estruturado, linha do tempo de etapas, slides de dados com interpretação, slide de próximos passos. Recebe outputs das skills analíticas da semana e formata em apresentação. Alta dependência de outputs anteriores como input |
| 24 | `deck-entrega-final` | **NENHUMA** | **CRIAR** | — | Skill que consolida todas as semanas em um único deck final com narrativa coesa: Dor → Diagnóstico → Plano → Forecast. Inclui DrawFlow, sumário executivo, forecast visual e cronograma de implantação. É o principal entregável tangível do produto |
| 25 | `diagnostico-travas-scoring` | **NENHUMA** | **CRIAR** | — | Skill no modelo Devstate: Pergunta estruturante → Dados com interpretação → Score 0-5 por dimensão → Total com faixa de diagnóstico → Consolidação causal em uma frase → Determinação preliminar. Aplicável a qualquer dimensão (Exposição, Atenção, CRO, CRM, Criativos). É o **padrão visual mais impactante** encontrado nos entregáveis reais — alta prioridade de criação |

---

## 2. Skills Existentes Fora do Escopo do Produto "Saber"

Estas skills foram criadas para uma versão mais ampla do produto (com execução/produção), mas o produto **Diagnóstico e Planejamento** é categoria **Saber** — não executa. São mantidas na pasta para outros produtos/contextos, mas **não devem ser usadas neste produto**.

| Skill Existente | Por que está fora do escopo |
|-----------------|----------------------------|
| `ee-s3-landing-page` | Execução: cria e faz deploy de LP em React — o produto Saber apenas diagnosica a LP existente |
| `ee-s3-identidade-visual` | Execução: cria paleta, tipografia, prompts Midjourney — fora do escopo diagnóstico |
| `ee-s3-brandbook` | Execução: cria manual de marca completo — o produto Saber não produz brandbook |
| `ee-s3-crm-setup` | Execução: configura Kommo CRM com pipeline e automações — fora do escopo |
| `ee-s3-copy-anuncios` | Execução: gera 30+ variações de copy para subir — fora do escopo |
| `ee-s3-gmb-otimizacao` | Execução: configura Google Meu Negócio — fora do escopo do diagnóstico |
| `ee-s5-scripts-sdr` | Execução: cria scripts de SDR IA para WhatsApp — fora do escopo |
| `ee-s5-sdr-ia-config` | Execução: configura agente SDR no Patagon + Kommo — fora do escopo |

> **Nota:** Estas skills podem compor um produto de **execução** separado (Implementação/Fazer). Não deletar — arquivar ou referenciar em outro contexto de produto.

---

## 3. Skills de Infraestrutura do Sistema (Manter sem Alteração)

Estas skills são operacionais do sistema — não produzem outputs de diagnóstico, mas sustentam o workflow. Usar sem alteração.

| Skill | Função |
|-------|--------|
| `ee-novo-cliente` | Cadastro, briefing, estrutura de pastas, integração V4MOS |
| `ee-continuar` | Retomar trabalho, dependency graph, checkpoint management |
| `ee-onboarding` | Setup inicial da workspace |
| `ee-adicionar-base` | Adicionar conteúdo à base de conhecimento do cliente |
| `ee-duvida` | FAQ / ajuda sobre o sistema |
| `ee-feedback` | Reportar problemas e sugestões via GitHub Issues |

---

## 4. Skills Existentes Sem Correspondência na Inteligência (mas dentro do escopo)

| Skill Existente | Papel | Recomendação |
|-----------------|-------|--------------|
| `ee-s1-diagnostico-maturidade` | Score inicial de maturidade digital (mídia, criativos, CRO, CRM, SEO) | **MANTER** — não foi mapeada como skill separada na inteligência, mas corresponde à leitura inicial que embase toda a Semana 2. Pode ser o ponto de entrada para determinar qual UCM o cliente pertence. Integrar como pré-requisito do fluxo |
| `ee-s2-diagnostico-criativos` | Diagnóstico de criativos existentes (serve tanto UCM 2 como UCM 1) | **MANTER e ITERAR** — já listada em #12 da tabela principal |

---

## 5. Resumo do Backlog

| Status | Quantidade | Skills |
|--------|-----------|--------|
| **USAR** | 1 | `cliente-oculto` (#19) → `ee-s4-cliente-oculto` |
| **ITERAR** | 17 | #1→`ee-s2-pesquisa-mercado` / #2→`ee-s2-pesquisa-mercado` / #3→`ee-s1-persona-icp` / #4→`ee-s1-persona-icp` / #5→`ee-s1-persona-icp` / #6→`ee-s1-swot` / #7→`ee-s2-posicionamento` / #8→`ee-s2-diagnostico-midia` / #9→`ee-s2-diagnostico-midia` / #10→`ee-s2-diagnostico-midia` / #12→`ee-s2-diagnostico-criativos` / #14→`ee-s1-auditoria-comunicacao` / #15→`ee-s2-diagnostico-cro` / #16→`ee-s2-diagnostico-cro` / #17→`ee-s2-diagnostico-cro` / #18→`ee-s4-diagnostico-comercial` / #22→`ee-s3-forecast-midia` |
| **CRIAR** | 8 | #11 `plano-de-acao-5w2h` / #13 `benchmarking-anuncios` / #20 `gtm-priorizacao-canais` / #21 `drawflow-estrategia-aquisicao` / #23 `deck-semana-estruturacao` / #24 `deck-entrega-final` / #25 `diagnostico-travas-scoring` / #26 `analise-crm-receita` |
| **Fora do escopo** | 8 | `landing-page` / `identidade-visual` / `brandbook` / `crm-setup` / `copy-anuncios` / `gmb-otimizacao` / `scripts-sdr` / `sdr-ia-config` |
| **Infraestrutura** | 6 | `novo-cliente` / `continuar` / `onboarding` / `adicionar-base` / `duvida` / `feedback` |

---

## 6. Prioridade de Execução do Backlog

### Alta — impacto em 100% dos projetos

| Prioridade | Ação | Skill | Justificativa |
|-----------|------|-------|---------------|
| 🔴 1 | CRIAR | `deck-semana-estruturacao` (#23) | Principal entregável de cada semana — sem ela o output do produto não existe como deck |
| 🔴 2 | CRIAR | `deck-entrega-final` (#24) | Principal entregável do produto inteiro — consolida tudo em narrativa para diretoria |
| 🔴 3 | CRIAR | `diagnostico-travas-scoring` (#25) | Padrão visual mais impactante dos entregáveis reais (Devstate) — qualifica o diagnóstico |
| 🔴 4 | CRIAR | `gtm-priorizacao-canais` (#20) | Presente em 100% dos projetos; slide de GTM é high-stakes para o cliente |
| 🔴 5 | ITERAR | `ee-s2-pesquisa-mercado` → `sizing-mercado-tam-sam-som` + `estudo-concorrentes` | Separar em 2 skills distintas e adicionar: parâmetro moeda, Meta Ads Library obrigatório, tipo_concorrente |

### Média — diferencial de qualidade do diagnóstico

| Prioridade | Ação | Skill | Justificativa |
|-----------|------|-------|---------------|
| 🟡 6 | ITERAR | `ee-s1-persona-icp` → B2B/B2C separados + JTBD 4 camadas | Comitê de compra e Jobs Sociais são diferenciais que outros players não entregam |
| 🟡 7 | CRIAR | `plano-de-acao-5w2h` (#11) | Reutilizável em 4 POPs — economiza tempo de Account e GT |
| 🟡 8 | ITERAR | `ee-s4-diagnostico-comercial` → auditoria CRM + LRT + Hunter/Farmer | Diagnóstico comercial é o "choque de realidade" mais impactante do produto |
| 🟡 9 | ITERAR | `ee-s3-forecast-midia` → UCM 1 mode + engenharia reversa | Maior impacto na renovação/LTV do produto |
| 🟡 10 | CRIAR | `drawflow-estrategia-aquisicao` (#21) | Visualiza a estratégia GTM — alto impacto no cliente |

### Normal — complementam e aprofundam

| Prioridade | Ação | Skill | Justificativa |
|-----------|------|-------|---------------|
| 🟢 11 | ITERAR | `ee-s1-swot` → adicionar Beachhead Market | Beachhead é o link entre SWOT e posicionamento — hoje o link está quebrado |
| 🟢 12 | ITERAR | `ee-s2-posicionamento` → 3 variações PUV (Ganho/Medo/Lógica) | Padrão observado em todos os entregáveis reais |
| 🟢 13 | CRIAR | `benchmarking-anuncios` (#13) | Separa moodboard de competição do diagnóstico de criativos |
| 🟢 14 | CRIAR | `analise-crm-receita` (#26) | Segmentação por fluxo de receita é diferencial do produto em clientes multi-produto |
| 🟢 15 | ITERAR | `ee-s2-diagnostico-midia` → separar Meta / Google / Eficiência | Auditorias específicas por plataforma são mais úteis que uma skill genérica |

---

*De-para gerado com base em leitura das 26 SKILL.md existentes + 26 skills mapeadas na inteligência.*
