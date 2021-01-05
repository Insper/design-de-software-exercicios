def monta_dicionario(lista1 = [], lista2 = []):
    dic = {}
    for i in range(len(lista1)):
        dic[lista1[i]] = lista2[i]
    return dic