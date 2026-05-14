# Checklist de Configuração Manual no GitHub — brain_v4_colli

Execute este checklist uma única vez ao configurar o repositório.
Depois disso, a governança funciona automaticamente via branch protection + CODEOWNERS.

---

## 1. Repositório

- [ ] Repositório criado no GitHub com o nome: `brain_v4_colli`
- [ ] Visibilidade: **Privado**
- [ ] Branch principal configurada como: `main`

---

## 2. Permissões de acesso

Settings → Collaborators and teams → Add people / Add teams

| Perfil | Permissão |
|---|---|
| Gestor(es) | Admin |
| Curadores / revisores | Maintain ou Write |
| Time que contribui | Write |
| Apenas consulta | Read |

> Mesmo quem tem `Write` **não** consegue enviar para `main` diretamente — isso é bloqueado pela branch protection.

---

## 3. Proteção da branch main

Settings → Branches → Add branch protection rule

- Branch name pattern: `main`

Ativar as seguintes opções:

- [ ] **Require a pull request before merging**
  - [ ] Require approvals: `1` (mínimo — suficiente para peer review em `/inputs/`)
  - [ ] Require review from Code Owners
- [ ] **Block direct pushes**
- [ ] **Do not allow bypassing the above settings**

> "Do not allow bypassing" garante que **nem admins** consigam fazer push direto.

> **Como funciona a governança de dois velocidades:**
> - Áreas com CODEOWNERS definido (`/schema/`, `/wiki/`, etc.) — o dono da área é notificado e sua aprovação é obrigatória
> - `/inputs/` não tem CODEOWNERS — basta a 1 aprovação acima, de qualquer colega com `Write`
> - Resultado: trabalho diário em `/inputs/` flui com peer review; mudanças estruturais exigem curador ou gestor

---

## 4. CODEOWNERS

- [ ] Criar o arquivo `.github/CODEOWNERS` no repositório
  - Usar o modelo em `assets/codeowners-model.md` desta skill
  - Substituir os placeholders pelos usuários e times reais
- [ ] Criar times no GitHub **antes** de referenciá-los no CODEOWNERS:
  - Settings → Teams → New team → `TIME-CURADORES`
  - Settings → Teams → New team → `TIME-TODO`
  - Adicionar os membros corretos em cada time

---

## 5. GitHub CLI — cada membro do time

Cada pessoa que vai contribuir precisa fazer isso **uma única vez** na própria máquina:

```bash
# 1. Instalar o GitHub CLI
# Mac: brew install gh
# Windows: winget install --id GitHub.cli
# Linux: https://github.com/cli/cli/blob/trunk/docs/install_linux.md

# 2. Autenticar
gh auth login

# 3. Verificar
gh auth status
```

---

## 6. Instalação da skill no repositório

Após clonar o `brain_v4_colli` localmente, copiar a pasta da skill:

```bash
# A partir da raiz do repo brain_v4_colli clonado:
mkdir -p .claude/skills
cp -r /caminho/para/Template/.claude/skills/brain-v4-colli-workflow-v1 .claude/skills/
chmod +x .claude/skills/brain-v4-colli-workflow-v1/scripts/*.sh
```

Commitar e fazer push da pasta `.claude/` para que todos do time tenham a skill disponível.

---

## 7. Verificação final

Após configurar tudo, testar o fluxo completo:

- [ ] Abrir Claude Code no repositório `brain_v4_colli` clonado
- [ ] Dizer: "começar uma alteração sobre teste-setup"
- [ ] Verificar que branch `contrib/<user>/teste-setup-<data>` foi criada
- [ ] Modificar qualquer arquivo de teste
- [ ] Dizer: "ver status" e verificar saída em português
- [ ] Dizer: "submeter para revisão" e verificar que PR foi criado com link
- [ ] Verificar no GitHub que o PR foi aberto corretamente
- [ ] Verificar que a branch `main` não foi alterada diretamente
