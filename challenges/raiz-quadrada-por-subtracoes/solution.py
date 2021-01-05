def raiz_quadrada(valor):
    counter=0
    while valor>0:
        valor = valor - (2*counter+1)
        counter += 1
    return counter