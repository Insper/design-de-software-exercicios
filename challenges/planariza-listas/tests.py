from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = [[[1, 2, 3], [4, 5, 6], [7, 8], [9], [10]], [[1, 2, 3], [], [], [4, 5, 6], [7, 8], [9], [10]]]
        esperados = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(entrada), 'Não funcionou para a entrada {0}'.format(entrada))
