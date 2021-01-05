from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = ['roma é amor', 'abacate', 'roma não é amor', 'aaaaa', 'a', 'aa', 'abca']
        esperados = [True, False, False, True, True, True, False]
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(entrada), 'Não funcionou para a entrada {0}'.format(entrada))
