def pos_arroba(email):
    cont = 0
    i = 0
    while email[i] != '@':
        cont += 1
        i += 1
    return cont