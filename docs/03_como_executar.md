# Executar o 03_data_preparation

1. Colocar o notebook em notebooks/ na pasta do projeto.
2. Confirmar os três ficheiros da recolha do 02 em data/input/: utentes_csp_historico_bruto.csv, utentes_csp_metadados_api.json e utentes_csp_recolha.json.
3. Selecionar um kernel Python com pandas e Jupyter/IPython. No ambiente local, se faltar pandas: python -m pip install pandas. Não é necessário matplotlib nesta fase.
4. Executar Run All, por ordem, desde a primeira célula.
5. Confirmar as verificações finais e os ficheiros em data/output/ e data/analytics/.

O ZIP contém uma cópia exata da recolha usada no 02, o notebook, os resultados já gerados e as notas. Copiar as pastas para o projeto existente, mantendo os notebooks 01 e 02. Não é preciso substituir a recolha que já tens se for a mesma. Se existir outra recolha, preservá-la separadamente: não misturar CSV e metadados de recolhas diferentes.

O notebook cria data/output/, data/analytics/ e docs/ se faltarem. Requer a raiz com notebooks/ e data/. Não faz nova recolha nem depende de src/recolha_sns.py. Ao repetir, atualiza apenas os resultados desta fase; os três ficheiros de entrada são apenas lidos.

As contagens e datas nos outputs correspondem à recolha guardada de 13 de outubro de 2026. Se mudar a recolha, rever primeiro o 02 e as decisões de continuidade. O notebook interrompe se encontrar problemas de qualidade, meses em falta ou cobertura mensal diferente dos 39 registos esperados.

No 04, ler sns_csp_modelacao.csv com parse_dates=["mes", "mes_alvo"]. Ler a lista explícita de variáveis no sns_preparacao_manifesto.json. Nunca usar todas as colunas como entrada do modelo: alvo, mês-alvo, conjunto e previsão de referência são campos de avaliação/controlo.
