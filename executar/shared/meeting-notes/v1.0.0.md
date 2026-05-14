# Skill: meeting-notes — v1.0.0

> owner: shared | status: active | published: 2026-04-06

---

## Instrução

Você é responsável por transformar anotações brutas de uma reunião em uma ata estruturada e acionável. O documento deve ser claro o suficiente para quem não participou entender as decisões tomadas.

## Protocolo de execução

### 1. Identifique o tipo de reunião

- **Estratégica**: foco em direcionamentos e aprovações de alto nível
- **Alinhamento**: foco em sincronização entre times sobre andamento
- **Resultado**: foco em análise de métricas e ajustes de curso
- **Kickoff**: foco em apresentações, expectativas e combinados iniciais

O tipo de reunião define a ênfase da ata.

### 2. Processe as anotações brutas

Leia o `raw_notes` e identifique:
- Tópicos discutidos (em ordem cronológica ou por importância)
- Decisões explícitas tomadas
- Ações acordadas com responsável nomeado
- Dúvidas ou pontos em aberto

### 3. Produza o documento

```
# Ata de Reunião — [Tipo] — [Data]

**Participantes**: [lista com nomes e papéis]  
**Data**: [data e hora]  
**Duração**: [X minutos]  
**Registrada por**: [agente]

---

## Contexto

[1–2 frases sobre o objetivo da reunião]

## Pontos discutidos

### [Tópico 1]
[Resumo do que foi discutido — sem transcrever, apenas o essencial]

### [Tópico 2]
[Resumo]

## Decisões tomadas

| # | Decisão | Responsável |
|---|---------|-------------|
| 1 | [decisão clara] | [nome] |
| 2 | [decisão clara] | [nome] |

## Próximos passos

| # | Ação | Responsável | Prazo |
|---|------|-------------|-------|
| 1 | [ação específica] | [nome] | [data] |
| 2 | [ação específica] | [nome] | [data] |

## Pontos em aberto

- [questão não resolvida que precisa de encaminhamento]

---
*Ata gerada em [data/hora] por [agente]*
```

## Regras

- Cada próximo passo deve ter **responsável e prazo** — nunca deixe em aberto
- Decisões devem ser formuladas como afirmações, não como perguntas
- Se não houve decisões ou próximos passos, registre explicitamente: "Nenhuma decisão tomada nesta reunião"
- Envie a ata para o coordenador em até 2 horas após a reunião
