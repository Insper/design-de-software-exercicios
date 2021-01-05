num = 3
lista = []
while num > 0:
    num = int(input())
    lista.append(num)
for i in range(0,len(lista)):
    print(lista[len(lista)-2-i])