# Fase 3 — Preparação dos dados: como executar

Notebook: [`notebooks/03_data_preparation.ipynb`](../notebooks/03_data_preparation.ipynb)

## Objetivo

Aplicar as decisões D01–D08 (recorte temporal, nomes e tipos, qualidade, continuidade, percentagens, faixas de dimensão, pares para previsão e taxas de consultas) e guardar os datasets tratados. Não faz nova recolha nem depende de `src/recolha_sns.py`.

## Entradas

Os três ficheiros da recolha em `data/input/` (ver [02_como_executar.md](02_como_executar.md)). As assinaturas são verificadas antes de ler os dados.

## Saídas

| Ficheiro em `data/output/` | Uso |
|---|---|
| `sns_csp_principal.csv` | Todas as linhas do período principal (rankings e geografia) |
| `sns_csp_series_completas.csv` | 38 séries com os 30 meses (evolução por unidade) |
| `sns_csp_regional.csv` | Totais e percentagens ponderadas por região e mês |
| `sns_csp_pares_mensais.csv` | Pares de meses consecutivos (referência simples) |
| `sns_csp_modelacao.csv` | Pares com histórico completo, para os modelos |
| `sns_faixas_dimensao.json` | Limites fixos das faixas de dimensão (H4) |
| `sns_preparacao_manifesto.json` | Contagens, assinaturas, variáveis permitidas e pendências |

Também: `data/analytics/03_*.csv` (verificações) e `docs/03_decisoes_preparacao.md` (gerado pelo notebook).

## Executar

Selecionar o kernel do projeto e executar com **Run All**. Biblioteca: `pandas`.

## Verificar

- `03_qualidade_historico.csv`: todas as verificações com 0 ocorrências.
- `03_validacoes_finais.csv`: todas as verificações com `passou = True`.
- `03_fluxo_registos.csv`: 6 450 linhas no histórico, 1 170 no recorte, 1 140 nas séries completas.

O notebook **para com erro** se encontrar problemas de qualidade, meses em falta ou uma cobertura mensal diferente dos 39 registos esperados. Nesse caso, investigar antes de alterar o código: não corrigir valores silenciosamente.

## Ler os resultados na fase seguinte

Os CSV usam vírgula como separador e ponto decimal (UTF-8 com BOM). Para a modelação:

```python
pd.read_csv("data/output/sns_csp_modelacao.csv", parse_dates=["mes", "mes_alvo"])
```

Usar apenas as variáveis listadas no manifesto. O alvo, o mês-alvo, o conjunto e a previsão de referência são campos de controlo e nunca entram como preditores.
