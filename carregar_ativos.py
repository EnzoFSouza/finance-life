import json
from finance_oop import Ativo

def encontrarAtivo(nome):
    #Percorrendo todos os ativos até encontrar aquele com o nome digitado
    for i in range(len(lista_de_objetos)):
        if lista_de_objetos[i].nome == nome:
            return i

def status(objeto, preco_atual):
    objeto.calcGanho(preco_atual)
    objeto.calcDividendos(preco_atual)

    print("Nome: ", objeto.nome)
    print("Preco Medio: ", objeto.preco_medio)
    print("Quantidade: ", objeto.qtd)
    print("DY: ", objeto.dy)
    print("Ganho: ", objeto.ganho)
    print("Dividendos: ", objeto.dividendos)

#criando uma lista de objetos
lista_de_objetos = list()

#pegando todos os ativos salvos em "ativos.txt" e obtendo uma lista de dicionários
with open("finance-life/ativos.txt", "r") as f:
    ativos = json.load(f) #lista de dicionarios
    #print(ativos)
    f.close()

for i in range(len(ativos)):
    #print(ativos[i])
    #preenchendo a lista de objetos (com objetos)
    meu_ativo = Ativo(ativos[i]["nome"], ativos[i]["preco_medio"], ativos[i]["quantidade"], ativos[i]["dy"])
    lista_de_objetos.append(meu_ativo)

#printando o nome de todos os objetos em "lista_de_objetos"
#for i in range(len(lista_de_objetos)):
#    print(lista_de_objetos[i].nome)

nome = input()
while (nome != "sair"):
    indice = encontrarAtivo(nome)
    #print(lista_de_objetos[indice].nome)
    #print(lista_de_objetos[indice].preco_medio)
    #print(lista_de_objetos[indice].qtd)
    #print(lista_de_objetos[indice].dy)
    status(lista_de_objetos[indice], 150)
    nome = input()