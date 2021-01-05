def eh_primo(num):
    if num == 2:
      return True
    elif num == 1 or num == 0:
      return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def lista_primos(num, lista = []):
    k = 0
    for i in range(0,num):
        conf = False
        j = k
        while conf == False:
            j += 1
            conf = eh_primo(j)
        k = j
        lista.append(j)
    return lista