def remove_vogais(string):
    lista_aux = []
    for i in string:
       	lista_aux.append(i)
    string_aux = ''
    for i in lista_aux:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
            string_aux = string_aux+i
    return string_aux