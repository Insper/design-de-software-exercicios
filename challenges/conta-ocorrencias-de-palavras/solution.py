def conta_ocorrencias(palavras):
    ocorrencias = {}
    for p in palavras:
        if p not in ocorrencias:
            ocorrencias[p] = 0
        ocorrencias[p] += 1
    return ocorrencias
