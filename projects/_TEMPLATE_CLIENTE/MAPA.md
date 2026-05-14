# MAPA - [Nome do Cliente]

> Schema do cliente. Leia isto primeiro: descreve convencoes e onde encontrar cada coisa.

---

## Arquitetura desta pasta

| Camada | Pasta | Papel |
|---|---|---|
| Fontes brutas | `inputs/` | Imutavel - documentos originais do cliente |
| Wiki compilada | `context/` | Estado atual do conhecimento sobre o cliente |
| Execucao | `produtos/` | Jornada do cliente pelos produtos |
| Entregaveis | `produtos/<Produto Ativo>/outputs/` | Tudo que foi ao cliente |

---

## Estado atual

| | |
|---|---|
| **Produto ativo** | `[Saber/E.E]` |
| **Fase em execucao** | `[a confirmar]` |
| **Maior risco** | `[a confirmar]` |
| **Proximo passo** | `[a confirmar]` |

---

## Onde encontrar cada coisa

**Wiki do negocio (`context/`):**
- Modelo de negocio, ICP, receita, capacidade -> `context/business.md`
- Restricoes e gargalos -> `context/constraints.md`
- GTM, canais, funil, ciclo comercial -> `context/gtm.md`
- Stakeholders e relacionamento -> `context/stakeholders.md`

**Fontes brutas (`inputs/` - nunca editar, apenas adicionar):**
- Transcricoes de reunioes -> `inputs/reunioes/`
- Sinteses processadas -> `inputs/sinteses/`
- Documentos do cliente -> `inputs/materiais/`

**Execucao (`produtos/`):**
- Saber / E.E -> `produtos/Saber/E.E/`
- Saber / DR-X -> `produtos/Saber/DR-X/`
- Executar -> `produtos/Executar/`
- Ter -> `produtos/Ter/`
- Potencializar -> `produtos/Potencializar/`

---

## Ultimos inputs relevantes

| Data | Evento | Impacto no context/ |
|---|---|---|
| AAAA-MM-DD | `[a confirmar]` | `[a confirmar]` |

---

## Decisoes recentes

- **D1 (AAAA-MM-DD)** - Projeto criado no Paperclip.

Registro completo: `DECISIONS.md`

