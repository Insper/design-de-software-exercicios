def nome_usuario(email):
    i=0
    while i<len(email):
        if email[i] == '@':
            return email [0:i] 
        i += 1
    