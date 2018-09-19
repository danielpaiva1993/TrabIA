class Pedra:
	esquerda = 0
	direita = 0

	def __init__(self,esquerda=0,direita=0):
		self.esquerda = esquerda
		self.direita = direita
		return

	def __str__(self):
		response = "||"+ str(self.esquerda) + "|"+ str(self.direita) + "||"
		return response

	def get_soma(self):
		soma = self.esquerda + self.direita
		return soma

	def is_simetrico(self):
		simetrico = (self.esquerda == self.direita)
		return simetrico

	def is_carrilhao(self):
		if self.is_simetrico() and self.esquerda == 6:
			return True
		return False

	def compara(pedraA, pedraB): ###TODO metodo de comparação
		return pedraA

	def invertePedra(self):
		aux = self.esquerda
		self.esquerda = self.direita
		self.direita = aux
		return True
