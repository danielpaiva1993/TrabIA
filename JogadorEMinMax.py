import random
import Pedra
import Mao
import Mesa
import Utils as u
class JogadorEMinMax:
	
	mao = [] 

	def __init__(self, mao):
		self.mao = mao

	def play_turno(self, mesa, sizeCompra, sizeAdversarioHand):
		jogaveisEsquerda = u.jogaveis_max_esquerda(mesa.atual)
		jogaveisDireita = u.jogaveis_max_direita(mesa.atual)
		if len(jogaveisEsquerda) == 0 and len(jogaveisDireita) == 0:
			return mesa.atual
		else:
			valor = -28
			novaMesa = mesa.atual
			novaMao = self.mao
			for pedra in jogaveisEsquerda:
				mesaTemp = Mesa.simula_insert_esquerda(mesa.atual.copy(), pedra)
				maoTemp = self.mao.pedras.copy()
				maoTemp.remove(pedra)
				novoValor = self.prob_min(mesaTemp, maoTemp, sizeCompra, sizeAdversarioHand, 0)
				se novoValor > valor:
					valor = novoValor
					novaMesa = mesaTemp
					novaMao = maoTemp
			for pedra in jogaveisDireita:
				mesaTemp = Mesa.simula_insert_direita(mesa.atual.copy(), pedra)
				maoTemp = self.mao.pedras.copy()
				maoTemp.remove(pedra)
				novoValor = self.prob_min(mesaTemp, maoTemp, sizeCompra, sizeAdversarioHand, 0)
				se novoValor > valor:
					valor = novoValor
					novaMesa = mesaTemp
					novaMao = maoTemp
			self.mao = novaMao
			return novaMesa
	
	def buy_pedra(self, compra):
		purchasedPedra = random.choice(compra)
		self.mao.append(purchasedPedra)
		compra.remove(purchasedPedra)
		return compra

	def max(self, mesa, mao, sizeCompra, sizeAdversarioHand, turnosSemJogo):
		if(len(mao) == 0): ##se mão de min tbm for 0, vai dar empate, se não max vai ganhar pois a subtração dará valor positivo
			return sizeAdversarioHand - len(mao)
		jogaveisEsquerda = u.jogaveis_max_esquerda(mesa, mao)
		jogaveisDireita = u.jogaveis_max_direita(mesa, mao)
		valor = -28
		for pedra in jogaveisEsquerda:
			mesaTemp = Mesa.simula_insert_esquerda(mesa.copy(), pedra)
			maoTemp = mao.copy()
			maoTemp.remove(pedra)
			novoValor = self.prob_min(mesaTemp, maoTemp, sizeCompra, sizeAdversarioHand, 0)
			se novoValor > valor:
				valor = novoValor
		for pedra in jogaveisDireita:
			mesaTemp = Mesa.simula_insert_direita(mesa.atual.copy(), pedra)
			maoTemp = mao.copy()
			maoTemp.remove(pedra)
			novoValor = self.prob_min(mesaTemp, maoTemp, sizeCompra, sizeAdversarioHand, 0)
			se novoValor > valor:
				valor = novoValor
		return valor
	def min(self, mesa, mao, sizeCompra, sizeAdversarioHand, turnosSemJogo):
		if(sizeAdversarioHand == 0):##se mão de max tbm for 0, vai dar empate, se não vai dar um valor negativo pois adversario ganhou
			return sizeAdversarioHand - len(mao)
		valor = 28
		jogaveisEsquerda = u.jogaveis_min_esquerda(mesa, mao)
		jogaveisDireita = u.jogaveis_min_esquerda(mesa, mao)
		for pedra in jogaveisEsquerda:
			mesaTemp = Mesa.simula_insert_esquerda(mesa.copy(), pedra)
			novoValor = self.prob_min(mesaTemp, mao, sizeCompra, sizeAdversarioHand-1, 0)
			se novoValor < valor:
				valor = novoValor
		for pedra in jogaveisDireita:
			mesaTemp = Mesa.simula_insert_direita(mesa.atual.copy(), pedra)
			novoValor = self.prob_min(mesaTemp, mao, sizeCompra, sizeAdversarioHand-1, 0)
			se novoValor < valor:
				valor = novoValor
		return valor

	def prob_max(self, mesa, mao, sizeCompra, sizeAdversarioHand):
		prob = 0
		if len(u.jogaveis_max_esquerda(mesa, mao)) == 0 and len(u.jogaveis_max_direita(mesa, mao)) == 0:
			if sizeCompra == 0: #se max não pode comprar nem jogar, pula a vez
				turnosSemJogo += 1
				if(turnosSemJogo==2): ##ninguem consegue jogar
					prob= sizeAdversarioHand - len(mao) 
				else:##max não comprou, então é um turno sem jogo
					prob = self.prob_min(mesa, mao, sizeCompra, sizeAdversarioHand, turnosSemJogo)
			else: #se max não pode jogar, mas pode comprar, vamos tentar calcular a sorte
				for pedra in u.compraveis(mesa, mao):
					maoTemp = mao.copy()
					maoTemp.append(pedra)
					prob = prob + u.probabilidade_buy_pedra(len(compraveis), sizeCompra, sizeAdversarioHand)*self.prob_min(mesa, maoTemp, sizeCompra-1, sizeAdversarioHand, 0) 
		else: #se max pode jogar, ve qual é mlehor jogada
			prob = self.max(mesa, mao, sizeCompra, sizeAdversarioHand, 0)
		return prob

	def prob_min(self, mesa, mao, sizeCompra, sizeAdversarioHand, turnosSemJogo):
		prob = 0
		if len(u.jogaveis_min_esquerda(mesa, mao)) == 0 and len(u.jogaveis_min_direita(mesa,mao)) == 0:
			if sizeCompra == 0: ## se min não pode jogar nem comprar, pula a vez
				turnosSemJogo += 1
				if(turnosSemJogo==2): ##ninguem consegue jogar ou comprar
					prob = sizeAdversarioHand - len(mao)
				else: ##min não comprou, então é um turno sem jogo
					prob = self.prob_max(mesa, mao, sizeCompra, sizeAdversarioHand, turnosSemJogo)
			else: ##se min não pode jogar, mas pode comprar vamos continuar o jogo
				 prob = self.prob_max(mesa, mao, sizeCompra-1, sizeAdversarioHand+1, 0) 
		else: ##se é possivel min ter pedra para jogar, vamos tentar calcular a sorte de ele ter ou não
			prob =  u.prob_min_play(mesa, mao, sizeCompra, sizeAdversarioHand) * self.min(mesa, mao, sizeCompra, sizeAdversarioHand, 0) +
				u.prob_min_buy(mesa, mao, sizeCompra, sizeAdversarioHand) * self.prob_max(mesa, mao, sizeCompra-1, sizeAdversarioHand+1, 0)

		return prob
