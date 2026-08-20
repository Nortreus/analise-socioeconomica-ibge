# Análise de Tendência Socioeconômica: Renda Média vs. Alfabetização com Python (IBGE)

Este projeto analisa o impacto da renda na educação brasileira usando dados da API do IBGE (SIDRA), executando todo o processo de análise via Python no navegador.

---

## 🚀 Execução Direta (Sem Instalação)

Clique no botão abaixo para abrir e rodar a análise de dados completa diretamente pelo seu navegador utilizando o ambiente em nuvem do Google Colab:

[![Abrir no Colab](https://google.com)](https://google.com)

---

## Visualização dos Dados
O gráfico cruza a renda média per capita mensal (eixo X) com a taxa de alfabetização (eixo Y), evidenciando a relação entre infraestrutura econômica e desenvolvimento social.

![Análise de Renda vs Alfabetização](grafico_socioeconomico.png?v=2)

---

## 🔍 Análise do Gráfico
*   **Tendência Linear Positiva:** Comprova a correlação positiva: estados com maior renda (direita) possuem maiores taxas de alfabetização.
*   **Vulnerabilidade:** A cor vermelha indica alta vulnerabilidade (baixa renda/alfabetização), amarela a transição, e verde a consolidação social.
*   **Jitter:** Utilizado para melhorar a visualização e evitar sobreposição de estados próximos.

---

## Conceitos Aplicados
*   Consumo de APIs Públicas (IBGE/SIDRA).
*   Correlação de Pearson (`scipy.stats`).
*   Categorização Dinâmica de Variáveis.
*   Data Visualization com `seaborn`.

---

## 💬 Contribuições
*   Sugira mudanças via [Issues](https://github.com).
*   Debata no campo de [Discussions](https://github.com).
