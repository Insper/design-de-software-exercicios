"""
Demonstração de uso de variáveis com diversos tipos de dados em Python.

@author: Profs. de Design de Software.
"""

# Variáveis podem armazenar texto (strings).
disciplina = 'Design de Software'
print(disciplina)

# Variáveis podem armazenar inteiros.
num_alunos = 120

# Variáveis podem armazenar os valores especiais True e False
# São usados em expressões lógicas, ou também chamadas
# expressões booleanas.
a = True
b = False
c = a or b  # Operação booleana 'OU'.

# Variáveis podem armazenar números reais. Em computação,
# estes números são chamados de números em ponto flutuante.
base = 0.5
altura = 4.2e1  # 4.2 x 10**1 => 42.0
area = base * altura / 2.0

# Variáveis armazenam muitos outros tipos que veremos depois.
ponto = (3.2, 5.7)  # Tupla.
teste = [5.2, 'laranja', False, 42]  # Lista.
notas = {'dessoft': 10.0, 'gde': 10.0,
         'modsim': 10.0}  # dicionário.
