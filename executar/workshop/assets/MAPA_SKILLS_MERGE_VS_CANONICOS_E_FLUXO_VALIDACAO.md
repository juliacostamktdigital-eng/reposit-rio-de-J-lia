# Mapa: skills `merge` × assets `canonicos` + fluxo de validação

**Atualizado:** 2026-04-30  
**Fonte:** inventário `assets/legacy/merge` e `assets/canonicos`; consolidação final em `assets/canonicos`; README `canonicos`; leitura cruzada skills merge × docs canônicos; incorporação V01 em `12_BENCHMARK_...`; validação formal V02 merge × `13_DOSSIE_...`; merge final V01–V16 em `assets/canonicos/`.

---

## 0. Estado da incorporação (feito / pendente) e método de junção

### 0.1 O que já foi feito

| Item | Detalhe |
|------|---------|
| **V01 — Benchmark** | Conteúdo de `assets/legacy/merge/skills/01-benchmarking-estudo-mercado.md` **fundido** em `canonicos/12_BENCHMARK_MERCADO_TAM_SAM_SOM_CANONICO.md` (2026-04-30). O canônico passou a incluir fluxo de 7 passos, § quando usar/não usar, inputs mínimos operacionais, mapa do campo de batalha, DoD operacional + N2 unificados, gestão contínua (KPIs/semáforo/cadência/changelog), remoção da “lacuna” de ferramentas em favor de orientação explícita, e metadados **Atualizado** / **Fonte** no topo do `12_`. |
| **Skill merge 01** | Mantida como espelho com **nota de redirecionamento** no topo: alterações futuras devem ocorrer no `12_...` para evitar divergência. |
| **README canônicos** | Entrada do índice do arquivo `12_...` atualizada mencionando incorporação da skill merge. |
| **Este mapa (seção 4)** | V01 registrado como **Incorporado**; V02 como **Aprovado com ressalvas**; histórico de gap analysis preservado como contexto das decisões. |
| **V02 — Documento de comunicação** | Validação cruzada `02-documento-comunicacao-ucm-dcc.md` × `13_DOSSIE_ESTRATEGICO_OFERTA_COMUNICACAO_CANONICO.md` (contexto `10`/`04` conforme README) concluída **2026-04-30**. Status anterior: **Aprovado com ressalvas**. Na consolidação final em `canonicos`, a skill `02_` foi incorporada ao `13_` como roteiro operacional do DEOC. |
| **V03–V16 — Consolidação final** | Conteúdo operacional das demais skills incorporado em `assets/canonicos/` seguindo a matriz da seção 1: casos 1:1 preservados, casos N:1 consolidados por domínio e casos 1:N divididos por responsabilidade. |
| **Templates** | `assets/canonicos/templates/` criado com os 8 templates oficiais; `assets/legacy/merge/templates` fica redundante/histórico. |
| **README canônicos** | Atualizado para apontar `canonicos/` como fonte final consolidada dos playbooks reescritos. |

### 0.2 O que ainda não foi feito

| Área | Pendência |
|------|-----------|
| **V03–V16** | Resolvido em `assets/canonicos/`; cada skill foi incorporada, distribuída ou consolidada conforme a matriz final. |
| **Bloco transversal** | Resolvido em `assets/canonicos/`; canônicos sem skill dedicada foram copiados/revisados com metadado de fonte final e papel transversal. |
| **`assets/legacy/merge/templates` × `assets/canonicos/templates`** | Resolvido em `assets/canonicos/templates/`; os 8 templates oficiais foram consolidados a partir de `assets/canonicos/templates`. |
| **`workflow.knowledge-os.v1.json`** | Não alterado por ser referência v1; a fonte documental final desta task é `assets/canonicos/`. |
| **Demais skills merge** | Não precisam permanecer como fonte ativa; `assets/legacy/merge/skills` passa a ser origem histórica do merge. |

### 0.3 Método de junção (reutilizável)

Objetivo: trazer **tudo o que a merge acrescenta** (curadoria operacional, passos, DoD, gestão) para dentro do **arquivo canônico âncora**, **sem apagar** o que o canônico já exige para N2/N3 ou para auditoria, e **eliminando redundância** (um conceito, um lugar).

1. **Mapear pares**  
   Usar a tabela da seção 1 (skill merge → doc(s) canônico(s)). Se um par for N:1 (ex.: uma merge, dois canônicos), decidir **um âncora** e referenciar o outro no texto.

2. **Ler os dois arquivos por completo**  
   Anotar: blocos exclusivos da merge; blocos exclusivos do canônico; sobreposições (mesmo significado, redação diferente).

3. **Definir esqueleto do canônico pós-junção**  
   Manter a ordem lógica do canônico (princípio → inputs → estrutura entregável → N2/N3 → evitar). Inserir blocos da merge onde fizer sentido sem duplicar título:  
   - “Quando usar / não usar” → fundir com “quando produzir” em uma seção de **momento na jornada + anti-padrões**.  
   - “Passo a passo” → seção **fluxo de execução** antes ou intercalado com a **estrutura canônica** (entregáveis), com referência cruzada (“a etapa 3 do fluxo alimenta o §6.3”).  
   - “DoD” da merge → **checklist operacional** alinhado ao **N2** (checklist obrigatório ou justificativa N/A).  
   - “Gerenciado” → **gestão contínua** (KPI, semáforo, cadência, dono, registro).  
   - Lacunas declaradas na merge (“ferramentas não padronizadas”) → transformar em **orientação normativa** ou encaminhamento explícito, não deixar como desculpa vazia.

4. **Resolver redundância**  
   - Se o canônico já diz o mesmo com mais rigor: **manter o canônico** e absorver só frases da merge que agregam nuance ou exemplo.  
   - Se a merge diz algo que o canônico não diz: **incluir** no lugar mais próximo da estrutura.

5. **Renumerar seções**  
   Após inserções, **renumerar** todo o documento canônico para leitura linear estável.

6. **Metadados e índice**  
   No canônico: **Atualizado**, **Fonte** (citando merge + origens anteriores). No `canonicos/README.md`: uma linha no índice se o título ou escopo mudar de forma relevante.

7. **Espelho merge**  
   No arquivo em `assets/legacy/merge/skills/`: aviso no topo apontando para o canônico como **fonte única**; opcional manter corpo como leitura offline.

8. **Registrar neste mapa**  
   Na seção 4: **Status = Incorporado** + uma linha **Decisão**; atualizar seções **0.1 / 0.2** deste arquivo.

**Critério de parada:** o canônico âncora, lido sozinho, cobre o trabalho que a skill merge pedia **e** mantém (ou estende) critérios N2/N3 e estrutura obrigatória que já existiam.

---

## 1. Relação skills `legacy/merge/skills` → assets `canonicos`

Legenda da coluna **Encaixe:** alinhamento temático entre skill merge e canônico; o valor **Incorporado** indica que a merge foi **fundida** no canônico da coluna anterior (ver seção 0). A coluna **Notas** traz contexto ou pendências.

| # merge | Arquivo merge | Asset(s) canônico(s) principal(is) | Encaixe | Notas |
|--------:|---------------|-------------------------------------|---------|-------|
| 01 | `01-benchmarking-estudo-mercado.md` | `12_BENCHMARK_MERCADO_TAM_SAM_SOM_CANONICO.md` | **Incorporado** (2026-04-30) | Conteúdo da merge unificado no `12_`; skill merge com nota de redirecionamento. |
| 02 | `02-documento-comunicacao-ucm-dcc.md` | `13_DOSSIE_ESTRATEGICO_OFERTA_COMUNICACAO_CANONICO.md` **(primário)**; `10_PLANEJAMENTO_ESTRATEGICO_UCM_CANONICO.md`; `04_DOCUMENTO_COPY_FINAL_DCC_CANONICO.md` | Merge = legado UCM+DCC; canônico = DEOC + legados | README canônico: DEOC substitui UCM+DCC como fonte única; usar 10 e 04 só como contexto/histórico. **Validação 2026-04-30:** aprovado com ressalvas (seção 4); sem incorporação no `13_`. |
| 03 | `03-plano-midia-estrategia-canais-campanhas.md` | `03_PLANO_DE_MIDIA_CANONICO.md` | 1:1 | Canônico: investimento, cadência, metas, risco. |
| 04 | `04-funil-unificado-a2.md` | `17_FUNIL_UNIFICADO_CONVERSOES_A2_CANONICO.md` | 1:1 (A-2) | |
| 05 | `05-protocolo-handoff-a4.md` | `18_PROTOCOLO_HANDOFF_MQL_SQL_A4_CANONICO.md` **(primário)**; `07_CRM_HANDOFF_SLA_MARKETING_VENDAS_CANONICO.md` | A-4 + CRM/SLA | Doc 07 complementa 18 (README canônico). |
| 06 | `06-jornada-lead-raci.md` | `19_JORNADA_LEAD_RACI_CANONICO.md` | 1:1 | |
| 07 | `07-empacotamento-oferta.md` | `13_DOSSIE_ESTRATEGICO_OFERTA_COMUNICACAO_CANONICO.md` **(seção oferta)**; `12_BENCHMARK_MERCADO_...` (contexto) | Subconjunto do DEOC / benchmark | Merge é focado “boa o suficiente”; canônico 13 é mais amplo (oferta + comunicação). |
| 08 | `08-banco-tipos-criativos.md` | `20_BANCO_TIPOS_CRIATIVOS_CANONICO.md` | 1:1 + `templates/tipo-criativo.md` | Ambos pastas têm o mesmo template em `templates/`. |
| 09 | `09-briefing-pack-producao-criativos-e-conversao.md` | `05_BRIEFING_CRIATIVO_VIDEO_FIRST_CANONICO.md`; `08_LP_PONTO_DE_CONVERSAO_CANONICO.md`; opcional `06_ASSETS_ESQUECIDOS_E_BACKLOG_CANONICO.md` | Merge agrega briefing + “ambiente de conversão” | Canônicos separam briefing (05) e LP/ponto de conversão (08); 06 cobre gaps operacionais. |
| 10 | `10-estrutura-campanhas-meta-ads.md` | `15_SETUP_CAMPANHAS_META_ADS_CANONICO.md` | Skill “guarda-chuva” Meta | Um canônico cobre conta, pixel/CAPI, públicos, estrutura, go-live. |
| 10-1 | `10-1-meta-lead-nativo.md` | `15_SETUP_CAMPANHAS_META_ADS_CANONICO.md` (objetivo lead) | Subtipo Meta | Validação: checar seção/objetivo no 15. |
| 10-2 | `10-2-meta-conversao.md` | `15_SETUP_CAMPANHAS_META_ADS_CANONICO.md` (objetivo conversão) | Subtipo Meta | Idem. |
| 10-3 | `10-3-meta-engajamento.md` | `15_SETUP_CAMPANHAS_META_ADS_CANONICO.md` (objetivo engajamento) | Subtipo Meta | Idem. |
| 11 | `11-estrutura-campanhas-google-ads-search.md` | `16_SETUP_CAMPANHAS_GOOGLE_ADS_CANONICO.md` (Search) | Subtipo Google | Um canônico cobre Search + PMax + Display + conversões etc. |
| 12 | `12-estrutura-campanhas-google-ads-pmax.md` | `16_SETUP_CAMPANHAS_GOOGLE_ADS_CANONICO.md` (PMax) | Subtipo Google | |
| 13 | `13-estrutura-campanhas-google-ads-display.md` | `16_SETUP_CAMPANHAS_GOOGLE_ADS_CANONICO.md` (Display) | Subtipo Google | |

### 1.1 Templates `assets/legacy/merge/templates` ↔ `assets/canonicos/templates`

Nomes alinhados (espelho): `asset-skill.md`, `estrutura-campanha-*.md`, `pack-producao.md`, `processo-loop.md`, `tipo-criativo.md`. Diff de conteúdo: comparar arquivo a arquivo; o canônico é a pasta “fonte oficial” segundo `canonicos/README.md`.

### 1.2 Canônicos sem skill dedicada em `legacy/merge/skills`

Estes assets existem só em `canonicos` (ou são transversais); entram no fluxo como **pré-requisito**, **pós-condição** ou **paralelo** à coluna merge:

| Asset canônico | Papel sugerido no fluxo |
|----------------|-------------------------|
| `00_MAPA_ASSETS_AI_NATIVE_PONTA_A_PONTA.md` | Mapa da jornada; referência antes/durante qualquer etapa. |
| `01_TAXONOMIA_UTM_IDS_E_SUBPARAMETROS.md` | Antes ou junto com mídia/tracking; não há skill merge equivalente. |
| `02_PLANILHA_DE_TESTES_GROWTH_CANONICA.md` | Paralelo à execução/testes; não há skill merge. |
| `06_ASSETS_ESQUECIDOS_E_BACKLOG_CANONICO.md` | Checklist transversal; especialmente perto de 09 e go-live. |
| `09_CONTRATO_DADOS_MKT_CRM_BACKUP_UTMS_CANONICO.md` | Entre funil/handoff e operação de mídia/CRM. |
| `11_HANDOFF_OPERACIONAL_EXECUTAR_CANONICO.md` | Entrada EXECUTAR / pacote inicial ops. |
| `14_CATALOGO_OFICIAL_ASSETS_JORNADA_CANONICO.md` | Inventário oficial de assets; útil na decisão de pacote v1. |

---

## 2. Fluxo de execução (merge como “skills canônicas” + canônicos como fonte completa)

**Princípio:** cada **skill merge** é o **artefato operacional** que você valida (tom de voz, passos, outputs). O **canônico** correspondente é a **fonte da verdade** para amplitude, definition of done, evidência N2/N3 e relação com a jornada AI-native.

**Regra de decisão por etapa:**

1. Ler o(s) canônico(s) da linha da tabela (seção 1).
2. Executar / revisar a skill merge como “prompt de trabalho”.
3. Registrar lacunas: o que o merge tem a mais (curadoria) vs o que só o canônico cobre.
4. **Aprovar** a skill merge se: (a) não contradiz o canônico; (b) outputs da merge são um subconjunto aceitável ou podem ser mapeados para seções do canônico; (c) lacunas críticas do canônico estão explícitas (para complementar depois).

**Ordem sugerida para você validar “uma por uma”** (alinhada à progressão estratégica → mídia → criativo):

| Ordem validação | Skill merge | Canônico “âncora” |
|----------------:|-------------|-------------------|
| V01 | `01-benchmarking-estudo-mercado.md` | `12_BENCHMARK_...` **✓ incorporado** |
| V02 | `02-documento-comunicacao-ucm-dcc.md` | `13_DOSSIE_...` (+ 10, 04 se necessário) **✓ validado (ressalvas)** |
| V03 | `07-empacotamento-oferta.md` | `13_DOSSIE_...` (oferta) |
| V04 | `03-plano-midia-estrategia-canais-campanhas.md` | `03_PLANO_DE_MIDIA_...` |
| V05 | `04-funil-unificado-a2.md` | `17_FUNIL_...` |
| V06 | `06-jornada-lead-raci.md` | `19_JORNADA_...` |
| V07 | `05-protocolo-handoff-a4.md` | `18_PROTOCOLO_...` + `07_CRM_...` |
| V08 | `09-briefing-pack-producao-criativos-e-conversao.md` | `05_BRIEFING_...` + `08_LP_...` |
| V09 | `08-banco-tipos-criativos.md` | `20_BANCO_...` |
| V10 | `10-estrutura-campanhas-meta-ads.md` | `15_SETUP_META_...` |
| V11 | `10-1-meta-lead-nativo.md` | `15_SETUP_META_...` |
| V12 | `10-2-meta-conversao.md` | `15_SETUP_META_...` |
| V13 | `10-3-meta-engajamento.md` | `15_SETUP_META_...` |
| V14 | `11-estrutura-campanhas-google-ads-search.md` | `16_SETUP_GOOGLE_...` |
| V15 | `12-estrutura-campanhas-google-ads-pmax.md` | `16_SETUP_GOOGLE_...` |
| V16 | `13-estrutura-campanhas-google-ads-display.md` | `16_SETUP_GOOGLE_...` |

**Bloco transversal (validação separada ou após V04–V07):**  
`01_TAXONOMIA_UTM`, `09_CONTRATO_DADOS`, `02_PLANILHA_TESTES`, `14_CATALOGO`, `06_ASSETS_ESQUECIDOS`, `11_HANDOFF_OPERACIONAL_EXECUTAR`, `00_MAPA` — não têm par merge 1:1; definem se o “pacote” está fechado para operação.

---

## 3. Como registrar aprovação (sugestão)

Para cada **Vxx**, anotar: **Aprovado / Aprovado com ressalvas / Reprovado / Incorporado**, 1–2 linhas de motivo, e links ou âncoras de seção no canônico que faltam na merge (ou vice-versa). Quando todas as V01–V16 + bloco transversal estiverem decididas, o merge fica “certificado” contra o barco canônico sem substituí-lo.

**Incorporado:** use quando o conteúdo da skill merge foi **fundido** no canônico âncora; em seguida atualizar a **seção 0** deste mapa e seguir o **método da seção 0.3**.

---

## 4. Registro de validação (preenchimento incremental)

### V01 — `01-benchmarking-estudo-mercado.md` × `12_BENCHMARK_MERCADO_TAM_SAM_SOM_CANONICO.md`

**Status:** Incorporado — 2026-04-30 (conteúdo da merge fundido no canônico `12_...`; merge mantida com nota de redirecionamento)

**O que a merge cobre bem (alinha ao 12):**

- Propósito e anti-padrões (“benchmark sem evidência”, não virar pesquisa infinita).
- Entradas mínimas de contexto e canais; passos de coleta por concorrente (comunicação, criativos, LPs, campanhas) alinhados à ordem de análise do §5.3 do canônico.
- Consolidação em padrões, matriz força/fraco, decisão baseline vs diferenciação, backlog de hipóteses com métrica.
- DoD operacional (amostra, evidências, bullets acionáveis, decisões explícitas).
- Bloco “Gerenciado” (KPIs, thresholds, cadência) — o canônico expressa parte disso em N2/N3 e “o que evitar”.

**O que só o canônico exige (lacunas da merge vs N2 / estrutura §5):**

- **TAM/SAM/SOM** com tabela obrigatória, regra do SOM (capacidade × budget × CPL) e fontes/ano/método — ausente na skill merge.
- **Contexto de mercado** formal (maturidade, sazonalidade, tendências, regulatório) — merge só tangencia via escopo.
- **Ruído de mercado** (promessas saturadas) — não nomeado na merge.
- **Mapa competitivo 2x2** — não pedido na merge.
- **SWOT específica** (regra anti-genérica + evidência/impacto/implicação) — não na merge.
- **Beachhead** com scorecard — não na merge.
- **Inputs** canônicos: handoff EXECUTAR, plano de ROI, diagnóstico GTM, budget, capacidade — a merge lista inputs “mínimos” mais leves; desalinhamento de **quando produzir** (canônico: depois de handoff + diagnóstico + discovery; merge: “onboarding antes de plano de mídia”).
- **Fontes:** canônico cita Meta Ads Library, Google/SERP, ordem explícita; merge declara lacuna de padronização de ferramentas.
- **N2/N3** explícitos no 12 — merge não referencia N2/N3 nem implicações formais para “pacote de assets v1”.

**Decisão registrada:** incorporação total da skill merge no canônico (substituição de redundâncias, preservação do fluxo de 7 passos, DoD operacional, gestão contínua e encaixe com N2).

### V02 — `02-documento-comunicacao-ucm-dcc.md` × `13_DOSSIE_ESTRATEGICO_OFERTA_COMUNICACAO_CANONICO.md`

**Status:** Aprovado com ressalvas — 2026-04-30 (validação cruzada; **não** incorporado — o `13_` já é o DEOC; `10_`/`04_` permanecem legado conforme README)

**O que a merge cobre bem (alinha ao DEOC):**

- Fronteira explícita com Plano de mídia (o que/para quem dizer vs onde/como operar), coerente com a função do DEOC como ponte para execução.
- Momento “antes de plano de mídia, brief, copy, criativos e LPs” compatível com o bloco “Antes de” do §3 do `13_`.
- Passos e outputs sobre ICP + anti-ICP operacional, persona(s), mensageria (promessa, provas, objeções, CTA), proposta de valor e regras de consistência — mapeiam para trechos do §5 (ex.: §5.3 ICP/persona, §5.6 proposta de valor, §5.7–5.8 narrativa/claims em parte).
- Nota operacional sobre ICP unificado (mídia × CRM × handoff MQL→SQL) — cola útil à jornada sem contradizer o canônico.
- DoD e bloco “Gerenciado” (KPIs, semáforo, cadência, changelog) como curadoria executável; o canônico formaliza N2/N3 e “o que evitar” em paralelo.

**O que só o canônico exige (lacunas da merge vs estrutura §4–§7):**

- **Nomenclatura:** merge usa “Documento de Comunicação (UCM + DCC)”; canônico fixa **DEOC** — risco de ruído para times e IA se não cruzar explicitamente com o `13_`.
- **Inputs obrigatórios §4:** handoff EXECUTAR, plano de ROI, transcrições (vendas, Growth Class), diagnóstico GTM, benchmark, TAM/SAM/SOM, beachhead, restrições jurídicas etc. — a merge lista apenas benchmark, contexto de produto e evidências internas (**subespecificação** para N2).
- **Quando produzir §3:** canônico exige handoff, diagnóstico GTM, benchmark/TAM/SOM e discovery **antes**; a merge enfatiza “antes da mídia” mas não reproduz a cadeia completa de pré-requisitos — risco de uso fora de ordem.
- **Estrutura §5 completa:** resumo estratégico, oferta/mecanismo (§5.2), problemas/VdC (§5.4), alternativas (§5.5), matriz §5.9 “tradução para execução” — não guiados pela merge (subconjunto).
- **N2/N3 explícitos** no `13_` — não citados na merge; quem usar só a skill precisa ler o canônico para evidência e maturidade do artefato.
- **Empacotamento de oferta:** já incorporado no DEOC final em `canonicos/13_...` a partir da skill merge `07_`; relevante para evitar UCM/DCC/oferta como trilhas paralelas.

**Decisão registrada:** status histórico anterior era **Aprovado com ressalvas**. Na consolidação final em `canonicos`, a skill `02_` foi incorporada ao DEOC `13_` como roteiro operacional; `10_`/`04_` permanecem legado/contexto e deixam de ser fonte ativa.

---

## 5. Consolidação final em `assets/canonicos`

**Status geral:** Incorporado — 2026-04-30.

| Bloco | Decisão final |
|------|---------------|
| V01 Benchmark | `01-benchmarking-estudo-mercado.md` consolidado em `12_BENCHMARK_MERCADO_TAM_SAM_SOM_CANONICO.md`. |
| V02 + V03 DEOC/Oferta | `02-documento-comunicacao-ucm-dcc.md` e `07-empacotamento-oferta.md` consolidados em `13_DOSSIE_ESTRATEGICO_OFERTA_COMUNICACAO_CANONICO.md`; `04_DCC` e `10_UCM` ficam legado/contexto. |
| V04 Plano de mídia | `03-plano-midia-estrategia-canais-campanhas.md` incorporado em `03_PLANO_DE_MIDIA_CANONICO.md`. |
| V05 Funil | `04-funil-unificado-a2.md` promovido em `17_FUNIL_UNIFICADO_CONVERSOES_A2_CANONICO.md`. |
| V06 + CRM/SLA | `05-protocolo-handoff-a4.md` mantido como âncora em `18_PROTOCOLO_HANDOFF_MQL_SQL_A4_CANONICO.md` e distribuído como complemento em `07_CRM_HANDOFF_SLA_MARKETING_VENDAS_CANONICO.md`. |
| V07 Jornada/RACI | `06-jornada-lead-raci.md` promovido em `19_JORNADA_LEAD_RACI_CANONICO.md`. |
| V08 Pack produção | `09-briefing-pack-producao-criativos-e-conversao.md` dividido entre `05_BRIEFING...`, `08_LP...` e gaps em `06_ASSETS...`. |
| V09 Banco criativos | `08-banco-tipos-criativos.md` promovido em `20_BANCO_TIPOS_CRIATIVOS_CANONICO.md`; template oficial em `templates/tipo-criativo.md`. |
| V10–V13 Meta Ads | `10`, `10-1`, `10-2`, `10-3` consolidados em `15_SETUP_CAMPANHAS_META_ADS_CANONICO.md`. |
| V14–V16 Google Ads | `11`, `12`, `13` consolidados em `16_SETUP_CAMPANHAS_GOOGLE_ADS_CANONICO.md`. |
| Transversais | `00`, `01`, `02`, `06`, `09`, `11`, `14` copiados/revisados em `` como pré-requisitos, checklists ou fontes de evidência. |
| Templates | 8 templates oficiais consolidados em `templates/`; `assets/legacy/merge/templates` fica redundante. |

**Critério de fonte única:** para uso operacional daqui em diante, ler `assets/canonicos/README.md` e os arquivos em `assets/canonicos/`; `assets/legacy/merge/skills` permanece apenas como origem histórica da redação operacional incorporada.

### 5.1 Revisão individual pós-merge mecânico

**Status:** Revisado item a item — 2026-04-30.

Após a primeira consolidação, foi feita uma segunda passada editorial para evitar `canônico + apêndice da skill`. As decisões finais foram:

- V01: manter `12_` como canônico profundo; limpar metadados e referências de template.
- V02: absorver a skill `02_` dentro do DEOC, sem manter “Documento de Comunicação” como trilha paralela.
- V03: absorver empacotamento de oferta em oferta/mecanismo, proposta, claims, N2/N3 e tradução para execução.
- V04: absorver a skill `03_` no plano de mídia, especialmente inputs, canais, estrutura de campanhas, tracking, guardrails, N2 e N3.
- V05/V06/V09: manter skills já promovidas em `17_`, `19_` e `20_`, com limpeza editorial.
- V07: manter split `18_` como protocolo A-4 e `07_` como CRM/SLA, removendo duplicação do protocolo dentro do CRM.
- V08: manter split em `05_` (criativo), `08_` (conversão) e `06_` (gaps), sem criar playbook guarda-chuva duplicado.
- V10–V13: integrar Meta Ads por subtipo dentro de `15_`, removendo apêndice colado das skills.
- V14–V16: integrar Search, PMax e Display dentro de `16_`, com Display como cobertura própria e sem apêndice colado.

**Critério aplicado:** um conceito, um lugar. Quando a skill era mais profunda no operacional, o conteúdo entrou na seção do playbook correspondente; quando o canônico era mais profundo em auditoria/N2/N3, ele foi preservado.
