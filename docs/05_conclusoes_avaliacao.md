# Fase 5 — Conclusões da avaliação

Recolha: 2026-10-13T17:20:14.911883+00:00 (UTC). Âmbito: 2024-01 a 2026-06.

## Previsão

A referência teve MAE 0.417 pp. O melhor candidato aprendido escolhido na validação (Regressão linear) teve MAE 0.449 pp no teste. A escolha final do 04 foi Último valor e não superou a referência. O critério preditivo não foi cumprido; os resultados dos candidatos estão na tabela, sem nova seleção pelo teste.

- Último valor: MAE 0.417357 pp; RMSE 0.679343 pp; viés -0.165416 pp.
- Regressão linear: MAE 0.448916 pp; RMSE 0.696505 pp; viés -0.189219 pp.
- Random Forest B: MAE 0.582157 pp; RMSE 0.841621 pp; viés -0.289083 pp.

Seleção feita pela validação e mantida na avaliação. Mesmas unidades e meses para as abordagens. Teste com seis meses-alvo e 38 unidades; modelos fixos com origens mensais móveis. Não houve novo treino nesta fase.

## Perguntas e hipóteses

- Q1: CSP da ULS Amadora / Sintra: 194,681 inscritos sem médico em 2026-06. Estado: respondida.
- Q2: CSP da ULS Estuário do Tejo: 47.74%. Rankings e tabelas geográficas guardados; inscritos são o denominador. Estado: respondida.
- Q3: Nas 38 séries completas, 19 reduziram e 19 aumentaram a percentagem. Maior redução: CSP da ULS Cova da Beira (-15.09 pp); maior aumento: CSP da ULS Arrábida (13.22 pp). Estado: respondida com restrição de continuidade.
- Q4: As variações regionais foram calculadas a partir dos totais de todos os registos mensais. Ver 05_evolucao_regioes.csv; evolução não uniforme. Estado: respondida.
- Q5: Não avaliada nesta versão: falta confirmar a janela exata do indicador de um ano. Taxas preservadas, sem conclusões sobre consultas. Estado: pendente de definição.
- Q6: A referência teve MAE 0.417 pp. O melhor candidato aprendido escolhido na validação (Regressão linear) teve MAE 0.449 pp no teste. A escolha final do 04 foi Último valor e não superou a referência. O critério preditivo não foi cumprido; os resultados dos candidatos estão na tabela, sem nova seleção pelo teste. Estado: avaliada no teste reservado.

- H1: 35 de 39 posições diferem; Spearman 0.938. Avaliação: sustentada no último mês.
- H2: 19 séries com redução e 19 com aumento; variações regionais diferentes. Avaliação: diferenças descritivas observadas.
- H3: Spearman das variações: 0.225, em 38 séries. A direção observada não demonstra causa nem uma relação mensal geral. Avaliação: evidência de associação limitada.
- H4: Há diferenças descritivas entre regiões dentro de faixas comuns; 7 pares são elegíveis nos 30 meses. No último mês, a maior diferença elegível foi 37.58 pp entre Lisboa e Vale do Tejo e Norte, na faixa intermedia (n=6 e n=4). Faixas aproximam dimensão; grupos pequenos e composição limitam a leitura. Sem efeito causal demonstrado. Avaliação: evidência descritiva condicionada.

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
