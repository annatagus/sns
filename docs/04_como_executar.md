# Executar o 04_modeling

1. Copiar notebooks/04_modeling.ipynb para notebooks/ do projeto.
2. Confirmar data/output/sns_csp_modelacao.csv e data/output/sns_preparacao_manifesto.json, produzidos no 03. O ZIP inclui cópias destes dois ficheiros; se já tiveres os mesmos, não precisas de os substituir.
3. Selecionar o mesmo kernel Python usado nos outros notebooks. Bibliotecas: pandas, numpy, matplotlib, scikit-learn e joblib. Se faltar alguma, usar uma célula com %pip install pandas numpy matplotlib scikit-learn joblib. Reiniciar o kernel se necessário.
4. Fazer Run All. O notebook cria data/analytics/, data/models/ e docs/ se faltarem.
5. Confirmar a tabela de validação, a seleção e as verificações finais.

O código de OneHotEncoder usa sparse_output, disponível em scikit-learn >= 1.2. A execução entregue foi verificada em scikit-learn 1.8.0; as restantes versões estão em data/models/04_execucao_modelacao.json. Para carregar os modelos guardados, usar preferencialmente o mesmo ambiente; executar novamente o notebook permite treinar na versão instalada.

A fase 04 não calcula métricas do teste. Guarda as previsões e a seleção antes da avaliação no 05. Não mudar candidatos com base no teste. A referência é elegível para a escolha final.

Ao repetir, atualiza apenas os resultados desta fase e os modelos com os nomes usados. Os dois ficheiros de entrada do 03 são apenas lidos. A seleção atual e os nomes dos modelos usados ficam registados em 04_selecao_modelo.json.

A modelação é histórica, sobre 38 séries completas do indicador antigo. Não constitui previsão atual do novo indicador de julho de 2026.
