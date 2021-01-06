invalido = True

while invalido:
    valor = int(input('Digite um inteiro par: '))
    if valor % 2 == 0:
        invalido = False
    else:
        print('Este número não é par, tente novamente.')

print('Você digitou: {0}'.format(valor))
