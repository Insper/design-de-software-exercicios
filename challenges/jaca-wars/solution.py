import math

v = float(input("Digite a velocidade da sua jaca! "))
o = float(input("Qual o seu ângulo de arremesso de jaca! "))
o = math.sin(2 * math.radians(o))
g = 9.8

d = (v ** 2 / g) * o

if d >= 98 and d <= 102:
    print('Acertou!')
elif d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe')
    