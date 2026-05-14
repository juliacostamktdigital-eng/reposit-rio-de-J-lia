# Skill: ci-cd-pipeline — v1.0.0

> owner: dev-infra-deploy | status: active | published: 2026-04-06

---

## Instrução

Você é o Dev Infra montando o pipeline de CI/CD. Seu objetivo é que o Dev Frontend consiga fazer deploy de forma segura e autônoma, com feedback rápido e rollback fácil.

## Branch strategy recomendada

```
main          ← produção (apenas via PR aprovado)
staging       ← ambiente de homologação
develop       ← integração de features
feature/*     ← branches de desenvolvimento
hotfix/*      ← correções urgentes em produção
```

## Pipeline GitHub Actions — Template

### Deploy automático para produção (via merge em `main`)

```yaml
# .github/workflows/deploy-production.yml
name: Deploy Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test
        # Remova se não houver testes — mas recomende criar

      - name: Build
        run: npm run build
        env:
          NODE_ENV: production

      - name: Deploy to server
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.PROD_SERVER_HOST }}
          username: ${{ secrets.PROD_SERVER_USER }}
          key: ${{ secrets.PROD_SSH_KEY }}
          script: |
            cd /var/www/[cliente]
            git pull origin main
            npm ci --production
            pm2 restart [app-name]
```

### Deploy automático para staging (via merge em `staging`)

```yaml
# .github/workflows/deploy-staging.yml
name: Deploy Staging

on:
  push:
    branches: [staging]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      # Mesma estrutura do production, usando secrets de staging
      - name: Deploy to staging
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.STAGING_SERVER_HOST }}
          # ...
```

## Configuração de secrets no GitHub

Nunca commite credenciais. Configure no repositório:
`Settings > Secrets and variables > Actions`

```
PROD_SERVER_HOST      → IP do servidor de produção
PROD_SERVER_USER      → usuário SSH (ex: v4deploy)
PROD_SSH_KEY          → chave privada SSH (conteúdo do arquivo)
STAGING_SERVER_HOST   → IP do servidor de staging (se houver)
```

## Configuração de PM2 (para apps Node.js em VPS)

```bash
npm install -g pm2

# Criar configuração do processo
# ecosystem.config.js
module.exports = {
  apps: [{
    name: '[cliente-app]',
    script: 'npm',
    args: 'start',
    env: {
      NODE_ENV: 'production',
      PORT: 3000
    }
  }]
}

pm2 start ecosystem.config.js
pm2 save
pm2 startup  # para reiniciar automaticamente após reboot
```

## Processo de rollback

Se um deploy quebrar produção:

```bash
# Via SSH no servidor
cd /var/www/[cliente]
git log --oneline -5  # ver commits recentes
git revert HEAD       # reverter último commit
# OU
git reset --hard [hash-do-commit-estável]
pm2 restart [app-name]
```

## Documentação de entrega

```
# CI/CD Pipeline — [Cliente]
Data de configuração: [data]
Dev Infra: [nome]

## Repositório
- URL: [link do repositório]
- Branch de produção: main
- Branch de staging: staging

## Pipelines configurados
- ✅ Deploy production: merge em main → deploy automático
- ✅ Deploy staging: merge em staging → deploy automático

## Environments no GitHub
- Production: aprovação manual necessária? [sim/não]
- Staging: deploy automático

## Como fazer deploy
1. Merge PR aprovado na branch correta
2. Pipeline roda automaticamente
3. Acompanhar status em: [link das Actions]
4. Em caso de falha: [link para documentação de rollback]

## Secrets configurados
[Lista dos secrets — valores no vault, não aqui]
```

## Regras

- **Todo secret vai no GitHub Secrets** — nunca em arquivos, nunca em mensagens
- Pipeline deve ter step de **build/teste** antes de deploy — falha no build não vai para produção
- Configure **environment protection rules** para produção (exigir aprovação manual)
- Documente o processo de rollback **antes** de precisar dele
