from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        entradas = [[{'A': 1, 'B': 2, 'C': 3, 'D': 4}, {'E': 3, 'F': 4, 'G': 5, 'H': 6}]]
        esperados = [[3, 4]]
        for entrada, esperado in zip(entradas, esperados):
            self.assertEqual(esperado, self.function(*entrada), 'Não funcionou para a entrada {0}'.format(entrada))
