# Checklist — QA go-live Meta Ads (playbook 15)

**Cliente/projeto:**  
**Data da revisão:**  
**Revisor:**  
**Link plano de mídia:**  
**Link estrutura setup / JSON:**  
**Link planilha growth / backup:**  

**Decisão humana após o relatório:** ☐ Go ☐ No-go ☐ Condicional — notas:

---

## A. Princípio (Seção 1)

| ID | Pergunta / critério | ok / gap / n.a. | Notas |
|----|---------------------|-----------------|-------|
| p-01 | Conta de anúncio configurada corretamente (BM, ad account) | | |
| p-02 | Pixel/CAPI/eventos funcionando | | |
| p-03 | Públicos básicos existem para o movimento | | |
| p-04 | Campanha, conjunto e anúncio têm IDs | | |
| p-05 | Estrutura permite teste sem fragmentar demais o orçamento | | |
| p-06 | Hipótese clara | | |
| p-07 | Plano de leitura definido | | |
| p-08 | Planilha backup e contrato de dados ativos e alinhados | | |

---

## B. Conta (Seção 4)

| ID | Item | ok / gap / n.a. | Notas |
|----|------|-----------------|-------|
| c-01 | Business Manager correto | | |
| c-02 | Conta de anúncios correta | | |
| c-03 | Método de pagamento ativo | | |
| c-04 | Página Facebook vinculada | | |
| c-05 | Instagram vinculado | | |
| c-06 | Domínio verificado (se aplicável) | | |
| c-07 | Permissões do time conferidas | | |
| c-08 | Pixel instalado | | |
| c-09 | CAPI configurada quando possível | | |
| c-10 | Eventos principais testados | | |
| c-11 | UTMs preservadas na LP/formulário | | |
| c-12 | Backup recebendo lead; CRM recebendo ou conciliável | | |

---

## C. Eventos (Seção 5)

| ID | Item | ok / gap / n.a. | Notas |
|----|------|-----------------|-------|
| e-01 | Evento de otimização = mais profundo possível sem matar volume (documentado) | | |
| e-02 | Eventos necessários ao funil disparando de forma verificável | | |
| e-03 | Eventos priorizados na conta quando aplicável | | |

---

## D. Públicos e estrutura (Seções 6–8, 7.3–7.5)

| ID | Item | ok / gap / n.a. | Notas |
|----|------|-----------------|-------|
| pv-01 | Temperatura separada (sem misturar quente/frio sem intenção) | | |
| pv-02 | Exclusões aplicadas (aquisição, remarketing, convertidos) | | |
| pv-03 | Quantidade de conjuntos compatível com orçamento (evitar 12+ sem motivo) | | |
| pv-04 | Públicos coerentes com objetivo da campanha e criativo | | |
| pv-05 | Estrutura mínima respeitada se budget baixo (consolidação) | | |

---

## E. Nomenclatura e IDs (Seção 10)

| ID | Item | ok / gap / n.a. | Notas |
|----|------|-----------------|-------|
| n-01 | Nomes de campanha seguem taxonomia (incl. campaign_id) | | |
| n-02 | Conjuntos com adgroup_id nos nomes | | |
| n-03 | Anúncios com creative_id nos nomes | | |

---

## F. Criativos (Seção 11)

| ID | Item | ok / gap / n.a. | Notas |
|----|------|-----------------|-------|
| cr-01 | 3–5 anúncios por conjunto (faixa inicial) | | |
| cr-02 | Variações reais (não peças quase idênticas) | | |
| cr-03 | Cada criativo com creative_id | | |
| cr-04 | Cada criativo com hipótese de leitura | | |

---

## G. Orçamento (Seção 12)

| ID | Item | ok / gap / n.a. | Notas |
|----|------|-----------------|-------|
| o-01 | Orçamento mínimo por conjunto viável para aprendizado | | |
| o-02 | CBO vs ABO coerente com o experimento | | |
| o-03 | Sem fragmentação excessiva vs verba disponível | | |

---

## H. Go-live (Seção 13)

| ID | Item | ok / gap / n.a. | Notas |
|----|------|-----------------|-------|
| gl-01 | Campanha criada com ID | | |
| gl-02 | Conjuntos criados com ID | | |
| gl-03 | Anúncios criados com ID | | |
| gl-04 | Público e temperatura corretos | | |
| gl-05 | Exclusões aplicadas | | |
| gl-06 | Pixel/eventos testados | | |
| gl-07 | UTMs aplicadas | | |
| gl-08 | Planilha backup testada | | |
| gl-09 | CRM/handoff testado | | |
| gl-10 | Criativos aprovados | | |
| gl-11 | Matriz de testes registrada | | |
| gl-12 | Campos/perguntas lead nativo conferidos (se aplicável) | | |
| gl-13 | Regra engajamento/vídeo definida (se aplicável) | | |
| gl-14 | Orçamento e datas conferidos | | |
| gl-15 | Hipótese na planilha de growth | | |
| gl-16 | Change log preparado | | |

---

## I. Complementos N2 (Seção 14)

| ID | Item | ok / gap / n.a. | Notas |
|----|------|-----------------|-------|
| n2-01 | UTMs e campos v4_* aplicados | | |
| n2-02 | Públicos padrão da estratégia criados | | |
| n2-03 | Checklist pré go-live consolidado preenchido (este doc / JSON) | | |

---

## J. Subtipos (Seção 14 + 9)

Marque **aplicável** somente se o go-live inclui o subtipo.

| Subtipo | Aplicável (s/n) | Checklist da subskill atendido (s/n) | Ref. artefato |
|---------|-----------------|--------------------------------------|---------------|
| Lead nativo (formulário Meta) | | | |
| Conversão no site | | | |
| Engajamento / construção de audiência | | | |

---

## K. Anti-padrões (Seção 16) — algum detectado?

| ID | Descrição (canônico) | Detectado | Notas |
|----|----------------------|-----------|-------|
| ap-01 | Campanha sem ID | ☐ | |
| ap-02 | Criativo sem ID | ☐ | |
| ap-03 | Quente e frio misturados sem intenção | ☐ | |
| ap-04 | 12+ conjuntos com pouca verba | ☐ | |
| ap-05 | Muitos interesses pequenos sem volume | ☐ | |
| ap-06 | Remarketing sem exclusão de convertidos | ☐ | |
| ap-07 | Criativos genéricos (não segmentam pelo conteúdo) | ☐ | |
| ap-08 | Pixel/evento não testado | ☐ | |
| ap-09 | Lead sem planilha backup | ☐ | |
| ap-10 | Só CPL sem qualidade comercial | ☐ | |
| ap-11 | Lead nativo sem SLA ou perguntas mínimas | ☐ | |
| ap-12 | Conversão no site sem evento validado | ☐ | |
| ap-13 | Engajamento eterno sem ponte remarketing/performance | ☐ | |

---

## L. Gaps bloqueadores e ações corretivas (livre)

**Gaps bloqueadores:**  

**Ações corretivas / donos / prazo:**  
