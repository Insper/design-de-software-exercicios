def calcula_total_da_nota(prod = [], quant = []):
    preco = 0
    for i in range(0,len(prod)):
        preco += prod[i]*quant[i]
    return preco