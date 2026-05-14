# CHANGELOG — ee-s4-diagnostico-comercial

---

## [1.2.0] — 2026-05-07 — MINOR

**Contexto:** Revisão do output piloto (Alisson Joias) revelou que conclusões de diagnóstico estavam sendo fundamentadas em declarações de kick-off e briefing — fontes de contexto (Tier 2), não de evidência (Tier 1). Diagnóstico baseado em percepção do cliente sobre seu próprio processo não tem validade consultiva.

**O que mudou:**

### Adicionado
- **Hierarquia de fontes formalizada:**
  - Tier 1 (evidência): CSV de CRM, screenshots de conversas, exports, cliente oculto, transcrições reais
  - Tier 2 (contexto): kick-off, briefing, declarações do gestor
- Regra: kick-off/briefing validam causa mas não geram conclusões diagnósticas independentes
- Marcação obrigatória `[Fonte: Tier 2 — validar com dado Tier 1]` quando apenas declaração disponível
- Seção 2.5 (Hunter/Farmer): passa a exigir dados de conversão por canal como única base quantitativa — declarações de perfil não qualificam

### Modificado
- Seções 2.2–2.5 revisadas: declarações de kick-off não mais aceitas como evidência de diagnóstico nessas seções
- Seção 2.5 (Hunter/Farmer): critério de evidência endurecido — Win Rate por canal de origem ou por consultora, não perfil declarado

### Não modificado
- Escopo: relatório diagnóstico puro (sem plano de ação, sem objeções, sem critérios de qualificação)
- Benchmarks com referências inline obrigatórias
- 5 seções diagnósticas: funil, higiene CRM, processo real vs declarado, análise de calls, Hunter/Farmer
- Output: `ee-s4-diagnostico-comercial.md`

---

## [1.1.0] — 2026-05-07 — MINOR

**Contexto:** Escopo da skill estava misturado com elementos de skills subsequentes (objeções, qualificação, plano de ação), tornando o output denso e difícil de usar como input para outras skills.

**O que mudou:**

### Adicionado
- Diagnóstico de higiene do CRM (campos em branco, atribuição de origem, SLA por temperatura)
- Análise de processo real vs declarado (o que a empresa diz que faz vs o que o cliente oculto evidencia)
- Perfil Hunter/Farmer por canal de origem e por consultora
- Análise de calls/transcrições de atendimento
- Benchmarks com referências inline obrigatórias (fonte + ano + link quando disponível)

### Removido
- Mapa de objeções → movido para skill subsequente de scripts
- Critérios de qualificação 1–5 estrelas → movido para skill de qualificação/BANT
- Plano de ação → movido para `/plano-de-acao-5w2h`

### Modificado
- Output: de `.json` para `.md`
- Escopo redefinido: relatório diagnóstico puro

---

## [1.0.0] — 2026-01-01

Versão inicial. Funil de vendas, mapa de objeções, critérios de qualificação 1–5 estrelas e plano de ação em um único documento. Output em `.json`.
