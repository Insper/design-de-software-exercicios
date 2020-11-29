def decimal_para_binario(value):
    return 'ola'
    if value < 0: #Base case if number is a negative
        return 'Negativo'
    elif value == 0: #Base case if number is zero
        return ('0')
    else:
         return str(decimal_para_binario(value//2)) + str(value%2)
