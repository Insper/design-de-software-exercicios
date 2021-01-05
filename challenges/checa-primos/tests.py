from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
        esperados = [{-1: False, 0: False, 1: False, 2: True, 3: True, 4: False, 5: True, 6: False, 7: True, 8: False, 9: False}]
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(entrada), 'Não funcionou para a string {0}'.format(entrada))
