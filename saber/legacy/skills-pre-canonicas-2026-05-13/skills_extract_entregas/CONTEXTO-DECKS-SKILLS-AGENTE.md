# Contexto — Decks semanais, biblioteca de layouts e agente (EE)

**Escopo:** produto EE (Estruturação Estratégica / Diagnóstico e Planejamento de Marketing e Vendas), alinhado a `entegas_exemplos/`, skills em `skills/` e ao racional já descrito em `de-para-skills.md` (incl. `deck-semana-estruturacao`, `deck-entrega-final`).

**Tese:** combinar (1) **quatro decks semanais** que exercitem, como *golden paths*, uma **tipologia finita** de slides — determinísticos e não determinísticos — com (2) uma **biblioteca de layouts validados** e um **registry** skill → slide(s), orquestrados por (3) um **agente conversacional**, no qual o **utilizador humano é o direcionador** do “sistema operativo” (quais skills, que profundidade, que semana, que modo de entrega).

**Referências no repositório:**

| Recurso | Caminho / nota |
|--------|------------------|
| De-para skills × gaps | `de-para-skills.md` |
| Exemplos reais de entrega | `entegas_exemplos/` (pastas `01`–`05`, PDFs + MDs) |
| Skills analíticas | `skills/v4-diagnostico-planejamento/`, `skills/v4-estruturacao-marketplace-main/` |
| Deck HTML + JSON | `../../.claude/skills/relatorio-deck-html/` (ex.: `references/SCHEMA-DECK.md`, `ESTRUTURA-SEMANTICA-PPTX.md`) |
| PPTX nativo | `../../.claude/skills/pptx/` (PptxGenJS, edição OOXML, QA) |

---

## 1. Objetivo em duas frentes (não são excludentes)

### 1.1 Quatro decks semanais (*golden paths*)

- **Uma versão de deck por semana** (ciclo de 4 semanas do produto), cada uma cobrindo o **conjunto mínimo de skills** daquela fase **e** forçando a aparição dos **arquétipos de slide obrigatórios** da semana.
- Objetivo: não “explorar todas as combinações do universo”, e sim **cobrir 95% dos padrões** que já aparecem nos PDFs de `entegas_exemplos/` com **roteiros fixos e auditáveis**.

### 1.2 Biblioteca paralela de layouts + registry skill → slide(s)

- **Layouts semi-determinísticos:** estrutura fixa (títulos, zonas, tabelas, gráficos), conteúdo vindo de schema/JSON.
- **Layouts pouco ou nada determinísticos:** áreas “livres” (narrativa, interpretação, recomendação) com **limites** (caracteres, altura máxima, política de overflow = resumir).
- **Registry:** cada `skill_id` mapeia para **um ou mais** `{ layout_id, papel, campos obrigatórios/opcionais }` — uma skill pode gerar **vários slides** (ex.: dados brutos → interpretação → recomendação).

### 1.3 Agente conversacional

- Interface única para: escolher **semana**, **objetivo**, **subconjunto de skills**, **modo de saída**, **regerar slide X**, **refinar texto livre**.
- O agente implementa **orquestração**; não substitui o **modelo de conteúdo** nem a **biblioteca de layouts** — apenas encadeia e aplica políticas.

---

## 2. O utilizador como “Direcionador” do OS

O humano **define intenção e prioridades**; o sistema propõe skills, ordem, slides e artefactos. Exemplos de **direcionamento** (linguagem natural → política):

| Intenção do direcionador | O que o sistema resolve |
|--------------------------|-------------------------|
| “Deck completo da **semana 3**, cliente X.” | DAG da semana 3, registry, capa/índice/footer, limites de slides livres. |
| “Só **diagnóstico Meta Ads** + **5W2H**, formato comité.” | Duas skills, layouts mínimos + slide executivo; sem puxar forecast. |
| “Substitui o slide de **scoring** pelo modelo Devstate; mantém o resto.” | `layout_id` específico, re-render só desse bloco a partir do mesmo JSON. |
| “Este bloco é **100% narrativa** — sem campos fixos.” | `layout_id` tipo “livre” com caixa única e limite de caracteres. |
| “Quero **PPTX** para o cliente editar; eu revisto antes em **HTML**.” | Dois renderers: preview HTML → export PPTX (ver secção 7). |

**Princípio:** o direcionador **não precisa** escolher `layout_id` técnico — escolhe **objetivo e restrições**; o registry traduz para layouts. Opcionalmente, utilizadores avançados podem **forçar** template ou ordem.

---

## 3. Três camadas (evitar spaghetti no agente)

| Camada | O quê | Para quê |
|--------|--------|----------|
| **A. Modelo de conteúdo** | JSON/schema por skill: obrigatórios, opcionais, blocos `narrative` / `interpretation` / `free` | O **determinístico vs não determinístico** vive aqui, não no ficheiro PPT |
| **B. Biblioteca de layouts** | Slide masters validados: `.pptx` / `.potx` **ou** blocos HTML com contrato (ex. `ESTRUTURA-SEMANTICA-PPTX.md`) | Aspeto **estável** e **reutilizável** sem redesenhar cada entrega |
| **C. Orquestração** | Agente: semana, POPs, skills, inputs do cliente, modos de saída, regeneração | Escolhe **quais** arquétipos, **quantas** instâncias, **ordem** da história |

- **Skills** alimentam a camada **A**.  
- **Design/engineering** fecha a camada **B** e trata de regressão visual.  
- **Agente + direcionador** operam na camada **C**.

---

## 4. “Todas as possibilidades” = tipologia **finita** (~12–18 arquétipos)

Em vez de combinatória infinita, define-se um **catálogo** que cobre a maior parte dos PDFs em `entegas_exemplos/`:

| `layout_id` (exemplo) | Uso típico | Determinismo |
|----------------------|------------|--------------|
| `cover_v4` | Capa, tema, cliente, data | Alto |
| `agenda` | Índice / POPs da semana | Alto |
| `timeline` | Fases T+0…, marcos | Médio (datas variam) |
| `big_number` | KPI grande + label + interpretação curta | Médio |
| `two_column` | Problema / objetivo, antes / depois | Médio |
| `three_pillars` | Pilares, valores, eixos | Médio |
| `table` | Pricing, comparativos, marcos × % | Alto na grelha, médio no texto |
| `chart_bar` | Mix, funil simplificado | Médio (dados numéricos) |
| `matrix_2x2` | Posicionamento, concorrência | Médio |
| `scoring_dimensions` | 0–5 por dimensão + total (estilo Devstate) | Alto nos scores, médio na interpretação |
| `causal_one_liner` | Consolidação em uma frase | Baixo (texto) |
| `risks_next_steps` | Riscos + próximos passos | Baixo |
| `cta_close` | Decisão pedida, contacto | Médio |
| `freeform_box` | Narrativa / anexo / “só conteúdo direto” | Baixo (com limite de tamanho) |

- **Determinístico:** slots fixos (número, data, score, fonte).  
- **Não determinístico:** campos texto com **limite** e **layout já validado**; se ultrapassar → política de resumo ou divisão em segundo slide.

**Política global (exemplo):** máximo **N** slides `freeform_box` por semana; sempre um `risks_next_steps` antes do `cta_close` em modo “deck semanal completo”.

---

## 5. Os quatro decks como *golden paths* e `entegas_exemplos` como regressão

- **Semana N** = pacote mínimo de skills daquela semana (ver `de-para-skills.md` e POPs) **+** conjunto obrigatório de `layout_id` para essa semana.
- *Exemplo conceitual:* semana de diagnóstico força `table` + `chart_bar` + `scoring_dimensions`; semana de GTM força priorização (matriz ou tabela ICE) + `timeline` / fluxo.
- Os ficheiros em **`entegas_exemplos/`** funcionam como **bateria de testes narrativos e visuais**: qualquer layout novo deve “passar” num dos quatro roteiros sem sobrecarregar ou quebrar a história.

---

## 6. Registry: `skill_id` → slide(s)

Estrutura alvo (YAML/JSON no repo, mantido com o produto):

```yaml
# Exemplo ilustrativo — não é ainda contrato final
skill_id: diagnostico-meta-ads
slides:
  - layout_id: two_column
    role: findings_vs_evidence
    required: [top_issues, benchmarks_cited]
    optional: [screenshot_refs]
  - layout_id: table
    role: top_down_audit
    required: [campaign_adset_ad_notes]
  - layout_id: freeform_box
    role: recommendations_30d
    max_chars: 1200
```

- Uma skill → **vários slides** é regra esperada, não exceção.  
- O agente: resolve dependências entre skills (DAG) → expande o registry → aplica política global (capa V4, índice, footer, numeração).

---

## 7. `relatorio-deck-html` vs `pptx`: dois *renderers* do mesmo modelo

| Papel | Formato | Quando favorecer |
|--------|---------|------------------|
| Automação, PRD, preview, diff no Git | **HTML + JSON** (camada A + contrato B em HTML) | Equipa interna, iteração rápida, arquivo no repositório |
| Cliente edita no PowerPoint, template corporativo | **PPTX** (placeholders num `.potx` validado, ou geração via PptxGenJS / edição OOXML) | Entrega externa, comité, marca |

**Ideia-chave:** não competem — **o mesmo payload lógico** (camada A, eventualmente normalizado) alimenta **dois motores visuais**. O registry aponta para **semântica** de slide; cada motor sabe como desenhar essa semântica no seu medium.

---

## 8. Riscos a endereçar cedo

| Risco | Mitigação |
|-------|-----------|
| Duas fontes de verdade (skill em Markdown livre vs deck espera JSON) | **Um output estruturado por skill** (JSON ou front-matter + schema) como contrato oficial |
| *Layout drift* | Cada `layout_id` tem **snapshot** nos 4 decks semanais; alteração de layout = regressão explícita |
| Agente sem política | **Modos** explícitos: `modo_semana`, `modo_skill`, `modo_executive_summary`, com limites de slides e de texto livre |
| Utilizador perde controlo | Papéis claros: **direcionador** define objetivo; sistema propõe; confirmação antes de gerar PPTX final |

---

## 9. Exemplo end-to-end (ficcional)

**Direcionador:** “Semana 2 completa para o cliente PSM; quero destacar TAM/SAM/SOM e concorrentes; deck para comité em PPTX.”

1. Agente mapeia skills: `sizing-mercado-tam-sam-som`, `estudo-concorrentes`, … (DAG da semana 2).  
2. Cada skill produz **JSON** validado (camada A).  
3. Registry expande: `sizing-*` → `chart_bar` + `table` + `freeform_box` (premissas); `estudo-concorrentes` → `matrix_2x2` + `table` + interpretação.  
4. Render1: **HTML** para o direcionador rever no browser.  
5. Ajuste: “Encurta o slide 7 para metade do texto.” → alteração no JSON/bloco livre, re-render.  
6. Render 2: **PPTX** a partir do mesmo modelo (template validado).

---

## 10. Questões em aberto (formato ideal e iteração) — **para discussão**

Ainda **não há decisão fechada** no produto sobre os pontos abaixo. Cada opção tem trade-offs; a recomendação provável é **híbrido**, mas isso deve ser explicitamente escolhido.

### 10.1 Qual deve ser o formato “canónico” da entrega?

| Opção | Prós | Contras |
|-------|------|---------|
| **JSON** (camada A) como fonte de verdade | Diffável, regenerável, agente-friendly | Humanos não “apresentam” JSON; precisa sempre de renderer |
| **HTML** como fonte de verdade | Preview imediato, iteração rápida | PPTX derivado pode perder fidelidade se o contrato HTML→PPTX for frágil |
| **PPTX** como fonte de verdade | O que o cliente quer segurar | Difícil diff/merge; automação e agente trabalham pior |
| **Híbrido:** JSON canónico + HTML preview obrigatório + PPTX export | Melhor dos dois mundos para equipa + cliente | Dois pipelines a manter; disciplina de “não editar só o PPTX sem voltar ao JSON” |

**Discussão:** Para EE, o canónico deveria ser **JSON + schema** com HTML como preview padrão e PPTX como **export de entrega**, com regra explícita: alterações pós-export ou voltam ao JSON ou são aceites como “só cosméticas” (risco de deriva).

### 10.2 Como iterar e refinar slides específicos?

| Abordagem | Descrição | Quando faz sentido |
|------------|-----------|---------------------|
| **Refinar no PowerPoint** | Edição manual direta no `.pptx` | Último quilómetro, ajuste fino, comité urgente |
| **Refinar no HTML** | Ajustar conteúdo/estrutura no deck web e regenerar PPTX | Quando o contrato HTML→PPTX é maduro e fiável |
| **Refinar no JSON** | Corrigir dados, textos determinísticos, blocos livres com limites | **Ideal** para repetibilidade e para o agente aplicar “reescreve só o slide 5” |
| **Misto** | JSON para dados; PPTX só para “polimento” não modelado | Realista a curto prazo; exige política de o que pode ser mudado à mão |

**Discussão:** Sem disciplina, **PPTX vira silo** e o próximo *run* do agente **sobrescreve** ou **duplica** trabalho. Opções: (a) “PPTX final é *frozen* — novas versões só a partir do JSON”; (b) *round-trip* limitado (importar texto do PPTX de volta para JSON) — custo alto, raramente vale a pena na v1.

### 10.3 HTML → PPTX vs PPTX nativo desde o início?

| Abordagem | Prós | Contras |
|-----------|------|---------|
| **HTML → PPTX** (pipeline existente no `relatorio-deck-html`) | Um deck web único; export | Dependência de contrato semântico; edge cases de edição no Office |
| **PPTX nativo** (PptxGenJS / template) desde o início | Controlo fino OOXML; alinhado à skill `pptx` | Menos “preview web” gratuito; ligação a PRD/Git menos legível |
| **Ambos** (dois renderers) | Flexível | Manutenção dupla; exige mapa 1:1 `layout_id` → HTML **e** slide master |

**Discussão:** Para EE, **ambos** parecem desejáveis a médio prazo; na **v1** pode ser necessário **priorizar um** renderer para reduzir superfície (ex.: JSON + PPTX para entrega cliente, HTML opcional para interno).

### 10.4 O que o direcionador deve poder fazer sem tocar em ficheiros?

Exemplos de requisitos a validar com utilizadores:

- “Regenera só os slides da skill X.”  
- “Troca o layout do slide 4 para `scoring_dimensions`.”  
- “Aumenta o limite de caracteres do bloco livre do slide 9.”  
- “Exporta só PDF / só PPTX / pacote completo.”  

Isto implica **identidade estável de slide** (`slide_instance_id` ou `skill_id + role + index`) no modelo, não só “slide 4” frágil após reordenação.

---

## 11. Próximos passos sugeridos (produto / eng)

1. Congelar lista **v0** de `layout_id` (12–18) com base numa passagem **manual** por `entegas_exemplos/`.  
2. Definir **os quatro roteiros semanais** (lista de skills + layouts obrigatórios por semana).  
3. Esboçar **registry** para 5–10 skills piloto (as mais usadas no de-para).  
4. Decidir **formato canónico e política de iteração** (secção 10) numa sessão curta de ADR.  
5. Ligar o agente a **modos** (`modo_semana`, …) antes de crescer o catálogo de intents.

---

*Documento de contexto para alinhar produto, skills e agente. Revisões devem referenciar mudanças em `de-para-skills.md` e em exemplos em `entegas_exemplos/`.*
