import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

print("=== Sistema de Extração e Análise de Ativos ===")


# Entrada dos Tickers separados por "," 
entrada_usuario = input("Digite os códigos das ações separados por vírgula (ex: PETR4.SA, VALE3.SA, AAPL): ")

# Limpa os espaços em branco e deixa tudo em maiúsculo automaticamente
tickers = []
for ticker in entrada_usuario.split(','):
    tickers.append(ticker.strip().upper())


# Dicionário para guardar os dados que virão
resultados = {}

# For para rodar cada ticker separadamente
for ticker in tickers:
    print(f"\n[Extração] Buscando dados da API para: {ticker}...")
    
    # Extração de ativo no período de 2 anos
    dados = yf.download(ticker, period='2y')
    
    if dados.empty:
        print(f"⚠️ Aviso: Não foi possível encontrar dados para {ticker}. Verifique o código.")
        continue # Pula para a próxima ação
        
    print(f"[Tratamento] Limpando e calculando métricas para: {ticker}...")
    # pegando apenas os dados de fechamento do ticker
    df_ticker = pd.DataFrame(dados['Close'])
    df_ticker.columns = ['Preco_Fechamento']
    
    # Limpeza de dados nulos ( sabado e domingo )
    df_ticker.dropna(inplace=True)

    # Criando métricas temporais (Médias Móveis e Variação)
    df_ticker['Media_Movel_7d'] = df_ticker['Preco_Fechamento'].rolling(window=7).mean()
    df_ticker['Media_Movel_30d'] = df_ticker['Preco_Fechamento'].rolling(window=30).mean()
    df_ticker['Variacao_Diaria'] = df_ticker['Preco_Fechamento'].pct_change() * 100

    resultados[ticker] = df_ticker

# Geração dos Dashboards MatPlot
if not resultados:
    print("\nNenhum dado válido foi processado. Encerrando o sistema.")
else:
    print("\n[Dados] Gerando visualizações analíticas...")
    plt.style.use('dark_background')
    
    # Criação de um dashboard para cada ticker
    for ticker, df in resultados.items():
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), gridspec_kw={'height_ratios': [3, 1]})
        
        # Gráfico Superior
        ax1.plot(df.index, df['Preco_Fechamento'], label='Preço Real', color='#00a8ff', alpha=0.6)
        ax1.plot(df.index, df['Media_Movel_30d'], label='Média Móvel (30d)', color='#e84118', linewidth=2)
        ax1.set_title(f'Pipeline de Dados: {ticker} (Série Temporal de 2 Anos)', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Preço')
        ax1.legend()
        ax1.grid(True, alpha=0.2)

        # Gráfico Inferior 
        cores_barras = df['Variacao_Diaria'].apply(lambda x: '#4cd137' if x > 0 else '#e84118')
        ax2.bar(df.index, df['Variacao_Diaria'], color=cores_barras)
        ax2.set_title('Volatilidade / Variação Diária (%)', fontsize=12)
        ax2.set_ylabel('% Variação')
        ax2.grid(True, alpha=0.2)

        plt.tight_layout()
        plt.show() # Pausa o script mostrando o gráfico. Ao fechar a janela, ele mostra o próximo.

print("Operação finalizada com sucesso.")