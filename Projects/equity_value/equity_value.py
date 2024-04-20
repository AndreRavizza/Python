import pandas as pd

#Importando o arquivo

df = pd.read_excel('Equity Value.xlsx')

#Selecionando a coluna "Produto" e alterando-a para apenas o texto antes do "-"

#.str.split divide o texto em duas partes com base no caractere
#.str[0] seleciona apena a primeira parte do que foi selecionado
#.str.strip() remove os espaços do texto

df['Produto'] = df['Produto'].str.split('-').str[0].str.strip()

print(df)
