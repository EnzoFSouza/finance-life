PRECO_MEDIO = 10.0
QUANTIDADE = 2
GANHO_DIA = 1.0
DY = 10 #% ao ano

def calcGanhoAtivo(preco_atual):
    x = (preco_atual - PRECO_MEDIO) * QUANTIDADE
    if x >= 0:
        print(f"Ganho de R${x:.2f}")
    else:
        print(f"Perda de: R${abs(x):.2f}")

    return x

def calcDividendosAtivo(preco_atual):
    x = (preco_atual * DY/100) * QUANTIDADE
    print(f"De acordo com a estimativa, você receberá R${x:.2f} de dividendos no ano")
    return x

def calcGanhoMes(printar = False):
    x = GANHO_DIA * 22
    if printar:
        print(f"Em um mês, você receberá R${x}")
    return x

def calcGanhoAno(num_de_anos, printar = False):
    soma = calcGanhoMes(printar) * 12 * num_de_anos 
    
    print(f"Em {num_de_anos} ano(s), você receberá R${soma:.2f}")
    return soma

def calcTempoMeta(meta):
    tempo = meta // calcGanhoAno(1)
    print(tempo)
    return tempo

def calcBolaDeNeve(preco_atual, dy_mensal):
    x = preco_atual * (dy_mensal / 100) #rendimento de uma cota de um ativo
    qtd_bola_neve = preco_atual//x #qtd de cotas necessarias para comprar uma nova cota do ativo
    print(f"Quantidade aproximada de cotas para bola de neve: {qtd_bola_neve}")
    return qtd_bola_neve

meta = float(input())

calcGanhoAtivo(8)
calcDividendosAtivo(8)
calcGanhoMes(True)
calcGanhoAno(5)
calcTempoMeta(meta)
calcBolaDeNeve(10, 1)