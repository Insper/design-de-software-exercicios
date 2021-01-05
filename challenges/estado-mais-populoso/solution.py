def mais_populoso(brasil):
    maior_populacao = 0
    estado_mais_populoso = ''
    for estado, cidades in brasil.items():
        populacao_total = 0
        for populacao in cidades.values():
            populacao_total += populacao
        if populacao_total > maior_populacao:
            estado_mais_populoso = estado
            maior_populacao = populacao_total
    return estado_mais_populoso
