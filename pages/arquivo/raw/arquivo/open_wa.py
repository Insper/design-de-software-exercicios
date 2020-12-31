# Cria o arquivo para escrita (limpa o antigo se já existir)
with open('arquivo_texto.txt', 'w') as arquivo:
    # Escrevendo um texto
    arquivo.write("algum dado\n")

# Abre/Cria o arquivo para escrita SEM apagar o que tinha antes.
with open('arquivo_texto.txt', 'a') as arquivo:
    # Escrevendo um texto
    arquivo.write("novo dado\n")
