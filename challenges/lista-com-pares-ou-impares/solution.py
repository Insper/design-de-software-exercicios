def verifica_lista(lista):
    i=0
    
    impar=0
    par=0
    
    while i < len(lista):
        if lista[i] % 2 != 0:
            impar=1
            
        if lista[i] % 2 == 0:
            par=1
            
        i+=1
            
    if impar>=1 and par>=1:
        return 'misturado'
    
    if par>=1 and impar==0:
        return 'par'
    
    if par==0 and impar>=1:
        return 'ímpar'
    return 'misturado'