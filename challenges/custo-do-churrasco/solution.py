with open('churras.txt','r') as churras:
    linhas = churras.readlines()

total = 0
for linha in linhas:
    dados = linha.split(',')
    total += int(dados[1]) * float(dados[2])
    

print(total)
