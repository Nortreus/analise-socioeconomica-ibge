# Análise de Tendência Socioeconômica: Renda Média vs. Alfabetização com Python (IBGE)

**Ambiente:** Python 3.10 | **Status:** Automatizado via GitHub Actions | **Licença:** MIT

Este projeto avalia o impacto direto dos indicadores econômicos no desenvolvimento educacional das unidades federativas brasileiras, utilizando microdados reais estruturados para mapear a relação entre renda per capita domiciliar e a alfabetização básica.

Toda a infraestrutura de execução foi construída para rodar na nuvem em um pipeline CI/CD de backend, processando os dados e gerando novos outputs gráficos.

---

## 📊 Visualização dos Dados

O gráfico cruza a renda média per capita mensal (eixo X) com a taxa de alfabetização da população (eixo Y).

![Análise de Renda vs Alfabetização](grafico_socioeconomico.png?v=2)

---

## 🔍 Análise do Gráfico

*   **Comportamento da Curva (Mínimos Quadrados OLS):** Comprova uma forte correlação linear positiva, onde o aumento da renda per capita está associado a uma taxa de alfabetização mais elevada.
*   **Estratificação Social (Vulnerabilidade):**
    *   **Alta Vulnerabilidade (Vermelho):** Estados com menores faixas de renda e alfabetização.
    *   **Zona de Transição (Amarelo):** Ponto de inflexão socioeconômica.
    *   **Consolidação Social (Verde):** Estados com maiores indicadores educacionais e de renda.

---

## 🛠️ Arquitetura Tecnológica

*   **Pandas:** Manipulação de dados estruturados e tratamento de nulos.
*   **NumPy:** Cálculo de percentis e distribuição de vulnerabilidade.
*   **Seaborn & Matplotlib:** Visualização e renderização gráfica de alta resolução.
*   **SciPy:** Análise estatística de correlação linear (Pearson).
*   **GitHub Actions:** Automação do pipeline CI/CD na nuvem.
