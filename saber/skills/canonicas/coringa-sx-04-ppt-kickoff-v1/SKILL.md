---
slug: coringa-sx-04-ppt-kickoff-v1
name: coringa-sx-04-ppt-kickoff-v1
description: "Lê os arquivos de contexto do cliente (`context/business.md`, `context/gtm.md`, `context/constraints.md`) e gera um arquivo **PPTX preenchido** com os dados do cliente, usando o template de kickoff existente como base."
---

# Skill: Kickoff — Geração de Apresentação PPT

## Descrição
Lê os arquivos de contexto do cliente (`context/business.md`, `context/gtm.md`, `context/constraints.md`) e gera um arquivo **PPTX preenchido** com os dados do cliente, usando o template de kickoff existente como base.

O output é um arquivo `.pptx` pronto para revisão e ajuste visual pelo time antes da reunião de kickoff.

## Quando Usar
- Triggers: "gerar PPT de kickoff", "criar apresentação de kickoff", "montar ppt do kickoff", "preencher slides do kickoff"
- **Pré-requisito:** `context/business.md`, `context/gtm.md` e `context/constraints.md` devem existir (gerados pela `coringa-sx-01`). Template PPTX deve estar na raiz do projeto.
- **NÃO usar se:** os arquivos de context/ não existirem — sem dados não há o que preencher.

## Inputs Necessários
1. `clientes/[nome-cliente]/context/business.md`
2. `clientes/[nome-cliente]/context/gtm.md`
3. `clientes/[nome-cliente]/context/constraints.md`
4. Template PPTX: `[Kick-off] Globo Eventos - Estruturacao Estrategica v2.pptx` (raiz do projeto)

---

## Processo de Execução

### Step 0 — Leitura dos Contextos e Localização do Template

1. Leia os três arquivos de context/ do cliente ativo.
2. Template fixo: `[Kick-off] Globo Eventos - Estruturacao Estrategica v2.pptx` na raiz do projeto.
3. Identifique o produto ativo em `produtos/` para definir o caminho de salvamento.
4. Verifique se python-pptx está disponível: `pip show python-pptx`. Se não estiver: `pip install python-pptx`.

---

### Step 1 — Extração e Organização dos Dados por Slide

Organize os dados dos context files mapeados para cada slide que precisa ser preenchido.

**Estrutura do template (22 slides) — slides que exigem dados do cliente:**

| Slide | Seção | Dados necessários | Fonte |
|---|---|---|---|
| 6 | Equipe V4 | Nomes e cargos do time alocado | [A CONFIRMAR — perguntar ao consultor antes de rodar] |
| 8 | Sobre a Empresa | Nome, segmento, tempo de mercado, clientes atuais, faturamento, momento estratégico | business.md |
| 9 | Produtos e Serviços | Lista de serviços, ticket médio, diferenciais, posicionamento | business.md |
| 11 | Benchmarking | Lista de concorrentes com posicionamento | gtm.md |
| 12 | Processo Comercial | Funil, CRM, objeções, pós-venda, time comercial | gtm.md |
| 13 | Objetivos | Metas declaradas | business.md |
| 14 | Público e Mercado | ICP atual, ICP desejado, geografia, lead qualificado | gtm.md + business.md |
| 15 | Sobre o Design | Presença digital atual, ativos, identidade visual | constraints.md + gtm.md |
| 17 | Assessment & Dados | Plataformas, ferramentas, CRM, integrações | constraints.md |

**Slides estáticos — NÃO modificar:**
- Slides 1–5: Capa, cronograma, etapas, divisória kickoff, agenda
- Slides 7, 10, 16, 18–19: Dinâmica pessoal, divisórias de seção, background
- Slides 20–22: Summary semanal, fechamento

---

### Step 2 — Geração do PPTX via python-pptx

Escreva e execute um script Python que:

1. **Copia o template** para o destino: `clientes/[nome-cliente]/produtos/[produto-ativo]/outputs/slides/kickoff-[nome-cliente].pptx`
2. **Abre o arquivo copiado** com `python-pptx`
3. **Para cada slide relevante**, localiza as caixas de texto e substitui o conteúdo com os dados do cliente
4. **Salva o arquivo**

**Estratégia de substituição:**
- Iterar sobre `prs.slides[N].shapes` para cada slide relevante (índice base 0, então slide 8 = índice 7)
- Para cada shape com `has_text_frame == True`, inspecionar os parágrafos e runs
- Substituir texto via `run.text =` (nunca via `paragraph.text =`) para preservar formatação
- Campos sem dado nos context files: inserir `"[A CONFIRMAR NO KICKOFF]"` como placeholder

**Exemplo de padrão para substituição:**
```python
from pptx import Presentation
from pptx.util import Pt
import copy, shutil

template_path = "caminho/template.pptx"
output_path = "caminho/output.pptx"
shutil.copy(template_path, output_path)

prs = Presentation(output_path)

def replace_in_shape(shape, replacements):
    if shape.has_text_frame:
        for para in shape.text_frame.paragraphs:
            for run in para.runs:
                for old, new in replacements.items():
                    if old in run.text:
                        run.text = run.text.replace(old, new)

# Dicionário de substituições por slide
# ...
prs.save(output_path)
```

---

### Step 3 — Validação e Entrega

1. Após gerar o PPTX, listar quais slides foram preenchidos e quais campos ficaram como `[A CONFIRMAR NO KICKOFF]`.
2. Informar o caminho do arquivo gerado.
3. Alertar o consultor sobre slides que precisam de revisão manual (especialmente slide 6 — equipe, e slide 15 — design/ativos visuais).

---

### Step 4 (Opcional) — Ajustes Visuais com /v4-slides

Use `/v4-slides` quando:
- O template gerado precisar de ajustes visuais significativos (reconstrução de slides, re-layout)
- Novos slides precisarem ser adicionados ao deck além do template padrão
- A identidade visual V4 precisar ser reaplicada (cores, logo, tipografia) após manipulação do XML

> **Não usar no fluxo padrão** — `python-pptx` preserva a identidade visual do template ao substituir apenas texto. O `/v4-slides` é para casos onde o template em si precisa ser alterado ou expandido.

---

## 🛑 Regras de Ouro

- **NUNCA inventar dados** — campos ausentes nos context files recebem `[A CONFIRMAR NO KICKOFF]`
- **NÃO modificar slides estáticos** — apenas os slides de dados do cliente listados no Step 1
- **NÃO usar fontes externas** — apenas os três arquivos de context/
- **Preservar identidade visual do template** — substituir apenas texto, nunca cores, fontes ou layouts

---

## Formato de Saída

Arquivo gerado em: `clientes/[nome-cliente]/produtos/[produto-ativo]/outputs/slides/kickoff-[nome-cliente].pptx`

Relatório no chat após execução:
```
✅ PPTX gerado: clientes/[...]/outputs/slides/kickoff-[cliente].pptx
   Slides preenchidos: 8, 9, 11, 12, 13, 14, 15, 17
   Campos [A CONFIRMAR NO KICKOFF]: [lista]
   Slides que precisam revisão manual: [lista]
```
