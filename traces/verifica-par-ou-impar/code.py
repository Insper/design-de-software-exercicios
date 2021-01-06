# Função que verifica que retorna 1 se par, -1 se ímpar.
def verifica_par_impar(numero):
    y = (-1)**numero
    return y


# Testando um número par.
x = verifica_par_impar(2)
print(x)

# Testando um número ímpar.
x = verifica_par_impar(1)
print(x)
