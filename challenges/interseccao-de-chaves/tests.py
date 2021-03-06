from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = [[{'A': 1, 'B': 2, 'C': 3, 'D': 4}, {'A': 5, 'B': 6, 'C': 7, 'E': 8}]]
        esperados = [['A', 'B', 'C']]
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(*entrada), 'Não funcionou para a entrada {0}'.format(entrada))
