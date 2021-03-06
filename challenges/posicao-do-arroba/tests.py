from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = ['usuario@insper.edu.br']
        esperados = [7]
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(entrada), 'Não funcionou para a entrada {0}'.format(entrada))
