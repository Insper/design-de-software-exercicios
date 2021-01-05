import math

def calcula_distancia_do_projetil(vel, ang, pos):
    return (vel**2/19.6)*(1 + math.sqrt(1 + 19.6/(vel*math.sin(ang))**2))*math.sin(2*ang)