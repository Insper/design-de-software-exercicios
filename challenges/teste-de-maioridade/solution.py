def verifica_idade(idade):
    if idade >= 18:
        if idade < 21:
            return 'Liberado BRASIL'
        else:
            return 'Liberado EUA e BRASIL'
    else:
        return 'Não está liberado'