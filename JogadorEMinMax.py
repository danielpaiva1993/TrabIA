import random
import Pedra
import Mao
import Utils as u
class JogadorEMinMax:
	
	mao = [] 

	def __init__(self, mao):
		self.mao = mao

	def play_turno(self, mesa, sizeCompra, sizeAdversarioHand):
		'''
			jogaveisEsquerda = u.jogaveis_max_esquerda(mesa)
			jogaveisDireita = u.jogaveis_max_direita(mesa)
			Se jogaveisEsquerda.lenght == 0 and jogaveisDireita.lenght == 0:
				return mesa
			Se não:
				bestPedra = null
				valor = -999999
				Para cada pedra em jogaveisEsquerda:
					novoValor = self.prob_min(self, u.put_in_mesa(mesa, pedra, esquerda), mao sem pedra, sizeCompra, sizeAdversarioHand, 0)
					se novoValor > valor:
						valor = novoValor
						bestPedra = pedra
				Para cada pedra em jogaveisDireita:
					novoValor = self.prob_min(self, u.put_in_mesa(mesa, pedra, direita), mao sem pedra, sizeCompra, sizeAdversarioHand, 0)
					se novoValor > valor:
						valor = novoValor
						bestPedra = pedra
				novaMesa = u.putInMesa(mesa, bestPedra)
				return novaMesa
		'''
		return 

	
	def buy_pedra(self, compra):
		purchasedPedra = random.choice(compra)
		self.compra.append(purchasedPedra)
		return compra.remove(purchasedPedra)

	def max(self, mesa, mao, sizeCompra, sizeAdversarioHand, turnosSemJogo):
		'''
			if(mao.length == 0):
				return sizeAdversarioHand - mao.length
				##se mão de min tbm for 0, vai dar empate, se não max vai ganhar pois a subtração dará valor positivo
			
			valor = -9999999999
			jogaveisEsquerda = u.jogaveis_max_esquerda(mesa)
			jogaveisDireita = u.jogaveis_max_direita(mesa)
			Para cada pedra em jogaveisEsquerda:
				novoValor = self.min(u.put_in_mesa(mesa, pedra, esquerda), mao sem pedra, sizeCompra, sizeAdversarioHand, turnosSemJogo)
				se novoValor > valor:
					valor = novoValor
			Para cada pedra em jogaveisDireita:
				novoValor = self.min(u.put_in_mesa(mesa, pedra, direita), mao sem pedra, sizeCompra, sizeAdversarioHand, turnosSemJogo)
				se novoValor > valor:
					valor = novoValor
			return valor
		'''
		return ##int

	def min(self, mesa, mao, sizeCompra, sizeAdversarioHand, turnosSemJogo):
		'''
			if(sizeAdversarioHand == 0):
				return sizeAdversarioHand - mao.length
				##se mão de max tbm for 0, vai dar empate, se não vai dar um valor negativo pois adversario ganhou
			
			valor = 9999999999
			jogaveisEsquerda = self.jogaveis_min_esquerda(mesa)
			jogaveisDireita = self.jogaveis_min_esquerda(mesa)
			Para cada pedra em jogaveisEsquerda:
				novoValor = self.prob_max(u.put_in_mesa(mesa, pedra, esquerda), mao, sizeCompra, sizeAdversarioHand-1)
				se novoValor < valor:
					valor = novoValor
			Para cada pedra em jogaveisDireita:
				novoValor = self.prob_max(u.put_in_mesa(mesa, pedra, direita), mao, sizeCompra, sizeAdversarioHand-1)
				se novoValor < valor:
					valor = novoValor
			return valor
		'''
		return ##int


	def worst_compra_max(self, mesa, mao, sizeCompra, sizeAdversarioHand):
		'''
			valor = 999999
			worstPedra = None
			compraveis = u.compraveis(mesa, mao)
			para cada pedra compraveis:
				jogaveisEsquerda = u.jogaveis_max_esquerda(mesa, mao com pedra)
				jogaveisDireita = u.jogaveis_max_direita(mesa, mao com pedra)
				if(jogaveisEsquerda.length == 0 and jogaveisDireita.length==0)
					novoValor = self.min(mesa, mao com pedra, sizeCompra-1, sizeAdversarioHand)
					if(novoValor<valor):
						valor = novoValor
						worstPedra = pedra
			return worstPedra
		'''
		return None

	def prob_max(self, mesa, mao, sizeCompra, sizeAdversarioHand):
		''' 
			if u.jogaveis_max_esquerda().length == 0:
				if sizeCompra == 0:
					turnosSemJogo += 1
					if(turnosSemJogo==2):
						return sizeAdversarioHand - mao.length ##ninguem consegue jogar
					return self.prob_min(mesa, mao, sizeCompra, sizeAdversarioHand, turnosSemJogo)##max não comprou, então é um turno sem jogo
				else: 
					##se da pra comprar, considera pior caso de compra
					novaMao = self.worst_compra_max(mesa, mao, sizeCompra, sizeAdversarioHand)
					return self.max(mesa, novaMao, sizeCompra-1, sizeAdversarioHand, 0) 
			else:
				return self.max(mesa, mao, sizeCompra, sizeAdversarioHand, 0)
				
		'''
		return ##int

	def prob_min(self, mesa, mao, sizeCompra, sizeAdversarioHand, turnosSemJogo):
		''' if self.jogaveis_min_esquerda().length == 0:
				if sizeCompra == 0:
					turnosSemJogo += 1
					if(turnosSemJogo==2):
						return sizeAdversarioHand - mao.length
					return self.prob_max(mesa, mao, sizeCompra, sizeAdversarioHand, turnosSemJogo)##min não comprou, então é um turno sem jogo
				else:
					return self.prob_max(mesa, mao, sizeCompra-1, sizeAdversarioHand+1, 0) 
					##min vai comprar mas nunca vai vir pedra "boa" pois todas estão na mesa ou com max
					##então chama logo max ao inves de chamar min e testar isso dentro do metodo
					##melhor testar aqui pois so aqui existe o controle se min comprou ou passou a vez
			else:
				return
						(
							probabilidade de min ter alguma pedra pra jogar * self.min(mesa, mao, sizeCompra, sizeAdversarioHand, 0) +
							probabilidade dele comprar uma pedra que de para jogar * self.min(mesa, mao, sizeCompra-1sizeAdversarioHand+1, 0) +
							probabilidade dele comprar uma pedra ruim * self.prob_max(mesa, mao, sizeCompra-1sizeAdversarioHand+1, 0)
						) ##considera que ele sempre tem ou compra a melhor pedra possivel, então calcula o pior caso
			
		'''
		return ##int