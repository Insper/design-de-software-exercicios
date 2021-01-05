def acha_bigramas(palavra):
  lista = []
  for i in range(1,len(palavra)):
    if palavra[i-1]+palavra[i] not in lista:
     lista.append(palavra[i-1]+palavra[i])
  return lista