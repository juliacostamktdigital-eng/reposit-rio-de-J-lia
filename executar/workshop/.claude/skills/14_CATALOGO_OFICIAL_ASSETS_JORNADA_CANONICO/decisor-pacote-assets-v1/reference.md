# Referência — Decisão do pacote v1 (playbook 14)

## Seção 6 — texto canônico

| Asset | Classificação | Quando entra |
| --- | --- | --- |
| Lista curta de assets v1 | Obrigatório | Após diagnóstico e benchmark, dentro da etapa de construção de assets. |
| Lista de assets fora do ciclo | Obrigatório | Para não transformar tudo em card/entrega. |
| Matriz de dependências do cliente | Obrigatório | Antes de tracking e setup. |
| Critérios de N2 por componente | Obrigatório | Antes da auditoria. |

## Interpretação operacional

### Lista curta v1

- Cada linha deve ser **um asset reconhecível** do catálogo (nome alinhado a `reference.md` / `catalogo_assets.json`) **ou** exceção justificada (ex.: peça nomeada no contrato).
- **P0**: sem isso não há go-live ou não há auditoria N2 possível.
- **P1**: escopo declarado do v1; pode ser paralelizado após desbloqueios.
- **P2**: desejável no ciclo; cortável sem quebrar promessa ao cliente se documentado.

### Fora do ciclo

Função: **gestão de expectativa** e redução de escopo implícito. Cada linha responde implicitamente: *por que não agora?* (capacidade, fase, dependência, risco legal, falta de dado).

### Matriz de dependências do cliente

Tipos úteis de dependência:

- **Acesso** (BM, GA/GTM, DNS, CRM).
- **Decisão** (oferta, budget, tomada de risco criativo).
- **Dado** (lista, pixel histórico, definição de MQL).
- **Legal / compliance** (claims, formulário, cookies).
- **Operação** (SLA comercial, owner interno).

Para cada dependência, declare **o que ela bloqueia** no pacote v1 (ex.: “sem pixel → não enviar tráfego para LP de conversão otimizada”).

### Critérios N2 por componente

- **Componente**: bloco da jornada (ex.: DEOC, plano de mídia, setup Meta, CRM/UTM, evidências N2).
- **N2 mínimo**: condição verificável (não adjetivo).
- **Evidência esperada**: artefato, print, link, checklist assinado, etc.

Para **DEOC e comunicação**, use como referência o critério N2 do playbook **13** (Seção 6); traduza em uma linha por componente do **seu** pacote.

## Alinhamento com a Seção 14 do catálogo

Cada asset no pacote v1 deve responder **sim** a pelo menos uma pergunta do critério anti-bullshit:

- Sem ele o processo não roda?
- Sem ele não dá para auditar N2?
- Sem ele não dá para aprender em N3?
- Sem ele o time recoleta contexto toda vez?
- Sem ele mídia, criativo, LP ou vendas decidem no escuro?

Se todas forem **não**, o item não deveria estar no pacote v1 — mova para fora do ciclo ou para suporte.

## Anti-padrões

- Pacote v1 que é uma **cópia do catálogo inteiro** (falta corte).
- **Fora do ciclo** vazio ou genérico (“tudo que não listamos”).
- Dependências só em “precisamos de acesso” **sem** dizer o que isso bloqueia.
- N2 por componente **só em nível de conta** (“estar bom”) sem evidência.
