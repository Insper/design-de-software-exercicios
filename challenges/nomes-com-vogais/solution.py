def nomes_com_vogais(nomes):
    i = 0
    vogais = 0
    while i<len(nomes):
        if nomes[i][0]=="A" or nomes[i][0]=="E" or nomes[i][0]=="I" or nomes[i][0]=="O" or nomes[i][0]=="U":
            vogais += 1
        i += 1
    return [vogais, len(nomes)-vogais]

# nomes = ["André", "Carlos", "João", "Otavio", "Thiago"]
# print(nomes_com_vogais(nomes))

# nomes = ["BRENO", "CARLOS", "ERIC", "EDUARDO", "ALICE", "Sarah", "STEPHAN", "LORENA", "LETÍCIA", "ADNEY", "JERÔNIMO", "NÍVEA", "GABRIEL", "RODRIGO", "LUCCA", "YKARO", "CARLOS", "Gabriel", "RODRIGO", "EDUARDO", "PAULO", "RENATO", "ANDRÉ", "LUCAS", "LUÍSA", "JOAO", "RICARDO", "KEIYA", "LISTER", "GABRIEL", "PEDRO", "FELIPE", "MATHEUS", "FLAVIO", "CELINA", "GABRIEL"]
# print(nomes_com_vogais(nomes))
