def agrupa_por_idade(nomes_idades):
    por_faixa = {
        'criança': [],
        'adolescente': [],
        'adulto': [],
        'idoso': [],
    }
    for nome, idade in nomes_idades.items():
        if idade <= 11:
            por_faixa['criança'].append(nome)
        elif idade <= 17:
            por_faixa['adolescente'].append(nome)
        elif idade <= 59:
            por_faixa['adulto'].append(nome)
        else:
            por_faixa['idoso'].append(nome)
    return por_faixa
