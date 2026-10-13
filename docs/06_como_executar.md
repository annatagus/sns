# Executar o 06_deployment

1. Colocar 06_deployment.ipynb em notebooks/ do projeto.
2. Executar antes o 05 corrigido para Windows, usando as tuas entradas locais do 03/04. O 06 lê sns_avaliacao_resumo.json e confere os ficheiros avaliados.
3. Usar o mesmo kernel com pandas e matplotlib. Não é necessário scikit-learn nesta fase.
4. Fazer Run All. Abrir docs/06_resultados_sns.html com duplo clique num navegador e experimentar mês, região e ordenação.
5. Guardar todos os notebooks com Ctrl + S e executar novamente a última célula de código para incluir as versões guardadas no pacote data/output/Projeto_SNS.zip.

O ZIP SNS_Fase06.zip contém apenas os novos ficheiros desta fase. Mantém os resultados do 03/04/05 que geraste no teu PC; não são substituídos. O pacote completo gerado pelo notebook usa a tua versão local do projeto.

README.md e requirements.txt existentes são preservados. As propostas completas ficam em docs/06_README_proposto.md e docs/06_requirements_propostos.txt para integração na revisão final. Se esses ficheiros não existirem, são criados na raiz.

O notebook cria as pastas de resultados que faltarem. Os ficheiros de entrada são apenas lidos. Ao repetir, atualiza apenas os resultados e notas do 06 e o ZIP gerado. O .gitignore não é alterado; ambientes virtuais, caches e outros ZIP são excluídos do pacote.

Se o inventário indicar ficheiros essenciais em falta, a página continua disponível, mas o pacote completo não é criado. Colocar os ficheiros indicados no projeto e executar novamente a célula de inventário e a última célula.

O HTML é autónomo: dados e gráficos incluídos, sem instalação, servidor ou nova recolha para consultar. A publicação externa não é feita por este notebook.
