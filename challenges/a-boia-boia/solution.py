import math

def will_it_float(P, R, r):
    DENSIDADE_AGUA = 997

    volume = 2 * (math.pi**2) * (R*0.01) * (r*0.01)**2
    densidade = P/volume
    
    return densidade <= DENSIDADE_AGUA
