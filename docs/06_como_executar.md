# Fase 6 — Disponibilização: como executar

Notebook: [`notebooks/06_deployment.ipynb`](../notebooks/06_deployment.ipynb)

## Objetivo

Gerar a página de resultados autónoma, a documentação de atualização e o pacote ZIP do projeto. Lê a avaliação do 05; não faz nova recolha, previsão ou seleção de modelos.

## Entradas

`data/output/sns_avaliacao_resumo.json` e todos os ficheiros avaliados no 05 (as assinaturas são verificadas antes de gerar a página). O resumo tem de incluir as explicações e os exemplos das hipóteses: se o notebook avisar que faltam, executar primeiro o 05.

## Saídas

| Ficheiro | Conteúdo |
|---|---|
| `docs/06_resultados_sns.html` | Página autónoma: filtros por mês, região e ordenação, gráficos e cartões das hipóteses |
| `docs/06_disponibilizacao_e_atualizacao.md` | Decisões de disponibilização e manutenção |
| `docs/06_README_proposto.md`, `docs/06_requirements_propostos.txt` | Propostas geradas a partir da execução (o `README.md` e o `requirements.txt` da raiz não são substituídos) |
| `docs/06_disponibilizacao_manifesto.json` | Lista e assinaturas dos ficheiros do pacote |
| `data/analytics/06_*` | Gráficos da página, inventário e verificações |
| `data/output/Projeto_SNS.zip` | Pacote local do projeto (só é criado se todos os ficheiros essenciais existirem; não é versionado) |

## Executar

1. Executar antes o 05.
2. Selecionar o kernel do projeto e executar com **Run All**. Bibliotecas: `pandas` e `matplotlib`.
3. Abrir `docs/06_resultados_sns.html` com duplo clique (se já estiver aberta, **Ctrl + F5**).
4. Guardar todos os notebooks (**Ctrl + S**) e executar novamente a **última célula de código**, para o ZIP incluir as versões guardadas.

## Verificar a página

- Os filtros de mês, região e ordenação alteram a tabela e os totais.
- Os quatro cartões das hipóteses mostram o resultado real, o exemplo fictício (identificado como tal) e o botão **Ver detalhe técnico**.
- As hipóteses e os gráficos mostram o período completo: não mudam com os filtros.

## Entrega

O projeto é entregue pelo repositório GitHub ([annatagus/sns](https://github.com/annatagus/sns)). Antes do último *push*:

1. Executar os notebooks 02 a 06 com **Run All** e guardá-los, para os outputs ficarem atualizados.
2. Confirmar que o `.gitattributes` vai no commit e registar os ficheiros de `data/` sem conversão de finais de linha. O `.gitignore` já exclui os ZIP, mas o `Projeto_SNS.zip` continua seguido pelo Git até ser retirado:

   ```bash
   git rm --cached data/output/Projeto_SNS.zip
   git add --renormalize .
   git add -A
   git commit -m "Versão final do projeto"
   git push
   ```

3. Fazer um clone limpo numa pasta temporária e executar o `02` para confirmar que as assinaturas são aceites.

Se o inventário indicar ficheiros essenciais em falta, a página fica criada mas o ZIP não: colocar os ficheiros indicados e executar novamente a célula de inventário e a última célula.
