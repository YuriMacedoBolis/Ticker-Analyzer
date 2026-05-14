# Script Ticker Analyzer: Pipeline ETL e Análise de Dados

## Sobre o Projeto
Este projeto consiste em um script Python focado na construção de um pipeline automatizado de extração, transformação e visualização (ETL) voltado para séries temporais. Utilizando a API do Yahoo Finance, o sistema coleta dados históricos de ativos financeiros, realiza a limpeza e o tratamento estatístico das informações, e gera painéis analíticos visuais. 

O objetivo principal é demonstrar proficiência na manipulação de matrizes de dados com a biblioteca Pandas e na aplicação de filtros temporais (como médias móveis), conceitos estruturais que formam a base da engenharia de dados e da análise de séries históricas.

## Funcionalidades
* **Extração Dinâmica (Extract):** Coleta automatizada de dados históricos (últimos 2 anos) de múltiplos ativos financeiros a partir de inputs dinâmicos do usuário.
* **Transformação e Limpeza (Transform):** Tratamento automatizado de valores nulos ou ausentes (método dropna) inerentes a séries temporais em dias sem captação de dados.
* **Modelagem Estatística:** Cálculo de médias móveis (7 e 30 dias) para suavização de tendências e remoção de ruídos temporais.
* **Análise de Volatilidade:** Cálculo contínuo da variação percentual diária de cada ativo, convertendo valores absolutos em indicativos de comportamento de mercado.
* **Visualização de Dados (Load/Viz):** Geração iterativa de gráficos utilizando subplots do Matplotlib, parametrizados com design focado em ambientes de desenvolvimento (dark theme).

## Stack Tecnológica
* **Python 3.x**
* **Pandas** (Estruturação, limpeza e cálculos sobre DataFrames)
* **yfinance** (Integração com a API do Yahoo Finance)
* **Matplotlib** (Renderização de gráficos analíticos e data storytelling)

*(As dependências completas estão listadas no arquivo `requirements.txt`)*

## Como Executar

1. Certifique-se de ter o Python instalado em seu ambiente.
2. Instale as dependências necessárias através do terminal de comando utilizando o arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

3. Execute o arquivo principal do script:
```bash
python main.py
```

4. Quando solicitado no terminal, insira os códigos das ações (tickers) desejadas, separados por vírgula (exemplo válido: PETR4.SA, VALE3.SA, AAPL, MSFT).

5. O sistema irá extrair e processar os dados. O gráfico analítico do primeiro ativo será exibido. Ao fechar a janela do gráfico, o sistema prosseguirá automaticamente para a renderização do próximo ativo da fila.

## Estrutura Lógica do Pipeline e Resiliência
O processamento em lote foi desenhado com foco em resiliência de execução. A arquitetura iterativa isola as requisições de cada ativo. Dessa forma, caso o usuário insira um ticker inválido ou a API não retorne dados consistentes para um item específico, o sistema não interrompe a execução geral (crash). Em vez disso, ele registra um aviso no log do terminal e avança de forma autônoma para a extração do próximo elemento da fila.
