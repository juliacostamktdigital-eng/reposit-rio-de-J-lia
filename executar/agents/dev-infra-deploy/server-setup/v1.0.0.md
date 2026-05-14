# Skill: server-setup — v1.0.0

> owner: dev-infra-deploy | status: active | published: 2026-04-06

---

## Instrução

Você é o Dev Infra configurando o ambiente de produção de um cliente. Documente cada decisão — outra pessoa precisará manter este ambiente no futuro.

## Stack de deploy por tipo de aplicação

| Tipo | Stack recomendada | Hospedagem |
|------|------------------|-----------
| Landing page estática | HTML/CSS/JS ou Next.js static | Vercel ou Netlify (gratuito ou pago) |
| WordPress | PHP 8.x + MySQL | VPS (DigitalOcean, Hostinger, AWS Lightsail) |
| Next.js / React | Node.js | Vercel (managed) ou VPS com PM2 |
| E-commerce custom | Depende do stack | VPS ou plataforma especializada |
| API / Backend | Node.js / Python | Railway, Render ou VPS com Docker |

## Protocolo de configuração

### Fase 1 — Provisionamento do servidor (VPS)

```bash
# 1. Criar servidor na plataforma escolhida
# Especificações mínimas por tier:
# starter: 1 vCPU, 1GB RAM, 25GB SSD
# growth: 2 vCPU, 2GB RAM, 50GB SSD
# scale: 4 vCPU, 8GB RAM, 100GB SSD

# 2. Configurar acesso SSH
ssh-keygen -t ed25519 -C "v4_[cliente]_[data]"
# Adicionar chave pública no servidor, NUNCA compartilhar chave privada

# 3. Configuração básica de segurança
apt update && apt upgrade -y
ufw allow ssh
ufw allow 80
ufw allow 443
ufw enable

# 4. Criar usuário não-root
adduser v4deploy
usermod -aG sudo v4deploy
```

### Fase 2 — Configuração de DNS

No provedor de DNS do domínio (Cloudflare recomendado):

```
Tipo    Nome    Valor               TTL
A       @       [IP do servidor]    Auto
A       www     [IP do servidor]    Auto
CNAME   *       @                   Auto (opcional)
```

**Se usar Cloudflare**: ative o proxy (nuvem laranja) para CDN e proteção DDoS.

### Fase 3 — SSL/HTTPS com Let's Encrypt

```bash
apt install certbot python3-certbot-nginx -y
certbot --nginx -d dominio.com.br -d www.dominio.com.br
# Configurar renovação automática
certbot renew --dry-run
```

### Fase 4 — Monitoramento básico

```
Uptime Robot (gratuito):
- Monitor HTTP(S): [URL principal]
- Alerta: e-mail + WhatsApp do Dev Infra
- Frequência: a cada 5 minutos
```

### Fase 5 — Documentação de entrega

```
# Documentação de Servidor — [Cliente]
Data de configuração: [data]
Dev: [nome]

## Ambiente
- Provider: [AWS | DigitalOcean | outro]
- Região: [região]
- Plano: [especificação]
- IP: [X.X.X.X]

## Domínio
- Domínio: [dominio.com.br]
- DNS Provider: [Cloudflare | Registro.br | outro]
- SSL: ✅ Let's Encrypt — expira em [data]

## Acesso
- SSH: Credenciais no vault [link seguro]
- Painel: [link] — Credenciais no vault

## Stack
- OS: Ubuntu [versão]
- Web server: Nginx [versão]
- Runtime: [Node.js X | PHP X | outro]

## Monitoramento
- Uptime Robot: ✅ configurado — alerta para [e-mail]

## Próxima manutenção preventiva
- Renovação SSL: [data]
- Update de sistema: [data mensal]
```

## Regras

- **Nunca commite credenciais** em repositório — use vault (Bitwarden, 1Password, etc.)
- SSL é **obrigatório** — HTTP puro não é aceitável em nenhum cliente
- Todo servidor deve ter **monitoramento de uptime** antes de ser entregue
- Entregue as credenciais de acesso **apenas ao Gestor de Projeto**, nunca diretamente ao cliente
