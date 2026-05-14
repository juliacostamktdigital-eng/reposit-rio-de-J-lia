# Versionamento oficial — skills SABER (`saber/skills/`)

> **Referência de ouro:** o padrão usado em `executar/shared/client-intake/` (`v{X.Y.Z}.md` imutáveis + `latest.md` + `CHANGELOG.md` + `context.md` quando aplicável).  
> Regras semânticas e critérios MAJOR/MINOR/PATCH: [`executar/_meta/versioning.md`](../executar/_meta/versioning.md).

Este documento alinha as skills no formato **Paperclip** (`SKILL.md`, `schema.json`, `references/`) ao **mesmo princípio de governança** que as skills do processo Executar.

---

## Objetivo

- **Histórico auditável:** cada versão publicada permanece intacta.
- **Produção previsível:** `latest.md` (e, no ecosistema Paperclip, `SKILL.md` alinhado a ele) reflete sempre a versão aprovada mais recente.
- **Aprovação explícita:** mudanças entram via **uma pull request por skill**, não por merge direto de alterações pontuais na `main`.

---

## Estrutura alvo por pasta de skill

Cada skill em `saber/skills/` deve evoluir para a seguinte disposição (além do que já existir: `references/`, `schema.json`, etc.):

```
{nome-da-skill}/
├── SKILL.md           ← deve espelhar o conteúdo de produção (ver abaixo)
├── latest.md          ← cópia integral da versão vigente aprovada
├── v1.0.0.md          ← imutável após publicação
├── v1.1.0.md          ← imutável após publicação
├── …
├── CHANGELOG.md       ← histórico cronológico (obrigatório quando houver versões)
├── context.md         ← opcional; metadados / índice se a skill ganhar frontmatter Executar-like
├── schema.json        ← quando existir, manter coerente com a versão documentada no CHANGELOG
└── references/        ← anexos; alterações que mudem comportamento da skill exigem nova versão
```

### `SKILL.md` e `latest.md` (Paperclip)

- O Paperclip e ferramentas associadas leem **`SKILL.md`** (frontmatter com `name` e `description` é obrigatório).
- **`latest.md`** deve conter o **mesmo corpo e frontmatter** que `SKILL.md` na versão em produção, para permitir diff claro e paridade com o padrão `client-intake`.
- Ao **promover** uma nova versão `vX.Y.Z`:
  1. O conteúdo final aprovado vive em `vX.Y.Z.md` (imutável).
  2. **Copie integralmente** esse arquivo para **`latest.md`**.
  3. **Copie integralmente** para **`SKILL.md`** (para o runtime e descoberta continuarem corretos).

Versões antigas (`v1.0.0.md`, …) **nunca** são editadas; correções são um novo `PATCH`/`MINOR`/`MAJOR` em um **novo** ficheiro `v….md`.

---

## Fluxo obrigatório ao modificar uma skill

1. **Não edite** ficheiros `v*.*.*.md` já publicados.
2. Crie um **novo** ficheiro versionado (ex.: `v1.1.0.md`) a partir da versão anterior ou de `latest.md`, aplicando apenas as alterações necessárias.
3. Atualize **`CHANGELOG.md`** com data, tipo de mudança e resumo.
4. Somente após revisão humana: **promova** a versão — copie o novo `vX.Y.Z.md` para `latest.md` e para `SKILL.md`.
5. Se existir `context.md` com campo `latest`, atualize `latest` e `updated`.
6. Abra **uma pull request dedicada a esta skill** (ver secção seguinte).

Incremento de versão (MAJOR / MINOR / PATCH): seguir tabela e exemplos em [`executar/_meta/versioning.md`](../executar/_meta/versioning.md).

---

## Governança Git: uma PR por skill

- **Proibido** integrar alteração de skill via commit direto na `main` sem revisão em PR (ajustar à política do repositório: branch protection).
- Cada alteração de skill deve ter **pull request própria** (título e descrição referenciam o nome da skill e a versão, ex.: `skill(saber): saber_session_extract v1.1.0`).
- Uma PR **não** deve misturar mudanças de várias skills não relacionadas; isso facilita aprovação por dono de domínio e rollback.

Detalhamento alinhado ao processo Executar: secção *Governança Git* em [`executar/_meta/versioning.md`](../executar/_meta/versioning.md).

---

## Skills geradas em lote

O script `_generate_domain_skills.mjs` recria skills de domínio. Após passar a usar `v*.*.*.md` + `latest.md` numa pasta:

- Regenerações devem **preservar** histórico versionado ou ser feitas numa PR que **só** trate dessa migração/regeneração, com changelog explícito.

---

## Referências

| Documento | Conteúdo |
|-----------|----------|
| [`executar/_meta/versioning.md`](../executar/_meta/versioning.md) | Semver, templates, imutabilidade, **PR por skill** |
| [`executar/shared/client-intake/`](../executar/shared/client-intake/) | Exemplo canónico (`v1.0.0.md`, `latest.md`, `CHANGELOG.md`) |
| [`executar/shared/README.md`](../executar/shared/README.md) | Pasta partilhada Executar + ligação ao padrão |
| [`README.md`](README.md) (esta pasta) | Catálogo de skills SABER |
