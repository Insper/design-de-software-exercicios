def tamanho_minimo(str1,n):
    word_len = []
    txt = str1.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	

