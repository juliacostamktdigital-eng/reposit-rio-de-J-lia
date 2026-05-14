# Skills partilhadas — processo Executar

Skills em `executar/shared/` são usadas por **dois ou mais agentes** do processo Executar sem variante por agente.

## Padrão ideal de versionamento (referência)

O exemplo canónico neste repositório é **`client-intake/`**:

| Ficheiro | Função |
|----------|--------|
| `v{X.Y.Z}.md` | Conteúdo **imutável** após publicação de cada versão |
| `latest.md` | **Cópia integral** da versão atual aprovada em produção |
| `CHANGELOG.md` | Histórico de alterações |
| `context.md` | Metadados YAML, propósito, índice de versões |

Regras completas (semver, imutabilidade, depreciação, **pull request obrigatória por skill**): [`../_meta/versioning.md`](../_meta/versioning.md).

## Alinhamento com skills SABER

O mesmo princípio de governança aplica-se a `saber/skills/`, com adaptação para `SKILL.md` Paperclip. Documentação oficial: [`../../saber/skills/VERSIONAMENTO.md`](../../saber/skills/VERSIONAMENTO.md).

## Consumo

1. Ler `context.md` da skill (propósito, inputs, outputs).
2. Executar o protocolo em `latest.md`.
3. Para auditoria ou rollback conceitual, usar o ficheiro `v{X.Y.Z}.md` indicado no changelog ou no `context.md`.
