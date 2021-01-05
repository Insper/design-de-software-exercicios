def calcula_media(lista):
    lista2=[]
    i=0
    while i < len(lista):
        lista2 += lista[i].values()
        i+=1
        
    p=sum(lista2)
    d=p/len(lista2)
    
    return d
        