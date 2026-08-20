# Análise de Tendência Socioeconômica: Renda Média vs. Alfabetização com Python (IBGE)

[![Last Commit](https://shields.io)](https://github.com)
[![Python Version](https://shields.io)](https://github.com)
[![License](https://shields.io)](https://github.com)

Este projeto analisa o impacto da renda per capita domiciliar na alfabetização dos estados brasileiros, utilizando dados do IBGE e pipeline CI/CD na nuvem.

---

## 📊 Visualização dos Dados

O gráfico abaixo mostra a relação entre renda média (eixo X) e taxa de alfabetização (eixo Y), com cores indicando o Índice de Vulnerabilidade Social.

![Análise de Renda vs Alfabetização](grafico_socioeconomico.png?v=3)

---

## 🔍 Análise Avançada do Gráfico

*   **Tendência (OLS):** Correlação linear positiva, mostrando que maior renda per capita está associada a maiores taxas de alfabetização.
*   **Vulnerabilidade:**
    *   **Alta (Vermelho):** Baixa renda e alfabetização (quadrante inferior esquerdo).
    *   **Transição (Amarelo):** Ponto de inflexão.
    *   **Consolidação (Verde):** Alta renda e alfabetização estável (quadrante superior direito).

---

## 🛠️ Arquitetura Tecnológica

*   **Pandas:** Manipulação e limpeza dos dados brutos.
*   **NumPy:** Cálculo de percentis e intervalos de vulnerabilidade social.
*   **Seaborn & Matplotlib:** Geração do gráfico de dispersão com alta resolução (300 dpi).
*   **SciPy:** Validação estatística (correlação de Pearson).
*   **GitHub Actions:** Automação de pipeline na nuvem.
