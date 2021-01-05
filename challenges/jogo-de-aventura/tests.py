from numbers import Number
from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 1

    def test_1(self):
        exemplos = [
            ({
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
            }, 21),
            ({
                'nome': 'Outro Herói',
                'força': 18,
                'vida': 42,
                'equipamentos': [],
            }, 18),
            ({
                'nome': 'Batman',
                'força': 2,
                'vida': 18,
                'dinheiro': 999999,
                'equipamentos': [
                    {
                        'nome': 'Bat-Lança-Chamas',
                        'força': 20,
                    },
                    {
                        'nome': 'Bat-Patins a Jato',
                        'força': 1,
                    },
                    {
                        'nome': 'Bat-Repelente de Tubarões',
                        'força': 10,
                    },
                ],
            }, 33),
        ]
        for entrada, esperado in exemplos:
            obtido = self.function(entrada)
            self.assertIsNotNone(obtido, msg='Sem resposta. Você não se esqueceu do return?')
            self.assertTrue(isinstance(obtido, Number), msg='O valor devolvido não é um número. Era esperado apenas um número representando o dano causado pelo personagem.')
            self.assertEqual(esperado, obtido, msg='Resposta diferente da esperada para o dicionário {0}. Obtido: {1}. Esperado: {2}'.format(entrada, obtido, esperado))

