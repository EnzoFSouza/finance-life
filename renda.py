def criarDespesa(nome, valor):
    despesa = {
        "nome": nome,
        "valor": valor,
    }
    return despesa

def criarFonteRenda(nome, valor):
    fonte_renda = {
        "nome": nome,
        "valor": valor,
    }   

    return fonte_renda

#lista contendo dicionarios, cada dicionario é uma despesa
lista_despesas = list() 

#lista contendo dicionarios, cada dicionario é uma fonte de renda
lista_fontes_renda = list()

#numero de despesas e de fontes de renda
n_despesas = int(input())
n_fontes_renda = int(input())

for i in range(n_despesas):
    nome = input()
    valor = float(input())
    lista_despesas.append(criarDespesa(nome, valor))

for i in range(n_fontes_renda):
    nome = input()
    valor = float(input())
    lista_fontes_renda.append(criarFonteRenda(nome, valor))

print(lista_despesas)
print(lista_fontes_renda)