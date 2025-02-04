def criarRendaOuDespesa(nome, valor):
    x = {
        "nome": nome,
        "valor": valor,
    }
    return x

def somar(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]["valor"]
    
    return soma

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

total_despesas = somar(lista_despesas)
total_fontes_renda = somar(lista_fontes_renda)

print(lista_despesas)
print(total_despesas)

print(lista_fontes_renda)
print(total_fontes_renda)
