substituicoes = {
    'z': 's',
    'e': 'a',
    'b': 'r',
    'r': 'b',
    'a': 'e',
    's': 'z'
}

# with open('criptografado.txt', 'r') as arquivo:
#     for criptografado in arquivo.readlines():
#         descriptografado = ''
#         for c in criptografado:
#             if c in substituicoes:
#                 novo_c = substituicoes[c]
#             else:
#                 novo_c = c
#             descriptografado += novo_c
#         print(descriptografado)

with open('criptografado.txt', 'r') as arquivo:
    criptografado = arquivo.read()
descriptografado = ''
for c in criptografado:
    if c in substituicoes:
        novo_c = substituicoes[c]
    else:
        novo_c = c
    descriptografado += novo_c
print(descriptografado)

