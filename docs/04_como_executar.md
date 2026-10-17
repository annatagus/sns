# Fase 4 — Modelação: como executar

Notebook: [`notebooks/04_modeling.ipynb`](../notebooks/04_modeling.ipynb)

## Objetivo

Comparar a referência simples (repetir o último valor) com uma regressão linear e duas configurações de Random Forest, escolher a abordagem pela **validação temporal** e guardar as previsões do teste — sem calcular ainda as métricas do teste.

## Entradas

- `data/output/sns_csp_modelacao.csv`
- `data/output/sns_preparacao_manifesto.json`

O notebook confirma que a assinatura do CSV coincide com a registada no manifesto do 03.

## Saídas

| Ficheiro | Conteúdo |
|---|---|
| `data/models/04_selecao_modelo.json` | Escolha feita na validação, antes de ver o teste |
| `data/models/04_execucao_modelacao.json` | Versões das bibliotecas, parâmetros e assinaturas |
| `data/models/04_regressao_linear.joblib`, `04_random_forest_*.joblib` | Pipelines treinadas no desenvolvimento completo |
| `data/output/sns_previsoes_validacao.csv` | Previsões da validação |
| `data/output/sns_previsoes_teste.csv` | Observados e previsões do teste, alinhados por unidade e mês |
| `data/analytics/04_*.csv`, `04_mae_validacao.png` | Divisão temporal, métricas e verificações |
| `docs/04_decisoes_modelacao.md` | Decisões da modelação (gerado pelo notebook) |

## Divisão temporal (por mês-alvo)

| Bloco | Meses-alvo | Linhas |
|---|---|---:|
| Treino inicial | 2024-05 a 2025-06 | 532 |
| Validação | 2025-07 a 2025-12 | 228 |
| Desenvolvimento completo | 2024-05 a 2025-12 | 760 |
| Teste reservado | 2026-01 a 2026-06 | 228 |

## Executar

Selecionar o kernel do projeto e executar com **Run All**. Bibliotecas: `pandas`, `numpy`, `matplotlib`, `scikit-learn` (≥ 1.2, por causa de `sparse_output` no `OneHotEncoder`) e `joblib`. As versões usadas estão em `04_execucao_modelacao.json`; para carregar os `.joblib` guardados, usar de preferência as mesmas versões (`requirements.txt`).

## Verificar

- `04_verificacoes_execucao.csv`: todas as verificações com `passou = True`.
- A seleção não deve mudar depois de ver o teste. A referência é elegível e foi a escolhida nesta execução.

Ao repetir, os resultados desta fase são substituídos; as entradas do 03 são apenas lidas. Se o 03 mudar, executar novamente o 04 e depois o 05 e o 06.
