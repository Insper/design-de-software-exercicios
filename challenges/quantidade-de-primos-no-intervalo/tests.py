from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        testes = [(2, (2, 3)), (21, (10, 100)), (8, (450, 500))]
        for esperado, entrada in testes:
            self.assertEqual(esperado, self.function(*entrada), 'Não funcionou para o intervalo [{0}, {1}]'.format(*entrada))
