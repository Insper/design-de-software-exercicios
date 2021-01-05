from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        # Teste do enunciado
        eng2port = {
            'pineapple': 'abacaxi',
            'plum': 'ameixa',
            'blackberry': 'amora',
            'apple': 'maçã',
            'cashew': 'caju',
            'cherry': 'cereja',
        }
        words = ['blackberry', 'cherry', 'plum', 'apple', 'pineapple']
        esperado = ['amora', 'cereja', 'ameixa', 'maçã', 'abacaxi']
        obtido = self.function(words, eng2port)

        self.assertTrue(obtido is not None,
                        msg='Será que você esqueceu do return?')
        msg = 'Não funcionou para o teste do enunciado. Obtido: {2}. Esperado: {3}.'.format(
            words, eng2port, obtido, esperado)
        self.assertTrue(isinstance(obtido, list),
                        msg=msg + ' O resultado obtido não é uma lista.')
        self.assertEqual(
            len(obtido),
            len(words),
            msg=msg +
            ' O resultado obtido tem uma quantidade de palavras diferente da lista de entrada.'
        )
        self.assertEqual(esperado, obtido, msg=msg)

        # Mais um teste
        eng2port = {
            'house': 'casa',
            'plant': 'planta',
            'mouse': 'rato',
            'desk': 'mesa',
        }
        words = ['house', 'mouse', 'mouse', 'plant']
        esperado = ['casa', 'rato', 'rato', 'planta']
        obtido = self.function(words, eng2port)

        self.assertTrue(obtido is not None,
                        msg='Será que você esqueceu do return?')
        msg = 'Não funcionou para o teste com a lista {0} e o dicionário {1}. Obtido: {2}. Esperado: {3}.'.format(
            words, eng2port, obtido, esperado)
        self.assertTrue(isinstance(obtido, list),
                        msg=msg + ' O resultado obtido não é uma lista.')
        self.assertEqual(
            len(obtido),
            len(words),
            msg=msg +
            ' O resultado obtido tem uma quantidade de palavras diferente da lista de entrada.'
        )
        self.assertEqual(esperado, obtido, msg=msg)
