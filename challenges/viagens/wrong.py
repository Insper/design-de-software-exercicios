
def promocao_viagens(destinos):
    for destino in destinos:
        preco = destinos[destino]
        desconto = preco[0]*0.1
        passagem= preco[1]*(1-desconto)
        destinos[destino]=10    
         
    return destinos

