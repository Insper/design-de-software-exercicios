# Função que soma dois números.
def soma(x, y):
    z = x + y
    return z


# Lendo os dois números.
a = input('Entre com o primeiro número: ')
b = input('Entre com o segundo número: ')
c = int(a)
d = int(b)

# Somando os dois números.
e = soma(c, d)
print('A soma dos dois números é: {0}'.format(e))
