from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2


    def test_1(self):
        entradas = ['', 'abacate']
        esperados = [[], ['a', 'b', 'c', 't', 'e']]
        for entrada, esperado in zip(entradas, esperados):
            recebido = self.function(entrada)
            self.assertEqual(len(esperado), len(recebido))
            for c in esperado:
                self.assertTrue(c in recebido, 'Não funcionou para a entrada {0}'.format(entrada))
