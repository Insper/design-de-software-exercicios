def lista_celulares(telefones):
    celulares = []
    for t in telefones:
        if len(t) == 14 and t[5] == '9':
            celulares.append(t[5:])
        elif len(t) == 11 and t[2] == '9':
            celulares.append(t[2:])
        elif len(t) == 9 and t[0] == '9':
            celulares.append(t)
    return celulares


# Outra maneira
# def lista_celulares(telefones):
#     celulares = []
#     for t in telefones:
#         limpo = t[-9:]
#         if len(t) in [9, 11, 14] and limpo[0] == '9':
#             celulares.append(limpo)
#     return celulares


if __name__=='__main__':
    celulares = lista_celulares([
        '+5511912345678',
        '1155556666',
        '77778888',
        '+551133334444',
        '918273645',
        '11987654321',
    ])
    for cel in ['912345678', '918273645', '987654321']:
        assert cel in celulares
    assert len(celulares) == 3
    print('Tudo OK')
