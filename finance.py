PRECO_MEDIO = 10
QUANTIDADE = 2
DY = 10 #% ao ano
GANHO_DIA = 1.00

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

calcGanhoAtivo(8)
calcDividendosAtivo(8)
calcGanhoMes(True)
calcGanhoAno(5)