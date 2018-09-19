import Pedra

class Mesa:
    atual = []

    def insert_esquerda(self,p):
        if p.direita != self.atual[0].esquerda:
            p.invertePedra()
        self.atual.insert(0, p)
        return

    def insert_direita(self,p):
        if p.esquerda != self.atual[-1].direita:
            p.invertePedra()
        self.atual.append(p)
        return

    def simula_insert_esquerda(mesa, pedra):
        if p.direita != mesa[0].esquerda:
            p.invertePedra()
        mesa.insert(0, p)
        return mesa

    def simula_insert_direita(mesa, pedra):
        if p.esquerda != mesa[-1].direita:
            p.invertePedra()
        mesa.append(p)
        return mesa
