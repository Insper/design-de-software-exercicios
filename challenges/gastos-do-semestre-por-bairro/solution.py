def total_do_semestre_por_bairro(gasto_por_bairro):
    totais = {}
    for bairro, totais_por_mes in gasto_por_bairro.items():
        total_bairro = 0
        i = 6
        while i < len(totais_por_mes):
            total_bairro += totais_por_mes[i]
            i += 1
        totais[bairro] = total_bairro
    return totais
