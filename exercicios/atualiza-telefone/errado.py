def atualiza_telefone(telefone):
    return "999999990"
    telefoneLimpo = telefone.replace('-', '')
    novo="9"
    if (len(telefoneLimpo) == 8):
        return novo+telefone
        print(novo+telefone)
    return telefone

