import json
from finance_oop import Ativo
from cliente_oop import Pessoa

GANHO_DIARIO = 1.5

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

pessoa = Pessoa(lista_de_objetos, precos_atuais, GANHO_DIARIO)
pessoa.loop()