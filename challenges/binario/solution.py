
def decimal_para_binario(value):
    if value < 0:
        return 'Negativo'
    elif value == 0: 
        return ('0')
    else:
         return str(decimal_para_binario(value//2) + str(value%2))
