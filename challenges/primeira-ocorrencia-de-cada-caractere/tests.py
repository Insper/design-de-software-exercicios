from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = ['abracadabra']
        esperados = [{'a': 0, 'b': 1, 'r': 2, 'c': 4, 'd': 6}]
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(entrada), 'Não funcionou para a entrada {0}'.format(entrada))
