def eh_primo(num):
    if num == 2:
      return True
    elif num == 1 or num == 0:
      return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def verifica_primos(lista=[]):
  dic = {}
  for i in lista:
    if i >= 0:
    	dic[i] = eh_primo(i)
    else:
        dic[i] = False
  return dic