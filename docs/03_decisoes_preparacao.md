# Fase 3 — Decisões de preparação

Recolha: 2026-10-13T17:20:14.911883+00:00 (UTC). Fonte: https://transparencia.sns.gov.pt/api/explore/v2.1/catalog/datasets/utentes-inscritos-em-cuidados-de-saude-primarios.

- D01: 6450 linhas no histórico; 1170 no recorte de 2024-01 a 2026-06; 5280 fora do período. Brutos preservados.
- D02: nomes claros e tipos explícitos; unidade_fonte e periodo_fonte mantêm os valores da fonte. Chave: região, unidade e mês. Ver 03_mapa_colunas.csv.
- D03: qualidade verificada sem correções automáticas, imputação, interpolação ou remoção de duplicados. Diferença tolerada de arredondamento: 0,01 pp. Valores extremos válidos mantidos.
- D04: 40 designações ao longo do recorte, 39 por mês. Não fundir os dois nomes da Póvoa/Vila do Conde sem confirmação territorial. 1140 linhas de 38 séries completas para evolução e previsão; 30 linhas mantidas apenas no principal/regionais/H4.
- D05: percentagens recalculadas das contagens, publicadas preservadas. Região calculada com soma das contagens / soma dos inscritos, em cada mês.
- D06: limites das faixas comuns fixados pelos tercis dos inscritos de janeiro de 2024: 194226.333333 e 327435.333333. Grupos com menos de três unidades assinalados; esta regra não garante suficiência estatística. A pertença à faixa pode mudar.
- D07: 1102 pares consecutivos; 988 com histórico completo. 114 pares não usados nos modelos por falta de histórico inicial. Teste por mês-alvo, janeiro a junho de 2026. Validação sugerida: julho a dezembro de 2025, com treino anterior. Variáveis permitidas no manifesto; não ajustar modelos ou pré-processadores nesta fase.
- D08: taxas de consultas preservadas mas excluídas das variáveis do modelo e da interpretação da Q5 até confirmar a janela de um ano.

## Limitações e pendências

Os nomes estáveis não provam continuidade territorial. As coordenadas são pontos de referência. Inscritos não são a população residente. A recolha atual pode conter revisões. Não ligar a série antiga ao novo indicador de julho de 2026.

Continuam pendentes a correspondência territorial da Póvoa/Vila do Conde e a janela exata das consultas. A comparação temporal e a previsão cobrem 38 séries; rankings e totais regionais mantêm os 39 registos mensais.

A alteração ACES/ULS e a quebra de definição do indicador estão justificadas no 01 e verificadas no 02. Fontes: [API SNS](https://transparencia.sns.gov.pt/api/explore/v2.1/catalog/datasets/utentes-inscritos-em-cuidados-de-saude-primarios) e [ERS — reorganização ULS](https://www.ers.pt/pt/atividade/supervisao/selecionar/alertas-de-supervisao/2024/alertas/alerta-de-supervis%C3%A3o-n-%C2%BA-1-2024/).

## Próxima fase

Usar sns_csp_modelacao.csv no 04. Comparar modelos com a referência simples nas mesmas linhas. Usar só as variáveis permitidas do manifesto. Ajustar codificações e escalas no treino, escolher o modelo pela validação temporal e reservar o teste final para avaliação.
