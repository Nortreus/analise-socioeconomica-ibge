# =====================================================================
# Análise de Tendência Socioeconômica (IBGE)
# Autor: Rafael Silveira Assunção
# =====================================================================

import matplotlib
matplotlib.use('Agg')  # Força o matplotlib a gerar imagens em segundo plano na nuvem

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# --- 1. Leitura Local dos Dados Estruturados ---

caminho_dados = 'dados_ibge.csv'

if not os.path.exists(caminho_dados):
    raise FileNotFoundError(f"O arquivo de contingência {caminho_dados} não foi encontrado no repositório.")

print("Carregando base de contingência local do IBGE...")
dados_socio = pd.read_csv(caminho_dados)

# CORREÇÃO DO BUG: Força as colunas a virarem números (floats), limpando espaços ou sujeiras no texto
dados_socio['Renda_Per_Capita'] = pd.to_numeric(dados_socio['Renda_Per_Capita'], errors='coerce')
dados_socio['Taxa_Alfabetizacao'] = pd.to_numeric(dados_socio['Taxa_Alfabetizacao'], errors='coerce')
dados_socio = dados_socio.dropna() # Remove qualquer linha que tenha falhado na conversão

# --- 2. Modelagem e Categorização Dinâmica ---

# Classificação em 3 níveis (Baixo, Médio, Alto) baseada nos tercis da amostra
tercis = np.percentile(dados_socio['Renda_Per_Capita'], [33.3, 66.6])
dados_socio['Vulnerabilidade'] = np.where(dados_socio['Renda_Per_Capita'] <= tercis[0], 'Alta',
                                  np.where(dados_socio['Renda_Per_Capita'] <= tercis[1], 'Média', 'Baixa'))

# Trava a ordem categórica para o Seaborn desenhar a legenda na sequência correta
dados_socio['Vulnerabilidade'] = pd.Categorical(dados_socio['Vulnerabilidade'], categories=['Alta', 'Média', 'Baixa'], ordered=True)

# --- 3. Diagnóstico Estatístico ---

print("\n=== RESUMO CRÍTICO DOS DADOS BRASILEIROS ===")
print(f"Estados processados: {len(dados_socio)}")
print(f"Renda média per capita: R$ {dados_socio['Renda_Per_Capita'].mean():.2f}")
print(f"Média nacional de alfabetização: {dados_socio['Taxa_Alfabetizacao'].mean():.1f}%\n")

# Coeficiente de Pearson para validar a força do relacionamento
correlacao, p_valor = stats.pearsonr(dados_socio['Renda_Per_Capita'], dados_socio['Taxa_Alfabetizacao'])
print("=== FORÇA DA TENDÊNCIA SOCIOECONÔMICA ===")
print(f"Índice de Correlação Linear (Pearson): {correlacao:.3f}")
print(f"Significância Estatística (p-valor): {p_valor:.5f}")

# --- 4. Engenharia Visual do Gráfico ---

plt.figure(figsize=(11, 6))
sns.set_theme(style="whitegrid")

# Define o semáforo social: Alta vulnerabilidade (vermelho) -> Baixa (verde)
paleta_cores = {'Alta': '#e74c3c', 'Média': '#f1c40f', 'Baixa': '#2ecc71'}

# Gráfico de Dispersão (Agora sim os eixos vão se espalhar corretamente do zero aos maiores valores)
sns.scatterplot(
    data=dados_socio, 
    x='Renda_Per_Capita', 
    y='Taxa_Alfabetizacao', 
    hue='Vulnerabilidade', 
    palette=paleta_cores, 
    s=100, # Aumentei um pouco o tamanho dos pontos para melhor leitura
    alpha=0.85
)

# Ajuste da reta de regressão OLS cortando a dispersão de ponta a ponta
sns.regplot(
    data=dados_socio, 
    x='Renda_Per_Capita', 
    y='Taxa_Alfabetizacao', 
    scatter=False, 
    color='#2c3e50', 
    line_kws={'linewidth': 1.5, 'linestyle': '--'}
)

# Refinamento dos textos e rótulos
plt.title('Tendência Socioeconômica: Renda per Capita vs. Educação Básica', fontsize=14, pad=15, weight='bold')
plt.xlabel('Renda Média Mensal Per Capita (R$)', fontsize=11, labelpad=10)
plt.ylabel('Taxa de Alfabetização (%)', fontsize=11, labelpad=10)
plt.legend(title='Vulnerabilidade Social', loc='lower right', frameon=True)

plt.tight_layout()

# Salva a imagem corrigida para o README
plt.savefig('grafico_socioeconomico.png', dpi=300)
print("\nGráfico exportado com sucesso como 'grafico_socioeconomico.png'!")
