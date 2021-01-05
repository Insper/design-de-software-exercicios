from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 1

    def test_1(self):
        self.program()
        msg = 'Não chegou no resultado. Dica: o resultado esperado é 12. Verifique a saída do terminal.'
        self.assert_printed(12, msg=msg)
        self.assertEqual(1, self.mock_print.calls, msg='Deveria chamar a função print apenas uma vez.')
