from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 2

    def test_1(self):
        self.program()
        self.assertTrue('871' in self.mock_print.printed[-1], 'Resposta errada')
