from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        self.program()
        try:
            resposta = float(self.mock_print.printed[-1])
        except ValueError:
            raise AssertionError('O último print deve conter somente a resposta: imprima somente o resultado, sem nenhum texto adicional.')
        self.assertEquals(2, int(resposta))
