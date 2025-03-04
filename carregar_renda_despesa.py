import json

def somar(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]["valor"]
    
    return soma

def status():
    print(f"Lista renda: {lista_renda}")
    print(f"Total renda: R${total_renda:.2f}")
    print(f"Lista despesas: {lista_despesas}")
    print(f"Total despesas: R${total_despesas:.2f}")
    if diferenca < 0:
        print(f"Déficit de R${abs(diferenca):.2f}")
    else:
        print(f"Ganho de R${diferenca:.2f}")
        
lista_renda = list()
lista_despesas = list()

#pegando todas as rendas salvas em "fontes_renda.txt" e obtendo uma lista de dicionários
with open("finance-life/fontes_renda.txt", "r") as f:
    lista_renda = json.load(f) #lista de dicionarios
    f.close()

#pegando todas as despesas salvas em "despesas.txt" e obtendo uma lista de dicionários
with open("finance-life/despesas.txt", "r") as f:
    lista_despesas = json.load(f) #lista de dicionarios
    f.close()

total_despesas = somar(lista_despesas)
total_renda = somar(lista_renda)

diferenca = total_renda - total_despesas

status()