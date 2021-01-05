with open('macacos-me-mordam.txt') as arq:
    ocorrencias = arq.read().lower().count('banana')
print(ocorrencias)