def pedra_papel_tesoura(um, dois):
    um=um.lower()
    dois=dois.lower()
    possbilidades=["pedra","papel","tesoura"]
    if um == dois and um in possbilidades:
        return("empate")
    elif um == 'pedra':
        if dois == 'tesoura':
            return("um")
        else:
            return("um")
    elif um == 'tesoura':
        if dois == 'papel':
            return("dois")
        else:
            return("dois")
    elif um == 'papel':
        if dois == 'pedra':
            return("dois")
        else:
            return("um")
    else:
        return("Escolha pedra, papel ou tesoura para jogar")








