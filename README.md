<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="media/cegid_academy_logo_branco.svg">
    <img src="media/cegid_academy_logo_azul.svg" alt="cegid Academy" width="320">
  </picture>
</p>

# Projeto 02 — Cobertura de Médico de Família no SNS 🩺

Este repositório contém o **Projeto 02** do curso **AiDAPT 04** da **cegid Academy** — *Análise de Dados com Recolha por Web Scraping / APIs*. O projeto recolhe dados públicos do Portal da Transparência do SNS através da API oficial e percorre o ciclo completo **CRISP-DM** em Python e Jupyter Notebook: recolha, exploração, preparação, modelação, avaliação e disponibilização.

A pergunta central é: **onde existem maiores falhas de cobertura de médico de família em Portugal Continental, quais estão a agravar-se e o histórico ajuda a prever o mês seguinte?**

O projeto será apresentado **entre os dias 21 e 22 de outubro de 2026** pelo **Grupo #4**.

| | |
|---|---|
| **Curso** | AiDAPT 04 — cegid Academy |
| **Grupo** | #4 |
| **Projeto** | Projeto 02 — Recolha, Tratamento e Análise de Dados |
| **Tema** | Utentes inscritos nos cuidados de saúde primários e cobertura de médico de família |
| **Entrega** | 18 de outubro de 2026, no repositório GitHub |
| **Apresentação** | 21 e 22 de outubro de 2026 |

---

## 👥 Elementos do Grupo #4

* Raquel Cunha: 📧 raquelmcunha [at] gmail [dot] com :octocat: [@annatagus](https://github.com/annatagus)
* Tiago Rodrigues: 📧 tiag0rkayh [at] gmail [dot] com :octocat: [@Tiago-Alex](https://github.com/Tiago-Alex)

## 👩‍🏫 Professora Orientadora

* Marta Martinho: 💼 [LinkedIn](https://www.linkedin.com/in/marta-martinho-b22b6865/)

---

## 📊 Principais Resultados

Período analisado: **janeiro de 2024 a junho de 2026**, nas 39 unidades (ULS) de Portugal Continental. Recolha feita pela API a 13 de outubro de 2026.

| Pergunta | Resultado (junho de 2026) |
|---|---|
| **Q1** — Onde há mais inscritos sem médico? | CSP da ULS Amadora / Sintra: **194 681** inscritos sem médico |
| **Q2** — Onde é maior a percentagem sem médico? | CSP da ULS Estuário do Tejo: **47,74 %** dos inscritos |
| **Q3** — Que unidades melhoraram ou pioraram? | Nas 38 séries completas, 19 reduziram e 19 aumentaram a percentagem. Maior redução: Cova da Beira (−15,09 pp); maior aumento: Arrábida (+13,22 pp) |
| **Q4** — Como evoluiu cada região? | Evolução não uniforme: o Centro desceu 5,17 pp; Alentejo, Lisboa e Vale do Tejo, Algarve e Norte subiram entre 0,5 e 1,5 pp |
| **Q5** — Há associação com a utilização de consultas? | Não avaliada: falta confirmar a janela exata do indicador de um ano |
| **Q6** — O histórico prevê melhor o mês seguinte? | **Não.** Repetir o último valor teve o menor erro no teste (MAE 0,417 pp) |

Comparação das previsões a um mês, no teste reservado (janeiro a junho de 2026, 228 previsões):

| Abordagem | MAE (pp) | RMSE (pp) | Viés (pp) |
|---|---:|---:|---:|
| **Último valor** (referência, escolhida na validação) | **0,417** | 0,679 | −0,165 |
| Regressão linear | 0,449 | 0,697 | −0,189 |
| Random Forest B | 0,582 | 0,842 | −0,289 |

A conclusão completa, incluindo as hipóteses H1 a H4 com explicações e exemplos, está em [docs/05_conclusoes_avaliacao.md](docs/05_conclusoes_avaliacao.md).

---

## 🌐 Consultar os Resultados

A página de resultados reúne rankings, evolução regional, comparação de modelos e conclusões, e permite escolher o mês, a região e a ordenação das unidades. Os quatro cartões das hipóteses explicam cada resultado em linguagem simples, com um exemplo fictício e o detalhe técnico.

* 🔗 **[Abrir a página de resultados no navegador](https://htmlpreview.github.io/?https://github.com/annatagus/sns/blob/main/docs/06_resultados_sns.html)** (pré-visualização online, sem instalar nada).
* 💾 Em alternativa, descarregar [docs/06_resultados_sns.html](docs/06_resultados_sns.html) e abrir com duplo clique: é um ficheiro autónomo, com os dados e os gráficos incluídos.

> Ao abrir o ficheiro diretamente no GitHub, aparece o código HTML em vez da página.

---

## 📁 Organização do Repositório

```text
sns/
├── notebooks/              Um notebook por fase CRISP-DM (01 a 06)
│   └── template_original/  Template fornecido pela professora
├── src/
│   └── recolha_sns.py      Recolha pela API e verificação das assinaturas SHA-256
├── data/
│   ├── input/              Dados brutos da recolha (nunca alterados)
│   ├── output/             Dados preparados, previsões e resumo da avaliação
│   ├── analytics/          Tabelas de verificação, métricas e gráficos
│   └── models/             Modelos treinados (.joblib) e registo da seleção
├── docs/                   Decisões, instruções por fase e página de resultados
├── media/                  Logótipos e imagens de apoio
├── requirements.txt        Dependências com as versões usadas
└── README.md
```

### Fases CRISP-DM

| Notebook | Fase | Principais saídas |
|---|---|---|
| [01_business_understanding](notebooks/01_business_understanding.ipynb) | Entendimento do negócio | Problema, perguntas Q1–Q6, hipóteses H1–H4, critérios de sucesso |
| [02_data_understanding](notebooks/02_data_understanding.ipynb) | Entendimento dos dados | Recolha em `data/input/`, qualidade, continuidade, exploração |
| [03_data_preparation](notebooks/03_data_preparation.ipynb) | Preparação | Datasets tratados em `data/output/` e manifesto da preparação |
| [04_modeling](notebooks/04_modeling.ipynb) | Modelação | Validação temporal, seleção e modelos em `data/models/` |
| [05_evaluation](notebooks/05_evaluation.ipynb) | Avaliação | Métricas de teste, respostas às perguntas e hipóteses |
| [06_deployment](notebooks/06_deployment.ipynb) | Disponibilização | Página de resultados e pacote do projeto |

Cada notebook verifica as assinaturas (SHA-256) dos ficheiros que recebe da fase anterior e para se algo tiver mudado. Assim, os resultados apresentados vêm sempre da mesma recolha e da mesma execução.

---

## 🚀 Como Executar o Projeto

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/annatagus/sns.git
   ```

2. **Criar o ambiente Python** (na raiz do projeto). A modelação foi executada com **Python 3.14**; as versões exatas das bibliotecas estão em `requirements.txt` e em `data/models/04_execucao_modelacao.json`.

   Windows (CMD):
   ```cmd
   python -m venv .venv
   .venv\Scripts\python -m pip install -r requirements.txt
   ```

   macOS / Linux:
   ```bash
   python3 -m venv .venv
   .venv/bin/python -m pip install -r requirements.txt
   ```

3. **Selecionar o kernel:** no VS Code (com as extensões Python e Jupyter), escolher **Select Kernel → Python Environments → .venv**.

4. **Executar os notebooks por ordem** (01 → 06), cada um com **Run All**. Se alterar uma fase, executar novamente as fases seguintes.

> O notebook 02 **não volta à API**: reutiliza a recolha guardada em `data/input/` depois de confirmar que os ficheiros não foram alterados. Para uma recolha nova, ver [docs/02_como_executar.md](docs/02_como_executar.md).

Instruções detalhadas de cada fase (entradas, saídas e verificações): [02](docs/02_como_executar.md) · [03](docs/03_como_executar.md) · [04](docs/04_como_executar.md) · [05](docs/05_como_executar.md) · [06](docs/06_como_executar.md).

---

## 🛠️ Tecnologias Utilizadas

* **Python** e **Jupyter Notebook** (VS Code) — desenvolvimento e documentação das fases.
* **pandas** e **numpy** — leitura, verificação e preparação dos dados.
* **matplotlib** — gráficos exploratórios e de avaliação.
* **scikit-learn** — `Pipeline`, `ColumnTransformer`, regressão linear e Random Forest.
* **joblib** — gravação dos modelos treinados.
* **urllib** (biblioteca padrão) — recolha pela API oficial.
* **Git & GitHub** — controlo de versões e trabalho em grupo.

---

## 📚 Fonte dos Dados

* [Utentes inscritos em cuidados de saúde primários — Portal da Transparência do SNS](https://transparencia.sns.gov.pt/explore/assets/utentes-inscritos-em-cuidados-de-saude-primarios/) (indicador mensal, por ULS e região de saúde).
* [Metadados e API oficial](https://transparencia.sns.gov.pt/api/explore/v2.1/catalog/datasets/utentes-inscritos-em-cuidados-de-saude-primarios).
* [ERS — Alerta de supervisão n.º 1/2024](https://www.ers.pt/pt/atividade/supervisao/selecionar/alertas-de-supervisao/2024/alertas/alerta-de-supervis%C3%A3o-n-%C2%BA-1-2024/) — enquadramento da reorganização em ULS.

**Recolha:** 13 de outubro de 2026 (17:20 UTC), 6 450 registos de janeiro de 2016 a junho de 2026. Foi usada a **API oficial**, como recomendado nas regras de boas práticas do enunciado; os dados são públicos, agregados por unidade e não contêm dados pessoais.

**Porquê janeiro de 2024 a junho de 2026?** Em janeiro de 2024 os ACES foram reorganizados em ULS (de 55 para 39 unidades), pelo que os territórios anteriores não são diretamente comparáveis. Em julho de 2026 mudou a definição do indicador; a série antiga termina em junho e não é ligada à nova.

---

## ⚠️ Interpretação e Limites

* **Inscritos não são população residente**; não extrapolar o indicador para todos os habitantes.
* A categoria **sem médico por opção** fica separada de sem médico atribuído.
* Cada mês é uma fotografia: não somar pessoas entre meses. As percentagens regionais usam os totais, não a média simples das unidades.
* A correspondência territorial das duas designações da **Póvoa de Varzim / Vila do Conde** não foi confirmada; ambas ficam nos rankings, mas fora das 38 séries completas de evolução e previsão.
* Meses e unidades não são observações independentes; as faixas de dimensão da H4 são aproximadas. **As associações observadas não identificam causas.**
* O teste usa a recolha atual, que pode incluir revisões. O modelo foi escolhido pela validação temporal; o teste não serviu para ajustar modelos.
* Trata-se de uma análise histórica do indicador antigo: não é uma previsão operacional do novo indicador nem determina a distribuição de médicos.

### Por fazer

- [ ] Confirmar a correspondência territorial entre as duas designações da Póvoa de Varzim / Vila do Conde antes de as ligar numa série única.
- [ ] Confirmar a janela exata das taxas de consultas de um ano antes de avaliar a Q5.

---

## 📄 Documentação

| Documento | Conteúdo |
|---|---|
| [docs/CA_AiDAPT4_Projeto_Enunciado_v2.pdf](docs/CA_AiDAPT4_Projeto_Enunciado_v2.pdf) | Enunciado do projeto |
| [docs/02_constatacoes_e_pendencias.md](docs/02_constatacoes_e_pendencias.md) | Constatações da exploração e pendências |
| [docs/03_decisoes_preparacao.md](docs/03_decisoes_preparacao.md) | Decisões D01–D08 da preparação |
| [docs/04_decisoes_modelacao.md](docs/04_decisoes_modelacao.md) | Divisão temporal, candidatos e seleção |
| [docs/05_conclusoes_avaliacao.md](docs/05_conclusoes_avaliacao.md) | Resultados, respostas e hipóteses |
| [docs/06_disponibilizacao_e_atualizacao.md](docs/06_disponibilizacao_e_atualizacao.md) | Disponibilização e manutenção |

Os ficheiros de decisões e conclusões são gerados pelos notebooks e atualizados em cada execução.
