# Executar o 05 — Avaliação

O notebook avalia as previsões históricas e responde às perguntas e hipóteses do projeto. Não volta a treinar modelos e mantém a seleção feita na validação do 04.

## Antes de executar

1. Colocar `05_evaluation.ipynb` em `notebooks/`, na raiz do projeto que contém `data/`.
2. Ter os resultados do 03 e do 04 já gerados. Se apenas atualizaste as explicações dos cartões, não precisas de repetir essas fases.
3. Selecionar o mesmo kernel Python. São necessários `pandas`, `numpy` e `matplotlib`; a apresentação das tabelas usa IPython do kernel. O 05 não precisa de importar scikit-learn nem de carregar os modelos joblib.

Entradas de `data/output/`: `sns_csp_principal.csv`, `sns_csp_series_completas.csv`, `sns_csp_regional.csv`, `sns_faixas_dimensao.json`, `sns_preparacao_manifesto.json` e `sns_previsoes_teste.csv`.

Entradas de `data/models/`: `04_selecao_modelo.json` e `04_execucao_modelacao.json`.

## Executar e conferir

1. Fazer **Run All**, desde a primeira célula.
2. Confirmar as verificações de entrada, as métricas do teste e as respostas às perguntas e hipóteses.
3. Guardar o notebook com **Ctrl + S**.
4. Executar o [06 — Disponibilização](../notebooks/06_deployment.ipynb) para atualizar a página e o pacote.

O 05 cria as pastas de resultados que faltarem. As entradas são apenas lidas e as assinaturas são conferidas. Caminhos guardados em Windows ou Linux são normalizados antes da comparação.

Se alterares o 03, volta a executar o 04 e depois o 05. Não misturar previsões e observados de execuções diferentes. A correção dos textos dos cartões não exige novo treino.

## Hipóteses e exemplos

Na secção 9, as quatro hipóteses são guardadas com título, explicação, evidência calculada, exemplo fictício, utilidade, interpretação e detalhe técnico. Os exemplos ajudam a ler os resultados; os seus números não pertencem aos dados reais do SNS.

Os resultados reais continuam ligados às variáveis da execução. Não substituir esses cálculos por números escritos manualmente. Os exemplos e as explicações passam para `data/analytics/05_avaliacao_hipoteses.csv`, `data/output/sns_avaliacao_resumo.json` e `docs/05_conclusoes_avaliacao.md`.

## Limites que se mantêm

- O teste não serve para escolher novos candidatos ou ajustar parâmetros depois de conhecer os erros.
- As associações e diferenças são descritivas; não demonstram causas nem determinam quantos médicos contratar.
- A Q5 continua pendente da definição da janela das consultas.
- A correspondência territorial das duas designações da Póvoa/Vila do Conde continua por confirmar.
- O indicador histórico analisado termina em junho de 2026; não representa uma previsão atual do indicador novo.
