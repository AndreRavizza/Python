import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import numpy as np

#Importando o arquivo

df = pd.read_excel('Equity Value.xlsx')

#Selecionando a coluna "Produto" e alterando-a para apenas o texto antes do "-"

#.str.split divide o texto em duas partes com base no caractere
#.str[0] seleciona apena a primeira parte do que foi selecionado
#.str.strip() remove os espaços do texto

df['Produto'] = df['Produto'].str.split('-').str[0].str.strip()

# convertendo a coluna "Data" para formato de data utilizando a biblioteca "Datetime"
# dayfirst define que o primeiro número da data se refere ao dia

df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)

# Localizar a menor e a maior data da tabela na coluna "Data"

min_date = df['Data'].min()
max_date = df['Data'].max()

# Criando uma lista vazia que será armazenadas todas as datas entre a menor e a maior data

date_list = []

# Definindo a data atual igual a menor data

current_date = min_date

# Criando um loop que insere na lista todas os dias entre a data mínima e a data máxima

while current_date <= max_date:

    date_list.append(current_date)

    current_date = current_date + timedelta(days=1)

# Criando um dicionário que irá armazenar os ativos e a quantidade

assets_dic = {}

# Verificando em cada dia qual o valor do portfólio

for day in date_list:

    asset_value = 0

    #Verificando a quantidade de linhas que existem para o dia

    rows_count = (df['Data'] == day).sum()

    if rows_count > 0:

        index_list = []

        current_row = 0

        while current_row < rows_count:

            # Inserindo todos os valores dos índices do dia em uma lista

            index_list.append(df[df['Data'] == day].index[current_row])

            current_row = current_row + 1

        # Verificando o ativo e a quantidade de cada movimentação e atualizando o dicionário

        for index_number in index_list:

            asset_ticker = df.loc[index_number, 'Produto']

            if asset_ticker in assets_dic:

                if df.loc[index_number, 'Entrada/Saída'] == 'Credito':

                    old_amount = np.sum(np.array([assets_dic[asset_ticker]]))

                    new_amount = df.loc[index_number, 'Quantidade']

                    asset_amount = old_amount + new_amount

                    assets_dic[asset_ticker] = asset_amount

                elif df.loc[index_number, 'Entrada/Saída'] == 'Debito':

                    old_amount = np.sum(np.array([assets_dic[asset_ticker]]))

                    new_amount = df.loc[index_number, 'Quantidade']

                    asset_amount = old_amount - new_amount

                    assets_dic[asset_ticker] = asset_amount

                    if asset_amount <= 0:

                        assets_dic.pop(asset_ticker)

                else:

                    raise SystemError("Entrada/Saída deve ser Credito ou Debito")

            else:

                asset_amount = df.loc[index_number, 'Quantidade']
                
                assets_dic[df.loc[index_number, 'Produto']] = [asset_amount]

    # Calculando o valor total de todos os ativos daquele dia

    for asset in assets_dic:

        asset_amount = assets_dic[asset]

        if asset.find("3") == -1 and asset.find("4") == -1 and asset.find("11") == -1:

            day_format = day.strftime("%Y-%m-%d")
            data = yf.Ticker(asset)
            data = data.history(day_format)
            data = data['Close'].iloc[-1]

        elif asset.find("1") == -1:

            day_format = day.strftime("%Y-%m-%d")
            data = yf.Ticker(f"{asset}.SA")
            data = data.history(day_format)
            data = data['Close'].iloc[-1]

        asset_value = asset_value + (data * np.sum(np.array(asset_amount)))

    print(day, asset_value)
