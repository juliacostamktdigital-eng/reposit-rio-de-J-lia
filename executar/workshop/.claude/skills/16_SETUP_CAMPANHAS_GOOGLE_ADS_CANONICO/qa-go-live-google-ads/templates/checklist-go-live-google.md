# Checklist — QA go-live Google Ads (playbook 16)

**Cliente/projeto:**  
**Data da revisão:**  
**Revisor:**  
**Link plano de mídia:**  
**Link estrutura setup / JSON Google:**  
**Link planilha growth / backup:**  

**Decisão humana após o relatório:** ☐ Go ☐ No-go ☐ Condicional — notas:

---

## A. Princípio (Seção 1)

| ID | Pergunta / critério | ok / gap / n.a. | Notas |
|----|---------------------|-----------------|-------|
| p-01 | Conta e faturamento aptos a rodar verba | | |
| p-02 | Tag/GA4/GTM e conversões alinhadas ao objetivo de otimização | | |
| p-03 | Estrutura evita fragmentação excessiva vs orçamento | | |
| p-04 | Termos, URLs finais e assets coerentes com a oferta | | |
| p-05 | UTMs e `v4_*` previstos até backup/CRM | | |
| p-06 | Hipótese e plano de leitura registrados | | |

---

## B. Conta e stack (Seção 4)

| ID | Item | ok / gap / n.a. | Notas |
|----|------|-----------------|-------|
| c-01 | Conta Google Ads correta | | |
| c-02 | Faturamento ativo | | |
| c-03 | Permissões do time conferidas | | |
| c-04 | Auto-tagging avaliado | | |
| c-05 | GA4 vinculado quando aplicável | | |
| c-06 | GTM publicado e tag Google instalada | | |
| c-07 | Listas de remarketing elegíveis quando o plano exige | | |
| c-08 | Customer Match preparado quando houver base; senão n.a. | | |
| c-09 | Enhanced conversions avaliadas/ativas quando possível | | |

---

## C. Conversões (Seção 5)

| ID | Item | ok / gap / n.a. | Notas |
|----|------|-----------------|-------|
| cv-01 | Otimização na conversão mais profunda com volume viável (documentado) | | |
| cv-02 | Principais vs secundárias/observação diferenciadas quando aplicável | | |
| cv-03 | Importação offline MQL/SQL/venda planejada quando há CRM maduro | | |

---

## D. GTM e parâmetros (Seção 6)

| ID | Item | ok / gap / n.a. | Notas |
|----|------|-----------------|-------|
| g-01 | `gclid` preservado no fluxo | | |
| g-02 | `gbraid` / `wbraid` quando aplicável | | |
| g-03 | UTMs preservadas | | |
| g-04 | `v4_client_id`, `v4_campaign_id`, `v4_adgroup_id`, `v4_creative_id`, `v4_test_id` mapeados | | |
| g-05 | Campos hidden no formulário conforme contrato | | |
| g-06 | Planilha backup recebendo teste real | | |
| g-07 | CRM recebe ou há plano de conciliação | | |
| g-08 | Não publicar sem submissão real de lead testada | | |

---

## E. Nomenclatura e IDs (Seção 10)

| ID | Item | ok / gap / n.a. | Notas |
|----|------|-----------------|-------|
| n-01 | Campanhas com `campaign_id` na convenção | | |
| n-02 | Grupos/asset groups com `adgroup_id` | | |
| n-03 | Criativos/anúncios com `creative_id` | | |

---

## F. Negativas (Seção 11)

| ID | Item | ok / gap / n.a. | Notas |
|----|------|-----------------|-------|
| ng-01 | Lista inicial de negativas aplicável ao escopo | | |
| ng-02 | Cadência de revisão de termos (1ª semana / semanal inicial) definida | | |

---

## G. Orçamento e aprendizado (Seção 12)

| ID | Item | ok / gap / n.a. | Notas |
|----|------|-----------------|-------|
| o-01 | Orçamento compatível com aprendizado (sem micro-fragmentação injustificada) | | |
| o-02 | Sem mudanças grandes/diárias sem evidência | | |
| o-03 | Estratégia de lance/objetivo documentada para a fase (ex.: volume inicial) | | |

---

## H. Checklist antes do go-live (Seção 14)

| ID | Item | ok / gap / n.a. | Notas |
|----|------|-----------------|-------|
| gl-01 | Conversões testadas | | |
| gl-02 | Enhanced conversions avaliadas | | |
| gl-03 | UTMs e IDs aplicados | | |
| gl-04 | Lead teste na planilha backup | | |
| gl-05 | CRM recebeu ou será conciliado | | |
| gl-06 | Search com negativas iniciais | | |
| gl-07 | PMax com assets suficientes | | |
| gl-08 | Audience signals configurados (quando PMax no escopo) | | |
| gl-09 | Search: clusters, negativas e RSAs conferidos (quando aplicável) | | |
| gl-10 | PMax: asset groups, URL expansion, brand controls e metas conferidos (quando aplicável) | | |
| gl-11 | Display: placements/apps, frequência, exclusões e brand safety conferidos (quando aplicável) | | |
| gl-12 | URLs finais conferidas | | |
| gl-13 | Orçamento, lances e datas conferidos | | |
| gl-14 | Hipótese na planilha de growth | | |
| gl-15 | Change log preparado para mudanças relevantes | | |

---

## I. Critério N2 (Seção 15)

| ID | Item | ok / gap / n.a. | Notas |
|----|------|-----------------|-------|
| n2-01 | Conta e faturamento prontos | | |
| n2-02 | GTM/tag/conversões funcionando | | |
| n2-03 | UTMs e IDs aplicados | | |
| n2-04 | Estrutura Search/PMax (e Display se houver) documentada | | |
| n2-05 | Públicos/listas/sinais configurados conforme escopo | | |
| n2-06 | Planilha backup captura lead teste | | |
| n2-07 | Hipótese e critério de leitura registrados | | |

---

## J. Subtipos (subskills)

Marque no JSON: `subtipos.search|pmax|display` → `aplicavel` e `checklist_subskill_ok`.

| Canal | Subskill esperada |
|-------|-------------------|
| Search | `setup-google-search-leadgen` |
| PMax | `setup-google-pmax-leadgen` |
| Display | `setup-google-display-remarketing` |

---

## K. Anti-padrões (Seção 17)

No JSON: `anti_padroes[].detectado` = true/false.

| ID | Descrição |
|----|-----------|
| ap-01 | Campanha sem conversão testada |
| ap-02 | PMax sem asset decente |
| ap-03 | PMax sem audience signal |
| ap-04 | Marca e não-marca misturadas sem leitura separada |
| ap-05 | Otimizar para clique quando o objetivo é lead qualificado |
| ap-06 | Não importar/evoluir qualidade offline quando o funil exige |
| ap-07 | Search sem negativas |
| ap-08 | Alterar budget/lance todo dia sem evidência |
| ap-09 | Lead sem planilha backup |
| ap-10 | Avaliar Google só por CPL sem MQL/SQL |
| ap-11 | Display como “sobra de verba” sem função, exclusões, frequência ou brand safety |

---

## L. Gaps bloqueadores e ações (livre)

Registrar também em `gaps_bloqueadores_livre` e `acoes_corretivas` no JSON para o relatório.
