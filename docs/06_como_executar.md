# Executar o 06 — Disponibilização

O notebook cria uma página local de resultados, propostas de documentação e um pacote do projeto. Lê a avaliação do 05; não volta a treinar nem escolhe modelos.

## Antes de executar

1. Colocar `06_deployment.ipynb` em `notebooks/`, na raiz do projeto que contém `data/`.
2. Executar primeiro o **05 atualizado**, para que `data/output/sns_avaliacao_resumo.json` contenha as explicações e os exemplos dos cartões. Se já o executaste e apenas atualizaste esta documentação e o modelo de README do 06, não precisas de repetir o 05.
3. Usar o mesmo kernel com `pandas` e `matplotlib`. Não é necessário scikit-learn nesta fase.

O 06 confere o resumo e os ficheiros avaliados no 05. As entradas de dados e previsões são apenas lidas. O notebook cria as pastas de resultados que faltarem.

## Gerar e consultar a página

1. Fazer **Run All**.
2. Abrir `docs/06_resultados_sns.html` com duplo clique num navegador. Se a página já estiver aberta, atualizar com **Ctrl + F5**.
3. Experimentar os filtros de mês, região e ordenação. Conferir que alteram a tabela e os totais.
4. Ler os quatro cartões das hipóteses e abrir **Ver detalhe técnico**. Os exemplos estão identificados como fictícios e separados dos resultados reais.

Os filtros não recalculam as hipóteses nem os gráficos: estes continuam a mostrar a análise global do período. O HTML contém os dados e as imagens; pode abrir sem instalação, servidor ou nova recolha.

## README, dependências e .gitignore

O 06 preserva `README.md` e `requirements.txt` existentes. As propostas ficam em `docs/06_README_proposto.md` e `docs/06_requirements_propostos.txt`. Quando os ficheiros da raiz não existem, o notebook cria-os.

A proposta de README inclui o curso AIDAPT-04 da cegid Academy, os responsáveis Raquel Cunha e Tiago Rodrigues e os seus perfis GitHub. O README fornecido nesta atualização já integra essa informação. Se tiveres acrescentado conteúdo próprio ao teu README, juntar os textos antes de o substituir.

O `.gitignore` base acompanha esta atualização. Copiá-lo para a raiz, ou integrar as suas regras num `.gitignore` próprio. O notebook inclui esse ficheiro no pacote quando existe, mas não o cria nem o altera. As regras excluem ambientes, caches, temporários, segredos de configuração e ZIP; mantêm os dados públicos, os resultados, os modelos e os notebooks disponíveis para versionamento. Ficheiros já seguidos pelo Git não deixam de o ser por adicionar uma regra.

## Preparar o pacote final

1. Guardar os notebooks com **Ctrl + S** depois da execução.
2. Voltar a executar a última célula de código do 06. Esta célula lê os ficheiros guardados em disco e atualiza o pacote `data/output/Projeto_SNS.zip` e o respetivo registo.
3. Abrir o ZIP e confirmar os ficheiros esperados.

O pacote completo reúne a versão local do projeto: notebooks, dados, código, documentação e imagens, com README e dependências. Exclui ambientes virtuais, caches, logs, ficheiros ocultos em geral e outros ZIP; o `.gitignore` da raiz é incluído explicitamente.

Se o inventário indicar ficheiros essenciais em falta, a página pode ficar disponível, mas o pacote completo não é criado. Colocar os ficheiros indicados no projeto e executar novamente a célula de inventário e a última célula.

Esta fase não publica o projeto num serviço externo. Mantêm-se as limitações da análise e as duas definições pendentes indicadas no README.
