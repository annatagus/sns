# Fase 2 — Como executar

O pacote contém apenas os ficheiros da fase 2. A primeira fase e os restantes ficheiros do teu repositório devem ser mantidos.

1. Extrair o ZIP para uma pasta temporária.
2. Copiar o conteúdo das pastas `notebooks`, `src`, `data` e `docs` para as pastas com os mesmos nomes na raiz do projeto. Conservar o `01_business_understanding.ipynb` existente.
3. Abrir a raiz do projeto no VS Code e selecionar o kernel Python.
4. Se faltarem bibliotecas, executar `%pip install pandas matplotlib` numa célula temporária do kernel.
5. Abrir `notebooks/02_data_understanding.ipynb` e executar as células por ordem. O notebook entregue contém os resultados da execução de verificação.

## Dados e reprodutibilidade

O pacote inclui uma recolha real da API de 13 de outubro de 2026. O histórico tem 6 450 linhas e 126 meses. O módulo em `src/recolha_sns.py` reutiliza a recolha e verifica as somas de verificação para evitar alterar os dados brutos.

Para fazer uma recolha própria nova, alterar `PASTA_INPUT` para uma pasta ainda vazia, por exemplo `raiz / "data" / "input" / "recolha_nova"`, e executar desde o início. Conservar a recolha anterior. As alterações publicadas pela fonte podem fazer variar os resultados.

Os ficheiros de `data/input` não devem ser editados. As tabelas e gráficos da exploração ficam em `data/analytics`. Os dados preparados em `data/output` e os modelos em `data/models` serão produzidos em fases posteriores.

## O que rever agora

- Secções 1 a 4: fonte, dicionário, leitura e qualidade numérica.
- Secções 5 e 6: mudança de estrutura em 2024 e continuidade dos nomes no recorte.
- Secções 7 a 10: exploração das hipóteses, com limitações explícitas.
- Secção 11: pendências para a preparação dos dados.

A correspondência de nomes da ULS Póvoa de Varzim/Vila do Conde ainda precisa de validação. A comparação geográfica inclui grupos pequenos e não estabelece causalidade. A definição das taxas de consultas de um ano continua pendente antes de analisar a Q5.
