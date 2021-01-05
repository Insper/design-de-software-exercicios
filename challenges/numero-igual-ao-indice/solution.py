def numero_no_indice(lista = []):
    lista_aux = []
    for i in range(0,len(lista)):
        if i == lista[i]:
            lista_aux.append(i)
    return lista_aux