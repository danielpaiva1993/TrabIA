import json
import Pedra

#Monte Carlo Tree Search Player
class MCTSPlayer:

	game_pedras

	mao = None
	mesa = None
	monte = None
	edgeA = None
	edgeB = None
	opponent_hand_amount = None
	# pedra_most_valorosa = None


	def __init__(self,mao,opponent_hand_amount):
		self.mao = mao
		self.opponent_hand_amount = opponent_hand_amount
		self.game_pedras = [Pedra.Pedra(0,0), Pedra.Pedra(0,1), Pedra.Pedra(0,2), Pedra.Pedra(0,3), Pedra.Pedra(0,4), Pedra.Pedra(0,5),
		Pedra.Pedra(0,6), Pedra.Pedra(1,1), Pedra.Pedra(1,2), Pedra.Pedra(1,3), Pedra.Pedra(1,4), Pedra.Pedra(1,5), Pedra.Pedra(1,6),
		Pedra.Pedra(2,2), Pedra.Pedra(2,3), Pedra.Pedra(2,4), Pedra.Pedra(2,5), Pedra.Pedra(2,6), Pedra.Pedra(3,3), Pedra.Pedra(3,4),
		Pedra.Pedra(3,5), Pedra.Pedra(3,6), Pedra.Pedra(4,4), Pedra.Pedra(4,5), Pedra.Pedra(4,6), Pedra.Pedra(5,5), Pedra.Pedra(5,6),
		Pedra.Pedra(6,6)]

		# self.pedra_most_valorosa = mao.pedra_most_valorosa
		return

	def __str__(self):
		response = "\nThe current Hand for the MCTSPlayer is \n"
		for i in self.mao.pedras:
			response += str(i) + " "
		response += "\n"
		return response

	def play_turno(self,mesa,monte,opponent_hand_amount):
		self.mesa = mesa
		self.monte = monte
		self.edgeA = mesa[0] 
		self.edgeB = mesa[len(mesa)]
		self.opponent_hand_amount = opponent_hand_amount
		self.select()
		return True 

	def select():
		# Inicia a árvore a partir do estado de jogo inicial, usando como root o nó da primeira jogada possivel
		# Loop sobre as pedras na mão 
		for pedra in self.mao.pedras:
			if(pedra.ladoA == self.edgeA.edge or pedra.ladoB == self.edgeA.edge): # Checa se é possivel fazer a jogada
				if(pedra.ladoA == self.edgeA.edge): 
					pedra.set_edge(pedra.ladoB) # Seta qual a extremidade da pedra que ficará exposta 
					mesa.insert(0,pedra) # Insere na mesa a pedra na posiçao referente à jogada
					self.mao.pedras.remove(pedra) # remove a Pedra jogada da mão do jogador
					node = Node(pedra,self.mesa,self.mao,self.game_pedras,self.opponent_hand_amount) # Cria o Node ROOT do MCTS





# Node 
class Node:

	# Class node da MCTS

	# Parent será usado para definir se o Nó tem um Pai, e se ele é o opponent ou eu

	game_pedras = None
	mao_state = None
	mesa_state = None
	opponent_hand_plus_mount = []
	opponent_hand_amount = None
	parent = None
	wins = 0
	deaths = 0
	empates = 0
	children = []
	edgeA = None
	edgeB = None

	# "construtor" da classe nó
	def __ini__(self,mesa_state,mao_state,game_pedras,opponent_hand_amount,parent=None,won=None):

		# Checa se venceu, empatou ou perdeu
		if(self.is_vencedor(mao_state)):
			if(won == False):
				self.wins += 1
			else:
				self.empates += 1

		if(!self.is_vencedor(mao_state)):
			if(won == True):
				self.deaths += 1

		else:

			# Caso nao esteja no final ( não seja folha )

			self.children = [] # Inicia a lista de filhos para aquele nó
			self.edgeA = mesa_state[0] # define as pontas da mesa
			self.edgeB = mesa_state[len(mesa_state)] # define as pontas da mesa
			self.mesa_state = mesa_state # atribui mesa_state a self.mesa_state
			self.mao_state = mao_state # atribui mao_state a self.mao_state

			if(parent != "opponent"): # Se o parent foi jogado por mim
				self.opponent_hand_amount = opponent_hand_amount # atribui opponent_hand_amount em self.opponent_hand_amount
				self.game_pedras = game_pedras # atribui game_pedras a self.game_pedras
				self.parent = parent # atribui parent a self.parent
				self.opponent_hand_plus_mount = self.get_resto() # atribui o conteudo de opponent hand plus mount da função get_resto()
				self.expand() # expand o nó baseado no parent "me"

			else:
				buy = True
				for pedra in self.mao_state.pedras:
					if(pedra.ladoA == self.edgeA.edge or pedra.ladoB == self.edgeA.edge):
						if(pedra.ladoA == self.edgeA.edge):
							buy = False
							pedra.set_edge(pedra.ladoB)
							self.mesa_state.insert(0,pedra)
							self.mao.pedras.remove(pedra)
							node = Node(pedra,self.mesa,self.mao,self.game_pedras,opponent_hand_amount,parent="me")
							self.add_children(node)

						if(pedra.ladoB == self.edgeA.edge):
							if(!pedra.is_simetrico()):
								buy = False
								pedra.set_edge(pedra.ladoA)
								mesa_state.insert(0,pedra)
								mao_state.pedras.remove(pedra)
								node = Node(pedra,mesa_state,mao_state,game_pedras,opponent_hand_amount,parent="me")
								self.add_children(node)
				self.count_wins()					
		return

	def add_children(self,child_state):
		self.children.append(child_state)
		return

	def get_resto(self):
		for p in self.mao_state.pedras:
			self.game_pedras.remove(p)
		return game_pedras

	def expand(self):
		max_tests = 10 # expande até um maximo de 10 nós
		for p in self.opponent_hand_plus_mount: # loop sobre as pedras no opponent hand plus mount
			max_tests += 1 # incrementa 1 em max_tests
			if(max_tests < 10): # mantem o limite de 10 nós
				if(p.ladoA == self.edgeA.edge or p.ladoB == self.edgeA.edge): # checa se é possivel fazer a jogada com aquela pedra
					self.mesa_state.insert(0,p) # insere a pedra na mesa
					opponent_hand_amount -= 1 # retira 1 do valor mão do oponente
					game_pedras.remove(p) # remove a pedra do game_pedras
					if(opponent_hand_amount == 0): # se a mão do oponente é = 0, inicia o próximo nó com a tag Won = True
						child = Node(self.mesa_state,self.mao_state,self.game_pedras,self.opponent_hand_amount,parent="opponent",won=True)
						self.add_children(child)
					else: # else inicia sem a tag Won
						child = Node(self.mesa_state,self.mao_state,self.game_pedras,self.opponent_hand_amount,parent="opponent")
						self.add_children(child)

					self.count_wins() # Conta os wins, deaths, draws

	# Checa se o length da mão é = 0 || vencedor ou não
	def is_vencedor(self,mao):
		if(len(mao)==0):
			return True
		else:
			return False

	# Conta os valores de wins deaths e empates
	def count_wins(self):
		for nodes in self.children:
			wins += nodes.wins
			deaths += nodes.deaths
			empates += nodes.empates