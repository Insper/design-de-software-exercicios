def estritamente_crescente(lista = []):
  lista_aux = []
  maior = 0
  for i in lista:
    if i > maior:
      maior = i
      lista_aux.append(i)
  return lista_aux