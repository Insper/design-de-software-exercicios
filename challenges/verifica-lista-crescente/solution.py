def eh_crescente(lista=[]):
    cont = 0
    for i in range(0,len(lista)-1):
        if lista[i+1] > lista[i]:
            cont += 1
    if cont < len(lista)-1:
        return False
    return True