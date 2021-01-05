lista = []

def acha_bigramas(palavra):
  for i in range(1,len(palavra)):
    if palavra[i-1]+palavra[i] not in lista:
     lista.append(palavra[i-1]+palavra[i])
  return lista

def conta_bigramas(palavra):
    acha_bigramas(palavra)
    dic = {}
    for i in lista:
        dic[i] = palavra.count(i)
    return dic