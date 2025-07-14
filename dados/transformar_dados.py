import pandas as pd

# Carregar CSV já pulando cabeçalho
df = pd.read_csv('dados/taxa de analfabetismo.csv', sep=';', encoding='utf-8', skiprows=4)

# Lista dos anos com índice
anos = [2016, 2017, 2018, 2019, 2022, 2023, 2024]

# Lista final para armazenar os dados reorganizados
dados_longos = []

colunas_total = [f'Total' if i == 0 else f'Total.{i}' for i in range(len(anos))]
colunas_branca = [f'Branca' if i == 0 else f'Branca.{i}' for i in range(len(anos))]
colunas_preta = [f'Preta ou parda' if i == 0 else f'Preta ou parda.{i}' for i in range(len(anos))]

for index, row in df.iterrows():
    faixa = row['Grupo de idade']
    if pd.isnull(faixa):
        continue

    for i in range(len(anos)):
        try:
            dados_longos.append({'Ano': anos[i], 'Faixa Etária': faixa, 'Cor/Raça': 'Total', 'Valor': row[colunas_total[i]]})
            dados_longos.append({'Ano': anos[i], 'Faixa Etária': faixa, 'Cor/Raça': 'Branca', 'Valor': row[colunas_branca[i]]})
            dados_longos.append({'Ano': anos[i], 'Faixa Etária': faixa, 'Cor/Raça': 'Preta ou parda', 'Valor': row[colunas_preta[i]]})
        except KeyError:
            print(f"❌ Coluna não encontrada para ano {anos[i]} — pulando...")
            continue

# Criar novo DataFrame organizado
df_longo = pd.DataFrame(dados_longos)

# Exibir para teste
print(df_longo.head(10))

# Salvar para usar no Power BI / Tableau
df_longo.to_csv('dados/analfabetismo_transformado.csv', index=False, encoding='utf-8-sig')
print("Arquivo transformado salvo com sucesso!")
print(df_longo.head(10))
print(f"\nTotal de linhas: {len(df_longo)}")
