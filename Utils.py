import Pedra
class Utils:

	def jogaveis_max_esquerda(mesa, mao):
		jogaveis = []
		for pedra in mao:
			if pedra.direita == mesa[0].esquerda or pedra.esquerda == mesa[0].esquerda:
				jogaveis.push(pedra)
		return jogaveis

	def jogaveis_max_direita(mesa, mao):
		jogaveis = []
		for pedra in mao:
			if pedra.direita == mesa[-1].direita or pedra.esquerda == mesa[-1].direita:
				jogaveis.push(pedra)
		return jogaveis

	def jogaveis_min_esquerda(self, mesa, mao):
		jogaveis = self.compraveis(mesa, mao) ##ou seja, todos que podem estar na mao de min
		for pedra in jogaveis:
			if pedra.direita != mesa[0].esquerda and pedra.esquerda != mesa[0].esquerda:
				jogaveis.remove(pedra)
		return jogaveis
	def jogaveis_min_direita(mesa, mao):
		jogaveis = self.compraveis(mesa, mao)##ou seja, todos que podem estar na mao de min
		for pedra in jogaveis:
			if pedra.direita != mesa[-1].direita and pedra.esquerda != mesa[-1].direita:
				jogaveis.remove(pedra)
		return jogaveis

	def compraveis(mesa, mao):
		pedras = [Pedra.Pedra(0,0), Pedra.Pedra(0,1), Pedra.Pedra(0,2), Pedra.Pedra(0,3), Pedra.Pedra(0,4), Pedra.Pedra(0,5),
		Pedra.Pedra(0,6), Pedra.Pedra(1,1), Pedra.Pedra(1,2), Pedra.Pedra(1,3), Pedra.Pedra(1,4), Pedra.Pedra(1,5), Pedra.Pedra(1,6),
		Pedra.Pedra(2,2), Pedra.Pedra(2,3), Pedra.Pedra(2,4), Pedra.Pedra(2,5), Pedra.Pedra(2,6), Pedra.Pedra(3,3), Pedra.Pedra(3,4),
		Pedra.Pedra(3,5), Pedra.Pedra(3,6), Pedra.Pedra(4,4), Pedra.Pedra(4,5), Pedra.Pedra(4,6), Pedra.Pedra(5,5), Pedra.Pedra(5,6),
		Pedra.Pedra(6,6)]
		novaMesa = mesa.copy()
		novaMao = mao.copy()
		for pedra in pedras:
			removeu = False
			for p in novaMesa:
				if Pedra.is_igual(pedra, p):
					pedras.remove(pedra)
					novaMesa.remove(p)
					removeu = True
					break
			if not removeu:
				for p in novaMao:
					if Pedra.is_igual(pedra, p):
					pedras.remove(pedra)
					novaMao.remove(p)
					break
		return pedras
	def probabilidade_buy_pedra(self, sizeCompraveis, sizeCompra, sizeAdversarioHand):
		return sizeCompra/(sizeCompraveis*(sizeCompra+sizeAdversarioHand))

	def prob_min_play(mesa, mao, sizeCompra): #ALTERADO
		if len(mesa) == 0:
			return 1

		edgeA = mesa[0].esquerda
		edgeB = mesa[-1].direita
		if edgeA == edgeB:  #caso dos dois cantos da mesa terem o mesmo valor, só existem 7 peças em todo o jogo que poderiam ser jogadas nessa situação(todas que contenham esse valor)
			cont = 7
			for i in range(len(mesa)):
				if mesa[i].direita == edgeA or mesa[i].esquerda == edgeA: #ambos cantos iguais, checando quais peças que poderiam ser jogadas ja estão na mesa
					cont -= 1
			for j in range(len(mao)):
				if mao[i].direita == edgeA or mao[i].esquerda == edgeA:
					cont -= 1
			prob = 1 - cont/sizeCompra #cont/sizeCompra representa a probabilidade de todas as pedras que min poderia jogar estarem na pilha de compra, o cont é o número de peças disponíveis para serem jogadas por min
			return prob
		else: # para o caso de ambos os cantos da mesa serem numeros diferentes se tem 13 peças possiveis no jogo, são 7 peças para um canto e 7 para o outro, com uma repetida, portanto 13
			cont = 13
			for i in range(len(mesa)):
				if (mesa[i].direita == edgeA or mesa[i].esquerda == edgeA) or (mesa[i].direita == edgeB or mesa[i].esquerda == edgeB):
					cont -= 1
			for j in range(len(mao)):
				if (mao[i].direita == edgeA or mao[i].esquerda == edgeA) or (mao[i].direita == edgeB or mao[i].esquerda == edgeB):
					cont -= 1
			prob = 1 - cont/sizeCompra
			return prob
	def prob_min_buy(self, mesa, mao, sizeCompra):
		return 1 - self.prob_min_play(mesa, mao, sizeCompra)
