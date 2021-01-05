def login_disponivel(nome, existentes):
    if nome not in existentes:
        return nome
    i = 1
    while '{0}{1}'.format(nome, i) in existentes:
        i += 1
    return '{0}{1}'.format(nome, i)
