# Análise de Tendência Socioeconômica: Renda Média vs. Alfabetização com Python (IBGE)

![GitHub Last Commit](https://shields.io)
![Python Version](https://shields.io)
![License](https://shields.io)

Este projeto avalia o impacto direto dos indicadores econômicos no desenvolvimento educacional das unidades federativas brasileiras. A análise utiliza microdados reais estruturados, mapeando como a infraestrutura de renda per capita domiciliar atua como variável preditora no acesso à alfabetização básica da população. 

Toda a infraestrutura de execução foi construída para rodar na nuvem em um pipeline CI/CD de backend, processando os dados e gerando novos outputs gráficos de forma agnóstica a ambientes locais.

---

## 📊 Visualização dos Dados

O gráfico cruza a renda média per capita mensal (eixo X) com a taxa de alfabetização da população (eixo Y). A reta central exibe a linha de tendência calculada pelo modelo e as cores agrupam as regiões de acordo com o Índice de Vulnerabilidade Social calculado sobre a amostragem.

![Análise de Renda vs Alfabetização](grafico_socioeconomico.png?v=2)

---

## 🔍 Análise Avançada do Gráfico

A visualização consolida três dimensões analíticas (Renda, Alfabetização e Vulnerabilidade) e expõe com clareza as assimetrias socioeconômicas estruturais do cenário brasileiro:

*   **Comportamento da Curva de Tendência (Mínimos Quadrados OLS):** A linha tracejada que intercepta a distribuição comprova uma forte correlação linear positiva entre as variáveis. O comportamento indica que o ganho de renda per capita gera um efeito diretamente proporcional na taxa de alfabetização, descrevendo uma curva ascendente estável que desloca a amostragem das faixas mais críticas em direção ao platô de desenvolvimento.
*   **Estratificação Social por Semáforo de Cores:** O agrupamento de vulnerabilidade revela que o capital financeiro dita a velocidade do ganho educacional regional:
    *   **Alta Vulnerabilidade (Vermelho):** Concentração de estados de menor porte econômico no quadrante inferior esquerdo. Registram faixas de renda restritas associadas às menores taxas de alfabetização do estudo, evidenciando o impacto da escassez estrutural.
    *   **Zona de Transição (Amarelo):** Faixa central que funciona como um ponto de inflexão socioeconômica, acomodando estados que estão rompendo barreiras de desenvolvimento.
    *   **Consolidação Social (Verde):** Predominância absoluta no quadrante superior direito. Estados que ultrapassaram a linha crítica de renda média conseguem estabilizar seus indicadores educacionais nos níveis mais altos e homogêneos, registrando baixa vulnerabilidade e variação interna quase nula.
*   **Controle de Densidade Populacional:** O espalhamento espacial dos eixos permite mapear a exata posição de cada unidade da federação, isolando visualmente estados com dinâmicas atípicas de renda (*outliers*) em relação ao bloco principal da distribuição sem distorcer o comportamento da linha central de tendência.

---

## 🛠️ Arquitetura Tecnológica e Ferramentas Aplicadas

O ecossistema computacional do projeto foi estruturado utilizando bibliotecas consagradas de Data Science em Python, cada uma cumprindo um papel específico no pipeline de extração e tratamento:

*   **Pandas:** Responsável pelo gerenciamento de dados tabulares. Utilizado para carregar a matriz bruta do arquivo em formato estruturado (`DataFrame`), realizar merge de colunas com base nas chaves geográficas, converter os tipos de dados de texto para ponto flutuante e aplicar técnicas de tratamento de valores nulos (`dropna`).
*   **NumPy:** Utilizado no motor matemático e de modelagem. Responsável pelo cálculo dinâmico de percentis e distribuição de tercis para fatiar e criar os intervalos de vulnerabilidade social de maneira estatisticamente equilibrada.
*   **Seaborn & Matplotlib:** Núcleo de engenharia visual do projeto. O Seaborn gerencia a estética das camadas gráficas de dispersão condicional (`hue`) e as marcações de eixos, enquanto o Matplotlib fornece o controle de backend para renderização vetorial e exportação física do arquivo de imagem final em alta resolução (`dpi=300`) sem depender de monitores locais.
*   **SciPy (`scipy.stats`):** Motor de cálculo estatístico. Aplicado para rodar a correlação linear de Pearson e extrair o p-valor da amostragem, validando de forma matemática a hipótese nula e provando a relevância científica do comportamento da reta.
*   **GitHub Actions:** Orquestrador de automação. Executa em segundo plano e de forma independente rotinas recorrentes de pipeline para garantir que o projeto processe os dados locais de contingência e regenere o visual de documentação de ponta a ponta na nuvem.
