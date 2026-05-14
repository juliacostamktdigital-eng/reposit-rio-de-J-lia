# Google Ads Performance Max — blueprint leadgen

| Campo | Valor |
|-------|-------|
| Cliente | |
| Versão | |
| Data | |
| Responsável | |
| Link plano de mídia (PMax) | |
| Link `setup-campanhas-google-ads` | |
| Conversão primária otimizada | |

---

## A. Gate — quando usar / quando evitar (Seção 8)

Marque **somente** se verdadeiro para ativar PMax neste momento. Se não, pare ou documente exceção em **L**.

| Pré-requisito (“quando usar”) | OK (s/n) |
|-------------------------------|----------|
| Conversão bem configurada e validada | |
| LP/formulário preserva dados | |
| Há assets planejados (mínimo decente) | |
| Há audience signal relevante | |
| Budget adequado para aprendizado | |
| Objetivo é expandir além de Search | |

| Exceção | |
|---------|--|
| Aceito subir com risco explícito (s/n) | |
| Nota / aprovação (obrigatória se gate incompleto) | |

---

## B. Campanha

| Campo | Valor |
|-------|-------|
| `campaign_id` | |
| Nome (taxonomia §10) | |
| URL final padrão | |
| Objetivo / conversão na interface | |
| Resumo orçamento e aprendizado | |
| Prospecção / remarketing / ambos | |

---

## C. Audience signals (Seção 8)

*Não sobrecarregar — listar só os mais fortes.*

| Tipo (CM, site, MQL, termos, URL ref, in-market, GA4…) | Descrição | Notas |
|--------------------------------------------------------|-----------|-------|

---

## D. Asset groups (2 a 5 no início — Seção 8)

### Asset group 00 — oferta principal

| Campo | Valor |
|-------|-------|
| `adgroup_id` | |
| Nome taxonomia | |
| URL final (se diferente) | |

**Headlines curtas:**  

**Headlines longas:**  

**Descrições:**  

| Logo | Img quadrada | Img horizontal | Img vertical | Vídeo próprio (s/n) |
|------|----------------|------------------|---------------|---------------------|
| | | | | |

**Sitelinks / snippets / call (resumo):**  

---

*Repita §D para asset group 01 (persona) e 02 (dor/caso de uso); adicione grupos só se necessário.*

---

## E. Guardrails (URL expansion, marca, conversões — Seção 12 + legado)

| Tema | Decisão registrada |
|------|---------------------|
| URL expansion | |
| Brand controls / excluded URLs / termos | |
| Metas de conversão principais/secundárias | |
| Lance (max conv, tCPA, tROAS, etc.) | |

---

## F. Matriz de testes

- **Varia:**  
- **Constante:**  

---

## G. Checklist pré go-live PMax (Seção 14)

| Item | OK (s/n) |
|------|---------|
| Assets suficientes por grupo | |
| Audience signals configurados (poucos, fortes) | |
| Asset groups + URL final conferidos | |
| URL expansion + brand controls + metas conferidos | |
| UTMs / `v4_*` / lead teste (herdado do setup base) | |
| Hipótese na planilha growth | |
| Change log preparado | |
| Sem alteração diária de budget/lance sem evidência (§12) | |

---

## H. Gaps / maturidade N3 (referência §16)

**Gaps N2:**  

**Notas import offline / qualidade comercial:**  
