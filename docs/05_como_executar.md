# Fase 5 — Avaliação: como executar

Notebook: [`notebooks/05_evaluation.ipynb`](../notebooks/05_evaluation.ipynb)

## Objetivo

Avaliar no teste reservado a escolha feita no 04, verificar a consistência dos erros por mês e por unidade, e responder às perguntas Q1–Q6 e às hipóteses H1–H4. Não treina nem carrega modelos.

## Entradas

- `data/output/`: `sns_csp_principal.csv`, `sns_csp_series_completas.csv`, `sns_csp_regional.csv`, `sns_faixas_dimensao.json`, `sns_preparacao_manifesto.json`, `sns_previsoes_teste.csv`
- `data/models/`: `04_selecao_modelo.json`, `04_execucao_modelacao.json`

As assinaturas são verificadas contra o manifesto do 03 e o registo do 04 (os caminhos gravados em Windows ou Linux/macOS são normalizados).

## Saídas

- `data/analytics/05_*.csv` e `05_*.png` — métricas do teste, erros por mês e unidade, rankings, evolução, H3 e H4, respostas e critérios de sucesso.
- `data/analytics/05_avaliacao_hipoteses.csv` — as quatro hipóteses com explicação, evidência, exemplo, utilidade, interpretação e detalhe técnico.
- `data/output/sns_erros_teste.csv` — erros linha a linha.
- `data/output/sns_avaliacao_resumo.json` — resumo usado pelo 06 (página de resultados).
- `docs/05_conclusoes_avaliacao.md` — conclusões (gerado pelo notebook).

## Executar

Executar antes o 03 e o 04. Depois, selecionar o kernel do projeto e executar com **Run All**. Bibliotecas: `pandas`, `numpy` e `matplotlib`. Por fim, executar o [06](../notebooks/06_deployment.ipynb) para atualizar a página.

Se só mudarem os textos das hipóteses, basta executar o 05 e depois o 06: não é preciso voltar a treinar o 04.

## Hipóteses e exemplos

Na secção 9, cada hipótese é guardada com título, explicação em linguagem simples, evidência calculada, **exemplo fictício**, utilidade, interpretação e detalhe técnico. Os números dos exemplos servem só para explicar a comparação; não são dados do SNS.

Os resultados reais vêm sempre das variáveis da execução: não substituir esses cálculos por números escritos à mão.

## Verificar

- `05_validacoes_entrada.csv`: todas as verificações com `passou = True`.
- A mensagem final `Avaliação concluída`, as tabelas de perguntas e hipóteses e o ficheiro de conclusões.

## Limites que se mantêm

- O teste não serve para escolher novos candidatos nem ajustar parâmetros depois de conhecer os erros.
- As associações e diferenças são descritivas: não demonstram causas nem determinam quantos médicos contratar.
- A Q5 continua pendente da definição da janela das consultas.
- A correspondência territorial das duas designações da Póvoa de Varzim / Vila do Conde continua por confirmar.
- O indicador analisado termina em junho de 2026; não é uma previsão do indicador novo.

Se o 03 ou o 04 mudarem, executar novamente o 04 e só depois o 05: não misturar resultados de execuções diferentes.
