# Estrutura de campanhas Meta Ads (pré go-live)

| Campo | Valor |
|-------|-------|
| Cliente | |
| Versão deste doc | |
| Data | |
| Responsável media | |
| Link planilha growth / backup | |
| Link contrato de dados | |

---

## A. Checklist de conta (antes de estruturar)

| Item | OK (s/n) | Notas / IDs |
|------|---------|----------------|
| Business Manager correto | | BM ID: |
| Conta de anúncios correta | | Ad account ID: |
| Pagamento ativo | | |
| Página Facebook vinculada | | |
| Instagram vinculado | | |
| Domínio verificado (se aplicável) | | |
| Permissões do time | | |
| Pixel instalado | | Pixel ID: |
| CAPI configurada (se possível) | | |
| Eventos principais testados | | |
| Eventos priorizados (se aplicável) | | |
| UTMs preservadas na LP/form | | |
| Planilha backup recebendo lead | | |
| CRM recebendo / conciliável | | |

---

## B. Eventos e otimização

| Evento / papel | Uso |
|----------------|-----|
| PageView | |
| ViewContent ou equivalente | |
| Lead (formulário) | |
| MQL custom (se houver) | |
| SQL/offline (se houver) | |

**Evento de otimização escolhido:**  
**Justificativa (profundidade vs volume):**

---

## C. Públicos (planejados ou criados)

### Frios

| Nome interno | Definição resumida |
|----------------|-------------------|

### Mornos

| Nome interno | Definição resumida |
|----------------|-------------------|

### Quentes

| Nome interno | Definição resumida |
|----------------|-------------------|

### Exclusões globais ou por campanha

---

## D. Estrutura — campanhas / conjuntos / anúncios

*Use a taxonomia do playbook (Seção 10).*

### Campanha 1 — [rótulo ex.: aquisição frio]

| Campo | Valor |
|-------|-------|
| `campaign_id` | |
| Nome completo (taxonomia) | |
| Objetivo Meta | |
| Tipo (aquisição / remarketing / reativação) | |
| Orçamento CBO ou ABO | |
| Valor / lógica de orçamento | |
| Hipótese principal | |

#### Conjuntos

| `adgroup_id` | Nome (taxonomia) | Temperatura | Público resumo | Exclusões | Orçamento (se ABO) |
|--------------|------------------|-------------|----------------|-----------|---------------------|
| | | | | | |

##### Anúncios (por conjunto — repetir bloco)

**Conjunto:** [adgroup_id]

| `creative_id` | Nome (taxonomia) | Formato | Hipótese de leitura |
|---------------|-------------------|---------|---------------------|
| | | | |

*(Repetir para Campanha 2, 3…)*

---

## E. Matriz de testes do ciclo

| O que varia | O que fica constante |
|-------------|---------------------|
| | |

---

## F. Checklist pré go-live (Seção 13)

| Item | OK |
|------|-----|
| Campanha com ID | |
| Conjuntos com ID | |
| Anúncios com ID | |
| Público/temperatura corretos | |
| Exclusões aplicadas | |
| Pixel/eventos testados | |
| UTMs aplicadas | |
| Backup testada | |
| CRM/handoff testado | |
| Criativos aprovados | |
| Matriz de testes registrada | |
| Lead nativo: campos/perguntas (se aplicável) | |
| Regra engajamento/vídeo → remarketing (se aplicável) | |
| Orçamento e datas | |
| Hipótese na planilha growth | |
| Change log preparado | |

---

## G. Subtipo (marcar)

- [ ] Lead formulário nativo → ver subskill `setup-meta-lead-nativo` quando existir  
- [ ] Conversão site → ver `setup-meta-conversao-site` quando existir  
- [ ] Engajamento / construção de audiência  

---

## H. N2 — autoavaliação

Todos os bullets da Seção 14 do playbook 15 atendidos? (s/n)  
**Gaps:**
