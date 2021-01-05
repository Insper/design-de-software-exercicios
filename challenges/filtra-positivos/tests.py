from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = [[-1, -2, -3],[-1, -2, -3, 0, 1, 2],[0, -1, 1, -2, 2]]
        esperados = [[], [1, 2], [1, 2]]
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(entrada), 'Não funcionou para a entrada {0}'.format(entrada))
