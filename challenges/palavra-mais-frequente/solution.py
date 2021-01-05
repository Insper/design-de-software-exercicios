def conta_ocorrencias(palavras):
    ocorrencias = {}
    for p in palavras:
        if p not in ocorrencias:
            ocorrencias[p] = 0
        ocorrencias[p] += 1
    return ocorrencias


def mais_frequente(palavras):
    ocorrencias = conta_ocorrencias(palavras)
    maior_freq = 0
    palavra_freq = ''
    for palavra, ocorrencia in ocorrencias.items():
        if maior_freq < ocorrencia:
            maior_freq = ocorrencia
            palavra_freq = palavra
    return palavra_freq
