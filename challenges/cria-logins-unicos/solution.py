def login_disponivel(nome, existentes):
    if nome not in existentes:
        return nome
    i = 1
    while '{0}{1}'.format(nome, i) in existentes:
        i += 1
    return '{0}{1}'.format(nome, i)


nomes = []
nome = input('Digite um nome: ')
while nome != 'fim':
    novo_nome = login_disponivel(nome, nomes)
    nomes.append(novo_nome)
    nome = input('Digite um nome: ')
for nome in nomes:
    print(nome)
