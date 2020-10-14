def atualiza_telefone(telefone):
    telefoneLimpo = telefone.replace('-', '')
    novo="9"
    if (len(telefoneLimpo) == 8):
        return novo+telefone
        print(novo+telefone)
    return telefone

