import pandas as pd
from finance_oop import Ativo
from cliente_oop import Pessoa

GANHO_DIARIO = 1

#carregar dataframe usando pandas
ativos_df = pd.read_csv("finance-life/ativos_melhor.csv")

lista_ativos = list() #lista que irá armazenar objetos criados a partir das propriedades dos ativos
lista_precos_atuais = list() #lista que irá armazenar os preços atuais

for i in range(ativos_df.shape[0]):
    #print(f"Ativo {i+1}")
    nome = ativos_df.at[i, "Nome"]
    preco_medio = ativos_df.at[i, "Preco Medio"]
    preco_atual = ativos_df.at[i, "Preco Atual"]
    quantidade = ativos_df.at[i, "Quantidade"]
    dy_mensal = ativos_df.at[i, "Dividend Yield Mensal"]
    dy_anual = ativos_df.at[i, "Dividend Yield Anual"]
    lista_ativos.append(Ativo(nome, preco_medio, quantidade, dy_anual, dy_mensal))
    lista_precos_atuais.append(preco_atual)

pessoa = Pessoa(lista_ativos, lista_precos_atuais, GANHO_DIARIO)
pessoa.loop()