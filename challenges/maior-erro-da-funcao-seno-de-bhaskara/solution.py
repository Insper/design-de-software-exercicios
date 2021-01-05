import math

def bhaskara(x):
    return (4*x*(180-x)/(40500-x*(180-x)))

maior_erro = 0
angulo = 0
for n in range(91):
    resultado_b = bhaskara(n)
    resultado_m = math.sin(math.radians(n))
    dif = abs(resultado_b - resultado_m)
    if dif > maior_erro:
        maior_erro = dif
        angulo = n
print(angulo)