import json
from finance_oop import Ativo

def encontrarAtivo(nome):
    #Percorrendo todos os ativos até encontrar aquele com o nome digitado
    for i in range(len(lista_de_objetos)):
        if lista_de_objetos[i].nome == nome:
            return i

def printarOpcoes():
    for i in range(len(lista_de_objetos)):
        print(lista_de_objetos[i].nome, end = " ")

precos_atuais = list()
#criar funcao para somar todos os precos atuais de cada ativo, multiplicar pelas respectivas quantidades
#e obter o valor _total, para ter a porcentagem de cada ativo na carteira
def obterValorCarteira():
    valor_carteira = 0
    for i in range(len(precos_atuais)):
        valor_carteira += precos_atuais[i] * lista_de_objetos[i].qtd
    return valor_carteira

def status(objeto, preco_atual, valor_carteira):
    objeto.calcGanho(preco_atual)
    objeto.calcDividendos(preco_atual)
    objeto.calcParticipacao(preco_atual, valor_carteira)
    objeto.calcValorTotalAtivo(preco_atual)

    print("Nome: ", objeto.nome)
    print("Preco Medio: ", objeto.preco_medio)
    print("Preco Atual: ", preco_atual)
    print("Quantidade: ", objeto.qtd)
    print("DY: ", objeto.dy)
    print("Ganho: ", objeto.ganho)
    print("Dividendos: ", objeto.dividendos)
    print(f"Participacao: {objeto.participacao}%")
    print(f"Valor total do ativo: {objeto.valor_total}")

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
    #preenchendo a lista de precos atuais com o valor do preco medio + 5 para fins de testes
    precos_atuais.append(ativos[i]["preco_medio"] + 5)

print(precos_atuais)
#printando o nome de todos os objetos em "lista_de_objetos"
#for i in range(len(lista_de_objetos)):
#    print(lista_de_objetos[i].nome)

printarOpcoes()
print()
nome = input()
while (nome != "sair"):
    indice = encontrarAtivo(nome)
    #print(lista_de_objetos[indice].nome)
    #print(lista_de_objetos[indice].preco_medio)
    #print(lista_de_objetos[indice].qtd)
    #print(lista_de_objetos[indice].dy)
    status(lista_de_objetos[indice], precos_atuais[indice], obterValorCarteira())
    printarOpcoes()
    print()
    nome = input()