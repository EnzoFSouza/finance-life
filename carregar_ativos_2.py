import pandas as pd

ativos_df = pd.read_csv("ativos.csv")
valores_df = ativos_df[["Preco Medio", "Dividend Yield", "Quantidade", "Preco Atual"]]
print(ativos_df)
print(valores_df)