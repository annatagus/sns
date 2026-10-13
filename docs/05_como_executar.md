# Executar o 05_evaluation

1. Colocar 05_evaluation.ipynb em notebooks/ do projeto.
2. Executar antes o 03 e o 04. O 05 usa os ficheiros já gerados no teu PC e não volta a treinar modelos.
3. Entradas de data/output/: sns_csp_principal.csv, sns_csp_series_completas.csv, sns_csp_regional.csv, sns_faixas_dimensao.json, sns_preparacao_manifesto.json e sns_previsoes_teste.csv. Entradas de data/models/: 04_selecao_modelo.json e 04_execucao_modelacao.json.
4. Selecionar o mesmo kernel e executar Run All. Bibliotecas necessárias: pandas, numpy e matplotlib; display usa IPython do kernel. Não é necessário importar scikit-learn ou carregar joblib nesta fase.
5. Confirmar a mensagem final, as respostas e as limitações.

O ZIP inclui apenas os novos ficheiros do 05 e os resultados desta execução. Não inclui cópias das entradas do 03/04: manter os resultados que geraste no teu PC. Ao executar novamente o 05, os resultados desta fase são atualizados com essas entradas locais. Pode haver pequenas diferenças entre versões das bibliotecas usadas para treinar o 04.

O notebook verifica assinaturas e a correspondência das previsões com os observados preparados. Se alterares o 03, volta a executar o 04 e só depois o 05; não misturar resultados de execuções diferentes.

O link no final do 05 aponta para 06_deployment.ipynb, que será criado na fase seguinte. Para ligar o 04 ao 05, adicionar uma célula Markdown ao final do 04 com:

[Avançar para o 05 — Avaliação](./05_evaluation.ipynb)

Esta versão avalia a escolha feita no 04 pela validação. Não escolher um novo modelo pelo teste nem ajustar parâmetros depois de ver o resultado final. Q5 continua pendente da definição da janela das consultas; a previsão histórica termina em junho de 2026.
