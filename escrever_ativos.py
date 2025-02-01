import json

ABC11 = {
    "nome": "ABC11",
    "preco_medio": 20.0,
    "quantidade": 2,
    "dy": 12,
    "preco_atual": 25,
}

DEF11 = {
    "nome": "DEF11",
    "preco_medio": 5.0,
    "quantidade": 10,
    "dy": 6,
    "preco_atual": 10,
}

GHI34 = {
    "nome": "GHI34",
    "preco_medio": 10,
    "quantidade": 2,
    "dy": 12,
    "preco_atual": 15,
}

JKL33 = {
    "nome": "JKL33",
    "preco_medio": 1,
    "quantidade": 15,
    "dy": 0,
    "preco_atual": 2,
}

MNO11 = {
    "nome": "MNO11",
    "preco_medio": 10,
    "quantidade": 5,
    "dy": 8,
    "preco_atual": 5,
}

PQR3 = {
    "nome": "PQR3",
    "preco_medio": 50,
    "quantidade": 2,
    "dy": 12,
    "preco_atual": 60,
}

STU3 = {
    "nome": "STU3",
    "preco_medio": 90,
    "quantidade": 1,
    "dy": 12,
    "preco_atual": 100,
}

VWX4 = {
    "nome": "VWX4",
    "preco_medio": 15,
    "quantidade": 3,
    "dy": 0,
    "preco_atual": 20,
}

YZA4 = {
    "nome": "YZA4",
    "preco_medio": 3,
    "quantidade": 12,
    "dy": 0,
    "preco_atual": 5,
}

BCD34 = {
    "nome": "BCD34",
    "preco_medio": 28,
    "quantidade": 6,
    "dy": 9,
    "preco_atual": 30,
}

EFG11 = {
    "nome": "EFG11",
    "preco_medio": 34,
    "quantidade": 1,
    "dy": 12,
    "preco_atual": 35,
}

HIJ4 = {
    "nome": "HIJ4",
    "preco_medio": 30,
    "quantidade": 4,
    "dy": 9,
    "preco_atual": 35,
}

KLM11 = {
    "nome": "KLM11",
    "preco_medio": 12,
    "quantidade": 5,
    "dy": 8,
    "preco_atual": 15,
}

NOP3 = {
    "nome": "NOP3",
    "preco_medio": 70,
    "quantidade": 4,
    "dy": 10,
    "preco_atual": 50,
}

QRS4 = {
    "nome": "QRS4",
    "preco_medio": 40,
    "quantidade": 5,
    "dy": 9,
    "preco_atual": 40,
}

TUV4 = {
    "nome": "TUV4",
    "preco_medio": 89,
    "quantidade": 10,
    "dy": 13,
    "preco_atual": 90,
}

WXY11 = {
    "nome": "WXY11",
    "preco_medio": 50,
    "quantidade": 4,
    "dy": 12,
    "preco_atual": 49,
}

ZAB4 = {
    "nome": "ZAB4",
    "preco_medio": 50,
    "quantidade": 2,
    "dy": 11,
    "preco_atual": 55,
}

CDE3 = {
    "nome": "CDE3",
    "preco_medio": 7,
    "quantidade": 7,
    "dy": 8,
    "preco_atual": 10,
}

FGH34 = {
    "nome": "FGH34",
    "preco_medio": 9,
    "quantidade": 5,
    "dy": 10,
    "preco_atual": 10,
}

IJK11 = {
    "nome": "IJK11",
    "preco_medio": 18,
    "quantidade": 4,
    "dy": 9,
    "preco_atual": 20,
}

LMN5 = {
    "nome": "LMN5",
    "preco_medio": 18,
    "quantidade": 10,
    "dy": 12,
    "preco_atual": 25,
}

OPQ11 = {
    "nome": "OPQ11",
    "preco_medio": 3,
    "quantidade": 10,
    "dy": 9,
    "preco_atual": 6,
}

RST11 = {
    "nome": "RST11",
    "preco_medio": 2,
    "quantidade": 10,
    "dy": 0,
    "preco_atual": 6,
}

UVW3 = {
    "nome": "UVW3",
    "preco_medio": 10,
    "quantidade": 5,
    "dy": 9,
    "preco_atual": 18,
}

XYZ11 = {
    "nome": "XYZ11",
    "preco_medio": 100,
    "quantidade": 1,
    "dy": 13,
    "preco_atual": 150,
}

lista_ativos = [ABC11, DEF11, GHI34, JKL33, MNO11, PQR3, STU3, VWX4, YZA4, BCD34,
                EFG11, HIJ4, LMN5, OPQ11, RST11, UVW3, XYZ11]

f = open("finance-life/ativos.txt", "a+")

#loop por todos os dicionários python para escrever todos os ativos
for i in range(len(lista_ativos)):
    if i == 0:
        f.write("[")

    #convertendo de python para json
    if i == len(lista_ativos) - 1:
        y = json.dumps(lista_ativos[i])
        f.write(y + "]")
    
    else:
        y = json.dumps(lista_ativos[i])
        f.write(y + ",")

f.close()