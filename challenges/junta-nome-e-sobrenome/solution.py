def junta_nome_sobrenome(nome = [], sobrenome = []):
    lista_aux = []
    for i in range(0,len(nome)):
        lista_aux.append(nome[i]+' '+sobrenome[i])
    return lista_aux