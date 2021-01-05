def inverte_dicionario(dic = {}):
    dic_novo = {}
    for i in dic.values():
        if i not in dic_novo:
            lista = []
            for j in dic:
                if dic[j] == i:
                    lista.append(j)
            dic_novo[i] = lista
    lista = []
    for i in dic_novo:
      lista.append(i)
    lista.sort()
    dic_mais_novo = {}
    for i in lista:
      dic_mais_novo[i] = dic_novo[i]
    return dic_mais_novo