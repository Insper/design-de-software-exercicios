from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = ['casa', 'abacate', 'MAIÚSCULAS', 'texto com espaços']
        esperados = ['Casa', 'Abacate', 'MAIÚSCULAS', 'Texto com espaços']
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(entrada), 'Não funcionou para a entrada {0}'.format(entrada))
