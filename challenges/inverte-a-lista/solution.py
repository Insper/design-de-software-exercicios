def inverte_lista(lista=[]):
    lista_aux = []
    for i in range(0,len(lista)):
        lista_aux.append(lista[len(lista)-1-i])
    return lista_aux