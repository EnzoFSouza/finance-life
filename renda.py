import json

def escreverRenda():
    f = open("finance-life/fontes_renda.txt", "a+")
    y = json.dumps(lista_fontes_renda)
    f.write(y)
    f.close()

def escreverDespesa():
    f = open("finance-life/despesas.txt", "a+")
    y = json.dumps(lista_despesas)
    f.write(y)
    f.close()

def criarRendaOuDespesa(nome, valor):
    x = {
        "nome": nome,
        "valor": valor,
    }
    return x

#lista contendo dicionarios, cada dicionario é uma despesa
lista_despesas = list() 

#lista contendo dicionarios, cada dicionario é uma fonte de renda
lista_fontes_renda = list()

#numero de despesas e de fontes de renda
n_despesas = int(input())
n_fontes_renda = int(input())

#preenchendo lista_despesas
for i in range(n_despesas):
    nome = input()
    valor = float(input())
    lista_despesas.append(criarRendaOuDespesa(nome, valor))

#preenchendo lista_fontes_renda
for i in range(n_fontes_renda):
    nome = input()
    valor = float(input())
    lista_fontes_renda.append(criarRendaOuDespesa(nome, valor))

escreverRenda()
escreverDespesa()
print(lista_despesas)
print(lista_fontes_renda)