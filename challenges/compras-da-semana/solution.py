def compras_da_semana(receitas, pratos):
    ingredientes = {}
    for prato in pratos:
        for ingrediente, quantidade in receitas[prato].items():
            ingredientes[ingrediente] = ingredientes.get(ingrediente, 0) + quantidade
    return ingredientes
