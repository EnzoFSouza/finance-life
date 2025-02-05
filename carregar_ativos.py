import json
from finance_oop import Ativo

def printarOpcoes():
    for i in range(len(lista_de_objetos)):
        print(lista_de_objetos[i].nome, end = " ")
    print()

def encontrarAtivo(nome):
    #Percorrendo todos os ativos até encontrar aquele com o nome digitado
    for i in range(len(lista_de_objetos)):
        if lista_de_objetos[i].nome == nome:
            return i
    return None

#Somatoria da multiplicacao dos precos atuais pelas respectivas quantidades para obter o valor da carteira
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

    print(f"Nome: {objeto.nome}")
    print(f"Preco Medio: R${objeto.preco_medio:.2f}")
    print(f"Preco Atual: R${preco_atual:.2f}")
    print(f"Quantidade: {objeto.qtd}")
    print(f"DY: {objeto.dy}")
    print(f"Ganho: R${objeto.ganho:.2f}")
    print(f"Dividendos: R${objeto.dividendos:.2f}")
    print(f"Participacao: {objeto.participacao}%")
    print(f"Valor total do ativo: R${objeto.valor_total:.2f}")

#criando uma lista de objetos
lista_de_objetos = list()

#lista de precos atuais
precos_atuais = list()

#pegando todos os ativos salvos em "ativos.txt" e obtendo uma lista de dicionários
with open("finance-life/ativos.txt", "r") as f:
    #lista de dicionarios
    ativos = json.load(f) 
    f.close()

for i in range(len(ativos)):
    #preenchendo a lista de objetos (com objetos)
    meu_ativo = Ativo(ativos[i]["nome"], ativos[i]["preco_medio"], ativos[i]["quantidade"], ativos[i]["dy"])
    lista_de_objetos.append(meu_ativo)

    #preenchendo a lista de precos atuais com o valor do preco medio + 5 para fins de testes
    precos_atuais.append(ativos[i]["preco_medio"] + 5)

valor_carteira = obterValorCarteira()
printarOpcoes()

nome = input()
while (nome != "sair"):
    indice = encontrarAtivo(nome)
    if (indice == None):
        print("Ativo não encontrado, digite novamente")
    
    else:
        status(lista_de_objetos[indice], precos_atuais[indice], valor_carteira)
    
    printarOpcoes()
    nome = input()