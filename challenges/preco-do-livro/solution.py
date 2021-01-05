def verifica_preco(titulo, livros, cores):
    if titulo not in livros:
        return -1
    return cores[livros[titulo]]
