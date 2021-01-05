import math
def distancia_euclidiana(x1,y1,x2,y2):
    a = ((x1 - x2)**2) + ((y1 - y2)**2)
    b = math.sqrt(a)
    return b
