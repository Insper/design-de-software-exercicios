def lista_sufixos(string):
    
    sufixos = []
    cont = 0
    rascunho = []
    while cont < len(string):
        for letra in string[cont:]:
            rascunho.append(letra)
        sufixos.append(''.join(rascunho))
        rascunho.clear()
        cont += 1

    return sufixos[::-1]