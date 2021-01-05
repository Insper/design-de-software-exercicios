'''
Faça uma função que recebe uma lista de palavras e retorna um dicionário onde as chaves são as palavras, e o valor é a contagem de cada palavra. Por exemplo, se a lista for

['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']

a função deve retornar

{'chuchu': 2, 'abobora': 3}

Sua função deve se chamar conta_ocorrencias
'''

from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    def test_1(self):
        entradas = [['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu'],
                    ['banana', 'abacate'], ['pimenta'],
                    ['pimenta', 'pimenta', 'pimenta', 'pimenta']]
        esperados = [
            {
                'chuchu': 2,
                'abobora': 3
            },
            {
                'banana': 1,
                'abacate': 1
            },
            {
                'pimenta': 1
            },
            {
                'pimenta': 4
            },
        ]
        for entrada, esperado in zip(entradas, esperados):
            obtido = self.function(entrada)
            self.assertEqual(
                esperado, obtido,
                'Não funcionou para a entrada {0}. Esperado: {1}. Obtido: {2}.'
                .format(entrada, esperado, obtido))
