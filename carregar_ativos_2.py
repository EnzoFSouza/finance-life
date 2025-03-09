import pandas as pd

ativos_df = pd.read_csv("finance-life/ativos.csv")
valores_df = ativos_df[["Preco Medio", "Dividend Yield", "Quantidade", "Preco Atual"]]
coluna_preco_medio = ativos_df[["Preco Medio"]]
preco_especifico = ativos_df.at[0, "Preco Medio"]

print(ativos_df) #print dataframe inteiro
print(valores_df) #print das colunas preco medio, dividend yield, quantidade e preco atual
print(coluna_preco_medio) #print coluna preco medio
print(preco_especifico) #print valor especifico da linha 0 e coluna preco medio