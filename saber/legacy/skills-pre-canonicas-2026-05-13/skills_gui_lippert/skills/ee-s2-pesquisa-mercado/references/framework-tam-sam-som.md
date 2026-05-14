# Framework TAM/SAM/SOM para PMEs Brasileiras

## O que e cada metrica

### TAM (Total Addressable Market)
Mercado total disponivel. O tamanho do mercado inteiro se voce pudesse atender 100% dele.

**Para PMEs brasileiras, o TAM geralmente e:**
- O faturamento total do segmento no Brasil
- Ou o numero total de empresas no segmento x ticket medio anual

### SAM (Serviceable Addressable Market)
Mercado enderecavel. A fatia do TAM que voce PODE atingir considerando restricoes reais.

**Filtros comuns para PMEs:**
- Regiao geografica (cidade, estado, regiao)
- Porte do cliente (micro, pequena, media)
- Perfil de cliente (B2B vs B2C, segmento especifico)
- Canal de distribuicao disponivel
- Capacidade operacional atual

### SOM (Serviceable Obtainable Market)
Mercado obtenivel. O que e realista conquistar nos proximos 12 meses.

**Premissas realistas para PMEs:**
- Considere a capacidade de atendimento atual
- Considere o investimento em marketing previsto
- Considere o ciclo de venda medio do segmento
- Normalmente: 1-5% do SAM para empresas novas, 5-15% para empresas estabelecidas

## Metodologias de estimativa

### Top-Down (do macro para o micro)
1. Comece com dados macro do setor (IBGE, SEBRAE, associacoes)
2. Aplique filtros de regiao e perfil
3. Estime o share obtenivel

**Quando usar:** Quando ha dados setoriais publicos disponiveis.

**Fontes confiáveis:**
- IBGE — Pesquisa Anual de Servicos, CEMPRE, PNAD
- SEBRAE — Estudos setoriais, DataSEBRAE
- ABComm — E-commerce brasileiro
- ABRASEL — Alimentacao fora do lar
- ABES — Software brasileiro
- Statista — Dados globais com recorte Brasil
- Euromonitor — Mercados de consumo
- BNDES — Relatorios setoriais

### Bottom-Up (do micro para o macro)
1. Estime o numero de potenciais clientes na regiao
2. Multiplique pelo ticket medio
3. Aplique taxa de conversao realista

**Quando usar:** Quando o segmento e muito nicho ou nao ha dados macro.

**Exemplo:**
```
Clientes potenciais na regiao: 500 empresas
Ticket medio mensal: R$ 2.000
Conversao realista: 5% no primeiro ano
SOM = 500 x R$ 2.000 x 12 x 5% = R$ 600.000/ano
```

### Mista (recomendada)
1. Use top-down para TAM e SAM
2. Use bottom-up para SOM
3. Valide cruzando os dois

## Erros comuns ao estimar mercado para PMEs

### Erro 1: TAM inflado
**Errado:** "O mercado de saude no Brasil e R$ 700 bilhoes"
**Correto:** "O mercado de clinicas de estetica no Brasil fatura R$ 12 bilhoes" (segmento especifico)

### Erro 2: SAM sem filtros reais
**Errado:** "Nosso SAM e 50% do TAM"
**Correto:** "Filtrando por Grande Porto Alegre, clinicas com 2-10 funcionarios, com presenca digital: 1.200 clinicas, R$ 3.6 bilhoes"

### Erro 3: SOM otimista demais
**Errado:** "Vamos capturar 20% do SAM no primeiro ano"
**Correto:** "Com 3 vendedores e R$ 5K/mes em midia, estimamos converter 25 clientes novos em 12 meses"

### Erro 4: Fontes genericas
**Errado:** "Segundo pesquisas, o mercado cresce 10% ao ano"
**Correto:** "Segundo o SEBRAE (Perfil dos Pequenos Negocios, 2025), o segmento de beleza e estetica cresceu 8.3% no ultimo ano"

## Heuristicas por segmento

| Segmento | TAM Brasil estimado | Ticket medio mensal PME | Fontes recomendadas |
|---|---|---|---|
| Odontologia | R$ 45 bi | R$ 1.500-5.000 | CFO, ANS, SEBRAE |
| Clinicas estetica | R$ 12 bi | R$ 2.000-8.000 | ABIHPEC, SEBRAE |
| Imobiliarias | R$ 170 bi | R$ 3.000-10.000 | SECOVI, CRECI |
| Restaurantes | R$ 230 bi | R$ 1.000-3.000 | ABRASEL, ANR |
| Academias | R$ 12 bi | R$ 1.500-4.000 | IHRSA, ACAD |
| E-commerce moda | R$ 55 bi | R$ 2.000-5.000 | ABComm, Neotrust |
| Advocacia | R$ 80 bi | R$ 2.000-6.000 | OAB, CNJ |
| Contabilidade | R$ 25 bi | R$ 800-2.500 | CFC, FENACON |
| Educacao/cursos | R$ 40 bi | R$ 1.500-5.000 | ABED, MEC |
| SaaS B2B | R$ 30 bi | R$ 3.000-15.000 | ABES, Gartner |

**ATENCAO:** Esses valores sao heuristicas para referencia. Sempre busque dados atualizados e cite a fonte especifica.

## Template de apresentacao

```
TAM: R$ [valor]
[Descricao em 1 frase]
Fonte: [nome] ([ano]) — [link se disponivel]

SAM: R$ [valor]
[Descricao em 1 frase]
Filtros: [lista de filtros aplicados]
Calculo: [como chegou no numero]

SOM: R$ [valor] (12 meses)
[Descricao em 1 frase]
Premissas: [lista de premissas]
Calculo: [detalhamento]

Metodologia: [top-down / bottom-up / mista]
Confianca: [alta / media / baixa]
```
