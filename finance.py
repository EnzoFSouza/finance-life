#Código      Preço Médio      Quantidade      Preço Atual      Valorização
ABC11 = {
    "preco_medio": 20.0,
    "quantidade": 2,
    "dy": 12,
    "preco_atual": 25,
}
DEF11 = {
    "preco_medio": 5.0,
    "quantidade": 10,
    "dy": 6,
    "preco_atual": 10,
}

GHI34 = {
    "preco_medio": 10,
    "quantidade": 2,
    "dy": 12,
    "preco_atual": 15,
}

JKL33 = {
    "preco_medio": 1,
    "quantidade": 15,
    "dy": 0,
    "preco_atual": 2,
}

MNO11 = {
    "preco_medio": 10,
    "quantidade": 5,
    "dy": 8,
    "preco_atual": 5,
}

PQR3 = {
    "preco_medio": 50,
    "quantidade": 2,
    "dy": 12,
    "preco_atual": 60,
}

STU3 = {
    "preco_medio": 90,
    "quantidade": 1,
    "dy": 12,
    "preco_atual": 100,
}

VWX4 = {
    "preco_medio": 15,
    "quantidade": 3,
    "dy": 0,
    "preco_atual": 20,
}

YZA4 = {
    "preco_medio": 3,
    "quantidade": 12,
    "dy": 0,
    "preco_atual": 5,
}

BCD34 = {
    "preco_medio": 28,
    "quantidade": 6,
    "dy": 9,
    "preco_atual": 30,
}

EFG11 = {
    "preco_medio": 34,
    "quantidade": 1,
    "dy": 12,
    "preco_atual": 35,
}

HIJ4 = {
    "preco_medio": 30,
    "quantidade": 4,
    "dy": 9,
    "preco_atual": 35,
}

KLM11 = {
    "preco_medio": 12,
    "quantidade": 5,
    "dy": 8,
    "preco_atual": 15,
}

NOP3 = {
    "preco_medio": 70,
    "quantidade": 4,
    "dy": 10,
    "preco_atual": 50,
}

QRS4 = {
    "preco_medio": 40,
    "quantidade": 5,
    "dy": 9,
    "preco_atual": 40,
}

TUV4 = {
    "preco_medio": 89,
    "quantidade": 10,
    "dy": 13,
    "preco_atual": 90,
}

WXY11 = {
    "preco_medio": 50,
    "quantidade": 4,
    "dy": 12,
    "preco_atual": 49,
}

ZAB4 = {
    "preco_medio": 50,
    "quantidade": 2,
    "dy": 11,
    "preco_atual": 55,
}

CDE3 = {
    "preco_medio": 7,
    "quantidade": 7,
    "dy": 8,
    "preco_atual": 10,
}

FGH34 = {
    "preco_medio": 9,
    "quantidade": 5,
    "dy": 10,
    "preco_atual": 10,
}

IJK11 = {
    "preco_medio": 18,
    "quantidade": 4,
    "dy": 9,
    "preco_atual": 20,
}

LMN5 = {
    "preco_medio": 18,
    "quantidade": 10,
    "dy": 12,
    "preco_atual": 25,
}

OPQ11 = {
    "preco_medio": 3,
    "quantidade": 10,
    "dy": 9,
    "preco_atual": 6,
}

RST11 = {
    "preco_medio": 2,
    "quantidade": 10,
    "dy": 0,
    "preco_atual": 6,
}

UVW3 = {
    "preco_medio": 10,
    "quantidade": 5,
    "dy": 9,
    "preco_atual": 18,
}

XYZ11 = {
    "preco_medio": 100,
    "quantidade": 1,
    "dy": 13,
    "preco_atual": 150,
}

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

calcGanhoAtivo(8)
calcDividendosAtivo(8)
calcGanhoMes(True)
calcGanhoAno(5)