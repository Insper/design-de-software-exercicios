num = 0
maior = 0
for i in range(1,1000):
    cont = 1
    aux = i
    while aux != 1:
      if aux%2 == 0:
        aux = aux*0.5
      else:
        aux = aux*3 + 1
      cont += 1
    if cont > maior:
      maior = cont
      num = i

print(num)