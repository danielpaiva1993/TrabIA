import Pedra
class Mao:
	pedras = [7]
	pedra_most_valorosa = None
	def __init__(self, pedras):
		self.pedras = pedras
		self.pedra_most_valorosa = self.most_valorosa()

	def __str__(self):
		response = ""
		for x in self.pedras:
			response += str(x) + "  "
		return response

	def most_valorosa(self):
		response = self.pedras[0]
		for x in self.pedras:
			if x.is_carrilhao():
				response = x
				return response
			elif x.is_simetrico() and (not response.is_simetrico()):
				response = x
			elif (x.is_simetrico() and response.is_simetrico()) or ((not x.is_simetrico()) and (not response.is_simetrico())):
				if x.get_soma() > response.get_soma():
					response = x
		return response
	def mao_most_valorosa(maoA, maoB):## retorna True se maoA é quem começa
		fakeMao = Mao.Mao([maoA.most_valorosa(), maoB.most_valorosa()])
		if Pedra.is_igual(fakeMao.most_valorosa(),maoA,most_valorosa()):
			return True
		return False
