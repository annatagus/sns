# Cobertura de médico de família — SNS

Este repositório contém o projeto prático desenvolvido no âmbito do curso **AIDAPT-04** da **cegid Academy**.

## Responsáveis

- **Raquel Cunha** — GitHub: [@annatagus](https://github.com/annatagus)
- **Tiago Rodrigues** — GitHub: [@Tiago-Alex](https://github.com/Tiago-Alex)

## Objetivo

Análise dos inscritos nos cuidados de saúde primários em Portugal Continental, por unidade e região de saúde. O projeto compara o número e a percentagem de inscritos sem médico, acompanha a evolução e avalia previsões históricas a um mês.

## Consultar os resultados

Abrir [a página de resultados](docs/06_resultados_sns.html) num navegador. Funciona localmente, sem servidor: permite escolher mês, região e ordenação dos rankings. A página inclui os dados da tabela e os gráficos. Os quatro cartões das hipóteses apresentam explicações em linguagem simples, resultados calculados na avaliação, exemplos fictícios e a utilidade das comparações. Os detalhes técnicos podem ser abertos em cada cartão. Os filtros alteram a tabela e os totais; as hipóteses e os gráficos continuam a representar o período global.

Período principal: **2024-01 a 2026-06**. Recolha: 2026-10-13T13:34:39.656847+00:00 (UTC). Há 39 registos mensais no principal; a evolução por unidade e a previsão usam 38 séries completas.

Na avaliação desta execução, a abordagem escolhida na validação foi **Último valor**. O seu MAE no teste foi 0.417 pontos percentuais; a referência de repetir o último valor teve 0.417 pp. Manter a referência simples como comparação principal; não foi demonstrado ganho da abordagem selecionada. Disponibilizar também os resultados dos modelos para transparência.

## Fonte e período

- [Indicador histórico do Portal da Transparência do SNS](https://transparencia.sns.gov.pt/explore/assets/utentes-inscritos-em-cuidados-de-saude-primarios/).
- [Metadados e API](https://transparencia.sns.gov.pt/api/explore/v2.1/catalog/datasets/utentes-inscritos-em-cuidados-de-saude-primarios).
- Histórico bruto preservado desde 2016. Recolha pela API oficial; sem scraping nesta versão.
- Recorte desde janeiro de 2024 devido à reorganização em ULS, com alterações territoriais. [Enquadramento da ERS](https://www.ers.pt/pt/atividade/supervisao/selecionar/alertas-de-supervisao/2024/alertas/alerta-de-supervis%C3%A3o-n-%C2%BA-1-2024/).
- Fim em junho de 2026 devido à mudança de regras e definição do indicador a partir de julho. Não juntar os dois indicadores como uma série contínua.

## Organização

| Local | Conteúdo |
|---|---|
| notebooks/ | Um notebook por fase CRISP-DM, com decisões e resultados. |
| data/input/ | Histórico bruto e metadados, preservados. |
| data/output/ | Dados preparados, previsões e resumos. |
| data/analytics/ | Verificações, tabelas, gráficos e métricas. |
| data/models/ | Pipelines guardadas e registo da seleção/modelação. |
| src/ | Funções reutilizáveis de recolha. |
| docs/ | Decisões, instruções e página de resultados. |
| media/ | Imagens de apoio, quando existirem. |

## Preparar um ambiente novo

O Python usado na modelação foi 3.12.14. As versões das bibliotecas estão em `data/models/04_execucao_modelacao.json`. Usar preferencialmente a mesma versão de Python e as dependências registadas para reproduzir o treino; podem existir pequenas diferenças entre plataformas e versões.

Na raiz do projeto, em CMD do Windows:

```cmd
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```

No VS Code, selecionar esse ambiente em **Select Kernel → Python Environments**. É necessário ter as extensões Python e Jupyter disponíveis. Não é preciso recriar o ambiente se já tens um kernel funcional com as bibliotecas.

## Executar

Executar os notebooks por ordem, com Run All:

1. [01 — Entendimento do negócio](notebooks/01_business_understanding.ipynb).
2. [02 — Entendimento dos dados](notebooks/02_data_understanding.ipynb).
3. [03 — Preparação](notebooks/03_data_preparation.ipynb).
4. [04 — Modelação](notebooks/04_modeling.ipynb).
5. [05 — Avaliação](notebooks/05_evaluation.ipynb).
6. [06 — Disponibilização](notebooks/06_deployment.ipynb).

O 02 reutiliza a recolha existente depois de verificar as assinaturas. Os restantes leem os ficheiros guardados; o 04 treina modelos. Os resultados gerados podem ser atualizados ao executar novamente cada fase. Se mudares uma fase, executar novamente as fases que dependem dela.

O 06 guarda a página em `docs/06_resultados_sns.html` e prepara `data/output/Projeto_SNS.zip` quando os ficheiros essenciais estiverem presentes. O pacote reúne a versão local do projeto e exclui ambientes virtuais, caches e o próprio pacote. Depois de Run All, guardar os notebooks com **Ctrl + S** e executar novamente a última célula do 06, para incluir no ZIP as versões guardadas.

Se apenas atualizaste os textos dos cartões, executar o **05 atualizado e depois o 06**; não é necessário voltar a treinar o 04. Se a única alteração foi à documentação e ao modelo de README no 06, basta executar o **06** sobre a avaliação já gerada.

O 06 preserva `README.md` e `requirements.txt` existentes e guarda propostas em `docs/`. O README desta versão já inclui os responsáveis e o curso. Numa nova recolha ou avaliação, comparar `docs/06_README_proposto.md` com o README da raiz e integrar as alterações necessárias.

O `.gitignore` base exclui ambientes virtuais, caches, ficheiros temporários, configurações de segredos e pacotes ZIP. Os notebooks, os dados públicos, os resultados, os gráficos e os modelos do projeto continuam disponíveis para versionamento. O `.gitignore` não retira ficheiros que já estejam seguidos pelo Git.

## Interpretação e limites

- Inscritos não são população residente; não extrapolar o indicador para todos os habitantes.
- A categoria sem médico por opção fica separada de sem médico atribuído.
- Cada mês é uma fotografia: não somar pessoas entre meses. Percentagens regionais usam os totais, não a média simples das unidades.
- A correspondência territorial dos dois nomes da Póvoa/Vila do Conde não foi confirmada. Ambos ficam no principal, mas fora das séries completas de evolução e previsão.
- A janela exata das taxas de consultas de um ano continua pendente. A Q5 não foi avaliada nesta versão.
- Meses e unidades não são observações independentes; faixas de dimensão são aproximadas. As associações não identificam causas.
- O teste usa a recolha atual, que pode incluir revisões. A escolha foi feita pela validação temporal; o teste não serviu para ajustar os modelos.
- A página apresenta uma análise histórica do indicador antigo. Não constitui previsão operacional do novo indicador nem determina distribuição de médicos.

## Atualização

Se a fonte mudar, recolher para uma pasta separada e confirmar esquema, definições e territórios antes de atualizar a análise. Não substituir os brutos guardados sem preservar a recolha anterior. Para o indicador novo, definir um projeto/série próprios; não reaproveitar o teste antigo como avaliação independente depois de ajustar modelos com os seus resultados.


## Por fazer

- [ ] Confirmar a correspondência territorial entre as duas designações da Póvoa de Varzim/Vila do Conde antes de as ligar numa série única. A análise atual mantém essa limitação explícita.
- [ ] Confirmar a janela exata das taxas de consultas de um ano antes de avaliar a Q5. As conclusões atuais não usam essas taxas.
- [ ] Na versão local a entregar, abrir a página num navegador, experimentar os filtros e ler os quatro cartões, incluindo os detalhes técnicos.
- [ ] Guardar os notebooks depois de executar, voltar a executar a última célula do 06 e conferir o ZIP final.
