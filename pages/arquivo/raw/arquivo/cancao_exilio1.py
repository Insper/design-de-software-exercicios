# Lendo tudo de uma vez
with open('cancao_do_exilio.txt', 'r') as arquivo:
    conteudo_completo = arquivo.read()
print(conteudo_completo)
