# Abre um arquivo para a leitura.
with open('arquivo_texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
# Quando sai do bloco do 'with', fecha o arquivo automaticamente.

# Imprime o conteúdo
print(conteudo)
