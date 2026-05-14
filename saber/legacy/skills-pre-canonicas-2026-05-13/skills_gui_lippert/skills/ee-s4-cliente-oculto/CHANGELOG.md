# CHANGELOG — ee-s4-cliente-oculto

---

## [1.1.0] — 2026-05-07 — MINOR

**Contexto:** Piloto com Alisson Joias evidenciou um problema recorrente: timestamps de C1 (tempo de primeira resposta) eram declarados como `[não disponível]` mesmo quando visíveis nos prints — causando subavaliação sistemática de critérios verificáveis. Adicionalmente, o relatório gerado como texto de resposta em vez de arquivo dificultava o versionamento e reuso.

**O que mudou:**

### Adicionado
- **Dupla verificação de timestamps obrigatória antes de classificar C1:** percorrer TODAS as mensagens visíveis, identificar timestamps (a) lead, (b) bot, (c) humano, calcular intervalo
- Instrução explícita: nunca declarar `[não disponível]` sem realizar varredura explícita dos inputs
- Nota sobre leitura de prints de WhatsApp: balões de mensagem têm timestamps — ler dígitos com atenção (não confundir "11:07" com "11:37")
- Estrutura obrigatória do `.md` documentada no SKILL.md (seções, tabela de cálculo de nota, evidências com timestamp)

### Modificado
- Output: de resposta de texto para arquivo salvo diretamente em `clientes/{slug}/outputs/ee-s4-cliente-oculto.md`
- Instrução de geração: output salvo antes de ser apresentado ao operador

### Não modificado
- 7 critérios de avaliação (C1–C7) com pesos
- Escala de classificação (EXCELENTE 9-10 / BOM 7-8 / REGULAR 5-6 / RUIM 3-4 / CRÍTICO 0-2)
- Fluxo de geração de perfil → script → execução manual → análise

---

## [1.0.0] — 2026-01-01

Versão inicial. Output em resposta de texto (não salvo em arquivo). Verificação de timestamps sem instrução explícita de varredura obrigatória.
