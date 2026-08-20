# =====================================================================
# Análise de Tendência Socioeconômica (IBGE)
# Autor: Rafael Silveira Assunção
# =====================================================================

import matplotlib
matplotlib.use('Agg')  # Força o matplotlib a gerar imagens em segundo plano na nuvem

import os
import time
import requests
import json
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Configuração essencial para o Google Colab funcionar com um clique
if os.environ.get('COLAB_RELEASE_TAG'):
    print("Ambiente Colab detectado. Instalando dependências ausentes...")
    os.system('pip install -q pandas numpy seaborn matplotlib scipy requests')

def obter_dados_ibge(url_api):
    """
    Consome a API SIDRA utilizando uma sessão persistente com lógica de 
    repetição para contornar o bloqueio HTTP 403 do firewall do IBGE.
    """
    session = requests.Session()
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://sidra.ibge.gov.br/',
        'Origin': 'https://sidra.ibge.gov.br',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0'
    }
    
    max_tentativas = 5
    atraso = 3  # Segundos de espera entre falhas
    
    for tentativa in range(max_tentativas):
        try:
            resposta = session.get(url_api, headers=headers, timeout=45)
            
            if resposta.status_code == 200:
                dados_brutos = resposta.json()
                df = pd.DataFrame(dados_brutos[1:], columns=dados_brutos)
                return df
                
            print(f"[Tentativa {tentativa + 1}/{max_tentativas}] Servidor do IBGE retornou HTTP {resposta.status_code}. Aguardando para tentar novamente...")
        except Exception as e:
            print(f"[Tentativa {tentativa + 1}/{max_tentativas}] Conexão falhou: {str(e)}")
            
        time.sleep(atraso)
        atraso *= 2  # Aumenta gradativamente o tempo de espera (Backoff)
        
    raise Exception("Não foi possível coletar os dados do IBGE devido ao bloqueio persistente do servidor.")

# --- 1. Carga e Higienização das Variáveis (Via API SIDRA) ---

# URLs tratadas com URL Encoding (%5Ball%5D representa os colchetes requisitados pela API)
url_renda = "https://ibge.gov.br"
url_educacao = "https://ibge.gov.br"

print("Coletando indicadores diretamente dos servidores do IBGE...")
df_renda_bruto = obter_dados_ibge(url_renda)
df_educ_bruto = obter_dados_ibge(url_educacao)

# Filtragem cirúrgica e renomeação para merge limpo
df_renda = df_renda_bruto[['Unidade da Federação', 'Valor']].rename(columns={'Valor': 'Renda_Per_Capita'})
df_educ = df_educ_bruto[['Unidade da Federação', 'Valor']].rename(columns={'Valor': 'Taxa_Alfabetizacao'})

# Unificação das bases usando o nome do Estado como chave primária
dados_socio = pd.merge(df_renda, df_educ, on='Unidade da Federação')

# Garante que os números vindos da string JSON sejam interpretados corretamente como float
dados_socio['Renda_Per_Capita'] = pd.to_numeric(dados_socio['Renda_Per_Capita'], errors='coerce')
dados_socio['Taxa_Alfabetizacao'] = pd.to_numeric(dados_socio['Taxa_Alfabetizacao'], errors='coerce')
dados_socio = dados_socio.dropna()

# --- 2. Modelagem e Categorização Dinâmica ---

# Classificação em 3 níveis (Baixo, Médio, Alto) baseada estritamente nos tercis da própria amostra
tercis = np.percentile(dados_socio['Renda_Per_Capita'], [33.3, 66.6])
dados_socio['Vulnerabilidade'] = np.where(dados_socio['Renda_Per_Capita'] <= tercis[0], 'Alta',
                                  np.where(dados_socio['Renda_Per_Capita'] <= tercis[1], 'Média', 'Baixa'))

# Trava a ordem categórica para o Seaborn desenhar a legenda na sequência social correta
dados_socio['Vulnerabilidade'] = pd.Categorical(dados_socio['Vulnerabilidade'], categories=['Alta', 'Média', 'Baixa'], ordered=True)

# --- 3. Diagnóstico Estatístico ---

print("\n=== RESUMO CRÍTICO DOS DADOS BRASILEIROS ===")
print(f"Estados processados: {len(dados_socio)}")
print(f"Renda média per capita: R$ {dados_socio['Renda_Per_Capita'].mean():.2f}")
print(f"Média nacional de alfabetização: {dados_socio['Taxa_Alfabetizacao'].mean():.1f}%\n")

# Coeficiente de Pearson para validar estatisticamente se a hipótese da reta faz sentido
correlacao, p_valor = stats.pearsonr(dados_socio['Renda_Per_Capita'], dados_socio['Taxa_Alfabetizacao'])
print("=== FORÇA DA TENDÊNCIA SOCIOECONÔMICA ===")
print(f"Índice de Correlação Linear (Pearson): {correlacao:.3f}")
print(f"Significância Estatística (p-valor): {p_valor:.5f}")

# --- 4. Engenharia Visual do Gráfico ---

plt.figure(figsize=(11, 6))
sns.set_theme(style="whitegrid")

# Define o semáforo social: Alta vulnerabilidade (vermelho) -> Baixa (verde)
paleta_cores = {'Alta': '#e74c3c', 'Média': '#f1c40f', 'Baixa': '#2ecc71'}

# Jitter controlado para evitar que siglas de estados empilhem e sumam do mapa
sns.stripplot(
    data=dados_socio, 
    x='Renda_Per_Capita', 
    y='Taxa_Alfabetizacao', 
    hue='Vulnerabilidade', 
    palette=paleta_cores, 
    size=9, 
    alpha=0.85, 
    jitter=0.15
)

# Ajuste da reta de regressão OLS cortando a dispersão
sns.regplot(
    data=dados_socio, 
    x='Renda_Per_Capita', 
    y='Taxa_Alfabetizacao', 
    scatter=False, 
    color='#2c3e50', 
    line_kws={'linewidth': 1.5, 'linestyle': '--'}
)

# Refinamento dos textos e rótulos comerciais
plt.title('Tendência Socioeconômica: Renda per Capita vs. Educação Básica', fontsize=14, pad=15, weight='bold')
plt.xlabel('Renda Média Mensal Per Capita (R$)', fontsize=11, labelpad=10)
plt.ylabel('Taxa de Alfabetização (%)', fontsize=11, labelpad=10)
plt.legend(title='Vulnerabilidade Social', loc='lower right', frameon=True)

# Ajuste fino das margens para não cortar as labels dos eixos
plt.tight_layout()

# Salva a imagem para o README renderizar direto na raiz do repositório
plt.savefig('grafico_socioeconomico.png', dpi=300)
print("\nGráfico exportado com sucesso como 'grafico_socioeconomico.png'!")
