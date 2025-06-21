import pandas as pd
from finance_oop import Ativo
from cliente_oop import Cliente

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
    datas_pag = ativos_df.at[i, "Datas Pag"]
    lista_ativos.append(Ativo(nome, preco_medio, quantidade, dy_anual, dy_mensal, datas_pag))
    lista_precos_atuais.append(preco_atual)

cliente = Cliente(lista_ativos, lista_precos_atuais, GANHO_DIARIO)
cliente.loop()

#ativos_df = pd.read_csv("finance-life/ativos.csv")
#valores_df = ativos_df[["Preco Medio", "Dividend Yield", "Quantidade", "Preco Atual"]]
#coluna_preco_medio = ativos_df[["Preco Medio"]]
#preco_especifico = ativos_df.at[0, "Preco Medio"]
#print(ativos_df) #print dataframe inteiro
#print(valores_df) #print das colunas preco medio, dividend yield, quantidade e preco atual
#print(coluna_preco_medio) #print coluna preco medio
#print(preco_especifico) #print valor especifico da linha 0 e coluna preco medio
#print(ativos_df.shape)
#print(ativos_df.shape[0]) #linhas
#print(ativos_df.shape[1]) #colunas