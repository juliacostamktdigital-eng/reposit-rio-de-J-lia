# Context — ee-s4-cliente-oculto

## Identidade

**Nome:** ee-s4-cliente-oculto
**Status:** ativa
**Versão atual:** 1.1.0

---

## Histórico de Versões

| Versão | Data | Tipo | Resumo |
|--------|------|------|--------|
| 1.0.0 | 2026-01-01 | — | Versão inicial — output em resposta de texto, sem instrução de varredura de timestamps |
| **1.1.0** | **2026-05-07** | **MINOR** | **Output .md salvo em arquivo, dupla verificação de timestamps C1 obrigatória, estrutura de relatório fixada** |

---

## Contextos de Aplicação

| Contexto | Uso | Observações |
|----------|-----|-------------|
| POP Semana 4 — Diagnóstico de Atendimento | **Principal** | Executa após `/ee-s4-diagnostico-comercial` |
| Input para SDR IA | **Downstream** | Contraste "antes vs depois" alimenta scripts e critérios do SDR |

---

## Decisões de Design

**Por que a varredura de timestamps é obrigatória antes de classificar C1?**
Em testes anteriores, o critério C1 (tempo de primeira resposta) era declarado `[não disponível]` mesmo quando os prints continham timestamps legíveis nos balões de mensagem do WhatsApp. Este padrão de erro sistemático justifica uma instrução explícita de varredura prévia — elimina a possibilidade de subavaliação por leitura incompleta dos inputs.

**Por que output .md e não texto de resposta?**
O relatório de cliente oculto é um documento consultivo que pode ser compartilhado com o cliente como evidência de diagnóstico de atendimento. Arquivo salvo é versionável, repassável e referenciável em sessões futuras — resposta de texto não.

**Por que execução MANUAL pelo operador?**
O cliente oculto precisa acontecer no canal real, com número não associado à V4. A IA não tem acesso a WhatsApp, Instagram DM ou outros canais do cliente — a execução manual é estrutural, não uma limitação temporária.

---

## Evidência de Validação

**Piloto:** Alisson Joias — 07/05/2026
**Operador:** Jhonatan Mayer
**Output gerado:** `saber/clientes/alisson-joias/outputs/ee-s4-cliente-oculto.md`
