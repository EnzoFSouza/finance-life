PRECO_MEDIO = 10
QUANTIDADE = 2

def calcGanhos(preco_atual):
    x = (preco_atual - PRECO_MEDIO) * QUANTIDADE
    if x >= 0:
        print(f"Ganho de R${x:.2f}")
    else:
        print(f"Perda de: R${abs(x):.2f}")

    return x

calcGanhos(8)