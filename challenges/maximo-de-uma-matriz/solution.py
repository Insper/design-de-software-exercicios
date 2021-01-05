def encontra_maximo(lista = []):
  maior = 0
  for i in range(0,3):
    for j in range(0,3):
      if abs(lista[i][j]) > maior:
        maior = abs(lista[i][j])
  return maior