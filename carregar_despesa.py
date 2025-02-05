import json

lista_despesas = list()
#pegando todas as despesas salvas em "despesas.txt" e obtendo uma lista de dicionários
with open("finance-life/despesas.txt", "r") as f:
    lista_despesas = json.load(f) #lista de dicionarios
    f.close()

print(lista_despesas)
