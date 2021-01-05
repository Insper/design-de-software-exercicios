def medias_por_inicial(alunos):
    medias = {}
    for aluno, nota in alunos.items():
        if aluno[0] in medias.keys():
            medias[aluno[0]] += nota
        else:
            medias[aluno[0]] = nota
    for chave, valor in medias.items():
        rep = [ini[0] for ini in alunos.keys()]
        medias[chave] = valor / rep.count(chave)
    return medias