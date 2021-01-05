def soma_impares(lista = []):
    sum = 0
    for i in lista:
        if i%2 == 1:
            sum += i
    return sum