def conta_letras(texto):
    letras = {}
    for c in texto:
        if c not in letras:
            letras[c] = 0
        letras[c] += 1
    return letras
