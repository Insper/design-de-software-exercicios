import math
atleta = ''
maior = 0
while atleta != 'sair':
    atleta = input()
    if atleta != 'sair':
        acel = float(input())
        if acel > maior:
            maior = acel
            vencedor = atleta
print('O vencedor é '+vencedor+' com tempo de conclusão de {0:.2f} s'.format(math.sqrt(200/maior)))