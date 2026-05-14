---
name: analise-desvios-venda-boas-vindas
description: Compara call de vendas, Growth Class e plano de ROI eixo a eixo (escopo, resultado, prazo, responsabilidades, próximo passo), classifica risco Baixo/Médio/Alto e exige ação corretiva quando handoff não está completo. Use após boas-vindas, antes de validar pacote EXECUTAR ou quando houver suspeita de promessa mal entendida.
---

# Análise Desvios Venda Boas-vindas

## Quando Usar

Use quando precisar tornar explícito o alinhamento entre o que foi vendido e o que o cliente entendeu.

Situações típicas:

- compilação do handoff operacional EXECUTAR;
- risco de churn M0 por expectativa errada;
- revisão supervisionada pelo coordenador/account;
- auditoria N2 do handoff.

## Eixos Canônicos

| Eixo | Call de vendas | Growth Class | Risco |
| --- | --- | --- | --- |
| Escopo | O que foi vendido | O que o cliente entendeu | Baixo/Médio/Alto |
| Resultado esperado | Promessa/premissa | Expectativa verbalizada | Baixo/Médio/Alto |
| Prazo | O que foi sinalizado | O que o cliente espera | Baixo/Médio/Alto |
| Responsabilidades | O que depende da operação | O que depende do cliente | Baixo/Médio/Alto |
| Próximo passo | O que vendas indicou | O que boas-vindas confirmou | Baixo/Médio/Alto |

Regra do playbook: risco médio ou alto implica handoff incompleto até registro de ação corretiva pelo coordenador/account.

## Workflow

1. Liste evidências na call de vendas e na Growth Class por eixo.
2. Atribua risco Baixo, Médio ou Alto por célula comparativa.
3. Documente divergências textuais objetivas.
4. Para cada risco médio ou alto, defina ação corretiva, dono e prazo.
5. Anexe a matriz ao pacote de `handoff-operacional-executar`.

## Output Esperado

- matriz de desvios preenchida;
- severidade por eixo;
- lista de ações corretivas quando aplicável;
- decisão se o handoff pode ser marcado como completo.

Use `templates/matriz-desvios-handoff.md`.
Use `templates/desvios-handoff.json` com o script para gerar tabela Markdown e CSV.

## Script Utilitário

```bash
python3 scripts/classify_handoff_deviations.py templates/desvios-handoff.json --md /tmp/desvios.md --csv /tmp/desvios.csv
```

## Definition Of Done

- Os cinco eixos foram comparados.
- Riscos médios/altos têm ação corretiva registrada ou o handoff permanece incompleto até correção.
- Matriz pode ser auditada sem depender de memória oral.
