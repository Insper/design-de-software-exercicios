import json

with open('alunos.json', 'r') as arquivo_json:
    texto = arquivo_json.read()

print(texto)
# Para verificar que é realmente um texto (string),
# vamos usar um fatiamento:
print(texto[:15])

# Criando um dicionário a partir das informações no texto
dicionario = json.loads(texto)

# Para verificar que é um dicionário,
# vamos imprimir o valor armazenado na chave "Alunos"
print(dicionario['Alunos'])

# Adicionando um novo aluno no dicionário
novo_aluno = {'nome': 'Alice', 'notas': [10, 7, 8]}
dicionario['Alunos'].append(novo_aluno)

# Transformando de volta para JSON (texto)
novo_json = json.dumps(dicionario)

# Salvando o arquivo
with open('alunos.json', 'w') as arquivo_json:
    arquivo_json.write(novo_json)

# Abra o arquivo alunos.json e verifique seu conteúdo.
