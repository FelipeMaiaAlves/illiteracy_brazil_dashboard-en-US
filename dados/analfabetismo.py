import pandas as pd

# Lê o arquivo ignorando as 4 primeiras linhas com texto
df = pd.read_csv('dados/taxa de analfabetismo.csv', sep=';', encoding='utf-8', skiprows=4)

# Exibir as primeiras linhas
print(df.head())

# Ver colunas
print(df.columns.tolist())

# Ver informações
print(df.info())
