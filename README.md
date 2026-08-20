# Análise de Tendência Socioeconômica: Renda Média vs. Alfabetização com Python (IBGE)

<p align="left">
  <img src="https://shields.io" alt="GitHub Last Commit">
  <img src="https://shields.io" alt="Python Version">
  <img src="https://shields.io" alt="License">
</p>

Este projeto analisa o impacto da renda per capita na alfabetização dos estados brasileiros, utilizando dados do IBGE e processamento em nuvem (CI/CD).

---

## 📊 Visualização dos Dados

O gráfico cruza renda média (eixo X) com taxa de alfabetização (eixo Y), com linha de tendência e agrupamento regional por vulnerabilidade social.

![Análise de Renda vs Alfabetização](grafico_socioeconomico.png?v=3)

---

## 🔍 Análise do Gráfico

*   **Curva de Tendência (OLS):** Correlação linear positiva clara; maior renda implica maior alfabetização.
*   **Estratificação Social:**
    *   **Alta Vulnerabilidade (Vermelho):** Baixa renda/educação.
    *   **Transição (Amarelo):** Ponto de inflexão.
    *   **Consolidação (Verde):** Alta renda/educação.
*   **Controle de Densidade:** Mapeamento preciso de *outliers* regionais.

---

## 🛠️ Arquitetura Tecnológica

*   **Pandas:** Manipulação de dados e limpeza.
*   **NumPy:** Cálculo de percentis e vulnerabilidade.
*   **Seaborn/Matplotlib:** Visualização e renderização gráfica.
*   **SciPy:** Validação estatística (Correlação de Pearson).
*   **GitHub Actions:** Automação do pipeline na nuvem.
