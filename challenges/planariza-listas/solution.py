def junta_listas(lista):
    i=0    
    lista2 = []
    while i < len(lista):
        j = 0
        while j < len(lista[i]):
            lista2.append(lista[i][j])
            j +=1
        i +=1
    return lista2
        