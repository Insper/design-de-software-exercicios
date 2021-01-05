def mais_medalhas(lista):
    nacionalidades = {}
    for esportista in lista:
        if esportista["nacionalidade"] in nacionalidades:
            nacionalidades[esportista["nacionalidade"]] += esportista["ouro"]
        else:
            nacionalidades[esportista["nacionalidade"]] = esportista["ouro"]

    vitoriosa = ""
    maior = 0
    for nacionalidade, medalhas in nacionalidades.items():
        if medalhas > maior:
            vitoriosa = nacionalidade
            maior = medalhas

    return vitoriosa

# EXEMPLO
# esportistas = []
# esportistas.append({"nome":"Fulano", "nacionalidade":"brasileiro", "ouro":2, "prata":0, "bronze":0})
# esportistas.append({"nome":"Beltrano", "nacionalidade":"paraguaio", "ouro":1, "prata":1, "bronze":1})
# esportistas.append({"nome":"Ciclano", "nacionalidade":"brasileiro", "ouro":0, "prata":0, "bronze":1})
# print(mais_medalhas(esportistas))
