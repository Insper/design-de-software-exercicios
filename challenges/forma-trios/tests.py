from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = [['A0'], ['A0', 'A1', 'A2'], ['A0', 'A1', 'A2', 'A3', 'A4'], ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6']]
        esperados = [[['A0']], [['A0', 'A1', 'A2']], [['A0', 'A1', 'A2'], ['A3', 'A4']], [['A0', 'A1', 'A2'], ['A3', 'A4', 'A5'], ['A6']]]
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(entrada), 'Não funcionou para a entrada {0}'.format(entrada))
