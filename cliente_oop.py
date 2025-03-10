import math
class Cliente():
    def __init__(self, carteira, precos_atuais, ganho_diario):
        self.carteira = carteira #lista de objetos
        self.precos_atuais = precos_atuais #lista com precos atuais dos ativos na ordem correta
        self.valor_carteira = 0
        self.ganho_diario = ganho_diario
        self.ganho_mes = 0
        self.ganho_ano = 0
        self.num_anos = 1
        self.meta = 0
        self.tempo_meta = 0 #Em anos
        self.nome = ""
        self.indice = None
    
    def calcGanhoMes(self):
        self.ganho_mes = self.ganho_diario * 22
        return self.ganho_mes

    def calcGanhoAno(self):
        self.ganho_ano = self.calcGanhoMes() * 12 * self.num_anos 
        print(f"Em {self.num_anos} ano(s), você receberá R${self.ganho_ano:.2f}")
        return self.ganho_ano

    def calcTempoMeta(self):
        self.tempo_meta = self.meta / self.calcGanhoAno() #tempo em anos
        self.tempo_meta = math.ceil(self.tempo_meta)
        return self.tempo_meta

    def status(self, objeto, preco_atual):
        objeto.calcGanho(preco_atual)
        objeto.calcDividendosAnual(preco_atual)
        objeto.calcParticipacao(preco_atual, self.valor_carteira)
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

    def encontrarAtivo(self):
        #Percorrendo todos os ativos até encontrar aquele com o nome digitado
        for i in range(len(self.carteira)):
            if self.carteira[i].nome == self.nome:
                return i
        return None

    def obterValorCarteira(self):
        for i in range(len(self.precos_atuais)):
            self.valor_carteira += self.precos_atuais[i] * self.carteira[i].qtd
        return self.valor_carteira

    def opcoes(self):
        for i in range(len(self.carteira)):
            print(self.carteira[i].nome, end = " ")
    
        nomes_funcoes = ["calcGanhoMes", "calcGanhoAno", "calcTempoMeta"]
        for i in range(len(nomes_funcoes)):
            print(nomes_funcoes[i], end = " ")
        
        print("sair", end = " ")
        
        print()

    def loop(self):
        self.opcoes()
        self.nome = input()
        while (self.nome != "sair"):
            if self.nome == "calcGanhoMes":
                self.ganho_mensal = self.calcGanhoMes()
                print(f"Recebendo R${self.ganho_diario:.2f} por dia durante um mês, você receberá R${self.ganho_mensal:.2f}")
        
            elif self.nome == "calcGanhoAno":
                self.num_anos = int(input())
                self.ganho_anual = self.calcGanhoAno()
                self.num_anos = 1
    
            elif self.nome == "calcTempoMeta":
                self.meta = int(input())
                self.tempo_meta = self.calcTempoMeta()
                print(f"Em {self.tempo_meta} ano(s), você atingirá sua meta de R${self.meta:.2f}")

            else:
                self.indice = self.encontrarAtivo()
                if (self.indice == None):
                    print("Ativo não encontrado, digite novamente")
    
                else:
                    self.valor_carteira = self.obterValorCarteira()
                    self.status(self.carteira[self.indice], self.precos_atuais[self.indice])
    
            self.opcoes()
            self.nome = input()