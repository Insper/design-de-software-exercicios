from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = [[['A', 'B', 'C'], [1, 2, 3]]]
        esperados = [{'A': 1, 'B': 2, 'C': 3}]
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(*entrada), 'Não funcionou para a entrada {0}'.format(entrada))
