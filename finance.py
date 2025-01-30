PRECO_MEDIO = 10
QUANTIDADE = 2
DY = 10 #% ao ano
GANHO_DIA = 2.40

def calcGanhos(preco_atual):
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

def calcGanhoMes():
    x = GANHO_DIA * 22
    print(f"Em um mês, você receberá R${x}")

calcGanhos(8)
calcDividendosAtivo(8)
calcGanhoMes()