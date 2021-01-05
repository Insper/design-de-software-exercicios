def calcula_porcentagens(dicionario):
    total=0
    for j in dicionario:
        total+=dicionario[j]
    novo={}
    for i in dicionario: 
        novo[i]=(dicionario[i]*100)/total
    return novo    
    

