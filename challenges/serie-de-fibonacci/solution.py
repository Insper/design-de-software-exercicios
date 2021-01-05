def fibonacci(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

def calcula_fibonacci(num):
    lista = []
    for i in range(1,num+1):
        lista.append(fibonacci(i))
    return lista