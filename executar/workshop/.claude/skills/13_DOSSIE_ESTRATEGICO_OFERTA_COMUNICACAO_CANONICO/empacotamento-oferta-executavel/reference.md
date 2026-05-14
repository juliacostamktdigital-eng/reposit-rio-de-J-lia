# Referência — Empacotamento de oferta executável

Fonte normativa: **`13_DOSSIE_ESTRATEGICO_OFERTA_COMUNICACAO_CANONICO.md`**, seções **5.2** e **5.8** (na parte que governa promessa e claims). Complemento de fluxo da skill legada **07-empacotamento-oferta** (sem redesenho de pricing).

## O que a oferta precisa responder (5.2)

- O que é vendido.
- Para quem serve.
- Quando faz sentido.
- Quando **não** faz sentido.
- Como funciona.
- Mecanismo de geração de resultado.
- Features, implicações, benefícios, provas.
- **Brainer comercial** em uma frase: *faço X em Y, para Z, com W*.
- Condições diferenciais que reduzem risco ou aumentam confiança.
- **Escopo explícito:** o que entra, o que não entra, pré-requisitos.
- **Limites da promessa:** quando não vender, anti-ICP e risco de passivo.

## Forces of Progress (Bob Moesta) — filtro pré-empacotamento

**Antes** de empacotar oferta, validar 4 forças. Se ≤2 estão nomeadas, oferta não move ninguém — voltar ao diagnóstico.

| Força | Pergunta | Exemplo (consultoria fictícia) |
|-------|----------|--------------------------------|
| **Push** | O que empurra o ICP pra fora do status quo? | Reunião de board cobrando crescimento |
| **Pull** | O que puxa pra essa solução específica (não a categoria)? | Promessa de ritual semanal embutido no produto |
| **Habit / inércia** | Que elemento da oferta ataca ativamente o hábito atual? | Onboarding em 14d com migração assistida da planilha |
| **Anxiety** | A ansiedade da migração tem **antídoto explícito**? | Garantia de devolução em 30d + check-in semanal |

Score: 4/4 → oferta tem chance. 3/4 → ajustar antídoto da força fraca. ≤2/4 → bloqueio.

---

## Estrutura Hormozi-style pronta pra LP

A oferta empacotada tem **6 blocos canônicos** que descem direto pra LP:

### (a) Núcleo
O que é entregue de fato (sem inflar com bônus). É o produto/serviço base.

### (b) Bônus reativos (cada um neutraliza UMA objeção)
**Campo obrigatório por bônus: `objecao_neutralizada`**. Bônus sem objeção mapeada **não entra**.

Exemplo:
- Bônus: "Template de scorecard pré-preenchido por persona" → objeção neutralizada: "vai dar trabalho configurar".
- Bônus: "30min com sales engineer no kickoff" → objeção neutralizada: "não temos tempo de implementar".

### (c) Garantia (classificada em 3 tipos)
| Tipo | Quando usar | Risco |
|------|-------------|-------|
| **Incondicional** | Capacidade real de devolver dinheiro / refazer | Alto se sem caixa; libera maior conversão |
| **Condicional com checklist auditável** | Cliente faz X, Y, Z; senão garantia não vale | Médio; **checklist precisa ser claro** |
| **Nenhuma + por quê** | Produto inerentemente sem como devolver (curso ao vivo, consultoria executada) | Baixo se justificativa for honesta |

**Não inventar garantia falsa.** Hormozi 2024 reforçou: oferta com garantia que não se honra destrói trust e LTV; CONAR/FTC tratam como propaganda enganosa.

### (d) Escassez REAL (não fake)
Apenas 4 fontes válidas:
- **Cohort** (turma fecha em data X com N pessoas)
- **Capacidade operacional** (atendemos N clientes/mês — limite de equipe real)
- **Deadline de calendário** (lançamento Q1, evento, promoção fiscal)
- **Janela de produção** (fornecedor, importação, sazonalidade)

**NÃO usar:** countdown que reseta, "últimas 3 vagas" sem lastro, "promoção termina hoje" recorrente. CONAR Art. 23 (Brasil) e FTC Endorsement Guides tratam como engano.

### (e) Ancoragem de preço comparativa
Explicitar **contra o quê** o preço se ancora. Exemplos:
- vs alternativa nominal (concorrente nomeado)
- vs custo do não-agir (mensurado em receita perdida / hora)
- vs item de referência conhecido (coworking, hotel, mensalidade SaaS comparável)

Sem âncora → preço fica isolado e vira objeção pura.

### (f) CTA único
Uma promessa-objeto consistente. Não misturar "agende uma demo" com "baixe o ebook" no mesmo bloco.

---

## Honesty constraint (regra dura)

Escassez, urgência e garantia **não podem ser fake**. Cada uma:
- tem **lastro operacional auditável** (capacidade, cohort, calendário, política), **OU**
- é declarada como **ausente** com justificativa.

Risco regulatório:
- **CONAR (Brasil)** Art. 23: propaganda não pode induzir a erro sobre disponibilidade.
- **FTC (EUA)** Section 5: deceptive practices, inclui fake scarcity / fake countdown.
- **Hormozi 2024**: oferta com fake scarcity destrói trust e LTV de longo prazo (custo invisível mas mensurável em churn).

Se o cliente insiste em fake scarcity → registrar no backlog como **claim proibido** e seguir.

---

## Formato canônico por feature (5.2)

Para cada feature (ou bloco entregável equivalente), documentar:

```text
Feature:
Como funciona:
Implicação:
Benefício:
Prova:
Como vira copy:
```

## Claims e empacotamento (5.8)

**Permitidos** quando sustentados por evidência: promessas com prova, números com fonte, comparações verificáveis, benefícios plausíveis.

**Evitar / tratar como proibidos até haver lastro:** garantias absolutas; ROI sem premissa; superlativos sem prova; promessas que dependem de capacidade que o cliente não tem; claims regulatórios sem validação; garantia ou condição diferencial sem lastro real de entrega; promessa que depende de heroísmo operacional; mudança de pricing disfarçada de empacotamento quando pricing estiver fora do escopo.

Use a coluna **pendentes** para o que a comunicação gostaria de dizer mas ainda não tem prova ou validação.

## Inputs úteis (_subset_ da seção 4 do playbook 13)

- Beachhead e ICP/persona.
- Benchmark de mercado e concorrentes (como outros empacotam).
- Materiais comerciais, provas/cases.
- Objeções e feedback comercial.
- Restrições jurídicas ou regulatórias.
- Evidências de ganhos/perdas e perguntas recorrentes.
- **Capacidade real de entrega**, restrições e pré-requisitos da oferta.

## Checklist de risco (legado 07, alinhado ao 13)

- Dá para entregar sem depender de heroísmo operacional?
- A promessa é **auditável** (prova ou caminho claro para obter prova)?
- Condições diferenciais não criam passivo impossível?
- Escopo e pré-requisitos estão explícitos para vendas e marketing?
- Times conseguem repetir o **brainer** da mesma forma?

## Critério N2 relevante (trecho do playbook 13, seção 6)

Para a fatia de oferta, o conjunto está coerente com N2 quando há:

- Oferta **dizível**, escopo explícito, provas mínimas e limites da promessa.
- Provas ou claims claramente **pendentes** onde faltar evidência.
- ICP e anti-ICP utilizáveis na prática (esta skill foca anti-ICP e limites; o DEOC completo expande ICP).

## O que evitar

- Empacotamento que esconde mudança de preço como “novo pacote” sem decisão explícita de pricing.
- Lista de features sem **prova** ou sem **como vira copy** (quebra a ponte para execução).
- Anti-ICP vago (“não é para empresas ruins”) sem critério operacional.
