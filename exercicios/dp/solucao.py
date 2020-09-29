def notas_dp(list_of_dicts):
    dps = []
    for d in list_of_dicts:
        n1 = d["PI"]
        n2 = d['PF']
        media = float((n1 + n2)/2)
        if media < 5:
            dps.append(d['matricula'])

    return dps
