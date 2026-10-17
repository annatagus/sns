# Fase 2 — Entendimento dos dados: como executar

Notebook: [`notebooks/02_data_understanding.ipynb`](../notebooks/02_data_understanding.ipynb)

## Objetivo

Recolher (ou reutilizar) o histórico do indicador pela API oficial do SNS, confirmar a estrutura e a qualidade dos dados e explorar as perguntas Q1–Q4 e as hipóteses H1–H4 antes da preparação.

## Entradas

| Ficheiro | Origem |
|---|---|
| `data/input/utentes_csp_historico_bruto.csv` | CSV original exportado pela API |
| `data/input/utentes_csp_metadados_api.json` | Metadados publicados pela API |
| `data/input/utentes_csp_recolha.json` | Data, parâmetros e assinaturas SHA-256 da recolha |
| `src/recolha_sns.py` | Função `recolher_historico` |

Se os três ficheiros de `data/input/` existirem, são **reutilizados** depois de verificar as assinaturas; o notebook não volta à API. Se a pasta estiver vazia, é feita uma recolha nova.

## Saídas

- `data/analytics/02_*.csv` e `02_*.png` — dicionário, perfil das colunas, qualidade, cobertura mensal, continuidade, rankings, evolução e gráficos exploratórios.
- `data/analytics/02_resumo_exploracao.json` — resumo numérico da exploração.
- `docs/02_constatacoes_e_pendencias.md` — constatações e pendências para a fase 3 (gerado pelo notebook).

## Executar

1. Abrir a raiz do repositório no VS Code e selecionar o kernel `.venv` (ver [README](../README.md#-como-executar-o-projeto)).
2. Abrir o notebook e executar com **Run All**.

Bibliotecas: `pandas` e `matplotlib`.

## Verificar

- Secções 1 a 4: fonte, dicionário, leitura e qualidade numérica (todas as verificações com 0 ocorrências).
- Secções 5 e 6: passagem de 55 para 39 unidades em janeiro de 2024 e continuidade dos nomes no recorte.
- Secções 7 a 10: exploração das hipóteses, com as limitações explícitas.
- Secção 11: pendências para a preparação.

Valores esperados com a recolha de 13 de outubro de 2026: **6 450 linhas**, **126 meses** no histórico; **1 170 linhas** e **30 meses** no recorte de 2024-01 a 2026-06.

## Fazer uma recolha nova

Não substituir os ficheiros de `data/input/`. Alterar `PASTA_INPUT` na primeira célula de código para uma pasta vazia (por exemplo `raiz / "data" / "input" / "recolha_nova"`) e executar desde o início. Os notebooks seguintes leem `data/input/`; antes de os executar com a recolha nova, rever as decisões de continuidade do 02 e apontar o 03 para a nova pasta. A fonte pode ter revisto valores, pelo que os resultados podem mudar.

## Erros comuns

| Mensagem | Causa provável e solução |
|---|---|
| `O ficheiro bruto foi alterado … Apenas os finais de linha diferem` | O Git converteu CRLF/LF no checkout. Atualizar o repositório (`git pull`) para obter o `.gitattributes`; se persistir, repor os ficheiros com `git checkout HEAD -- data` (substitui alterações locais em `data/`). |
| `O ficheiro bruto foi alterado` | O CSV ou os metadados foram editados. Repor os ficheiros originais a partir do Git. |
| `A recolha está incompleta` | Falta um dos três ficheiros de `data/input/`. |
