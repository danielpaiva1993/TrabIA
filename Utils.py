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
	def probabilidade_buy(pedra, mesa, sizeCompra, sizeAdversarioHand)):
		##return a probabilidade de comprar determinada pedra
		return ##int
