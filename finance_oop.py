class Ativo():
    def __init__(self, nome, preco_medio, qtd, dy):
        self.nome = nome
        self.preco_medio = preco_medio
        self.qtd = qtd
        self.dy = dy #% ao ano

        self.ganho = 0
        self.dividendos = 0
        self.participacao = 0 #%
    
    #calcular ganho considerando todas as acoes
    def calcGanho(self, preco_atual):
        self.ganho = (preco_atual - self.preco_medio) * self.qtd
        self.ganho = round(self.ganho, 2)
        return self.ganho
    
    #calcular estimativa de dividendos anual
    def calcDividendos(self, preco_atual):
        self.dividendos = (preco_atual * (self.dy/100) * self.qtd)
        self.dividendos = round(self.dividendos, 2)
        return self.dividendos
    
    def calcPorcentagem(self, preco_atual, valor_total):
        self.participacao = ((preco_atual * self.qtd) * 100) / valor_total
        self.participacao = round(self.participacao, 2)
        return self.participacao


#meu_ativo = Ativo("ABC3", 20, 2, 12)
#
#print(meu_ativo.ganho)
#meu_ativo.calcGanho(22)
#print(meu_ativo.ganho)

#print(meu_ativo.dividendos)
#meu_ativo.calcDividendos(22)
#print(meu_ativo.dividendos)