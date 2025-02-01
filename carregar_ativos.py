import json
from finance_oop import Ativo

#criando uma lista de objetos
lista_de_objetos = list()

#pegando todos os ativos salvos em "ativos.txt" e obtendo uma lista de dicionários
with open("finance-life/ativos.txt", "r") as f:
    ativos = json.load(f) #lista de dicionarios
    print(ativos)
    f.close()

for i in range(len(ativos)):
    #print(ativos[i])
    #preenchendo a lista de objetos (com objetos)
    meu_ativo = Ativo(ativos[i]["nome"], ativos[i]["preco_medio"], ativos[i]["quantidade"], ativos[i]["dy"])
    lista_de_objetos.append(meu_ativo)

for i in range(len(lista_de_objetos)):
    print(lista_de_objetos[i].nome)