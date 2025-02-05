import json

lista_renda = list()
#pegando todas as rendas salvas em "fontes_renda.txt" e obtendo uma lista de dicionários
with open("finance-life/fontes_renda.txt", "r") as f:
    lista_renda = json.load(f) #lista de dicionarios
    f.close()

print(lista_renda)
