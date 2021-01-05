def filtra_positivos(lista = []):
    lista_aux = []
    for i in lista:
        if i>0:
            lista_aux.append(i)
    return lista_aux