import math

class Circulo:
    def __init__(self, p1, raio):
        self.p1 = p1
        self.raio = raio
        
    def contem(self, ponto):
        dist =  math.sqrt(abs(self.p1.x - ponto.x)** 2 + abs(self.p1.y - ponto.y) ** 2)
        if dist > self.raio:
            return False
        else:
            return True