import math

def calcula_norma(myList = []):
    modulo = 0
    for i in myList:
        modulo = modulo + i**2
    return math.sqrt(modulo)