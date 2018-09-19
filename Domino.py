import Pedra
import Mao
import random
import JogadorEMinMax
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
		###self.jogadorB = intB.MonteCarlo(self.maoB)

		self.compra = self.pedras[14:]
		'''
		TODO comparar as duas mãos e ver quem joga
		self.turno(self.jogadorQueComeca, self.outroJogador)
		'''
	
	def turno(self, jogadorA, jogadorB, turnosSemJogo):
		##1 jogadorA ganhou
		##2 jogadorB ganhou
		##0 empate
			if(jogadorA.mao.length == 0):
				if(jogadorB.mao.length == 0):
					return 0 ##empate
				else:
					return 1 ##A ganhou
			else:
				resp = jogadorA.play_turno(mesa, self.compra.length, jogadorB.mao.length)

				if(resp == self.mesa):
					if(self.compra.length == 0):
						turnosSemJogo+=1

						if(turnosSemJogo==2): ##Se B tbm não jogou nem comprou na partida anterior, empate
							return 0
						
					else:
						self.compra = self.jogadorA.buy_pedra(self.compra)
						turnosSemJogo = 0
				else:
					self.mesa = 
					turnosSemJogo = 0

				proxTurno = self.turno(jogadorB, jogadorA, turnosSemJogo)
				
				if(proxTurno == 0): ##Empate
					return 0

				if(proxTurno == 1): ##jogadorB ganhou (pois B é "A" em proxTurno)
					return 2
				
				if(proxTurno == 2): ##jogadorA ganhou (pois A é B em proxTurno)
					return 1
