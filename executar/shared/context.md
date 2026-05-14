# Shared Skills — V4 Company

> Skills reutilizáveis consumidas por dois ou mais agentes

---

## Propósito

Skills em `executar/shared/` não têm um único owner — são mantidas coletivamente e podem ser consumidas por qualquer agente do processo **Executar**. Elas encapsulam capacidades **transversais** que aparecem em múltiplos contextos operacionais.

## Quando colocar uma skill aqui

- A skill é usada por **2 ou mais agentes distintos**
- O comportamento é **idêntico** independente do agente que executa
- Não há especialização de mercado ou contexto que justifique duplicação

## Quando NÃO usar shared

- A skill tem comportamento diferente dependendo do agente → crie versões específicas por agente com `extends: executar/shared/{skill}` no context.md
- A skill é experimental ou em draft → crie primeiro no agente owner antes de promover para `executar/shared/`

---

## Skills disponíveis

| Skill | Descrição | Consumers | Versão atual |
|-------|-----------|-----------|-------------|
| `client-intake` | Coleta estruturada de informações do novo cliente | gerente, coordenador, copywriter, designer | v1.0.0 |
| `meeting-notes` | Registro padronizado de reuniões com cliente | gerente, coordenador, gestor-de-projeto | v1.0.0 |
| `sop-template` | Geração de procedimento operacional padrão | coordenador, gestor-de-projeto, dev-frontend, dev-infra-deploy, gestor-de-trafego | v1.0.0 |

---

## Processo de promoção para shared

1. Skill existe e está `active` no agente owner
2. Outro agente precisa da mesma skill sem modificação
3. Abrir proposta de promoção (PR ou doc de decisão) com:
   - Lista de agentes que vão consumir
   - Confirmação de que o comportamento é idêntico
4. Mover a pasta para `executar/shared/`
5. Atualizar `context.md` dos agentes consumers com `consumes: executar/shared/{skill}`
6. Remover a cópia do agente owner (ou manter referência)
