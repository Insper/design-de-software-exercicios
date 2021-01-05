lista=[]
i=0

while i==len(lista):
    palavra=str(input('Digite algo: '))
    if palavra=='fim':
        break
    else:
        lista.append(palavra)
    i+=1
i=0
while i<len(lista):
    if lista[i][0]=='a':
        print(lista[i])
    i+=1