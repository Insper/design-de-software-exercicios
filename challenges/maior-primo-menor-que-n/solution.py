def eh_primo(num):
    if num == 2:
      return 1
    for i in range(2,num):
        if num%i == 0:
            return 0
    return 1

maior = 0      
        
def maior_primo_menor_que(num):
    if num <= 1:
        return -1
    else:
        for i in range(1,num+1):
            if eh_primo(i) == 1:
                maior = i
    return maior