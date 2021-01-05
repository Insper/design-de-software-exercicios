def separa_trios(lista = []):
    lista_trios = []
    for i in range(len(lista)):
      if i%3 == 0:
        lista_aux = []
        lista_aux.append(lista[i])
        if i > len(lista) - 2:
          lista_trios.append(lista_aux)
      elif i%3 == 1:
        lista_aux.append(lista[i])
        if i > len(lista) - 2:
          lista_trios.append(lista_aux)
      else:
        lista_aux.append(lista[i])
        lista_trios.append(lista_aux)
    return lista_trios