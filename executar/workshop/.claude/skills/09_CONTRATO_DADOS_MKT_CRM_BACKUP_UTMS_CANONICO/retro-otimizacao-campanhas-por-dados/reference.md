# Referência Da Retro Otimização Por Dados

Fonte normativa: `assets/canonicos/09_CONTRATO_DADOS_MKT_CRM_BACKUP_UTMS_CANONICO.md`.

## Princípio

Retro-otimizar é cruzar mídia, leads e CRM para comparar lead barato contra lead qualificado. A decisão deve considerar avanço no funil e qualidade comercial, não apenas custo por lead.

## Processo Canônico

1. Exportar mídia por campanha, conjunto e criativo.
2. Capturar leads na planilha backup.
3. Atualizar status CRM.
4. Cruzar por `lead_id`, email/telefone ou campos de origem.
5. Parsear UTMs e `creative_id`.
6. Agrupar por atributos.
7. Comparar lead barato vs lead qualificado.
8. Registrar decisão na planilha de testes.
9. Rebriefar próximo ciclo.

## Dimensões Recomendadas

- campanha;
- conjunto;
- criativo;
- formato;
- hook;
- persona;
- dor;
- ângulo;
- stage;
- canal;
- cohort;
- segmento.

## Métricas Recomendadas

- spend;
- leads;
- MQL;
- SQL;
- oportunidades;
- vendas;
- receita;
- CPL;
- CPMQL;
- CPSQL;
- CAC;
- ROAS;
- taxa MQL;
- taxa SQL;
- taxa de desqualificação.

## Classificações

### Vencedor

Bom volume, custo aceitável e avanço real no funil.

### Promissor

Sinal positivo, mas volume ainda insuficiente.

### Caro Mas Qualificado

CPL alto, porém MQL/SQL/venda justificam investigação e possível reforço.

### Barato Mas Ruim

CPL baixo, mas baixa qualidade comercial ou alta desqualificação.

### Inconclusivo

Volume ou dados insuficientes.

### Tracking Insuficiente

Dados não sustentam decisão confiável.

## Saídas Para Rebrief

- manter;
- escalar;
- pausar;
- corrigir tracking;
- criar variação;
- reescrever promessa;
- revisar LP;
- ajustar SLA ou handoff.
