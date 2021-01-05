with open('texto.txt', 'r') as arquivo:
    texto = arquivo.read()
    palavras = texto.split()
    print('O texto tem {0} palavras'.format(len(palavras)))
