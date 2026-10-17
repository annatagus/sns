# Fase 6 — Disponibilização e atualização

Produto: página local de resultados históricos, notebooks e pacote reproduzível. Período: 2024-01 a 2026-06. Recolha: 2026-10-13T17:20:14.911883+00:00.

## Decisões

- Página HTML autónoma, com filtros por mês/região e ordenação dos rankings. Não exige servidor ou nova recolha para consultar.
- Não faz novas previsões nem altera a seleção do 04. Disponibiliza a avaliação histórica e os limites conhecidos.
- Dados e gráficos são gerados a partir das entradas conferidas do 05. Originais, modelos e métricas anteriores são apenas lidos.
- README e requirements existentes são preservados; propostas ficam em docs para revisão. Quando não existem, são criados na raiz.
- Pacote local reúne notebooks, dados, src, docs e media, com README/requirements. Ambientes e caches ficam de fora; o .gitignore, quando existir, é incluído. A documentação desta versão inclui um .gitignore base revisto. O notebook preserva o ficheiro existente; se ainda não existir no projeto local, copiar o fornecido com a atualização.
- A criação desta página não implica publicação externa. Qualquer atualização tem de indicar a recolha, as definições e o período.

## Manutenção

1. Nova recolha numa pasta separada; preservar a anterior.
2. Conferir esquema, conceitos, categorias e territórios.
3. Reexecutar preparação, modelação e avaliação dependentes da mudança, com validação temporal apropriada.
4. Gerar novamente a página e o pacote; verificar os resultados e limites antes de os disponibilizar.

A série antiga termina em junho de 2026. Uma análise atual teria de usar a definição nova separadamente, com histórico suficiente e novo enquadramento. Mantêm-se pendentes a correspondência da Póvoa/Vila do Conde e a janela das consultas.
