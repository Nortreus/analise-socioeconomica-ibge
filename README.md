# Análise de Tendência Socioeconômica: Renda Média vs. Alfabetização com Python (IBGE)

![GitHub Last Commit](https://shields.io)
![Python Version](https://shields.io)
![License](https://shields.io)

Este projeto analisa a relação entre renda per capita e alfabetização nas unidades federativas brasileiras, utilizando dados do IBGE e ferramentas de automação (CI/CD) para processamento e geração de gráficos.

---

## 📊 Visualização dos Dados

O gráfico cruza renda média (X) com taxa de alfabetização (Y), segmentado pelo Índice de Vulnerabilidade Social.

![Análise de Renda vs Alfabetização](grafico_socioeconomico.png?v=2)

---

## 🔍 Análise Avançada do Gráfico

*   **Curva de Tendência (OLS):** Correlação linear positiva entre renda e alfabetização.
*   **Estrutura de Vulnerabilidade:** Classificação em Alta (Vermelho), Transição (Amarelo) e Consolidação (Verde).
*   **Controle de Densidade:** Identificação de outliers regionais.

---

## 🛠️ Arquitetura Tecnológica

*   **Pandas & NumPy:** Processamento de dados e cálculo de tercis.
*   **Seaborn & Matplotlib:** Visualização de dados (DPI 300).
*   **SciPy (`scipy.stats`):** Correlação de Pearson e relevância estatística.
*   **GitHub Actions:** Automação de pipeline na nuvem.
