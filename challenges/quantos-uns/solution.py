def quantos_uns(num):
    cont = 0
    num = str(num)
    for i in num:
        if i == '1':
            cont += 1
    return cont