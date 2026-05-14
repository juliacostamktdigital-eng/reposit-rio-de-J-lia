# Modelo de CODEOWNERS — brain_v4_colli

Criar este arquivo em `.github/CODEOWNERS` na raiz do repositório `brain_v4_colli`.

## Como usar

1. Substituir `@SEU-USUARIO-GITHUB` pelo handle real do gestor (ex: `@ruanmths-sudo`)
2. Criar o time `@ORG/TIME-CURADORES` no GitHub: Settings → Teams → New team
3. Criar o time `@ORG/TIME-TODO` com todos os colaboradores do repositório
4. Salvar o arquivo abaixo como `.github/CODEOWNERS` na raiz do repo

> Os times precisam existir no GitHub **antes** de serem referenciados aqui.
> Times são vinculados à organização GitHub (`@NOME-ORG/NOME-TIME`).
> Se o repo for pessoal (não de uma org), usar apenas usuários individuais (`@usuario`).

---

## Arquivo CODEOWNERS

```
# brain_v4_colli — CODEOWNERS
# Documentação: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners

# Áreas críticas — aprovação obrigatória do gestor
# Mudam raramente; impacto alto; rigor total justificado
/schema/        @SEU-USUARIO-GITHUB
/mapa/          @SEU-USUARIO-GITHUB
/decisoes/      @SEU-USUARIO-GITHUB
.github/        @SEU-USUARIO-GITHUB
.claude/        @SEU-USUARIO-GITHUB

# Conhecimento estruturado — aprovação de qualquer curador (gestor não obrigatório)
# Time de curadores pode ser amplo para evitar gargalo
/wiki/          @NOME-ORG/TIME-CURADORES
/projetos/      @NOME-ORG/TIME-CURADORES

# Área de trabalho diário — qualquer colega aprova (peer review)
# CODEOWNERS não definido aqui: 1 aprovação via branch protection é suficiente
# /inputs/ → sem entrada no CODEOWNERS
```

> **Sobre `/inputs/`:** não listada no CODEOWNERS intencionalmente. A branch protection
> exige 1 aprovação de qualquer membro com `Write` — peer review rápido, sem gargalo.

---

## Níveis de governança

| Área | Velocidade | Quem aprova | Motivo |
|---|---|---|---|
| `/schema/`, `/mapa/`, `/decisoes/` | Baixa | Apenas o gestor | Impacto alto, muda raramente |
| `.github/`, `.claude/` | Baixa | Apenas o gestor | Configuração crítica do repo |
| `/wiki/`, `/projetos/` | Média | Qualquer curador | Time curador amplo, sem gargalo do gestor |
| `/inputs/` | Alta | Qualquer colega com Write | Trabalho diário, peer review é suficiente |
