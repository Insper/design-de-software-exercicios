lista = [["Fulano", "99999-1111"], ["Sicrano", "99999-2222"], ["Beltrano", "99999-3333"]]

nome_selecionado = input("Digite um nome: ")

for nome_e_telefone in lista:
    nome = nome_e_telefone[0]
    if nome == nome_selecionado:
        telefone = nome_e_telefone[1]
        print("Telefone de {0} é: {1}".format(nome, telefone))
