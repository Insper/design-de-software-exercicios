def pacotes_correio(lista):
    tamanho=lista[0][2]
    total=lista[0][0]
    anterior=0
    atual=0
    for l in lista:
        atual=l[1]
        tamanho_atual=l[2]
        if atual != anterior+1:
            return "ordem errada"
        if tamanho_atual != tamanho:
            return "tamanho errado"
        anterior = atual
    if atual != total:
        return "pacote perdido"
    else:
        return "tudo certo"
    