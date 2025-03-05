class Ativo():
    def __init__(self, nome, preco_medio, qtd, dy_anual, dy_mensal):
        self.nome = nome
        self.preco_medio = preco_medio
        self.qtd = qtd
        self.dy_anual = dy_anual #% ao ano
        self.dy_mensal = dy_mensal #% ao mes

        self.ganho = 0
        self.dividendos = 0
        self.participacao = 0 #%
        self.valor_total = 0
        self.dividendo_uma_cota = 0
        self.qtd_bola_neve = 0
        self.expectativa_de_ganho = 0
    
    #calcular ganho considerando todas as acoes
    def calcGanho(self, preco_atual):
        self.ganho = (preco_atual - self.preco_medio) * self.qtd
        self.ganho = round(self.ganho, 2)
        return self.ganho
    
    #calcular estimativa de dividendos anual
    def calcDividendosAnual(self, preco_atual):
        self.dividendos = (preco_atual * (self.dy_anual/100) * self.qtd)
        self.dividendos = round(self.dividendos, 2)
        return self.dividendos
    
    #calcular participacao de um ativo na carteira
    def calcParticipacao(self, preco_atual, valor_carteira):
        self.participacao = ((preco_atual * self.qtd) * 100) / valor_carteira
        self.participacao = round(self.participacao, 2)
        return self.participacao
    
    #calcular valor total do ativo na carteira
    def calcValorTotalAtivo(self, preco_atual):
        self.valor_total = preco_atual * self.qtd
        return self.valor_total
    
    def calcBolaDeNeve(self, preco_atual):
        self.dividendo_uma_cota = preco_atual * (self.dy_mensal / 100) #rendimento de uma cota de um ativo
        self.qtd_bola_neve = preco_atual//self.dividendo_uma_cota #qtd de cotas necessarias para comprar uma nova cota do ativo
        return self.qtd_bola_neve

    def calcRendimentoMes(self, preco_atual):
        self.expectativa_de_ganho = preco_atual * (self.dy_mensal / 100) * self.qtd
        return self.expectativa_de_ganho