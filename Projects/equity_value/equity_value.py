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

# Criando uma lista para controlar os ativos inválidos que devem ser removidos

removed_assets = []

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

            if asset_ticker not in removed_assets:

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

    day = pd.to_datetime(day, format="%Y-%m/%d")

    start_date = day - timedelta(days=7)

    end_date = day + timedelta(days=1)

    start_date = start_date.strftime("%Y-%m-%d")

    end_date = end_date.strftime("%Y-%m-%d")

    day = day.strftime("%Y-%m-%d")
    
    for asset in assets_dic:

        asset_amount = assets_dic[asset]

        if asset.find("3") == -1 and asset.find("4") == -1 and asset.find("11") == -1 and asset.find("1") == -1:

            asset_yf = yf.Ticker(asset)

            historical_data = asset_yf.history(start=start_date, end=end_date)

            if day in historical_data.index:

                close_price = historical_data.loc[day, 'Close']

                asset_value = asset_value + (close_price * np.sum(np.array(asset_amount)))

            elif day not in historical_data.index and not historical_data.empty:

                close_price = historical_data['Close'].iloc[-1]

                asset_value = asset_value + (close_price * np.sum(np.array(asset_amount)))

            else:

                if asset not in removed_assets:

                    removed_assets.append(asset)

        elif asset.find("1") == -1:

            asset_yf = yf.Ticker(f"{asset}.SA")

            historical_data = asset_yf.history(start=start_date, end=end_date)

            if day in historical_data.index:

                close_price = historical_data.loc[day, 'Close']

                asset_value = asset_value + (close_price * np.sum(np.array(asset_amount)))

            elif day not in historical_data.index and not historical_data.empty:

                close_price = historical_data['Close'].iloc[-1]

                asset_value = asset_value + (close_price * np.sum(np.array(asset_amount)))

            else:

                 if asset not in removed_assets:

                    removed_assets.append(asset)

    for removed_asset in removed_assets:

        if removed_asset in assets_dic:

            assets_dic.pop(removed_asset)

    print(day, asset_value)
