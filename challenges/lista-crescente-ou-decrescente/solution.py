def classifica_lista(numeros):
    if len(numeros) < 2:
        return 'nenhum'
    anterior = numeros[0]
    i = 1
    crescente = True
    decrescente = True
    while i < len(numeros):
        if numeros[i] < anterior:
            crescente = False
        if numeros[i] > anterior:
            decrescente = False
        anterior = numeros[i]
        i += 1
    if crescente:
        return 'crescente'
    if decrescente:
        return 'decrescente'
    return 'nenhum'
