import json
from finance_oop import Ativo

GANHO_DIA = 1.0

def calcGanhoMes():
    x = GANHO_DIA * 22
    #print(f"Recebendo {GANHO_DIA} por dia durante um mês, você receberá R${x}")
    return x

def calcGanhoAno(num_anos):
    valor = calcGanhoMes() * 12 * num_anos 
    print(f"Em {num_anos} ano(s), você receberá R${valor:.2f}")
    return valor

def calcTempoMeta(meta):
    tempo = meta // calcGanhoAno(1) #tempo em anos
    return tempo

def printarOpcoes():
    for i in range(len(lista_de_objetos)):
        print(lista_de_objetos[i].nome, end = " ")
    
    nomes_funcoes = ["calcGanhoMes", "calcGanhoAno", "calcTempoMeta"]
    for i in range(len(nomes_funcoes)):
        print(nomes_funcoes[i], end = " ")
        
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
    objeto.calcDividendosAnual(preco_atual)
    objeto.calcParticipacao(preco_atual, valor_carteira)
    objeto.calcValorTotalAtivo(preco_atual)
    objeto.calcBolaDeNeve(preco_atual)
    objeto.calcRendimentoMes(preco_atual)

    print(f"Nome: {objeto.nome}")
    print(f"Preco Medio: R${objeto.preco_medio:.2f}")
    print(f"Preco Atual: R${preco_atual:.2f}")
    print(f"Quantidade: {objeto.qtd}")
    print(f"DY Anual: {objeto.dy_anual}")
    print(f"DY Mensal: {objeto.dy_mensal}")
    print(f"Ganho: R${objeto.ganho:.2f}")
    print(f"Rendimento estimado para o ano: R${objeto.dividendos:.2f}")
    print(f"Participacao: {objeto.participacao}%")
    print(f"Valor total do ativo: R${objeto.valor_total:.2f}")
    print(f"Quantidade para efeito bola de neve: {objeto.qtd_bola_neve}")
    print(f"Rendimento estimado para o mês: R${objeto.expectativa_de_ganho:.2f}")

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
    meu_ativo = Ativo(ativos[i]["nome"], ativos[i]["preco_medio"], ativos[i]["quantidade"], ativos[i]["dy_anual"], ativos[i]["dy_mensal"])
    lista_de_objetos.append(meu_ativo)

    #preenchendo a lista de precos atuais com o valor do preco medio + 5 para fins de testes
    precos_atuais.append(ativos[i]["preco_medio"] + 5)

valor_carteira = obterValorCarteira()
printarOpcoes()

nome = input()
while (nome != "sair"):
    if nome == "calcGanhoMes":
        ganho_mensal = calcGanhoMes()
        print(f"Recebendo {GANHO_DIA} por dia durante um mês, você receberá R${ganho_mensal}")
    
    elif nome == "calcGanhoAno":
        n_anos = int(input())
        ganho_anual = calcGanhoAno(n_anos)
    
    elif nome == "calcTempoMeta":
        meta = int(input())
        tempo_anos = calcTempoMeta(meta)
        print(f"Em {tempo_anos}, você atingirá sua meta de {meta}")

    else:
        indice = encontrarAtivo(nome)
        if (indice == None):
            print("Ativo não encontrado, digite novamente")
    
        else:
            status(lista_de_objetos[indice], precos_atuais[indice], valor_carteira)
    
    printarOpcoes()
    nome = input()