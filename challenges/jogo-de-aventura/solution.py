def calcula_dano(personagem):
    dano = personagem['força']
    for equip in personagem['equipamentos']:
        dano += equip['força']
    return dano

if __name__ == "__main__":
    exemplo1 = {
        'nome': 'Herói',
        'força': 4,
        'vida': 25,
        'equipamentos': [
            {
                'nome': 'Martelo Mortal',
                'força': 15,
            },
            {
                'nome': 'Luva Leve',
                'força': 2,
            },
        ],
    }

    exemplo2 = {
        'nome': 'Outro Herói',
        'força': 18,
        'vida': 42,
        'equipamentos': [],
    }

    assert calcula_dano(exemplo1) == 21
    assert calcula_dano(exemplo2) == 18
    print('Tudo OK')
