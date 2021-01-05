from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = [{'Ana': 19, 'Bruno': 18, 'João': 19}]
        esperados = [{18: ['Bruno'], 19: ['Ana', 'João']}]
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(entrada), 'Não funcionou para a entrada {0}'.format(entrada))
