def traduz(lista_ing, eng2port):
    lista_tradução=[]
    for palavra in lista_ing:
        palavra_pesquisada = eng2port[palavra]
        lista_tradução.append(palavra_pesquisada)
    
    return lista_tradução