def pedra_papel_tesoura(um, dois):
    um=um.lower()
    dois=dois.lower()
    possbilidades=["pedra","papel","tesoura"]
    if um == dois and um in possbilidades:
        return("empate")
    elif um == 'pedra':
        if dois == 'tesoura':
            return("dois")
        else:
            return("um")
    elif um == 'tesoura':
        if dois == 'papel':
            return("um")
        else:
            return("dois")
    elif um == 'papel':
        if dois == 'pedra':
            return("um")
        else:
            return("dois")
    else:
        return("Escolha pedra, papel ou tesoura para jogar")








