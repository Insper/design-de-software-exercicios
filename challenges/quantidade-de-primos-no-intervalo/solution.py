def eh_primo(num):
    if num == 2:
      return True
    elif num == 1 or num == 0:
      return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def primos_entre(a,b):
    cont = 0
    for i in range(a,b+1):
        if eh_primo(i) == True:
            cont += 1
    return cont