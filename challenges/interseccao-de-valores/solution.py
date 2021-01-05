def interseccao_valores(dic1 = {}, dic2 = {}):
    lista1 = []
    lista2 = []
    lista = []
    for i in dic1:
        lista1.append(dic1[i])
    for i in dic2:
        lista2.append(dic2[i])
    for i in lista1:
        if i in lista2:
            lista.append(i)
    return lista