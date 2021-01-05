class Foguete:

    def __init__(self, velocidade):
        self.velocidade = velocidade
        self.distancia = 0

    def atualizar(self, tempo):
        self.distancia += self.velocidade * (tempo / 3600)
        return self.distancia

# EXEMPLO
# foguete = Foguete(10000)
# print(foguete.atualizar(9))
# print(foguete.atualizar(18))
