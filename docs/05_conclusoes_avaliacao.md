# Fase 5 — Conclusões da avaliação

> Ficheiro gerado automaticamente pelo notebook `05_evaluation.ipynb`. Alterações manuais são substituídas na próxima execução.

Recolha: 2026-10-13T17:20:14.911883+00:00 (UTC). Âmbito: 2024-01 a 2026-06.

## Previsão

A referência teve MAE 0,417 pp. O melhor candidato aprendido escolhido na validação (Regressão linear) teve MAE 0,449 pp no teste. A escolha final do 04 foi Último valor e não superou a referência. O critério preditivo não foi cumprido; os resultados dos candidatos estão na tabela, sem nova seleção pelo teste.

- Último valor: MAE 0.417357 pp; RMSE 0.679343 pp; viés -0.165416 pp.
- Regressão linear: MAE 0.448916 pp; RMSE 0.696505 pp; viés -0.189219 pp.
- Random Forest B: MAE 0.582157 pp; RMSE 0.841621 pp; viés -0.289083 pp.

Seleção feita pela validação e mantida na avaliação. Mesmas unidades e meses para as abordagens. Teste com 6 meses-alvo e 38 unidades; modelos fixos com origens mensais móveis. Não houve novo treino nesta fase.

## Perguntas e hipóteses

- Q1: CSP da ULS Amadora / Sintra: 194 681 inscritos sem médico em 2026-06. Estado: respondida.
- Q2: CSP da ULS Estuário do Tejo: 47,74 %. Rankings e tabelas geográficas guardados; inscritos são o denominador. Estado: respondida.
- Q3: Nas 38 séries completas, 19 reduziram e 19 aumentaram a percentagem. Maior redução: CSP da ULS Cova da Beira (-15,09 pp); maior aumento: CSP da ULS Arrábida (13,22 pp). Estado: respondida com restrição de continuidade.
- Q4: As variações regionais foram calculadas a partir dos totais de todos os registos mensais. Ver 05_evolucao_regioes.csv; evolução não uniforme. Estado: respondida.
- Q5: Não avaliada nesta versão: falta confirmar a janela exata do indicador de um ano. Taxas preservadas, sem conclusões sobre consultas. Estado: pendente de definição.
- Q6: A referência teve MAE 0,417 pp. O melhor candidato aprendido escolhido na validação (Regressão linear) teve MAE 0,449 pp no teste. A escolha final do 04 foi Último valor e não superou a referência. O critério preditivo não foi cumprido; os resultados dos candidatos estão na tabela, sem nova seleção pelo teste. Estado: avaliada no teste reservado.


### H1 — O ranking por número de inscritos sem médico difere do ranking por percentagem

Uma unidade pode ter mais inscritos sem médico, mas uma percentagem menor do seu total.

**O que encontrámos:** Em 2026-06, 35 das 39 unidades mudam de posição quando usamos número ou percentagem. Mudar de posição não significa, por si só, que os rankings sejam completamente diferentes.

**Exemplo fictício:** Uma unidade com 40 mil pessoas sem médico em 200 mil inscritos tem 20% sem médico. Outra com 20 mil em 50 mil tem 40%. A primeira tem mais pessoas afetadas; a segunda tem uma maior proporção afetada.

**Para que serve:** Perceber a dimensão do problema através das duas medidas e identificar situações que merecem atenção por motivos diferentes.

**Como interpretar:** A hipótese é sustentada no último mês; convém consultar os dois rankings.

**Detalhe técnico:** Spearman entre os rankings: 0,938. Valores próximos de 1 indicam uma ordenação semelhante; uma troca de apenas uma posição já conta como diferença.

### H2 — A evolução da cobertura não é uniforme entre unidades e regiões

Comparamos a percentagem de inscritos sem médico no início e no fim do período, nas unidades com histórico completo.

**O que encontrámos:** Entre 2024-01 e 2026-06, a percentagem de inscritos sem médico diminuiu em 19 unidades e aumentou em 19, nas 38 unidades com histórico completo.

**Exemplo fictício:** Passar de 30% para 20% significa uma redução de 10 pontos percentuais. Passar de 20% para 30% representa um agravamento de igual dimensão.

**Para que serve:** Identificar unidades onde interessa investigar o que contribuiu para a melhoria ou para o agravamento.

**Como interpretar:** A evolução do conjunto pode esconder situações locais diferentes. Estes dados não explicam as causas das mudanças.

**Detalhe técnico:** A evolução por unidade usa 38 séries completas. A correspondência territorial dos dois nomes da Póvoa/Vila do Conde continua por confirmar e não foi unida automaticamente. A comparação dos extremos não descreve cada subida ou descida mensal.

### H3 — Um aumento dos inscritos pode estar associado a um aumento da percentagem sem médico

Nas 38 unidades com histórico completo, comparámos o crescimento do total de inscritos com a mudança na percentagem sem médico.

**O que encontrámos:** Encontrámos uma relação fraca entre as duas mudanças, com muitas exceções. A tendência foi para maior crescimento dos inscritos acompanhar maior aumento da percentagem sem médico.

**Exemplo fictício:** Uma unidade pode passar de 100 mil para 110 mil inscritos e de 20 mil para 22 mil sem médico. Há mais pessoas sem médico, mas a percentagem mantém-se nos 20%.

**Para que serve:** Perceber se as duas mudanças tendem a acompanhar-se e orientar uma investigação com mais informação.

**Como interpretar:** Esta comparação resume a mudança entre o início e o fim do período. Não demonstra que o crescimento tenha causado o agravamento, nem que a relação se repita todos os meses.

**Detalhe técnico:** Spearman das variações: 0,225, em 38 séries. Compara as posições das unidades nas duas variações. A designação de relação fraca usa |Spearman| < 0,3 como referência descritiva; não foi feito um teste de significância.

### H4 — Unidades com números semelhantes de inscritos apresentam percentagens sem médico diferentes consoante a região de saúde

Agrupámos as unidades pelo número de inscritos e comparámos regiões dentro das mesmas faixas de dimensão.

**O que encontrámos:** A comparação usa a mediana: o valor central das percentagens das unidades de cada grupo. Em 2026-06, a maior diferença elegível foi de 37,58 pontos percentuais entre as regiões «Lisboa e Vale do Tejo» e «Norte», na faixa intermédia. Foram comparados grupos de 6 e 4 unidades.

**Exemplo fictício:** Se um grupo tiver um valor central de 40% e outro de 10%, a diferença é de 30 pontos percentuais. São grupos de unidades, não grupos de pessoas.

**Para que serve:** Identificar diferenças geográficas que merecem investigação, aproximando a dimensão das unidades comparadas.

**Como interpretar:** Os grupos são pequenos. Ter dimensão semelhante não significa ter os mesmos recursos ou características. A comparação não demonstra que a região seja a causa da diferença.

**Detalhe técnico:** Há 7 combinações de duas regiões e uma faixa com grupos elegíveis durante os 30 meses. Exigimos pelo menos três unidades em cada grupo. Os limites das faixas são fixos, definidos em janeiro de 2024. A mediana das percentagens das unidades não é a percentagem regional calculada pelos totais.

## Decisão

Manter a referência simples como comparação principal; não foi demonstrado ganho da abordagem selecionada. Disponibilizar também os resultados dos modelos para transparência.

Avançar para disponibilização da análise histórica com as respostas, tabelas e gráficos. O critério preditivo é avaliado separadamente do valor descritivo.

## Limitações e pendências

- Histórico antigo; sem extrapolação para julho de 2026
- 38 séries completas na evolução/previsão
- Nomes estáveis não comprovam território estável
- Recolha atual pode incluir revisões
- Meses e unidades não são observações independentes
- Faixas de dimensão aproximadas e grupos pequenos na H4
- Inscritos não são população residente; sem médico por opção separado
- Resultados descritivos não identificam causas

Pendentes: correspondência territorial da Póvoa/Vila do Conde e janela exata das taxas de consultas. Nenhum resultado demonstra causalidade ou determina distribuição de recursos.
