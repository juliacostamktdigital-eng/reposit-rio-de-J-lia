---
name: plano-automacao-ai-native
description: Define plano de automação AI-native para Marketing OS, separando tarefas manuais, semi-automáticas e automáticas por etapa, input, output, ferramenta, risco, dono, evidência e próximo passo técnico. Use em revisão operacional, desenho de escala, automação de workflows, backlog técnico ou maturidade N3.
---

# Plano Automação AI-Native

## Fonte canônica

Playbook **`06_ASSETS_ESQUECIDOS_E_BACKLOG_CANONICO.md`**:

- **§ 2.20 Plano de automação / AI-native:** operação AI-native exige saber o que é manual, semi-automático ou automático. Campos obrigatórios por tarefa: **etapa**, **tarefa**, **input**, **output**, **ferramenta**, **nível de automação**, **risco**, **dono**, **evidência**, **próximo passo técnico**.
- **§ 3 Prioridade 3 — “Sem isso não escala”:** o **plano de automação** aparece junto de bibliotecas de padrões, packs por cohort e skills operacionais — esta skill formaliza o plano antes de escalar headcount ou orçamento.

## Quando Usar

Use quando a operação precisa sair de execução manual dispersa para um sistema com automações claras, rastreáveis e seguras.

Situações típicas:

- mapear o que pode ser automatizado;
- reduzir retrabalho em geração de assets;
- estruturar workflows com IA;
- priorizar scripts e integrações;
- definir riscos de automação;
- criar backlog técnico;
- evoluir componentes para N3.

## Inputs Necessários

- etapas do Marketing OS;
- tarefas recorrentes;
- inputs e outputs;
- ferramentas atuais;
- donos;
- evidências;
- riscos;
- frequência da tarefa;
- esforço manual atual;
- impacto esperado;
- dependências técnicas.

## Níveis De Automação

- manual: execução humana, sem template/script confiável;
- assistido: IA apoia, humano decide e edita;
- semi-automático: script/template gera saída estruturada, humano revisa;
- automático: integração executa com validações e logs;
- bloqueado: não automatizar agora por risco, falta de dado ou dependência.

## Workflow

1. Liste etapas e tarefas.
2. Para cada tarefa, declare:
   - input;
   - output;
   - ferramenta;
   - frequência;
   - esforço manual;
   - nível atual;
   - nível desejado;
   - risco;
   - dono;
   - evidência;
   - próximo passo técnico.
3. Classifique risco:
   - dados sensíveis;
   - decisão estratégica;
   - compliance;
   - tracking;
   - qualidade criativa;
   - dependência de integração;
   - risco de automação errada em escala.
4. Defina prioridade:
   - alto volume + baixo risco + output estruturado primeiro;
   - tarefas críticas com validação humana;
   - decisões estratégicas ficam assistidas, não automáticas;
   - automação sem evidência vira risco.
5. Gere backlog técnico:
   - script;
   - template;
   - integração;
   - validação;
   - dashboard/log;
   - documentação.

## Output Esperado

- mapa de automação;
- nível atual/desejado;
- riscos;
- donos;
- evidências;
- próximos passos técnicos;
- prioridades;
- backlog de automação.

Use `templates/plano-automacao.md` para entrega manual.
Use `templates/automacao-ai-native.json` com o script para gerar CSV/Markdown.

## Script Utilitário

```bash
python3 scripts/prioritize_automation_plan.py --write-default templates/automacao-ai-native.json
python3 scripts/prioritize_automation_plan.py templates/automacao-ai-native.json --md ./plano-automacao-consolidado.md --csv ./plano-automacao.csv
python3 scripts/prioritize_automation_plan.py templates/automacao-ai-native.json --audit
```

O script pontua oportunidades por frequência, impacto, esforço manual, risco e prontidão de input/output; `--audit` verifica aderência mínima ao § 2.20 do playbook 06.

## Artefatos

- `reference.md`
- `templates/plano-automacao.md`
- `templates/automacao-ai-native.json`
- `scripts/prioritize_automation_plan.py`

## Definition Of Done

- Tarefas manuais, assistidas, semi-automáticas e automáticas estão separadas.
- Riscos estão explícitos.
- Decisões estratégicas não foram automatizadas sem revisão humana.
- Cada automação tem dono e evidência.
- Próximo passo técnico está claro.
- O plano vira backlog técnico priorizado.
