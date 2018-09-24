import Pedra
import Mao
import Mesa
import random
import JogadorEMinMax
import MCTSPlayer

class Domino:
	pedras = []
	maoA = []
	jogadorA = None
	maoB = []
	jogadorB = None
	mesa = []
	compra = []

	def __init__(self):
		self.pedras = [Pedra.Pedra(0,0), Pedra.Pedra(0,1), Pedra.Pedra(0,2), Pedra.Pedra(0,3), Pedra.Pedra(0,4), Pedra.Pedra(0,5),
		Pedra.Pedra(0,6), Pedra.Pedra(1,1), Pedra.Pedra(1,2), Pedra.Pedra(1,3), Pedra.Pedra(1,4), Pedra.Pedra(1,5), Pedra.Pedra(1,6),
		Pedra.Pedra(2,2), Pedra.Pedra(2,3), Pedra.Pedra(2,4), Pedra.Pedra(2,5), Pedra.Pedra(2,6), Pedra.Pedra(3,3), Pedra.Pedra(3,4),
		Pedra.Pedra(3,5), Pedra.Pedra(3,6), Pedra.Pedra(4,4), Pedra.Pedra(4,5), Pedra.Pedra(4,6), Pedra.Pedra(5,5), Pedra.Pedra(5,6),
		Pedra.Pedra(6,6)]
		random.shuffle(self.pedras)

		self.maoA = Mao.Mao(self.pedras[:7])
		self.jogadorA = JogadorEMinMax.JogadorEMinMax(self.maoA)

		self.maoB = Mao.Mao(self.pedras[7:14])
		self.jogadorB = JogadorEMinMax.JogadorEMinMax(self.maoB) ##TODO apagar
		###self.jogadorB = intB.MonteCarlo(self.maoB)

		self.compra = self.pedras[14:]

		if Mao.mao_most_valorosa(self.maoA, self.maoB):
			turno = self.turno(self.jogadorA, self.jogadorB, 0)
		else:
			turno = self.turno(self.jogadorB, self.jogadorA, 0)
		if turno == 0:
			print('Empate')
		elif turno == 1:
			print('EMinMax ganhou!)
		else:
			print('MonteCarlo ganhou!)

	def turno(self, jogadorA, jogadorB, turnosSemJogo):
		##1 jogadorA ganhou
		##2 jogadorB ganhou
		##0 empate
			if(len(jogadorA.mao) == 0): #ALTERADO
				if(len(jogadorB.mao) == 0): #ALTERADO
					return 0 ##empate
				else:
					return 1 ##A ganhou
			else:
				resp = jogadorA.play_turno(mesa, len(self.compra), len(jogadorB.mao)) #ALTERADO

				if(resp == self.mesa.atual):
					if(len(self.compra) == 0): #ALTERADO
						turnosSemJogo+=1

						if(turnosSemJogo==2): ##Se B tbm não jogou nem comprou na partida anterior, empate
							return 0

					else:
						self.compra = self.jogadorA.buy_pedra(self.compra)
						turnosSemJogo = 0
				else:
					self.mesa.atual = resp
					turnosSemJogo = 0

				proxTurno = self.turno(jogadorB, jogadorA, turnosSemJogo)

				if(proxTurno == 0): ##Empate
					return 0

				if(proxTurno == 1): ##jogadorB ganhou (pois B é "A" em proxTurno)
					return 2

				if(proxTurno == 2): ##jogadorA ganhou (pois A é B em proxTurno)
					return 1
