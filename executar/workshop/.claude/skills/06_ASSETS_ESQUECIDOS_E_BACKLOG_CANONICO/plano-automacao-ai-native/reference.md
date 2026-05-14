# Referência Do Plano De Automação AI-Native

Fonte normativa: `assets/canonicos/06_ASSETS_ESQUECIDOS_E_BACKLOG_CANONICO.md` — **§ 2.20** e contexto de **escala** no **§ 3 (Prioridade 3)**.

## Checklist § 2.20 (campos por tarefa)

Cada linha do mapa deve permitir responder, sem ambiguidade:

1. **Etapa** do OS / jornada  
2. **Tarefa** nomeada  
3. **Input** confiável  
4. **Output** esperado  
5. **Ferramenta** (humano, IA, script, integração)  
6. **Nível de automação** (manual → automático ou bloqueado)  
7. **Risco** se falhar ou escalar errado  
8. **Dono** da manutenção  
9. **Evidência** de que o nível atual foi validado  
10. **Próximo passo técnico** concreto  

## Princípio

Se a operação quer ser AI-native, precisa saber o que será manual, semi-automático ou automático. Automação sem dono, evidência e validação vira risco operacional.

## Relação com outras skills (playbook 06)

- **`inventario-gaps-assets-marketing-os`** e **`backlog-operacional-growth`** — gaps que viram tarefas neste plano.  
- **`rubrica-n1-n2-n3-componentes`** — evidência N2 antes de escalar automação rumo a N3.

## Níveis

### Manual

Execução humana sem template, script ou validação estruturada.

### Assistido

IA ajuda a produzir, revisar ou resumir, mas humano decide.

### Semi-Automático

Script/template gera saída estruturada e humano revisa antes de usar.

### Automático

Integração executa com validação, logs, dono e fallback.

### Bloqueado

Não automatizar agora por risco, falta de input confiável, compliance ou dependência.

## Critérios De Priorização

Priorize automação quando:

- tarefa é recorrente;
- input é estruturado;
- output é padronizável;
- risco é baixo ou controlável;
- há dono;
- há evidência de validação;
- reduz gargalo real;
- melhora rastreabilidade.

Evite automatizar quando:

- decisão é estratégica e ambígua;
- dados são sensíveis sem controle;
- output exige julgamento subjetivo;
- input é instável;
- erro em escala criaria dano;
- não há dono para manutenção.

## Tipos De Próximo Passo Técnico

- criar template;
- criar script;
- criar validador;
- conectar API;
- criar dashboard/log;
- criar rotina de QA;
- documentar processo;
- manter assistido;
- bloquear até resolver dependência.

## Relação Com N2/N3

N2 exige processo auditável.

N3 exige cadência, aprendizado, changelog e melhoria contínua. Automação ajuda N3 quando:

- preserva dados;
- reduz retrabalho;
- registra decisões;
- facilita comparação;
- gera evidências;
- cria logs.

Automação não compensa ausência de processo N2.
