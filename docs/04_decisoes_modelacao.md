# Fase 4 — Modelação

> Ficheiro gerado automaticamente pelo notebook `04_modeling.ipynb`. Alterações manuais são substituídas na próxima execução.

Entrada: sns_csp_modelacao.csv, preparada no 03 e verificada contra o manifesto.

## Decisões

- Separação por mês-alvo: treino inicial até junho de 2025, validação julho–dezembro de 2025, teste janeiro–junho de 2026. Sem divisão aleatória.
- Variáveis explícitas do manifesto; retirada variacao_sem_medico_pp por ser combinação exata da percentagem atual e lag1. Taxas de consultas, alvo e campos de identificação/avaliação excluídos dos preditores.
- Referência: repetir último valor. Candidatos aprendidos: regressão linear e Random Forest A/B previamente definidos. Configurações e versões no 04_execucao_modelacao.json.
- Transformadores ajustados apenas no treino; após seleção, novo ajuste apenas no desenvolvimento completo.
- Seleção por menor MAE na validação, incluindo a referência. Empate até 1e-10 pp favorece simplicidade. Previsões limitadas a 0–100 pela regra definida antes da comparação; valores brutos guardados.
- Abordagem selecionada: ultimo_valor. Melhor candidato aprendido: regressao_linear. Configuração Random Forest que avança: random_forest_b.
- MAE referência na validação: 0.689268 pp. MAE selecionado: 0.689268 pp. Ganho: 0.000000 pp.
- Treino final com 760 linhas; previsões para 228 linhas de teste, mesmas unidades e meses para as três abordagens finais. Modelos fixos, origens mensais móveis e dados observados até cada origem.
- O teste não foi avaliado nesta fase. A seleção deve ser mantida no 05 mesmo que o ranking no teste mude.

## Ficheiros para o 05

- data/output/sns_previsoes_teste.csv: observados e previsões alinhados por região, unidade, origem e mês-alvo.
- data/models/04_selecao_modelo.json: escolha feita antes de avaliar o teste.
- data/analytics/04_metricas_treino_validacao.csv: resultados usados no desenvolvimento.
- data/models/04_execucao_modelacao.json: configuração, versões e assinaturas.

## Limitações

Só 38 séries completas; nomes estáveis não garantem continuidade territorial. Amostra curta e unidades/meses dependentes. Recolha atual pode conter revisões. Indicador antigo até junho de 2026; não extrapolar para a quebra de definição de julho. Nenhum coeficiente ou importância constitui evidência causal.

Fontes técnicas: [Pipeline](https://scikit-learn.org/stable/modules/compose.html), [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) e [prevenção de fuga de informação](https://scikit-learn.org/stable/common_pitfalls.html).
